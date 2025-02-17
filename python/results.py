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



# seq_5_v3

# compressor, basic shapes, baseline cnn 2x
# epoch 39  loss: 0.0145 - mae: 0.0939 - val_loss: 0.0118 - val_mae: 0.0822 ...
# epoch 50  loss: 0.0140 - mae: 0.0923 - val_loss: 0.0110 - val_mae: 0.0791

# n_fft 2048
# epoch 48  loss: 0.0134 - mae: 0.0904 - val_loss: 0.0107 - val_mae: 0.0785

# n_fft 1024, hop_length 256
# epoch 53  loss: 0.0139 - mae: 0.0924 - val_loss: 0.0104 - val_mae: 0.0772

# mfcc 30
# epoch  3  loss: 0.0212 - mae: 0.1111 - val_loss: 0.0170 - val_mae: 0.0971 ...
# epoch 50  loss: 0.0093 - mae: 0.0754 - val_loss: 0.0068 - val_mae: 0.0620 ...
# epoch 87  loss: 0.0085 - mae: 0.0721 - val_loss: 0.0059 - val_mae: 0.0579

# compressor, adv shapes, baseline cnn 2x
# epoch 32  loss: 0.0105 - mae: 0.0801 - val_loss: 0.0075 - val_mae: 0.0658 ...
# epoch 44  loss: 0.0100 - mae: 0.0783 - val_loss: 0.0070 - val_mae: 0.0637

# mfcc 30
# epoch 53  loss: 0.0070 - mae: 0.0658 - val_loss: 0.0044 - val_mae: 0.0510

# compressor, temporal, baseline cnn 2x
# epoch 18  loss: 0.0113 - mae: 0.0832 - val_loss: 0.0082 - val_mae: 0.0689 ...
# epoch 71  loss: 0.0090 - mae: 0.0750 - val_loss: 0.0057 - val_mae: 0.0585

# mfcc 30
# epoch 39  loss: 0.0070 - mae: 0.0659 - val_loss: 0.0039 - val_mae: 0.0486


# distortion, basic shapes, baseline cnn 2x
# epoch 40  loss: 0.1385 - dist_mode_loss: 0.1036 - cont_output_loss: 0.0349 - dist_mode_acc: 0.9656 - cont_output_mae: 0.1528
# val_loss: 0.1017 - val_dist_mode_loss: 0.0769 - val_cont_output_loss: 0.0248 - val_dist_mode_acc: 0.9712 - val_cont_output_mae: 0.1272

# n_fft 2048
# epoch 52  loss: 0.1185 - dist_mode_loss: 0.0820 - cont_output_loss: 0.0364 - dist_mode_acc: 0.9734 - cont_output_mae: 0.1560
# val_loss: 0.0892 - val_dist_mode_loss: 0.0647 - val_cont_output_loss: 0.0246 - val_dist_mode_acc: 0.9770 - val_cont_output_mae: 0.1269

# n_fft 1024, hop_length 256
# epoch 45  loss: 0.1648 - dist_mode_loss: 0.1224 - cont_output_loss: 0.0424 - dist_mode_acc: 0.9593 - cont_output_mae: 0.1703
# val_loss: 0.1248 - val_dist_mode_loss: 0.0917 - val_cont_output_loss: 0.0332 - val_dist_mode_acc: 0.9673 - val_cont_output_mae: 0.1529

# mfcc 60
# epoch 38  loss: 0.1144 - dist_mode_loss: 0.0759 - cont_output_loss: 0.0386 - dist_mode_acc: 0.9755 - cont_output_mae: 0.1610
# val_loss: 0.0781 - val_dist_mode_loss: 0.0514 - val_cont_output_loss: 0.0266 - val_dist_mode_acc: 0.9820 - val_cont_output_mae: 0.1339

# n_mfcc 30
# epoch 48  loss: 0.1033 - dist_mode_loss: 0.0650 - cont_output_loss: 0.0383 - dist_mode_acc: 0.9799 - cont_output_mae: 0.1603
# val_loss: 0.0734 - val_dist_mode_loss: 0.0438 - val_cont_output_loss: 0.0296 - val_dist_mode_acc: 0.9850 - val_cont_output_mae: 0.1422

