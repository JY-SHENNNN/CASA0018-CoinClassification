# Uk coin classification
Jiaying Shen

Github link: https://github.com/JY-SHENNNN/CASA0018-CoinClassification

Edge impulse link: https://studio.edgeimpulse.com/studio/652263

---
## Introduction
<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/overview.png" width="800">
  <p><strong>Fig. 1.</strong> Example images of UK coins</p>
</div>

This project aims to develop Egde Impulse and transfer learning based UK coin classification system, which ables to classify 5 catrgories coin (1 penty, 5 pence, 10 pence, 20 pence, 50 pence) with over 80% accuracy. Initial idea comes from the scenario that UK coin always choas in daily life, which is hard to quickly tell them apart especially when checking out. 

Traditional vending machines identify coins based on their size (Segrave, 2015). However, many coins have similar sizes but different values, which leads to recognition errors. This problem becomes worse when coins are worn out or stacked together. By contrast, manual sorting is a way to solve but time-consuming. In that case, an efficient classification system needed. 

Previous studies have shown that convolutional neural networks (CNNs) can perform better than the human eye in recognizing coins (Xiang and Yan, 2021). Building on this, Jahan et al. (2023) proposed a deep learning model using MobileNetV2 for global coin detection, which is a compact and efficient neural network based on depth-wise separable convolutions, achieving an accuracy of 84.24%.

---
## Research Question
Can a mobile-based system effectively classify UK coins?

---
## Application Overview

<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/buildingblock.png" width = "800">
  <p><strong>Fig. 2.</strong> Full pipeline for coin classification system.</p>
</div>

The project follows a modular pipeline shows in the Fig. 2. In the data collection stage, I sourced data from both oline open-source (Sourikta, 2024) and self-collected data. During the preprocessing stage, Python scripts were developed to filter the useful data and group the data into labeled classes for easier uploading to Edge impulse. 

The training phase involves building a MobileNetV2-based image classification network with an input resolution of 96x96 grayscale on 196 number of samples across 5 classes. Various techniques were applied to enhance performance, like data augmentation, dropout regularization and early stopping.

Once the trained model experierenced testing, which have the similar behaviour as the validation step, the model was converted into default format. The model can be tested either by launching it directly in a browser or by scanning a generated QR code using the Edge Impulse mobile application. This approach enables real-time image classification through a phone camera, showcasing the model’s predictions instantly and interactively. 

---
## Data
<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/open_source_Data.png" width="800">
  <p><strong>Fig. 3.</strong> Open-source data from (Sourikta, 2024).</p>
</div>

<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/labelled_self_data.png" width="800">
  <p><strong>Fig. 4.</strong> Self-collected data with label</p>
</div>

The data combines both online open-source datasets and self-collected image data to ensure comprehensive coverage. The open-source images were primarily sourced from (Sourikta, 2024), which provided a diverse collection of coins from various countries. However, since these images were captured against a uniform background, additional self-collected images were necessary to improve variability and real-world relevance. Initially, an OV7675 camera module was used for image collection, but due to its limited resolution and inability to capture fine coin textures, a mobile phone was later used instead. During this process, efforts were made to capture clear images from multiple angles to enhance dataset diversity and improve model robustness.

Before model training, all raw data underwent preprocessing steps. The downloaded datasets applied Python script to filter filenames that contained label "united_kingdom". Then organized the remaining valid samples into denomination-specific directories (1p, 2p, etc.). The similar process applied for the self-collected data, with both datasets being automatically divided into training (80%) and tesing (20%). This step was designed to be recursive, allowing for seamless integration of new data to continuously improve model performance. Images were further processed after uploading, which resized to 96 x 96 pixels, converted to grayscale, and augmented during training to improve generalization. 

---

## Model

<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/simple_classify_model.png" width="800">
  <p><strong>Fig. 5.</strong> Comparison between classification models.</p>
</div>
<br>

<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/transfer_learning_block.png" width="800">
  <p><strong>Fig. 6.</strong> Comparison between classification models.</p>
</div>
<br>
<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/transfer_learning_model.png"  width="800">
  <p><strong>Fig. 7.</strong> Comparison between MobileNet models.</p>
</div>

Initially, the model experimented with a simple classification model, shown in Fig. 5,  achieving only 40.6% accuracy. When the number of training epoch increases, the accuracy improved to 65.6%. Adding one more dense layer led to a slight improvement (69.4%), but the results were still not ideal. This led to the adoption of transfer learning approaches, which shown in Fig. 6, specifically MobileNet architectures. The process begins with feature extraction, where the base layers are reused to capture visual features like edges, texutres, and shapes. These layers remain frozen during the initial training phase to preserve the learned general patterns. On top of this fundation, custom dense layers are added and trained specifically for the classification task. The structure of MobileNetV2, especially its use of inverted residual blocks and linear bottlenecks, helped it extract features more effectively. Thus, among the tested variants, MobileNetV2 consistently outperformed MobileNetV1 across different configurations. 

In addition, this configuration supported both RGB and grayscale inputs. Larger models with a 160x160 input size only supported RGB images, which limited their flexibility. Comparative analysis showed that reducing the width multiplier (e.g., to 0.1 or 0.05) significantly decreased accuracy to 63.6% and 57.6% respectively. While simpler models like MobileNetV1 failed to exceed 57.6% accuracy regardless of parameter adjustments. The optimal model was MobileNetV2 (96x96 input, 0.35 width multiplier), which balanced performance and resource efficiency. The accuracy achieved 72.7% with 0.49 loss while utilizing approximately 296.8k RAM and 575.2 ROM.

---
## Experiments
<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/trasfer_learning_model_adjust.png" width="800">
  <p><strong>Fig. 8.</strong> Comparison between MobileNetV2 models.</p>
