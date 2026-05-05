# Excalibur Orders API

A FastAPI-based microservice for managing orders, built with Python and containerized using Docker.

---

## Features

- Create an order (POST /orders)
- Get all orders (GET /orders)
- Get single order by ID (GET /orders/{id})
- Delete an order (DELETE /orders/{id})
- Interactive API documentation (Swagger UI)

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Docker

---

## Project Structure

backend/
  app/
    main.py
    routes/
      order_routes.py
    schemas/
      order_schema.py
    models/
      order.py
  Dockerfile

---

## ▶️ Run Locally (Without Docker)

cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Open:
http://localhost:8000/docs

---

## Run with Docker

Build image:

docker build -t excalibur-api .

Run container:

docker run -d -p 8000:8000 excalibur-api

Open:
http://localhost:8000/docs

---

## API Endpoints

GET /orders
POST /orders
GET /orders/{order_id}
DELETE /orders/{order_id}

---

## Example Request (POST /orders)

{
  "order_id": 1,
  "order_date": "2026-05-05",
  "amount": 100.0,
  "description": "Sample order"
}

---

## Author

Kuchambi Atud
