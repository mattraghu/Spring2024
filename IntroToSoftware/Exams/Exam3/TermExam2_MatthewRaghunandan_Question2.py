#read in data.txt
averages = []
try: 
    with open('data.txt', 'r') as file:
        # print(file.read().splitlines())
        for line in file:
            nums = line.strip().replace('\n', '').split(' ')

            if len(nums) == 1 and nums[0] == '':
                print("Cannot calculate average for an empty line")
                continue

            total = 0
            err = False
            for num in nums:
                try: 
                    total += float(num)
                except ValueError:
                    print("Invalid data format")
                    err = True
                    break

            if err:
                continue

            

            try: 
                avg = total/len(nums)
            except ZeroDivisionError: 
                print("Cannot calculate average for an empty line")
                continue

            averages.append(avg)
except FileNotFoundError:
    print("File not found") 
    exit()

#Now write the averages to a file called averages.txt
with open('averages.txt', 'w') as file:
    for avg in averages:
        file.write(str(avg) + '\n')

