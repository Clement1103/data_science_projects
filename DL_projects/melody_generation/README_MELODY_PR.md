
This file explains how to run the notebook in which is implemented the project. The presentation of the project is included in the notebook. 

Instead of running the notebook and installing all the dependancies, you can visualize it as a pdf file (melody_generation.pdf).

## Environment 
This code runs thanks to a conda virtual environment that you can install by following these steps in a shell :
- Create a virtual environment :
 ```sh
conda create -n melody_generation python=3.9 # We use an old version of Python in order to make sure that Tensorflow is compatible.
```
- Activate the environment :
 ```sh
conda activate melody_generation 
```
- Install the librairies :
 ```sh
pip install -r requirements.txt
```
If you encounter any issue installing the environment, you could install the three different librairies individually :
 ```sh
conda install -c conda-forge music21
conda install -c conda-forge opencv
conda install -c conda-forge tensorflow
```
Finally, if you do not have it yet, you have to install Jupyter in order to open the notebook :
 ```sh
conda install jupyter
```

Thus, you should be able to run the notebook : 
 ```sh
jupyter notebook
```
## MuseScore

To take advantage of the Notebook and view results correctly, especially music scores, you need to use a dependency. Personally, I've used MuseScore, whose installation depends on your operating system.
The tool is not necessary to understand my work, especially because results can be visualized in the pdf notebook.

However, if you still want to download it, you can do it on the official website (https://musescore.org/fr).
- On Linux:
Move the .AppImage folder to the current directory, make it executable and then run it using the following commands:
 ```sh
chmod +x MuseScore-*.AppImage
./MuseScore-*.AppImage
```
- On Windows:
Run the downloaded .exe file and follow the installation instructions.
- On Mac:
Open the .dmg file and drag the MuseScore icon into the Applications folder.

Finally, you have to modify the configuration of the *.music21rc* file (often located at /Users/<your_user_name>/), and add the following line to it :
 ```sh
musescoreDirectPNGPath = <path_to_your_muse_score_executor>
```
You have to replace the "<path_to_your_muse_score_executor>" by the actual path of your executor.


If you encounter any issue or have any bad explanation to report, do not hesitate to contact me.
