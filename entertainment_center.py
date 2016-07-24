import fresh_tomatoes

import media

lion_king = media.Movie("Lion King",
						"A young lion who triumphs despite tragedy",
						"http://vignette3.wikia.nocookie.net/disney/images/c/cb/The_Lion_King_Textless_poster_1.jpg/revision/latest?cb=20140810104158",
						"https://www.youtube.com/watch?v=f0fReuRs890")
finding_dory = media.Movie("Finding Dory",
					"A fish tries to find her long-lost parents",
					"https://i.ytimg.com/vi/hXI-sTDVU-Y/maxresdefault.jpg",
					"https://www.youtube.com/watch?v=JhvrQeY3doI&spfreload=10")
jumanji = media.Movie("Jumanji",
					"A board game that comes alive",
					"https://www.movieposter.com/posters/archive/main/68/MPW-34112",
					"https://www.youtube.com/watch?v=bFPN23BktYA")
the_devil_wears_prada = media.Movie("The Devil Wears Prada",
						"A woman lands a job as an assistant job in fashion",
						"http://www.impawards.com/2006/posters/devil_wears_prada.jpg",
						"https://www.youtube.com/watch?v=XTDSwAxlNhc")
fireproof = media.Movie("Fireproof",
						"A firefighter tries to save his marriage",
						"http://www.impawards.com/2008/posters/fireproof_xlg.jpg",
						"https://www.youtube.com/watch?v=tKJyKHlRzi0")
iron_man = media.Movie("Iron Man",
						"A billionaire plays superhero",
						"http://cdn.collider.com/wp-content/uploads/2015/04/iron-man-1-poster.jpg",
						"https://www.youtube.com/watch?v=7H0yo-lDuk0")
						
movies = [lion_king, finding_dory, jumanji, the_devil_wears_prada, fireproof, iron_man]
#Calls list of movie instances to open a generated HTML file in the web browser
fresh_tomatoes.open_movies_page(movies)