# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskCreate
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.embed import components
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
from plotly.graph_objs import Scatter

from tkinter import Tk, filedialog
from tkinter import messagebox as mb
import csv, io
from django.contrib import messages

#method immplimentation of saving data to database,retriving data from database and plot a graph
def index(request):
	shelf = Task.objects.all()[:50]
	return render(request, 'task/data.html', {'shelf': shelf})

def upload(request):
	upload = TaskCreate()
	if request.method == 'POST':
		upload = TaskCreate(request.POST, request.FILES)
		if upload.is_valid():
			upload.save()
			return redirect('index')
		else:
			return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
	else:
		return render(request, 'task/upload_form.html', {'upload_form':upload})

def upload1(request):
	'''root = Tk() # pointing root to Tk() to use it as Tk() in program.
	root.withdraw() # Hides small tkinter window.
	root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
	open_file = filedialog.askopenfilename(filetypes=[("Excel files", ".csv ")])# Returns opened path as str
	#print(open_file) 
	df = pd.read_csv(open_file)'''

	df = pd.read_csv('Book1.csv')	
	plot_div = plot([go.Scatter(x=df['Date'], y=df['Close'],mode='lines', name='Date Vs Close',opacity=1.0, marker_color='green')],output_type='div')
	#script, div = components(fig)
 
	return render(request, 'task/graph_view.html', context={'plot_div': plot_div})

def upload2(request):
	root = Tk() # pointing root to Tk() to use it as Tk() in program.
	root.withdraw() # Hides small tkinter window.
	root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
	open_file = filedialog.askopenfilename(filetypes=[("Excel files", ".csv ")])# Returns opened path as str
	#print(open_file) 
	if open_file == '':
		shelf = Task.objects.all()
		return render(request, 'task/data.html', {'shelf': shelf})
	else:
		df = pd.read_csv(open_file)
	plot_div = plot([go.Scatter(x=df['Date'], y=df['Close'],mode='lines',name='Date Vs Close',opacity=1.0, marker_color='green')],output_type='div')
	#script, div = components(fig)
 
	return render(request, 'task/file_view.html', context={'plot_div': plot_div})

def csv_data_upload(request):
    # declaring template
    #template = "csv_upload.html"
	data=Task.objects.all()
	# prompt 
	prompt = {
        'order': 'Select Your CSV File From Your Device Storage !!',
		'CSVDATA': data    
    }
    # GET request 
	if request.method == "GET":
		return render(request, 'task/csv_upload.html', prompt)
	csv_file = request.FILES['file']
    # let's check if it is a csv file
	if not csv_file.name.endswith('.csv'):
		#mb.showerror("Answer", "Sorry, no answer available")
		messages.error(request, 'THIS IS NOT A CSV FILE')
		return render(request, 'task/csv_upload.html', context={})
	data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		created = Task.objects.update_or_create(Date1=column[0],Open=column[1],High=column[2],Low=column[3],Close=column[4],WAP=column[5],No_Of_Shares=column[6],No_Of_Trades=column[7],Total_Turnover=column[8],Deliverable=column[9],Per_Of_Del_Qty_To_Trd_Qty=column[10],Spread_H_L=column[11],Spread_C_O=column[12])
	context = {}
	return render(request, 'task/csv_upload.html', context)