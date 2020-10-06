# chorus
# INFO:__main__:{'loss': 0.038295578211545944,
#                'mae': 0.14439217746257782}
# INFO:__main__:y_cont granular MAE = [0.1099736  0.23523717 0.2215074  0.14365272 0.12369812 0.03228392]
# INFO:__main__:mean mse = 0.0082
# INFO:__main__:std mse = 0.0082
# INFO:__main__:mean mae = 0.0508
# INFO:__main__:std mae = 0.0318

# compressor
# INFO:__main__:{'loss': 0.0009621087228879333,
#                'mae': 0.020053954795002937}
# INFO:__main__:y_cont granular MAE = [0.0174068  0.02829562 0.01445946]
# INFO:__main__:mean mse = 0.0023
# INFO:__main__:std mse = 0.0021
# INFO:__main__:mean mae = 0.0239
# INFO:__main__:std mae = 0.0153

# distortion
# INFO: __main__:{'loss': 0.3983064591884613,
#                 'dist_mode_loss': 0.36372750997543335,
#                 'cont_output_loss': 0.03457893803715706,
#                 'dist_mode_acc': 0.8669999837875366,
#                 'cont_output_mae': 0.13383513689041138}
# INFO:__main__:n_perfect_pred = 2
# INFO:__main__:perfect pred = 0.20%
# INFO:__main__:mean mse = 0.0185
# INFO:__main__:std mse = 0.0339
# INFO:__main__:mean mae = 0.0728
# INFO:__main__:std mae = 0.0787

# eq
# INFO:__main__:{'loss': 0.883407473564148,
#                'eq_typl_loss': 0.5597400069236755,
#                'eq_typh_loss': 0.2613202631473541,
#                'cont_output_loss': 0.0623471662402153,
#                'eq_typl_acc': 0.7680000066757202,
#                'eq_typh_acc': 0.890999972820282,
#                'cont_output_mae': 0.20215460658073425}
# INFO:__main__:y_cont granular MAE = [0.1690348  0.1691671  0.23900047 0.23175344 0.2012385  0.20273289]
# INFO:__main__:mean mse = 0.0352
# INFO:__main__:std mse = 0.0492
# INFO:__main__:mean mae = 0.1248
# INFO:__main__:std mae = 0.0893

# filter
# INFO:__main__:{'loss': 2.0681264400482178,
#                'fx_fil_type_loss': 1.997994065284729,
#                'cont_output_loss': 0.0701325386762619,
#                'fx_fil_type_acc': 0.3919999897480011,
#                'cont_output_mae': 0.22187009453773499}
# INFO:__main__:y_cont granular MAE = [0.17660359 0.23106153 0.18933657 0.2514241  0.2609247 ]
# INFO:__main__:mean mse = 0.0592
# INFO:__main__:std mse = 0.0664
# INFO:__main__:mean mae = 0.1671
# INFO:__main__:std mae = 0.0955

# flanger
# INFO:__main__:{'loss': 0.022245261818170547,
#                'mae': 0.09270791709423065}
# INFO:__main__:y_cont granular MAE = [0.04631894 0.06270943 0.03522167 0.22658174]
# INFO:__main__:mean mse = 0.0218
# INFO:__main__:std mse = 0.0144
# INFO:__main__:mean mae = 0.1010
# INFO:__main__:std mae = 0.0349

# phaser
# INFO:__main__:{'loss': 0.025490181520581245,
#                'mae': 0.10815902054309845}
# INFO:__main__:y_cont granular MAE = [0.1029989  0.09811173 0.05666324 0.03905379 0.24396719]
# INFO:__main__:mean mse = 0.0247
# INFO:__main__:std mse = 0.0220
# INFO:__main__:mean mae = 0.1083
# INFO:__main__:std mae = 0.0521

# reverb-hall
# INFO:__main__:{'loss': 0.03149664029479027,
#                'mae': 0.13025474548339844}
# INFO:__main__:y_cont granular MAE = [0.09304024 0.17627536 0.09998553 0.18617088 0.06083341 0.16522278]
# INFO:__main__:mean mse = 0.0339
# INFO:__main__:std mse = 0.0076
# INFO:__main__:mean mae = 0.1657
# INFO:__main__:std mae = 0.0255


# training_eq_l
# saw 56k baseline cnn

