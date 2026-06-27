'''
You had saved the Itams and thelr price detalls In a text file, whlch you
purchasad yestarday from a nearby super markat.

You need to know:

1. How many Itams did you purchasa?
2. How many Itams are frea?
3. What is the total amount you had to pay?
4. What is the discount amount?
S. What is the final amount did you pay aftar the discount?

Halp yourself by writing a python code to do this. Include nacessary code to
handle the possible exceptions.

Note:

. Data is stored In a taxt file Purchase-1.txt.
. Each line contains one ttem's detalls.
. Itam name and price is separated by a space.
. You have to enter the file nama during run time.

Sample input 1:

Purchase-1.txt

Chocolate SO
Biscult 35

Icocraam SO

(blank IIne)
Discount 5

Sample output 1:

Enter the file name: Purchase-1
No of Items purchased: 3
No of free Itoms: O

Amount to pay: 135

Discount glvan: 5
Final amount pald: 130
'''


def process_purchases():
    filename = input("Enter the file name: ")
    if not filename.endswith('.txt'):
        filename += '.txt'
        
    items_purchased = 0
    free_items = 0
    amount_to_pay = 0
    discount_given = 0
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('(blank line)'):
                    continue
                
                parts = line.split()
                if len(parts) >= 2:
                    name = " ".join(parts[:-1])
                    price_str = parts[-1]
                    
                    if name.lower() == 'discount':
                        try:
                            discount_given = int(price_str)
                        except ValueError:
                            print(f"Error parsing discount: {price_str}")
                    elif price_str.lower() == 'free':
                        free_items += 1
                    else:
                        try:
                            price = int(price_str)
                            amount_to_pay += price
                            items_purchased += 1
                        except ValueError:
                            print(f"Error parsing price for {name}: {price_str}")
                            
        print(f"No of items purchased: {items_purchased}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {amount_to_pay}")
        print(f"Discount given: {discount_given}")
        print(f"Final amount paid: {amount_to_pay - discount_given}")
        
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_purchases()
