# Rock, Paper, Scissors Detection using YOLO

This project implements a Rock, Paper, Scissors detection system using the YOLO (You Only Look Once) real-time object detection system. The model is trained using a windows PC with RTX 3080 Ti

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you'll need to have Python and Conda installed on your local machine. You can download Python [here](https://www.python.org/downloads/) and Conda [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

### Installation

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

4. Install the required dependencies
    ```
    pip install ultralytics
    ```

    For windows with RTX 3080 ti with CUDA=11.8, install PyTorch with the following command:
    ```
    conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
    ```
    If training using another machine, check which pytorch version you have to install [here](https://pytorch.org/get-started/locally/).

## Training the Model

If you want to train the model, you can run the provided Jupyter notebook file. 

1. Start the Jupyter notebook server:
    ```
    jupyter notebook
    ```

2. Open the provided notebook file and run the cells to train the model.

## Running the Project

To simply use the provided model (trained using RTX 3080 Ti for 100 epochs), you can run the main project script to start detecting Rock, Paper, Scissors gestures via your webcam:
    ```
    python detect_gestures.py
    ```

## Dataset

The dataset used for this project can be found [here](https://universe.roboflow.com/roboflow-58fyf/rock-paper-scissors-sxsw/dataset/11).