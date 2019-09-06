

# class Statistics:


#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def mean(self):

#         x_bar = sum(self.x)/ len(self.x)
#         y_bar = sum(self.y)/ len(self.y)
#         print(x_bar, y_bar)
#         return x_bar, y_bar


#     def mean_deviation(self, x_bar, y_bar):
#         x_xbar = [x - x_bar for x in self.x]
#         y_ybar = [y - y_bar for y in self.y]
#         x_mean_deviation = sum(x_xbar) / len(self.x)
#         y_mean_deviation = sum(y_ybar) / len(self.y)


#         print("x".center(13), "y".center(10), "x-xbar".center(10), "y-ybar".center(10))

#         for i in zip(self.x,self.y,x_bar.mean_deviation()[0],y_bar.mean_deviation()[1]):
#             print(str(i[0]).center(13), str(i[1]).center(10), str(i[2]).center(10), str(i[3]).center(10))

#         print("The mean deviation of x is", x_mean_deviation)
#         print("The mean deviation of y is", y_mean_deviation)

        
# x = [1,2,3,4,9797,6,7,8,9,10]
# y = [2,4,6,8,10,16754,14,16,18,20]
# print(x,  y)
# Stat = Statistics(x,y)              
# Stat.mean()
# Stat.mean_deviation(Stat.mean(x_bar,y_bar))


class Statistics:


    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mean(self):
        x_bar = sum(self.x)/ len(self.x)
        y_bar = sum(self.y)/ len(self.y)
        return x_bar, y_bar
    
    def list_meanbar(self):
        mean_bar = self.mean()
        x_bar = mean_bar[0]
        y_bar = mean_bar[1]

        x_xbar = [x - x_bar for x in self.x]
        y_ybar = [y - y_bar for y in self.y]

        return x_xbar, y_ybar



    def mean_deviation(self):
        list_bar = self.list_meanbar()
        x_xbar = list_bar[0]
        y_ybar = list_bar[1]

        x_mean_deviation = sum(x_xbar) / len(self.x)
        y_mean_deviation = sum(y_ybar) / len(self.y)

        print("x".center(13), "y".center(10), "x-xbar".center(10), "y-ybar".center(10))

        for i in zip(self.x,self.y,self.list_meanbar()[0],self.list_meanbar()[1]):
            print(str(i[0]).center(13), str(i[1]).center(10), str(i[2]).center(10), str(i[3]).center(10))

        print("The mean deviation of x is", x_mean_deviation)
        print("The mean deviation of y is", y_mean_deviation)

        
x = [1,2,3,4,9797,6,7,8,9,10]
y = [2,4,6,8,10,16754,14,16,18,20]

print(x,  y)
Stat = Statistics(x,y)              

Stat.mean_deviation()






