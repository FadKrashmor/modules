"""
26 Nov22
"""
from math import atan2, cos, sin, pi

class ComplexVar():    
    _SYSTEM = "Cartesian"

    def __init__(self, first=0.0, second=0.0):
        self._coord1 = first
        self._coord2 = second

    def __str__(self):
        return "(" + str(self._coord1) + ", " + str(self._coord2)\
            + ") " + self._SYSTEM

    def set_var(self, first, second):
        self._coord1 = first
        self._coord2 = second
            
    def val_coord1(self):
        return self._coord1
    
    def val_coord2(self):
        return self._coord2
    
    def abs_val(self):
        return (self._coord1**2 + self._coord2**2)**0.5

    def add_c1(self, c1):
        self._coord1 += c1
        
    def add_c2(self, c2):
        self._coord1 += c2
        
    def plus(self, z):
        return ComplexVar(self._coord1 + z._coord1, 
                            self._coord2 + z._coord2)

    def divide(self, z):
        denominator = z._coord1**2 + z._coord2**2
        return ComplexVar((self._coord1*z._coord1 + self._coord2*z._coord2)\
                            /denominator,
                            (self._coord2*z._coord1 - self._coord1*z._coord2)\
                            /denominator)
        
    def minus(self, z):
        return ComplexVar(self._coord1 - z._coord1, 
                            self._coord2 - z._coord2)
    
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

#
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
            
    def val_coord1(self):
        return self._coord1
    
    def val_coord2(self):
        return self._coord2
    
    def abs_val(self):
        return self._coord1

    def plus(self, z):
        #Add two polar complex vars
        return self.polar_to_cart().plus(z.polar_to_cart()).cart_to_polar()
    
    def minus(self, z):
        #Subtract polar complex var
        return self.polar_to_cart().plus(z.polar_to_cart()).cart_to_polar()

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
        rPower = self._coord1**power
        return ComplexVar(rPower*cos(power*self._coord2),
                          rPower*sin(power*self._coord2)).cart_to_polar()

    def polar_to_cart(self):
        #Convert from polar to cartesian coords
        r = self._coord1
        angle = self._coord2
        return ComplexVar(r*cos(angle),r*sin(angle))

#MAIN
if __name__ == "__main__":
    PASS = 1
    FAIL = 0
    testResults = []
    tc=14
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
        if round(x.val_coord1(), 2) == -5.18 \
            and round(x.val_coord2(), 2) == 8.46:
            testResults.append([str(tc), PASS])
        else:
            testResults.append([str(tc), FAIL])
    if tc==4:
        print("TEST CASE", tc, "divide, cartesian value")    
        z = ComplexVar(1, 2.2)
        y = ComplexVar(2, 3.4)
        x = z.divide(y)
        print(x)
        if round(x.val_coord1(), 2) == 0.61 \
            and round(x.val_coord2(), 2) == 0.06:
            testResults.append([str(tc), PASS])
        else:
            testResults.append([str(tc), FAIL])
    if tc==5:
        print('TEST CASE', tc, "plus, cartesian")
        z = ComplexVar(1, 2)
        y = ComplexVar(2, 3)
        z = z.plus(y)
        print(z)
    if tc==10:
        print("TEST CASE", tc, "Polar, init")
        z = ComplexVarPolar()
        print(z)
        a = ComplexVarPolar(1, 7)
        print(a)
    if tc==11:
        print("TEST CASE", tc, "Polar, set")
        z = ComplexVarPolar()
        z.set_var(2**0.5, 20)
        print(z) 
        if z.val_coord1() == 10 and z.val_coord2() == 20:
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
        if y.val_coord1() == 8**0.5 and y.val_coord2() == (pi/4):
            testResults.append([str(tc), PASS])
        else:
            testResults.append([str(tc), FAIL])
    if tc==21:
        print("TEST CASE", tc, "convert polar to cartesian")
        z = ComplexVarPolar(2**0.5, 0.75*pi)
        print(z)
        y = z.polar_to_cart()
        print(y)
        if round(y.val_coord1(), 8) == -1 and round(y.val_coord2(), 8) == 1:
            testResults.append([str(tc), PASS])
        else:
            testResults.append([str(tc), FAIL])
    if tc==40:
        print("TEST CASE", tc, "power_dm, cartesian value")
        z = ComplexVar(1,1)
        print(z.power_dm(3))
        y = z.power_dm(3)
        if round(y.val_coord1(), 2) == -2 \
            and round(y.val_coord2(), 2) == 2:
            testResults.append([str(tc), PASS])
        else:
            testResults.append([str(tc), FAIL])
    if tc==41:
        print("TEST CASE", tc, "power_dm, polar value")
        z = ComplexVarPolar(2**0.5, pi/4)
        y = z.power_dm(3)
        print(y)
        if round(y.val_coord1(), 8) == round(8**0.5, 8) \
            and round(y.val_coord2(), 8) == round(3*pi/4, 8):
            testResults.append([str(tc), PASS])
        else:
            testResults.append([str(tc), FAIL])
    if tc==42:
        print("TEST CASE", tc, "power, cartesian value")
        z = ComplexVar(1,1)
        print(z.power(3))
        y = z.power(3)
        if y.val_coord1() == -2 \
            and y.val_coord2() == 2:
            testResults.append([str(tc), PASS])
        else:
            testResults.append([str(tc), FAIL])
    if tc==43:
        print("TEST CASE", tc, "power, polar value")
        z = ComplexVarPolar(2**0.5, pi/4)
        y = z.power(3)
        print(y, 8**0.5, 3*pi/4)
        if round(y.val_coord1(), 8) == round(8**0.5, 8) \
            and round(y.val_coord2(), 8) == round(3*(pi/4), 8):
            testResults.append([str(tc), PASS])
        else:
            testResults.append([str(tc), FAIL])
    if tc==50:
        pass
    """
    """
    for el in testResults:
        if el[1] == FAIL:
            print("TC #", el[0], "failed")
