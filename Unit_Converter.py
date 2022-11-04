# File unit converter
# Made by Hitman-2005
# Such as byte, kb, mb, gb

size_value = float(input('Value: '))

unit1 = 'byte'
unit2 = 'kb'
unit3 = 'mb'
unit4 = 'gb'

print('Units: byte, kb, mb, gb')

current_unit = input('Current Unit: ')

if current_unit == unit1: # Byte
	print('Byte -> kb, mb, gb')
	unit_convert1 = size_value / 1024 # byte -> kb
	unit_convert2 = size_value / 1048576 # byte -> mb
	unit_convert3 = size_value / 1073741824 # byte -> gb
	
	print(unit_convert1,'kb')
	print(unit_convert2,'mb')
	print(unit_convert3,'gb')
elif current_unit == unit2: # KB
	print('KB -> byte, mb, gb')
	unit_convert1 = size_value * 1024 # kb -> byte
	unit_convert2 = size_value / 1024 # kb -> mb
	unit_convert3 = size_value / 1048576 # kb -> gb
	
	print(unit_convert1,'byte')
	print(unit_convert2,'mb')
	print(unit_convert3,'gb')
elif current_unit == unit3: # MB
	print('MB -> byte, kb, gb')
	unit_convert1 = size_value * 1048576 # mb -> byte
	unit_convert2 = size_value * 1024 # mb -> kb
	unit_convert3 = size_value / 1024 # mb -> gb
	
	print(unit_convert1,'byte')
	print(unit_convert2,'kb')
	print(unit_convert3,'gb')
elif current_unit == unit4: # GB
	print('GB -> byte, kb, mb')
	unit_convert1 = size_value * 1073741824 # gb -> byte
	unit_convert2 = size_value * 1048576 # gb -> kb
	unit_convert3 = size_value * 1024 # gb -> mb
		
	print(unit_convert1,'byte')
	print(unit_convert2,'kb')
	print(unit_convert3,'mb')
else:
	print('An error has occured, maybe due to wrong unit input')
		
