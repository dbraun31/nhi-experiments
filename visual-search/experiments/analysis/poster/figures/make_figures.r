library(tidyverse)
library(ggridges)

height = 5
width = 8

### one plot per exp
for (i in 1:3) {
  d <- read.csv(paste0('data/exp', i, '_group_clicking.csv'))
  
  p <- d %>% 
    gather(metric, value, RT:Accuracy) %>% 
    ggplot(aes(x = value, y = click_order, group = click_order)) + 
    geom_density_ridges(fill = 'steel blue', alpha = .8) + 
    facet_wrap(~metric, scales = 'free') +
    labs(
      x = '',
      y = 'Click Order'
    ) + 
    scale_y_continuous(breaks = 1:3) + 
    theme_bw() + 
    theme(strip.background = element_rect(color = 'black', fill = 'white'),
          panel.grid = element_blank(),
          axis.ticks = element_blank(),
          text = element_text(size = 16))
  
  ggsave(p, file = paste0('exp', i, '_clicking_plot.png'), height = height, width = width, dpi = 300, units = 'in')
  
}

