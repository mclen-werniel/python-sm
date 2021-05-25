

class SparseMatrix:

    def __init__ (self, rows, columns):
        self.__rows__ = rows
        self.__columns__ = columns
        self.__number__ = 0
        self.__matrix__ = []

    
    def __repr__(self):
        response = "{} x {} \n".format(self.__rows__, self.__columns__)
        for lst in self.__matrix__:
            response += lst.__repr__() + '\n'
        response += "Total: {}".format(self.__number__)
        return response

    def insert(self, row, column, value):
        if row < 0 | column < 0 | row >= self._rows | column >= self._columns:
            raise ValueError("Invalid row or column")
             
       
         
        filled = False
        for i in range(self.__number__):
            if(self.__matrix__[i][0] < row):
                continue
            elif(self.__matrix__[i][0] > row):
                self.__matrix__.insert(i, [row, column, value])
                self.__number__ += 1
                filled = True
                break
            elif(self.__matrix__[i][1] < column):
                continue
            elif(self.__matrix__[i][1] > column):
                self.__matrix__.insert(i, [row, column, value])
                self.__number__ += 1
                filled = True
                break
            else:
                raise ValueError("The position is already filled")
        if(filled == False):
            self.__matrix__.append([row, column, value])
            self.__number__ += 1
        return

    def remove(self, row, column):
        if row < 0 | column < 0 | row >= self.__rows__ | column >= self.__columns__:
            raise ValueError("Invalid row or column")
             
        for i in range(self.__number__):
            if(self.__matrix__[i][0] == row | self.__matrix__[i][1] == column):
                return pop(i)
        return None

    def size(self):
        return self.__number__
     
    def shape(self):
        return tuple((self.__rows__, self.__columns__))
     
    def display(self):
        print(self)

    def add(self, obj):
        if(isinstance(obj, SparseMatrix) != True):
            raise TypeError("add() method needs an object of type Sparse")
         
        if(self.shape() == obj.shape()):
            result = SparseMatrix(self.__rows__, self.__columns__)
        else:
            raise ValueError("Invalid row or columns")
         
        i = 0
        j = 0
        k = 0
        while((i < self.__number__) & (j < obj.__number__)):
            if(self.__matrix__[i][0] < obj.__matrix__[j][0]):
                result.__matrix__.insert(k, self.__matrix__[i])
                k += 1
                i += 1
            elif(self.__matrix__[i][0] > obj.__matrix__[j][0]):
                result.__matrix__.insert(k, obj.__matrix__[j])
                k += 1
                j += 1
            elif(self.__matrix__[i][1] < obj.__matrix__[j][1]):
                result.__matrix__.insert(k, self.__matrix__[i])
                k += 1
                i += 1
            elif(self.__matrix__[i][1] > obj.__matrix__[j][1]):
                result.__matrix__.insert(k, obj.__matrix__[j])
                k += 1
                j += 1
            else:
                result.__matrix__.insert(k, list([self.__matrix__[i][0], self.__matrix__[i][1], self.__matrix__[i][2] + obj.__matrix__[j][2]]))
                k += 1
                i += 1
                j += 1
        while(i < self.__number__):
            result.__matrix__.insert(k, self.__matrix__[i])
            k += 1
            i += 1
        while(j < obj.__number__):
            result.__matrix__.insert(k, obj.__matrix__[j])
            k += 1
            j += 1
             
        result.__number__ = k
        return result
     
    def transpose(self):
        occurrence = []
        index = []
         
        for i in range(self.__columns__):
            occurrence.append(0)
        for i in range(self.__number__):
            occurrence[self.__matrix__[i][1]] += 1
         
        index.append(0)
        for i in range(1, self.__columns__):
            index.append(index[i-1] + occurrence[i-1])
             
        result = SparseMatrix(self.__columns__, self.__rows__)
        result.__number__ = self.__number__
        for i in range(self.__number__): result.__matrix__.append(list())
        for i in range(self.__number__):
            result.__matrix__[index[self.__matrix__[i][1]]] = list([self.__matrix__[i][1], self.__matrix__[i][0], self.__matrix__[i][2]])
            index[self.__matrix__[i][1]] += 1
        return result