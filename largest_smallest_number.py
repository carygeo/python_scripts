largest = None
smallest = None
largest_so_far = None
smallest_so_far = None

error = "Invalid input"

print "Welcome to Cary's program of largest and smallest numbers.  Watch as the program remembers the highest and lowest number you enter!  (try to trick it by entering letters) If you wish to stop and see your largest and smallest number, enter 'done'"

name = raw_input("Please enter your name: ")

while True:
	num = raw_input("Enter a number: ")
	
        if num == "done":
            break
       
        else:
            try:
                num_try = int(num)
                
                if  largest is None:
            		largest = num_try

                elif num_try > largest:
            		largest = num_try

                if  smallest is None:
                	smallest = num_try

                elif num_try < smallest:
                	smallest = num_try

            except:
                print error

print "Nice work", name, "!"
print "Your largest number was", largest
print "Your smallest number was", smallest