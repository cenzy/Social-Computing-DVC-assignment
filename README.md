# Social-Computing-DVC-assignment
Social Computing's lab assignment about DVC, a tool for version control system and reproducibility for Data Science and Machine Learning projects.
The assignment partially reproduces the notebook https://github.com/trekhleb/machine-learning-experiments/blob/master/experiments/digits_recognition_mlp/digits_recognition_mlp.ipynb

## How to reproduce the pipeline
1. Clone the project.
2. Install the dependencies from the file dependencies.txt.
3. For retrieving the dataset and models do `dvc pull`, give the permission to DVC and enter the verification code.
4. Now the dataset and the model are retrieved. Try to change some parameters into params.yaml and do `dvc repro`. 
See the pipeline's dag using `dvc dag` commands. 
Alternately do not download the dataset and the model but do `dvc repro` to execute the original experiment.

## Author
Vincenzo Digeno
