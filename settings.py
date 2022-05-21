TRIVIA_CATEGORIES = {
    9: "General Knowledge",
    10: "Books",
    11: "Film",
    12: "Music",
    13: "Musicals & Theatres",
    14: "Television",
    15: "Video Games",
    16: "Board Games",
    17: "Science & Nature",
    18: "Computers",
    19: "Mathematics",
    20: "Mythology",
    21: "Sports",
    22: "Geography",
    23: "History",
    24: "Politics",
    25: "Art",
    26: "Celebrities",
    27: "Animals",
    28: "Vehicles",
    29: "Comics",
    30: "Gadgets",
    31: "Japanese Anime & Manga",
    32: "Cartoon & Animations",
}
DIFFICULTIES = {0: "easy", 1: "medium", 2: "hard"}
try:
    with open("settings.txt", mode="r") as file:
        settings = file.read()
        settings = [int(x) for x in settings.split(",")]
        QUESTIONS = settings[0]
        DIFFICULTY = settings[1]
        CATEGORY = settings[2]
except FileNotFoundError:
    QUESTIONS = 10
    DIFFICULTY = 0
    CATEGORY = 9
    with open("settings.txt", mode="w") as file:
        file.write(f"{QUESTIONS},{DIFFICULTY},{CATEGORY}")


def save_settings(_questions, _difficulty, _category):
    with open("settings.txt", mode="w") as out_file:
        out_file.write(f"{_questions},{_difficulty},{_category}")