# eq
# loss: 0.1923 - eq_typl_loss: 0.1514 - cont_output_loss: 0.0409 - eq_typl_acc: 0.9402 - cont_output_mae: 0.1566
# val_loss: 0.2436 - val_eq_typl_loss: 0.2071 - val_cont_output_loss: 0.0365 - val_eq_typl_acc: 0.9248 - val_cont_output_mae: 0.1447
# multi
# loss: 0.1730 - eq_typl_loss: 0.1343 - cont_output_loss: 0.0387 - eq_typl_acc: 0.9467 - cont_output_mae: 0.1510
# val_loss: 0.2712 - val_eq_typl_loss: 0.2363 - val_cont_output_loss: 0.0349 - val_eq_typl_acc: 0.9089 - val_cont_output_mae: 0.1400

# compressor
# loss: 0.0049 - mae: 0.0533 - val_loss: 0.0039 - val_mae: 0.0425
# multi
# loss: 0.0050 - mae: 0.0536 - val_loss: 0.0040 - val_mae: 0.0439

# distortion
# loss: 0.4207 - dist_mode_loss: 0.3757 - cont_output_loss: 0.0451 - dist_mode_acc: 0.8445 - cont_output_mae: 0.1678
# val_loss: 0.5214 - val_dist_mode_loss: 0.4812 - val_cont_output_loss: 0.0402 - val_dist_mode_acc: 0.8132 - val_cont_output_mae: 0.1536
# multi
# loss: 0.4153 - dist_mode_loss: 0.3701 - cont_output_loss: 0.0451 - dist_mode_acc: 0.8440 - cont_output_mae: 0.1674
# val_loss: 0.5112 - val_dist_mode_loss: 0.4700 - val_cont_output_loss: 0.0411 - val_dist_mode_acc: 0.8209 - val_cont_output_mae: 0.1568


# seq_5


# compressor

# basic shapes  baseline cnn 2x
# loss: 0.0120 - mae: 0.0813 - val_loss: 0.0102 - val_mae: 0.0670
# loss: 0.0211 - mae: 0.1103 - val_loss: 0.0225 - val_mae: 0.1065  (x, x)
# loss: 0.0120 - mae: 0.0811 - val_loss: 0.0103 - val_mae: 0.0669  2nd time individual

# epoch 47  loss: 0.0165 - mae: 0.0990 - val_loss: 0.0137 - val_mae: 0.0870  exclude all
# epoch  8  loss: 0.0206 - mae: 0.1090 - val_loss: 0.0174 - val_mae: 0.0963  exclude all bi

# basic shapes  baseline cnn
# loss: 0.0118 - mae: 0.0773 - val_loss: 0.0110 - val_mae: 0.0692

# adv shapes  baseline cnn 2x
# loss: 0.0064 - mae: 0.0616 - val_loss: 0.0037 - val_mae: 0.0441

# temporal  baseline cnn 2x
# loss: 0.0073 - mae: 0.0660 - val_loss: 0.0044 - val_mae: 0.0478


# distortion

# basic shapes  baseline cnn 2x
# loss: 0.4964 - dist_mode_loss: 0.4445 - cont_output_loss: 0.0519 - dist_mode_acc: 0.8090 - cont_output_mae: 0.1834
# val_loss: 0.5108 - val_dist_mode_loss: 0.4669 - val_cont_output_loss: 0.0439 - val_dist_mode_acc: 0.7986 - val_cont_output_mae: 0.1660
# loss: 0.4345 - dist_mode_loss: 0.3846 - cont_output_loss: 0.0499 - dist_mode_acc: 0.8297 - cont_output_mae: 0.1794
# val_loss: 0.4957 - val_dist_mode_loss: 0.4548 - val_cont_output_loss: 0.0409 - val_dist_mode_acc: 0.8047 - val_cont_output_mae: 0.1585  2nd time individual

# epoch 48  loss: 0.3490 - dist_mode_loss: 0.2888 - cont_output_loss: 0.0602 - dist_mode_acc: 0.8726 - cont_output_mae: 0.2003  exclude all
# val_loss: 0.3027 - val_dist_mode_loss: 0.2563 - val_cont_output_loss: 0.0464 - val_dist_mode_acc: 0.8788 - val_cont_output_mae: 0.1754
# epoch 28  loss: 0.3879 - dist_mode_loss: 0.3294 - cont_output_loss: 0.0586 - dist_mode_acc: 0.8575 - cont_output_mae: 0.1975  exclude all bi
# val_loss: 0.3441 - val_dist_mode_loss: 0.2980 - val_cont_output_loss: 0.0461 - val_dist_mode_acc: 0.8641 - val_cont_output_mae: 0.1728

