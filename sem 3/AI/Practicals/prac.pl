conc([], L2, L2) :- !.
conc([H|T], L2, [H|R]) :-
    conc(T, L2, R).


reverse(L, R) :-
    reverse(L, [], R).

reverse([], Acc, Acc) :- !.
reverse([H|T], Acc, R) :-
    reverse(T, [H|Acc], R).


sum(A, B, R) :-
    R is A + B.


max(A, B, R) :-
    A > B -> R = A; R = B.

factorial(1, 1) :- !.
factorial(A, R) :-
    A1 is A - 1,
    factorial(A1, R1),
    R is A * R1.

generate_fib(1, 1) :- !.
generate_fib(0, 0) :- !.
generate_fib(N,T) :-
    N1 is N - 1,
    N2 is N - 2,
    generate_fib(N1, T1),
    generate_fib(N2, T2),
    T is T1 + T2.

power(N, 1, N) :- !.
power(N, P, A) :-
    P1 is P - 1,
    power(N, P1, A1),
    A is A1 * N.

multi(N1, 1, N1) :- !.
multi(N1, N2, R) :- 
    NN2 is N2 - 1,
    multi(N1, NN2, R1),
    R is R1 + N1.

memb(X, [X|_]) :- !.
memb(X, [_|T]) :-
    memb(X, T).


sumlist([], 0) :- !.
sumlist([H|T], S) :-
    sumlist(T, S1),
    S is H + S1.


evenlength([H|T]) :-
    evenlength([H|T], S),
    0 is S mod 2.

evenlength([_], 1) :- !.
evenlength([_|T], S) :-
    evenlength(T, S1),
    S is 1 + S1.


oddlength([H|T]) :-
    oddlength([H|T], S),
    1 is S mod 2.

oddlength([_], 1) :- !.
oddlength([_|T], S) :-
    oddlength(T, S1),
    S is 1 + S1.

maxlist([X], X) :- !.
maxlist([H|T], M) :-
    maxlist(T, M1),
    (H > M1 -> M = H; M = M1).


insert(I, 1, L, [I|L]) :- !.
insert(I, N, [H|T], [H|R]) :-
    N1 is N - 1,
    insert(I, N1, T, R).


delete(1, [_|T], T):- !.
delete(N, [H|T], [H|R]) :-
    N1 is N - 1,
    delete(N1, T, R).
    
% GCD

gcd(X, 0, X) :- X > 0, !.
gcd(X, Y, G) :-
    Y > 0,
    R is X mod Y,
    gcd(Y, R, G).

