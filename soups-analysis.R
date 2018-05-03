library(tidyverse)

soups <- read_csv('soups-tidy.csv')


soups %>%
  distinct(timestamp, location_name, soup) %>%
  group_by(location_name, soup) %>%
  summarize(count=n()) %>%
  ggplot(
    aes(x=reorder(soup, -count),
        y=count)) +
  geom_bar(stat='identity') +
  facet_wrap(~location_name) +
  coord_flip()
