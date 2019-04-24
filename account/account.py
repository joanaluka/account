class account:
	def __init__ (self,first_name,last_name,balance):
		self.first_name=first_name
		self.last_name=last_name
		self.balance=balance
	def welcome(self):
	    return "Dear customer {} {} your currrent balance is {}".format(self.first_name,self.last_name,self.balance)
	def deposit(self, new_deposit):
	 	deposit=new_deposit
	 	self.balance=self.balance + new_deposit
	 	text="Dear customer {} {} you have deposited {}".format(self.first_name,self.last_name,new_deposit)	
	 	return text
	def withdraw(self,withdrawal):
	 	withdraw=withdrawal
	 	self.balance=self.balance - withdrawal
	 	msg="Dear customer {} {} you have withdrawal {}".format(self.first_name,self.last_name,withdrawal)
	 	return msg
	def showbalance(self):
		showbalance=self.balance
		text="Dear customer {} {} your balance is {}".format(self.first_name,self.last_name,showbalance)
		return text