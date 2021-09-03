cd /home/ubuntu/personalsite
source /home/ubuntu/personalsite/personalwebenv/bin/activate
export $(grep -v '^#' .env | xargs)
pip install --upgrade pip
pip install -r requirements.txt
./manage.py migrate