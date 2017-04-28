alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
plain_text = 'Pz-/aI/J`EvfthGH'
rotation = 66
cipher = ''
for character in plain_text:
	if (ord(character) >= 97 and ord(character) <= 122):
		old_pos = ord(character)
		if (old_pos + rotation) <= 122:
			new_pos = old_pos + rotation
		else:
			new_pos = ((old_pos + rotation - 1) % 122) + 97
		cipher += chr(new_pos)
	elif (ord(character) >= 65 and ord(character) <= 90):
		old_pos = ord(character)
		if (old_pos + rotation) <= 90:
			new_pos = old_pos + rotation
		else:
			new_pos = ((old_pos + rotation - 1) % 90) + 65
		cipher += chr(new_pos)
		print character, old_pos, new_pos, chr(new_pos)
	else:
		cipher += character
print cipher
