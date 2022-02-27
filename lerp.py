"""
0-x-1
  |
a-y-b

(x-0)/(1-x)=(y-a)/(b-y)
x(b-y)=(1-x)(y-a)
xb-xy=y-a-xy+xa
xb=y-a+xa
xb=y-a(1+x)
xb+a(1-x)=y

y=xb-ax+a
y=x(b-a)+a

x(b-a)=y-a
x=(y-a)/(b-a)

a(1-x)=y-xb
a=(y-xb)/(1-x)

xb=y+xa-a
b=(y+xa-a)/x
b=(y+a(x-1))/x
"""

def lerp(a,b,x):
    return x*(b-a)+a #(x*b)-(x*a)+a

def arclerp(a,b,y):
    return (y-a)/(b-a) if (b-a)!=0.0 else 0.5

def lerpa(b,x,y):
    return (y-(x*b))/(1-x) if (1-x)!=0.0 else b

def lerpb(a,x,y):
    return (y+(a*(x-1)))/x if x!=0.0 else a

print(lerp( 0.0,  2.0,  0.5))
print(lerp( 2.0,  0.0,  0.5))
print(lerp(-2.0,  2.0,  0.5))
print(lerp( 2.0, -2.0,  0.5))
print(lerp(-1.0,  2.0,  0.5))
print(lerp( 2.0, -1.0,  0.5))
print(lerp( 2.0,  2.0,  0.5))
print(lerp( 0.0,  0.0,  0.5))
print(lerp(-2.0, -2.0,  0.5))

#Expected
1.0
1.0
0.0
0.0
0.5
0.5
2.0
0.0
-2.0
print()

print(arclerp( 0.0,  2.0,  1.0))
print(arclerp( 2.0, -0.0,  1.0))
print(arclerp(-2.0,  2.0,  0.0))
print(arclerp( 2.0, -2.0,  0.0))
print(arclerp(-1.0,  2.0,  0.5))
print(arclerp( 2.0, -1.0,  0.5))
print(arclerp( 2.0,  2.0,  2.0))
print(arclerp( 0.0, -0.0,  0.5))
print(arclerp(-2.0, -2.0, -2.0))

#Expected
0.5
0.5
0.5
0.5
0.5
0.5
0.5
0.5
0.5
print()

print(lerpa( 2.0,  0.5,  1.0))
print(lerpa( 0.0,  0.5,  1.0))
print(lerpa( 2.0,  0.5,  0.0))
print(lerpa(-2.0,  0.5,  0.0))
print(lerpa( 2.0,  0.5,  0.5))
print(lerpa(-1.0,  0.5,  0.5))
print(lerpa( 2.0,  0.5,  2.0))
print(lerpa( 0.0,  0.5,  0.0))
print(lerpa(-2.0,  0.5, -2.0))

#Expected
0.0
2.0
-2.0
2.0
-1.0
2.0
2.0
0.0
-2.0
print()

print(lerpb( 0.0,  0.5,  1.0))
print(lerpb( 2.0,  0.5,  1.0))
print(lerpb(-2.0,  0.5,  0.0))
print(lerpb( 2.0,  0.5,  0.0))
print(lerpb(-1.0,  0.5,  0.5))
print(lerpb( 2.0,  0.5,  0.5))
print(lerpb( 2.0,  0.5,  2.0))
print(lerpb( 0.0,  0.5,  0.0))
print(lerpb(-2.0,  0.5, -2.0))

#Expected
2.0
0.0
2.0
-2.0
2.0
-1.0
2.0
0.0
-2.0
print()
