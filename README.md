# ExtraCredit-Algorithm-Design
Extra Credit Assignment for CSC 3430
Project by Duncan Hook

Video of program running: https://youtu.be/UGE-8Dsxp9U

For this extra credit assignment I chose to work on the second problem: Implement the algorithm to solve Problem 5 of Chapter 4 of the Kleinberg Book.

I do not believe this program has any external requirements, but I included a requirements file just in case something is necessary that I don't know about. 

To run this project after cloning it, you can either debug or hit the run button with anything that supports running Python programs. 

Upon launch, the program will ask you to input the name of a text file. I have two different .txt files given here with easydistances.txt and harddistances.txt, but you are freely capable to use your own .txt files, as long as the files only contain numeric values. (The program will check if there are any non-numeric values, notify you if there are, and then end the program so that you can edit the file). 

The program will then read the values from your file, analyze them, and output where the base stations should be placed in order to cover every house with the least aomount of base stations in a file called StationLocations.txt. 

That's all there to actually run the program, as for how the program works I shall explain below. 

This program uses a greedy algorithm in order to decide where the base camps should go. 
To do this, it finds the first house in the list of provided values, and then places the first base station 4 miles away from said house.
Then, Every house within 4 miles of the newly placed base station gets deleted from the list of house locations.
The algorithm then finds the next house, places a base station 4 miles away from it, and deletes all of the houses within 4 miles of that base station from the list.
This continues until no houses remain inside the list, and thus, all houses are covered by a base tower.

This is, as far as I know, the most efficient way to solve this problem. it will use the least amount of base stations because of the fact that it places base stations only when there is a house uncovered by another base station. And by removing every house within a 4 mile radius of the base station, it ensures no house gets double covered and thus no base stations are wasted/redundant.