# mfcc 30
# epoch  5  loss: 0.2878 - dist_mode_loss: 0.2518 - cont_output_loss: 0.0360 - dist_mode_acc: 0.9032 - cont_output_mae: 0.1570
# val_loss: 0.2171 - val_dist_mode_loss: 0.1884 - val_cont_output_loss: 0.0287 - val_dist_mode_acc: 0.9266 - val_cont_output_mae: 0.1393 ...
# epoch 14  loss: 0.1509 - dist_mode_loss: 0.1152 - cont_output_loss: 0.0357 - dist_mode_acc: 0.9602 - cont_output_mae: 0.1553
# val_loss: 0.1140 - val_dist_mode_loss: 0.0835 - val_cont_output_loss: 0.0305 - val_dist_mode_acc: 0.9696 - val_cont_output_mae: 0.1452 ...
# epoch 34  loss: 0.1102 - dist_mode_loss: 0.0729 - cont_output_loss: 0.0373 - dist_mode_acc: 0.9765 - cont_output_mae: 0.1582
# val_loss: 0.0806 - val_dist_mode_loss: 0.0530 - val_cont_output_loss: 0.0276 - val_dist_mode_acc: 0.9824 - val_cont_output_mae: 0.1365 ...
# epoch 42  loss: 0.1056 - dist_mode_loss: 0.0677 - cont_output_loss: 0.0378 - dist_mode_acc: 0.9787 - cont_output_mae: 0.1593
# val_loss: 0.0734 - val_dist_mode_loss: 0.0471 - val_cont_output_loss: 0.0263 - val_dist_mode_acc: 0.9845 - val_cont_output_mae: 0.1329

# only mfcc 30
# epoch 48  loss: 0.1867 - dist_mode_loss: 0.1423 - cont_output_loss: 0.0443 - dist_mode_acc: 0.9527 - cont_output_mae: 0.1762
# val_loss: 0.1449 - val_dist_mode_loss: 0.1083 - val_cont_output_loss: 0.0366 - val_dist_mode_acc: 0.9624 - val_cont_output_mae: 0.1632 ...

# proc
# epoch 37  loss: 0.1078 - dist_mode_loss: 0.0704 - cont_output_loss: 0.0375 - dist_mode_acc: 0.9776 - cont_output_mae: 0.1583
# val_loss: 0.0815 - val_dist_mode_loss: 0.0534 - val_cont_output_loss: 0.0281 - val_dist_mode_acc: 0.9811 - val_cont_output_mae: 0.1376 ...
# epoch 38  loss: 0.1075 - dist_mode_loss: 0.0700 - cont_output_loss: 0.0375 - dist_mode_acc: 0.9780 - cont_output_mae: 0.1585
# val_loss: 0.0768 - val_dist_mode_loss: 0.0496 - val_cont_output_loss: 0.0272 - val_dist_mode_acc: 0.9823 - val_cont_output_mae: 0.1352

# distortion, adv shapes, baseline cnn 2x
# epoch 48  loss: 0.2018 - dist_mode_loss: 0.1614 - cont_output_loss: 0.0404 - dist_mode_acc: 0.9488 - cont_output_mae: 0.1657
# val_loss: 0.1935 - val_dist_mode_loss: 0.1587 - val_cont_output_loss: 0.0348 - val_dist_mode_acc: 0.9467 - val_cont_output_mae: 0.1553

# mfcc 30
# epoch 38  loss: 0.1420 - dist_mode_loss: 0.1007 - cont_output_loss: 0.0413 - dist_mode_acc: 0.9707 - cont_output_mae: 0.1679
# val_loss: 0.1215 - val_dist_mode_loss: 0.0902 - val_cont_output_loss: 0.0312 - val_dist_mode_acc: 0.9727 - val_cont_output_mae: 0.1483
# epoch 40  loss: 0.1401 - dist_mode_loss: 0.0986 - cont_output_loss: 0.0415 - dist_mode_acc: 0.9715 - cont_output_mae: 0.1683
# val_loss: 0.1180 - val_dist_mode_loss: 0.0871 - val_cont_output_loss: 0.0309 - val_dist_mode_acc: 0.9728 - val_cont_output_mae: 0.1475

