# Rock, Paper, Scissors Detection using YOLO

This project implements a Rock, Paper, Scissors detection system using the YOLO (You Only Look Once) real-time object detection system. The model is trained using a windows PC with RTX 3080 Ti

## Getting Started

- **NOTE: This project was tested on a windows 11 PC with RTX 3080Ti running CUDA=11.8 and python=3.8.0**
- These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installations

- To run this project, you'll need to have Python and Conda installed on your local machine. You can download Python [here](https://www.python.org/downloads/) and Conda [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

### Run

1. Clone the repository
    ```
    git clone https://github.com/A-Alviento/rock-paper-scissors-yolo-object-detection.git
    ```

2. Navigate into the cloned repository directory
    ```
    cd rock-paper-scissors-yolo-object-detection
    ```

3. Using a Conda environment is recommended to keep dependencies required by different projects separate. You can create a Conda environment using the following command:
    ```
    conda create --name myenv
    ```
    And activate the Conda environment:
    ```
    conda activate myenv
    ```

4. Open `train-model.ipynb` and follow the installation and subsequent instructions


## Acknowledgements

* The dataset used for this project can be found [here](https://universe.roboflow.com/roboflow-58fyf/rock-paper-scissors-sxsw/dataset/11).
