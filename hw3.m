syms x

a = 2.57;
b = 0.89;
y0 = 10.0;
y0r = y0;
ar = 1.02*a;
br = 0.97*b;
cr = -0.01;
x0 = 1.00;
x1 = 30.00;
x2 = 10.00;
e1 = 2.2 * 10.0^-2;
e2 = 1.34 * 10.0^-1;

y_true(x) = y0r + ar*x + br*x^2 + cr*x^3
y_obs(x) = y0 + a*x +b*x^2

error(x) = (y_true - y_obs)/y_true

y_true1(x) = y0r + ar*(x+e1) + br*(x+e1)^2 + cr*(x+e1)^3
y_obs1(x) = y0 + a*(x+e1) +b*(x+e1)^2

error1(x) = (y_true1 - y_obs1)/y_true1


y_true2(x) = y0r + ar*(x+e1+e2*(x-x1)) + br*(x+e1+e2*(x-x1))^2 + cr*(x+e1+e2*(x-x1))^3
y_obs2(x) = y0 + a*(x+e1+e2*(x-x1)) +b*(x+e1+e2*(x-x1))^2

error2(x) = (y_true2 - y_obs2)/y_true2