# distortion, temporal, baseline cnn 2x
# epoch 13  loss: 0.2067 - dist_mode_loss: 0.1719 - cont_output_loss: 0.0348 - dist_mode_acc: 0.9376 - cont_output_mae: 0.1538
# val_loss: 0.1755 - val_dist_mode_loss: 0.1486 - val_cont_output_loss: 0.0268 - val_dist_mode_acc: 0.9436 - val_cont_output_mae: 0.1345 ...
# epoch 39  loss: 0.1380 - dist_mode_loss: 0.1007 - cont_output_loss: 0.0373 - dist_mode_acc: 0.9677 - cont_output_mae: 0.1592
# val_loss: 0.1199 - val_dist_mode_loss: 0.0910 - val_cont_output_loss: 0.0290 - val_dist_mode_acc: 0.9701 - val_cont_output_mae: 0.1419

# mfcc 30
# epoch 27  loss: 0.1061 - dist_mode_loss: 0.0695 - cont_output_loss: 0.0366 - dist_mode_acc: 0.9792 - cont_output_mae: 0.1573
# val_loss: 0.0765 - val_dist_mode_loss: 0.0503 - val_cont_output_loss: 0.0262 - val_dist_mode_acc: 0.9836 - val_cont_output_mae: 0.1334

# eq, basic shapes, baseline cnn 2x
# epoch 16  loss: 0.0171 - mae: 0.0982 - val_loss: 0.0153 - val_mae: 0.0894 ... ?

# n_fft 2048
# epoch 64  loss: 0.0121 - mae: 0.0842 - val_loss: 0.0100 - val_mae: 0.0733

# n_fft 1024, hop_length 256
# epoch 16  loss: 0.0152 - mae: 0.0934 - val_loss: 0.0132 - val_mae: 0.0833
# epoch 64  loss: 0.0120 - mae: 0.0839 - val_loss: 0.0099 - val_mae: 0.0735
# epoch 78  loss: 0.0117 - mae: 0.0830 - val_loss: 0.0096 - val_mae: 0.0725

# mfcc 30
# epoch 44  loss: 0.0095 - mae: 0.0746 - val_loss: 0.0074 - val_mae: 0.0626
# epoch 63  loss: 0.0088 - mae: 0.0719 - val_loss: 0.0067 - val_mae: 0.0598

# eq, adv shapes, baseline cnn 2x
# epoch 24  loss: 0.0121 - mae: 0.0838 - val_loss: 0.0098 - val_mae: 0.0724 ...
# epoch 39  loss: 0.0109 - mae: 0.0804 - val_loss: 0.0086 - val_mae: 0.0683

# mfcc 30
# epoch 59  loss: 0.0067 - mae: 0.0641 - val_loss: 0.0046 - val_mae: 0.0505

# eq, temporal, baseline cnn 2x
# epoch 51  loss: 0.0109 - mae: 0.0805 - val_loss: 0.0085 - val_mae: 0.0683

# mfcc 30
# epoch  9  loss: 0.0127 - mae: 0.0855 - val_loss: 0.0103 - val_mae: 0.0739 ...
# epoch 20  loss: 0.0095 - mae: 0.0751 - val_loss: 0.0075 - val_mae: 0.0645 ...
# epoch 36  loss: 0.0081 - mae: 0.0695 - val_loss: 0.0059 - val_mae: 0.0571 ...
# epoch 75  loss: 0.0069 - mae: 0.0643 - val_loss: 0.0047 - val_mae: 0.0512

# phaser, basic shapes, baseline cnn 2x
# epoch 81  loss: 0.0110 - mae: 0.0815 - val_loss: 0.0071 - val_mae: 0.0617

# n_fft 2048
# epoch 53  loss: 0.0111 - mae: 0.0821 - val_loss: 0.0072 - val_mae: 0.0630

# n_fft 1024, hop_length 256
# epoch 45  loss: 0.0122 - mae: 0.0857 - val_loss: 0.0083 - val_mae: 0.0677

# mfcc 30
# epoch 37  loss: 0.0085 - mae: 0.0718 - val_loss: 0.0052 - val_mae: 0.0532 ...
# epoch 76  loss: 0.0076 - mae: 0.0680 - val_loss: 0.0042 - val_mae: 0.0476

# only mfcc 30
# epoch 49  loss: 0.0116 - mae: 0.0839 - val_loss: 0.0086 - val_mae: 0.0683 ...

