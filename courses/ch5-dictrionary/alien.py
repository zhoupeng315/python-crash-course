alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


#delete record
del alien_0['points']
print(alien_0)


# use get() default a value
point_value = alien_0.get('points', 'No Point value assigned')
print(point_value)