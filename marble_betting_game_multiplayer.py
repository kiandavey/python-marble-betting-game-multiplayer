import random 

class Player:
    def __init__(self, name, gold=1000, games_played=0, games_won=0):
        self.name = name
        self.gold = gold 
        self.original_gold_balance = gold
        self.games_played = games_played
        self.games_won = games_won
        self.is_active = True

    def can_bet(self, amount):
        return amount >= 1 and amount <= self.gold
      
class MarbleGameManager:
    def __init__(self):
        self.marble_bag = ["green", "green", "green", "green", "green", 
                           "black", "white", "red", "red", "red"]

    def run_round(self, player, bet_amount):

        if not player.can_bet(bet_amount):
            return f"tried to bet {bet_amount}, but it was invalid."
        
        chosen_marble = random.choice(self.marble_bag)
        payout = 0
        
        player.games_played += 1
        
        if chosen_marble == 'green':
            payout = bet_amount
            player.games_won += 1
            result_message = f"drew {chosen_marble.title()}: Won (+{bet_amount} Gold)"
        elif chosen_marble == 'black':
            payout = bet_amount * 10
            player.games_won += 1
            result_message = f"drew BLACK: JACKPOT! Won (+{payout} Gold)"
        elif chosen_marble == 'white':
            payout = -(bet_amount * 5)
            loss_amount = bet_amount * 5 
            result_message = f"drew WHITE: 5X LOSS (-{loss_amount} Gold)"
        elif chosen_marble == 'red':
            payout = -bet_amount
            result_message = f"drew RED: Loss (-{bet_amount} Gold)"

        player.gold += payout

        if player.gold <= player.original_gold_balance / 2:
            player.is_active = False
            return f"❌ drew {chosen_marble.title()}: **ELIMINATED!** Final Gold: {player.gold}"

        return f"✅ {result_message} | Current Gold: {player.gold}"

def run_simulation(total_rounds, player_names): 
    print("+-------------- MARBLE BETTING GAME MULTIPLAYER SIMULATION --------------+") 
    
    manager = MarbleGameManager()
    players = [Player(name) for name in player_names]
    active_players = players.copy()

    for round_num in range(1, total_rounds + 1):
        if not active_players:
            print(f"\nSimulation ended early at Round {round_num-1}: No active players left.")
            break

        print(f"\n### Round {round_num} of {total_rounds} ###")

        for player in list(active_players):
            if not player.is_active:
                active_players.remove(player) 
                continue
            
            max_bet = min(player.gold, 100)
            if max_bet < 1: 
                player.is_active = False
                continue
            bet_amount = random.randint(1, max_bet)

            outcome = manager.run_round(player, bet_amount)
            print(f"[{player.name}, Bet: {bet_amount}]: {outcome}")
            
            if not player.is_active:
                active_players.remove(player)
    
    print("\n+---------------------- 📈 FINAL SIMULATION REPORT ----------------------+")

    players.sort(key=lambda p: p.gold, reverse=True)

    winner = players[0]

    for player in players:
        status = "Active" if player.is_active else "OUT (Lost Half)"
        profit = player.gold - player.original_gold_balance
        
        print(f"[{player.name}]: Gold: {player.gold} (Profit: {profit:+} Gold) | Rounds: {player.games_played} | Wins: {player.games_won} | Status: {status}")

    print(f"\n🏆 The overall winner of the simulation is {winner.name} with {winner.gold} gold!")


if __name__ == "__main__":
    player_list = ["KDA", "LM", "MDC", "JDC"]
    SIMULATION_ROUNDS = 10
    players_for_simulation = [Player(name) for name in player_list] 
    
    run_simulation(SIMULATION_ROUNDS, player_list)