</div>


During the model optimization process, various parameters were adjusted to achieve the best performance for MobileNetV2 (96x96, 0.35). Experimental results are shown in Fig. 7. Using 64 neurons led to significantly faster training than 128 neurons, while maintaining the same accuracy of 81.8%. Results indicated that 60 epochs were sufficient, as more epochs only slightly reduced the loss but introduced a higher risk of overfitting.

Although Edge Impulse does not support full training accuracy curve visualization, I evaluated model performance using the confusion matrix and data explorer tools. These tools provided detailed insights into misclassifications and class-wise performance, which helped verify the model's learning behavior and generalization capability. To further ensure the model did not overfit, I continuously monitored the gap between training and test accuracy throughout the training process. A significant drop in test accuracy compared to training accuracy suggested overfitting, which prompted adjustments to the model parameters. On the other hand, when the test accuracy exceeded the training accuracy, it indicated either the effect of strong regularization or a limited training dataset, leading to the decision to expand the dataset in order to improve generalization. 

Specifically, the parameters were alterned under "expert mode". A ModelCheckpoint callback was implemented to save the best-performing model based on validation accuracy. In addition, the script adopted a modular and well-organized callback structure, making it easier to manage and test different configurations. The dropout rate of 0.3 yielded the best results, improving accuracy by 3%. Freezing 35% of base layers significantly outperformed the 50% freeze ratio, which caused a 3–7% drop in accuracy. The patience setting for early stopping was also crucial. A patience value of 8 achieved the best balance with 85% accuracy. Altogether, the configuration of 64 neurons, 0.3 dropout rate, 35% freeze ratio, and patience of 8 offered the best balance of accuracy and efficiency. Training was stopped when the accuracy gap narrowed to an acceptable range, signaling a well-balanced and robust model.

---
## Results and Observations

<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/feature.png" width="800">
  <p><strong>Fig. 9.</strong> Generated feature based on the 196 training dataset. </p>
</div>

<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/training_model.png" width="800">
  <p><strong>Fig. 10.</strong> Training model results.</p>
</div>


<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/test_model.png" width="800">
  <p><strong>Fig. 11.</strong> Testing model results.</p>
</div>

The coin classification model demonstrated generally good performance while exhibiting some specific limitations. It performed particularly well in identifying distinctive coin types, with the 50p and 20p coins achieving approximately 90% accuracy in both the training and testing phases. This strong result can be attributed to their unique heptagonal shapes, which made them easily distinguishable. The 1p coin also achieved relatively high accuracy, largely due to its distinctive copper color and the prominent "1" marking on its reverse side. Interestingly, the 5p coin showed a training accuracy of 83.3%, which improved to 85.7% during testing. As illustrated in Fig. 8, the feature characteristics of these coin denominations are well-defined and contribute effectively to the model’s classification performance.

However, the model encountered significant challenges in classifying 10p coins. A noticeable gap between training and test accuracy suggests potential overfitting specific to this class. Approximately 20% of 10p coins were misclassified as 5p coins, likely due to the similar Queen's head designs on the obverse side and comparable textures on the reverse. As shown in Fig. 8, the features generated for 10p coins during training are not well-defined, which may have contributed to the confusion. Additionally, around 10% of 10p coins were misclassified as 50p coins, possibly due to their similar physical sizes.

<div align=center>
  <img src="https://raw.githubusercontent.com/JY-SHENNNN/CASA0018-CoinClassification/refs/heads/main/Projects/Final%20Project/Img/real_test00.jpg" width="800">
  <p><strong>Fig. 12.</strong> Real-world testing results.</p>
</div>


Real-world testing conducted through Edge Impulse's QR code deployment revealed additional limitations, the results shown in Fig. 12. The model's performance varied considerably depending on different backgrounds and coin orientations. I guess it's because the training dataset contains most of image were taken from the front.

During testing, several key challenges emerged. One issue was the variation in the Queen’s portrait design, which differed depending on the year the coin was minted. Another difficulty came from the coins’ small size, which made it harder to capture fine texture details in the images. In addition, the reflective nature of the coin material often caused lighting interference during image capture, affecting image consistency and model accuracy.

With additional development time, several improvements could be implemented. Expanding the training dataset to include images taken under different lighting conditions and from multiple angles, which would help to enhance the model’s generalization. Enhancing preprocessing methods to more effectively manage glare and reflections from coin surfaces could improve input quality. Also, applying temporal analysis to video streams, rather than relying on single-frame inputs, may give better performance during real-world testing. These enhancements would address the current limitations while building upon the model's existing strengths in recognizing distinctive coin features.
 
## Bibliography

1. Jahan, Z., Nazia Parween, Agrawal, A.P., Choudhary, A., Raj, G. and Aziz Deraman (2023). Deep Learning Based World Coin Currency Detection. Algorithms for intelligent systems, pp.439–449. doi:https://doi.org/10.1007/978-981-99-1620-7_35.

2. Xiang, Y., Yan, W.Q. Fast‐moving coin recognition using deep learning. Multimed Tools Appl 80, 24111–24120 (2021). https://doi.org/10.1007/s11042-021-10857-5

3. Segrave, K. (2015) Vending machines: an American social history. Jefferson, NC: McFarland.

4. Sourikta (2024). Assignment Dataset. [online] Roboflow. https://universe.roboflow.com/sourikta/assignment-za0qo


----

## Declaration of Authorship

I, Jiaying Shen, confirm that the work presented in this assessment is my own. Where information has been derived from other sources, I confirm that this has been indicated in the work.


*Jiaying shen*

ASSESSMENT DATE
23/4/2025
Word count: 1524
