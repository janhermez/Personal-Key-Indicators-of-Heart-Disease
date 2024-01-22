# Personal Key Indicators of Heart Disease

https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease

Baza zawierająca dane o chorobach serca i różnych powiązanych z tym czynnikach ryzyka.


## Configuration 
Use R

## Initial setup
setup only once:

alternatively:

install.packages("tidyverse")

install.packages("rstatix")

```shell
library(rstatix)
library(tidyverse)

heart_df <- read_csv("heart_2020_cleaned.csv")
```

## Configuration (data verification)

To create and update application configuration use following scripts:

```shell
heart_df %>% 
  select(where(is.character)) %>% 
  map(unique)

heart_df %>% 
  select(where(is.numeric)) %>% 
  names()

heart <- heart_df

heart %>% 
  select(where(is.character)) %>% 
  map(unique) 

pivot1 <- heart %>% 
  select(-HeartDisease) %>% 
  map_df(typeof) %>% 
  pivot_longer(everything()) 

pivot_number <- pivot1 %>% 
  count(value)

pivot1
pivot_number

heart %>% 
  select(where(is.numeric)) %>% 
  get_summary_stats()

heart %>% 
  select(where(is.character)) %>% 
  map(table)

heart %>% 
  filter(if_any(everything(), ~is.na(.)))
```
Baza nie zawiera żadnych braków danych.

## Running

To run the application use:

```shell
lol
```


## Useful commands:

 * Commit and push the change to a new branch.

* `git secret 

## Links
Kaggle:
- https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease

GitHub repository:
- https://github.com/kamilpytlak/data-science-projects/blob/main/heart-disease-prediction/2022/notebooks/data_processing.ipynb

### Local (http)

Available on github and Rmd, html, csv, md files.

#### Apps

possibly use:

AI

ChatGPT

#### Admin

## License
The GNU General Public License v3.0

