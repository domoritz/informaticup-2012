% Generate
selected(0).
{ selected(X) } :- node(X).
1 { cycle(X,Y) : edge(X,Y) } 1 :- selected(X).
1 { cycle(X,Y) : edge(X,Y) } 1 :- selected(Y).

% Define
reached(0).
reached(Y) :- cycle(X,Y), reached(X).
:- selected(X), not reached(X).

cost(P,C) :- cost(P,Y,C).
selected_costs(P,C) :- selected(Y), cost(P,Y,C).

sorted_costs(P,C1,C2) :- cost(P,C1), cost(P,C2), C1<C2, not cost(P,C3):cost(P,C3):C1<C3:C3<C2.
first_sorted_cost(P,C) :- product(P), C = #min [ cost(P,CC) = CC ], C != #supremum.
not_minimum_cost(P,C) :- first_sorted_cost(P,C), not selected_costs(P,C).
not_minimum_cost(P,C) :- not_minimum_cost(P,C2), sorted_costs(P,C2,C), not selected_costs(P,C).

minimum_cost(P,C) :- first_sorted_cost(P,C), not not_minimum_cost(P,C).
minimum_cost(P,CC) :- not_minimum_cost(P,C), sorted_costs(P,C,CC), not not_minimum_cost(P,CC).

bought(P) :- cost(P,Y,C), selected(Y).
:- not bought(P), product(P).

%somehow we need this additional option
:- cycle(X,Y), cycle(Z,Y), Z!=X.

% Display
#hide.
#show cycle/2.
