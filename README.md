# DS4A-Team13-Digital-Divide-Project

<img src="https://github.com/mosymns13/DS4A-Team13-Digital-Divide-Project/blob/9eae19a164e73bc9505714473ae66aff7a6286e4/Presentation%20Materials/Team%2013%20DataFolio.png" width="700">


**Status: Complete**

*Follow up projects pending*

## Background

Data Science For All (DS4A) by Correlation One is an intensive fellowship program free for scholars from underepresented populations to learn data science methodologies to use in jobs across industries. Each fellowship includes a capstone project components where people work in teams to address an issue or solve a business problem.

For the Data Science for All (Empowerment Fellowship), in Cohort 3 my group (Team 13) worked on a capstone project hoping to solve issues around the digital divide in the United States.  

In this program, I was the technical lead for my project team providing guidance on analysis strategies and predictive modeling. I managed the project timeline for deliverables and led in the design of the presentation materials. I also gave detailed feedback on deliverables other teammates led.

## Topic

Currently, there are 30 million Americans that lack adequate internet access.

The Bipartisan Infrastructure Deal has pledged $65 billion to invest in broadband infrastructure deployment, including digital proficiency. With the developing COVID-19 infection rates comes even more need to have access to the internet has working and schooling from home becomes a public health neccessity.

Additionally, device availability is a factor in addressing the digital divide. As families are home with children and parents all working and schooling on one device creates other barriers.

## Goals & Questions
- What are the counties and regions in the U.S. with the highest need for internet and technology?
- What are the significant factors that led to internet and technology access issues?

## Method & Tools

- **Language**: Python, R
- **Data Processing**: Python (Pandas & Numpy)
- **Data Visualizations**: Python (Seaborn & Ploty), R (ggplot2)
- **Documentation**: Juypter Notebook, RMarkdown
- **Other Tools**: Tableau, RStudio


## Deliverables
- [Datafolio](https://github.com/mosymns13/DS4A-Team13-Digital-Divide-Project/blob/9eae19a164e73bc9505714473ae66aff7a6286e4/Presentation%20Materials/Team%2013%20DataFolio.png)
- [Slide Deck Presentation](https://github.com/mosymns13/DS4A-Team13-Digital-Divide-Project/blob/9eae19a164e73bc9505714473ae66aff7a6286e4/Presentation%20Materials/Final%20Team%2013%20DS4A%20Project%20Presentation.pdf)
- [Dashboard in Tableau](https://public.tableau.com/app/profile/geri.harding/viz/DS4AClosingtheDigitalDivide/Dashboard2)
- [Report](https://github.com/mosymns13/DS4A-Team13-Digital-Divide-Project/blob/4b6fd8965fdb54034e9c40a4cce432bad2934326/Presentation%20Materials/Team13_Report_Digital_Divide.pdf)

## Other Information

### Folder Organization
Here is a list of folders and what is in them

- **!Archive** : All old notebooks from our past submissions are stored. We can later delete files no longer needed.
- **EDA Notebooks** : All old notebooks dedicated to intial EDA of individual datasets are stored.
- **Initial Clean Data**: CSV files produced by the `cleaning_all_datasets.py` script (Note: Except the `internet_price_data.csv` is from a different script)
- **Raw Data** : All initial downloaded datasets that have been untouched from the source
- **Cleaning Data Scripts** : Python scripts used to create the inital clean datasets
- **Presentation Materials** : Final documents and other notebooks for the presentations materials (i.e., slidedeck, datafolio, and report)


### Active files
Here are a list of imporant files that are in the order of our process flow

- `requirements.txt` holds all the packages that are needed so far. You can add more packages as time goes on and re-run in your terminal as needed
- `cleaning_all_datasets.py` is the python script with the condensed code from all the individual notebooks from cleaning is saved. This is so that only need to run the script and not multiple notebooks.
- `Key Variables Selection.ipynb` is the notebook that takes all that are chosen for initial analysis work.
- `initial_analytic_dataset.csv` is the file that holds the varibles chosen from the "Key Variables Seclection" notebook 
- `Analytic Dataset.ipynb` is the notebook where we explore the data and choose the variables we wanted to focus on 
- `revised_analytic_dataset.csv` is the file that holds all the data with the additional scoring information for certain key columns produced from the "Analytic Dataset" notebook
- `Exploration and Modeling.ipynb` is the notebook where we work through different models for our internet and device outcomes

