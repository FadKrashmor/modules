# -*- coding: utf-8 -*-
"""
Matrices
"""
from math import pi, cos, sin
class matrix_3x3():
    
    def __init__(self):
        self._matrix = [[0 for x in range(3)] for y in range(3)]
        
    def construct_x_rotation(self, angle):
        alpha = (angle * pi)/180
        self._matrix[0] = [1, 0, 0]
        self._matrix[1] = [0, cos(alpha), -sin(alpha)]
        self._matrix[2] = [0, sin(alpha), cos(alpha)]
        
    def construct_y_rotation(self, angle):
        beta = (angle * pi)/180
        self._matrix[0] = [cos(beta), 0, sin(beta)]
        self._matrix[1] = [0, 1, 0]
        self._matrix[2] = [-sin(beta), 0, cos(beta)]

    def construct_z_rotation(self, angle):
        gamma = (angle * pi)/180
        self._matrix[0] = [cos(gamma), -sin(gamma), 0]
        self._matrix[1] = [sin(gamma), cos(gamma), 0]
        self._matrix[2] = [0, 0, 1]

    def matrix_v_multiply(self, v):
        return [self._matrix[0][0]*v[0] +
                    self._matrix[0][1]*v[1] +
                        self._matrix[0][2]*v[2],
                self._matrix[1][0]*v[0] +
                    self._matrix[1][1]*v[1] +
                        self._matrix[1][2]*v[2],
                self._matrix[2][0]*v[0] +
                    self._matrix[2][1]*v[1] +
                        self._matrix[2][2]*v[2]]
   
class matrix_2x2():
    #In development
    def __init__(self):
        self._matrix = [[0 for x in range(2)] for y in range(2)]
        
    def construct_rotation(self, angle):
        alpha = (angle * pi)/180
        self._matrix[0] = [0, cos(alpha), -sin(alpha)]
        self._matrix[1] = [0, sin(alpha), cos(alpha)]

    def matrix_v_multiply(self, v):
        return [self._matrix[0][0]*v[0] +
                    self._matrix[0][1]*v[1],
                self._matrix[1][0]*v[0] +
                    self._matrix[1][1]*v[1]]
        
       