# phaser, adv shapes, baseline cnn 2x
# epoch 32  loss: 0.0105 - mae: 0.0802 - val_loss: 0.0064 - val_mae: 0.0595

# mfcc 30
# epoch 58  loss: 0.0069 - mae: 0.0654 - val_loss: 0.0037 - val_mae: 0.0455

# phaser, temporal, baseline cnn 2x
# epoch 63  loss: 0.0104 - mae: 0.0801 - val_loss: 0.0066 - val_mae: 0.0611

# mfcc 30
# epoch 51  loss: 0.0075 - mae: 0.0682 - val_loss: 0.0042 - val_mae: 0.0490

# reverb-hall, basic shapes, baseline cnn 2x
# epoch 13  loss: 0.0059 - mae: 0.0586 - val_loss: 0.0034 - val_mae: 0.0427

# mfcc 30
# epoch 10  loss: 0.0052 - mae: 0.0551 - val_loss: 0.0028 - val_mae: 0.0393 ...
# epoch 32  loss: 0.0042 - mae: 0.0500 - val_loss: 0.0020 - val_mae: 0.0339

# reverb-hall, adv shapes, baseline cnn 2x
# epoch 82  loss: 0.0094 - mae: 0.0747 - val_loss: 0.0074 - val_mae: 0.0642

# mfcc 30
# epoch 50  loss: 0.0065 - mae: 0.0626 - val_loss: 0.0051 - val_mae: 0.0519

# reverb-hall, temporal, baseline cnn 2x
# epoch 42  loss: 0.0078 - mae: 0.0679 - val_loss: 0.0055 - val_mae: 0.0552

# mfcc 30
# epoch 43  loss: 0.0054 - mae: 0.0568 - val_loss: 0.0034 - val_mae: 0.0433

# rnn, basic shapes, baseline cnn
# epoch  9  loss: 0.0653 - acc: 0.9777 - val_loss: 0.0458 - val_acc: 0.9837

# gru
# epoch 13  loss: 0.0772 - acc: 0.9745 - val_loss: 0.0510 - val_acc: 0.9844
# no cnn
# epoch 31  loss: 1.1545 - acc: 0.3430 - val_loss: 1.1498 - val_acc: 0.3426

# mfcc 30, next_effect_rnn
# epoch  6  loss: 0.0741 - acc: 0.9749 - val_loss: 0.0490 - val_acc: 0.9829

# mfcc 30, next_effect_seq_only_rnn
# epoch 12  loss: 0.1139 - acc: 0.9620 - val_loss: 0.0837 - val_acc: 0.9707

# mfcc 30, all_effects_cnn
# epoch 25  loss: 0.1380 - acc: 0.3322 - val_loss: 0.1291 - val_acc: 0.2870

# rnn, adv shapes, baseline cnn
# epoch  8  loss: 0.0559 - acc: 0.9815 - val_loss: 0.0403 - val_acc: 0.9858

# gru
# epoch 10  loss: 0.0645 - acc: 0.9795 - val_loss: 0.0415 - val_acc: 0.9863
# no cnn
# epoch 20  loss: 1.1553 - acc: 0.3421 - val_loss: 1.1507 - val_acc: 0.3434

# mfcc 30, next_effect_rnn
# epoch  5  loss: 0.0712 - acc: 0.9760 - val_loss: 0.0454 - val_acc: 0.9861

# mfcc 30, next_effect_seq_only_rnn
# epoch 16  loss: 0.1161 - acc: 0.9617 - val_loss: 0.0877 - val_acc: 0.9689

# mfcc 30, all_effects_cnn
# epoch 18  loss: 0.1360 - acc: 0.4729 - val_loss: 0.1241 - val_acc: 0.4792

# rnn, temporal, baseline cnn
# epoch 10  loss: 0.0552 - acc: 0.9819 - val_loss: 0.0383 - val_acc: 0.9877

# gru
# epoch  8  loss: 0.0639 - acc: 0.9790 - val_loss: 0.0406 - val_acc: 0.9865

# mfcc 30, next_effect_rnn
# epoch  4  loss: 0.0712 - acc: 0.9761 - val_loss: 0.0450 - val_acc: 0.9838

# mfcc 30, next_effect_seq_only_rnn
# epoch 16  loss: 0.1003 - acc: 0.9686 - val_loss: 0.0707 - val_acc: 0.9741

