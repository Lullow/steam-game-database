# Steam Game Database

A terminal-based video game explorer built in Python, using real Steam store data.

This was my **fourth Python lab** — a take-home exam built during the course *Programmering i Python* in April 2026. The focus was on advanced object-oriented programming: separation of concerns, encapsulation, reusability, and the entity pattern. The database class (`VideoGameDatabase`) acts as a standalone, reusable component — the way you'd think about a third-party package — while `Menu` handles all user interaction and presentation logic.

## What it does

- Search for a game by name or Steam app ID
- View a full game summary (description, price, developers, genres, categories)
- Look up the price of any game
- Compare ratings between two games
- List all games by a specific developer
- Export games filtered by tag or genre to a JSON file
- Display the latest games by release date
- List the most popular games by rating
- Show top developers by average rating
- Download and open a game's cover image

## How to run

```
pip install -r requirements.txt
python main.py
```

## Structure

- `main.py` — `Menu` class with all user interaction and presentation logic
- `utils/game_utils.py` — `VideoGameDatabase` class (data access and logic) and `VideoGame` entity class
- `data/steam.json` — Steam game dataset
- `requirements.txt` — dependencies

## Tech

- Python 3
- `requests` library
- Pillow (image handling)

## Reflection

This was a timed exam (written under pressure), so some parts of the code are rougher than I'd like. I've left it as-is — it's an honest snapshot of where I was at this point in my learning. The architecture itself I'm happy with: the clean split between the database layer and the menu layer made the code much easier to reason about and extend.
