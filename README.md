# LottoLite - Django Telegram Bot Integration

This project integrates Django with a Telegram bot, allowing you to use Django models in your Telegram bot.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory with your bot configuration:
```
BOT_TOKEN=your_telegram_bot_token_here
BASE_URL=http://localhost:8000
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage

### Run Django server only:
```bash
python manage.py runserver
```

### Run Telegram bot only:
```bash
python manage.py runbot
```

### Run both Django server and Telegram bot simultaneously:
```bash
python manage.py runserver_bot
```

You can also specify custom host and port:
```bash
python manage.py runserver_bot --host 0.0.0.0 --port 8000
```

## Bot Features

- User registration and management through Django models
- Integration with Django's User model
- Async/await support for better performance

## Project Structure

- `app_account/` - User management and authentication
- `app_bot/` - Telegram bot implementation
- `lottolite/` - Django project settings
- `templates/` - Django templates 