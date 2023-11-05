## HW1P2

These are the details of the experiments conducted for the assignment
While I maintained this sheet for the experiments, albeit very lately.

I was stuck for a long while on the 14% - 20% accuracy. Took me almost 20 different variation of the model architecture and a week and a half to realize that, my dataloader had a bug, which was causing the data to be shuffled every time. I fixed it, and was able to achieve 70% accuracy almost immediately.

| Hyperparameter         | Values                                                                 | Notes                                                   |
|------------------------|------------------------------------------------------------------------|---------------------------------------------------------|
| Batch Size             | 256, 512, 1024, 2048, 4096                                             | 1024 is ideal                                           |
| Context                | 0-50                                                                   |                                                         |
| Optimizer              | SGD, Adam, Nesterov Momentum, RMSProp, AdamW                           | AdamW > Adam > SGD                                      |
| LR Scheduler           | StepLR, ReduceLROnPlateau, Exponential, CosineAnnealing                | CosineAnnealing                                         |
| Batch Norm             | Before or After Activation, Every layer or Alternate Layer or No Layer | Before activation every alternate layer (not in output) |
| Number of Layers       | 2-8                                                                    | 6-7 was enough with cylindrical architecture            |
| Dropout                | 0-0.5, Dropout in alternate layers                                     | Only in hidden (0.2 to 0.5); Every/Alternate layers     |
| Architecture           | Cylinder, Pyramid, Diamond                                             | Cylinder > Diamond > Pyramid >                          |
| Regularization         | Weight Decay (L1, L2, L1+L2)                                           | If overfitting                                          |
| Weight Initialisations |                                                                        |                                                         |
| Data Augmentation      | Time masking, freq masking                                             |

The above table is the group table that we were maintaining for the experiments.
Unfortunately, I didn't manage wandb logs and my personal experiments properly, as I didn't realize that we would require this for submission, early on. I'm fixing it on HW2.
This is my wandb logs, https://wandb.ai/suriyag/hw1p2/overview?workspace=user-sayyampe.
although this misses almost all the experiments I did, after fixing the dataloader bug.

the model.model file in this folder is the best model I could achieve with the above hyperparameters.

Almost all the experiments were split between Kaggle and colab.
This notebook is my highest achieving notebook with 80%.
And, this should run out of the box when run on kaggle.