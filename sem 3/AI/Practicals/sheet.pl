% 2. CONCAT

conc([], L, L) :- !.
conc([H|T], L, [H|R]):-
    conc(T, L, R).

% 3. REVERSE

reverse(L, R):-
    reverse(L, [], R).
reverse([], Acc, Acc) :- !.
reverse([H|T], Acc, R):-
    reverse(T, [H|Acc], R).

% 4. SUM

sum(X, Y, S):-
    S is X + Y.

% 5. MAX

max(X, Y, M):-
    X > Y -> M = X; M = Y.

% 6. FACTORIAL

factorial(1, 1) :- !.
factorial(N, F):-
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

% 7. FIBONACCI

generate_fib(0, 0) :- !.
generate_fib(1, 1) :- !.

generate_fib(N, T) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    generate_fib(N1, T1),
    generate_fib(N2, T2),
    T is T1 + T2.

% 8. POWER

power(_, 0, 1) :- !.
power(N1, 1, N1) :- !.
power(N1, N2, R):-
    SN2 is N2 - 1,
    power(N1, SN2, R1),
    R is R1 * N1.

% 9. MULTIPLY

multi(N1, 1, N1) :- !.
multi(N1, N2, R):-
    SN2 is N2 - 1,
    multi(N1, SN2, R1),
    R is R1 + N1.

% 10. LIST MEMBER

memb(X, [X|_]) :- !.
memb(X, [_|T]):-
    memb(X, T).


% 11. SUM LIST

sumlist([], 0) :- !.
sumlist([H|T], S):-
    sumlist(T, S1),
    S is H + S1.

% 12. EVEN ODD

evenlength([_], N) :-
    0 is N mod 2, !.
evenlength([_|T], N) :-
    N1 is N + 1,
    evenlength(T, N1).
evenlength(R) :-
    evenlength(R, 1).

oddlength([_], N) :-
    1 is N mod 2, !.
oddlength([_|T], N) :-
    N1 is N + 1,
    oddlength(T, N1).
oddlength(R) :-
    oddlength(R, 1).

% 13. MAX

maxlist([X], X) :- !.
maxlist([H|T], M) :-
    maxlist(T, NM),
    (H > NM -> M = H; M = NM).

% 14. INSERT

insert(I, 1, L, [I|L]) :- !.
insert(I, N, [H|T], [H|R]) :-
    N > 1,
    N1 is N - 1,
    insert(I, N1, T, R).

% 15. DELETE

del(1, [_|L], L) :- !.
del(N, [H|T], [H|R]) :-
    N > 1,
    N1 is N - 1,
    del(N1, T, R).

% EXTRAS

% LENGTH

len([_], 1) :- !.
len([_|T], L):-
    len(T, L1),
    L is L1 + 1.

% GCD

gcd(X, 0, X) :- X > 0, !.
gcd(X, Y, G) :-
    Y > 0,
    R is X mod Y,
    gcd(Y, R, G).

