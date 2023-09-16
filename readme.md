
# Milliy Gvardiya Transport Tizimi

### Ishga tushurish ketma ketligi

1. Kerakli kutubxonalar o'rnatib olish kerak!
    ```
        pip install -r requirements.txt      
    ```
2. Ishga tushurishdan avval `core` va `common` applarida `migrations/__init__.py` papkasi va fayli borligini tekshirib oling!!
3. 2chi qism bajrarib bo'lingach migratsiya qilib olish kerak bo'ladi.
    ```
       python manage.py makemigrations && python manage.py migrate
    ```
    

4. Ishga tushurish uchun default ma'lumotlarni yuklab olish zarur
    ```
        python manage.py load_regions
   ```
5. Ma'lumotlar Yuklab olingach ishlatish uchun admin user yaratiladi
   ```commandline
      python manage.py createsuperuser
   ``` 
   diqqat bu qismda sizdan 4ta ma'lumot so'raladi
   1. username
   2. user type - (1-Super Admin, 2-Admin) # default 1ni bosib keting
   3. region_id # default 1ni bosib keting
   4. password

6. Ketma ketlik tugagach endi run berib ishlatishingiz mumkin :)
   ```commandline
      python manage.py runserver
   ```
   

#### Biror muommo bo'lganda yoki o'zgartirish kiritishdan avval [Xudoyberdi](https://t.me/xudikk)  bn bog'laning