alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
plain_text = 'Pz-/aI/J`EvfthGH'
rotation = 66
cipher = ''
print rotation
for character in plain_text:
	if (ord(character) >= 97 and ord(character) <= 122) or (ord(character) >= 65 and ord(character) <= 90):
		if (ord(character) - rotation) >= 0:
			cipher += chr(ord(character) - rotation)
		else:
			cipher += chr(ord(character) - rotation + 26)
print cipher,