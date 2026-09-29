# 9. Movie Collection System			
				
	# Develop a Python application to manage movie records.			
				
	# Requirements			
	# 	Read movie records from movies.csv.		
	# 	Display all movie information.		
	# 	Search for a movie using Movie ID.		
	# 	Use Regular Expressions to search movies by title.

import csv
import re

with open("movies.csv", "r", newline="") as file:
	movies = list(csv.DictReader(file))

print("All Movies")
for movie in movies:
	print("--------------------")
	for heading, detail in movie.items():
		print(heading + ":", detail)

movie_id = input("Enter Movie ID to search: ")
found = False

for movie in movies:
	if movie["Movie_ID"] == movie_id:
		print("Movie found:")
		for heading, detail in movie.items():
			print(heading + ":", detail)
		found = True
		break

if not found:
	print("Movie not found.")

title_pattern = input("Enter a title or regular expression to search: ")
found = False

for movie in movies:
	if re.search(title_pattern, movie["Title"], re.IGNORECASE):
		print("Matching movie:")
		for heading, detail in movie.items():
			print(heading + ":", detail)
		found = True

if not found:
	print("No matching movies found.")
