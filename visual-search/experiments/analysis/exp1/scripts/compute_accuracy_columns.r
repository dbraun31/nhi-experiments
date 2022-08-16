compute_trial <- function(data, thinnest_lines) {
  ## function takes in data from one participant and one trial at a time
  participant <- data$participant[1]
  trial <- data$trial_count[1]
  ## defaults to treat this var as a factor, and that messes everything up
  data$line_id <- as.character(data$line_id)
  
  ## vector of ids of thinnest lines (length 3) on a given trial for a given participant
  thinnest_lines_set <- thinnest_lines[thinnest_lines$participant == participant & thinnest_lines$trial_count == trial,]$line_id
  
  ## determine the final three lines they selected
  ## some extra logic to assign NA to any lines that were selected and later released
  selected_lines <- c(NA, NA, NA)
  indices <- c(NA, NA, NA)
  for (row in 1:(nrow(data))) {
    if (data[row,]$selected_or_released == 'selected') {
      ## get the index of the first empty slot in selected lines
      slot <- which(is.na(selected_lines))[1]
      selected_lines[slot]<- data[row,]$line_id
      indices[slot] <- row
    } else if (data[row,]$selected_or_released == 'released'){
      slot <- which(!(is.na(selected_lines)) & selected_lines == data[row,]$line_id)
      selected_lines[slot] <- NA
      indices[slot] <- NA
    }
  }
  
  
  selected_lines_accuracy_column <- rep(NA, nrow(data))
  accuracy_code <- ifelse(selected_lines %in% thinnest_lines_set, 'hit', 'false_alarm')
  ## extra code to record misses in the thinnest lines data
  misses_code <- ifelse(thinnest_lines_set %in% selected_lines, 'hit', 'miss')
  selected_lines_accuracy_column[indices] <- accuracy_code

  return(list(selected_lines_accuracy_column, misses_code))

}


compute_accuracy_columns <- function(d, thinnest_lines) {
  out  <- vector()
  misses_out <- c()
  
  for (participant in sapply(unique(d$participant), as.integer)) {
    ## during preprocessing i eliminated trials based on certain criteria
    for (trial in sapply(unique(d[d$participant == participant,]$trial_count), as.integer)) {
      result <- compute_trial(d[d$participant == participant & d$trial_count == trial,], thinnest_lines)
      out <- c(out, result[[1]])
      misses_out <- c(misses_out, result[[2]])
    }
  }
  
  thinnest_lines$accuracy_type <- misses_out
  d$accuracy_type <- out
  
  return(list(d, thinnest_lines))

}