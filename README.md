# ALX Project Nexus – ProDev Backend Engineering

## 📌 Overview
The **ProDev Backend Engineering Program** is an intensive, project-based learning journey designed to build strong backend development skills.  
This repository documents my **learnings, challenges, implemented solutions, and best practices**, serving as a hub for my backend development growth.

---

## 🚀 Key Learnings

### 🔧 Technologies Covered
- Python  
- Django  
- Django REST Framework (DRF)  
- REST APIs  
- GraphQL  
- Docker  
- Continuous Integration / Continuous Deployment (CI/CD)  

### 🧠 Backend Development Concepts
- **Database Design:** Relational modeling, normalization, query optimization  
- **Asynchronous Programming:** Async views, event loops, concurrency  
- **Caching Strategies:** Redis caching, per-view caching, cache invalidation  
- **API Security:** Authentication, permissions, token-based access  
- **Deployment & DevOps:** Docker, CI/CD pipelines, cloud-ready architectures  

---

## ⚔️ Challenges & Solutions
- **Slow API Responses:** Optimized queries and implemented Redis caching  
- **Docker Environment Conflicts:** Structured Dockerfiles and used Docker Compose  
- **Authentication Complexity:** Implemented DRF token authentication and custom permissions  
- **Scaling API Endpoints:** Used DRF ViewSets, clean URL design, and reusable serializers  

---

## 📘 Best Practices & Personal Takeaways
- Write **modular, clean, and reusable code**  
- Follow **PEP8 and style guidelines**  
- Use **environment variables** for secrets and configuration  
- **Test early and document APIs**  
- Optimize queries to prevent performance issues  
- **Collaborate with frontend developers** for seamless integration  
- Continuously **learn new backend patterns and tools**  

---


---

# 🛒 E-Commerce Backend  
### **ALX ProDev Backend Engineering – Capstone Project**
This repository contains my **E-Commerce Backend System**, developed as part of the **ALX ProDev Backend Engineering** program.  
The goal of this project is to build a **scalable, secure, and fully documented backend API** for managing an online product catalog, user authentication, and product exploration features.

---

## 🔍 Project Overview

The E-Commerce Backend is a real-world simulation of building the backend for a product catalog system. It focuses on:

- Clean API design  
- Security  
- Database optimization  
- Scalability  
- Documentation  

---

## 🎯 Project Goals

### ✔ 1. Build CRUD APIs  
- Products  
- Categories  
- User authentication (JWT)  
- Profiles  

### ✔ 2. Implement Core E-Commerce Logic  
- Filtering  
- Sorting  
- Pagination  
- Efficient DB queries  

### ✔ 3. Database Design  
- PostgreSQL relational schema  
- Indexing  
- Reference integrity (FKs)  

### ✔ 4. Full Swagger Documentation  
- Endpoint examples  
- Request/response schemas  
- Authentication samples  

---

## 🧰 Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Django |
| API | Django REST Framework |
| Auth | JWT |
| Database | PostgreSQL |
| Documentation | Swagger / OpenAPI |
| Version Control | Git & GitHub |


