library(tidyverse)
library(gt)

system("rm game-text-png/*.png")

# set size of image output from values in game.py
X = 1280
Y = 720

# read text in as vector
game_text_raw <- 
    read_delim("things-to-fiddle-with/game_text_raw.txt", 
        delim = "XXX", col_types = "c") |> pull("game_text")

head(game_text_raw)

# read text key as dataframe
game_meta_raw <- read_csv("things-to-fiddle-with/game_text_key.csv")
head(game_meta_raw)

# vectorise over meta table
game_meta <- game_meta_raw |>
    mutate(
        file_path = str_c(
            "game-text-png/",
            "img-",
            game_text_line,
            "-",
            game_event,
            ".png"
        )
    )


# cleaning
# trim white space from end?

library(magick)

img <- image_read("whiteboard_frame.png")

img_dim <- list(
    width = image_info(img) |> pull(width),
    height = image_info(img) |> pull(height)
)

this_wb <- image_draw(img) |>
    image_annotate(
        font = "courier",
        str_wrap(game_text_raw[1], 50),
        color = "black",
        loc = sprintf("+%f+%f", 
            img_dim$width * 0.1, 
            img_dim$height * 0.2),
        size = 20)
        
image_write(this_wb, "wb_test.png")

make_game_text_png <- function(this_text, png_path){
this_wb <- image_draw(img) |>
    image_annotate(
        font = "courier",
        str_wrap(this_text, 50),
        color = "black",
        loc = sprintf("+%f+%f", 
            img_dim$width * 0.1, 
            img_dim$height * 0.2),
        size = 20)

image_write(this_wb, png_path)
dev.off()
}

map2(game_text_raw, game_meta$file_path, make_game_text_png)

write_csv(game_meta, "game-data/game-text-meta.csv")

# output image meta table
# - image path
