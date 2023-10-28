from django.shortcuts import render
from django.http import HttpResponse
from .forms import TexttoHtmlForm
import markdown
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TexttoHtmlForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            html = markdown.markdown(text)
            return render (request, 'htmlapp/result.html' , {'html':html})
    else:
            form = TexttoHtmlForm()
    return render(request , 'htmlapp/convert.html' , {'form':form})