# mfcc 30, all_effects_cnn
# epoch 19  loss: 0.1239 - binary_accuracy: 0.9535 - val_loss: 0.1149 - val_binary_accuracy: 0.9541

# workshop results

# INFO:__main__:model_name = seq_5_v3__basic_shapes__rnn__baseline_cnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.048544157296419144, 'acc': 0.9833188652992249}
# INFO:__main__:pred.shape = (24159, 5)
# INFO:__main__:n_effects: 1, n = 3329, % = 0.9969960949234005
# INFO:__main__:n_effects: 2, n = 7939, % = 0.9833732208086661
# INFO:__main__:n_effects: 3, n = 8099, % = 0.9813557229287566
# INFO:__main__:n_effects: 4, n = 4000, % = 0.97275
# INFO:__main__:n_effects: 5, n = 792, % = 0.9987373737373737
# INFO:__main__:all_results length = 24159
# INFO:__main__:all_results % = 0.9833188459787243

# INFO:__main__:model_name = seq_5_v3__adv_shapes__rnn__baseline_cnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.043449752032756805, 'acc': 0.9849331378936768}
# INFO:__main__:pred.shape = (24159, 5)
# INFO:__main__:n_effects: 1, n = 3304, % = 0.9930387409200968
# INFO:__main__:n_effects: 2, n = 8049, % = 0.9845943595477699
# INFO:__main__:n_effects: 3, n = 7949, % = 0.9788652660712039
# INFO:__main__:n_effects: 4, n = 4025, % = 0.9878260869565217
# INFO:__main__:n_effects: 5, n = 832, % = 1.0
# INFO:__main__:all_results length = 24159
# INFO:__main__:all_results % = 0.9849331512065896

# INFO:__main__:model_name = seq_5_v3__temporal__rnn__baseline_cnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.04112916439771652, 'acc': 0.9863399267196655}
# INFO:__main__:pred.shape = (24158, 5)
# INFO:__main__:n_effects: 1, n = 3394, % = 0.9970536240424278
# INFO:__main__:n_effects: 2, n = 8001, % = 0.9886264216972879
# INFO:__main__:n_effects: 3, n = 8147, % = 0.9831839941082607
# INFO:__main__:n_effects: 4, n = 3863, % = 0.976702045042713
# INFO:__main__:n_effects: 5, n = 753, % = 0.99734395750332
# INFO:__main__:all_results length = 24158
# INFO:__main__:all_results % = 0.9863399288020531


# EvoMUSART RNN Results

# INFO:__main__:model_name = seq_5_v3__mfcc_30__temporal__rnn__next_effect_rnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.044726308435201645, 'acc': 0.9848911166191101}
# INFO:__main__:pred.shape = (24158, 5)
# INFO:__main__:
# INFO:__main__:effect_results:
# INFO:__main__:effect_name: compressor , n = 4969, % = 0.97947
# INFO:__main__:effect_name: distortion , n = 4373, % = 0.97645
# INFO:__main__:effect_name: eq         , n = 4955, % = 0.97982
# INFO:__main__:effect_name: phaser     , n = 4947, % = 0.99030
# INFO:__main__:effect_name: reverb-hall, n = 4914, % = 0.99756
# INFO:__main__:
# INFO:__main__:effect_all_results length = 24158
# INFO:__main__:effect_all_results % = 0.98489
# INFO:__main__:
# INFO:__main__:seq_len_results:
# INFO:__main__:n_effects: 1, n = 3361, % = 0.99405
# INFO:__main__:n_effects: 2, n = 7990, % = 0.98448
# INFO:__main__:n_effects: 3, n = 7996, % = 0.98299
# INFO:__main__:n_effects: 4, n = 4008, % = 0.97904
# INFO:__main__:n_effects: 5, n = 803, % = 0.99875
# INFO:__main__:
# INFO:__main__:seq_len_all_results length = 24158
# INFO:__main__:seq_len_all_results % = 0.98489
# INFO:__main__:
# INFO:__main__:latex table row = 0.994 & 0.984 & 0.983 & 0.979 & 0.999 & 0.985

