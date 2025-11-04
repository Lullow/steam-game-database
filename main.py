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
        self.video_game_db = VideoGameDatabase(filename="steam.json")
        self.start_main_menu()

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
        # Remove pass when you've added code
        pass

    def show_game_summary(self):
        """
        - Print a simple summary of a single game chosen by name or appid
        - Ask the user for input and handle any raised exceptions
        - Use the relevant / corresponding method in the Database class
        - If you want (optional), you can also add some interesting information about the game, such
        as how the price compares to the average of all game prices, if the average playtime is high or low compared to others
        and so forth. Only do this once you have completed the other requirements (hint: this is easy to do with pandas).

        Hint: First use the search-method in the Database class
        """

        # Remove pass when you've added code
        pass

    def display_game_pricing(self):
        """
        Allow the user to check the price of a specific game
        - Should ask the user for the relevant input and handle any exceptions raised
        - As a bonus, you might want to add some general price statistics based on the dataset
        , e.g how does the price compare to other games
        """
        # Remove pass when you've added code
        pass

    def compare_ratings(self):
        """
        - Should use the relevant method in the Database class
        - Should ask the user for the relevant input and handle any exceptions raised
        """

        # Remove pass when you've added code
        pass

    def display_developer_games(self):
        """
        - Should be able to show all games made by a specific game developer company
        - Should use the corresponding method in the Database class to show developer games
        - Should ask the user for the relevant input and handle any exceptions raised
        """

        # Remove pass when you've added code
        pass

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
