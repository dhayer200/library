# 🧠 mylibrary

> *“I study myself more than any other subject. That is my metaphysics, that is my physics.”*  
> — Michel de Montaigne

## Who Am I?

I’m Deep Hayer, 15 years old, from Austin, Texas. I’ve been in college since I was 12. My focus is quantitative finance, systems trading, and self-mastery.

This repo is a record of rigor, reflection, and execution. It’s how I study math, code, finance, and myself.

The best thinkers didn’t just learn — they wrote, reflected, revised. This is how I build systems. This is how I build myself.

## Structure

Nothing here is static. Code, notes, and structure will evolve.

### 🧾 `/library/`

This is my Zettelkasten system:
- **Fleeting Notes**: raw ideas, unfiltered thoughts
- **Literature Notes**: knowledge pulled from books, lectures, papers
- **Permanent Notes**: linked concepts, derivations, essays — inspired by Montaigne

### 🧠 `/code/`

Same structure, in code:
- **`/fleeting/`**: scratch scripts, math jots, problem solvers
- **`/literature/`**: code based on books, tutorials, reference materials
- **`/permanent/`**: full projects, simulation engines, quant toolkits

Topics include:
- Calculus, linear algebra, probability, statistics
- Real analysis, ODEs, stochastic calculus
- Monte Carlo methods, portfolio optimization, risk modeling
- Strategy engines, systematic trading, data pipelines
- Philosophy amongst the likes of Montaigne, Plato, Nietzche, and more...

This is going to be a mix of rigourous writing that of Montaigne, but simultaneously showing my entire thought process, even that of what might be seen as "sporadic."

## Why?

Mastery means solving problems while understanding yourself. This is a place to write, build, and think in public. No wasted thoughts.

## Goal

The goal is to set a standard. To show that even one person, documenting clearly and building deliberately, can go deep. If you’re learning, moving, building — document it. Own it.

This is my work. But at the same time, what is mine, is yours.

## the zettel stack

- [ ] vimtex  
- [ ] obsidian.nvim  
- [ ] markdown previewer  

---

## the philosophy

what we're doing is making our notes so accessible that we can pick one at random and immediately start writing about it.  
an atomic note: one idea per note, made from your own thought, linked to other notes. a brick in your second brain.

we’ll be using this for two kinds of notes: math and non-math.  
math notes will be LaTeX-only at the final stage — permanent and post-permanency.

---

## types of notes

### 1. fleeting notes (`.md` only)

fleeting notes must be referenced or deleted within 24 hours. a python script handles cleanup.  
use these for quick **jots** or **scratch work** while reading or thinking.

> **Example:**
```markdown
% Fleeting note  
% ID: F001  
% Date: 06/10/2025  
% Note: Improper integrals  

looks like you need to make $\lim_{b \to \infty}$.  
compare it to series later. who discovered them first?  
chapter 10, schaum’s outline — come back later.
```

### 2. literature notes (.md only)

same deal — either referenced or deleted in 24 hours.
these are for references, so don’t take too long writing these. think formulas, theorems, rules, definitions, anything from books or lectures.
you use these when you're writing permanent notes — they’re support material, not the main idea.

> **Example:**
```
% Literature note  
% ID: L001  
% Date: 06/10/2025  
% Note: Improper integrals formula  

$$
\int_a^{\infty} f(x) \, dx = \lim_{b \to \infty} \int_a^b f(x) \, dx
$$

textbook says something about convergence, but come back to that when writing permanent.  
also check if there's a special case when $x = \text{some bound}$
```

### 3. permanent notes (.tex → pandoc → .md)

this is where it gets serious. after all your problems are done, you’ve finished your fleeting + literature notes, and you actually get the chapter, you move on to writing your permanent notes — the true atomic ones.

these are written 100% in your own words, and they’re linked to everything else. this is the idea. this is where the thought lives.

you write these in LaTeX, either with vimtex or obsidian.nvim. once it’s clean, you run it through pandoc and convert it into .md so it integrates with your vault.

> **Example**:
```
% PERMANENT NOTE  
% ID: P001  
% Date: 06/10/2025  
% Note: Improper integrals  

a function $f(x)$ is said to have an improper integral over $[a, \infty)$ if...

you define it like this:

$$
\int_a^{\infty} f(x) \, dx = \lim_{b \to \infty} \int_a^b f(x) \, dx
$$

you can use comparison tests if the limit doesn’t exist.

% import of problems done on paper goes here
```