# INFO:__main__:model_name = seq_5_v3__mfcc_30__temporal__rnn__next_effect_seq_only_rnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.07591500133275986, 'acc': 0.9710654616355896}
# INFO:__main__:pred.shape = (24158, 5)
# INFO:__main__:
# INFO:__main__:effect_results:
# INFO:__main__:effect_name: compressor , n = 4969, % = 0.97062
# INFO:__main__:effect_name: distortion , n = 4373, % = 0.96684
# INFO:__main__:effect_name: eq         , n = 4955, % = 0.98507
# INFO:__main__:effect_name: phaser     , n = 4947, % = 0.96321
# INFO:__main__:effect_name: reverb-hall, n = 4914, % = 0.96907
# INFO:__main__:
# INFO:__main__:effect_all_results length = 24158
# INFO:__main__:effect_all_results % = 0.97107
# INFO:__main__:
# INFO:__main__:seq_len_results:
# INFO:__main__:n_effects: 1, n = 3361, % = 0.99197
# INFO:__main__:n_effects: 2, n = 7990, % = 0.97447
# INFO:__main__:n_effects: 3, n = 7996, % = 0.96061
# INFO:__main__:n_effects: 4, n = 4008, % = 0.96183
# INFO:__main__:n_effects: 5, n = 803, % = 1.00000
# INFO:__main__:
# INFO:__main__:seq_len_all_results length = 24158
# INFO:__main__:seq_len_all_results % = 0.97107
# INFO:__main__:
# INFO:__main__:latex table row = 0.992 & 0.974 & 0.961 & 0.962 & 1.000 & 0.971

# INFO:__main__:model_name = seq_5_v3__mfcc_30__temporal__rnn__all_effects_cnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.11370770633220673, 'binary_accuracy': 0.9549914598464966}
# INFO:__main__:pred.shape = (24158, 5)
# INFO:__main__:
# INFO:__main__:effect_results:
# INFO:__main__:effect_name: compressor , n = 24158, % = 0.96539
# INFO:__main__:effect_name: distortion , n = 24158, % = 0.97798
# INFO:__main__:effect_name: eq         , n = 24158, % = 0.88087
# INFO:__main__:effect_name: phaser     , n = 24158, % = 0.97901
# INFO:__main__:effect_name: reverb-hall, n = 24158, % = 0.97160
# INFO:__main__:
# INFO:__main__:effect_all_results length = 120790
# INFO:__main__:effect_all_results % = 0.95497
# INFO:__main__:
# INFO:__main__:seq_len_results:
# INFO:__main__:n_effects: 1, n = 16805, % = 0.99250
# INFO:__main__:n_effects: 2, n = 39950, % = 0.97477
# INFO:__main__:n_effects: 3, n = 39980, % = 0.94555
# INFO:__main__:n_effects: 4, n = 20040, % = 0.91602
# INFO:__main__:n_effects: 5, n = 4015, % = 0.88917
# INFO:__main__:
# INFO:__main__:seq_len_all_results length = 120790
# INFO:__main__:seq_len_all_results % = 0.95497
# INFO:__main__:
# INFO:__main__:latex table row = 0.993 & 0.975 & 0.946 & 0.916 & 0.889 & 0.955



# INFO:__main__:model_name = seq_5_v3__mfcc_30__adv_shapes__rnn__next_effect_rnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.04636402800679207, 'acc': 0.9846020340919495}
# INFO:__main__:pred.shape = (24159, 5)
# INFO:__main__:
# INFO:__main__:effect_results:
# INFO:__main__:effect_name: compressor , n = 4914, % = 0.96540
# INFO:__main__:effect_name: distortion , n = 4376, % = 0.98766
# INFO:__main__:effect_name: eq         , n = 5007, % = 0.98822
# INFO:__main__:effect_name: phaser     , n = 4931, % = 0.99250
# INFO:__main__:effect_name: reverb-hall, n = 4931, % = 0.98945
# INFO:__main__:
# INFO:__main__:effect_all_results length = 24159
# INFO:__main__:effect_all_results % = 0.98460
# INFO:__main__:
# INFO:__main__:seq_len_results:
# INFO:__main__:n_effects: 1, n = 3365, % = 0.99346
# INFO:__main__:n_effects: 2, n = 7938, % = 0.98312
# INFO:__main__:n_effects: 3, n = 7958, % = 0.98077
# INFO:__main__:n_effects: 4, n = 4097, % = 0.98584
# INFO:__main__:n_effects: 5, n = 801, % = 0.99376
# INFO:__main__:
# INFO:__main__:seq_len_all_results length = 24159
# INFO:__main__:seq_len_all_results % = 0.98460
# INFO:__main__:
# INFO:__main__:latex table row = 0.993 & 0.983 & 0.981 & 0.986 & 0.994 & 0.985

