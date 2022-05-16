n = 1; 
m = 1;

E = [y,u];

% y_dot = diff(y);
% h = [0;y_dot];
h = y_dot;

XX = (E' * E)^(-1) * E' * h;
X21 = XX';
XA = X21(:,1:n);
XB = X21(:,n+1:end);
XC = eye(n,n);
XD = zeros(n,m);

pilot01 = ss(XA, XB, XC, XD);

% Wc = tf(2, [1 2]);

% CL = feedback(Wc*pilot01,1);