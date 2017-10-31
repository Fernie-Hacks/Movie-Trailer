#Import the Movie class and fresh_tomatoes module provided
import media
import fresh_tomatoes

#Create multiple Movie instances.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
donnie_darko = media.Movie("Donnie Darko",
                           "Time Traveling to save the world",
                           "https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg",
                           "https://www.youtube.com/watch?v=ZZyBaFYFySk")
pulp_fiction = media.Movie("Pulp Fiction",
                           "American black comedy neo-noir crime film",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
inglourious_basterds = media.Movie("Inglourious Basterds",
                                   "A fictional alternate history story of two plots to assassinate Nazi Germany's political leadership.",
                                   "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                                   "https://www.youtube.com/watch?v=6AtLlVNsuAc")
source_code = media.Movie("Source Code",
                          "A captain who is sent into a computed reality to find a bomber.",
                          "https://upload.wikimedia.org/wikipedia/en/e/e5/Source_Code_Poster.jpg",
                          "https://www.youtube.com/watch?v=NkTrG-gpIzE")

#Creates an array of Movie instances
movies = [toy_story, avatar, donnie_darko, pulp_fiction, inglourious_basterds, source_code]
#Call the fresh_tomatoes open_movie_page() function which takes the list
fresh_tomatoes.open_movies_page(movies)
