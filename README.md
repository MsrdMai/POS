# POS ( Point of sale)

##Framework : Django
[![1-4-QDbb-e-O98w-IB32-CNNu-Wjw.png](https://i.postimg.cc/8P8jMDdm/1-4-QDbb-e-O98w-IB32-CNNu-Wjw.png)](https://postimg.cc/3WB8Qsck)



ความสามารถของระบบ:
1. หน้า Log In
2. หน้าแรก
- สําหรับบันทึกข้อมูลการขาย
- แสดงรายการสินค้าทังหมดทีมีในร้าน
- มีFilter ในการค้นหาสินค้า จากชือสินค้า หรือประเภทสินค้า
- แสดงสินค้าในตะกร้าสินค้า
- สามารถเพิมสินค้าเข้าตะกร้าได้
- สามารถลบสินค้าเข้าตะกร้าได้
- แสดงราคารวมของสินค้าในตะกร้า
- มีปุมสําหรับบันทึกการขาย

3. หน้าจัดการสินค้า - สําหรับเพิม/ลบ/แก้ไขสินค้า และประเภทสินค้า
- แสดงรายการสินค้าทังหมดทีมีในร้าน
- มีFilter ในการค้นหาสินค้า จากชือสินค้า หรือประเภทสินค้า
- มีปุมสําหรับเพิมสินค้าใหม่
- มีปุมสําหรับลบ/แก้ไขสินค้าแต่ละชนิด
- มีปุมสําหรับเพิมประเภทสินค้าใหม่
- มีปุมสําหรับลบ/แก้ไขประเภทสินค้าแต่ละชนิด

4. หน้าแสดงยอดขาย
- สามารถดูรายได้ทังหมดทีขายได้ตาม วัน หรือ สัปดาห์หรือ เดือน หรือ ป

Usecase :
[![108947.jpg](https://i.postimg.cc/59KDRNK8/108947.jpg)](https://postimg.cc/Z03f9ZSq)

Database :
[![108946.jpg](https://i.postimg.cc/ZY9hZddw/108946.jpg)](https://postimg.cc/DmKNPm5G)



Develop : Sirilada Sonsomboon

Note : setting Django
.\env\Scripts\activate
python manage.py createsuperuser
python -m venv env
python -m pip install django
django-admin startproject (myweb)(สร้างชื่อโฟเดอร์)
python manage.py runserver 127.0.0.1:8080
python manage.py startapp (authen) 
python -m pip install --upgrade pip
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate management 0001
 python manage.py shell

