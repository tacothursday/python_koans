#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
class TriangleError(Exception):
    pass

def triangle(a, b, c):
    if a==b==c:
        if a == 0:
            raise TriangleError("All zeros")
        else: return 'equilateral'
    elif c<0 : raise  TriangleError("Negative Value")
    elif a+b<=c: raise  TriangleError("Invalid triangle")
    elif b+c<= a: raise  TriangleError("Invalid triangle")
    elif c+a<= b: raise  TriangleError("Invalid triangle")
    elif len(set([a, b, c])) == 2:
        return 'isosceles'

    else: return 'scalene'


