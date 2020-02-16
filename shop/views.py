from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from shop.models import Product
# Create your views here.

def product_list(request):
    #상품의 갯수
    count = Product.objects.count()
    productList = Product.objects.order_by("-product_id")

    # 사진 깨진 것 때문에 사진 파일명을 출력 해보았다
    for e in productList:
        print(e.picture_url)

    return render(request,"shop/product_list.html",{"productList":productList,"count":count})

def product_write(request):
    return render(request, "shop/product_write.html")

UPLOAD_DIR = "/home/bigdata/PycharmProjects/myweb/shop/static/images/"
@csrf_exempt
def product_insert(request):
    # 첨부파일이 있는 경우
    if "file1" in request.FILES: # 업로드 된 파일을 복사처리
        file = request.FILES["file1"]
        file_name = file._name # 첨부파일 이름
        # 파일 오픈 (wb: write binary)
        fp = open("%s%s"%(UPLOAD_DIR, file_name), "wb")
        # 파일을 1 파이트씩 조금씩 읽어서 저장
        for chunk in file.chunks():
            fp.write(chunk)
        #파일 닫기
        fp.close()
    else:
        file_name = "-"
        #Database 처리
    dto = Product(product_name=request.POST["product_name"],
                  description=request.POST["description"],
                  price=request.POST["price"],
                  picture_url=file_name
                  )
    #레코드를 저장함
    dto.save()
    #상품 목록으로 이동함
    return redirect("product_list")

def product_detail(request):
    productDetail = Product.objects.order_by("-product_id")
    return render(request,"shop/product_detail.html",{"productDetail":productDetail})