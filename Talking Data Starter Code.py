#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

def resource_path(relative):
    #print(os.environ)
    application_path = os.path.abspath(".")
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    #print(application_path)
    return os.path.join(application_path, relative)

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv(resource_path('rotten_tomatoes_movies.csv'))
favMovie = "Leap!"

print("My favorite movie is " + favMovie)
#Part 3 Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])
#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie

favMovieData = movieData.loc[favMovieBooleanList]
print("\n\n")

print(favMovieData)
#Create a new variable to store a new data set with a certain genre
romanceMovieBooleanList = movieData["genres"].str.contains("Romance")

romanceMovieData = movieData.loc[romanceMovieBooleanList]

numOfMovies = romanceMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre romance in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category romance.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = romanceMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 53 points higher than the lowest rated movie.")
print()

#find max
max = romanceMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 38 points lower than the highest rated movie.")
print()

#find mean
mean = romanceMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is lower than the mean movie rating.")

#find median
median = romanceMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is lower than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(romanceMovieData["audience_rating"], range(0, 100))
#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Romance Movies")
plt.xlabel("Audience Rating")
plt.ylabel("Number of Romance Movies")

#Prints interpretation of histogram
print(
    "According to the histogram, most romance movies have an audience rating between 60 and 80."
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data=romanceMovieData, x="audience_rating", y="critic_rating")
#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs. Critic Rating of Romance Movies")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
    "According to the scatter plot, there is a positive correlation between audience rating and critic rating for romance movies."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
