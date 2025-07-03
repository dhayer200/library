# mylibrary

> _“i study myself more than any other subject. that is my metaphysics, that is my physics.”_  
> — michel de montaigne

## who am i?

i’m deep hayer, 15 years old, from austin, texas. i’ve been in college since i was 12.

this repo is a record of rigor, reflection, and execution. it’s how i study myself.

the best thinkers didn’t just learn — they wrote, reflected, revised. this is how i build systems. this is how i build myself.

## structure

nothing here is static. code, notes, and structure will evolve. tenative.

## library

this is my zettelkasten system:

- **fleeting notes**: ideas that come to you, write all of them, if not near a laptop, iPad concepts processed later, notebook + pencil + eraser always on hand, voice recordings
    
- **literature notes**: knowledge pulled from books, lectures, papers, something you want to remember and use later in your permanent notes
    
- **permanent notes**: linked concepts, derivations, essays — inspired by montaigne, you are writing papers to inform others, liberating others with sharing your ideas
    

###  `/code/`

implementations of fleeting notes, literature notes and permanent notes


### what will be here? 

anything, to limit my writing to one specific thing would be an injustice, write about anything, i'm mainly channeling montaigne.

## why?

mastery means solving problems while understanding yourself. this is a place to write, build, and think in public. no wasted thoughts.

## goal

the goal is to set a standard. to show that even one person, documenting clearly and building deliberately, can go deep. if you’re learning, moving, building — document it. own it.

this is my work. but at the same time, what is mine, is yours.

## the zettel stack

-  vimtex
    
-  obsidian.nvim
    
-  markdown previewer
    

---

## the philosophy

what we're doing is making our notes so accessible that we can pick one at random and immediately start writing about it.  
an atomic note: one idea per note, made from your own thought, linked to other notes. a brick in your second brain.

we’ll be using this for two kinds of notes: math and non-math.  
math notes will be latex-only at the final stage — permanent and post-permanency.

---

## music

if ur listening to music thats buns, ur gonna perform like buns, simple
i be listening to hella ug
but it gotta be chill
1oneam
summrs
even house sometimes (like garage)
breakcore puts u in the mood
ambience... fire
izaya tiji
classical music too lowkey i recommend it 
first mathematician to listen to elijxhwtf 2025

---

## types of notes

### 1. fleeting notes (written anywhere, key word is spontaneous, idea comes to you, write it ASAP, if written physically scan it and send to self)

fleeting notes must be referenced or deleted within 24 hours. a python script handles cleanup.  
use these for quick **jots** or **scratch work** while reading or thinking.

> **example:**
> 
> ```markdown
> ---
> id: F001
> aliases:
>  - improper integrals
> tags:
>  - fleeting
>  - schaums
>  - calculus
>  - integrals
> date: 06/20/2025
> --- 
> looks like you need to make $\lim_{b \to \infty}$.  
> compare it to series later. who discovered them first?  
> chapter 10, schaum’s outline — come back later.
> ```

### 2. literature notes (`.md` only)

same deal — either referenced or deleted in 24 hours.  
these are for references, so don’t take too long writing these. think formulas, theorems, rules, definitions, anything from books or lectures.  
you use these when you're writing permanent notes — they’re support material, not the main idea.

> **example:**
> 
> ```markdown
> ---
> id: L001
> aliases:
>  - improper integrals
> tags:
>  - literature
>  - schaums
>  - calculus
>  - integrals
> date: 06/20/2025
> ---  
> $$
> \int_a^{\infty} f(x) \, dx = \lim_{b \to \infty} \int_a^b f(x) \, dx
> $$
> 
> textbook says something about convergence, but come back to that when writing permanent.  
> also check if there's a special case when $x = \text{some bound}$
> ```

### 3. permanent notes (`.tex` → pandoc → `.md`)

this is where it gets serious. after all your problems are done, you’ve finished your fleeting + literature notes, and you actually get the chapter, you move on to writing your permanent notes — the true atomic ones.

these are written 100% in your own words, and they’re linked to everything else. this is the idea. this is where the thought lives.

you write these in latex, either with vimtex or obsidian.nvim. once it’s clean, you run it through pandoc and convert it into `.md` so it integrates with your vault.

> **example:**
> 
> ```latex -> markdown / markdown
> ---
> id: 1
> aliases:
>  - improper integrals
> tags:
>  - literature
>  - schaums
>  - calculus
>  - integrals
> date: 06/20/2025
> ---   
> a function $f(x)$ is said to have an improper integral over $[a, \infty)$ if...
> 
> you define it like this:
> 
> $$
> \int_a^{\infty} f(x) \, dx = \lim_{b \to \infty} \int_a^b f(x) \, dx
> $$
> 
> you can use comparison tests if the limit doesn’t exist.
> ```

---


## note conversion pipeline

> how i seamlessly convert my notes between latex, markdown, and pdf on macos

---

### 1. latex → markdown

- **tool**: `pandoc`
    
- **command**:
    
    ```bash
    pandoc file.tex -o file.md
    ```
    
- **notes**:
    
    - i preserve headings and inline math (`$…$`, `$$…$$`)
        
    - equations default to `$$…$$`
        
    - to transform into `align` blocks:
        
        ```bash
        sed -i '' 's/\$\$\n\\begin{aligned}/\\begin{align}/g' file.md
        sed -i '' 's/\\end{aligned}\n\$\$/\\end{align}/g' file.md
        ```
        

---

### 2. scanned handwritten notes → `.md` / `.tex` / `.pdf`

- **primary tool**: **mathpix snip**
    
    1. install on macos
        
    2. open your scan (preview or pdf expert)
        
    3. snip equations or blocks → outputs:
        
        - markdown with embedded latex
            
        - raw latex (incl. `\begin{align}…\end{align}`)
            
        - export to `.tex` or `.pdf` directly
            
    4. paste into my vault
        
- **alternative (free)**: `ocrmypdf` + manual cleanup
    
    ```bash
    brew install ocrmypdf
    ocrmypdf input.pdf output.pdf
    ```
    
    → then feed snippets into mathpix or hand-format equations
    

---

### 3. ipad notes (concepts/freeform pdf) → `.md` / `.tex` / `.pdf`

- **purely handwritten**:
    
    1. export pdf from concepts
        
    2. drag into mathpix snip → choose latex/markdown output
        
- **mixed diagrams + handwriting**:
    
    1. export pdf via notability
        
    2. use mathpix to extract text and equations
        
    3. optionally run `pdfimages` to grab raw drawings
        

---

## 🧰 toolset (macos)

|task|tool|notes|
|---|---|---|
|`.tex` → `.md`|`pandoc`|great structure; use `sed` for `align`|
|image/pdf → `.md` / `.tex`|mathpix snip|best-in-class ocr + math parser|
|batch ocr (full document)|`ocrmypdf` + mathpix|ocr then snippet extraction via mathpix|

---

> with this pipeline, every formula, block, and thought lives in my zettelkasten
