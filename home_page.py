from projectfunctions import delete_data,search_data,show_data,print_invoice

print("------------MENU------------\n")
print("1) Show Products\n")
print("2) Search Product\n")
print("3) Delete Product\n")
print("4) Create Invoice\n")
print("----------------------------")

print("Enter Your Choice: ")
choice=int(input())

if choice==1:
    show_data.show()
elif choice==2:
    search_data.search()
elif choice==3:
    delete_data.delete()
elif choice==4:
    print_invoice.invoice()
    
        
    