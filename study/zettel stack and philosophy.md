---
id: "1"
aliases:
  - stack
tags:
  - zettel
---

## the stack
[ ] vimtex
[ ] obsidian.nvim
[ ] markdown previewer
## the philosophy
what we're doing is trying to make our notes so excessible, that we can choose one from random and just write about it. 
an atomic note: one idea per note, made from your own thought, linked to other notes, a brick placed for a house in your second brain
we'll be using this for two types of notes, one for math, and one for non math
math notes will only be done in LaTeX at the final stage, permanent and post-permanancy
we have three different type of notes
1. fleeting
2. literature
3. permanent & post-permanancy
### fleeting notes (.md only)
all of your fleeting notes should be either referenced to permanent notes or discarded in 24 hours, a python script will clean this up (find when .md file was created, if >= 24h, deleted).
these are for quick **jots** or **scratch work**. You will revisit these when writing your permanent notes.

if we were writing on improper integrals:
% Fleeting note
% ID: F001
% Date: 06/10/2025
% Note: Improper integrals 
Looks like you need to make $\lim_{b \to \infinity}.
Looks cool, compare it to series later, find out who first discovered them.
Chapter 10 schaum's outline, come back later

### literature notes (.md only)
all of your literature notes should be either referenced to permanent notes or discarded in 24 hours, a python script will clean this up for you.
these are for *references*, so don't take too long. think of formulas, theorems, theories, etc.
literature notes are referenced to permanent notes
% Literature note 
% ID: L001
% Date: 06/10/2025
% Note: Improper integrals formula 
$$
    \text{insert math here}
.$$

\textbf{Special case when x: }

### permanent notes (.tex -> pandoc -> .md)
after all your problems are finished, you finished your literature and fleeting notes, and you understand the chapter, you move onto your permanent notes, the true atomicness
this is all in your own words using the fleeting notes and literature notes you previously written, with this in mind, you can also use dates as id so you can access them better, but you still dont really need it

this is a true zettel, one idea, linked to other ideas, you can use either vimtex or obsidian.nvim for this stage, the others are exclusively obsidian.nvim. import your work here.

% PERMANENT NOTE 
% ID: P1
% Date: 06/10/2025
% Note: Improper integrals 
...

% import of problems done on paper:

