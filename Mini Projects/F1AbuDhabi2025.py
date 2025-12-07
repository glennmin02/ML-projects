import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Historical race data (simplified)
np.random.seed(42)
data = {
    'driver': ['VER']*50 + ['NOR']*50 + ['PIA']*50,
    'grid_position': np.random.randint(1, 10, 150),
    'won': [1]*20 + [0]*30 + [1]*10 + [0]*40 + [1]*5 + [0]*45  # Win rates
}
df = pd.DataFrame(data)

# Features and target
X = df[['grid_position']]
y = df['won']

# Scale and train
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression()
model.fit(X_scaled, y)

# Yesterday's qualifying results
tonight = pd.DataFrame({
    'driver': ['VER', 'NOR', 'PIA'],
    'grid_position': [1, 2, 3]
})

# Predict win probability
tonight_scaled = scaler.transform(tonight[['grid_position']])
win_probs = model.predict_proba(tonight_scaled)[:, 1]

# Results
print("2025 Abu Dhabi GP Race Winner Probabilities")
for i, row in tonight.iterrows():
    print(f"{row['driver']}: {win_probs[i]*100:.1f}%")

np.random.seed(42)

# Current Standings
standings = {'NOR': 408, 'VER': 396, 'PIA': 392}

# Points system
points = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
for i in range(11, 21):
    points[i] = 0

# Tonight's Grid
grid = {'VER': 1, 'NOR': 2, 'PIA': 3}

# Historical data patterns (simplified from real F1 stats)
# Probability of finishing position based on starting position
# Format: start_pos -> [P1%, P2%, P3%, P4%, P5-10%, DNF%]

historical_patterns = {
    1: [0.45, 0.25, 0.12, 0.08, 0.07, 0.03],  # Pole has 45% win rate
    2: [0.22, 0.30, 0.20, 0.12, 0.12, 0.04],  # P2 start
    3: [0.12, 0.18, 0.25, 0.18, 0.22, 0.05],  # P3 start
}


def simulate_race():
    """Simulate one race based on historical patterns"""
    results = {}

    for driver, start_pos in grid.items():
        probs = historical_patterns[start_pos]

        # Random outcome based on probabilities
        rand = np.random.random()

        if rand < probs[0]:
            finish = 1
        elif rand < probs[0] + probs[1]:
            finish = 2
        elif rand < probs[0] + probs[1] + probs[2]:
            finish = 3
        elif rand < probs[0] + probs[1] + probs[2] + probs[3]:
            finish = 4
        elif rand < probs[0] + probs[1] + probs[2] + probs[3] + probs[4]:
            finish = np.random.randint(5, 11)
        else:
            finish = 20  # DNF

        results[driver] = finish

    # Handle position conflicts (no two drivers same position)
    positions = list(results.values())
    while len(positions) != len(set(positions)):
        for driver in results:
            for other in results:
                if driver != other and results[driver] == results[other]:
                    results[other] = min(results[other] + 1, 20)
        positions = list(results.values())

    return results


def calculate_champion(race_results):
    """Determine champion based on race results"""
    final_points = {}
    for driver in standings:
        final_points[driver] = standings[driver] + points.get(race_results[driver], 0)

    # Find champion (highest points)
    champion = max(final_points, key=final_points.get)
    return champion, final_points


# Run simulation
n_simulations = 10
champions = {'NOR': 0, 'VER': 0, 'PIA': 0}
race_results_log = []

print()
print("2025 Formula 1 World Championship Probabilities")

for i in range(n_simulations):
    race = simulate_race()
    champion, final_pts = calculate_champion(race)
    champions[champion] += 1

    if i < 5:  # Log first 5 simulations
        race_results_log.append({
            'sim': i + 1,
            'VER_pos': race['VER'],
            'NOR_pos': race['NOR'],
            'PIA_pos': race['PIA'],
            'champion': champion
        })

for driver in ['NOR', 'VER', 'PIA']:
    prob = champions[driver] / n_simulations * 100
    print(f"{driver}: {prob:.1f}%")

winner = max(champions, key=champions.get)
names = {'NOR': 'Lando Norris', 'VER': 'Max Verstappen', 'PIA': 'Oscar Piastri'}

print(f"\n{names[winner]} will be 2025 World Champion")
"""
Memo:
- 2025 Formula 1 Abu Dhabi Grand Prix is set to take for one last time, with Max Verstappen on pole at yesterday's qualifying session, followed by Lando Norris in 2nd and Oscar Piastri in 3rd.
- The race is expected to be thrilling with championship implications across three contenders.
- Who will win the race? And who will be come the next World Champion?
"""
