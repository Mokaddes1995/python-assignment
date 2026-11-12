# Program Name : Shopping Cart


print("\nWelcome to Shopping Cart CLI Program")


# Take Input From User

name = input("\nCustomer Name: ")


product = {}


for i in range(3):
    
    while True:
    
        item = input(f"\nProduct Name {i + 1}: ")
        
        price = int(input("Price (TK): "))
        
        # Prevent Negative Value
        
        if price <= 0:
            
            print("Price Must be Greater than 0")
            
        else:
                
            product[item] = price
            
            break
    

# Sub Total

subtotal = sum(product.values())

# Discount Amount

if subtotal >= 5000:
    
    discount = subtotal * 20 / 100
    
elif subtotal >= 3000:
    
    discount = subtotal * 10 / 100

elif subtotal >= 1000:
    
    discount = subtotal * 5 / 100

else:
    
    discount = 0
    

# Final Amount

finalAmount = subtotal - discount


print(f"\n{'=' * 7}Cart{'=' * 7}")

print(f"Customer Name: {name}")

print(f"\nSubtotal: {subtotal:.2f}")

print(f"Discount: {discount:.2f}")

print(f"Final Total: {finalAmount:.2f}")

print("\n*" * 18)