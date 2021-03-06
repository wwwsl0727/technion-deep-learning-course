# -*- coding: utf-8 -*-
import os
import re
import sys
import glob
import numpy as np
import unittest
import torch
import torchvision
import torchvision.transforms as tvtf
import hw2.experiments as experiments
import hw2.models as models


seed = 42
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

torch.manual_seed(seed)
data_dir = os.path.join(os.getenv('HOME'), '.pytorch-datasets')
ds_train = torchvision.datasets.CIFAR10(root=data_dir, download=True, train=True, transform=tvtf.ToTensor())
ds_test = torchvision.datasets.CIFAR10(root=data_dir, download=True, train=False, transform=tvtf.ToTensor())

print(f'Train: {len(ds_train)} samples')
print(f'Test: {len(ds_test)} samples')

x0,_ = ds_train[0]
in_size = x0.shape
num_classes = 10
print('input image size =', in_size)

params = [
    {
        'filename': 'exp1_1_K32_L2',
        'K': [32],
        'L': 2
    },
    {
        'filename': 'exp1_1_K32_L4',
        'K': [32],
        'L': 4
    },
    {
	'filename': 'exp1_1_K32_L8',
	'K': [32],
        'L': 8
    },
    {
        'filename': 'exp1_1_K32_L16',
        'K': [32],
        'L': 16
    },
    {
        'filename': 'exp1_1_K64_L2',
        'K': [64],
        'L': 2
    },
    {
        'filename': 'exp1_1_K64_L4',
        'K': [64],
        'L': 4
    },
    {
        'filename': 'exp1_1_K64_L8',
        'K': [64],
        'L': 8
    },
    {
        'filename': 'exp1_1_K64_L16',
        'K': [64],
        'L': 16
    },

]

for p in params:
    print(p)
    experiments.run_experiment(p['filename'],
                               seed=seed,
                               epochs=10,
                               early_stopping=5,
                               filters_per_layer=[p['K']],
                               layers_per_block=p['L'])