# basic shapes  baseline cnn
# loss: 0.4849 - dist_mode_loss: 0.4343 - cont_output_loss: 0.0506 - dist_mode_acc: 0.8115 - cont_output_mae: 0.1806
# val_loss: 0.5252 - val_dist_mode_loss: 0.4815 - val_cont_output_loss: 0.0437 - val_dist_mode_acc: 0.8005 - val_cont_output_mae: 0.1652
# basic shapes  exposure cnn
# loss: 0.6227 - dist_mode_loss: 0.5424 - cont_output_loss: 0.0803 - dist_mode_acc: 0.7761 - cont_output_mae: 0.2309
# val_loss: 0.6168 - val_dist_mode_loss: 0.5515 - val_cont_output_loss: 0.0653 - val_dist_mode_acc: 0.7797 - val_cont_output_mae: 0.2114
# basic shapes  baseline lstm
# loss: 0.5199 - dist_mode_loss: 0.4714 - cont_output_loss: 0.0485 - dist_mode_acc: 0.8018 - cont_output_mae: 0.1743
# val_loss: 0.6044 - val_dist_mode_loss: 0.5589 - val_cont_output_loss: 0.0455 - val_dist_mode_acc: 0.7726 - val_cont_output_mae: 0.1666

# adv shapes  baseline cnn 2x
# loss: 0.6594 - dist_mode_loss: 0.6006 - cont_output_loss: 0.0587 - dist_mode_acc: 0.7471 - cont_output_mae: 0.1990
# val_loss: 0.7390 - val_dist_mode_loss: 0.6894 - val_cont_output_loss: 0.0496 - val_dist_mode_acc: 0.7163 - val_cont_output_mae: 0.1813

# temporal  baseline cnn 2x
# loss: 0.6372 - dist_mode_loss: 0.5803 - cont_output_loss: 0.0569 - dist_mode_acc: 0.7557 - cont_output_mae: 0.1946
# val_loss: 0.6931 - val_dist_mode_loss: 0.6463 - val_cont_output_loss: 0.0468 - val_dist_mode_acc: 0.7315 - val_cont_output_mae: 0.1723


# eq

# basic shapes  baseline cnn 2x
# loss: 0.2039 - eq_typl_loss: 0.1600 - cont_output_loss: 0.0439 - eq_typl_acc: 0.9341 - cont_output_mae: 0.1629
# val_loss: 0.2483 - val_eq_typl_loss: 0.2119 - val_cont_output_loss: 0.0365 - val_eq_typl_acc: 0.9115 - val_cont_output_mae: 0.1440
# loss: 0.4000 - eq_typl_loss: 0.3351 - cont_output_loss: 0.0649 - eq_typl_acc: 0.8398 - cont_output_mae: 0.2089   (x, x)
# val_loss: 0.4419 - val_eq_typl_loss: 0.3806 - val_cont_output_loss: 0.0613 - val_eq_typl_acc: 0.8099 - val_cont_output_mae: 0.2026  (x, x)
# loss: 0.2109 - eq_typl_loss: 0.1669 - cont_output_loss: 0.0440 - eq_typl_acc: 0.9312 - cont_output_mae: 0.1632
# val_loss: 0.2420 - val_eq_typl_loss: 0.2043 - val_cont_output_loss: 0.0377 - val_eq_typl_acc: 0.9147 - val_cont_output_mae: 0.1475  2nd time individual

# epoch 11  loss: 0.2521 - eq_typl_loss: 0.1870 - cont_output_loss: 0.0651 - eq_typl_acc: 0.9218 - cont_output_mae: 0.2086  exclude all
# val_loss: 0.2528 - val_eq_typl_loss: 0.1948 - val_cont_output_loss: 0.0579 - val_eq_typl_acc: 0.9159 - val_cont_output_mae: 0.1966
# epoch 16  loss: 0.2167 - eq_typl_loss: 0.1503 - cont_output_loss: 0.0664 - eq_typl_acc: 0.9390 - cont_output_mae: 0.2110  exclude all
# val_loss: 0.2301 - val_eq_typl_loss: 0.1704 - val_cont_output_loss: 0.0597 - val_eq_typl_acc: 0.9292 - val_cont_output_mae: 0.2003
# epoch  9  loss: 0.2747 - eq_typl_loss: 0.2103 - cont_output_loss: 0.0645 - eq_typl_acc: 0.9106 - cont_output_mae: 0.2073  exclude all bi
# val_loss: 0.2917 - val_eq_typl_loss: 0.2339 - val_cont_output_loss: 0.0578 - val_eq_typl_acc: 0.8974 - val_cont_output_mae: 0.1953

# basic shapes  baseline cnn 8x
# epoch 10  loss: 0.7824 - eq_typl_loss: 0.6957 - cont_output_loss: 0.0867 - eq_typl_acc: 0.5006 - cont_output_mae: 0.2543  exclude all
# val_loss: 0.7788 - val_eq_typl_loss: 0.6934 - val_cont_output_loss: 0.0853 - val_eq_typl_acc: 0.4946 - val_cont_output_mae: 0.2531  exclude all

