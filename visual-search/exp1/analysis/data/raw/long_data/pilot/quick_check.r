library(tidyverse)

d <- read.csv('pilot_data.csv')

d$participant <- ifelse(is.na(d$participant), 99, d$participant)

d %>% 
  filter(participant != 0) %>% 
  group_by(participant) %>% 
  summarize(across(everything(), last)) %>% 
  select(participant,overall_time)


d %>% 
  filter(pressed_object == 'submit', participant != 0) %>% 
  group_by(participant) %>% 
  summarize(count = n())
