from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from address.models import Address

# Create your views here.
def home(request):
    # 보통 때면 connection, cursor, sql문 작성하고 보내는 작업했었어야 하는데
    # 아래의 문구가 connection, cursor : Address.objects 하면 데이터베이스 접근 객체가 생성된다
    # order_by 정렬
    # 내림차순으로 가져와야 한다?
    # order_by('[부호]컬럼') => - : 내림차순, 기본은 오름차순
    items = Address.objects.order_by('-idx')
    # ResultSet 에 해당되는 <QuerySet =>
    #print("items",items)
    #print("type",type(items))
    # 테이블의 레코드 총 갯수 => select count(*) cnt from address_address
    address_count = Address.objects.all().count()
    return render(request, "address/index.html", {'items':items, 'address_count':address_count}) # 이 home 이 index 가 되면 안된다? 그래서 바꿔줘야 한다

# 입력폼 만들기
def write(request):
    return render(request, "address/write.html")

# 입력 처리
@csrf_exempt # csrf 공격 막는
def insert(request):
    # Post 방식을 request.POST('파라미터'), request.GET('파라미터')
    addr = Address(name=request.POST['name'],
                   tel=request.POST['tel'],
                   email=request.POST['email'],
                   address=request.POST['address'])

    #입력 처리
    addr.save()
    return redirect('/address') #import 하겠냐고 나온다 (왼쪽에 빨간 전구모양 나오면 Alt+Entr 눌러서 import 해주기)

# detail 페이지
# GET 방식으로 idx 가 넘어온다
def detail(request):
    idv = request.GET['idx']
    # address_address 테이블의 레코드 중에서 idx 값으로 조회
    # select * from address_address where idx=idv
    addr = Address.objects.get(idx=idv)
    return render(request, 'address/detail.html', {'addr':addr}) # addr 는 한 row 데이터 값의 키값

@csrf_exempt
def update(request):
    id = request.POST["idx"]
    #수정 처리
    addr = Address(idx=id, name=request.POST['name'],
                   tel=request.POST['tel'],
                   email=request.POST['email'],
                   address=request.POST['address'])
    addr.save()
    return redirect('/address')

def delete(request):
    id = request.POST["idx"]
    #삭제 처리 delete()
    # delete from address_address where idx = id
    Address.objects.get(idx=id).delete()
    return redirect('/address')

def chart2(request):
    return render(request,'address/chart2.html')

def chart3(request):
    return render(request,'address/chart3.html')