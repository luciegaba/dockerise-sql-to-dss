# dockerise-sql-to-dss

## Table of Contents

* [About the Project](#about_the_project)
* [Contact](#contact)

<br>

## About the Project 🐳

The following project is realized as part of the Linux course given by the MoSEF Master at the University of Paris 1 Panthéon-Sorbonne. The main goal is to deploy an app with Docker or with a simple shell file. 
This was very challenging and really cool to realize!



In this project, we aim to connect a simple MySQL Database (extracted data from Spotify API) to DSS (Dataiku Data Science Studio :https://doc.dataiku.com/dss/latest/)
In this repository, you will find the following elements:
* A Docker-compose.yml which orchestrates the containers.
* Some Docker Images each folder corresponds to an Image to build (with Python)):
    * data_request_app: requesting Spotify API with Python and push it to mySQL Database
    * dss : composing image for Dataiku + downloading required connector for MySQL
 
 ## Contact

* [Lucie Gabagnou👸](https://github.com/luciegaba) - Lucie.Gabagnou@etu.univ-paris1.fr


