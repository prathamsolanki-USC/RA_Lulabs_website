# Genomic Data Query Interface - Django Web Application

A production-level Django web application that provides an intuitive, interactive interface for querying genomic datasets stored in AWS S3 using AWS Athena.

## 🚀 Features

- **Modern, Professional UI**: State-of-the-art design with Bootstrap 5, custom CSS, and smooth animations
- **Interactive Query Interface**: Dynamic forms with real-time validation and comparison operators
- **Responsive Design**: Mobile-first approach that works on all devices
- **Advanced Filtering**: Multiple criteria, comparison operators, and file selection
- **File Download Integration**: Seamless integration with external file download APIs
- **Production Ready**: Security features, error handling, and performance optimizations

## 🏗️ Architecture

- **Frontend**: HTML5, CSS3, JavaScript (ES6+), Bootstrap 5
- **Backend**: Django 4.2.7, Django REST Framework
- **Database**: SQLite (development), PostgreSQL (production ready)
- **External APIs**: AWS Lambda integration for genomic data queries
- **Security**: CORS handling, input validation, CSRF protection

## 📁 Project Structure

```
RA_LuLabs/
├── api_website/              # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI application
├── query_interface/          # Main Django app
│   ├── __init__.py
│   ├── views.py             # View logic and API endpoints
│   ├── urls.py              # App URL routing
│   └── admin.py             # Admin interface
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   └── query_interface/     # App-specific templates
│       ├── home.html        # Home page
│       ├── query.html       # Query interface
│       ├── results.html     # Results display
│       └── documentation.html # API documentation
├── static/                   # Static files
│   ├── css/
│   │   └── style.css        # Custom CSS
│   ├── js/
│   │   └── main.js          # Custom JavaScript
│   └── images/              # Image assets
├── requirements.txt          # Python dependencies
├── env_template.txt          # Environment variables template
├── manage.py                # Django management script
└── README_Django.md         # This file
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtual environment (recommended)

### 1. Clone and Setup

```bash
# Navigate to project directory
cd RA_LuLabs

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

```bash
# Copy environment template
cp env_template.txt .env

# Edit .env file with your configuration
nano .env
```

**Required Environment Variables:**
- `DEBUG`: Set to `True` for development, `False` for production
- `DJANGO_SECRET_KEY`: Your Django secret key
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `EXTERNAL_API_URL`: Your AWS Lambda function URL

### 3. Database Setup

```bash
# Run database migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 4. Static Files

```bash
# Collect static files
python manage.py collectstatic
```

### 5. Run Development Server

```bash
# Start development server
python manage.py runserver

# Access the application at http://localhost:8000
```

## 🌐 Usage

### Home Page (`/`)
- Landing page with feature overview
- Navigation to different sections
- Call-to-action buttons

### Query Interface (`/query/`)
- Interactive form for building genomic data queries
- Multiple filter options with comparison operators
- File type selection
- Real-time validation
- AWS credentials input

### Documentation (`/documentation/`)
- Comprehensive API reference
- Query examples
- Deployment instructions
- Troubleshooting guide

### API Endpoint (`/api/query/`)
- POST endpoint for executing queries
- JSON request/response format
- Integration with external genomic data APIs

## 🔧 Configuration

### Development Settings

```python
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

### Production Settings

```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### External API Integration

Update the `EXTERNAL_API_URL` in your `.env` file to point to your AWS Lambda function:

```bash
EXTERNAL_API_URL=https://your-lambda-function-url.lambda-url.us-east-2.on.aws/
```

## 🚀 Deployment

### Local Development

```bash
python manage.py runserver
```

### Production with Gunicorn

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn api_website.wsgi:application --bind 0.0.0.0:8000
```

### Production with Nginx + Gunicorn

1. **Configure Nginx**:
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location /static/ {
        alias /path/to/your/staticfiles/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

2. **Run Gunicorn**:
```bash
gunicorn api_website.wsgi:application --bind 127.0.0.1:8000 --workers 3
```

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "api_website.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 🔒 Security Features

- **CSRF Protection**: Built-in Django CSRF middleware
- **Input Validation**: Comprehensive form validation
- **CORS Handling**: Configurable cross-origin resource sharing
- **Secure Headers**: HSTS, XSS protection, content type sniffing
- **Environment Variables**: Secure credential management

## 📱 Responsive Design

- **Mobile First**: Optimized for mobile devices
- **Bootstrap 5**: Modern CSS framework
- **Custom CSS**: Professional styling with CSS variables
- **Smooth Animations**: CSS transitions and keyframes
- **Accessibility**: ARIA labels and keyboard navigation

## 🧪 Testing

```bash
# Run tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 📊 Performance

- **Static File Optimization**: WhiteNoise for static file serving
- **Database Optimization**: Efficient queries and indexing
- **Caching**: Ready for Redis/Memcached integration
- **CDN Ready**: Static files optimized for CDN deployment

## 🔍 Monitoring & Logging

- **Performance Monitoring**: Built-in performance tracking
- **Error Handling**: Comprehensive error logging
- **Console Logging**: Development-friendly logging
- **Production Logging**: File-based logging for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Check the documentation at `/documentation/`
- Review the troubleshooting section
- Open an issue on GitHub

## 🔄 Updates

To update the application:

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Restart the application
```

---

**Built with ❤️ using Django and modern web technologies**
