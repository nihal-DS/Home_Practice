#  Find the index values of all the "sui" in x
x = "sui is the great player, but is sui as good as I think, sui could be the second best player,all I know is he can sui"
idx = 0
st = 0
for i in range(x.count("sui")):
    idx = x.find("sui", st)
    st = idx+3
    print(idx)
