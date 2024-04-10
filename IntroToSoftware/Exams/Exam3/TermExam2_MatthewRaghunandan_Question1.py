import pandas as pd
import matplotlib.pyplot as plt

# read in salary.txt
salary = pd.read_csv('salary.txt', sep = ' ')

# header is  Employee, Salary, Year, and Gender
salary.columns = ['Employee', 'Salary', 'Year', 'Gender']

# print data in tablar format
print(salary)

# ma, standard deviation, and mean based on gender
gender_data = salary.groupby('Gender').agg({'Salary': ['max', 'mean', 'std']})
print(gender_data)

# boxplots for salary for each gender
salary.boxplot(column = 'Salary', by='Gender')
plt.show()

#plot them on the same scatter plot
plt.scatter(salary[salary['Gender'] == "M"]['Year'], salary[salary['Gender'] == 'M']['Salary'], color = 'red', label = 'Male',)
plt.scatter(salary[salary['Gender'] == "F"]['Year'], salary[salary['Gender'] == 'F']['Salary'], color = 'blue', label = 'Female',)
plt.xlabel('Years')
plt.ylabel('Salary')
plt.legend()
plt.title('Scatter plot of Salary vs Year for M and F')
plt.show()


# histogram for salariers 
salary.hist(column = 'Salary', bins=5)
plt.show()

print("so this dooes not follow a normal distribution because it is skewed to the left") 

print("i would rule in favor of the women because even just from looking at the scatter plot of years worked vs salary for the different genders, you can seee that for the same amount of years worked the women are still paid less") 



