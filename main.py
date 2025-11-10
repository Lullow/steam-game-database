###### -- READ THIS --#######################################################################

# Methods in the "Menu" class will usually have a corresponding or related method in the "VideoGameDatabase" class
# This means that usually the Menu will have methods that call the methods in the VideoGameDatabase class
# Feel free to add a few more methods if needed (optional)

# The purpose of this lab is to practice on separation of concerns.
# The VideoGameDatabase class should only be responsible for handling the data, while the Menu class is responsible for the presentation logic (print, input, etc)
# The Database-class should raise exceptions when needed, and the Menu is the only responsible for handling these exceptions
# One of the classes should be considered reusable, the other is most likely not reusable.
# In practice, we should be able to use the Database-class with other classes that might want to use the same data
# Such as a tkinter-based app, or a web application.

# YOU ARE 100% FREE TO MODIFY PARAMETERS IF YOU WANT TO IMPROVE / CHANGE THE STRUCTURE - As long as you can make a case for it!
# YOU ARE 100% FREE TO USE EXTERNAL PACKAGES! e.g pillow (for images), pandas, requests, tabulate.. etc. Just make sure to include a requirements.txt-file.
# YOU SHOULD IMPLEMENT AS MANY METHODS AS YOU ARE CAPABLE OF IMPLEMENTING -
# - Leaving a few out does not mean you will fail. What matters is you try your best to write the code yourself.
##############################################################################################

import json
from pathlib import Path
from typing import Any

from utils.game_utils import VideoGame, VideoGameDatabase


