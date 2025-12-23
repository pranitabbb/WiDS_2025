## Key Insights from EDA

## Dataset Overview
The PlantVillage dataset consists of 38 plant disease classes. Images are provided in three variants (color, grayscale, segmented).
For this analysis, color images were used.

### Class Imbalance
Several disease classes are significantly underrepresented (e.g., Potato___healthy,
Apple___Cedar_apple_rust), while others contain a large number of images.
This class imbalance may bias the model toward majority classes and will likely
require augmentation or class-weighted training strategies.

## Image Resolution
Classes have fixed and consistent image dimensions, resulting in overlapping points in resolution scatter plots.

## Aspect Ratio Characteristics
Most images have aspect ratio ≈ 1.

### Image Quality
Most images are clear, with no significant blur observed across the dataset.
This suggests that image quality is generally sufficient for training deep learning models.

### Lighting Conditions
Lighting conditions are mostly consistent across classes, with daylight illumination
in the majority of images. 
However, a small number of images exhibit poor lighting
or strong reflections on leaf surfaces, which may affect feature extraction and
model robustness.

### Background Consistency
The dataset largely contains uniform backgrounds, which simplifies the learning task.
The Corn_(maize)_Common_rust_ class has different background overall.

### Visual Similarity
Some disease classes are visually similar, with differences that are subtle rather than obvious.
Even though I can differentiate them by closely inspecting the images, the differences are small and subtle which might make classification difficult.


## Conclusion
The dataset is well-structured but not perfectly balanced.
Image resolutions are largely consistent, simplifying preprocessing.
Visual similarity between classes represents the primary challenge as the differences are subtle.


