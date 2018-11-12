import pandas as pd
import numpy as np

import glob
import re
import matplotlib.pyplot as plt


data="/Users/ashikshafi/Downloads/WEOApr2017all.xls"


Data=pd.read_csv(data, sep='\t', encoding='latin-1')
ImportGoods=Data[((Data["WEO Subject Code"]=="TMG_RPCH"))]
ImportGoods["2022"]=ImportGoods["2022"].apply(lambda x: float(x))

NationalSavings=Data[((Data["WEO Subject Code"]=="NGSD_NGDP"))]
NationalSavings["2022"]=NationalSavings["2022"].apply(lambda x: float(x))

AccBalance=Data[((Data["WEO Subject Code"]=="BCA_NGDPD"))]
AccBalance["2022"]=AccBalance["2022"].apply(lambda x: float(x))


Debt=Data[((Data["WEO Subject Code"]=="GGXWDG_NGDP"))]
Debt["2022"]=Debt["2022"].apply(lambda x: float(x))



NewData=Data[((Data["WEO Subject Code"]=="NGSD_NGDP"))]



#Analysis: Import of goods

fig=plt.figure(len(ImportGoods["Country"])*.45)

plt.bar(ImportGoods["Country"],ImportGoods["2022"], width= 1)
plt.ylabel('Volume of Imports of Goods (% Change)')
plt.title('Countries by their Volume of Imports of Goods in 2022')
plt.xticks(ImportGoods["Country"], fontsize=5, rotation=90)
plt.tight_layout()
plt.show()


# National Savings:

plt.bar(NationalSavings["Country"],NationalSavings["2022"], width= 1, color=['black', 'red'])
plt.ylabel('Gross National Savings (As % of GDP')
plt.title('National savings of different countries in 2022')
plt.xticks(NationalSavings["Country"], fontsize=5, rotation=90)
plt.tight_layout()
plt.show()



#Acc Balance
plt.bar(AccBalance["Country"],AccBalance["2022"], width= 1, color=['green', 'black'])
plt.ylabel('Projected account balance (As % of GDP')
plt.title('Countries by their projected account balance in 2022')
plt.xticks(AccBalance["Country"], fontsize=5, rotation=90)
plt.tight_layout()
plt.show()


#Debt:

plt.bar(Debt["Country"],Debt["2022"], width= 1, color=['brown', 'yellow'])
plt.ylabel('Debt held by government (As % of GDP')
plt.title('Countries by how much debt their governments are likely to carry in 2022')
plt.xticks(Debt["Country"], fontsize=5, rotation=90)
plt.tight_layout()
plt.show()

#GDP Per capita vs population


GDP=Data[((Data["WEO Subject Code"]=="NGDPDPC"))]

Population= Data[((Data["WEO Subject Code"]=="LP"))]

GDP["2022"]=GDP["2022"].apply(lambda x: str(x))

GDP["2022"]=GDP["2022"].apply(lambda x: x.replace(",", ""))
GDP["2022"]=GDP["2022"].apply(lambda x: float(x))


Population["2022"]=Population["2022"].apply(lambda x: str(x))

Population["2022"]=Population["2022"].apply(lambda x: x.replace(",", ""))
Population["2022"]=Population["2022"].apply(lambda x: float(x))

#Scatterplot

plt.scatter(Population["2022"], GDP["2022"], marker= "o", c=np.arange(192))
for i, txt in enumerate(GDP["Country"]):
    plt.annotate(txt, (Population["2022"].iat[i], GDP["2022"].iat[i]))
plt.ylabel('GDP Per Capita in 2022 (In US Dollars')
plt.xlabel('Population (In Millions')
plt.title('Population vs GDP Per Capita of different countries in 2022)')
plt.show()

