from rest_framework import serailizars
from .models import Todilist

class TodilistSerailizer(serailizars.ModelSerailizer):
    class Meta:
        model = Todilist
        fields = ('id','title','detail')#'__all__ 'เอาทั้งหมด