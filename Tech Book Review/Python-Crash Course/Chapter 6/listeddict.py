aliens = []
for alien in range(0,30):
    new_alien = {'color': 'green', 'points' : 50, 'speed' : 'slow' }
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[0:10]:
    print(alien)
print("...")