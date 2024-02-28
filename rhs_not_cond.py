from analysis import Analysis

#Arrays, for each alpha, with the values of the relation between the norm of the previous iteration and the norm of the current iteration

#xdiv = 5
#alpha = 0.1
norms_rhs1 = [0.15231, 0.0221501, 0.00518877, 0.00137366, 0.00037565, 0.000103679, 2.86916e-05, 7.946e-06, 2.20109e-06, 6.09756e-07, 1.6892e-07, 
              4.6796e-08, 1.2964e-08, 3.59142e-09, 9.94935e-10, 2.75628e-10, 7.63576e-11]
r_norms_rhs1 = [6.87626, 4.26886, 3.77733, 3.65676, 3.62319, 3.61358, 3.61082, 3.61002, 3.60979, 3.60973, 3.60971, 3.6097, 3.6097, 3.6097, 
                3.6097, 3.6097]

#alpha = 0.1e-1
norms_rhs2 = [0.0172662, 0.000356789, 1.18287e-05, 4.27272e-07, 1.56965e-08, 5.787e-10, 2.1352e-11, 7.87945e-13]
r_norms_rhs2 = [48.3933, 30.1629, 27.6843, 27.2209, 27.1237, 27.1028, 27.0984]

#alpha = 0.1e-2
norms_rhs3 = [0.001753, 3.78256e-06, 1.30535e-08, 4.88698e-11, 1.85805e-13]
r_norms_rhs3 = [463.443, 289.772, 267.108, 263.017]

#alpha = 0.1e-3
norms_rhs4 = [0.000175572, 3.80524e-08, 1.31854e-11, 4.99062e-15]
r_norms_rhs4 = [4613.96, 2885.94, 2642.04]
#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#xdiv = 6
#alpha = 0.1
norms_rhs5 = [0.190554, 0.0377731, 0.0124113, 0.00468992, 0.00185431, 0.000745016, 0.000301055, 0.000121905, 4.93983e-05, 2.00224e-05, 
              8.11639e-06, 3.29021e-06, 1.33379e-06, 5.407e-07, 2.19192e-07, 8.88572e-08, 3.60214e-08, 1.46026e-08, 5.91967e-09, 2.39975e-09, 
              9.72824e-10, 3.94369e-10, 1.59871e-10, 6.48096e-11]
r_norms_rhs5 = [5.0447, 3.04344, 2.64638, 2.52921, 2.48895, 2.47468, 2.4696, 2.46779, 2.46714, 2.46691, 2.46683, 2.4668, 2.46679, 2.46679, 
                2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679, 2.46679]

#alpha = 0.1e-1
norms_rhs6 = [0.0228905, 0.00078727, 4.48466e-05, 2.79249e-06, 1.77217e-07, 1.12958e-08, 7.20727e-10, 4.5997e-11, 2.93569e-12]
r_norms_rhs6 = [29.0759, 17.5547, 16.0597, 15.7575, 15.6888, 15.6728, 15.669, 15.6682]

#alpha = 0.1e-2
norms_rhs7 = [0.00234696, 8.71713e-06, 5.32667e-08, 3.53226e-10, 2.38103e-12, 1.61229e-14]
r_norms_rhs7 = [269.236, 163.651, 150.801, 148.35, 147.68]
 
#alpha = 0.1e-3
norms_rhs8 = [0.000235308, 8.81009e-08, 5.42247e-11, 3.61979e-14]
r_norms_rhs8 = [2670.9, 1624.74, 1498.01]
#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#xdiv = 7
#alpha = 0.1
norms_rhs9 = [0.225676, 0.0547547, 0.0222719, 0.0105478, 0.00529196, 0.00272169, 0.00141505, 0.000739194, 0.000386934, 0.000202722, 0.000106251, 
              5.56973e-05, 2.9199e-05, 1.53079e-05, 8.0254e-06, 4.20748e-06, 2.20586e-06, 1.15647e-06, 6.06304e-07, 3.17868e-07, 1.66649e-07, 
              8.73697e-08, 4.58055e-08, 2.40145e-08, 1.25902e-08, 6.60066e-09, 3.46054e-09, 1.81427e-09, 9.5117e-10, 4.98672e-10, 2.6144e-10, 
              1.37066e-10, 7.18596e-11, ]
r_norms_rhs9 = [4.12158, 2.45846, 2.11152, 1.99317, 1.94437, 1.92339, 1.91431, 1.91039, 1.90869, 1.90796, 1.90765, 1.90751, 1.90745, 1.90743, 
                1.90741, 1.90741, 1.90741, 1.90741, 1.90741, 1.90741, 1.90741, 1.90741, 1.90741, 1.90741, 1.90741, 1.90741, 1.90741, 1.90741, 
                1.90741, 1.90741, 1.90741, 1.90741, ]

#alpha = 0.1e-1
norms_rhs10 = [0.0287698, 0.00149304, 0.000131206, 1.26586e-05, 1.24772e-06, 1.23635e-07, 1.22672e-08, 1.21756e-09, 1.20858e-10, 1.19968e-11, 
               1.19086e-12, ]
r_norms_rhs10 = [19.2693, 11.3793, 10.365, 10.1454, 10.0919, 10.0786, 10.0752, 10.0744, 10.0741, 10.0741, ]

#alpha = 0.1e-2
norms_rhs11 = [0.00298799, 1.75267e-05, 1.72114e-07, 1.83511e-09, 1.99041e-11, 2.16719e-13, ]
r_norms_rhs11 = [170.482, 101.832, 93.7894, 92.1976, 91.8428, ]

#alpha = 0.1e-3
norms_rhs12 = [0.000300011, 1.78289e-07, 1.77127e-10, 1.90845e-13, 2.34823e-13, ]
r_norms_rhs12 = [1682.73, 1006.56, 928.12, 0.81272, ]