![Status](https://img.shields.io/badge/Project%20Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-0C4B33?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-REST%20Framework-red)
![GitHub](https://img.shields.io/badge/GitHub-Repo-black?logo=github)
![VSCode](https://img.shields.io/badge/Editor-VSCode-blue?logo=visualstudiocode)
![License](https://img.shields.io/badge/License-MIT-green)
![Docs](https://img.shields.io/badge/Docs-Swagger%2FRedoc-orange)


---

## 🗂️ Features

### 🔐 Authentication  
- JWT login & registration  
- Profile management  

### 📦 Product Management  
- CRUD operations  
- Product detail endpoint  

### 🏷 Category Management  
- CRUD operations  
- Category–product filtering  

### 🔎 Search & Discovery  
- Filtering  
- Sorting  
- Pagination  

### 📘 API Documentation  
- Swagger UI  
- OpenAPI schema  

---

## 📡 API Endpoints

<details>
<summary>🛒 Carts</summary>

| Method | Endpoint | Action |
|--------|---------|--------|
| GET    | /carts/cart-items/ | List cart items |
| POST   | /carts/cart-items/ | Create cart item |
| GET    | /carts/cart-items/{id}/ | Retrieve cart item |
| PUT    | /carts/cart-items/{id}/ | Update cart item |
| PATCH  | /carts/cart-items/{id}/ | Partial update cart item |
| DELETE | /carts/cart-items/{id}/ | Delete cart item |
| GET    | /carts/carts/ | List all carts |
| POST   | /carts/carts/ | Create a cart |
| GET    | /carts/carts/{cart_id}/ | Retrieve cart |
| PUT    | /carts/carts/{cart_id}/ | Update cart |
| PATCH  | /carts/carts/{cart_id}/ | Partial update cart |
| DELETE | /carts/carts/{cart_id}/ | Delete cart |

</details>

<details>
<summary>🏷 Categories</summary>

| Method | Endpoint | Action |
|--------|---------|--------|
| GET    | /categories/ | List categories |
| POST   | /categories/ | Create category |
| GET    | /categories/{category_id}/ | Retrieve category |
| PUT    | /categories/{category_id}/ | Update category |
| PATCH  | /categories/{category_id}/ | Partial update category |
| DELETE | /categories/{category_id}/ | Delete category |

</details>

<details>
<summary>📦 Products</summary>

| Method | Endpoint | Action |
|--------|---------|--------|
| GET    | /products/ | List products |
| POST   | /products/ | Create product |
| GET    | /products/{product_id}/ | Retrieve product |
| PUT    | /products/{product_id}/ | Update product |
| PATCH  | /products/{product_id}/ | Partial update product |
| DELETE | /products/{product_id}/ | Delete product |

</details>

<details>
<summary>📝 Orders & Order Items</summary>

**Orders**
| Method | Endpoint | Action |
|--------|---------|--------|
| GET    | /orders/ | List orders |
| POST   | /orders/ | Create order |
| GET    | /orders/{order_id}/ | Retrieve order |
| PUT    | /orders/{order_id}/ | Update order |
| PATCH  | /orders/{order_id}/ | Partial update order |
| DELETE | /orders/{order_id}/ | Delete order |

**Order Items**
| Method | Endpoint | Action |
|--------|---------|--------|
| GET    | /order_items/ | List order items |
| POST   | /order_items/ | Create order item |
| GET    | /order_items/{order_item_id}/ | Retrieve order item |
| PUT    | /order_items/{order_item_id}/ | Update order item |
| PATCH  | /order_items/{order_item_id}/ | Partial update order item |
| DELETE | /order_items/{order_item_id}/ | Delete order item |

</details>

<details>
<summary>⭐ Reviews</summary>

| Method | Endpoint | Action |
|--------|---------|--------|
| GET    | /reviews/ | List reviews |
| POST   | /reviews/ | Create review |
| GET    | /reviews/{review_id}/ | Retrieve review |
| PUT    | /reviews/{review_id}/ | Update review |
| PATCH  | /reviews/{review_id}/ | Partial update review |
| DELETE | /reviews/{review_id}/ | Delete review |

</details>

<details>
<summary>👤 Users</summary>

| Method | Endpoint | Action |
|--------|---------|--------|
| GET    | /users/ | List users |
| POST   | /users/register/ | Register user |
| GET    | /users/profile/ | Retrieve current user profile |
| POST   | /users/token/ | Obtain JWT token |
| POST   | /users/token/refresh/ | Refresh JWT token |
| GET    | /users/{user_id}/ | Retrieve user |
| PUT    | /users/{user_id}/ | Update user |
| PATCH  | /users/{user_id}/ | Partial update user |
| DELETE | /users/{user_id}/ | Delete user |

</details>

**Base URL:** `https://alx-project-nexus-8wjo.onrender.com/api/`  
**Swagger UI:** [Explore API](https://alx-project-nexus-8wjo.onrender.com/swagger/?format=openapi)

---


## 🚀 How to Run Locally

```bash
# Clone repository
git clone https://github.com/<your-username>/alx-project-nexus.git

cd alx-project-nexus

# Virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Migrate
python manage.py migrate

# Run server
python manage.py runserver

