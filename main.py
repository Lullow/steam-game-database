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

        while True:
            print("--------------------------------")
            print("What would you like to do?\n")
            print("[1] - Show summary of a game") # Check
            print("[2] - Show price of a game") # Check
            print("[3] - Compare game ratings") # Check
            print("[4] - Show developer games") # Check
            print("[5] - Export games by tag or genre") # Check
            print("[6] - Latest video games summary") # Check
            print("[7] - Get game image") # Check
            print("[8] - List most popular games\n")
            print("--------------------------------")
            

            choice = input("Enter choice: ").lower().strip()

            if choice == "1":
                self.show_game_summary()
            elif choice == "2":
                self.display_game_pricing()
            elif choice == "3":
                self.compare_ratings()
            elif choice == "4":
                self.display_developer_games()
            elif choice == "5":
                self.export_games_by_tag_or_genre()
            elif choice == "6":
                self.display_latest_games()
            elif choice == "7":
                self.display_game_image()
            else:
                print("Invalid choice, please try again.\n")

    # Create a private reusable helper function:
    def _as_list(self, value):
        """
        Converts the given input to a list of strings:
        None, single strings and other datatpes is converted to a list [].
        This is neccessary when working with big datasets - which can be inconsistent.
        """

        if value is None:
            return [] # When value is None, create empty list.
        elif isinstance(value, list):
            return [str(x) for x in value] # Convert the items in the list to strings.
        else:
            return [str(value)] # Wrap single value in a list and convert it to a string.


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

        # Guard empty input
        if not summary_input:
            print("Please enter a game name or app_id - Returning to menu.\n")
            return

        try:
            game = self.video_game_db.search_game(summary_input)
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
            return

        name = game.get("name", "N/A")
        price = game.get("price", "N/A")
        about_the_game = game.get("about_the_game", "N/A")
        release_date = game.get("release_date", "N/A")

        developers = ", ".join(self._as_list(game.get("developers")))
        categories = ", ".join(self._as_list(game.get("categories")))
        genres = ", ".join(self._as_list(game.get("genres")))

        print("--------------------------------")
        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Release date: {release_date}\n")
        print(f"About the game: {about_the_game}\n")
        print(f"Developers: {developers or 'N/A'}")
        print(f"Categories: {categories or 'N/A'}")
        print(f"Genres: {genres or 'N/A'}")
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

        price_input = input("Enter game name or app_id to see price: ").strip()

        # Guard empty input
        if not price_input:
            print("Please enter a game name or app_id - Returning to menu.\n")
            return

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
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
            return

        name = game.get("name", "N/A")
        raw_price = game.get("price", None)
        try:
            price_str = f"{float(raw_price):.2f}"
        except (TypeError, ValueError):
            price_str = "N/A"

        print(f"Name: {name}")
        print(f"Price: {price_str}\n")

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
        game_a = input("Enter first game (name or app_id): ").strip()
        game_b = input("Enter second game (name or app_id): ").strip()

        # Guard both inputs.
        if not game_a or not game_b:
            print("Please enter a game name or app_id for both games - Returning to menu.\n")
            return

        try:
            # Get games from database so we can print them.
            fetch_game_a = self.video_game_db.search_game(game_a)
            fetch_game_b = self.video_game_db.search_game(game_b)

            # Compares raiting and returns True if first > second, and False if first < second.
            if self.video_game_db.compare_video_game_ratings(game_a, game_b):
                print(f"{fetch_game_a.get('name', "N/A")}' has higher rating than '{fetch_game_b.get('name', 'N/A')}'.")
            elif self.video_game_db.compare_video_game_ratings(game_b, game_a):
                print(f"'{fetch_game_b.get('name', "N/A")}' has higher rating than '{fetch_game_a.get('name', "N/A")}.")
            else:
                # Check for ties.
                print(f"'{fetch_game_a.get('name', "N/A")}' and '{fetch_game_b.get('name', "N/A")}' has the same rating.")

        # Errorhandling that catches if game doesn't exist in database and unexcpected errors.
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexcpected error: {e}")


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

            # Print userinput and how many games found matching the input keyword.
            print(f"Games by {user_developer} ({len(games)} found).")
            
            # For-loop that prints out a small summary of found games.
            # Use helper method, clean output and print it.
            for game in games:
                name = game.get("name", 'N/A')
                date = game.get("release_date", 'N/A')
                price = game.get("price", 'N/A')
                developers = ", ".join(self._as_list(game.get("developers")))
                print(f"Name: {name}\n - Date: {date}\n - Price: {price}\n - Developer: {developers}")

        # Handles empty input etc, no developer or unexcpected errors.
        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
        except Exception as e:
            print(f"Error: {e}")


    def export_games_by_tag_or_genre(self):
        """
        TEACHER:
        - Should use the corresponding methods in the Database class to export games by tag or genre
        - Should ask the user for the relevant input and handle any exceptions raised
        - Should export these games to a new json-file

        --------------------
        Ask user to export via a tag or genre and fetch matching games from database.
        Export them to a new json-file.
        --------------------
        """

        # Keep asking user what method they want to use to export data.
        while True:
            user_choice = input("Export data by 'tag' or 'genre': ").strip().lower()

            # Accept either 'tag' or 'genre'
            if user_choice in ("tag", "genre"):                
                break
            else:
                print("Please provide either a 'tag' or a 'genre'")

        # Ask for the filterword, doesn't accept empty input.
        user_filter = input(f"Enter the {user_choice} to filter by: ").strip()
        if not user_filter:
            print("Please provide filter information - Returning to main menu.\n")
            return

        try:
            # Fetch information from database depending on users input.
            if user_choice == "tag":
                games = self.video_game_db.get_game_by_tag(user_filter)
            else:
                games = self.video_game_db.get_game_by_genre(user_filter)

            # Create folder "output", if it already exists, it's ok - dont crasch.
            out_dir = Path("output")
            out_dir.mkdir(exist_ok=True)

            # Safety messure to store users input:
            # Remove whitespace and dots (replace with underscore, lowercase text)
            # Check if it's numbers or letters, keep and join them.
            slug = "".join(ch if ch.isalnum() else "_" for ch in user_filter.lower())
            out_path = out_dir / f"export_{user_choice}_{slug}.json"

            # Open or create the file for writing, encode it so it accepts special symbols, save as file.
            # Write games in the file, keep non-english characters and indent so it's easy to read.
            with out_path.open("w", encoding='utf-8') as f:
                json.dump(games, f, ensure_ascii=False, indent=2)

            # Shows number of games and where the games were saved.
            print(f"Exported {len(games)} games with filter '{user_filter}' to: {out_path} - Returning to main menu.\n")

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


    def quit(self):
        """
        Should quit the program
        """
        # Remove pass when you've added code
        pass

    def display_game_image(self):
        """
        TEACHER:
        - Should fetch the image of a selected game and open it
        - Should ask the user for the relevant input and handle any exceptions raised

        ------------
        Ask user for game name or app_id and fetch the image via database, then open it.
        Handles errors.
        -----------
        """

        # Ask for a game name or app_id to fetch its image.
        user_input = input("Enter games name or app_id to get its image: ").strip()
        
        # Check that the user entered something.
        if not user_input:
            print("Please provide either a game name or app_id - Returning to main menu.\n")

        # Fetch and download the games image from database and handle common errors.
        try:
            image = self.video_game_db.get_image(user_input)
        except (ValueError, KeyError, ConnectionError) as e:
            print(f"Unexpected error {e}")
            return
        
        # Try to open the image using the systems default image viewer through Pillow.
        # Handle errors if pillow can't open image.
        try:
            image.show()
            print("Image opend.")
        except Exception:
            print("Image was downloaded, but couldn't be automatically opened.")


    def display_latest_games(self):
        """
        TEACHER:
        - Should use the relevant method in the Database class
        - Should ask the user for the relevant input and handle any exceptions raised
        
        ---------
        Ask user for input and handles exceptions.
        Uses database method to list the latest games.
        ---------
        """

        user_raw = input("How many recent games do you want to show? (For example '5'): ")

        # Convert input to int, and handle bad input (strings or symbols).
        try:
            n = int(user_raw)
        except ValueError:
            print("Please enter whole numbers - Returning to main menu.\n")
            return
        
        # Gets the list from database and handles errors from the database method (invalid input or no data). 
        try:
            games = self.video_game_db.list_latest_games(n)
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
            return
        
        # For-loop that prints out a small summary of found games.
        for game in games:
            name = game.get("name", 'N/A')
            date = game.get("release_date", 'N/A')
            price = game.get("price", 'N/A')
            developers = ", ".join(self._as_list(game.get("developers")))
            print(f"Game: {name}\n - Date: {date}\n - Price: {price}\n - Developers: {developers}\n")

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

# Today:
#  implemented in videogamedatabaseclass: get_game_by_tag, get_game_by_genre
#  implemented in menu class: export_games_by_tag_or_genre

if __name__ == "__main__":
    menu = Menu()
