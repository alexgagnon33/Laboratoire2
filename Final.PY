import statistics
import math

# Step 1: read the data from the files and store them in a dictionary
data = {}
files = ['data1.txt', 'data2.txt', 'data3.txt']
for file in files:
    with open(file, 'r') as f:
        lines = f.readlines()
        team = lines[0].strip()
        times = [float(line.strip()) for line in lines[1:]]
        data[team] = times

# Step 2: display the menu and handle the user input
while True:
    print('Menu:')
    print('1. Afficher les statistiques')
    print('2. Afficher l\'équipe la plus homogène')
    print('3. Ajouter une faute à une équipe')
    print('4. Sauvegarder les statistiques')
    print('5. Sortir')
    choice = int(input('Choix: '))
    
    if choice == 1:
        # Step 3: display the statistics
        fastest_team = ''
        fastest_time = float('inf')
        for team, times in data.items():
            mean = statistics.mean(times)
            if mean < fastest_time:
                fastest_team = team
                fastest_time = mean
        print(f'Coureur gagnant: {fastest_team} ({fastest_time:.2f} secondes)')
        print('Équipe en ordre croissant de moyenne:')
        for team, times in sorted(data.items(), key=lambda x: statistics.mean(x[1])):
            mean = statistics.mean(times)
            print(f'{team} - Moyenne: {mean:.2f}s')
        
    elif choice == 2:
        # Step 4: display the team with the smallest standard deviation
        best_team = ''
        smallest_stddev = float('inf')
        for team, times in data.items():
            stddev = math.sqrt(sum((x - statistics.mean(times))**2 for x in times) / (len(times) - 1))
            if stddev < smallest_stddev:
                best_team = team
                smallest_stddev = stddev
        print(f'Équipe la plus homogène: {best_team} ({smallest_stddev:.2f})')
        
    elif choice == 3:
        # Step 5: add a penalty to a team
        team = input('Équipe: ')
        player = input('Numéro de joueur: ')
        infraction = input('Infraction: ')
        with open(f'fautes_{team}.txt', 'a') as f:
            f.write(f'{player} - {infraction}\n')
        
    elif choice == 4:
        # Step 6: save the statistics to a file
        with open('stats.txt', 'w') as f:
            f.write(f'Coureur gagnant: {fastest_team} ({fastest_time:})')