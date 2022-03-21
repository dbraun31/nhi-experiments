library(tidyverse)
library(plotly)

d <- read.csv('../data/compare_lines.csv')
head(d)

keep <- c('participant', 'line_orientation', 'SeqResponse.keys', 'SeqResponse.rt', 'ResponseSimul.keys', 'ResponseSimul.rt', 'left_width', 'right_width', 'first_line_label', 'second_line_label')

d <- d[,keep]

deidentify <- data.frame(participant = names(summary(factor(d$participant))), id = sample(c('a', 'b', 'c'), size = 3, replace = FALSE))

d <- d %>% 
  inner_join(deidentify, by = 'participant') %>% 
  select(-participant)

N <- d %>% 
  group_by(id) %>% 
  summarize(n()) %>% 
  nrow()

## tricky reshaping
colnames(d)[4:5] <- c('SimulResponse.keys', 'SimulResponse.rt')
d$row_id <- 1:(nrow(d))
d <- d %>% 
  gather(var, value, SeqResponse.keys, SeqResponse.rt, SimulResponse.keys, SimulResponse.rt) %>% 
  separate(var, c('block', 'response_type')) %>% 
  spread(response_type, value) %>% 
  filter(!is.na(rt))

## code accuracy
d$accuracy <- ifelse(d$left_width < d$right_width & d$keys == 'right', 1, 
                     ifelse(d$right_width < d$left_width & d$keys == 'left', 1,
                            ifelse(d$right_width == d$left_width & d$keys == 'down', 1, 0)))

## round widths
d$left_width <- round(d$left_width, 2)
d$right_width <- round(d$right_width, 2)

## keep widths in same order
d$small_width <- ifelse(d$left_width > d$right_width, d$right_width, d$left_width)
d$large_width <- ifelse(d$left_width > d$right_width, d$left_width, d$right_width)


## visualize

d %>% 
  unite('combinations', c('small_width', 'large_width'), sep = '-') %>% 
  group_by(id, combinations) %>% 
  summarize(accuracy = mean(accuracy)) %>% 
  group_by(combinations) %>% 
  summarize(accuracy = mean(accuracy)) %>% 
  separate(combinations, c('small_width', 'large_width'), sep = '-') %>% 
  ggplot(aes(x = small_width, y = large_width, fill = accuracy)) + 
  geom_tile() +
  labs(
    x = 'Line 1',
    y = 'Line 2',
    fill = 'Accuracy'
  ) + 
  theme_bw() 
  


p1 <- d %>% 
  unite('combinations', c('small_width', 'large_width'), sep = '-') %>% 
  group_by(id, combinations, block) %>% 
  summarize(accuracy = mean(accuracy)) %>% 
  group_by(combinations, block) %>% 
  summarize(accuracy = mean(accuracy)) %>% 
  separate(combinations, c('small_width', 'large_width'), sep = '-') %>% 
  mutate(text = paste0('Small width: ', small_width, '\nLarge Width: ', large_width, '\nAccuracy: ', round(accuracy,2))) %>% 
  ggplot(aes(x = small_width, y = large_width, fill = accuracy, text = text)) + 
  geom_tile() +
  facet_wrap(~block) +
  labs(
    x = 'Line 1',
    y = 'Line 2',
    fill = 'Accuracy'
  ) + 
  theme_bw() +
  theme(strip.background = element_rect(fill = NA, color = 'black'),
        text = element_text(size = 20),
        axis.text.x = element_text(angle = 90))



gp <- ggplotly(p1, tooltip = 'text')

htmlwidgets::saveWidget(as_widget(gp), 'index.html')


## accuracy and rt across blocks and orientations

d %>% 
  group_by(id, block, line_orientation) %>% 
  summarize(acc = mean(accuracy)) %>% 
  group_by(block, line_orientation) %>% 
  summarize(accuracy = mean(acc), se = sd(acc) / sqrt(N)) %>% 
  ggplot(aes(x = block, y = accuracy, group = line_orientation)) + 
  geom_bar(stat = 'identity', aes(fill = line_orientation), position = position_dodge(width = .9)) +
  geom_errorbar(aes(ymin = accuracy - se, ymax = accuracy + se), width = .5, position = position_dodge(width = .9)) +
  ylim(0,1) +
  theme_bw()














