# Unstable Product Detection

## Problem Description
In our research center, we stock around 6 tons of chemicals, divided into approximately **40,000 compounds**. One major issue we could face with chemicals is the stability of certain compounds.

Many chemicals tend to degrade over time, even under clean storage conditions. Our HSE (Health, Safety, and Environment) department has recorded numerous incidents over the past few years related to the degradation of chemicals, which has led to contamination and over-pressurized containers.

To prevent any accidents arising from this issue, we analyzed the nature of the compounds that tend to cause problems and implemented a Python script to detect them by analyzing data extracted from our database.

## Implementation
This short Python script works by identifying and filtering out key words to detect specific types of reagents, unwanted physical states, and by tracking certain reagents that we monitor regularly. The script uses the following columns from our database:
  * 'Product Name'
  * 'Refrigeration'
  * 'Storage Class'
  * 'CAS Number'
