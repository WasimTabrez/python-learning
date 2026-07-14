# Demonstrate set methods

colors = {"Red", "Green"}

print("Original:", colors)

colors.add("Blue")
print("add(\"Blue\"):", colors)

colors.add("Blue")
print("add(\"Blue\"):", colors)

colors.update(["Yellow", "Black"])
print("update():", colors)

copy_colors = colors.copy()
print("copy():", copy_colors)

colors.discard("Green")
print("discard():", colors)

print("Length:", len(colors))

colors.clear()
print("clear():", colors)

# copy_colors.remove("Wasim") # KeyError: 'Wasim'