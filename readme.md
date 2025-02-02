# Django FAQ System

A robust multilingual FAQ management system built with Django, featuring automatic translation, Redis caching, and a RESTful API. Perfect for websites and applications requiring multilingual FAQ support.

## 🌟 Features

- **Multilingual Support**
  - Automatic translations to Hindi, Bengali and over 100+ languages.
  - Dynamic translation to other languages on-demand
  - Persistent storage of common translations
- **Performance Optimization**
  - Redis caching implementation
  - Automatic fallback to local memory cache
  - Configurable cache timeouts
- **Rich Content Management**
  - CKEditor integration for rich text editing
  - Comprehensive admin interface
  - Search functionality
- **API Features**
  - RESTful API endpoints
  - Language-specific content delivery
  - Cached responses
- **Development Tools**
  - Comprehensive test coverage
  - PEP8 compliant codebase
  - Detailed documentation

## 🔧 Technical Stack

- Python 3.8+
- Django 5.1.5
- Django REST Framework
- Redis (with django-redis)
- CKEditor
- Google Translate API (via googletrans)
- SQLite (default database)

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Redis server (optional, will fallback to local cache)
- Git

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ishanmehta22/BharatFD_MultilingualFAQ.git
   cd BharatFD_MultilingualFAQ
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Redis Setup**
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install redis-server
   sudo systemctl start redis-server

   # macOS
   brew install redis
   brew services start redis

   # Windows
   # Download the MSI installer from https://github.com/microsoftarchive/redis/releases
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Admin User**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

# 🚀 API Usage

## FAQ Endpoints

### Get All FAQs
```http
GET /api/faqs/
```
Retrieves a list of all FAQs in English by default.

### Get FAQs in Specific Language
```http
GET /api/faqs/?lang={language_code}
```
Retrieves FAQs translated into the specified language using Google Translate.

#### Examples
##### English (Default)
```http
GET /api/faqs/
```
```json
[
  {
    "question": "What is Git?",
    "answer": "Git is a free, open-source version control system (VCS) that helps developers manage."
  },
  {
    "question": "What is NodeJS?",
    "answer": "Node.js is an open-source JavaScript runtime environment that allows developers to create server-side web applications."
  }
]
```

##### French (fr)
```http
GET /api/faqs/?lang=fr
```
```json
[
  {
    "question": "Qu'est-ce que Git?",
    "answer": "Git est un système de contrôle de version open-source gratuit (VCS) qui aide les développeurs à gérer."
  },
  {
    "question": "Qu'est-ce que NodeJS?",
    "answer": "Node.js est un environnement d'exécution JavaScript open-source qui permet aux développeurs de créer des applications Web côté serveur."
  }
]
```

##### Bengali (bn)
```http
GET /api/faqs/?lang=bn
```
```json
[
  {
    "question": "গিট কি?",
    "answer": "গিট হ'ল একটি বিনামূল্য, ওপেন-সোর্স সংস্করণ নিয়ন্ত্রণ সিস্টেম (VCS) যা বিকাশকারদের পরিচালনা করতে সহায়তা করে."
  },
  {
    "question": "নোডেজে কি?",
    "answer": "Node.js হ'ল একটি ওপেন-সোর্স জাভাস্ক্রিপ্ট রানটাইম পরিবেশ যা বিকাশকারদের সার্ভার-সাইড ওয়েব অ্যাপলিকেশন তিরিতে দেয়."
  }
]
```

## Supported Languages
The API supports translation to **all languages** recognized by Google Translate (over 100 languages). You can use any valid [Google Translate language code](https://cloud.google.com/translate/docs/languages) as the `lang` parameter.

Some commonly used language codes:
```
ar - Arabic
bn - Bengali
de - German
es - Spanish
fr - French
hi - Hindi
it - Italian
ja - Japanese
ko - Korean
pt - Portuguese
ru - Russian
zh - Chinese
```
Example usage:
```http
GET /api/faqs/?lang=ko    # Korean
GET /api/faqs/?lang=ar    # Arabic
GET /api/faqs/?lang=ru    # Russian
```

### Notes
- If no language code is provided, defaults to English (`en`).
- Invalid language codes will fall back to English.
- Translation quality may vary by language.
- All translations are performed in real-time using Google Translate API.

## Response Format
All responses follow this JSON structure:
```json
[
  {
    "question": "Translated question text",
    "answer": "Translated answer text"
  }
]
```

## Caching
- Responses are cached for **1 hour** by default.
- Each language has its **own cache key**.
- Cache automatically **invalidates** when FAQs are updated.

## Error Handling
- If translation fails, the API falls back to the original **English** content.
- All errors are **logged for monitoring**.
- Returns `200 OK` with available content even if some translations fail.

## ⚙️ Configuration

### Redis Configuration
```python
# settings.py
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
```

### Cache Timeout Settings
```python
# views.py
cache.set(cache_key, data, timeout=3600)  # 1 hour cache
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest faq/tests/test_models.py

# Run with coverage report
pytest --cov=faq
```

### Test Categories
- Model Tests: `test_models.py`
- View Tests: `test_views.py`
- API Tests: Included in view tests

## 👥 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the Repository**
   - Create your fork on GitHub

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Changes**
   - Write your code
   - Add tests for new features
   - Update documentation

4. **Run Tests**
   ```bash
   pytest
   flake8 .
   ```

5. **Commit Changes**
   ```bash
   git commit -m "Add amazing feature"
   ```

6. **Push to Branch**
   ```bash
   git push origin feature/amazing-feature
   ```

7. **Open Pull Request**
   - Provide clear description of changes
   - Link related issues


## 🔍 Troubleshooting

### Common Issues

1. **Redis Connection Errors**
   ```
   Error: redis.exceptions.ConnectionError
   ```
   **Solution:**
   ```bash
   # Check Redis status
   redis-cli ping
   
   # Start Redis if needed
   sudo systemctl start redis-server
   ```

2. **Translation API Issues**
   ```
   Error: googletrans.exceptions.TranslatorError
   ```
   **Solution:**
   - Check internet connection
   - Verify API quotas
   - Use VPN if region-blocked

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.


---
Made with ❤️ by Ishan Mehta