import sys

# print(sys.argv)

# map names to characters
emojis = {
    'snowman' : '\N{SNOWMAN WITHOUT SNOW}',
    'smiley' : '\U0001F603',
    'santa' : '\U0001F385',
    'alien' : '\U0001F47E',
    'chocolate' : '\U0001F4A9'
}

# was the script given any parameters
if len(sys.argv) == 1:
    print("format: python .\\emojis.py <name>")
    sys.exit()

name = sys.argv[1]
count = int(sys.argv[2])

print(f"{emojis[name] * count}")