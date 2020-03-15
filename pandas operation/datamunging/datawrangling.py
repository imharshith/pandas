#data munging
#converting .csv file to .html file or any other data format.

x=pd.read_csv("D:/project works/amazon.csv")
x.to_html('y.html')
