# Mealmate - Online Food Ordering System

Mealmate is a Django-based web application that allows users to register as restaurant owners or customers. Restaurant owners can add, edit, and delete restaurants, while customers can browse menus, place orders, and make payments using Razorpay.

## Features

### **Authentication**
- User registration and login (for both restaurant owners and customers)
- Secure authentication using Django's built-in authentication system

### **Restaurant Management**
- Add new restaurants
- Edit and update restaurant details
- Delete restaurants

### **Menu & Orders**
- Customers can browse menus
- Add items to the cart
- Place orders

### **Payment Integration**
- Razorpay integrated for secure online payments

## Installation & Setup

### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/mealmate.git
cd mealmate
```

### **2. Set Up a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Apply Migrations**
```sh
python manage.py migrate
```

### **5. Create a Superuser**
```sh
python manage.py createsuperuser
```

### **6. Run the Development Server**
```sh
python manage.py runserver
```

Now, open your browser and go to `http://127.0.0.1:8000/`

## Directory Structure
```
mealmate/
│── delivery/
│   │── migrations/
│   │── static/delivary/css
│   │── templates/delivary/
│   │   ├── add_res.html
│   │   ├── base.html
│   │   ├── checkout.html
│   │   ├── cusmenu.html
│   │   ├── customer_home.html
│   │   ├── display_res.html
│   │   ├── failed.html
│   │   ├── index.html
│   │   ├── menu.html
│   │   ├── orders.html
│   │   ├── show_cart.html
│   │   ├── sign_in.html
│   │   ├── sign_up.html
│   │   ├── success.html
│   │   ├── userdata.html
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── tests.py
│   │── views.py
│── manage.py
│── requirements.txt
```

## API Endpoints (If Using Django REST Framework)
| Method | Endpoint | Description |
|--------|----------------|--------------------------------|
| GET | `/restaurants/` | List all restaurants |
| POST | `/restaurants/add/` | Add a new restaurant |
| PUT | `/restaurants/update/<id>/` | Update restaurant details |
| DELETE | `/restaurants/delete/<id>/` | Delete a restaurant |
| GET | `/menu/` | Get menu items |
| POST | `/order/` | Place an order |

## Razorpay Payment Integration
1. Sign up at [Razorpay](https://razorpay.com/)
2. Get API keys from Razorpay Dashboard
3. Add API keys to Django settings:
```python
RAZORPAY_KEY_ID = "your_key_id"
RAZORPAY_KEY_SECRET = "your_key_secret"
```

## Some basic picture as user interface
1. Home page
   ![Screenshot 2025-03-15 144812](https://github.com/user-attachments/assets/766fe4ce-5235-49a7-b8c4-ad6b1c2f1717)
2. If are you new user in my application please sign_up
   ![Screenshot 2025-03-15 145049](https://github.com/user-attachments/assets/77dbe1a8-0589-4df1-9d04-54579d44dcac)
3. Owner of restarent Dashboard interface
   ![Screenshot 2025-03-15 145300](https://github.com/user-attachments/assets/104d2b3f-ae01-44e1-9b1f-c61b146b76bf)
4. Customer Interface
   ![Screenshot 2025-03-15 145611](https://github.com/user-attachments/assets/fed8cdc0-3da7-41c8-857e-fec2f870ca01)
5. Are you like anythis add to your card
   ![Screenshot 2025-03-15 145822](https://github.com/user-attachments/assets/cd9e7b7c-8ef6-4d3a-947c-aca5e7929fe8)
6. After completing your payment
   ![image](https://github.com/user-attachments/assets/240e7b0f-b11e-49c8-82e4-9874d1125eaf)
7. Thankyou for choosing my mealmate application
   ![image](https://github.com/user-attachments/assets/b5234311-7738-4465-953c-21ce306e2ebb)







