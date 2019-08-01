# Introduction:
There are two kinds of ride-hailing services in the United States. Many consumers are unsure of which service offers the cheaper ride. Many consumers are keen in savings.Therefore, they constantly check both the services before making a final decision on which service to use. Such a time-inducing process wastes a lot of time. There should be a better way of doing things.This is where the model that we are going to build comes to the rescue. The model predicts the price of rides based on the weather patterns and timing information. Hence, reducing the time needed to ascertain the cheaper ride.


# Problem Statement:
Build a model that predicts the price of a commute & suggests the cheaper service between Lyft and Uber.


# Summary and conclusion: 
After evaluating all the four models based on 3 vital metrics, we drew a conclusion. The Random Forest Regression was considered to be the optimal models for both they Lyft and Uber dataset. 

The first metric that was used was R2. The Random Forest Regressor Model offers the highest R2 and the lowest difference between the train and test r2 scores. The difference in the train and test score is important indicator to show whether the model is overfitting. Hence, with a small difference between the train and test r2 scores we can infer that our model is not an overfitting one. 

Further, The Root Mean Square Error (RMSE) was used as the second metric for choosing the right model. RMSE involves the calculation of the distance between the target and the model predicted target values. Hence, a small RMSE would be ideal. The Random Forest Regressors also gave us small RMSE values as compared to the other model. 

The final metric that was used to evaluate the models was the residual plot. The residual plots serves as a visual representation of the residuals against the actual target values. The residual is the difference between target and predicted target values. A residual plot that is centered heavily on zero without fluctuating too much would be the best possible situation. We observed that the Random Forest Regressor residual plots was superior than the other models. 

It is good to note that our price model might not be able to predict exact pricing of rides. This is because Lyft and Uber utilizes dynamic algorithms to set the price of journeys. To add on, Uber and Lyft pricing algorithms are constantly tweaked. Therefore, our model is based on their pricing model that was used between November through December. They might have changed their features or the importance of certain features. Moreover, we are unaware of the other pertinent features that might be in their price model. For instance, the supply of the vehicles in the vicinity is vital to determine the price. However, we are unable to ascertain such confidential information. Hence, the model we built might not be able predict exact prices as we do not have all the features that were used in their own model to quote a price. Nonetheless, the model serves as a good platform to compare the prices before moving ahead to choose the right journey for you. 
