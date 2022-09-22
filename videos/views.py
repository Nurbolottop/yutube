from django.shortcuts import render,redirect
from videos.models import Video

# Create your views here.
def index(request):
    videos = Video.objects.all()
    context = {
        'videos' : videos 
    }
    return render(request, 'index.html', context)



def video_detail(request, id):
    video = Video.objects.get(id = id)
    context = {
        'video' : video,
    }
    return render(request, 'video.html', context)

def create_video(request):
    if request.method =="POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        poster = request.FILES.get('poster')
        videofile = request.FILES.get('videofile')
        video = Video.objects.create(user=request.user,title= title,description = description,poster = poster,video_file = videofile)
        return redirect('video_detail', video.id)

    return render(request, 'create_video.html')
