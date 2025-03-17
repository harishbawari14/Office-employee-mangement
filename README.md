Office Employee Management System
A web-based application to manage employees, including adding, removing, filtering, and viewing employee details.

🛠 Features
Add new employees
Remove employees
Filter employees based on criteria
View all employee details
⚙️ Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS
Database: SQLite
🚀 Installation Guide
1. Clone the Repository
sh
Copy
Edit
git clone https://github.com/harishbawari14/Office-employee-mangement.git
cd Office-employee-mangement
2. Create a Virtual Environment (Optional but Recommended)
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3. Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4. Apply Migrations
sh
Copy
Edit
python manage.py migrate
5. Run the Development Server
sh
Copy
Edit
python manage.py runserver
Now, open http://127.0.0.1:8000/ in your browser.

📂 Project Structure
bash
Copy
Edit
Office-employee-mangement/
│── Project/                 # Main Django project settings  
│── emp_app/                 # Employee management app  
│── emp_app/migrations/       # Database migrations  
│── emp_app/templates/        # HTML Templates  
│── manage.py                 # Django management script  
│── db.sqlite3                # SQLite Database  
│── README.md                 # Project documentation  

📝 Future Enhancements
Add authentication for admin users
Export employee data as CSV
Improve UI with Bootstrap or React
