gcd(X, 0, X).
gcd(X, Y, G) :-
    Y > 0, X > 0,
    R is X mod Y,
    gcd(Y, R, G).

mul(0, _, 0).
mul(_, 0, 0).
mul(X, 1, X).
mul(1, Y, Y).
mul(X, Y, Z) :-
    X > 0, Y > 0,
    X1 is X - 1,
    mul(X1, Y, Z1),
    Z is Z1 + Y.

pow(_, 0, 1).
pow(1, _, 1).
pow(X, 0, 1).
pow(X, 1, X).
pow(X, Y, Z) :-
    Y > 1,
    Y1 is Y - 1,
    pow(X, Y1, Z1),
    Z is Z1 * X.

fib(0, 0).
fib(1, 1).
fib(N, F) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fib(N1, F1),
    fib(N2, F2),
    F is F1 + F2.