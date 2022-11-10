compute_quadrants <- function(d, line_data) {
	## returns data with 'quadrant' column
	top_left <- c(min(line_data$top_x), max(line_data$top_y))
	top_right <- c(max(line_data$top_x), max(line_data$top_y))
	bottom_left <- c(min(line_data$bottom_x), min(line_data$bottom_y))
	bottom_right <- c(max(line_data$bottom_x), min(line_data$bottom_y))

	center <- c(mean(c(top_left[1], top_right[1])), mean(c(top_left[2], bottom_left[2])))

	d <- d %>% 
  mutate(line_center_x = (top_x + bottom_x) / 2, line_center_y = (top_y + bottom_y) / 2) %>% 
  mutate(quadrant = ifelse(line_center_x > center[1] & line_center_y > center[2], 'I', ifelse(line_center_x < center[1] & line_center_y > center[2], 'II',
                    ifelse(line_center_x < center[1] & line_center_y < center[2], 'III', ifelse(line_center_x > center[1] & line_center_y < center[2], 'IV', '')))))

  d <- d %>% 
	  mutate(x_dist = abs(line_center_x - center[1]), y_dist = abs(line_center_y - center[2])) %>% 
	  mutate(is_on_axis = ifelse(x_dist < 0.1, 'y_axis', ifelse(y_dist < 0.1, 'x_axis', ''))) %>% 
	  mutate(quadrant = ifelse(is_on_axis == '', quadrant, is_on_axis)) 

  return(d)

}