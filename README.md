# Food Magnate — Group Programming Task

**AQA A-Level Computer Science (7517) · Paper 1 Skeleton Program**
Year 12 · Group Activity · Python

---

## Table of Contents

1. [About this repository](#about-this-repository)
2. [What the skeleton program does](#what-the-skeleton-program-does)
3. [Working with GitHub](#working-with-github)
4. [Working as a group](#working-as-a-group)
5. [Task list](#task-list)

---

## About this repository

This repository holds the shared codebase for your group's Paper 1 programming activity. AQA has already provided the base skeleton program — the **Food Magnate simulation**. Your task, working together as a group, is to extend it by implementing as many additional features as possible before the deadline.

There are more tasks here than any one person can finish. Split them up early and you'll score considerably more than if everyone works on the same thing.

---

## What the skeleton program does

Food Magnate is a turn-based economic simulation. Multiple companies compete to generate the most profit by running chains of restaurant outlets across a virtual settlement. Each simulated "day", the program works through a fixed sequence: households decide whether to eat out, outlets serve meals and incur costs, and the balances, reputations, and visit counts all update accordingly.

Before you write a single line of code, read through the existing program carefully. You can't extend something you don't understand.

### The Settlement

The settlement is a coordinate grid representing the virtual town. `Household` objects are distributed across it, each holding a randomised probability that determines whether the household eats out on a given day. A `LargeSettlement` subclass extends the base `Settlement` class — note how inheritance is used here, as this pattern recurs throughout the codebase.

### Companies and Outlets

Each `Company` object owns a collection of `Outlet` objects placed at various positions on the grid. Every outlet carries four key attributes:

| Attribute | What it represents |
|-----------|-------------------|
| `Capacity` | Maximum meals served per day |
| `DailyCosts` | Fixed overheads — staff, rent, and so on |
| `ReputationScore` | Influences how likely households are to choose this outlet |
| `PricePerMeal` | Revenue earned per customer served |

The simulation tracks each outlet's profit, total visits, and cumulative balance across the run.

### Company types

Not all companies operate identically. `NameChef` companies — premium-tier chains — tend to turn a profit more reliably than standard companies. That imbalance is deliberate and directly relevant to several of the tasks below.

### Delivery

Outlets can deliver food rather than requiring customers to visit. Delivery cost scales with the distance between outlet and household, calculated using their grid coordinates. Optimising that delivery route is one of the most algorithmically demanding tasks in this activity.

### The simulation loop

Each day executes in the following order:

```
Start of day
  → Each household evaluates its eat-out probability
  → If eating out: selects a company based on price, reputation, and proximity
  → The outlet serves the meal, logs revenue, and deducts daily costs
  → Balances, reputations, and visit counts update
End of day → Events log summarises what occurred
```

Run the program and step through a few days before you write anything. It's much easier to extend code you've actually seen running.

---

## Working with GitHub

GitHub is where your group's code lives. Every change you make gets saved here so your teammates can see it, build on it, or review it before it becomes part of the main program. All of the steps below use GitHub's website directly — no command line required.

### Step 1 — Get your own copy with a fork (first time only)

If you don't have write access to this repository, start by **forking** it. A fork is your personal copy of the project, hosted under your own GitHub account.

1. Click **Fork** in the top-right corner of this page.
2. Leave the settings as they are and click **Create fork**.
3. You'll land on your own copy at `github.com/YOUR-USERNAME/food-magnate`.

If your teacher has added you directly as a collaborator instead, skip this step — you already have access.

### Step 2 — Create a branch for your task

Never work directly on `main`. Branches let you work on one task in isolation without disturbing what your teammates are doing.

1. On the repository homepage, click the branch dropdown — it will say **main** by default.
2. Type a name for your new branch in the search box, for example: `feature/small-settlement-class` or `feature/currency-formatting`.
3. Click **Create branch: feature/your-task-name from main**.

Keep to one task per branch. It makes reviewing and merging much simpler for everyone.

### Step 3 — Edit files in the browser

GitHub lets you edit Python files directly in the browser — no IDE needed for straightforward changes.

1. Navigate to `food_magnate.py` in the file list.
2. Click the **pencil icon** (Edit this file) in the top-right of the file view.
3. Make sure your active branch is the one you just created, not `main`. Check the dropdown above the file.
4. Write your code in the editor.

For larger tasks, you'll want to download the file, work in your usual IDE, then upload the changed version. To do that:

1. Click the file, then click the **download icon** to save it locally.
2. Make your changes in your IDE and test them.
3. Back on GitHub, navigate to the file and click **Upload files**, or use the pencil editor to paste your updated code in.

### Step 4 — Commit your changes

When you're happy with your code and have tested it, scroll to the bottom of the editor page. You'll see a **Commit changes** section.

1. Write a short, specific message describing what you did — for example: `Add SmallSettlement subclass with reduced capacity defaults`. Vague messages like "update" or "fix" help nobody.
2. Make sure **Commit directly to `feature/your-task-name`** is selected, not `main`.
3. Click **Commit changes**.

Commit regularly as you work, not just once at the end. Frequent commits make it much easier to pinpoint where something went wrong.

### Step 5 — Open a Pull Request

A Pull Request (PR) is how your branch gets reviewed and merged into `main`. It's a way of saying "I've finished — here's what I've done" before it becomes part of the shared code.

1. After committing, GitHub will usually show a banner prompting you to **Compare & pull request**. Click it.
2. If you don't see the banner, go to the **Pull requests** tab and click **New pull request**. Set the base branch to `main` and the compare branch to your feature branch.
3. Write a short description: what does your code do, and what did you test?
4. Assign a teammate as a reviewer.
5. Click **Create pull request**.

Your teammate reviews it. Once they approve, whoever is managing `main` clicks **Merge pull request**.

### Key rules

| Rule | Reason |
|------|--------|
| Always branch from `main` | Ensures you're working from the latest shared code |
| One branch per task | Isolates changes and simplifies review |
| Test before opening a PR | Broken code on `main` blocks the whole group |
| Write descriptive commit messages | Makes it easy to track what changed and why |
| Never commit directly to `main` | All changes go through a branch and a Pull Request |

---

## Working as a group

Agree on who owns which tasks **before anyone starts coding**. A few principles worth establishing upfront:

- **Avoid editing the same function simultaneously.** If two people modify `CalculateDeliveryCost()` at the same time, a merge conflict is almost certain. Coordinate.
- **Sequence dependent tasks carefully.** If your task relies on a new class a teammate is writing, you'll need their branch merged first. Discuss the order early.
- **Start with shorter tasks** to build familiarity with both the codebase and the GitHub workflow before tackling the larger ones.
- **Use GitHub Issues to track progress.** Create an Issue for each task, assign it to the person taking it on, and close it when the Pull Request merges. That way nobody doubles up.

Marks go to working code. Something that half-works and runs is more valuable than something ambitious that crashes on the first input.

---

## Task list

Tasks are grouped by approximate difficulty, based on patterns from past Paper 1 examinations. Mark totals include screen captures, which typically account for one to two marks each — the remaining marks go to the code itself.

---

### Short tasks — 2 to 4 marks

Focused, self-contained changes. Start here if you're still finding your feet in the codebase.

| Task | Description |
|------|-------------|
| Currency formatting | Display all monetary values as `£X.XX` — pound sign, two decimal places, always. |
| Input validation — blank | Reject empty strings at every point the program accepts user input. |
| Input validation — type | Where a numeric value is required, handle non-numeric input without crashing. |
| Fuel cost floor | Prevent fuel costs from falling below zero. Add a lower bound and clamp to it. |
| Days elapsed display | Show the number of days that have elapsed in the current simulation run. |
| Eat-out probability update | At the end of each day: if a household ate out, re-randomise its probability. If it didn't, increment the probability by 0.1. |

---

### Medium tasks — 6 to 9 marks

These require writing new functions or meaningfully extending existing classes. The bulk of the available marks sits here.

| Task | Description |
|------|-------------|
| `SmallSettlement` class | Create a `SmallSettlement` subclass and add a menu option to initialise one at launch. |
| `RemoveCompany()` | Add a menu option to remove an entire company at once rather than deleting outlets individually. Deduct costs from the company balance on closure. |
| `ExpandOutlet()` edge case | Handle the case where capacity reaches zero after an expansion operation. |
| `AlterCapacity()` fix | Recalculate `DailyCosts` correctly when new capacity is bounded by the maximum permitted value. |
| Duplicate name check | In `AddCompany()`, verify the proposed name doesn't already exist before proceeding. |
| Net gain/loss display | Output each company's net profit or loss for the current simulation run. |
| Weekly average display | Show average daily gain and loss per outlet over the preceding seven days. |
| Reputation modifier | Allow the user to raise or lower a company's reputation score by a specified amount. |
| New restaurant category | Define a new company type with distinct characteristics and include a default instance in the startup scenario. |
| Temporary outlet closure | Allow an outlet to close for a specified number of days and reopen automatically once that period expires. |

---

### Large tasks — 11 to 14 marks

Substantial pieces of work. Each requires careful reading of the existing code before writing anything new. Tackle these once the shorter tasks are covered, or in parallel if your group has the capacity.

| Task | Description |
|------|-------------|
| Close Outlet event | Implement a full outlet closure: remove it from the simulation, log the event, deduct costs from the company balance, and trigger closure automatically after five consecutive loss-making days. |
| Delivery system | Allow households that chose not to eat out to instead order delivery at random. The company incurs fuel costs proportional to the delivery distance. |
| `CalculateDeliveryCost()` optimisation | Rewrite the delivery cost function to find the shortest path through all outlet locations using Dijkstra's algorithm, minimising total delivery expenditure. |
| Automatic outlet expansion | At each day's end, if any company holds a balance above £20,000, open a new outlet at a random grid location and deduct £20,000 from the balance. |
| Company merger | Allow two companies to combine — pooling outlets, balances, and reputations — under a single name. |
| Break-even analysis | Write a subroutine that determines, for each company type, what price per meal would have been required the previous day to break even. |
| Weather system | Introduce random rain events that halve all household eat-out probabilities for that day. Log each occurrence in the events feed. |
| Promotion system | Generate random promotional events for companies or individual outlets. During a promotion, daily costs rise but reputation also increases. |

---

### Stretch tasks — beyond the predicted questions

These extend the simulation in directions not directly predicted from past papers. Attempt them only once the tasks above are complete.

- **`FoodTruck` class** — a subclass of `Outlet` with a `move()` method that relocates the truck to a new grid position each day.
- **Outlet location uniqueness** — prevent two outlets of the same company type from sharing grid coordinates.
- **Budget-constrained households** — assign each household a randomised budget; households only visit outlets whose price falls within it.
- **Fast default loader** — add a menu shortcut that bypasses manual setup and loads the default scenario immediately.
- **Advance N days** — allow the user to skip forward a specified number of days in one operation.

---

## File structure

```
food-magnate/
│
├── food_magnate.py        # Skeleton program — do not rename
├── README.md              # This document
├── requirements.txt       # Third-party dependencies, if any
│
└── tests/
    └── test_examples.py   # Place any test scripts here
```

---

*Talk to each other. The students who coordinate are the ones who score.*
