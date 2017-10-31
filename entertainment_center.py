#Import the Movie class and fresh_tomatoes module provided
import media
import fresh_tomatoes

#Create multiple Movie instances.
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

#Creates an array of Movie instances
movies = [toy_story, avatar, donnie_darko]
#Call the fresh_tomatoes open_movie_page() function which takes the list
fresh_tomatoes.open_movies_page(movies)
