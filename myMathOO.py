"""
Created 26 Nov 22
Rev 1.1 14 Dec 22
    * Method "times" added for real value.
    * Methods for add.. return new object.
Rev 1.2 04 Jan 23
    * ComplexVarPolar.power_dm changed to return polar var, simply.
    * ComplexVar.add_c1 and .add_c2 renamed add_real and add_imag respectively.
    * Other names changed likewise.
    * Analogous functions ComplexVarPolar.add_r and .add_angle added.
"""
from math import atan2, cos, sin, pi

class ComplexVar():    
    _SYSTEM = "Cartesian"

    def __init__(self, real=0.0, imag=0.0):
        self._coord1 = real
        self._coord2 = imag

    def __str__(self):
        return "(" + str(self._coord1) + ", " + str(self._coord2)\
            + ") " + self._SYSTEM

    def set_var(self, real, imag):
        self._coord1 = real
        self._coord2 = imag
            
    def val_real(self):
        return self._coord1
    
    def val_imag(self):
        return self._coord2
    
    def abs_val(self):
        return (self._coord1**2 + self._coord2**2)**0.5

    def add_real(self, real):
        return ComplexVar(self._coord1 + real, self._coord2)
        
    def add_imag(self, imag):
        return ComplexVar(self._coord1, self._coord2 + imag)
        
    def plus(self, z):
        return ComplexVar(self._coord1 + z._coord1, 
                            self._coord2 + z._coord2)

    def minus(self, z):
        return ComplexVar(self._coord1 - z._coord1, 
                            self._coord2 - z._coord2)
    
    def times(self, val):
        return ComplexVar(self._coord1 * val, self._coord2 * val)
        
    def divide(self, z):
        denominator = z._coord1**2 + z._coord2**2
        return ComplexVar((self._coord1*z._coord1 + self._coord2*z._coord2)\
                            /denominator,
                            (self._coord2*z._coord1 - self._coord1*z._coord2)\
                            /denominator)
        
    def mult_complex(self, z):
        #Multiply two complex numbers
        return ComplexVar(self._coord1 * z._coord1 - 
                            self._coord2 * z._coord2, \
                            self._coord1 * z._coord2 + 
                            self._coord2 * z._coord1)

    def power(self, pow):
        #Returns the required integer power of a complex number,
        temp = ComplexVar(self._coord1, self._coord2)
        if pow > 1:
            for i in range(pow - 1):
                temp = self.mult_complex(temp)
        return temp
                
    def power_dm(self, power):
        #According to De Moivre's theorem
        temp = self.cart_to_polar()
        rPower = temp._coord1**power
        return ComplexVar(rPower*cos(power*temp._coord2),
                          rPower*sin(power*temp._coord2))

    def cart_to_polar(self):
        #Convert from cartesian to polar coords
        r = (self._coord1**2 + self._coord2**2)**0.5
        if self._coord1 == 0:
            if self._coord2 > 0:
                angle = (pi/2)
            elif self._coord2 == 0:
                angle = 0 #Arbitrarily 0, could be anything
            else:
                angle = (3*pi/2)
        else:
            angle = atan2(self._coord2, self._coord1)
        return ComplexVarPolar(r, angle)
#endclass

class ComplexVarPolar():
    _SYSTEM = "Polar"

    def __init__(self, first=0.0, second=0.0):
        self._coord1 = first
        self._coord2 = second

    def __str__(self):
        return "(" + str(self._coord1) + ", " + str(self._coord2)\
            + ") " + self._SYSTEM

    def set_var(self, first, second):
        self._coord1 = first
        self._coord2 = second
            
    def val_r(self):
        return self._coord1
    
    def val_angle(self):
        return self._coord2
    
    def abs_val(self):
        return self._coord1

    def add_r(self, r):
        return ComplexVarPolar(self._coord1 + r, self._coord2)
        
    def add_angle(self, angle):
        return ComplexVarPolar(self._coord1, self._coord2 + angle)
        
    def plus(self, z):
        #Add two polar complex vars
        return self.polar_to_cart().plus(z.polar_to_cart()).cart_to_polar()
    
    def minus(self, z):
        #Subtract polar complex var
        return self.polar_to_cart().minus(z.polar_to_cart()).cart_to_polar()

    def divide(self, z):
        #Divide by polar complex var
        return self.polar_to_cart().divide(z.polar_to_cart()).cart_to_polar()
    
    def mult_complex(self, z):
        #Multiply two complex numbers
        r = self._coord1 * z._coord1
        angle = (self._coord2 + z._coord2)
        if angle >= (2*pi):
            angle -= (2*pi)
        return ComplexVarPolar(r, angle)
        
    def power(self, pow):
        #Returns the required integer power of a complex number,
        temp = ComplexVarPolar(self._coord1, self._coord2)
        if pow > 1:
            for i in range(pow - 1):
                temp = self.mult_complex(temp)
        return temp

    def power_dm(self, power):
        #According to De Moivre's theorem
        return ComplexVarPolar(self._coord1**power, power*self._coord2)

    def polar_to_cart(self):
        #Convert from polar to cartesian coords
        r = self._coord1
        angle = self._coord2
        return ComplexVar(r*cos(angle),r*sin(angle))
#endclass

