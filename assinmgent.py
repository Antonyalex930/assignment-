
try:
    
    book1 = int(input("number of copies of Book1 - Introduction to Python Programming : Rs 499.00 : "))
    book2 = int(input("number of copies of Book2 - Python Libraries Cookbook : Rs. 855.00 : "))
    book3 = int(input("number of copies of Book3 -  Data Science in Python : Rs. 645.00 : "))
    
   
     
except Exception as e:
    print("please enter valid statement")
    exit(0)
v1 = book1 * 499
v2 = book2 * 855    
v3 = book3 * 645
t = v1+v2+v3
t1 = t*0.12
total = t + t1 +250
    
print("GST : 12%" "Delivery Charges : Rs. 250.00 {}".format(total))   



