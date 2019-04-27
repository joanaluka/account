class Account:
	def __init__ (self,first_name,last_name):
		self.first_name=first_name
		self.last_name=last_name
		self.balance=0
		self.deposits=[]
		self.withdrawals= []
	
	def welcome(self):
		return "Dear customer {} {} your currrent balance is {}".format(self.first_name,self.last_name,self.balance)
	
	def deposit(self, new_deposit):
		deposit=new_deposit
		self.balance=self.balance + new_deposit
		self.deposits.append(new_deposit)
		return "Dear customer {} {} you have deposited {}".format(self.first_name,self.last_name,new_deposit) 

	def withdraw(self,withdrawal):
		withdraw=withdrawal
		if withdrawal < self.balance:
			self.balance = self.balance - withdrawal
			self.withdrawals.append(withdrawal)
			return "Dear customer {} {} you have withdrawal {}".format(self.first_name,self.last_name,withdrawal)

		else :
			return "insufficient balance"

	def showbalance(self):
		showbalance=self.balance
		text="Dear customer {} {} your balance is {}".format(self.first_name,self.last_name,showbalance)
		return text

	def show_deposits(self):
		for x in self.deposits:
			print(x)
	def show_withdrawals(self):
		for x in self.withdrawals:
			print(x)	
    def give_loan(self,amount):
    	loan=amount

    	if len(self.deposits)>=5 and amount <=(1/3*sum (self.deposits)) and self.loan ==0:
    		self.loan = self.loan + amount
    		print("Dear customer your loan of{} has been approved".format(g))
    	else:
    		print("loan not approved")  

	
    def loan_repayment(self,a):

    	cash=a
    	if a<self.loan:
    		self.loan = self.loan -a
		    print( "Dear customer your remaining loan balance is {}".format(self.loan))
		elif a>self.loan:
		    excess_cash = a - self.loan
		    self.loan =a - exces_cash - self.loan

		    self.balance = excess_cash+ self.balance
        elif a== self.loan:
        	self.loan =self.loan- a
        	print("Dear customer your loan is not fully paid")


