% Nodes
node(0..3).

% (Directed) Edges
edge(X,Y) :- node(X),node(Y),X!=Y.

% Products
product(1..6).

