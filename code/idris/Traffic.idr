-- concept of module
-- concept of total function

module Traffic

data Traffic = 
  red |
  green |
  amber

nextLight: Traffic -> Traffic
nextLight red = green
nextLight green = amber
nextLight amber = red