#MAIN
if __name__ == "__main__":
    tc=0 #-1 to run all tests
    PASS = 1
    FAIL = 0
    testResults = []
    ALL=[0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 14, 15, 16, 20, 21, 40, 41, 42, 43]
    if tc==-1:
        tests = ALL
    else:
        tests = [tc]
    for tc in tests:
        if tc==0:
            print("TEST CASE", tc, "Cartesian, init")
            z = ComplexVar()
            print(z)
            a = ComplexVar(1, 2)
            print(a)
        if tc==1:
            print("TEST CASE", tc, "Cartesian, set")
            z = ComplexVar()
            z.set_var(0.1, 0.2)
            print(z)
        if tc==2:
            print("TEST CASE", tc, "Cart, abs")
            z = ComplexVar(3, 4)
            print(z)
            print(z.abs_val())
            if z.abs_val() == 5:
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])    
        if tc==3:
            print("TEST CASE", tc, "multiply, cartesian value")    
            z = ComplexVar(1, 2.2)
            y = ComplexVar(2.3, 3.4)
            x = z.mult_complex(y)
            print(x)
            if round(x.val_real(), 2) == -5.18 \
                and round(x.val_imag(), 2) == 8.46:
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])
        if tc==4:
            print("TEST CASE", tc, "divide, cartesian value")    
            z = ComplexVar(1, 2.2)
            y = ComplexVar(2, 3.4)
            x = z.divide(y)
            print(x)
            if round(x.val_real(), 2) == 0.61 \
                and round(x.val_imag(), 2) == 0.06:
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])
        if tc==5:
            print('TEST CASE', tc, "plus, cartesian")
            z = ComplexVar(1, 2)
            y = ComplexVar(2, 3)
            z = z.plus(y)
            print(z)
        if tc==6:
            print('TEST CASE', tc, "times, cartesian")
            z = ComplexVar(1, 2)
            y = 2
            x = z.times(y)
            print("x =", x, ", z =", z)
        if tc==10:
            print("TEST CASE", tc, "Polar, init")
            z = ComplexVarPolar()
            print(z)
            a = ComplexVarPolar(1, 7)
            print(a)
        if tc==11:
            print("TEST CASE", tc, "Polar, set")
            z = ComplexVarPolar()
            z.set_var(10, 20)
            print(z) 
            if z.val_r() == 10 and z.val_angle() == 20:
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])
        if tc==12:
            print("TEST CASE", tc, "Polar, abs")
            z = ComplexVarPolar(5, pi)
            print(z)
            print(z.abs_val())
            if z.abs_val() == 5:
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])    
        if tc==14:
            print('TEST CASE', tc, "divide, polar")
            z = ComplexVarPolar(2, pi/4)
            y = ComplexVarPolar(2, pi/2)
            x = z.divide(y)
            print("x", x)
        if tc==15:
            print('TEST CASE', tc, "plus, polar")
            z = ComplexVarPolar(2, pi/4)
            y = ComplexVarPolar(2, pi/2)
            x = z.plus(y)
            print("x", x)
        if tc==16:
            print('TEST CASE', tc, "subtract, polar")
            z = ComplexVarPolar(2, pi/4)
            y = ComplexVarPolar(2, pi/2)
            x = z.minus(y)
            print("x", x)
        if tc==20:
            print('TEST CASE', tc, 'Convert cartesian to polar')
            z = ComplexVar(2, 2)
            y = z.cart_to_polar()
            print(y)
            if y.val_r() == 8**0.5 and y.val_angle() == (pi/4):
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])
        if tc==21:
            print("TEST CASE", tc, "convert polar to cartesian")
            z = ComplexVarPolar(2**0.5, 0.75*pi)
            print(z)
            y = z.polar_to_cart()
            print(y)
            if round(y.val_real(), 8) == -1 and round(y.val_imag(), 8) == 1:
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])
        if tc==40:
            print("TEST CASE", tc, "power_dm, cartesian value")
            z = ComplexVar(1,1)
            print(z.power_dm(3))
            y = z.power_dm(3)
            if round(y.val_real(), 2) == -2 \
                and round(y.val_imag(), 2) == 2:
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])
        if tc==41:
            print("TEST CASE", tc, "power_dm, polar value")
            z = ComplexVarPolar(2**0.5, pi/4)
            y = z.power_dm(3)
            print(y)
            if round(y.val_r(), 8) == round(8**0.5, 8) \
                and round(y.val_angle(), 8) == round(3*pi/4, 8):
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])
        if tc==42:
            print("TEST CASE", tc, "power, cartesian value")
            z = ComplexVar(1,1)
            print(z.power(3))
            y = z.power(3)
            if y.val_real() == -2 \
                and y.val_imag() == 2:
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])
        if tc==43:
            print("TEST CASE", tc, "power, polar value")
            z = ComplexVarPolar(2**0.5, pi/4)
            y = z.power(3)
            print(y, 8**0.5, 3*pi/4)
            if round(y.val_r(), 8) == round(8**0.5, 8) \
                and round(y.val_angle(), 8) == round(3*(pi/4), 8):
                testResults.append([str(tc), PASS])
            else:
                testResults.append([str(tc), FAIL])
        if tc==50:
            pass
    """
    """
    for el in testResults:
        if el[1] == FAIL:
            print("TC #{} failed".format(el[0]))
