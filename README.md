# Hospitals-Access-Peru
This is a project to evaluate accesability to operational public hospitals in every district of Peru.

## Outputs

In this repository, we will deploy a dashboard where we will see the following outputs:

a. Data description (extracted from the peruvian's government database platform https://datosabiertos.gob.pe/dataset/minsa-ipress)

b. Static Maps (elaborated using Geopandas)

c. Dynamic Maps (elaborated using Folium)

## Code

In the folder "Code" you will find the code used to obtain the aforementioned outputs. This folder is comprised with the following files:

### 1. Geopandas

Using Geopandas, we made an analysis about the number of hospitals per district and elaborate static maps so we can identify those with more and less hospitals available.

### 2. Folium

Using Folium, we made dynamic maps that focus on the distribution of hospitals in relation to every peruvian settlement (with this, we will evaluate how isolated or concentrated are public hospitals) specifically for the peruvian regions of Lima and Loreto.

### 3. Streamlit

Using the Streamlit application, this file shows the code for the deployment of the dashboard that has the outputs we elaborated.
