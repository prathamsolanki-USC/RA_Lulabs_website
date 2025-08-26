# 🧬 Genomic Data Query Interface

A modern Django web application for querying genomic datasets with an intuitive interface and AWS Lambda integration.

## ✨ Features

- 🔍 **Interactive Query Interface** - Dynamic forms with real-time validation
- 📱 **Responsive Design** - Mobile-first approach with Bootstrap 5
- 🚀 **AWS Integration** - Lambda function integration for genomic data queries
- 🎨 **Modern UI** - Professional styling with smooth animations
- 🔒 **Production Ready** - Security features and performance optimizations

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/RA_Lulabs_website.git
cd RA_Lulabs_website

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your website!

## 🌐 Live Demo

- **Home**: `/` - Landing page with features
- **Query Interface**: `/query/` - Interactive data query form
- **Documentation**: `/documentation/` - API reference and guides
- **API Endpoint**: `/api/query/` - POST endpoint for queries

## 🏗️ Architecture

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend**: Django 4.2.7, Django REST Framework
- **Database**: SQLite (dev), PostgreSQL (production ready)
- **External APIs**: AWS Lambda for genomic data queries
- **Deployment**: GitHub Actions, Heroku ready

## 🔧 Configuration

### Environment Variables
```bash
DEBUG=True
DJANGO_SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
EXTERNAL_API_URL=https://your-lambda-function-url.lambda-url.us-east-2.on.aws/
```

### API Integration
Update the `EXTERNAL_API_URL` in `query_interface/views.py` to point to your working API endpoint.

## 🚀 Deployment

### GitHub Pages (Static Files)
The GitHub Actions workflow automatically deploys static files to GitHub Pages on push to main branch.

### Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
git push heroku main
```

### Vercel/Netlify
Configure for Django deployment with proper build commands.

## 📱 Screenshots

*Add screenshots of your website here*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- 📖 Check the [documentation](documentation/)
- 🐛 Open an [issue](../../issues)
- 💬 Start a [discussion](../../discussions)

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/RA_Lulabs_website&type=Date)](https://star-history.com/#yourusername/RA_Lulabs_website&Date)

---

**Built with ❤️ using Django and modern web technologies**

[![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
