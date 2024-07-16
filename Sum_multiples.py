class Solutions(object):
    def sumOfMultiples(self,n):
        sum=0
        for i in range(1,n):
            if (i%3==0 or i%5==0) or i%7==0:
                sum+=i
        return sum