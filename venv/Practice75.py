"""
Seaborn -> Data visualization
Why seaborn?
Seaborn in intergrated closely to pandas[data analysis library]

BeautifulSoup -> WebScrapping

"""
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
print(tips)

sns.set_theme()
#Relational Plot
#sns.relplot(data=tips, x="total_bill", y="tip", style="smoker", hue="sex", size="size", col="time", row="day" )

#Distribution Plot
#sns.displot(data=tips, x="total_bill", col="time", kde=True)

#Categorical Plot
sns.catplot(data=tips, x="day", y="total_bill", hue="smoker", kind="bar")

plt.show()
