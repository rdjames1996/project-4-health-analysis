# project-4-health-analysis

## Project 4 group members
Ana Gonzalez, Robert James, Cristian M. Jung, Kelly Stave, and Stephanie Tran

## INTRODUCTION

For Project 4, our group will be exploring diabetes in adults 18 and older within the US.

* According to the Diabetes Research Institute, 37.3 million people, or 11.3% of the U.S. population, have diabetes. An estimated 28.7 million people – or 28.5% of the population – had diagnosed diabetes. Approximately 8.5 million people have diabetes but have not yet been diagnosed (2022). (diabetesresearch.org)

* During 2014-2015, the estimated annual number of newly diagnosed cases of type 1 diabetes in the U.S. included 18,291 children and adolescents younger than age 20. Compared to adults aged 18 to 44 years, incidence rates of diagnosed diabetes were higher among adults aged 45 to 64 years and those aged 65 years and older. (diabetesreasearch.org).

* Group 4 will explore the relationships between those with type diabetes, pre-diabetes, and those without diabetes utilizing 253,680 survey responses from cleaned BRFSS 2015 + balanced dataset. Survey comes from CDC and were collected monthly in all 50 states, Puerto Rico, the U.S. Virgin Islands, and Guam.

## METHODS

* DATA:
	* There are different versions of the same dataset
		* diabetes_012_health_indicators_BRFSS2015.csv
			* Diabetes Indicators are seperated into: No diabetes, Pre-Diabetes, Diabetes
		* diabetes_binary_health_indicators_BRFSS2015.csv
			* Diabetes Indicators are seperated into: No diabetes, Diabetes
		* diabetes_binary_5050split_health_indicators_BRFSS2015.csv
			* Diabetes Indicators are seperated into: No diabetes, Diabetes
			* Selected Data in order to have a 50/50 split of No diabetes, Diabetes
	* For this is a Risk Predictor, we used the lumped Pre-Diabetes and Diabetes Dataset. After a couple trials with the regular Dataset, we learned 		the 50/50 split Dataset will serve us better in creating a more efficient model.
	* The data is from the BRFSS survey conducted in 2015.
	
	* For preliminary analysis, we plotted visualizations for each variable within the dataset vs. diabetes risk indicator utilizing Tableau.
		* The following is just one of 21 Visualization plotted on Tableau.

![BMI Vs. Diabetes Indicator](/Cristian/Diabetes_Patient_Count_per_Variable_Ver2/BMI_Vs_Diabetes_Indicator.png)

	* We dropped columns that we found to be too subjective to the important data.
		* Those columns are:
			* GENHLTH: Subjective because it asked the participant to rate how their general health was on a scale of 1-5. Not scientific
			* MENTHLTH: Subjective because it asked for participant’s opinion of their mental health. Not scientific.
			* PHYSHLTH: Same as above. Not scientific.
			* DiffWalk: difficulty walking or climbing stairs. We decided this feature could possibly skew our modeling too much.
			* CHOLCheck: Has a participant received a cholesterol check in the last 5 years? Same as above
		
* Machine Learning Modeling:
	* Initial Testing for all models:
		* We first decided to break up the dataset into 4 major categories:
			* Consumption: Veggies, Heavy Alcohol Consumption, Smoker, Fruits
			* Demographic: Age, Income, Education, Sex
			* General health: BMI, Physical Activity
			* Pre-existing conditions: HighBP, Heart Disease History or Attack, HighChol, Stroke
	* KMEANS:
		* StandardScaler, PCA, LogisticRegression Model, Desicion Tree Model, Deep Learning ML Model
		* RESULTS of each major categories:
			
			-Consumption:
				-StandardScaler, PCA, Desicion Tree Model
					-Accuracy Score 56.9%
				-StandardScaler, PCA, Deep Learning ML Model
					-Accuracy Score 56.3%
			
			-Demographic:
				-LogisticRegression Model
					-Accuracy Score 64.2%
			
			-General health:
				-StandardScaler, LogisticRegression Model
					-Accuracy Score 64.5%
			
			-Pre-existing conditions:
				-LogisticRegression Model
					-Accuracy Score 69.3%
	
	* XGBOOST:
		* XGBOOST XGBClassifier Modeling	
		* RESULTS of each major categories:
			
			-Consumption:
				-Accuracy Score 58.3%
				-Veggies F-Score: 101
				-HvyAlcoholConsumption F-Score: 83
				-Smoker F-Score: 81
				-Fruits F-Score: 66
			
			-Demographic:
				-Accuracy Score 70.8%
				-Age F-Score: 361
				-Income F-Score: 259
				-Education F-Score: 173
				-Sex F-Score: 110
			
			-General health:
				-Accuracy Score 69.8%
				-BMI F-Score: 717
				-PhysActivity: F-Score 47
			
			-Pre-existing conditions:
				-Accuracy Score 74.8%
				-HighBP F-Score: 53
				-HeartDiseaseorAttack F-Score: 45
				-HighChol F-Score: 41
				-Stroke F-Score: 30
			
			-We combined the top feature from each of the four categories:
				-Accuracy Score 78.1%
				-BMI F-Score: 415
				-Age F-Score: 372
				-HighBP F-Score: 110
				-Veggies F-Score: 57
		
		* FINAL RESULT (with all features minus subjective columns):
			-Accuracy Score 81.1%
			-Feature Importance:

## RESULTS
* XGBOOST Modeling, with all features minus subjective columns, gave an Accuracy score of entire Binary Dataset: 81.1%

* Webpage:
	* We created a webpage with Dashboard including Diabetes Risk Predictor.
		* Pages:
			* Home: Introduction with Categorized Features Result and Overall.
			* Data: 
			* Predict: Model Function
			* GitHub: Link to our builds and images
	* Visitor takes a quick survey, then we output if one is at risk or not.
	
![ScreenShot1](/Webpage/Screenshot1.png)
![ScreenShot2](/Webpage/Screenshot2.png)
![ScreenShot3](/Webpage/Screenshot3.png)

## CONCLUSION

In conclusion, after many trials, we were able to achieve a diabetes risk predictive model with Accuracy score of 81.1% utilizing XGBOOST. The model was then inputed onto our website to be accessible.

If given more time, we would continue to explore more models for a higher Accuracy Score.

## DATA
https://www.cdc.gov/brfss/annual_data/annual_data.htm

https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf

## RELEVANT RESOURCES
https://www.cdc.gov/pcd/issues/2019/19_0109.htm

https://www.cdc.gov/diabetes/basics/type2.html
