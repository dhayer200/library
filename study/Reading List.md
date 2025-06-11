---
id: Reading List
aliases: []
tags: []
---
Below is the **same roadmap** you gave me—**unchanged**—with **three new books** inserted in their own section so you can drop-paste straight into Obsidian.

---

### 0. Calculus I-III **(you’re here)**

| Topic                                   | Primary text                             | Why this text?                                            |
| --------------------------------------- | ---------------------------------------- | --------------------------------------------------------- |
| Single-/multivariable calc, vector calc | **Wrede – _Schaum’s Advanced Calculus_** | Fast drill-heavy review; knocks out Calc 2-3 conventions. |

---

### 🏗️ 1. Linear & Differential Core (start as soon as Calc II material feels natural)

| Sequence               | Primary text                                   | What to master                                                                                                                                                                     |
| ---------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1A. Linear algebra     | **Axler – _Linear Algebra Done Right_**        | Abstract vector spaces, eigen-stuff, spectral theorem. Reddit & Math.SE threads still rank Axler the top proof-oriented LA book for quants. ([reddit.com](https://www.reddit.com)) |
| 1B. Ordinary DEs       | **Arnold – _Ordinary Differential Equations_** | Geometric view; builds intuition you’ll reuse in stochastic calculus.                                                                                                              |
| 1C. Probability theory | **Ross – _A First Course in Probability_**     | Full undergrad probability toolkit; industry-standard for quant interviews. ([amazon.com](https://www.amazon.com))                                                                 |

Do 1A and 1C in parallel if you like variety; slot Arnold after Axler’s eigen material so phase-plane analysis makes sense.

---

### 2. Analysis & Transforms (begin once Ross §5–7 feel solid)
| Sequence                                                                  | Primary text                                                            | What it patches                                                                               |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 2A. Real/metric analysis (select chapters)                                | **Rudin – _Principles of Mathematical Analysis_**                       | Limits, continuity, sequences of functions—needed for Karatzas-Shreve proofs later.           |
| 2B. Fourier/Laplace, PDE intro, complex variables, vector-calc identities | **Boas – _Mathematical Methods in the Physical Sciences_ (Ch 5–7, 13)** | Fills every missing Kreyszig topic in one lean volume. ([reddit.com](https://www.reddit.com)) |

Skim Boas surgically—only the chapters above.

---

### 3. Numerical & Optimization (start after Boas Fourier/PDE chapters)

| Topic                                                       | Primary text                                               | Why this text?                                                                                                                   |
| ----------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Numerical algorithms (roots, ODE/PDE discretisation, error) | **Burden & Faires – _Numerical Analysis_**                 | Still the go-to “all algorithms in one” text; learners praise its balance of math & code. ([reddit.com](https://www.reddit.com)) |
| Convex & nonlinear optimisation                             | **Boyd & Vandenberghe – _Convex Optimization_** (free PDF) | Industry standard for portfolio & calibration problems. ([stanford.edu](https://web.stanford.edu/~boyd/cvxbook/))                |

Do Boyd after Burden so matrix conditioning & line-search ideas aren’t foreign.

---

### 4. Econometrics & Time-Series (run in parallel with Numerical)

| Level                 | Primary text                                         | Use-case                                                                                  |
| --------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Undergrad / fast ramp | **Brooks – _Introductory Econometrics for Finance_** | Quick, example-driven intro. ([amazon.com](https://www.amazon.com))                       |
| Grad / full depth     | **Hamilton – _Time Series Analysis_**                | ARIMA-GARCH-Kalman proofs; gold-standard PhD text. ([reddit.com](https://www.reddit.com)) |

Start with Brooks, then dip into Hamilton chapter-by-chapter as you need rigor.

---

### 📈 5. Stochastic Calculus & Monte-Carlo (only after 1C, 2A, 3 are comfortable)

| Topic                           | Primary text                                                    | Why this text?                                                                                                                  |
| ------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | | Continuous-time finance math    | **Karatzas & Shreve – _Brownian Motion & Stochastic Calculus_** | Deepest finance-flavoured stochastic calculus (combine with Shreve Vol I for intuition). ([amazon.com](https://www.amazon.com)) |
| Variance-reduction & MC pricing | **Glasserman – _Monte Carlo Methods in Financial Engineering_** | Industry bible for MC Greeks & pathwise tricks. ([amazon.com](https://www.amazon.com))                                          |

---

### 🛡️ 6. Risk & Derivatives “Desk Books” (read concurrently with stochastic calc)

|Domain|Primary text|Purpose|
|---|---|---|
|Vanilla & exotic derivatives|**Hull – _Options, Futures & Other Derivatives_**|Practical pricing cookbook.|
|Market-risk metrics (VaR/ES)|**Dowd – _Measuring Market Risk_**|Implement VaR back-tests; still cited in 2025 risk-job ads. ([amazon.com](https://www.amazon.com))|

---

### 💻 7. Implementation Layer (code while you study everything above)

|Stack|Primary text|Goal|
|---|---|---|
|C++ engines & patterns|**Joshi – _C++ Design Patterns and Derivatives Pricing_**|Production-style Monte-Carlo and lattice engines.|
|Python analytics|**Hilpisch – _Python for Finance_ (2nd ed.)**|Pandas, NumPy, vectorised Greeks; pairs with your NumPy project.|

---

### ⚙️ 8. Systematic Trading, ML Alpha & Position Sizing **(application layer)**

|Focus area|Primary text|Why it’s worth adding|
|---|---|---|
|End-to-end systematic trading rules|**Carver – _Systematic Trading_**|Turns forecasts & risk constraints into live position sizes.|
|ML feature engineering / regime detection|**López de Prado – _Advances in Financial Machine Learning_**|Walk-forward purging, fractional differentiation, DFML “edge” tricks all quants cite in 2025.|
|Optimal leverage & money management|**Vince – _The Leverage Space Trading Model_ (or _Mathematics of Money Management_)**|Deep dive on sizing capital using Kelly/leverage-space; complements VaR & MC tools.|

Read Carver first (pairs well with Brooks back-tests), move to López de Prado when your Python stack is solid, then Vince while refining risk engines.

---

## 🗺️ **Progress Timeline (no fixed dates, just dependency order)**

1. **Calc II-III refresh** – finish Schaum’s problem sets.
    
2. **Axler + Ross** (parallel); start **Arnold** once Axler Ch 6+ done.
    
3. **Selective Rudin** (limits → integration) then **Boas Ch 5–7, 13**.
    
4. **Burden & Faires** → **Boyd** while dabbling in **Brooks** examples.
    
5. Re-read key Ross chapters, then tackle **Karatzas & Shreve** (pair with Shreve Vol I for intuition).
    
6. Alongside stochastic calc, work through **Glasserman** MC chapters and **Hull** pricing recipes; implement in Python/C++.
    
7. Finish **Hamilton** time-series proofs as you build ARIMA/GARCH back-tests.
    
8. Layer on **Dowd** VaR/ES & stress testing once MC tools run.
    
9. **Carver** for systematic framework → **López de Prado** for ML alpha → **Vince** for advanced position sizing as you productionise strategies.
    

By the end of step 9 you’ll have every math, stats, risk, ML, and execution tool a modern front-office quant or systematic-trading quant needs—nothing extra, nothing missing.
 
