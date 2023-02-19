#Let's create ATm Machine using the Python
password=1234
name="Vinod"
print("Welcome to the Atm")
atm_pin=int(input("Enter your pin  "))
amount=70000
languages=["Telugu","English","Hindi"]
while True:
    if atm_pin==password:
        print(f'Hi {name} welcome to the Atm Machine have a nice day')
        for i in languages:
            print(i)
            # print("Choose Your language")
        number=int(input("Enter your langugae number in 0-2  "))
        if number==0:
                print(f'your language is {languages[0]}')
        elif number==1:
                print(f'your language is {languages[1]}')
        else:
                print(f'your language is {languages[2]}')
        
        bank_services=["Balance Enquery","Min statement","Pin Change","Withdraw","Transfor the funds"]
        for j in bank_services:
            print(j)
        print("Choose your option")
        m=int(input("Enter your option range between 0-4 "))
        if m==0:
                print(f'The balance in your account is {amount}')
                print('Thanks for visiting, Have a nice day')
        elif m==1:
                print("Print the last six month statement")
                print('Thanks for visiting, Have a nice day')
        elif m==2:
                if password==atm_pin:
                    print("Change you're old pin")
                    new_pin=int(input("Enter new pin "))
                    password=new_pin
                    print(f'You/re new password is {password}')
                    print('Thanks for visiting, Have a nice day')
        elif m==3:
                withdraw=int(input("Enter Your withdraw amount "))
                balance=amount-withdraw
                print(f'The remaing balance is {balance}')
                print('Thanks for visiting, Have a nice day')
        else:
                transfer=int(input("Enter the amount you want to transfer  "))
                account=int(input("Enter the account number  "))
                remaing_balance=amount-transfer
                print(f'The ammount is succefull transferd to the {account} and the balance is {remaing_balance}')
                print('Thanks for visiting, Have a nice day')
        break
            
            

        


        break
        
    else:
        print("Enter Worng Pin")
        break