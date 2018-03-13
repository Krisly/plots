from nodepy import *
from nodepy import rk
from nodepy.rooted_trees import *
import matplotlib.pyplot as plt
from matplotlib import cm

i=0
for p in range(6):
	trees = rt.list_trees(p)
	for i in range(1,len(trees)):
		tree = rt.RootedTree(trees[i])
		idx = int(tree.symmetry())

		print("{:<8} {:<8} {:<8} {:<8} \n {:>12} {:>6} {:>11} {:>8}".format('Tree Structure:',
            												  'Order:',
            												  'Density:',
            												  'Symmetry',
            											  	  trees[i],
            												  tree.order(),
              											      tree.density(),idx))



A=np.array([[(88-7*np.sqrt(6))/(360),(296-169*np.sqrt(6))/(1800),(-2+3*np.sqrt(6))/(225)],
	        [(296+169*np.sqrt(6))/(1800),(88+196*np.sqrt(6))/(360),(-2-3*np.sqrt(6))/(225)],
	        [(16-np.sqrt(6))/36,(16+np.sqrt(6))/(36),1/9]])
b=np.array([(16-np.sqrt(6))/36,(16+np.sqrt(6))/(36),1/9])

Radau5 = rk.RungeKuttaMethod(A,b)
Radau5.plot_stability_region(N=200,bounds=[-20,30,-20,20],longtitle=False)
plt.savefig('./abs_stab_reg_Radau5.pdf')
plt.show()


'''
des_tree = rt.list_trees(5)

j = 1
for i in range(0,9):
	des_tree[i].plot()
	if des_tree[i].density() == 20:
			plt.savefig('./tree_order_5_density_{}_{}.pdf'.format(j,des_tree[i].density()))
			j += 1
	else:
			plt.savefig('./tree_order_5_density_{}.pdf'.format(des_tree[i].density()))
	plt.close()

plot_all_trees(5)
plt.savefig('./all.pdf')

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
