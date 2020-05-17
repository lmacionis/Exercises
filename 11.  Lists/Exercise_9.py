"""
Describe the relationship between " ".join(song.split()) and song in the fragment of code below.
Are they the same for all strings assigned to song? When would they be different?

song = "The rain in Spain..."
"""
"""
# I dont know.
If both are the same, this is because of the difference between the identity operator is and the equality operator ==.

In short, is yields True when objects are identical. Because a new string is created in your example, it produces False.

If you'd use == a deep comparison of the strings' characters would take place and True would be returned.

If the compared strings are not the same, neither == or is should produce True.
"""

song = "The rain in Spain..."

if song == " ".join(song.split()):
    print("Yay")


if song is " ".join(song.split()):
    print("Yay")

print(song)