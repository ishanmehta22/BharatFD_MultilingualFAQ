# Django FAQ System

A multilingual FAQ management system built with Django, featuring automatic translation, caching, and a REST API.

## Features

- 🌐 Multilingual support with automatic translation (English, Hindi, Bengali)
- 💾 Redis caching for improved performance
- 🔄 Automatic fallback to local memory cache if Redis is unavailable
- 📝 Rich text editing support with CKEditor
- 🔑 Admin interface for FAQ management
- 🚀 RESTful API for accessing FAQs
- ✅ Comprehensive test coverage

## Tech Stack

- Django 5.1.5
- Django REST Framework
- Redis (with django-redis)
- CKEditor
- Google Translate API (via googletrans)
- SQLite (default database)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd faq_project
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Setup Redis:
```bash
# Windows
# Download and install Redis from https://github.com/microsoftarchive/redis/releases

# Linux
sudo apt-get install redis-server
sudo systemctl start redis-server

# MacOS
brew install redis
brew services start redis
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Configuration

The project uses a smart caching configuration that automatically falls back to local memory cache if Redis is unavailable. This configuration is in `settings.py`:

```python
try:
    import redis
    redis_client = redis.Redis(host='127.0.0.1', port=6379, db=1)
    redis_client.ping()
    
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
            'KEY_PREFIX': 'faq',
        }
    }
except (redis.ConnectionError, ModuleNotFoundError):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
        }
    }
```

## API Endpoints

### Get FAQs
- URL: `/api/faqs/`
- Method: `GET`
- Query Parameters:
  - `lang`: Language code (optional, default: 'en')
  - Available options: 'en', 'hi', 'bn'
- Response Example:
```json
[
    {
        "question": "What is Django?",
        "answer": "A Python web framework."
    },
    {
        "question": "How do I install Django?",
        "answer": "Using pip: pip install django"
    }
]
```

## Admin Interface

The admin interface is available at `/admin/` and provides the following features:
- Create, edit, and delete FAQs
- Rich text editing for answers
- View automatically translated content
- Search functionality

## Running Tests

To run the test suite:
```bash
pytest -v
```

The tests use Django's local memory cache backend and don't require Redis to be running.

## Development

### Project Structure
```
faq_project/
├── faq/
│   ├── migrations/
│   ├── tests/
│   │   ├── test_models.py
│   │   └── test_views.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── faq_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

### Adding New Features

1. Create a new branch for your feature
2. Write tests in the `tests/` directory
3. Implement your feature
4. Run the test suite
5. Submit a pull request

## Production Deployment

For production deployment:

1. Update `settings.py`:
   - Set `DEBUG = False`
   - Update `ALLOWED_HOSTS`
   - Use a secure `SECRET_KEY`
   - Configure production database

2. Set up Redis:
   - Configure Redis password
   - Update Redis configuration in settings
   - Enable Redis persistence

3. Set up proper web server (e.g., Nginx, Gunicorn)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting

### Common Issues

1. Redis Connection Error
```
redis.exceptions.ConnectionError: Error connecting to redis://127.0.0.1:6379/1
```
Solution: Ensure Redis is installed and running:
```bash
# Check Redis status
redis-cli ping
```

2. Translation Issues
```
googletrans.exceptions.TranslatorError
```
Solution: Check your internet connection and ensure you're not exceeding API limits.

## Support

For support, please open an issue in the repository or contact the maintainers.

## Authors

- Ishan Mehta - Initial work

## Acknowledgments

- Django Team
- Django REST Framework Team
- Redis Team
- CKEditor Team