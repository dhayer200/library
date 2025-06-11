---
id: Reading List
aliases: []
tags: []
---

## my quant roadmap

this is my full stack — everything i’m reading, building, and learning to become a full quant. nothing extra, nothing missing. theory, application, and code — all layered.

---

### 0. Calculus I–III (this is where i’m starting)

| topic                                  | book                                         | reason |
|----------------------------------------|----------------------------------------------|--------|
| calc ii, calc iii, vector calc         | **wrede – _schaum’s advanced calculus_**     | heavy problem drills, tight explanations, no fluff. gets me through calc ii–iii fast. |

---

### 1. linear algebra, odes, and probability (starts right after calc ii is smooth)

| topic                  | book                                          | why |
|------------------------|-----------------------------------------------|-----|
| linear algebra         | **axler – _linear algebra done right_**       | clean abstract foundations. spectral theorem. proof-focused, not just matrix crunch. |
| differential equations | **arnold – _ordinary differential equations_**| builds intuition, everything’s visual and geometric. i’ll need this for stochastic calc. |
| probability            | **ross – _a first course in probability_**    | covers everything from basic laws to CLT. interview standard, and just solid. |

i’ll probably do axler and ross at the same time, then bring in arnold once eigenvalues make sense.

---

### 2. analysis and transforms (start after ross §5–7 feels tight)

| topic                     | book                                               | purpose |
|---------------------------|----------------------------------------------------|---------|
| real analysis (selective) | **rudin – _principles of mathematical analysis_**  | need this for theoretical rigor — limits, sequences, convergence. essential for deeper finance math later. |
| fourier/pde/complex       | **boas – _mathematical methods in the physical sciences_ (ch 5–7, 13)** | fills in gaps. quick punch of everything i skipped from physics/applied math books. |

only doing key chapters from boas — not reading it end to end.

---

### 3. numerical methods + optimization (start once fourier stuff from boas is solid)

| topic                        | book                                         | why |
|------------------------------|----------------------------------------------|-----|
| numerical analysis           | **burden & faires – _numerical analysis_**   | every method in one place. discretizing PDEs, root finding, numerical error — critical for implementation. |
| convex + nonlinear opt       | **boyd & vandenberghe – _convex optimization_** | this is what everyone uses in quant and ML. it's the standard. |

i’ll do boyd after burden, once i’ve got a grip on matrix conditioning and basic iterative methods.

---

### 4. econometrics + time series (can run alongside numerical)

| level     | book                                                | use-case |
|-----------|-----------------------------------------------------|----------|
| undergrad | **brooks – _intro to econometrics for finance_**    | example-heavy and fast. gets me into regressions + time series quick. |
| grad      | **hamilton – _time series analysis_**               | this is the real deal — ARIMA, GARCH, Kalman, everything the PhDs actually use. |

start with brooks, move into hamilton chapter-by-chapter when i need depth.

---

### 5. stochastic calculus + monte carlo (only after i’m clean on 1C, 2A, and 3)

| topic                     | book                                                             | reason |
|---------------------------|------------------------------------------------------------------|--------|
| stochastic calculus       | **karatzas & shreve – _brownian motion and stochastic calculus_** | this is the deepest, most legit quant SDE book. i’ll pair with shreve vol 1 when needed. |
| monte carlo + greeks      | **glasserman – _monte carlo methods in financial engineering_** | pricing via simulation, variance reduction, pathwise tricks. must-know for real pricing work. |

this is the phase where things go from theory to trading math.

---

### 6. risk + derivatives “desk books” (read these during stochastic calc)

| domain                    | book                                               | why |
|---------------------------|----------------------------------------------------|-----|
| options + derivatives     | **hull – _options, futures, and other derivatives_**| everyone uses this. practical recipes. great for desk context. |
| market risk               | **dowd – _measuring market risk_**                | VaR, backtesting, stress testing. still shows up in job postings. |

these are plug-and-play books. not theory-first, but real-world needed.

---

### 7. implementation (code while reading everything above)

| stack        | book                                               | goal |
|--------------|----------------------------------------------------|------|
| C++ systems  | **joshi – _C++ design patterns and derivatives pricing_** | production-style pricing engines, object-oriented MCs |
| python stack | **hilpisch – _python for finance_ (2nd ed.)**      | pandas, NumPy, vectorized Greeks — ties into my NumPy lab |

as i read each theory book, i’ll write code here — no passive reading.

---

### 8. systematic trading, ML, position sizing (final application phase)

| topic                        | book                                                     | why |
|------------------------------|----------------------------------------------------------|-----|
| rule-based strategies        | **carver – _systematic trading_**                        | pure gold. how to size, allocate, and build strategies from the ground up. |
| ML alpha & regime detection  | **lopez de prado – _advances in financial ML_**          | walk-forward testing, labeling, feature engineering — all the tools quants use now. |
| leverage + money management  | **vince – _leverage space trading model_** or _math of money management_ | kelly criterion on steroids. risk frameworks that go beyond just “don’t overleverage.” |

start with carver, move to LdP once my python game is tight, then bring in vince while testing edge cases.

---

## progress order (no fake deadlines, just dependencies)

1. schaum’s advanced calc → finish all relevant calc II–III drills  
2. axler + ross in parallel → start arnold when you hit eigenvalues  
3. rudin selectively → then boas (only ch 5–7, 13)  
4. burden & faires → boyd while reading brooks  
5. re-read ross §5–8 → then hit karatzas & shreve + glasserman  
6. add hull + dowd while doing monte carlo + greeks in code  
7. work through hamilton proofs while building ARIMA/GARCH backtests  
8. once MC and VaR tools are coded → start carver, LdP, and vince

---

this roadmap builds *everything* — math, probability, models, risk, code, ML, and trading logic.  
when this is done, i'll have a quant foundation that doesn’t just match a graduate program — it surpasses it.

all of this tbh is kind of tenative, i expect to add and remove more and more topics as time elapses, but it's good for now. currently reading hull, finishing schaum's, doing axler's linear algebra, and using synopsis of elementary results by carr as a little bedtime reading.
