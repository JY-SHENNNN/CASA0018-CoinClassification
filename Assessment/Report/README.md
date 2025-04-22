# Uk coin classification
Jiaying Shen
Github link: 
Edge impulse link:

## Introduction
This project aims to develop Egde Impulse and transfer learning based UK coin classification system, which ables to classify 5 catrgories coin (1 penty, 5 pence, 10 pence, 20 pence, 50 pence) with over 80% accuracy. Initial idea comes from the scenario that UK coin always choas in daily life, it's hard to quickly tell them apart especially when checking out. 

Traditional vending machines identify coins based on their size (Segrave, 2015). However, many coins have similar sizes but different values, which leads to recognition errors. This problem becomes worse when coins are worn out or stacked together. By contrast, manual sorting is a way to solve but time-consuming. In that case, an efficient classification system needed. 

Previous studies have shown that convolutional neural networks (CNNs) can perform better than the human eye in recognizing coins (Xiang and Yan, 2021). Building on this, Jahan et al. (2023) proposed a deep learning model using MobileNetV2 for global coin detection, which is a compact and efficient neural network based on depth-wise separable convolutions, achieving an accuracy of 84.24%.

- an overview of what the project does
- your inspiration for making the project 
- examples that it is based on. 

*Tip: probably ~200 words and images are good!*

## Research Question
Is it able to develop a system that run on mobile phone to quick classify the UK coin?

## Application Overview
The project follows a modular pipeline shows in the graph. In the data collection stage, I sourced data from both oline open-source(Sourikta, 2024) and self-collected data to ensure a diverse and representative dataset. During the preprocessing stage, Python scripts were developed to filter the useful data and group the data into labeled classes for better uploading to Edge impulse for model training. 

The training phase involves building a MobileNetV2-based image classification network with an input resolution of 96x96 grayscale on 196 number of samples across 5 classed. Various techniques were applied to enhance performance, like data augmentation, dropout regularization and early stopping.

Once the tained model experierenced testing, which have the similar behaviour as the validation step, the model was converted into default format. For inference deployment, the trained model was hosted via Edge Impulse’s web-based runtime. Users can test the model either by launching it directly in a browser or by scanning a generated QR code using the Edge Impulse mobile application. This approach enables real-time image classification through a phone camera, showcasing the model’s predictions instantly and interactively. 


Thinking back to the various application diagrams you have seen through the module - how would you describe an overview of the building blocks of your project - how do they connect, what do the component parts include.

*Tip: probably ~200 words and a diagram is usually good to convey your design!*

## Data
The data combines both online open-source datasets and self-collected image data to ensure comprehensive coverage. The open-source images were primarily from (Sourikta, 2024), which provided a diverse collection of coins from various countries. However, these image come from the single background, the self-collected images are needed. Initially, OV7675 camera module was used to collect the, due to resolution limitations in capturing fine cointextures, mobile phone is instead. 

Before model training, all raw data underwent preprocessing steps. The downloaded datasets applied Python script to filter filenames that contained label "united_kingdom". Then organized the remaining valid samples into denomination-specific directories (1p, 2p, etc.). The similar process applied for the self-collected data, with both datasets being automatically divided into training (80%) and tesing (20%). This step was designed to be recursive, allowing for seamless integration of new data to continuously improve model performance. Images were further processed after uploading, which resized to 96 x 96 pixels, converted to grayscale, and augmented during training to improve generalization. 


Describe what data sources you have used and any cleaning, wrangling or organising you have done. Including some examples of the data helps others understand what you have been working with.

*Tip: probably ~200 words and images of what the data 'looks like' are good!*

## Model
Initially, the model experimented with a simple classification model, achieving only 40.6% accuracy. When the number of training epoch increases, the accuracy improved to 65.6%. Adding one more dense layer led to a slight improvement(69.4%), but the results were still not ideal. This led to the adoption of transfer learning approaches, specifically MobileNet architectures. Among the tested variants, MobileNetV2 consistently outperformed MobileNetV1 across different configurations. The optimal model was MobileNetV2 (96x96 input, 0.35 width multiplier), which balanced performance and resource efficiency. The accuracy achieved 72.7% with 0.49 loss while utilizing approximately 296.8k RAM and 575.2 ROM.

In addition, this configuration supported both RGB and grayscale inputs. Larger models with a 160x160 input size only supported RGB images, which limited their flexibility. Comparative analysis showed that reducing the width multiplier (e.g., to 0.1 or 0.05) significantly decreased accuracy to 63.6% and 57.6% respectively. 

The selection of MobileNetV2 was further justified by its ability to maintain reasonable accuracy (57.6%) even with aggressive 0.35 width multiplier, while simpler models like MobileNetV1 failed to exceed 57.6% accuracy regardless of parameter adjustments. The structure of MobileNetV2, especially its use of inverted residual blocks and linear bottlenecks, helped it extract features more effectively. This is likely why it performed better on the coin classification task than both the basic classification model and MobileNetV1.


This is a Deep Learning project! What model architecture did you use? Did you try different ones? Why did you choose the ones you did?

*Tip: probably ~200 words and a diagram is usually good to describe your model!*

