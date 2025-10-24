# 1. Write a program to print twinkle twinkle little star poem in python.

print("""Twinkle, Twinkle, Little Star

Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Twinkle, twinkle, little star,
How I wonder what you are!

Then the traveler in the dark
Thanks you for your tiny spark;
He could not see which way to go,
If you did not twinkle so.

Twinkle, twinkle, little star,
How I wonder what you are!

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye
Till the sun is in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!
      """)



# 2. Install an external module and use it to perform an operation of your interest.
import pyttsx3
# Initialize the TTS engine
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# 3. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
import os

# Specify the directory path
# Use '.' for current directory or provide a full path
directory_path = '.'

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:", directory_path)
for item in contents:
    print(item)
