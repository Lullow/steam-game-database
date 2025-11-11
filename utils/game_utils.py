import json
from datetime import date, datetime
from io import BytesIO
from typing import Any, Tuple

import requests
from PIL import Image


class VideoGameDatabase:
    """
    Handles logic associated with working with video game data.
    Data is derived from a local steam.json-file
    Change the docstrings to fit your implementation
    Remember: DOCSTRINGS ARE YOUR TOOL OF COMMUNICATING HOW YOUR CLASS AND METHODS WORK! I cannot stress enough how important docstrings are. 
    Think very clearly about this question: What is it that makes a class reusable, and how do we communicate how it works to the consumer of the class?
    
    
    ****** IMPORTANT VG NOTE *******
    You will need to restructure the VideoGameDatabase to internally use VideoGame objects instead.
    That means you should most likely store a list of videogame objects.
    Methods parameters might need to be changed as well. Here is my one recommendation: 
    The way you ensure that the reusability doesn't suffer, is by allowing the methods to still take primitives as parameters (e.g ints, strings) and not VideoGame objects as parameters
    However, when it makes sense, return VideoGame objects or similar instead. That is perfectly reasonable, and is considered reusable - assuming that the consumer of the class UNDERSTANDS and EXPECTS to
    have VideoGame objects returned. This means your docstrings will need to be reflect this change.
    """


    # Dunder method that runs automatically when you create an object
    # steam.json gets its new name with variable "filename"
    # If no games are passed in, create an empty dictionary to store them later
    # If games were given, store them in self.video_games
    def __init__(self, games: dict[str, Any] | None = None, filename: str = "steam.json"):
        # Save the filename for later use
        self.filename = filename

        # If no games are sent in, load from file
        if games is None:
            # Create a empty dict so it can have an attribute (self.video_games)
            self.video_games = {}
        # Then load data from the file automatically
            self._load_data()
        else:
            # If we get data from user - use that!
            self.video_games = games

    # Use _(underscore) to make it non-public. 
    # its only called inside the class (__init__), so its not meant to be used from outside.
    # This method is responsible for opening the file and turning the JSON to python data.
    def _load_data(self):
        """
        TEACHER:
        This is a non-public method (should never be called from outside the class)
        - This method should load the video game data from the json-file
        - It should be run ONCE when the class is created / instantiated

        ---------
        Loads all the game data from JSON file, and is non-public.
        The method should only be called once when the class starts.
        Raises exceptions if something goes wrong.
        -------- 
        """

        # Opens the self.filename with the utf-8 encoding, which makes special symbols safe (ä,ö,å etc).
        # Converts the json to python list/dict style with self.video_games = json.load(file).
        # Raises detailed errors if something goes wrong.
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.video_games = json.load(file)

                # Check if attribute is a dict, if not = valueerror.
                if not isinstance(self.video_games, dict):
                    raise ValueError("Format error: JSON file must contain a dictionary of games.")

        # More errorhandling
        # Filenotfound(selfexplanatiory), 
        # Json decoder = handles things like faulty "code" in the json file (like a bracket missing or something)
        except FileNotFoundError:
            raise FileNotFoundError("The datafile could not be found}")
        except json.JSONDecodeError:
            raise ValueError("The JSON file is unreadable or invalid")



    # @property  turns this method into a *read-only attribute*
    # That means you can access it like this: object.total_games (no parentheses!)
    # Instead of calling it like a function: object.total_games()
    @property
    def total_games(self) -> int:
        """
        TEACHER:
        Property that returns the total number of games in the database

        ---------
        Returns the total amount of games in the database.
        ---------

        """
        # Returns all games that are stored in json data via self.video_games (returns them in numbers).
        return len(self.video_games)

    # UNNECCESARY?
    def _get_game_by_id(self, app_id: str) -> dict[str, Any]:
        """
        Non public method that fetches a specific game
        Should only be used internally as a utility method
        """
        pass


    def search_game(self, word_to_search_for: str | None = None, app_id: int | None = None) -> dict[str, Any]:
        """
        TEACHER:
        - Should return the first video game with a "name" that either CONTAINS **or** COMPLETELY MATCHES the input word
        - It should also be able to use an appip instead of the name for searching
        - return the entire dictionary if it exists
        - raise a "KeyError" exception if it did not exist
        This method can be used both from the outside of the class AND from other methods inside the class
        You will probably use it a lot

        -----------------
        Finds the game through its name or app id.
        Returns the game data as a dictionary.
        Raises KeyError if it's not found.
        -----------------
        """

        # Baisc errorhandling if user doens't input anything.
        if word_to_search_for is None and app_id is None:
            raise ValueError("Please provide either 'word_to_search_for' or 'app_id'")

        # Treat user input as an app_id automatically if it's digits, instead of a name.
        if word_to_search_for and word_to_search_for.isdigit():
            app_id = int(word_to_search_for)
            word_to_search_for = None # do an id search instead.

        # If app_id was given, look for it in the dictionary.
        if app_id is not None:
            key = str(app_id) # JSON is usually string type.
            if key in self.video_games:
                return self.video_games[key]
            else:
                raise KeyError("No game found with the app_id")
        
        # Otherwise search by name:
        # Loop through games in dataset and get name of game, if not found set it to an empty string.
        for game in self.video_games.values():
            game_name = game.get("name", "").lower()

            # Check if userinput appears anywhere in game name.
            # Example: searching for "warcraft" will match "World of Warcraft".
            if word_to_search_for.lower() in game_name:
                return game
            
        raise KeyError("No game found with that name")

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Is this unneccessary now when the logic in search_game obj already exists?
    def get_price(self, game: str) -> float:
        """
        - Should return the price of the game
        - raise a "KeyError" exception if the game did not exist

        ---------
        Returns the price of the game by its name.
        Raises KeyError if it's not found.
        ---------
        """

        # Use search_game() method to find the game by name
        found_game = self.search_game(word_to_search_for=game)

        # Check if price exists, if not - keyerror
        if "price" not in found_game:
            raise KeyError("This game has no price information.")
        
        # Convert to float and handle errors (might be missing (None or N/A))
        try:
            return float(found_game["price"])
        except (TypeError, ValueError):
            raise ValueError("Price for the game is not available.") # MABY TRY TO FIX THIS TO BE MORE DETAILED.


    # Use _(underscore) to make it non-public. 
    def _get_rating(self, game: dict[str, Any]) -> float:
        """
        TEACHER:
        This is a non-public method (should never be called from outside the class)
        which should receive a game as a parameter and calculate the rating for it
        The rating should be a calculated by using the positive_ratings and negative_ratings.
        E.g rating = positive_ratings / (positive_ratings + negative_ratings)
        Return the rating as a float rounded to two decimals
        - *** DO NOT MODIFY THE ORIGINAL DATASET BY ADDING THIS AS A NEW PROPERTY, even if that makes it easier! ***
        --------------------

        --------------------
        """
        # Two different usages in dataset (positive / positive_ratings).
        # game.get from key and print value.
        # retrun float (.2 decimal).
        positive = game.get("positive", game.get("positive_ratings", 0)) or 0
        negative = game.get("negative", game.get("negative_ratings", 0)) or 0
        
        total = positive / (positive + negative)
        return float(total)


    def compare_video_game_ratings(self, first_game: str | int, second_game: str | int) -> bool:
        """
        TEACHER:
        Parameters can be either game names (str) or app_ids (int)
        - Should based on "_get_rating" compare two game ratings (how good the game is considered by users)
        - Return True if the first game has a higher rating
        - Return False if the first game has a lower rating
        - Raise appropriate exceptions

        -----------------------
        Compares rating between two games, using name or app_id.
        Returns True if the FIRST game has a higher rating, otherwise it returns False.
        Raises KeyError if a game can't be found.
        -----------------------
        """
        # Make sure all different datatypes is caught when getting input.
        if first_game.isdigit():
            # If it's digit (app_id) search for game thorugh it, but first we convert it to a str to match JSON datafile.
            game_1 = self.search_game(app_id=str(first_game))
        else:
            # Else search by name with string.
            game_1 = self.search_game(word_to_search_for=str(first_game))

        # Same same but different ^^
        if second_game.isdigit():
            game_2 = self.search_game(app_id=str(second_game))
        else:
            game_2 = self.search_game(word_to_search_for=str(second_game))

        # Use the non-public _get_rating() object to find calculates the rating - store in variable
        result_1 = self._get_rating(game_1)
        result_2 = self._get_rating(game_2)

        # Compare variables that holds result and return a boolean value 
        # (returns True if result_1 is bigger than result_2)
        return result_1 > result_2

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # THIS DOESN'T WORK AS INTENDED - IS IT BECAUSE THE IF TARGET EQUAL? WHAT ELSE TO USE?
    def get_developer_games(self, developer: str) -> list[dict[str, Any]]:
        """
        TEACHER:
        - Should return a list of all games made by a developer
        - raise an exception if the developer did not exist in the dataset

        -----------------
        Returns all games made by the developers.
        Raises ValueError if input is incorrect, KeyError if there's no games for that developer.
        ------------------
        """

        # Check input, if it's empty or contains spaces a ValueError is raised.
        # Use .strip() to further improve.
        if not developer or not developer.strip():
            raise ValueError("Please enter a developer name - Returning to main menu.\n")
        
        # Create variable that takes "friendy" input (convert to lowercase, remove whitespace).
        target = developer.strip().lower()
        # Create a empty list that stores each item as a dictionary.
        results: list[dict[str, Any]] = []

        # Loop through the games in dataset.
        # self.video_games is a dictionary, so .values() gives us all game dictionaries.
        for game in self.video_games.values():
            # .get() the list of developers for each game, use [] for safety if there's no "developers" in the game (returns a empty list).
            devs = game.get("developers", [])

            # Check if users input contains similar words as developers in the games list.
            # Convert developer name (d) to lowercase for better comparison.
            if any(target in d.lower() for d in devs):
                # Add the game to the list if found.
                results.append(game)

        # If no result is found (list is empty), raise KeyError.
        if not results:
            raise KeyError(f"No games found for developer: {developer}")
        
        # Return list of results if found.
        return results


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


    def get_game_by_tag(self, tag: str) -> list[dict[str, Any]]:
        """
        TEACHER:
        - Should return a list of all games with a specific tag
        - raise a custom exception if the tag did not exist in the dataset
        Note that some games do not have tags

        ----------------------
        Return all games as a list with a specific tag (case-insensitive and matches partial inputs).
        Raises ValueError if input is empty, KeyError if no games matches the input.
        ----------------------
        """

        # Make sure there's a input and no spaces. 
        if not tag or not tag.strip():
            raise ValueError("Please provide a tag.")
        
        # Create new variable for userinput that has no whitespaces and is lowercased.
        # Create a empty list (results) that contains dictionaries for each game.
        needle = tag.strip().lower()
        results: list[dict[str, Any]] = []

        # Loop through database and get values from game ID.
        # Get the games tag list (helper function handles "errors")
        # Make it case-insensetive for comparison
        for game in self.video_games.values():
            tags = self._as_list(game.get("tags"))
            tags_lower = [t.lower() for t in tags]

            # Make so it matches exactly or partial (so it can be found via "Action", "action" or "MMO action").
            # Use any to append partial or exact matches.
            if any(needle == t or needle in t for t in tags_lower):
                results.append(game)

        # No match -> raise Keyerror with message.
        if not results:
            raise KeyError(f"No games found with tag: {tag}")
        
        return results


    def get_game_by_genre(self, genre: str) -> list[dict[str, Any]]:
        """
        TEACHER:
        - Should return a list of all games with a specific genre
        - raise a custom exception if the genre did not exist in the dataset
        Note that some games do not have genres
        
        ----------------
        Return all games as a list with a specific genre (case-insensitive and matches partial inputs).
        Raises ValueError if input is empty, KeyError if no games matches the input.
        ----------------
        """
        # Check that the user entered something and that it's not just empty spaces.
        if not genre or not genre.strip():
            raise ValueError("Please provide genre.")
        
        # Clean the input -remove spaces and make lowercase.
        needle = genre.strip().lower()
        results: list[dict[str, Any]] = []

        # Loop through games in database.
        # Get genres for game as a list.
        # Lowercase the genres for more effective comparison.
        for game in self.video_games.values():
            genres = self._as_list(game.get("genres"))
            genres_lower = [g.lower() for g in genres]

            # Check if userinput genre matches or is part of any genre name, if so, append it.
            if any(needle == g or needle in g for g in genres_lower):
                results.append(game)
        
        # Raise error if no match is found.
        if not results:
            raise KeyError(f"No games found with genre: '{genre}' - Returning to main menu.\n")
        
        return results

    # Changing the "app_id" parameter to "app_id_or_name" so user can pass both name & id.
    def get_image(self, app_id_or_name: str) -> Any:  # Should probably return some kind of image
        """
        TEACHER:
        - Should fetch the image of a game if it exists, download it and convert it to an image
        using the pillow package, and return it.
        raise an exception of choice if something went wrong
        
        ---------------
        Finds a game with app_id or name, downloads its image to memory (isn't saved).
        Returns: PIL.Image object, game_dict.
        Raise:
        - ValueError for bad or empty input.
        - KeyError if no game found or image URL doens't exist in database.
        - ConnectionError: HTTP/network error when downloading.
        --------------
        """

        # Check that the user entered something - use isinstance to safely strip strings
        if app_id_or_name is None or (isinstance(app_id_or_name, str) and not app_id_or_name.strip()):
            raise ValueError("Please provide a name or app_id.")
        
        # Use search_game() method to fetch data.
        game = self.search_game(app_id_or_name)

        # Get the image URL from game dictionary.
        url = game.get("header_image")
        if not url or not isinstance(url, str):
            raise KeyError("Game does not have a image URL in dataset.")
        
        # Download image from internet.
        # Raise error if request failed or got connection error when downloading.
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
        except requests.RequestException as e:
            raise ConnectionError(f"Count not download image {e}") from e
        
        try:
            # Use pillow to download image to memory and load it.
            image = Image.open(BytesIO(resp.content))
            image.load()

            # Convert it to RGB if color is not "right".
            if image.mode not in ("RGB", "RGBA"):
                image = image.convert("RGB")

        # Raise error if not valid.
        except Exception as e:
            raise ValueError("Downloded file doesn't have a vaild image.") from e
        
        return image

    def _parse_release_date(self, raw: str):
        """
        Turns JSON string date to a datetime.date (common date formats).
        Returns None if missing or not readable.
        """

        # Check for empty or missing values, return None if so.
        if not raw or not str(raw).strip():
            return None

        # Clean up the date: string and strip it.
        raw = str(raw).strip()

        for fmt in ("%b %d, %Y", "%Y-%m-%d", "%d %b %Y"):
            try:
                return datetime.strptime(raw, fmt).date()
            except ValueError:
                continue

        return None

    def list_latest_games(self, number_of_games_to_list: int) -> list[dict[str, Any]]:
        """
        TEACHER:
        This method should return a list of the latest video games ordered by release_date
        Use the datetime-module
        raise an exception of choice if something went wrong

        ------------
        Returns a list of the latest video games that's ordered by release date.
        Uses the datetime-module.
        Raises ValueError if no input is given, and KeyError if something goes wrong.
        Uses a helper function to import date and time.
        -------------

        """

        # 
        if not isinstance(number_of_games_to_list, int) or number_of_games_to_list <= 0:
            raise ValueError("Please enter a positive number for how many games to list.")
        
        dated_games: list[tuple[datetime.date, dict[str, Any]]] = []
        for game in self.video_games.values():
            date = self._parse_release_date(game.get("release_date"))
            if date is not None:
                dated_games.append((date, game))
            
        if not dated_games:
            raise KeyError("No games found with valid release date.")
        
        # Sort by date - new first.
        dated_games.sort(key=lambda pair: pair[0], reverse=True)

        # Keep only the game dicts, remove requested length.
        latest_games = [game for _, game in dated_games][:number_of_games_to_list]
        return latest_games



    def popular_games(self, number_games_to_list: int) -> list[dict[str, Any]]:
        """
        - This method should return a list of X number of most popular video games
        based on the provided "number_games_to_list" parameter.
        - You should use the non-public/protected _get_rating method to do this.
        - raise an exception (you choose yourself which one) if something went wrong

        Max number: 20
        Minimum number: 5
        """

        # Remove pass when you've added code
        pass


    def get_top_developers(self, number_of_developers: int = 10, metric: str = "rating") -> list[tuple[str, float]]:
        """
        Returns a list of tuples containing (developer_name, metric_value)
        Parameters:
        - number_of_developers: How many top developers to return (default: 10)
        - metric: Which metric to use - "rating", "peak_ccu", or "review_count" (default: "rating")

        The method should calculate the metric for each developer based on their games
        For rating: use average rating of all their games
        - raise an exception (you choose yourself which one) if something went wrong
        """

        # Remove pass when you've added code
        pass


    def get_average_rating_by_date_range(self, start_date: str, end_date: str) -> float:
        """
        Calculate the average rating of all games released within a specific date range

        Parameters:
        - start_date: Start date in format "MMM DD, YYYY" (e.g., "Jan 1, 2020")
        - end_date: End date in format "MMM DD, YYYY" (e.g., "Dec 31, 2020")

        Returns:
        - The average rating as a float rounded to two decimals

        Raises:
        - ValueError if no games are found in the specified date range
        - ValueError if date format is invalid
        """
        # Remove pass when you've added code
        pass



    # FEEL FREE TO ADD MORE METHODS IF YOU WANT / NEED TO


