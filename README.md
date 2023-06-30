# FANNet+
Optimized SMT-based model checking for trained DNN analysis

This repository provides implementation of FANNet+, an optimized model checking-based DNN analysis framework, for the verification of robustness and safety properties of the trained neural networks. The verification results can be further used to to analyze noise tolerance, robustness bias and input node sensitivity of the networks. The following (fully-connected) networks are considered in the repository:

| Dataset | Model | No. of Network Parameters | Activation |
| :---        |    :----:   |      :----:       | ---:|
| [Leukemia](https://hastie.su.domains/CASI_files/DATA/leukemia.html)      | 5x20x2   | 160 | ReLU|
| [Heart Disease](https://archive.ics.uci.edu/dataset/45/heart+disease)  | 13x20x10x10x2   | 622 | ReLU|
| [ACAS Xu](https://github.com/guykatzz/ReluplexCav2017/tree/60b482eec832c891cb59c0966c9821e40051c082/nnet) | 5x50x50x50x50x50x50x5   | 13,305   | ReLU |

## Requirements
The following requirements correspond to CentOS Linux release 7.9.2009
- Python (tested with verison 3.6.12)
- g++ (tested with version 4.8.5)
- nuXmv (tested with version 1.1.1)
  
(*Note that: the nuXvm executable must be available to \*/basis/ and named nuXmv_linux64*)

## Usage
For analysis of DNNs trained on Leukemia or heart disease dataset, execute:
```
chmod +x FANNetPlus.sh 
./FANNetPlus.sh
```
***Result:*** 
The results, i.e., the misclassifying noise vectors (if exist), will be contained in `./Noise.csv`


For analysis of ACAS_Xu DNNs, execute:
```
chmod +x FANNetPlus_*.sh 
./FANNetPlus_*.sh
```
(*\*: coarse or ris, for coarse-grain or random input segmentation based safety analysis, respectively*)

***Result:*** 
The results, including execution timings, will be summarized in text files in the directory `./Logs/`


Sample results from the experiments provided in `./Sample_results`

## Citing the Work
Please refer to or cite the following publication:
M. Naseer, O. Hasan, M. Shafique, “Scaling Model Checking for DNN Analysis via State-Space Reduction and Input Segmentation”, FoMLAS 2023.

For details, refer to:
M. Naseer, O. Hasan, M. Shafique, “Scaling Model Checking for DNN Analysis via State-Space Reduction and Input Segmentation (Extended Version)”, arXiv 2023.

## License:
[MIT License](https://opensource.org/licenses/MIT)
