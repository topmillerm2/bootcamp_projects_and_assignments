class Mathdojo(object):
    def __init__(self):
        self.results = 0
    def add(self, *num1):
        for num in num1:
            if type(num) == list or type(num) == tuple:
                for k in num:
                    self.results += k
            else:
                self.results += num
        return self
    def sub(self, *num1):
        for num in num1:
            if type(num)==list or type(num) ==tuple:
                for k in num:
                    self.results -= k
            else:
                self.results -= num
        return self
    def result(self):
        print self.results
        return self

md = Mathdojo()
# md.add(50, [1,2]).add(2,5).sub(2,3, [5,1]).result()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).sub(2, [2,3], [1.1,2.3]).result()
