from Bankapp import Customer

c1 = Customer('Sumit',100,4000)
c2 = Customer('Aditya',101,5000)
c3 = Customer('Dipen',102,6000)

c1.deposit(500)
c1.withdraw(700)
c2.withdraw(100)

c1.check_balance()
c2.check_balance()
