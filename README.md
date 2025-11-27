# Checkers — Minimax Algorithm with Alpha-Beta Pruning

This repository contains an implementation of the classic board game **Checkers** enhanced with an **AI opponent** based on the **Minimax algorithm** optimized using **Alpha–Beta pruning**.  
The project includes a playable game, board visualization, AI logic, and a performance comparison between standard Minimax and optimized Alpha-Beta Minimax.

The full project description and analysis (algorithm explanation, illustrations, results) are documented in the accompanying report.

---

## Overview

Checkers is a two-player logical board game played on an 8×8 board with 12 pieces per player.  
This project implements:

- A complete rules-accurate Checkers game  
- A human-vs-AI mode  
- Minimax search for optimal decision-making  
- Alpha-Beta pruning optimization  
- Performance evaluation across different depths  
- Visualization of moves, including showing all valid moves for a selected piece  

Figures on pages **3–4** of the report show the game board visualization and the highlighting of legal moves for each piece (blue dots).

---

## Project Goal

The main objective is to:

**Build an intelligent Checkers AI** that selects optimal actions using game-tree search, and then  
**Compare Minimax vs. Alpha-Beta pruning performance** in terms of:

- number of explored nodes  
- decision-making time  
- computational efficiency  

Diagrams on pages **6 and 9** illustrate the Minimax and Alpha-Beta search trees used in the project.

---

## Algorithms Used

### **1. Minimax Algorithm**

A classical adversarial search algorithm assuming:

- AI = maximizing player  
- Human = minimizing player  

The evaluation function used in this project:

score = (#black_pieces - #white_pieces) + 0.5 * (#black_kings - #white_kings)

This scoring approach is justified on page **7** of the report. Kings receive a weight of **0.5**, representing higher mobility but avoiding over-prioritization.

---

### **2. Alpha-Beta Pruning**

An optimization of Minimax that prunes branches that cannot influence the final decision.

Key rules (page 8–9):  
- Maintain `alpha` = best option for maximizer  
- Maintain `beta` = best option for minimizer  
- Prune when `alpha >= beta`  
- Maximizer updates alpha only; minimizer updates beta only  

The Alpha-Beta tree diagram (page 9) shows all prune points visually.

---

## Performance Comparison

Full tables and charts on pages **10–17** provide empirical results.

### **Average Time Gain (Alpha-Beta vs. Minimax)**

| Depth | Faster by |
|-------|-----------|
| 3 | **2.2×** |
| 4 | **6.0×** |
| 5 | **10.3×** |
| 6 | **33×** |

(From the time comparison graph on page 15.)

### **Average Reduction in Nodes Explored**

| Depth | Nodes Reduced By |
|--------|------------------|
| 3 | 2.6× fewer |
| 4 | 6.3× fewer |
| 5 | 10.2× fewer |
| 6 | 56.3× fewer |

(From the node comparison graph on page 16.)

### Conclusion  
Alpha-Beta pruning drastically reduces the computational cost and allows deeper searches within feasible time, which is a key requirement for real-time Checkers AI. (Conclusion section, page 17.)
