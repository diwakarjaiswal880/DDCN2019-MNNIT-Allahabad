import pandas as pd
import matplotlib.pyplot as plt

#assignment 1 Q 4.a
myData = pd.read_csv('/home/cloudera/Desktop/diwakar/data/Auto.csv') 

# change path as required
for i in range(0, len(myData.index)):
    print (myData.iloc[i])
    
#assignment 1 Q 4.b    
print( myData.shape)
print( myData.describe())

#assignment 1 Q 4.c
for i in (32, 126,330,336,354):
    print( myData.iloc[i])
    
#assignment 1 Q 4.d
myData=pd.read_csv('/home/cloudera/Desktop/diwakar/data/Auto.csv',
na_values=["?"])
# change path as required
for i in (32, 126,330,336,354):
    print (myData.iloc[i])

#assignment 1 Q 4.e
newData = myData.dropna()
newData.to_csv('newAuto.csv', index=True)

#assignment 1 Q 4.f
print (newData.shape)
print (newData.describe())

#assignment 1 Q 5
data = [['E001', 'M', 34, 123, 'Normal', 350],
        ['E002', 'F', 40, 114, 'Overweight', 450],
        ['E003', 'F', 37, 135, 'Obesity', 169],
        ['E004', 'M', 30, 139, 'Underweight', 189],
        ['E005', 'F', 44, 117, 'Underweight', 183],
        ['E006', 'M', 36, 121, 'Normal', 80],
        ['E007', 'M', 32, 133, 'Obesity', 166],
        ['E008', 'F', 26, 140, 'Normal', 120],
        ['E009', 'M', 32, 133, 'Normal', 75],
        ['E010', 'M', 36, 133, 'Underweight', 40] ]
df = pd.DataFrame(data, columns = ['EMPID', 'Gender','Age', 'Sales','BMI', 'Income'] )

df.hist()
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5a.pdf')
plt.show()

df.plot.bar()

plt.bar(df['Age'], df['Sales'])
plt.xlabel("Age")
plt.ylabel("Sales")
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5b.pdf')
plt.show()

plt.boxplot(df['Age'])
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5c.pdf')
plt.show()
plt.boxplot(df['Sales'])
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5d.pdf')
plt.show()
plt.boxplot(df['Income'])
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5e.pdf')
plt.show()


plt.pie(df['Age'], labels = {"A", "B", "C","D", "E", "F","G", "H", "I", "J"},
autopct ='% 1.1f %%', shadow = True)
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5f.pdf')
plt.show()
plt.pie(df['Income'], labels = {"A", "B", "C","D", "E", "F","G", "H", "I", "J"},
autopct ='% 1.1f %%', shadow = True)
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5g.pdf')
plt.show()
plt.pie(df['Sales'], labels = {"A", "B", "C","D", "E", "F","G", "H", "I", "J"},
autopct ='% 1.1f %%', shadow = True)
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5h.pdf')
plt.show()

plt.scatter(df['Income'], df['Age'])
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5i.pdf')
plt.show()

plt.scatter(df['Income'], df['Sales'])
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5j.pdf')
plt.show()

plt.scatter(df['Sales'], df['Age'])
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_5k.pdf')
plt.show()

