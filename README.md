# 🎰 Multiplayer Marble Betting Game Simulation (OOP)

This project is a powerful console simulation of a marble betting game designed to run concurrent rounds for multiple players. It is built using **Object-Oriented Programming (OOP)**, clearly separating player data from game mechanics for scalability and maintainability.

The simulation automatically runs for a fixed number of rounds, with players being eliminated when they lose half of their starting capital.

---

## ⚙️ Project Structure and OOP Design

The core logic is structured into two main classes, enforcing a clean **separation of concerns**:

### 1. `Player` Class
* **Role:** Encapsulates the state of a single gambler.
* **Key Attributes:** `gold`, `original_gold_balance`, `games_played`, `games_won`, and an `is_active` flag.
* **Functionality:** Handles self-validation checks (e.g., `can_bet`).

### 2. `MarbleGameManager` Class
* **Role:** Acts as the central game engine and casino manager.
* **Functionality:** Holds the `marble_bag` and executes the core logic for **one draw** via the `run_round()` method, updating the individual player's state.

---

## 🎲 Game Rules and Mechanics

### Simulation Parameters
* **Starting Gold:** Each player begins with **1,000 Gold Pieces**.
* **Elimination (Game Over):** A player is immediately marked **OUT** and removed from future rounds if their gold drops to **500 or less** (losing half their starting stake).
* **Betting:** Bets are automatically generated between 1 and 100 Gold (or the player's remaining gold, whichever is lower) to facilitate the simulation.

### Marble Bag Composition (Total 10 Marbles)
The bag follows a high-stakes composition with replacement after every draw:

| Marble Color | Count | Odds | Payout/Loss | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Green** | 5 | 50% | **+1x** Bet | Standard Win |
| **Red** | 3 | 30% | **-1x** Bet | Standard Loss |
| **Black (10X)** | 1 | 10% | **+10x** Bet | **Jackpot** Win |
| **White (5X)** | 1 | 10% | **-5x** Bet | High-Risk Loss |

---

## 🚀 How to Run the Simulation

### Prerequisites
You need **Python 3** installed on your system.

### Running the Script
1.  **Clone the Repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    ```
2.  **Navigate to the Directory:**
    ```bash
    cd [your-repo-name]
    ```
3.  **Run the Script:**
    ```bash
    python your_script_name.py
    ```
    *Note: If you encounter a `UnicodeEncodeError` due to console printing, ensure your console environment (like Command Prompt) is set to UTF-8 using `chcp 65001` before running.*
