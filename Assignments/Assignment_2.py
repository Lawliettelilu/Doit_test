# 1. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა 
# რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.
# მაგ.:
# Enter a number: 56
  # The number in list
# #===========================
# Enter a number: 45
  # The number not in list

num_list = [44, 23, 11, 8, 20, 56, 33, 55]
num = int(input('შეიყვანეთ ციფრი: '))
if num in num_list:
    print('ციფრი არის სიაში')
else:
    print('ციფრი არ არის სიაში')

# 2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. 
# თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.
# მაგ.:
# Enter an integer: 25
# The number is odd
# #===========================
# Enter an integer: 36
# The number is even

num =int(input('შეიყვანეთ მთელი რიცხვი: '))
if num % 2 == 0:
    print(num, 'არის ლუწი')
else:
    print(num, 'არის კენტი')


# 3. შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, 
# თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"

st1 = input('შეიყვანეთ პირველი სტრინგი: ')
st2 = input('შეიყვანეთ მეორე სტრინგი: ')    
if st1 == st2:
    print('Same object')
else:
    print('Different object')



# 4. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:
# * თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";
# * თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
# * სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
# რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.
# მაგ.:
# Enter a number: 105
# None of the conditions were met
# #===========================
# Enter a number: 40
# More than list elements
# #===========================
# Enter a number: 56
# Equal

num_list = [44, 23, 11, 8, 20, 56, 33, 55]
num = int(input('შეიყვანეთ ციფრი: '))   
if num > num_list[2] and num < num_list[-1]:
    print('More than list elements')
elif num == num_list[5]:
    print('Equal')  
else:
    print('None of the conditions were met')    
