from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.request import Response
from rest_framework.decorators import api_view #สามารถget post ได้
from rest_framework import status
from serializers import TodilistSerailizer
from .models import Todilist

#-------------------get data -------------------- 
@api_view(['GET'])
def all_todilist(request):
    all_todilist = Todilist.objects.all() #ดึ้งข้อมมูลจากโมเดลtodolist
    serializers = TodilistSerailizer(alltodilist,many=True) #ดึงตัวด้านบนมา ต้องบอกว่าว่า ข้อมูที่ส่งไปมากกว่า1 ถ้ามีข้อมูล1 ไม่ต้องใส่many =true
    return Response(serializers.data,status =status.HTTP_200_OK)#โค้ดที่ส่งไปเป็นstatusเลขเท่าไหร่

data =[
    {
        "title":"เเลบท็อปคืออะไร",
        "subtitle":"อุปกรณที่ใช้สำหรับคำนวนเเละทำงานอื่นๆ",
        "image_url":"https://raw.githubusercontent.com/zawaneemakeng/FlutterAPI/main/laptop.jpg",
        "detail":"อุปกรณที่ใช้สำหรับคำนวนเเละทำงานอื่นๆ"
    },
    {
        "title":"Flutter คือ",
        "subtitle":"อุปกรณที่ใช้สำหรับคำนวนเเละทำงานอื่นๆ",
        "image_url":"https://raw.githubusercontent.com/zawaneemakeng/FlutterAPI/main/flutter.jpg",
        "detail":"ใช้สร้าง UI สำหรับ mobile application ที่สามารถทำงานข้ามแพลตฟอร์มได้ทั้ง iOS และ Android ในเวลาเดียวกัน โดยภาษาที่ใช้ใน Flutter นั้นจะเป็นภาษา dart ซึ่งถูกพัฒนาโดย Google"
    },
    {
        "title":"python คือ",
        "subtitle":"อุปกรณที่ใช้สำหรับคำนวนเเละทำงานอื่นๆ",
        "image_url":"https://raw.githubusercontent.com/zawaneemakeng/FlutterAPI/main/laptop.jpg",
        "detail":"อุปกรณที่ใช้สำหรับคำนวนเเละทำงานอื่นๆ"
    }
]

def Home(request):
    return JsonResponse(data = data,safe = False,json_dumps_params={'ensure_ascii':False})
