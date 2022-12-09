# Network Structure of the Digital Advertising Marketplace
By Subramanian, V., Chun-Yen, P., Stukalin, S., Sharp, M., Zhang, X.

This repository contains code for the aforementioned project. This project was done to meet the course requirements of the [EPPS 6302](https://catalog.utdallas.edu/2021/graduate/courses/epps6302) class.

## Instructions on how to use this repo
We recommend reading the report if you couldn't attend our inclass presentation to get a grip on the ideas that drove this project. 

If you are interested in replicating the Neo4j database we explained in our report, upload the [`admapper.dump`](https://drive.google.com/file/d/1JpYsUGDlpQP3Dvq--1P46Km03weGfIxF/view?usp=share_link) available here into a Neo4j database locally (or AuraDB instance on the cloud). One can also build the Neo4j database from scratch, by replicating the data model shown in the report using the `.csv` files provided in the `neo4j_files` directory.

To understand this code base, please read the jupyter notebooks (`.ipynb` files) in this order - `00_data_cleaning.ipynb`, `01_create_adjacency_list.ipynb` and `02_analysis.ipynb`. We have added useful comments within the notebooks to ease the reading process. The point of the `.py` files in the codebase will become clear as one reads the notebook files.

We are happy to hear any comments or concerns on this repo! Please DM [Venkatesh](https://www.linkedin.com/in/venkateshutd/) on LinkedIn.
