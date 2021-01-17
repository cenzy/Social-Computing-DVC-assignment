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
5. See the result metrics doing `dvc metrics show`

## How to compare experiments
1. Change the parameters into params.yaml and do `dvc repro` to execute again the experiment.
2. Do `dvc metrics diff` to show the differences in loss and accuracy between previous experiment and the new experiment.
3. If you want to see the plots about loss and accuracy values for each epoch (an history generated during the training phase) do `dvc plots show acc.json` for the accuracy plot and `dvc plots show loss.json` for the loss plot.

## Author
Vincenzo Digeno
