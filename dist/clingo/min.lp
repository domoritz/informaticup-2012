% Define

% Optimize
#minimize [ cycle(X,Y) : expenses(X,Y,E) = E, minimum_cost(P,C) = C ].

%bought(P,X,C) :- minimum_cost(P,C), cost(P,X,C), selected(X).

% Display
#hide.
%#show bought/3.
%#show minimum_cost/2.
