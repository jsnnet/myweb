from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from board.models import Board
# Create your views here.



def home(request):
    return render(request, "board/index.html")

def upload(request):
    return render(request, "board/upload.html")

@csrf_exempt
def add(request):
    add_up = Board(pwd=request.POST['pwd'],
                   writer=request.POST['writer'],
                   subject=request.POST['subject'],
                   content=request.POST['content'])

    add_up.save()
    return redirect('/board')

def view(request):
    no_idv = request.GET['no_idx']
    add_up = Board.objects.get(no_idx=no_idv)
    return render(request, 'board/view.html', {'add_up': add_up})
