% FACTS
parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, pat).
parent(bob, ann).
parent(pat, jim).
parent(liz, rahul).

male(bob).
male(tom).
male(jim).
male(rahul).

female(pat).
female(pam).
female(liz).
female(ann).

% RULES
grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

brother(X, Y) :-
    male(X),
    sibling(X, Y).

sister(X, Y) :-
    female(X),
    sibling(X, Y).

uncle(X, Y) :-
    brother(X, Z),
    parent(Z, Y).

aunt(X, Y) :-
    sister(X, Z),
    parent(Z, Y).

cousin(X, Y) :-
    parent(P1, X),
    parent(P2, Y),
    sibling(P1, P2).
