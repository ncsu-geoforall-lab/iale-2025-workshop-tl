# Building Geospatial Models in GRASS: From Python Workflows to Tangible Landscape
This is a repository for materials and Tangible Landscape activities for IALE-NA 2025 workshop.


## Overview
In this workshop, participants will be introduced to GRASS, a powerful open-source geospatial processing engine, and explore how it can be used to develop models for environmental applications. Participants will learn to build Python-based workflows for topics such as hydrology, flood modeling, and trajectory routing. These workflows will be implemented in computational notebooks, highlighting the capabilities of GRASS GIS for flexible and scalable analysis.

In the second half of the workshop, we will deploy these models into [Tangible Landscape](https://tangible-landscape.github.io/), an interactive, augmented reality environment that facilitates participatory science by integrating a physical landscape with real-time geospatial simulations. The Tangible Landscape environment allows users to interact with, for example, an overland flow model by carving sand with their hands and viewing the resulting water flow projected back onto the sand. Participants will gain hands-on experience with GRASS tools and its Python API while learning essential GitHub workflows for collaborative development. This workshop is ideal for those interested in applying geospatial tools to real-world environmental challenges or in fostering community engagement through participatory science.


Presenter(s): [Caitlin Haedrich](https://chaedri.github.io/), 
[Anna Petrasova](https://cnr.ncsu.edu/geospatial/people/anna-petrasova/), and 
[Helena Mitasova](https://cnr.ncsu.edu/geospatial/people/helena-mitasova/), North Carolina State University, Center for Geospatial Analytics.

## Workshop Outline

### 1. Building Geospatial Models in GRASS
#### 1.1 GRASS + Jupyter introduction
1. What is [GRASS](https://grass.osgeo.org/)? Learn about various [ways to interact with GRASS](https://grass.osgeo.org/grass-devel/manuals/interfaces_overview.html).
2. To learn how to get started with GRASS in Google Colab, go to the [Learn GRASS](https://grass-tutorials.osgeo.org/) website and open the [Get started with GRASS in Google Colab](https://grass-tutorials.osgeo.org/).
3. To learn how to visualize data in a notebook, go to [GRASS Jupyter introduction](https://grass.osgeo.org/grass-devel/manuals/jupyter_intro.html)  in documentation.
3. To learn how to run GRASS tools in a notebook, go to [GRASS Python API  documentation](https://grass.osgeo.org/grass-devel/manuals/python_intro.html).


#### 1.2 Hands-on exercise

1. Open the workshop.ipynb in Google Colab and execute the cells one by one:
[![Open_in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ncsu-geoforall-lab/iale-2025-workshop-tl/blob/main/workshop.ipynb)

Aletrnatively, try running the notebook through mybinder.org:  
 [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ncsu-geoforall-lab/iale-2025-workshop-tl/main?urlpath=%2Fdoc%2Ftree%2Fbinder_workshop.ipynb)

#### 1.3 Developing your own models

In this part, you will develop simple geospatial models that will be run on Tangible Landscape in the second part of the workshop.

Use the suggested tasks, together with [GRASS documentation](https://grass.osgeo.org/grass-devel/manuals/index.html) and provided template in the notebook
to (1) develop the models, (2) test them, and (3) visualize the results.
This model will then run on Tangible Landscape. 

_[15 min break]_

### 2. Tangible Landscape

#### 2.1 Tangible Landscape demo

We will show different applications of Tangible Landscape and explain how to develop an interactive model in Tangible Landscape.

#### 2.2 GitHub Introduction and Contributing a model through GitHub

In this part, we will explain why it's useful to understand GitHub contributing workflow and how Git and GitHub works. Then, we will fork this repository and make a pull request containing the script we developed in 1.3.

#### 2.3 Running contributed models in Tangible Landscape

We will plug in the participant contributed models in Tangible Landscape and see how they work with different parameters and modified elevation inputs.






## License

This material is dual licensed under GNU FDL 1.3 and CC BY-SA 4.0.

## Acknowledgement
This workshop was developed and delivered with the support of the U.S. National Science Foundation, award [2303651](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2303651) and was hosted by the [Center for Geospatial Analytics](https://cnr.ncsu.edu/geospatial/) at North Carolina State University.

<img src="NSF_logo.png" title="NSF" width=150>
