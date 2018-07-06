import media
import fresh_tomatoes

toyStory = media.Movie(
    "toyStory", "a story about a boy and his toys that comes to like",
    "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
    "https://youtu.be/KYz2wyBy3kc")
print(toyStory.storyline)

pickOfDestiny = media.Movie(
    "pickOfDestiny", "In a quest to become the best rock band ever!",
    "https://en.wikipedia.org/wiki/Tenacious_D_in_The_Pick_of_Destiny#/media/File:Tenacious_d_in_the_pick_of_destiny_ver3.jpg",
    "https://youtu.be/a9GT9YgDfKU")
# print(pickOfDestiny.storyline)
# pickOfDestiny.showTrailer()

avatar = media.Movie(
    "Avatar", "A marine on an alien planet",
    "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
    "https://youtu.be/5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.showTrailer()

schoolOfRock = media.Movie(
    "School of rock", "having fun at school",
    "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
    "https://youtu.be/ggdploL_tUo")

hungerGames = media.Movie(
    "Hunger Games", "A really real reality show",
    "https://en.wikipedia.org/wiki/The_Hunger_Games#/media/File:The_Hunger_Games_cover.jpg",
    "https://youtu.be/mfmrPu43DF8")

Nymphomaniac = media.Movie(
    "Nymphomaniac", "Lars Von Trier",
    "https://en.wikipedia.org/wiki/Nymphomaniac_(film)#/media/File:Nymphomaniac_poster.jpg",
    "https://youtu.be/VVIa7tvgKHg")

reeferMadness = media.Movie(
    "Reefer Madness", " Reefer Madness: The Movie Musical",
    "https://en.wikipedia.org/wiki/Reefer_Madness_(2005_film)#/media/File:Reefer_Madness_(2005_film)_poster.jpg",
    "https://youtu.be/_X82zLM0oUY")

# playground

movies = [
    toyStory, schoolOfRock, hungerGames, Nymphomaniac, reeferMadness,
    pickOfDestiny, avatar
]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__module__)
# print(media.Movie.__name__)
# media.Movie.__name__ = "test"
# print(media.Movie.__name__)
