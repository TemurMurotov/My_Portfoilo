# Temurbek | Portfolio Website

Bu — men haqimda ma'lumot beruvchi shaxsiy sayt. Django yordamida yaratilgan.

## Texnologiyalar
- Python
- Django
- HTML/CSS
- SQLite

## Bo'limlar
- **Hero** — tanishtiruv
- **About** — men haqimda
- **Projects** — loyihalarim
- **Contact** — ijtimoiy tarmoq havolalari

## Ishga tushirish

\`\`\`bash
git clone https://github.com/TemurMurotov/My_Portfoilo.git
cd My_Portfoilo
python -m venv venv
venv\Scripts\activate
pip install django pillow
python manage.py migrate
python manage.py runserver
\`\`\`

## API endpointlar
- `/api/projects/` — barcha loyihalar (JSON)
- `/api/projects/<id>/` — bitta loyiha tafsiloti
- `/api/social-links/` — ijtimoiy tarmoq havolalari
