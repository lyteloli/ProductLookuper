# A simple scrapper for your extraordinary wishes

This scrapper will check for wished items to appear at OLX and AllegroLokalnie marketplaces and will notify you via
Telegram.

# Requirements

##### Global

- Docker
- \[Optional\] Makefile support (Windows machine probably won't do, so be ready to execute commands manually)

##### Development

- Python3.10.X
- Pipenv

# Usage

1. Create and fill in `.env` file in project root like so:

```dotenv
BOT_ADMINS="0, 1, 2"
SEARCH_LIST="extra large coffee cup, chinese tea"
BOT_TOKEN="123456789:QWERTY"
```

- `BOT_ADMINS` - a comma-separated list of Telegram IDs of users who should be notified.
- `SEARCH_LIST` - a comma-separated list of your wishes.
- `BOT_TOKEN` - a Telegram bot token obtained from [BotFather](https://t.me/BotFather).

2. Run the project:

Execute `make run` in project root.
