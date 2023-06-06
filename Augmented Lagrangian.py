import numpy as np
import scipy.optimize as opt

def objective(x):
    # 目的関数
    return x[0]**2 + x[1]**2 

def constraint(x):
    # 制約条件
    return np.array([x[0]-3*x[1]-6])

rho0 = 1 # ペナルティ係数の初期値
tol = 10e-6 # KKT条件の許容誤差
lambda0 = 0 # ラグランジュ乗数
x_init = np.array([2, 2], dtype=float) # 解の初期値

# STEP 1：初期値の設定
x = x_init
lambd = lambda0
rho = rho0

def func(y):
    return y[0]**2+y[1]**2 + lambd * (y[0]-3*y[1]-6) + 1/2*rho*(y[0]-3*y[1]-6)**2
    # 拡張ラグランジュ関数

while rho*(constraint(x))**2>tol:               
# STEP 2：アルゴリズム終了条件
    x0 =np.array([2,2])                         
    res=opt.minimize(func, x0 , method='BFGS')
    x=res.x                                     
# STEP 3：lambdを固定して、最小化問題を解く
    print(res.x)
    print(rho*(constraint(x))**2)
    lambd=lambd+rho*(constraint(x))
    rho=2*rho                                   
# STEP 4：パラメータの更新
