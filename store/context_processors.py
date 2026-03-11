from .models import ShopInfo

def shop_context(request):
    #ດືງຂໍ້ມູນຮ້ານຂາຍ ແລະ ສົ່ງໄປໃນ context
    shop = ShopInfo.objects.first()
    return {'shop': shop}