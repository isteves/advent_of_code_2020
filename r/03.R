library(tidyverse)

input <- read_delim("raw/03.txt", delim = ",", col_names = FALSE)


# Part One ----------------------------------------------------------------

tob_positions <- input %>% 
  rename(tree_map = X1) %>% 
  mutate(x_pos = 1 + row_number() * 3 - 3,
         map_len = str_length(tree_map)) %>% 
  mutate(x_pos_mod = x_pos %% map_len,
         x_pos_mod = ifelse(x_pos_mod == 0, map_len, x_pos_mod)) %>% 
  mutate(pos = substr(tree_map, x_pos_mod, x_pos_mod))

sum(tob_positions$pos == "#")


# Part Two ----------------------------------------------------------------

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.

tree_hits <- function(n_right) {
  tob_positions <- input %>% 
    rename(tree_map = X1) %>% 
    mutate(x_pos = 1 + row_number() * n_right - n_right,
           map_len = str_length(tree_map)) %>% 
    mutate(x_pos_mod = x_pos %% map_len,
           x_pos_mod = ifelse(x_pos_mod == 0, map_len, x_pos_mod)) %>% 
    mutate(pos = substr(tree_map, x_pos_mod, x_pos_mod))
  
  sum(tob_positions$pos == "#")
}

slopes <- c(1, 3, 5, 7)

hits <- map_dbl(slopes, tree_hits)

# Right 1, down 2.

n_right <- 1

tob_positions_odds <- input %>% 
  rename(tree_map = X1) %>% 
  filter(row_number() %% 2 == 1) %>% 
  mutate(x_pos = 1 + row_number() * n_right - n_right,
         map_len = str_length(tree_map)) %>% 
  mutate(x_pos_mod = x_pos %% map_len,
         x_pos_mod = ifelse(x_pos_mod == 0, map_len, x_pos_mod)) %>% 
  mutate(pos = substr(tree_map, x_pos_mod, x_pos_mod))

hits_odd <- sum(tob_positions_odds$pos == "#")

reduce(c(hits, hits_odd), `*`)
