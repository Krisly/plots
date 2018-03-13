from nodepy import *
from nodepy import rk
from nodepy.rooted_trees import *
import matplotlib.pyplot as plt

i=0
for p in range(6):
	trees = rt.list_trees(p)
	for i in range(0,len(trees)):
		tree = rt.RootedTree(trees[i])
		print("{:<8} {:<8} {:<8} \n {:>12} {:>6} {:>11}".format('Tree Structure:',
            																  'Order:',
            																  'Density:',
            																  trees[i],
            															      tree.order(),
              																  tree.density()))

des_tree = rt.list_trees(5)

fig,ax = plt.subplots(1, 9, figsize=(15,10), sharex=False)
for i in range(len(des_tree)):
	ax[i] = des_tree[i].plot()
plt.show()
print(ax[0])
'''
plot_all_trees(5,title='')
plt.savefig('./figs/rooted_trees.pdf')
plt.show()


rk4 = rk.loadRKM('DP5')
rk4.plot_stability_region(N=200,bounds=[-5,5,-5,5])
plt.savefig('./figs/abs_stab_DP54.pdf')
plt.show()


rk4 = rk.loadRKM('RK44')
rk4.plot_stability_region(N=200,bounds=[-5,5,-5,5])
plt.savefig('./figs/abs_stab_rk44.pdf')
plt.show()
'''