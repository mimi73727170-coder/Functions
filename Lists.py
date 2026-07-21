#Practice
fruits = ["Apple","Berry","Orange","Mango"]
fruits.append("Pineapple")
fruits.remove("Apple")
fruits[2] = "Grapes"
print(fruits)

#MINI PROJECT-----Shopping list
shopping = ["Milk","Bread","Eggs"]
print("1.Show list")
print("2.Add item")
print("3.Remove item")
print("4.Exit")
choice = input("Enter your choice :")
if choice == "1" :
    print(shopping)
elif choice == "2" :
    a = input("Enter item to be added :")
    shopping.append(a)
elif choice == "3" :
    r = input("Enter item to be removed :")
    shopping.remove(r)
elif choice == "4" :
    print("Exit")
else :
    print("Invalid choice")

# Challenge
a = input("Enter fav movie 1 :")
b = input("Enter fav movie 2 :")
c = input("Enter fav movie 3 :")
d = input("Enter fav movie 4 :")
print("YOUR FAVORITE MOVIES")
movies = [a,b,c,d]
for movie in movies :
    print(movie)

#Challenge
print("=====Shopping List=====")
shopping = ["Sugar","Rice","Face wash"]
print("1.Show list")
print("2.Add items")
print("3.Remove items")
print("4.Count items")
print("5.Clear list")
print("6.Exit")
choice = input("Enter your choice :")
if choice == "1" :
    print(shopping)
elif choice == "2" :
    a = input("Enter item to be added :")
    shopping.append(a)
elif choice == "3" :
    r = input("Enter item to be removed :")
    shopping.remove(r)
elif choice == "4" :
    print(len(shopping))
elif choice == "5" :
    shopping.clear()
    print("List clear")
elif choice == "6" :
    print("Goodbye!")
else :
    print("Invalid choice")