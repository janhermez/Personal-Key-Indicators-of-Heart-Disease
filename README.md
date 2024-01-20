# Personal Key Indicators of Heart Disease

https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease

Baza zawierająca dane o chorobach serca i różnych powiązanych z tym czynnikach ryzyka.


## Configuration 
Use R

## Initial setup
setup only once:

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
./scripts/run-app.sh --profile all up -d
```

To run only application dependencies (i.e. databases) run:

```shell
./scripts/run-app.sh --profile deps up -d
```

## Secrets

 * Commit and push the change to a new branch.

Useful commands:
* `git secret 

## Links
- https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease

### Local (http)

Available on github and Rmd file.

#### Apps

- app1: http://localhost:8081/
- app2: http://localhost:8090/
- app3: http://localhost:8080/

#### Admin

## License
The GNU General Public License v3.0

