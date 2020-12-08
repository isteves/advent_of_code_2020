library(tidyverse)

# Part One ------------------------------------------------------------------

input <- read_delim("raw/02.txt", delim = " ", col_names = FALSE)

input_clean <- input %>% 
  separate(X1, c("min_n", "max_n"), sep = "-") %>% 
  rename(letter = X2, pwd = X3) %>% 
  mutate(letter = str_remove(letter, ":")) 

all_passwords <- input_clean %>% 
  mutate(letter_n = str_count(pwd, letter)) %>% 
  rowwise() %>% 
  mutate(is_valid = between(letter_n, min_n, max_n))

sum(all_passwords$is_valid)


# Part Two -----------------------------------------------------------------

all_passwords_rule2 <- input_clean %>% 
  mutate(pos1 = substr(pwd, min_n, min_n),
         pos2 = substr(pwd, max_n, max_n)) %>% 
  mutate(match_n = (letter == pos1) + (letter == pos2))

sum(all_passwords_rule2$match_n == 1)