# INFO:__main__:model_name = seq_5_v3__mfcc_30__adv_shapes__rnn__next_effect_seq_only_rnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.09090328961610794, 'acc': 0.9687901139259338}
# INFO:__main__:pred.shape = (24159, 5)
# INFO:__main__:
# INFO:__main__:effect_results:
# INFO:__main__:effect_name: compressor , n = 4914, % = 0.96337
# INFO:__main__:effect_name: distortion , n = 4376, % = 0.96824
# INFO:__main__:effect_name: eq         , n = 5007, % = 0.97324
# INFO:__main__:effect_name: phaser     , n = 4931, % = 0.97364
# INFO:__main__:effect_name: reverb-hall, n = 4931, % = 0.96532
# INFO:__main__:
# INFO:__main__:effect_all_results length = 24159
# INFO:__main__:effect_all_results % = 0.96879
# INFO:__main__:
# INFO:__main__:seq_len_results:
# INFO:__main__:n_effects: 1, n = 3365, % = 0.98990
# INFO:__main__:n_effects: 2, n = 7938, % = 0.96825
# INFO:__main__:n_effects: 3, n = 7958, % = 0.95866
# INFO:__main__:n_effects: 4, n = 4097, % = 0.96607
# INFO:__main__:n_effects: 5, n = 801, % = 1.00000
# INFO:__main__:
# INFO:__main__:seq_len_all_results length = 24159
# INFO:__main__:seq_len_all_results % = 0.96879
# INFO:__main__:
# INFO:__main__:latex table row = 0.990 & 0.968 & 0.959 & 0.966 & 1.000 & 0.969

# INFO:__main__:model_name = seq_5_v3__mfcc_30__adv_shapes__rnn__all_effects_cnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.12265175580978394, 'binary_accuracy': 0.9524088501930237}
# INFO:__main__:pred.shape = (24159, 5)
# INFO:__main__:
# INFO:__main__:effect_results:
# INFO:__main__:effect_name: compressor , n = 24159, % = 0.95331
# INFO:__main__:effect_name: distortion , n = 24159, % = 0.97831
# INFO:__main__:effect_name: eq         , n = 24159, % = 0.89859
# INFO:__main__:effect_name: phaser     , n = 24159, % = 0.98092
# INFO:__main__:effect_name: reverb-hall, n = 24159, % = 0.95083
# INFO:__main__:
# INFO:__main__:effect_all_results length = 120795
# INFO:__main__:effect_all_results % = 0.95239
# INFO:__main__:
# INFO:__main__:seq_len_results:
# INFO:__main__:n_effects: 1, n = 16825, % = 0.99156
# INFO:__main__:n_effects: 2, n = 39690, % = 0.96800
# INFO:__main__:n_effects: 3, n = 39790, % = 0.94076
# INFO:__main__:n_effects: 4, n = 20485, % = 0.92111
# INFO:__main__:n_effects: 5, n = 4005, % = 0.90861
# INFO:__main__:
# INFO:__main__:seq_len_all_results length = 120795
# INFO:__main__:seq_len_all_results % = 0.95239
# INFO:__main__:
# INFO:__main__:latex table row = 0.992 & 0.968 & 0.941 & 0.921 & 0.909 & 0.952



