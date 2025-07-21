# SnapGrub Backend

A modern restaurant ordering system backend built with **FastAPI**, **PostgreSQL**, and **Redis**. SnapGrub provides a scalable solution for restaurant management and food ordering with real-time capabilities.

---

## 🚀 Features

- 🔐 **Authentication & Authorization**: Secure user registration and login  
- 📋 **Menu Management**: CRUD operations for restaurant menus and items  
- 🧾 **Order Processing**: Real-time order tracking and updates  
- 💬 **Feedback System**: Customer feedback collection and handling  
- 💳 **Subscription Management**: SaaS-style subscription support  
- 🏢 **Multi-tenant Support**: Isolated data per restaurant  
- 🔄 **Real-time Updates**: Redis-powered pub/sub notifications  

---

## 📌 API Endpoints

All routes are prefixed with `/api/v1`

| Module         | Path Prefix      | Description                            |
|----------------|------------------|----------------------------------------|
| Authentication | `/auth`          | User login, registration, tokens       |
| Menu           | `/menu`          | Restaurant menu and item management    |
| Orders         | `/orders`        | Order placement and tracking           |
| Feedback       | `/feedback`      | Customer feedback endpoints            |
| Subscriptions  | `/subscriptions` | Plan handling and billing management   |
| Tenants        | `/tenants`       | Tenant onboarding and isolation        |

---

## 📦 Prerequisites

- Python 3.9+  
- Docker + Docker Compose  
- PostgreSQL  
- Redis  

---

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-org/snapgrub.git
   cd snapgrub/backend
   ```

2. **Configure Environment Variables**
   ```bash
   cp .env.example .env
   # Edit `.env` as needed
   ```

3. **Build & Start Services**
   ```bash
   docker compose up -d --build
   ```

4. **To Stop Services**
   ```bash
   docker compose down
   ```

---

## 🧭 Project Structure

```
backend/
├── app/
│   ├── api/              # API routers
│   ├── core/             # Settings, security, utils
│   ├── events/           # Startup/shutdown event handlers
│   └── main.py           # FastAPI app entrypoint
├── .env                  # Local environment config
├── .env.example          # Sample env config
├── Dockerfile            # Docker build instructions
├── docker-compose.yml    # Compose setup for services
└── requirements.txt      # Python dependencies
```

---

## ⚙️ Environment Variables

Set the following in your `.env` file:

```env
# Backend
BACKEND_PORT=8000
TIMEZONE=Asia/Manila
DEBUG=True
SECRET_KEY=your_secret_key_here

# PostgreSQL
POSTGRES_DB=snapgrub
POSTGRES_USER=admin
POSTGRES_PASSWORD=password
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432

# Redis
REDIS_HOST=redis
REDIS_PORT=6379
```

---

## 🤝 Contributing

1. Fork the repository  
2. Create your feature branch: `git checkout -b feature/your-feature`  
3. Commit your changes: `git commit -m 'Add your feature'`  
4. Push to the branch: `git push origin feature/your-feature`  
5. Open a Pull Request  