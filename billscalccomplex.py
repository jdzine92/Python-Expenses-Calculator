#################################
## JORDANS EXPENSES CALCULATOR ##
##    CREATED NOV - DEC 2020   ##
#################################

#IMPORT 
import tkinter as tk
from tkinter import messagebox

# -- END OF IMPORT --#

#SET FONTS
xlge_font = ("Calibri", 20)
lge_font = ("Calibri", 16) 
med_font = ("Calibri", 14)

#--- END OF FONTS ---#

class App:
	def __init__(self, main, *args, **kwargs):
		self.main = main
		#non resizable window 
		self.main.resizable(width=False, height=False)

		#CREATE FRAMES
		#LEFT FRAME
		leftFrame = tk.LabelFrame(
		self.main, text='  STEP 1 - INCOME', fg='white', bg='DeepSkyBlue4', labelanchor=tk.NW,
		font=lge_font, width=310, height=325, borderwidth=0, highlightthickness=0)
		leftFrame.grid(row=1, column=0, padx=(5,5), pady=10, ipadx=15, ipady=15, sticky=tk.E)

		#RIGHT FRAME
		rightFrame = tk.LabelFrame(
		self.main, text='  STEP 2 - EXPENSES', fg='white', bg='DeepSkyBlue3', labelanchor=tk.NW,
		font=lge_font, width=310, height=325, borderwidth=0, highlightthickness=0)
		rightFrame.grid(row=1, column=1, padx=(5,5), pady=10, ipadx=15, ipady=15, sticky=tk.W)

		#BOTTOM FRAME
		bottomFrame = tk.LabelFrame(
		self.main, text='  RESULTS', fg='white', bg='DeepSkyBlue2', labelanchor=tk.NW,
		font=lge_font, width=660, height=175, borderwidth=0, highlightthickness=0)
		bottomFrame.grid(
		row=2, column=0, columnspan=2, padx=(5,5), pady=10, ipadx=15, ipady=15, sticky=tk.S)
		#Force frame size
		leftFrame.grid_propagate(False)
		rightFrame.grid_propagate(False)
		bottomFrame.grid_propagate(False)

		#--- END OF FRAMES ---#

		# CURRENCY
		currency_label = tk.Label(
		leftFrame, fg='white', bg='DeepSkyBlue4', text='Select a currency:', font=med_font)
		currency_label.grid(row=1, column=0, padx=(20,0), pady=(15,5), sticky=tk.W)
		#define currency options var
		self.currency_options = tk.StringVar()
		#set default currency value
		self.currency_options.set('£')
		self.currency_entry = tk.OptionMenu(
		leftFrame, self.currency_options, '£', '$')
		self.currency_entry.grid(row=1, column=0, padx=(0,0), pady=(15,5), sticky=tk.E)

		#PERIOD
		period_label = tk.Label(
		leftFrame, fg='white', bg='DeepSkyBlue4', text='Select a period:', font=med_font)
		period_label.grid(row=2, column=0, padx=(20,0), pady=5, sticky=tk.W)
		#define period options var
		self.period_options = tk.StringVar()
		#set default period value
		self.period_options.set('Monthly')
		self.period_entry = tk.OptionMenu(
		leftFrame, self.period_options, 'Weekly', 'Monthly', 'Yearly')
		self.period_entry.grid(row=2, column=0, padx=(120,0), pady=5, sticky=tk.E)

		# INCOME FORM
		job_income_label = tk.Label(
		leftFrame, fg='white', bg='DeepSkyBlue4', text='Job income (After tax):', font=med_font)
		job_income_label.grid(row=3, column=0, padx=(20,0), pady=5, sticky=tk.W)
		self.job_income_entry = tk.Entry(
		leftFrame, width='7', font=med_font) 
		self.job_income_entry.grid(row=3, column=0, padx=(120,0), pady=5, sticky=tk.E)

		pension_income_label = tk.Label(
		leftFrame, fg='white', bg='DeepSkyBlue4', text='Pension income:', font=med_font)
		pension_income_label.grid(row=4, column=0, padx=(20,0), pady=5, sticky=tk.W)
		self.pension_income_entry = tk.Entry(
		leftFrame, width='7', font=med_font) 
		self.pension_income_entry.grid(row=4, column=0, padx=(120,0), pady=5, sticky=tk.E)

		other_income_label = tk.Label(
		leftFrame, fg='white', bg='DeepSkyBlue4', text='Other income:', font=med_font)
		other_income_label.grid(row=5, column=0, padx=(20,0), pady=5, sticky=tk.W)
		self.other_income_entry = tk.Entry(
		leftFrame, width='7', font=med_font) 
		self.other_income_entry.grid(row=5, column=0, padx=(120,0), pady=5, sticky=tk.E)

		#--- END OF INCOME FORM ---#

		#EXPENSES FORM
		mortgage_label = tk.Label(
		rightFrame, fg='white', bg='DeepSkyBlue3', text='Mortgage:', font=med_font)
		mortgage_label.grid(row=1, column=0, padx=(20,0), pady=(15,5), sticky=tk.W)
		self.mortgage_entry = tk.Entry(
		rightFrame, width='7', font=med_font) 
		self.mortgage_entry.grid(row=1, column=1, padx=(0,0), pady=(15,5), sticky=tk.E)

		council_label = tk.Label(
		rightFrame, fg='white', bg='DeepSkyBlue3', text='Council Tax:', font=med_font)
		council_label.grid(row=2, column=0, padx=(20,0), pady=5, sticky=tk.W)
		self.council_entry = tk.Entry(
		rightFrame, width='7', font=med_font) 
		self.council_entry.grid(row=2, column=1, padx=(0,0), sticky=tk.E)

		utility_label = tk.Label(
		rightFrame, fg='white', bg='DeepSkyBlue3', text='Utility Bills:', font=med_font)
		utility_label.grid(row=3, column=0, padx=(20,0), pady=5, sticky=tk.W)
		self.utility_entry = tk.Entry(
		rightFrame, width='7', font=med_font) 
		self.utility_entry.grid(row=3, column=1, padx=(0,0), pady=5, sticky=tk.E)

		internet_label = tk.Label(
		rightFrame, fg='white', bg='DeepSkyBlue3', text='Internet:', font=med_font)
		internet_label.grid(row=4, column=0, padx=(20,0), pady=5, sticky=tk.W)
		self.internet_entry = tk.Entry(
		rightFrame, width='7', font=med_font) 
		self.internet_entry.grid(row=4, column=1, padx=(0,0), pady=5, sticky=tk.E)

		other_label = tk.Label(
		rightFrame, fg='white', bg='DeepSkyBlue3', text='Other Expenses:', font=med_font)
		other_label.grid(row=5, column=0, padx=(20,0), pady=5, sticky=tk.W)
		self.other_entry = tk.Entry(
		rightFrame, width='7', font=med_font) 
		self.other_entry.grid(row=5, column=1, padx=(0,0), pady=5, sticky=tk.E)

		#DISABLE STEP 2 FIELDS (STEP 1 MUST BE FILLED IN FIRST)
		self.mortgage_entry.configure(state=tk.DISABLED)
		self.council_entry.configure(state=tk.DISABLED)
		self.utility_entry.configure(state=tk.DISABLED)
		self.internet_entry.configure(state=tk.DISABLED)
		self.other_entry.configure(state=tk.DISABLED)

		#--- END OF EXPENSES FORM ---#

		# BUTTONS
		self.income_entry_button = tk.Button(
		leftFrame, text='Enter Income >>', command=self.income, fg='white', bg='DeepSkyBlue3',
		font=med_font, borderwidth=0)
		self.income_entry_button.grid(row=6, column=0, pady=(10,0), padx=(150,0), ipadx=10, sticky=tk.E)

		self.calculate_button = tk.Button(
		rightFrame, text='Calculate >>', command=self.calculate, fg='white', bg='DeepSkyBlue4',
		font=med_font, borderwidth=0)
		self.calculate_button.grid(row=6, column=1, pady=(20,0), padx=(20,0), ipadx=10, sticky=tk.E)
		#set as disabled (step 1 must be filled in first)
		self.calculate_button.configure(state=tk.DISABLED)

		'''self.reset_button = tk.Button(self.rightFrame, text='Reset App', command=self.reset, \
		fg='white', bg='black', font=med_font, borderwidth=0)
		self.reset_button.grid(row=7, column=1, pady=(15,15), padx=(0,0), ipadx=10, sticky=tk.E)'''

		#--- END OF BUTTONS ---#

	#INCOME button function
	def income(self):
		#Define income_total as a float
		income_total = tk.DoubleVar()
		#check user entries are int/float not str
		try:
			float(self.job_income_entry.get())
			float(self.pension_income_entry.get())
			float(self.other_income_entry.get())

		#if entry is not an int/float show this error. 
		except ValueError:
			messagebox.showerror('Error!', 'Please enter a numerical value to use the calculator.')

		#statements below to be handled when there are NO exceptions
		else:
			#DISABLE Income button AND income fields
			self.currency_entry.configure(state=tk.DISABLED)
			self.period_entry.configure(state=tk.DISABLED)
			self.job_income_entry.configure(state=tk.DISABLED)
			self.pension_income_entry.configure(state=tk.DISABLED)
			self.other_income_entry.configure(state=tk.DISABLED)
			self.income_entry_button.configure(state=tk.DISABLED)

			#ENABLE STEP 2 FIELDS/BUTTON
			self.mortgage_entry.configure(state=tk.NORMAL)
			self.council_entry.configure(state=tk.NORMAL)
			self.utility_entry.configure(state=tk.NORMAL)
			self.internet_entry.configure(state=tk.NORMAL)
			self.other_entry.configure(state=tk.NORMAL)
			self.calculate_button.configure(state=tk.NORMAL)

			#format user income inputs to 2 decimal places
			a = "{: .2f}".format(float(self.job_income_entry.get()))
			b = "{: .2f}".format(float(self.pension_income_entry.get())) 
			c = "{: .2f}".format(float(self.other_income_entry.get())) 

			#add the 3 results together (keep formatted to 2dp)
			income_total = "{: .2f}".format(float(a) + float(b) + float(c)) 
		
			#define income_total_STR to confirm income as a string
			income_total_STR = tk.StringVar()
			#set value for income_total_STR
			income_total_STR.set \
			(self.period_options.get() +' income of ' + self.currency_options.get() \
			+ (str(income_total)) + ' entered successfully.')
			#show success message label (using data from income_total_STR)
			conf_income_label = tk.Label(
			leftFrame, textvariable= self.income_total_STR, fg='green2', bg='DeepSkyBlue4',
			font=med_font, wraplength=290)
			conf_income_label.grid(row=7, column=0, padx=(20,0), pady=(10,0), sticky=tk.E)

			#--- END OF INCOME BUTTON FUNCTION ---#

	#CALCULATE function for totals
	def calculate(self): 
		#define expenses_total as a float
		self.expenses_total = tk.DoubleVar()

		self.final_calculation = tk.DoubleVar()
		self.final_calculation_green = tk.StringVar()
		self.final_calculation_red = tk.StringVar()

		#check user entries are int/float not str
		try:
			float(self.mortgage_entry.get())
			float(self.council_entry.get())
			float(self.utility_entry.get())
			float(self.internet_entry.get())
			float(self.other_entry.get())

		#if entry is not an int/float show this error. 
		except ValueError:
			messagebox.showerror('Error!', 'Please enter a numerical value to use the calculator.')

		#Statements below to be handled when there are NO exceptions
		else: 
			#DISABLE calculate button and fields
			self.calculate_button.configure(state=tk.DISABLED)
			self.mortgage_entry.configure(state=tk.DISABLED)
			self.council_entry.configure(state=tk.DISABLED)
			self.utility_entry.configure(state=tk.DISABLED)
			self.internet_entry.configure(state=tk.DISABLED)
			self.other_entry.configure(state=tk.DISABLED)

			#format user expenses inputs to 2 decimal places
			a = "{: .2f}".format(float(self.mortgage_entry.get()))
			b = "{: .2f}".format(float(self.council_entry.get())) 
			c = "{: .2f}".format(float(self.utility_entry.get())) 
			d = "{: .2f}".format(float(self.internet_entry.get())) 
			e = "{: .2f}".format(float(self.other_entry.get()))

			#add  the 5 results together (keep formatted to 2dp)
			self.expenses_total = "{: .2f}".format(float(a) + float(b) + float(c) + float(d) + float(e))

			#define income_results_STR to confirm income as a string
			income_results_STR = tk.StringVar()
			#set value for income_results_STR
			income_results_STR.set \
			("Your " + self.period_options.get() +' income is ' + self.currency_options.get() \
			+ (str(income_total)))
			#show income results message label (using data from income_results_STR)
			income_results_label = tk.Label(
			bottomFrame, textvariable=income_results_STR, fg='white', bg='DeepSkyBlue2', font=xlge_font)
			income_results_label.grid(row=1, column=0, padx=(20,0), pady=(10,0), sticky=tk.NSEW)

			#define expenses_results_STR to confirm income as a string
			self.expenses_results_STR = tk.StringVar()
			#set value for expenses_results_STR
			self.expenses_results_STR.set \
			("Your " + self.period_options.get() +' expenditure is ' + self.currency_options.get() \
			+ (str(self.expenses_total)))
			#show expenses results message label (using data from expenses_results_STR)
			self.expenses_results_label = tk.Label(self.bottomFrame, textvariable= self.expenses_results_STR,\
			fg='white', bg='DeepSkyBlue2', font=xlge_font)
			self.expenses_results_label.grid(row=2, column=0, padx=(20,0), pady=(10,0), sticky=tk.NSEW)

	
			#final calculation as float
			self.f = "{: .2f}".format(float(self.income_total))
			self.g = "{: .2f}".format(float(self.expenses_total))

			self.final_calculation = "{: .2f}".format(float(self.f) - float(self.g))

			#final afford calculation as string
			self.final_calculation_green.set( \
			'You can afford this, with ' + self.currency_options.get() + self.final_calculation \
			 + ' to spare each ' + self.period_options.get() + ' period.')

			#final cant afford calculation as string
			self.final_calculation_red.set( \
			"You can't afford this, you will be " + self.currency_options.get() + \
			self.final_calculation + ' short each ' + self.period_options.get() + ' period.')

			#compare income against expenses, show relevant message
			if self.income_total < self.expenses_total:
				self.cant_afford_label = tk.Label(self.bottomFrame, textvariable=self.final_calculation_red, \
				fg='red3', bg='DeepSkyBlue2', font=xlge_font, wraplength=450)
				self.cant_afford_label.grid(row=3, column=0, padx=(20,0), sticky=tk.S)
			else:
				self.afford_label = tk.Label(self.bottomFrame, \
				textvariable=self.final_calculation_green, fg='green4', \
				bg='DeepSkyBlue2', font=xlge_font, wraplength=450)
				self.afford_label.grid(row=3, column=0, padx=(20,0), sticky=tk.S)



			'''convert between weekly / monthly / yearly figures
			self.income_converison.set( \
				)
			if self.period_options.get() == 'Monthly': 
				self.income_total.get() * 12 / 52 = self.income_total_weekly
				self.income_total.get() * 12 = self.income_total_yearly

			elif self.period_options.get() == 'Weekly':



			self.expenses_conversion.set( \
				) '''

				#--- END OF CALCULATE FUNCTION ---#

	#RESET ALL FUNCTION
	def reset(self):
		#re enable fields prior to deleting
		self.currency_entry.configure(state=tk.NORMAL)
		self.job_income_entry.configure(state=tk.NORMAL)
		self.pension_income_entry.configure(state=tk.NORMAL)
		self.other_income_entry.configure(state=tk.NORMAL)

		self.mortgage_entry.configure(state=tk.NORMAL)
		self.council_entry.configure(state=tk.NORMAL)
		self.utility_entry.configure(state=tk.NORMAL)
		self.internet_entry.configure(state=tk.NORMAL)
		self.other_entry.configure(state=tk.NORMAL)

		#enable buttons (return to state NORMAL)
		self.currency_button.configure(state=tk.NORMAL)
		self.income_entry_button.configure(state=tk.NORMAL)
		self.calculate_button.configure(state=tk.NORMAL)

		#clear income fields
		self.job_income_entry.delete(0, tk.END)
		self.pension_income_entry.delete(0, tk.END)
		self.other_income_entry.delete(0, tk.END)

		#clear expense fields (use delete - do not want to destroy altogether)
		self.currency_entry.delete(0, tk.END)
		self.mortgage_entry.delete(0, tk.END)
		self.council_entry.delete(0, tk.END)
		self.utility_entry.delete(0, tk.END)
		self.internet_entry.delete(0, tk.END)
		self.other_entry.delete(0, tk.END)

		if self.conf_currency_label is not None: 
			self.conf_currency_label.grid_remove()
		else:
			pass

		if self.conf_income_label is not None:
			self.conf_income_label.grid_remove()
		else:
			pass

		if self.inc_total_label is not None:
			self.inc_total_label.grid_remove()
		else:
			pass

		if self.exp_total_label is not None:
			self.exp_total_label.grid_remove()
		else:
			pass

		if self.cant_afford_label is not None:
			self.cant_afford_label.grid_remove()
		else:
			pass

		if self.afford_label is not None:
			self.afford_label.grid_remove()
		else:
			pass

		#--- END OF RESET ALL FUNCTION ---#

#RUN MAINLOOP		
def main(): 
	root = tk.Tk()
	#declare the class App
	app = App(root)
	#declare title attributes
	title = "Jordan's Expenses Calculator 2020 "
	version = "2.1"

	#root config 
	root.geometry('700x800')
	root.title(title + ' Version: ' + version)
	root.config(bg='white')

	#logo for top of app
	logo = tk.PhotoImage(file = 'expensescalc.png')
	logo_label = tk.Label(root, image=logo, borderwidth=0, highlightthickness=0)
	logo_label.grid(row=0, column=0, columnspan=2)
	

	tk.mainloop()

#run main if being run as standalone
if __name__ == '__main__':
	main()

#--- END OF MAINLOOP ---#





