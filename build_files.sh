
echo "BUILD START"
python3.12 -m pip install requirements.txt
python3.12 manage.py collectstatic --noinput --clear
echo "BUILD END"
