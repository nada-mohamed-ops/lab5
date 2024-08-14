
class Bank:
  

    def _init_(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer ({customer.name}) added successfully to ({self.name}) Bank.")


class Customer:
    

    def _init_(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(
            f"Account ({account.account_number}) added successfully for customer ({self.name})."
        )

    def transfer(self, from_account, to_account, amount):
        if from_account.balance >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(
                f"Successfully transferred ({amount}) from account ({from_account.account_number}) to account ({to_account.account_number})."
            )
        else:
            print(f"Failed to transfer ({amount}).  balance: ({from_account.balance}).")


class Account:
    

    def _init_(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Successfully deposited ({amount}) to account ({self.account_number}). New balance: ({self.balance})"
        )

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(
                f"Successfully withdrew ({amount}) from account ({self.account_number}). New balance: ({self.balance})"
            )
        else:
            print(
                f"Failed to withdraw ({amount}) from account ({self.account_number}). balance: ({self.balance})"
            )

    def get_balance(self):
        return self.balance



bank = Bank("MS")
print(bank.name)  # MS


customer = Customer("nada")
print(customer.name)  # nada

bank.add_customer(customer)  

# test account
account1 = Account(123456, 1000)
account2 = Account(789012, 500)
print(account1.account_number)  # 123456
print(account2.account_number)  # 789012
print(account1.balance)  # 1000
print(account2.balance)  # 500

# test customer
customer.add_account(
    account1
)  
customer.add_account(
    account2
) 


# test account
account1.deposit(
    200
) 
account2.deposit(
    200
)  


account1.withdraw(
    500
) 
account2.withdraw(
    500
) 

account1.withdraw(1500)  
account2.withdraw(1500) 


print(account1.get_balance())  # 700
print(account2.get_balance())  # 500


# test customer
customer.transfer(
    account1, account2, 300)

customer.transfer(
    account1, account2, 1000
)  # Failed to transfer (1000).  balance: (400).
customer.transfer(account2, account1, 10)  #


# =================================================================
# =================================================================
################### Q2 ##########################


class Animal:
    def _init_(
        self,
        name,
        age,
    ):
        self.name = name
        self.age = age

    def eat(self):
        print(f"({self.name}) is eating.")

    def drink(self):
        print(f"({self.name}) is drinking.")


class Cat(Animal):
    def _init_(
        self,
        name,
        age,
    ):
        super()._init_(name, age)

    def meow(self):
        print(f"({self.name}) is meowing.")

    def eat(self):
        print(f"({self.name}) is eating its favorite food.")


ca1 = Animal("mocha", 1)
ca1.eat()
ca1.drink()

cat2 = Cat("Gumball", 2)
cat2.meow()
cat2.eat()
cat2.drink()