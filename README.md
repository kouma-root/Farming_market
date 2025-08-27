# Farming Market

## Overview

**Farming Market** is a backend Django project designed to connect farmers and buyers in a digital marketplace. The platform streamlines the process of listing agricultural products, managing requests, and automating inventory and order status updates. It aims to empower farmers by providing them with a simple tool to manage their products and sales, while giving buyers an easy way to request and purchase farm produce.

---

## Problem Statement

Smallholder farmers often lack access to efficient digital tools for managing their inventory and connecting with buyers. Manual tracking of product quantities, order statuses, and communication can lead to errors, lost sales, and inefficiencies. **Farming Market** solves these problems by providing:

- A centralized platform for product listing and management.
- Automated inventory and status updates.
- Streamlined request and approval workflows.
- Role-based access for farmers and buyers.

---

## Features

### User Management
- **Registration & Authentication:** Secure signup and login for both farmers and buyers.
- **Role-based Access:** Farmers and buyers have different dashboards and permissions.

### Product Management (Farmers)
- **Add/Edit/Delete Products:** Farmers can manage their product listings, including images and descriptions.
- **Automatic Status Updates:** Product status (e.g., Available, Out of Stock) updates automatically based on quantity.
- **Image Uploads:** Products can have thumbnail images.

### Request Management (Buyers)
- **Create Requests:** Buyers can request products from farmers.
- **View Requests:** Buyers can track the status of their requests.

### Request Management (Farmers)
- **View Incoming Requests:** Farmers see all requests for their products.
- **Approve/Reject/Cancel Requests:** Farmers can manage requests, which automatically updates product quantities and statuses.

### Automation & Signals
- **Django Signals:** Automatic updates of product status and quantity when requests are approved or cancelled.
- **Inventory Integrity:** Prevents overselling by checking available quantity before approval.

### Dashboards
- **Farmer Dashboard:** Shows product stats, recent requests, and inventory status.
- **Buyer Dashboard:** Shows request history and statuses.

### Security
- **Permissions:** Only authenticated users can access features; role checks for sensitive actions.
- **Data Integrity:** Prevents unauthorized actions on products and requests.

---

## Technologies Used

- **Backend:** Django (Python)
- **Database:** SQLite (default, can be swapped for PostgreSQL/MySQL)
- **Authentication:** Django built-in auth
- **Image Handling:** Django ImageField with Pillow
- **Frontend:** Django Templates (for demonstration)

---

## Project Structure

```
Farming_market/
├── Product/
│   ├── models.py
│   ├── views.py
│   └── templates/
├── Request/
│   ├── models.py
│   ├── views.py
│   └── templates/
├── Users/
│   ├── models.py
│   ├── views.py
│   └── templates/
├── Farming_market/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── manage.py
```

---

## How to Run

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd Farming_market
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

4. **Create a superuser (optional):**
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the app:**
    - Visit `http://127.0.0.1:8000/` in your browser.

---

## API Endpoints & URLs

- `/register/` — User registration
- `/login/` — User login
- `/products/` — List all products
- `/product/<slug>/` — Product detail
- `/request/create/<product_id>/` — Create a request for a product
- `/farmer/dashboard/` — Farmer dashboard
- `/buyer/dashboard/` — Buyer dashboard

---

## Best Practices & Highlights

- **Django Signals** for business logic automation.
- **Role-based decorators** for view protection.
- **Atomic updates** to prevent race conditions.
- **Clean separation** of concerns (Users, Products, Requests).
- **Extensible** for future features (e.g., notifications, payments).

---

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License.

---

## Authors

- [Your Name]
- ALX Capstone Project Team