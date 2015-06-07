from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from django.views import generic

from django.utils import timezone
from .models import FileName
from .forms import RentForm, ReturnForm, AddForm

def setup(request):
    #template_name = 'gittracker/index.html'
    #context_object_name = 'all_files'
    list_of_files = FileName.objects.all()
    rentform = RentForm()
    returnform = ReturnForm()
    addform = AddForm()
    return render(request, 'gittracker/index.html', {'rentform': rentform,
						 'returnform': returnform,
						'addform': addform,
						'all_files': list_of_files
									})

def rentFile(request):
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            renter = form.cleaned_data['new_file_holder']
	    if FileName.objects.filter(name=file_name).exists():
	    	f = FileName.objects.get(name=file_name)
	    	if f.checked_out :
			errormessage = 'File is already locked! Please ask the lock holder to return their lock before you edit the document.'
			return render(request, 'gittracker/error.html', {'errormessage': errormessage									})
            	else:
                	f.owner = renter
			f.checked_out = True
			f.time_inserted = timezone.now()
                	f.save()
    return HttpResponseRedirect('/gittracker/')

def addFile(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            file_name = form.cleaned_data['new_file_name']
            renter = form.cleaned_data['file_holder']
	    if FileName.objects.filter(name=file_name).exists():
                errormessage = 'The file already exists!'
                return render(request, 'gittracker/error.html', {'errormessage': errormessage
      })

            else :
                f = FileName(name=file_name, checked_out=True, owner=renter, time_inserted=timezone.now())
                f.save()
    	else:
	    errormessage = 'Did not fill out form correctly'
	    return render(request, 'gittracker/error.html', {'errormessage': errormessage
      })

    return HttpResponseRedirect('/gittracker/')
                                        
def returnFile(request):
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            renter = form.cleaned_data['file_holder']
            if FileName.objects.filter(name=file_name).exists():
                f = FileName.objects.get(name=file_name)
                if f.owner == renter :
		    f.owner = ''
		    f.checked_out = False
		    f.time_inserted = timezone.now()
		    f.save()
                else:
                    errormessage = "Woah! You're trying to return a file that might not be yours. Please make sure you own the file before attempting to release the lock on it. If you need the file, please contact the current person with a lock on it."
                    return render(request, 'gittracker/error.html', {'errormessage': errormessage                                                                   })

    return HttpResponseRedirect('/gittracker/')