# basic shapes  baseline cnn shallow
# epoch  8  loss: 0.4466 - eq_typl_loss: 0.3719 - cont_output_loss: 0.0748 - eq_typl_acc: 0.8238 - cont_output_mae: 0.2273  exclude all
# val_loss: 0.3926 - val_eq_typl_loss: 0.3282 - val_cont_output_loss: 0.0644 - val_eq_typl_acc: 0.8427 - val_cont_output_mae: 0.2097  exclude all


# adv shapes  baseline cnn 2x
# loss: 0.2652 - eq_typl_loss: 0.2210 - cont_output_loss: 0.0442 - eq_typl_acc: 0.9073 - cont_output_mae: 0.1630
# val_loss: 0.2767 - val_eq_typl_loss: 0.2409 - val_cont_output_loss: 0.0357 - val_eq_typl_acc: 0.8988 - val_cont_output_mae: 0.1411

# temporal  baseline cnn 2x
# loss: 0.2523 - eq_typl_loss: 0.2064 - cont_output_loss: 0.0459 - eq_typl_acc: 0.9102 - cont_output_mae: 0.1671
# val_loss: 0.2955 - val_eq_typl_loss: 0.2571 - val_cont_output_loss: 0.0384 - val_eq_typl_acc: 0.8861 - val_cont_output_mae: 0.1461


# flanger

# basic shapes  baseline cnn 2x
# loss: 0.0096 - mae: 0.0733 - val_loss: 0.0095 - val_mae: 0.0592

# epoch 12  loss: 0.0135 - mae: 0.0867 - val_loss: 0.0098 - val_mae: 0.0657  exclude all
# epoch 17  loss: 0.0126 - mae: 0.0842 - val_loss: 0.0088 - val_mae: 0.0645
# epoch 20  loss: 0.0124 - mae: 0.0836 - val_loss: 0.0085 - val_mae: 0.0625  exclude all bi

# adv shapes  baseline cnn 2x
# loss: 0.0088 - mae: 0.0709 - val_loss: 0.0073 - val_mae: 0.0536

# temporal  baseline cnn 2x
# loss: 0.0084 - mae: 0.0703 - val_loss: 0.0075 - val_mae: 0.0554


# phaser

# basic shapes  baseline cnn 2x
# loss: 0.0176 - mae: 0.0992 - val_loss: 0.0175 - val_mae: 0.0876
# loss: 0.0205 - mae: 0.1081 - val_loss: 0.0211 - val_mae: 0.1011  (x, x)
# basic shapes  baseline cnn
# loss: 0.0202 - mae: 0.1037 - val_loss: 0.0195 - val_mae: 0.0963

# epoch 18  loss: 0.0186 - mae: 0.1036 - val_loss: 0.0141 - val_mae: 0.0845  exclude all
# epoch 24  loss: 0.0178 - mae: 0.1017 - val_loss: 0.0133 - val_mae: 0.0818
# epoch 84  loss: 0.0152 - mae: 0.0950 - val_loss: 0.0106 - val_mae: 0.0734  exclude all bi

# adv shapes  baseline cnn 2x
# loss: 0.0202 - mae: 0.1060 - val_loss: 0.0183 - val_mae: 0.0915

# temporal  baseline cnn 2x
# loss: 0.0198 - mae: 0.1063 - val_loss: 0.0197 - val_mae: 0.0972


# effect rnn

# basic shapes  baseline cnn 2x
# epoch  4 loss: 0.1635 - acc: 0.9439 - val_loss: 0.1124 - val_acc: 0.9589
# epoch  4 loss: 0.1629 - acc: 0.9434 - val_loss: 0.1169 - val_acc: 0.9573  2nd time same collapse
# basic shapes  baseline cnn
# epoch  5 loss: 0.1205 - acc: 0.9569 - val_loss: 0.0941 - val_acc: 0.9653
# epoch 11 loss: 0.1123 - acc: 0.9606 - val_loss: 0.0911 - val_acc: 0.9671
# epoch 17 loss: 0.1151 - acc: 0.9601 - val_loss: 0.0903 - val_acc: 0.9678
# epoch  2 loss: 1.1669 - acc: 0.3408 - val_loss: 1.1574 - val_acc: 0.3403  (x, x)

# adv shapes  baseline cnn
# epoch  3 loss: 0.1136 - acc: 0.9602 - val_loss: 0.0802 - val_acc: 0.9713
# epoch  6 loss: 0.0983 - acc: 0.9663 - val_loss: 0.0765 - val_acc: 0.9730
