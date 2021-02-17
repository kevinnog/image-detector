<h1 align="center">
    <img alt="ImageDetector" title="#ImageDetector" src="git/TOBIAS9000.png" width="250px" />
</h1>

<h4 align="center"> 
	Image Detector
</h4>

<p align="center">
  <a href="#-project">Image Detector</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rocket-Technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-how-to-use">How to use</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-how-to-contribute">How to contribute</a>
</p>

## 💻 Project

Simple AI examples to detect diferent objects.
The smile detector and the self driving app were created using OpenCV and haarcascade files to train the detector.
The image classifier was created using tensorflow to train a neural network.

## :rocket: Technologies

This project was developed with the following technologies:

- [Tensorflow][tensorflow]
- [OpenCV][opencv]
- [Numpy][numpy]

## :information_source: How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Python][python] + [Yarn][yarn] + [Pip][pip] installed on your computer.
After that, you need to download any video that has cars or pedestrians and save at the root with the name 'video.mp4'.

From your command line:

### Install API

```bash
# Clone this repository
$ git clone git@github.com:brain-ag/image-detector.git

# Go into the repository
$ cd image-detector

# Create the virtual env folder
$ mkdir venv_dir

# Create the virtual env files
$ virtualenv venv_dir

# Activate virtual env
$ source venv_dir/bin/activate

# Install packages
$ python -m pip install -r requirements.txt

# Start the AI
$ python self-driving.py

```

## 🤔 How to contribute

- Make a fork;
- Create a branch with your feature: `git checkout -b my-feature`;
- Commit changes: `git commit -m 'feat: My new feature'`;
- Make a push to your branch: `git push origin my-feature`.

[python]: https://www.python.org/
[yarn]: https://yarnpkg.com/
[pip]: https://pypi.org/project/pip/
[opencv]: https://opencv.org/
[tensorflow]: https://www.tensorflow.org/
[numpy]: https://numpy.org/
