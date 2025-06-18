 1. Pull Code from GitHub

git clone https://github.com/yourusername/esamudaay-backend.git

cd esamudaay-backend

2. Set Up Virtual Environment

sudo apt update

sudo apt install python3-pip python3-venv -y

python3 -m venv venv

source venv/bin/activate



3. Install Python Dependencies

pip install -r requirements.txt


4. Apply Migrations

python manage.py makemigrations

python manage.py migrate
