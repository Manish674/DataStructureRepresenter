content = '''

            val_holder = [ ]
            no_of_vals = input("How many vlaues you want to enter\n")
            
            for i in range(int(no_of_vals)):
                values = float(input('Enter your value'))
                val_holder.append(values)
            
            
            print(f"Values before pop {val_holder}")
            print(f'Last value you inserted {val_holder.pop()}')
            print(f"Values after pop {val_holder}")
'''