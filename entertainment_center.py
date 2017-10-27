import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
donnie_darko = media.Movie("Donnie Darko",
                           "Time Traveling to save the world",
                           "https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg",
                           "https://www.youtube.com/watch?v=ZZyBaFYFySk",)

movies = [toy_story, avatar, donnie_darko]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
