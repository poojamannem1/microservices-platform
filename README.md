# 🚀 Microservices Platform with API Gateway

This project is a **Dockerized Microservices Architecture** built using:

* ⚡ FastAPI (Python)
* 🐳 Docker & Docker Compose
* 🌐 Nginx (API Gateway)

---

## 📌 Architecture

```
Client → Nginx Gateway → Services
                        ├── Auth Service
                        ├── User Service
                        └── Order Service
```

---

## 🧩 Services

### 🔐 Auth Service

* User login
* Authentication handling

### 👤 User Service

* Create users
* Manage user data

### 📦 Order Service

* Create orders
* Manage order details

---

## 🌐 API Gateway (Nginx)

Routes requests:

| Endpoint   | Service       |
| ---------- | ------------- |
| `/auth/`   | Auth Service  |
| `/users/`  | User Service  |
| `/orders/` | Order Service |

---

## ⚙️ Tech Stack

* FastAPI
* Docker
* Nginx
* Python 3.10+

---

## 🚀 Getting Started

### 1️⃣ Clone Repo

```
git clone https://github.com/YOUR_USERNAME/microservices-platform.git
cd microservices-platform
```

---

### 2️⃣ Run with Docker

```
docker-compose up --build
```

---

### 3️⃣ Access Services

| Service | URL                          |
| ------- | ---------------------------- |
| Gateway | http://localhost:8080        |
| Auth    | http://localhost:8080/auth   |
| Users   | http://localhost:8080/users  |
| Orders  | http://localhost:8080/orders |

---

## 🧪 API Testing

### Create User

```
curl -X POST http://localhost:8080/users/ \
-H "Content-Type: application/json" \
-d '{"email":"test@test.com","password":"1234"}'
```

---

### Login

```
curl -X POST http://localhost:8080/auth/login \
-H "Content-Type: application/json" \
-d '{"email":"test@test.com","password":"1234"}'
```

---

### Create Order

```
curl -X POST http://localhost:8080/orders/ \
-H "Content-Type: application/json" \
-d '{"id":1,"user_id":101,"product_name":"Laptop","quantity":2}'
```

---

## 📂 Project Structure

```
microservices-platform/
│
├── gateway/          # Nginx API Gateway
├── auth-service/     # Authentication service
├── user-service/     # User management
├── order-service/    # Order management
├── docker-compose.yml
└── README.md
```

---

## 🔥 Future Improvements

* ✅ JWT Authentication
* ✅ PostgreSQL integration
* ✅ Service-to-service communication
* ✅ Kubernetes deployment
* ✅ CI/CD pipeline

---

## 👩‍💻 Author

Your Name

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