## Experiments
During the model optimization process, various parameters were adjusted to achieve the best performance for MobileNetV2 (96x96, 0.35). Experimental results showed that using 64 neurons led to significantly faster training than 128 neurons, while maintaining the same accuracy of 81.8%. Based on early tests, the number of epochs was fine-tuned starting from 60. Results indicated that 60 epochs were sufficient, as more epochs only slightly reduced the loss but introduced a higher risk of overfitting.

To avoid overfitting, I continuously monitored the difference between training and test accuracy. When the test accuracy dropped significantly compared to training, it suggested the model had memorized the training data, prompting further parameter adjustments. Conversely, when test accuracy exceeded training accuracy, it implied the model might have "cheated" by overfitting to the test set, which led to expand the dataset to improve generalization. The training was stopped when the gap between training and test accuracy became minimal, indicating a well-balanced model.

The dropout rate of 0.3 yielded the best results, improving accuracy by 3%. In transfer learning, freezing 35% of base layers significantly outperformed the 50% freeze ratio, which caused a 3–7% drop in accuracy. The patience setting for early stopping was also crucial. A patience value of 8 achieved the best balance with 85% accuracy, while smaller values like 3–5 limited performance to 78.8%. Altogether, the configuration of 64 neurons, 0.3 dropout rate, 35% freeze ratio, and patience of 8 offered the best balance of accuracy and efficiency.

Specifically, dropout, layer freezing, and callback settings were fine-tuned to improve training control and performance monitoring. A ModelCheckpoint callback was implemented to save the best-performing model based on validation accuracy. Additionally, the script adopted a modular and well-organized callback structure, making it easier to manage and test different configurations.

Although Edge Impulse does not support full training accuracy or loss curve visualization, we evaluated model performance using the confusion matrix and data explorer tools. These provided detailed insights into misclassifications and class-wise performance, helping verify the model's learning behavior and generalization quality.


What experiments did you run to test your project? What parameters did you change? How did you measure performance? Did you write any scripts to evaluate performance? Did you use any tools to evaluate performance? Do you have graphs of results? 

*Tip: probably ~300 words and graphs and tables are usually good to convey your results!*

## Results and Observations
The coin classificatino model achieved generally good peroformance while exhibiting some specific limitations. The system performed particularly well in recognizing distinctive coin types, with the 50p and 20p coins showing approximately 90% accuraacy in both training and testing phases. This strong performance can be attributed to their unique heptagonal shapes which made them easily distinguishable. The 1p coin also showed relatively good accuracy due to its distinctive copper color and the "1" marking on its reverse side. 5p coins showed 83.3% train accuracy but increased to 85.7% in test accuracy.


However, the model faced significant challenges with 10p coin classification. There is a noticeable accuracy gap between training and test sets, suggesting potential overfitting for 10p. About 20% of 10p coins were misclassified as 5p coins, primarily because both feature similar Queen's head designs on the obverse side and comparable textures on the reverse. Additionally, approximately 10% of 10p coins were confused with 50p coins suspectively due to similarities on size. 

Real-world testing conducted through Edge Impulse's QR code deployment revealed additional limitations. The model's performance varied considerably depending on different backgrounds and coin orientations. I guess it's because the training dataset contains most of image in font.

During testing, several key challenges emerged. One issue was the variation in the Queen’s portrait design, which differed depending on the year the coin was minted. Another difficulty came from the coins’ small size, which made it harder to capture fine texture details in the images. In addition, the reflective nature of the coin material often caused lighting interference during image capture, affecting image consistency and model accuracy.

With additional development time, several improvements could be implemented. Expanding the training dataset to include images taken under different lighting conditions and from multiple angles, which would help to enhance the model’s generalization. Enhancing preprocessing methods to more effectively manage glare and reflections from coin surfaces could improve input quality.
Also, applying temporal analysis to video streams, rather than relying on single-frame inputs, may give better performance while real-world testing.These enhancements would address the current limitations while building upon the model's existing strengths in recognizing distinctive coin features.

Synthesis the main results and observations you made from building the project. Did it work perfectly? Why not? What worked and what didn't? Why? What would you do next if you had more time?  

*Tip: probably ~300 words and remember images and diagrams bring results to life!*

## Bibliography
*If you added any references then add them in here using this format:*

1. Jahan, Z., Nazia Parween, Agrawal, A.P., Choudhary, A., Raj, G. and Aziz Deraman (2023). Deep Learning Based World Coin Currency Detection. Algorithms for intelligent systems, pp.439–449. doi:https://doi.org/10.1007/978-981-99-1620-7_35.

2. Xiang, Y., Yan, W.Q. Fast‐moving coin recognition using deep learning. Multimed Tools Appl 80, 24111–24120 (2021). https://doi.org/10.1007/s11042-021-10857-5

3. Segrave, K. (2015) Vending machines: an American social history. Jefferson, NC: McFarland.

4. Sourikta (2024). Assignment Dataset. [online] Roboflow. https://universe.roboflow.com/sourikta/assignment-za0qo

*Tip: we use [https://www.citethisforme.com](https://www.citethisforme.com) to make this task even easier.* 

----

## Declaration of Authorship

I, AUTHORS NAME HERE, confirm that the work presented in this assessment is my own. Where information has been derived from other sources, I confirm that this has been indicated in the work.


*Digitally Sign by typing your name here*

ASSESSMENT DATE

Word count: 
