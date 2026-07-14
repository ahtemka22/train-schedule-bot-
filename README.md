[🇬🇧 English](README.md) | [🇷🇺 Русский](README.ru.md)

# Train Schedule Bot 🚆

A Telegram bot that shows the nearest train departures between Dzerzhinsk and Minsk, and calculates when you need to leave your location to catch the next train — based on your live GPS position.

## Features

- 📅 Get the 3 nearest train departures in either direction
- 📍 Send your GPS location via Telegram
- 🚶 Automatic walking-time calculation to the station (via OpenRouteService API)
- ⏰ Tells you exactly what time to leave and which train you'll catch
- 💾 Stores user IDs locally for basic usage tracking

## Tech Stack

- **Python 3**
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) — Telegram Bot framework
- [OpenRouteService API](https://openrouteservice.org/) — walking distance/time calculation
- `python-dotenv` — environment variable management

## Project Structure

```
├── main.py           # Entry point, bot polling, user storage
├── config.py         # Environment variables & schedule data
├── handlers.py        # Telegram message handlers / bot logic
├── keyboards.py       # Reply keyboard layouts
├── storage.py          # In-memory user location storage
├── utils.py            # Schedule lookup, travel time, exit time calculation
├── requirements.txt
└── users.json.example  # Example structure for stored user IDs
```

## How It Works

1. User sends `/start` and gets a menu with three options
2. **"3 ближайших поезда"** — shows the next 3 scheduled departures in a chosen direction
3. **"Отправить GPS"** — user shares live location
4. **"Расчет"** — bot calculates walking time from the user's location to the station using OpenRouteService, then works out the latest possible departure time and which train they'll catch

## Setup & Run Locally

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/train-schedule-bot.git
cd train-schedule-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your own credentials:
```
BOT_TOKEN=your_telegram_bot_token
ORS_API_KEY=your_openrouteservice_api_key
```

- Get a bot token from [@BotFather](https://t.me/BotFather) on Telegram
- Get a free API key from [openrouteservice.org](https://openrouteservice.org/dev/#/signup)

4. Run the bot:
```bash
python main.py
```

## Notes

- Train schedules are currently hardcoded in `config.py` for the Dzerzhinsk–Minsk direction. This could be extended to pull live schedule data or support additional routes.
- `users.json` is excluded from version control (see `.gitignore`) since it stores real Telegram user IDs; `users.json.example` shows the expected format.

## Possible Improvements

- [ ] Support for multiple train routes
- [ ] Persist user data in a proper database instead of a JSON file
- [ ] Add unit tests
- [ ] Deploy to a server (e.g. Heroku, Railway) for 24/7 availability
