# Django App Runner Deployment Guide

This guide follows the [AWS App Runner documentation](https://aws.amazon.com/blogs/containers/deploy-and-scale-django-applications-on-aws-app-runner/) for deploying Django applications.

## 🚀 **Quick Deploy to AWS App Runner**

### **1. Prerequisites**
- AWS account with App Runner access
- GitHub repository with your Django code
- Python 3.11+ environment

### **2. Files Created for Deployment**
- `apprunner.yaml` - App Runner configuration
- `startup.sh` - Application startup script
- `requirements.txt` - Python dependencies
- Updated `settings.py` - App Runner compatible settings
- `.gitignore` - Proper exclusions for deployment

### **3. Deploy to App Runner**

#### **Step 1: Push to GitHub**
```bash
git add .
git commit -m "Add App Runner deployment files"
git push origin main
```

#### **Step 2: Create App Runner Service**
1. Go to [AWS App Runner Console](https://console.aws.amazon.com/apprunner/)
2. Click **"Create an App Runner service"**
3. Choose **"Source code repository"**
4. Connect to GitHub and select your repository
5. Choose **"Use a configuration file"** (apprunner.yaml)
6. Set service name (e.g., "django-lulabs")
7. Click **"Create & deploy"**

#### **Step 3: Wait for Deployment**
- App Runner will build and deploy your Django app
- Check the **"Events"** tab for deployment status
- Once **"Running"**, your app is live!

### **4. Your App Runner URL**
After successful deployment, you'll get:
```
https://[random-id].us-east-2.awsapprunner.com
```

### **5. Test Your Deployed App**
- **Main page**: `/`
- **Test page**: `/test/`
- **Health check**: `/health/`
- **Query interface**: `/query/`

## 🔧 **Configuration Details**

### **apprunner.yaml**
```yaml
version: 1.0
runtime: python3
build:
  commands:
    build:
      - pip install -r requirements.txt
run:
  runtime-version: 3.11
  command: sh startup.sh
  network:
    port: 8000
```

### **startup.sh**
```bash
#!/bin/bash
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --workers 2 api_website.wsgi:application --bind 0.0.0.0:8000
```

## 📊 **Scaling & Performance**

### **Auto-scaling**
- App Runner automatically scales based on traffic
- Configure min/max instances in console
- Adjust CPU/memory as needed

### **Static Files**
- WhiteNoise serves static files efficiently
- Files collected during startup with `collectstatic`
- Compressed and cached for performance

## 🗄️ **Database Options**

### **Current: SQLite (Development)**
- Works out of the box
- Good for testing and development

### **Future: PostgreSQL (Production)**
- Use Amazon RDS
- Configure via environment variables
- Secure with AWS Secrets Manager

## 🔒 **Security Features**

- HTTPS enabled by default
- Security headers configured
- CORS properly configured
- Environment-based settings

## 📝 **Next Steps**

1. **Deploy to App Runner** using the steps above
2. **Test all endpoints** on the deployed URL
3. **Monitor performance** in App Runner console
4. **Set up custom domain** if needed
5. **Configure database** for production use

## 🆘 **Troubleshooting**

### **Common Issues**
- **Build fails**: Check requirements.txt and Python version
- **Static files not loading**: Verify WhiteNoise configuration
- **Database errors**: Check DATABASE_SECRET environment variable

### **Logs**
- View logs in App Runner console
- Check CloudWatch for detailed logs
- Monitor application events

## 📚 **Resources**

- [AWS App Runner Documentation](https://docs.aws.amazon.com/apprunner/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [WhiteNoise Documentation](https://whitenoise.readthedocs.io/)

---

**Your Django app is now ready for App Runner deployment! 🎉**
