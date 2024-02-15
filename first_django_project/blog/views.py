from django.shortcuts import render

posts = [
    {
        'author':'Nicolas S',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '13 February, 2024'
    },
    {
        'author':'Nicolas S',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '14 February, 2024'
    },
]

def home(request):
    context={
        'posts_context':posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
