# Django Telegram Bot Integration Template

A comprehensive Django project template that integrates Telegram bots with Django, providing a solid foundation for building Telegram bot applications with Django backend.

## Features

- **Django Integration**: Full Django project structure with models, views, and admin interface
- **Telegram Bot**: Ready-to-use Telegram bot with async/await support
- **User Management**: Django User model integration with Telegram users
- **Management Commands**: Custom Django management commands for running bot and server
- **Environment Configuration**: Secure environment variable handling
- **Database Integration**: SQLite database with Django ORM
- **Template System**: Django templates for web interface
- **Admin Interface**: Django admin for managing bot data

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Django_telegram.git
cd Django_telegram
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the root directory:
```env
BOT_TOKEN=your_telegram_bot_token_here
BASE_URL=http://localhost:8000
SECRET_KEY=your_django_secret_key_here
DEBUG=True
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

## Usage

### Run Django Server Only
```bash
python manage.py runserver
```

### Run Telegram Bot Only
```bash
python manage.py runbot
```

### Run Both Django Server and Telegram Bot Simultaneously
```bash
python manage.py runserver_bot
```

### Custom Host and Port
```bash
python manage.py runserver_bot --host 0.0.0.0 --port 8000
```

## Project Structure

```
Django_telegram/
├── app_account/          # User management and authentication
│   ├── models.py         # User models
│   ├── views.py          # Account views
│   ├── admin.py          # Admin interface
│   └── migrations/       # Database migrations
├── app_bot/              # Telegram bot implementation
│   ├── bot.py            # Main bot logic
│   ├── models.py         # Bot-specific models
│   ├── views.py          # Bot web views
│   ├── admin.py          # Bot admin interface
│   └── management/       # Custom management commands
│       └── commands/
│           ├── runbot.py
│           └── runserver_bot.py
├── templates/            # Django templates
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Configuration

### Django Settings
The main Django settings are in `lottolite/settings.py`. Key configurations:

- Database: SQLite by default (easily changeable to PostgreSQL/MySQL)
- Static files: Configured for development
- Templates: Set up for the template directory
- Installed apps: Includes both `app_account` and `app_bot`

### Bot Configuration
Bot settings are managed through environment variables:

- `BOT_TOKEN`: Your Telegram bot token from @BotFather
- `BASE_URL`: Base URL for webhook (if using webhooks)
- `DEBUG`: Django debug mode

## Customization

### Adding New Bot Commands
1. Edit `app_bot/bot.py`
2. Add your command handlers
3. Register them in the bot setup

### Extending User Model
1. Modify `app_account/models.py`
2. Create and run migrations
3. Update bot logic in `app_bot/bot.py`

### Adding New Django Apps
1. Create new app: `python manage.py startapp your_app_name`
2. Add to `INSTALLED_APPS` in settings
3. Create models and views as needed

## Deployment

### Local Development
```bash
python manage.py runserver_bot
```

### Production Deployment
1. Set `DEBUG=False` in environment
2. Configure production database
3. Set up static file serving
4. Use a process manager like Supervisor or systemd
5. Configure webhook or polling for bot

### Environment Variables for Production
```env
BOT_TOKEN=your_production_bot_token
BASE_URL=https://yourdomain.com
SECRET_KEY=your_production_secret_key
DEBUG=False
DATABASE_URL=your_database_url
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues and questions:
- Create an issue on GitHub
- Check the documentation
- Review the code examples

## Changelog

### Version 1.0.0
- Initial release
- Django 5.2.4+ support
- python-telegram-bot 20.0+ integration
- Basic user management
- Management commands for bot and server
- Environment-based configuration 