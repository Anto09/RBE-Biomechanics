clc
clear

syms t1 t2 t1d t2d

l1 = 20;
l2 = 18;

r1 = l1/2;
r2 = l2/2;

m1 = 3;
m2 = 2;

z1 = (1/12)*m1*l1*l1;
z2 = (1/12)*m2*l2*l2;

x1d = -r1*sin(t1)*t1d;
y1d = r1*cos(t1)*t1d;

x2d = -(l1*sin(t1) + r2*sin(t1+t2))*t1d - r2*sin(t1+t2)*t2d;
y2d = (l1*cos(t1) + r2*cos(t1+t2))*t1d + r2*cos(t1+t2)*t2d;

kinetic = 0.5*m1*(x1d*x1d + y1d*y1d) + 0.5*z1*t1d*t1d + 0.5*m2*(x2d*x2d + y2d*y2d) + 0.5*z2*(t1d+t2d)*(t1d+t2d);

h1 = r1*sin(t1);
h2 = r2*sin(t1+t2);
g = -9.8;

potential = m1*g*h1 + m2*g*h2;

lagrangian = kinetic - potential;
lagrangian