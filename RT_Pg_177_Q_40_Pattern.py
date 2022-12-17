for i in range(0, 5):
    if i == 0 or i == 4:
        print("* " * 5)
    else:
        x = "*\t*"
        print(x.expandtabs(8))

# Answer
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
