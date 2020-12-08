library(tidyverse)

input <- read_delim("raw/01.txt", delim = ",", col_names = FALSE)

# Part I ------------------------------------------------------------------

input %>% 
  rename(col1 = X1) %>% 
  mutate(col2 = col1) %>% 
  expand(col1, col2) %>% 
  mutate(sum = col1 + col2,
         mult = col1 * col2) %>% 
  filter(sum == 2020)

# Part II -----------------------------------------------------------------

input %>% 
  rename(col1 = X1) %>% 
  mutate(col2 = col1, col3 = col1) %>% 
  expand(col1, col2, col3) %>% 
  mutate(sum = col1 + col2 + col3,
         mult = col1 * col2 * col3) %>% 
  filter(sum == 2020)
