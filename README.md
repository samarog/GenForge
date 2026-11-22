# GenForge — RPG Battle Simulator with Evolutionary Optimization

Academic project for **Advanced Programming in Python**.

> **Status:** planning stage. This README describes the initial proposal; no features have been implemented or experimental results obtained yet.

## 1. Overview

**GenForge** is a small, turn-based RPG battle simulator. The setting is intentionally simple: Warrior characters fight opponents with different characteristics.

The primary goal is **not to build a complete video game**, but to investigate whether a **simple evolutionary algorithm**, based on selection and mutation, can discover attribute distributions that improve a character's combat performance.

The project will be developed in Python, initially as a console application, without requiring a graphical interface, database, or external services.

## 2. Problem and Objective

Each Warrior has a limited pool of points to distribute among attributes such as **health, attack, and defense**. The distribution influences battle outcomes: investing more points in one attribute means investing fewer points in another.

**Main objective:** implement and analyze a character evolution process that seeks to improve combat performance **while keeping the total attribute-point budget constant**.

Evolution must be observable and measurable, rather than merely represented by visual improvements or arbitrary level increases.

## 3. Main Research Question

**Can an RPG character's combat performance be improved automatically through selection and mutation without increasing the total number of attribute points available?**

### Supporting Research Questions

1. Which distributions of health, attack, and defense perform best under the defined combat rules?
2. Does performance improve consistently across generations, or does it tend to plateau?
3. How do results change when the mutation probability is adjusted?
4. Does a character configuration that performs well against one opponent also perform well against other types of opponents?
5. Do different runs of the same algorithm produce similar solutions?
6. Does an evolved population outperform a simple baseline, such as randomly generated characters with the same point budget?

These are **questions to investigate**, not conclusions assumed in advance.

## 4. Initial Scope

### Included in the First Version

- **One evolvable character type:** Warrior.
- **Three main attributes:** health, attack, and defense.
- **A fixed attribute-point budget** for each Warrior.
- **Automatic turn-based battles** with simple, explicit rules.
- **Up to three opponent types**, each with a distinct profile.
- **A population of Warriors** with different attribute distributions.
- **Selection of stronger candidates and mutation** to produce new generations.
- **Result tracking** to compare generations and configurations.

### Outside the Initial Scope

- Maps, exploration, quests, levels, and inventory.
- Elaborate graphical interfaces or real-time gameplay.
- Multiple playable character classes (Mage, Archer, etc.).
- Databases or integration with online services.
- Genetic crossover between two parents: **a possible extension**, not a first-version requirement.
- Genetic programming based on evolving program trees: **not part of the initial proposal**.

## 5. Intended Workflow

1. Define the combat rules and create a character with specified attributes.
2. Simulate a complete battle and determine its winner.
3. Generate a group of Warriors with the same total attribute-point budget.
4. Have each Warrior face a comparable set of opponents.
5. Calculate a **fitness score** from the battle results.
6. Select better-performing candidates and create mutated variants.
7. Repeat across multiple generations and record the results.
8. Compare the initial population with later generations and a random baseline.

**Note:** character progression (gaining points after battle) is different from evolution through selection and mutation (searching for better distributions with constant resources). This project uses the latter approach.

## 6. Python Concepts to Explore

- Object-oriented programming: classes, objects, constructors, attributes, and methods.
- Composition and separation of responsibilities among characters, battles, and evolution.
- Data structures: lists and dictionaries.
- Loops, conditionals, functions, and parameter validation.
- Pseudorandom numbers and random **seeds** for reproducibility.
- Evaluation (**fitness**), selection, and mutation.
- Basic statistics for interpreting results (for example, win rates and averages).
- Reading and writing JSON, **if needed** to save experiments.

Inheritance and polymorphism may be introduced only when they serve a genuine need in the character design. They are not artificial requirements.

## 7. Planned Experiments and Metrics

To evaluate the algorithm, we may collect:

| Metric | What It Helps Us Understand |
| --- | --- |
| Win rate | Character effectiveness against the defined opponents |
| Best fitness per generation | Evolution of the strongest candidate |
| Average fitness per generation | Evolution of overall population performance |
| Attribute distribution | Which characteristics are favored |
| Generations without improvement | Possible stagnation of the process |
| Results across multiple random seeds | Sensitivity to randomness |

**Experimental control:** comparisons should use the same attribute budget and equivalent battle conditions. If battles include random events, simulations must be controlled or repeated to avoid misleading conclusions.

## 8. Decisions Still to Be Made

These choices will be made and justified during implementation rather than fixed prematurely:

- Total attribute-point budget and minimum/maximum values for each attribute.
- Damage formula, turn order, and victory conditions.
- Characteristics of the different opponents.
- Exact fitness formula and how defeats are penalized.
- Population size, number of generations, and mutation probability.
- Selection strategy and possible preservation of the best candidates (**elitism**).
- How results will be displayed and saved.

## 9. Development Plan — Micro-Steps

- [ ] **Step 1:** define the three attributes and the point budget.
- [ ] **Step 2:** create the `Character`/`Warrior` class and test object creation.
- [ ] **Step 3:** define an opponent and implement damage calculation.
- [ ] **Step 4:** implement a complete automatic battle.
- [ ] **Step 5:** generate several random Warriors, all with the same point budget.
- [ ] **Step 6:** define fitness and evaluate each Warrior.
- [ ] **Step 7:** implement candidate selection.
- [ ] **Step 8:** implement mutations that preserve the point budget.
- [ ] **Step 9:** run evolution across multiple generations.
- [ ] **Step 10:** record, compare, and interpret the results.
- [ ] **Step 11:** test edge cases, review the code, and prepare the presentation.

Each step should produce something small, executable, and understandable before moving to the next.

## 10. Success Criteria

The project will be considered complete when it is possible to:

1. Run automatic battles with clearly defined rules.
2. Create and evolve a population without violating attribute constraints.
3. Observe and save metrics that support comparisons across generations.
4. Reproduce an experiment using parameters and a random seed.
5. Explain **why** the algorithm selected certain characters and what limitations apply to the results.

**Important:** evolutionary improvement is not guaranteed in every run. If tests show stagnation or inconsistent results, those are also valid findings to analyze.

---
