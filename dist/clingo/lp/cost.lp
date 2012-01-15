% Edge Costs/ Traveling Expenses
% from program:
% expenses(0,1,300). expenses(0,2,400). expenses(0,3,600).
% expenses(1,2,200). expenses(1,3,500).
% expenses(2,3,300).

expenses(X,Y,E) :- expenses(Y,X,E). 

% Product Costs
% from program:
% cost(1,1,1495). cost(1,2,1699). cost(1,3,1150).
% cost(2,1,499).	cost(2,2,459). cost(2,3,499).
% cost(3,2,1290). cost(3,3,1199).
% cost(4,1,599). cost(4,2,455). cost(4,3,495).
% cost(5,1,1990). cost(5,2,1995).
% cost(6,2,819). cost(6,3,799).
