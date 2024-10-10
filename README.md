[![Build and Test](https://github.com/devplaybooks/.baseline/actions/workflows/CI.yml/badge.svg)](https://github.com/devplaybooks/.baseline/actions/workflows/CI.yml)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE-GPLv3)

# Ganttenzell

# WIP

![ganttenzell.jpg](docs/ganttenzell.jpg)

    1. Measure activities by the amount of time needed to complete them;
    2. The space on the chart can be used to represent the amount of the activity that should have been done in that time.
    
[Henry Gantt](https://en.wikipedia.org/wiki/Henry_Gantt) - [Organizing for Work](https://archive.org/details/organizingforwor00gant), 1919

## Setup

Setup scripts are avaialable in the `bin` directory. `bin/dosetup` does the
following:

* checks that asdf is installed 
* installs the python version specified in the .tool-versions file
* creates a virtual environment
* activates that virtual environment
* installs the depenedcies in the `requirements.txt` file

`bin/doact` activates that virtual environment.

`bin/dofreeze` updates the `requirements.txt` file with the current dependencies.

## Dependencies

* [Plotly](https://plotly.com/python/)

## Information

* [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
