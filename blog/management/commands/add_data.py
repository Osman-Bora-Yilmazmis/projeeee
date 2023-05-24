import os
import pandas as pd
from django.core.management.base import BaseCommand
from blog.models import SunCalisanModel, İdariCalisanModel
from sqlalchemy import create_engine
from account.models import CustomUserModel


# python manage.py add_data

class Command(BaseCommand):
    help = "A command to add data from an Excel file to the database"

    def handle(self, *args, **options):
        engine = create_engine('sqlite:///db.sqlite3')
        command_dir = os.path.dirname(os.path.abspath(__file__))
        sun_calisanlar = os.path.join(command_dir, "sun_calisanlar.xlsx")
        df = pd.read_excel(sun_calisanlar)

        df['id'] = range(1, len(df) + 1)

        for _, row in df.iterrows():
            email = row['email']
            password = str(row['sifre'])
            phone_number = row['tel_no']
            first_name = row['isim']
            last_name = row['soyisim']

            try:
                user = CustomUserModel.objects.get(email=email)

            except CustomUserModel.DoesNotExist:

                user = CustomUserModel.objects.create_user(username=email, email=email, password=password, phone_number=phone_number, first_name= first_name, last_name=last_name)

        df.to_sql(SunCalisanModel._meta.db_table, if_exists='replace', con=engine, index=False)


        command_dir1 = os.path.dirname(os.path.abspath(__file__))
        idari_calisanlar = os.path.join(command_dir1, "idari_calisanlar.xlsx")
        df1 = pd.read_excel(idari_calisanlar)

        df1['id'] = range(1, len(df1) + 1)

        for _, row in df1.iterrows():
            email = row['email']
            password = str(row['sifre'])
            phone_number = row['tel_no']
            first_name = row['isim']
            last_name = row['soyisim']
            try:
                user = CustomUserModel.objects.get(email=email)

            except CustomUserModel.DoesNotExist:

                user = CustomUserModel.objects.create_user(username=email, email=email, password=password, phone_number=phone_number, first_name= first_name, last_name=last_name, is_staff=True)



        df1.to_sql(İdariCalisanModel._meta.db_table, if_exists='replace', con=engine, index=False)