class VideoGame:
    """
    (VG REQUIREMENT, not required for G) - Below is a starting point which you might have to change. Feel free to completely rework it.
    
    Entity class representing a single video game.
    This class focuses on storing and presenting video game data.
    It can be used to create VideoGame objects from dictionary data returned by VideoGameDatabase.
    """

    def __init__(self, app_id: str, game_data: dict[str, Any]):
        """
        Initialize a VideoGame object from game data dictionary

        Parameters:
        - app_id: The Steam app ID of the game
        - game_data: Dictionary containing all the game information
        """
        self.app_id = app_id
        self.name = game_data.get("name", "Unknown")
        self.release_date = game_data.get("release_date", "Unknown")
        self.price = game_data.get("price", 0.0)
        self.developers = game_data.get("developers", [])
        self.publishers = game_data.get("publishers", [])
        self.genres = game_data.get("genres", [])
        self.tags = game_data.get("tags", {})
        self.positive = game_data.get("positive", 0)
        self.negative = game_data.get("negative", 0)
        self.header_image = game_data.get("header_image", "")
        self.about_the_game = game_data.get("about_the_game", "")
        self.categories = game_data.get("categories", [])
        self.peak_ccu = game_data.get("peak_ccu", 0)
        self.average_playtime_forever = game_data.get("average_playtime_forever", 0)
        self.metacritic_score = game_data.get("metacritic_score", 0)
        self.windows = game_data.get("windows", False)
        self.mac = game_data.get("mac", False)
        self.linux = game_data.get("linux", False)
        # Store the full data for any additional fields
        self._raw_data = game_data

    def get_rating(self) -> float:
        """
        Calculate and return the rating for this game
        Rating = positive / (positive + negative)
        Returns 0.0 if there are no ratings
        """
        total = self.positive + self.negative
        if total == 0:
            return 0.0
        return round(self.positive / total, 2)

    def get_platforms(self) -> list[str]:
        """
        Returns a list of platforms this game is available on
        """
        platforms = []
        if self.windows:
            platforms.append("Windows")
        if self.mac:
            platforms.append("Mac")
        if self.linux:
            platforms.append("Linux")
        return platforms

    def is_free(self) -> bool:
        """
        Returns True if the game is free to play
        """
        return self.price == 0.0

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the VideoGame object back to a dictionary format
        Useful for saving favorites or exporting data
        """
        return {
            "app_id": self.app_id,
            "name": self.name,
            "release_date": self.release_date,
            "price": self.price,
            "developers": self.developers,
            "publishers": self.publishers,
            "genres": self.genres,
            "tags": self.tags,
            "positive": self.positive,
            "negative": self.negative,
            "rating": self.get_rating(),
            "header_image": self.header_image,
            "platforms": self.get_platforms(),
        }

    def __str__(self) -> str:
        """
        String representation of the VideoGame object
        """
        return f"{self.name} ({self.app_id}) - Rating: {self.get_rating()}"

    def __repr__(self) -> str:
        """
        Detailed representation for debugging
        """
        return f"VideoGame(app_id='{self.app_id}', name='{self.name}', rating={self.get_rating()})"

