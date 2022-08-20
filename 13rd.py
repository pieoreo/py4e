counts = dict()
names = ['csev', 'cewn', 'csev', 'zqian', 'cwen']
for name in names:
    if name in counts:
        x = counts[name]
    else:
        x = 0

    x = counts.get(name, 0)      

