from django.shortcuts import render, get_object_or_404
from .models import Entry


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blog/entry.html', {'entry': entry})