class Menu:
    """
    This class is responsible for handling the specific presentation logic of the application

    This means that the menu will be responsible for:
    1. asking the user for **inputs**
    2. Responsible of the **actual menu** -
    3. **reacting** to raised exceptions and telling the user what went wrong

    The "VideoGameDatabase" class might raise exceptions, but it should be the
    responsibility of the "Menu" class to react to these errors, e.g by asking them to try again
    or telling them what went wrong
    
    REWRITE THIS DOCSTRING WHEN YOU ARE DONE. When you finish the assignment, there shouldn't be any trace left of my instructions.
    """

    def __init__(self):
        """
        You don't need to do anything here
        - An instance of the VideoGameDatabase is created
        - We are starting the menu-flow that should give the user a choice of what to do
        """
        # Build a path relative to this file (fixes many FileNotFoundError issues)
        self.video_game_db = VideoGameDatabase(filename="data/steam.json")
        
        self.start_main_menu()  # start loop

    def start_main_menu(self):
        """
        This should start a standard flow for a menu which asks the user what to do.
        Example:

        What would you like to do?
        [1] - Show summary of a game
        [2] - Show price of a game
        [3] - Compare game ratings
        [4] - Show developer games
        [5] - Export video games from a tag or genre of choice
        [6] - Latest video games summary
        [7] - Get game image
        [8] - List most popular games
        [9] - Top developers
        [10] - Get average rating by date range
        [11] - Add game to favorites (VG)
        [12] - View favorites (VG)
        [13] - Remove from favorites (VG)
        [q] - Quit (no dedicated method required)
        """

        # OBJECTS "COMPLETED" IN VGDB CLASS: init, load data, total games, serach games, get price
        # FIX MENU CHOICES AND OBJ FOR THEM BEFORE CONTINUING WITH VIDEOGAMESDATABASE 


        while True:
            print("What would you like to do?")
            print("[1] - Show summary of a game")
            print("[2] - Show price of a game")
            print("[3] - Compare game ratings")
            print("[4] - Show developer games")
            print("[5] - Export video games from a tag or genre of choice")
            print("[6] - Latest video games summary")
            print("[7] - Get game image")
            print("[8] - List most popular games")

            choice = input("Enter choice: ").lower().strip()

            if choice == "1":
                self.show_game_summary()
            elif choice == "2":
                self.display_game_pricing()
            elif choice == "3":
                self.compare_ratings()
            elif choice == "4":
                self.display_developer_games()
            else:
                print("Invalid choice, please try again.")


    # FIX A STR FORMATTER TO HANDLE UI (DONT USE .JOIN EVERYWHERE)
    def show_game_summary(self):
        """
        TEACHER:
        - Print a simple summary of a single game chosen by name or appid
        - Ask the user for input and handle any raised exceptions
        - Use the relevant / corresponding method in the Database class
        - If you want (optional), you can also add some interesting information about the game, such
        as how the price compares to the average of all game prices, if the average playtime is high or low compared to others
        and so forth. Only do this once you have completed the other requirements (hint: this is easy to do with pandas).

        Hint: First use the search-method in the Database class

        ----------------
        Ask the user for an input of the games name or app id and show summary of that game.
        Summary include: Name, price, developers, categories, genres and a description.
        If game is not found or something goes wrong, print an error message instead.
        ----------------
        """

        summary_input = input("What game would you like a summary of, you can enter app_id or a name: ").strip()

        try:
            game = self.video_game_db.search_game(summary_input)
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
        
        # USE FORMATTER HERE LATER
        # Removing square brackets with .join
        # .get the dicts value by assigning key, if not found print "N/A".
        print("--------------------------------")
        print("Name:", game.get("name", "N/A"))
        print("Price:", game.get("price", "N/A"))
        print("Developers:", ", ".join(game.get("developers", "N/A")))
        print("Categories:", ", ".join(game.get("categories", "N/A")))
        print("Genres:", ", ".join(game.get("genres", "N/A")))
        print("About_the_game:", game.get("about_the_game", "N/A"))
        print("--------------------------------")


    def display_game_pricing(self):
        """
        TEACHER:
        Allow the user to check the price of a specific game
        - Should ask the user for the relevant input and handle any exceptions raised
        - As a bonus, you might want to add some general price statistics based on the dataset
        , e.g how does the price compare to other games

        --------------------
        Ask the user for an input of the games name or app id and show the price of that game.
        The program searches for the game in the database and then shows its price.
        If game is not found or something goes wrong, print an error message instead.
        --------------------
        """

        price_input = input("Enter game name or app_id to se e price: ").strip()

        # Using the search_game() method from the VideoGameDatabase object (composition) instead of get_price() - more logic in search_game().
        # Treat user input as an app_id automatically if it's digits.
        # Otherwise, search by name.
        # Get the price info from the found game dictionary.
        # If price exists, print it, if not - print "N/A".
        # Handle possible errors (ValueError from input, KeyError if not found).
        try:
            if price_input.isdigit():
                game = self.video_game_db.search_game(app_id=int(price_input))
            else:
                game = self.video_game_db.search_game(word_to_search_for=price_input)

            price = game.get("price")
            print(f"Price for game: {price if price is not None else 'N/A'}")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
        # Print the full game data dictionary for debugging (remove later).
        #print(game)


    # GETTING WILD ERRORS HERE - FRUSTATED - FIX LATER 
    def compare_ratings(self):
        """
        TEACHER:
        - Should use the relevant method in the Database class
        - Should ask the user for the relevant input and handle any exceptions raised
        ----------
        Ask user for two games by name or app_id.
        Compare their rating via the db and print results.
        Not using the private _get_rating
        ----------
        """
        game_a = input("Enter first game (name or app_id): ")
        game_b = input("Enter second game (name or app_id): ")

        try:
            # Returns True when first game has higher rating, else False.
            highest_rating = self.video_game_db.compare_video_game_ratings(game_a, game_b)
            
            # LOL, I just did the whole code below with this..
            if highest_rating:
                print(f"{game_a} is higher than {game_b}")
            else:
                print(f"{game_b} is higher than {game_a}")

            # THAT THE FUUUUUUK DID I JUST DO HERE?!
            # ALL THE BELOW CODE WAS UNNECCASSAY - THE ABOVE DID IT BETTER.

            # # Get the games to use later (we can't fetch them from _get_rating, it's private).
            # # If userinput is digits, we handle it as app_id, else it's the name of the game.
            # if game_a.isdigit():
            #     game_1 = self.video_game_db.search_game(app_id=game_a)
            # else:
            #     game_1 = self.video_game_db.search_game(word_to_search_for=game_a)

            # if game_b.isdigit():
            #     game_2 = self.video_game_db.search_game(app_id=game_b)
            # else:
            #     game_2 = self.video_game_db.search_game(word_to_search_for=game_b)

            # # Calculate the rating internally, because we're not allowed to call the private _get_rating()
            # positive_1 = game_1.get("positive", game_1.get("positive_ratings", 0)) or 0
            # negative_1 = game_1.get("negative", game_1.get("negative_ratings", 0)) or 0
            # positive_2 = game_2.get("positive", game_2.get("positive_ratings", 0)) or 0
            # negative_2 = game_2.get("negative", game_2.get("negative_ratings", 0)) or 0

            # # Round to .2 decimals and handle divison by zero.
            # round_1 = round(positive_1 / (positive_1 + negative_1), 2) if (positive_1 + negative_1) > 0 else 0.0
            # round_2 = round(positive_2 / (positive_2 + negative_2), 2) if (positive_2 + negative_2) > 0 else 0.0

            # print("Comparing the ratings between games:")
            # print(f"{game_1.get('name', 'N/A')}: {round_1}")
            # print(f"{game_2.get('name', 'N/A')}: {round_2}")


            # Compare them: First check if they are equal.
            # Use varaible that holds boolean value and print message.
            # if round_1 == round_2:
            #     print("Games have the same rating.")
            # elif highest_rating:
            #     print(f"Result of comparison: {game_1('name', 'N/A')} is rated higher than {game_2('name', 'N/A')}")
            # else:
            #     print(f"Result of comparison: {game_2('name', 'N/A')} is rated higher than {game_1('name', 'N/A')}")

        # Errorhandling that catches if game doesn't exist in database and unexcpected errors.
        except KeyError as e:
            print(e)
        except Exception as e:
            print(f"Error: {e}")

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # THIS DOESN'T WORK AS INTENDED - CHECK GET_DEVELOPER_GAMES LOGIC.
    def display_developer_games(self):
        """
        TEACHER:
        - Should be able to show all games made by a specific game developer company
        - Should use the corresponding method in the Database class to show developer games
        - Should ask the user for the relevant input and handle any exceptions raised

        ------------------
        Ask user for developer name, fetch games via the database and print it.
        Handle errors.
        ------------------
        """

        user_developer = input("Enter a developer name you want to lookup: ").strip()

        try:
            games = self.video_game_db.get_developer_games(user_developer)

            print(f"Games by {user_developer} ({len(games)} found.)")
            
            # For-loop that prints out a small summary of found games.
            for g in games:
                name = g.get("name", 'N/A')
                date = g.get("release_date", 'N/A')
                price = g.get("price", 'N/A')
                print(f"{name} - {date} - Price: {price}")

        # Handles empty input etc, no developer or unexcpected errors.
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
        except Exception as e:
            print(f"Error: {e}")


    def export_games_by_tag_or_genre(self):
        """
        - Should use the corresponding methods in the Database class to export games by tag or genre
        - Should ask the user for the relevant input and handle any exceptions raised
        - Should export these games to a new json-file
        """
        # Remove pass when you've added code
        pass

    def quit(self):
        """
        Should quit the program
        """
        # Remove pass when you've added code
        pass

    def display_game_image(self):
        """
        - Should fetch the image of a selected game and open it
        - Should ask the user for the relevant input and handle any exceptions raised

        """
        # Remove pass when you've added code
        pass

    def display_latest_games(self):
        """
        - Should use the relevant method in the Database class
        - Should ask the user for the relevant input and handle any exceptions raised
        """

        # Remove pass when you've added code
        pass

    def display_popular_games(self):
        """
        - Should use the relevant method in the Database class
        - Should ask the user for the relevant input and handle any exceptions raised
        """

        # Remove pass when you've added code
        pass

    def display_top_developers(self):
        """
        - Should list the top developers, based on metrics of your own choice
        - E.g list the 10 top developers which have the best average rating or peak_ccu (concurrent users)
        """

        # Remove pass when you've added code
        pass

    def display_average_rating_by_date_range(self):
        """
        Display the average rating of games within a specific date range
        - Ask the user for start and end dates
        - Use the get_average_rating_by_date_range method from VideoGameDatabase
        - Display the result in a user-friendly format
        - Handle any exceptions raised (invalid dates, no games found, etc.)

        Example date format: "Jan 1, 2020" or "Dec 31, 2020"
        """
        # Remove pass when you've added code
        pass

    def _load_favorites(self):
        """
        (VG)
        Private method to load favorites from the favorites.json file
        This should be called when the Menu is initialized
        - Load the favorites from the json file
        - Create VideoGame objects from the loaded data
        - Handle the case where the file doesn't exist (first time running)
        """
        # Remove pass when you've added code
        pass

    def _save_favorites(self):
        """
        (VG)
        Private method to save favorites to the favorites.json file
        - Convert VideoGame objects to dictionaries using to_dict()
        - Save to json file
        - Handle any file writing errors
        """
        # Remove pass when you've added code
        pass

    def add_to_favorites(self):
        """
        (VG)
        Allow the user to add a game to their favorites list
        - Ask the user for the game name or app_id
        - Search for the game using VideoGameDatabase
        - Create a VideoGame object from the returned data
        - Add it to the favorites list
        - Save the favorites to file
        - Handle any exceptions raised
        """
        # Remove pass when you've added code
        pass

    def view_favorites(self):
        """
        (VG)
        Display all favorited games
        - Show a list of all games in the favorites list
        - Display relevant information for each game (name, rating, price, platforms)
        - Handle the case where there are no favorites
        """
        # Remove pass when you've added code
        pass

    def remove_from_favorites(self):
        """
        (VG)
        Allow the user to remove a game from favorites
        - Display current favorites
        - Ask the user which game to remove (by number or app_id)
        - Remove the game from the favorites list
        - Save the updated favorites to file
        - Handle any exceptions
        """
        # Remove pass when you've added code
        pass



    # FEEL FREE TO ADD MORE METHODS IF YOU WANT / NEED TO



if __name__ == "__main__":
    menu = Menu()
