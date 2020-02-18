import math
from math import sqrt
import numbers



def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    



class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
       
        
        # Check to see if matrix is 1x1 or 2x2
        if self.h == 1:
            return self.g[0][0]
        elif self.h ==2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            return (a*d)-(b*c)
                        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        trace = 0
        
        for i in range(self.h):
            trace += self.g[i][i]
                    
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        mInverse = zeroes(self.h, self.w)
        determinant = self.determinant()
        
        if self.h == 1:
            return Matrix(1/self.g[0][0])
        elif self.h == 2:
            mInverse[0][0] = 1/determinant * self.g[1][1]
            mInverse[0][1] = 1/determinant * -self.g[0][1]
            mInverse[1][0] = 1/determinant * -self.g[1][0]
            mInverse[1][1] = 1/determinant * self.g[0][0]
                    
            return mInverse
            

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        mTranspose = zeroes(self.h, self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                mTranspose.g[i][j] = self.g[j][i]
                
        return mTranspose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 

        mSum = []
        row = []
                           
        for i in range(self.h):
            for j in range(self.w):
                s = self.g[i][j] + other.g[i][j]
                row.append(s)
            mSum.append(row)
            row = []
                           
        return Matrix(mSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """

        mNegative = []
        row = []
                           
        for i in range(self.h):
            for j in range(self.w):
                row.append(-1*self.g[i][j])
            mNegative.append(row)
            row = []
        
        #Can I Skip This And Just 'return -self'?
                           
        return Matrix(mNegative)
        
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """

        mDifference = []
        row = []
                           
        for i in range(self.h):
            for j in range(self.w):
                d = self.g[i][j] - other.g[i][j]
                row.append(d)
            mDifference.append(row)
            row = []
                           
        return Matrix(mDifference)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """

        mResult = zeroes(self.h, other.w)
    
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    mResult[i][j] += self.g[i][k]*other.g[k][j]
                
                        
        return mResult                         

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass

        sProduct = []
        row = []
        
        for i in range(len(self.g)):
            for j in range(len(self.g[0])):
                row.append(other * self.g[i][j])
            sProduct.append(row)
            row=[]
                
        return Matrix(sProduct)