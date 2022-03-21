library(tidyverse)

d <- read.csv('exp3_line_data.csv')

d$line_orientation <- ifelse(d$top_x == d$bottom_x, 'vertical', ifelse(d$top_x > d$bottom_x, 'forward_slash', ifelse(d$top_x < d$bottom_x, 'back_slash', 'PROBLEM')))

if ('PROBLEM' %in% d$line_orientation) {
	print('PROBLEM, not writing data')

} else {
	write.csv(d, 'exp3_line_data.csv', row.names = FALSE)
}