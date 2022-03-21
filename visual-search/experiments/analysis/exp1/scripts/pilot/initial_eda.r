library(tidyverse)
library(data.table)

d <- read.csv('../../data/raw/long_data/pilot/pilot_data.csv')
head(d)

d$participant <- ifelse(is.na(d$participant), 99, d$participant)

## accuracy over time
d %>% 
  filter(trial_count != 0, pressed_object == 'submit') %>% 
  group_by(trial_count) %>% 
  summarize(acc = mean(accuracy), sd = sd(accuracy)) %>% 
  ggplot(aes(x = trial_count, y = acc)) +
  geom_ribbon(aes(ymin = acc - sd, ymax = acc + sd), alpha = .2) +
  geom_line() + 
  #ylim(0,1) +
  labs(
    x = 'Trial',
    y = 'Accuracy'
  ) + 
  theme_bw()

ggsave('acc_time.png', height = 1080 / 300, width = 1920 / 300, units = 'in')

## space bar rt over time
d %>% 
  filter(trial_count != 0, pressed_object == 'submit', participant != 0) %>% 
  #group_by(trial_count) %>% 
  #summarize(rt_sec = mean(prompt_rt_sec), sd = sd(prompt_rt_sec)) %>% 
  ggplot(aes(x = trial_count, y = prompt_rt_sec, group = participant)) +
  #geom_ribbon(aes(ymax = rt_sec + sd, ymin = rt_sec - sd), alpha = .2) +
  geom_line(aes(color = factor(participant))) + 
  labs(
    x = 'Trial',
    y = 'Space Bar RT (s)',
    color = 'Participant'
  ) + 
  theme_bw() + 
  theme(legend.position = 'bottom')

ggsave('space_bar_time.png', height = 1080 / 300, width = 1920 / 300, units = 'in')

## line rt over time
d %>% 
  mutate(line_rt = ifelse(lag(pressed_object) == 'submit', selection_rt_ms, selection_rt_ms - lag(selection_rt_ms)),
         participant = recode(participant, `91` = 'Subject 91', `92` = 'Subject 92', `93` = 'Subject 93', `99` = 'Subject 99')) %>% 
  filter(pressed_object != 'submit', participant != 0, trial_count != 0) %>% 
  group_by(participant, trial_count, selected_or_released) %>% 
  summarize(rt = mean(line_rt) / 1000, sd = sd(line_rt)) %>% 
  ggplot(aes(x = trial_count, y = rt)) + 
  #geom_ribbon(aes(ymin = rt - sd, ymax = rt + sd, fill = selected_or_released, group = selected_or_released), alpha = .2) + 
  geom_line(aes(color = selected_or_released)) + 
  facet_wrap(~participant) +
  labs(
    x = 'Trial',
    y = 'Line Selection RT (s)',
    color = ''
  ) + 
  theme_bw() +
  theme(legend.position = c(.8,.9),
        strip.background = element_rect(color = 'black', fill = 'white'),
        legend.key.size = unit(.2, 'cm'),
        legend.text = element_text(size = 8),
        legend.background = element_blank())

ggsave('line_time.png', height = 1080 / 300, width = 1920 / 300, units = 'in')

## selection button rt over time

d %>% 
  filter(pressed_object == 'submit', participant != 0, trial_count != 0) %>% 
  mutate(selection_rt_ms = selection_rt_ms / 1000) %>% 
  group_by(participant, trial_count) %>% 
  summarize(line_rt = mean(selection_rt_ms)) %>% 
  ggplot(aes(x = trial_count, y = line_rt, group = participant)) +
  geom_line(aes(color = factor(participant))) + 
  labs(
    x = 'Trial',
    y = 'Submit Button RT (s)',
    color = 'Participant'
  ) + 
  theme_bw() + 
  theme(legend.position = 'bottom')
  
ggsave('submit_time.png', height = 1080 / 300, width = 1920 / 300, units = 'in')














