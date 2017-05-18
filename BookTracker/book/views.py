from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
 
from book.models import books
from .forms import BookForm
from .forms import SearchForm
from .forms import DeleteForm
from .forms import UpdateForm
  
def home(request):
    entries = books.objects.all()[:10]
    return render_to_response('index.html', {'books' : entries})

def book_new(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			book = form.save(commit=False)
			books.objects.filter(title = book.title).delete()
			book.save()			
			return render(request, 'success_update.html')
	else:
		form = BookForm()
	return render(request, 'book_edit.html', {'form': form})

def book_list(request):
	entries = books.objects.all()
	for book in entries:
		print book.title
	return render(request, 'book_list.html', {'books' : entries})



def book_delete(request):
	if request.method == "POST":
		form = DeleteForm(request.POST)
		if form.is_valid():
			book = form.save(commit=False)
			books.objects.filter(title = book.title).delete()			
			return render(request, 'success_delete.html')
	else:
		form = DeleteForm()
	return render(request, 'book_delete.html', {'form': form})

def book_update(request):
	if request.method == "POST":
		form = UpdateForm(request.POST)
		if form.is_valid():
			book = form.save(commit=False)
			books.objects.filter(title = book.title).delete()
			book.save()			
			return render(request, 'success_update.html')
	else:
		form = UpdateForm()
	return render(request, 'book_update.html', {'form': form})

def book_search(request):
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			book = form.save(commit=False)
			entries = books.objects.filter(title = book.title)		
			return render(request, 'book_list.html', {'books' : entries})
	else:
		form = SearchForm()
	return render(request, 'book_search.html', {'form': form})