# INFO:__main__:model_name = seq_5_v3__mfcc_30__basic_shapes__rnn__next_effect_rnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.04527899622917175, 'acc': 0.9831532835960388}
# INFO:__main__:pred.shape = (24159, 5)
# INFO:__main__:
# INFO:__main__:effect_results:
# INFO:__main__:effect_name: compressor , n = 4935, % = 0.98379
# INFO:__main__:effect_name: distortion , n = 4355, % = 0.96785
# INFO:__main__:effect_name: eq         , n = 4853, % = 0.97445
# INFO:__main__:effect_name: phaser     , n = 5077, % = 0.99173
# INFO:__main__:effect_name: reverb-hall, n = 4939, % = 0.99575
# INFO:__main__:
# INFO:__main__:effect_all_results length = 24159
# INFO:__main__:effect_all_results % = 0.98315
# INFO:__main__:
# INFO:__main__:seq_len_results:
# INFO:__main__:n_effects: 1, n = 3326, % = 0.99248
# INFO:__main__:n_effects: 2, n = 8060, % = 0.98263
# INFO:__main__:n_effects: 3, n = 7943, % = 0.98250
# INFO:__main__:n_effects: 4, n = 3956, % = 0.97396
# INFO:__main__:n_effects: 5, n = 874, % = 1.00000
# INFO:__main__:
# INFO:__main__:seq_len_all_results length = 24159
# INFO:__main__:seq_len_all_results % = 0.98315
# INFO:__main__:
# INFO:__main__:latex table row = 0.992 & 0.983 & 0.983 & 0.974 & 1.000 & 0.983

# INFO:__main__:model_name = seq_5_v3__mfcc_30__basic_shapes__rnn__next_effect_seq_only_rnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.08474721759557724, 'acc': 0.9687073230743408}
# INFO:__main__:pred.shape = (24159, 5)
# INFO:__main__:
# INFO:__main__:effect_results:
# INFO:__main__:effect_name: compressor , n = 4935, % = 0.96069
# INFO:__main__:effect_name: distortion , n = 4355, % = 0.94627
# INFO:__main__:effect_name: eq         , n = 4853, % = 0.97074
# INFO:__main__:effect_name: phaser     , n = 5077, % = 0.96908
# INFO:__main__:effect_name: reverb-hall, n = 4939, % = 0.99413
# INFO:__main__:
# INFO:__main__:effect_all_results length = 24159
# INFO:__main__:effect_all_results % = 0.96871
# INFO:__main__:
# INFO:__main__:seq_len_results:
# INFO:__main__:n_effects: 1, n = 3326, % = 0.99128
# INFO:__main__:n_effects: 2, n = 8060, % = 0.96960
# INFO:__main__:n_effects: 3, n = 7943, % = 0.95380
# INFO:__main__:n_effects: 4, n = 3956, % = 0.97093
# INFO:__main__:n_effects: 5, n = 874, % = 1.00000
# INFO:__main__:
# INFO:__main__:seq_len_all_results length = 24159
# INFO:__main__:seq_len_all_results % = 0.96871
# INFO:__main__:
# INFO:__main__:latex table row = 0.991 & 0.970 & 0.954 & 0.971 & 1.000 & 0.969

# INFO:__main__:model_name = seq_5_v3__mfcc_30__basic_shapes__rnn__all_effects_cnn__best.h5
# INFO:__main__:eval_results = {'loss': 0.12926480174064636, 'binary_accuracy': 0.9467304348945618}
# INFO:__main__:pred.shape = (24159, 5)
# INFO:__main__:
# INFO:__main__:effect_results:
# INFO:__main__:effect_name: compressor , n = 24159, % = 0.95770
# INFO:__main__:effect_name: distortion , n = 24159, % = 0.93741
# INFO:__main__:effect_name: eq         , n = 24159, % = 0.86709
# INFO:__main__:effect_name: phaser     , n = 24159, % = 0.97496
# INFO:__main__:effect_name: reverb-hall, n = 24159, % = 0.99640
# INFO:__main__:
# INFO:__main__:effect_all_results length = 120795
# INFO:__main__:effect_all_results % = 0.94671
# INFO:__main__:
# INFO:__main__:seq_len_results:
# INFO:__main__:n_effects: 1, n = 16630, % = 0.98978
# INFO:__main__:n_effects: 2, n = 40300, % = 0.96330
# INFO:__main__:n_effects: 3, n = 39715, % = 0.93564
# INFO:__main__:n_effects: 4, n = 19780, % = 0.91269
# INFO:__main__:n_effects: 5, n = 4370, % = 0.88444
# INFO:__main__:
# INFO:__main__:seq_len_all_results length = 120795
# INFO:__main__:seq_len_all_results % = 0.94671
# INFO:__main__:
# INFO:__main__:latex table row = 0.990 & 0.963 & 0.936 & 0.913 & 0.884 & 0.947
