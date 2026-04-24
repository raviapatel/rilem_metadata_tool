## How to use the tool:
This document is a instruction how to use the *RILEM Metadata Compilation Tool*.

The tool is split in two parts.

### Part one: author information

<img width="1484" height="1008" alt="image" src="https://github.com/user-attachments/assets/f1d0f965-4f50-483b-a909-78bee1cd88b3" />


It requires a description of:


**Title:**
Try to give the dataset a distinctive title, you might have already named it in the repository you use, please use the same name as there.

**Keywords:** 
Use some keywords that fit your data, experiment or material. This field might be later used to search it with a LLM so you should follow usual descriptions that are already common in the field.

**Description:** 
Describe your data in your own words. Keep in mind that at one point a LLM might pick this information for finding your data. So you might want to be a bit specific as it can improve your chance of someone re-using the data and therefore citing your work.

**Uploaded by:**
Because in some cases the data will not be handled by the creators or authors themselfes but by e.g. a designated Data Steward of an organization. The persons name and email can be put here. This field could also be used similar to the corresponding author if one of the authors of the research data did the upload.

**E-mail:**
The contact e-mail of the person who uploaded the data. This can be an author or e.g. the organizations Data Steward. If there is a common data steward e-mail address of an organization it could also be used here. This should enable personal contact but it has the same difficulties as contacting authors of papers, it might work but in case there is a change of employer the usefulness might be lost after some time.

**Date:**
When was the dataset uploaded to the repository?

**Identifyer:**
Unique persistent identifier for your dataset. Depending on your repository that might be a doi, a Handle ID, a URN etc.

**Contributors:**
Same as the authors of a paper, or if there is a corresponding paper it could be the same authors there are on the paper.

When every field was filled out click the ***Submit Author*** button.

If you are sucessful you get a confirmation an a preview of the structured view of the author information:
<img width="1493" height="1152" alt="image" src="https://github.com/user-attachments/assets/e24b7eda-1861-4f10-8492-debe37521071" />

### Part two: Dataset Information
This part is separated in some subsections. The first subsection requires some general information about the research data that should be described.
<img width="1488" height="500" alt="image" src="https://github.com/user-attachments/assets/3c608be3-0a10-412f-8127-e0c0f4265ddd" />

First the kind of data should be described. 
In the dropdown menue a selection between text, table, image, audio and video is required. In the case of more than one data type in your repository or the situation that e.g. multiple tables were saved in the repository please pick one first, **you will be able to come back and enter additional descriptions** as soon as you filled out this section. The information enables sorting of your data and allows researchers e.g. looking for graphic information in microscopy pictures to find research datasets that contain pictures.

The checkbox for time series should be checked when measurments were done at multiple points in time on the samples (e.g. 1d, 2d, 7d, 28d values). 

The field *Number of Files* is shown in case of image, audio or video selection. It allows to detail how many files are in your repository folder (e.g. 10 microscopy images were put in one folder and the metadata I am describing is for this folder content).

In case the information that is entered is for a table the field *Number of Rows* is displayed. 
This information is important for researchers that are looking for data to estimate how big your dataset is (which might also influence the method that will be used to process the data in case of modeling). 

The field *Dataset Description* allows to freely enter a description of your data, it can be formulated however it is deemed fit. Researchers looking for data can derive some additional information from this field and at a later point in time it might be used for LLM searches.

What follows is a description of **Data Categories (global)** (the category *tables* is special and has another entry instead).
Here is an example:
<img width="1489" height="596" alt="image" src="https://github.com/user-attachments/assets/0ba17e49-d56b-4b09-94b7-2e72e868880d" />
The first two fields are dropdown lists. The user should pick information that fits their data from the list and add it. Multiple data categories can be added by clicking the button *Add data categorie*. 
The two fields *Common Units* and *Category Description* are just there help the user select the data categories. They just display information that is common to the selected options in the dropdown lists.

In the case of *table* the following filed pops up:
<img width="1488" height="732" alt="image" src="https://github.com/user-attachments/assets/81d1972c-62d9-4cde-85b8-58e1609ba5c9" />

It works similar to the previously described *Data Categories (global)* regarding the entry of information but asks for additional information for each entered column.
The goal is to proviede the actual of title or header of each column (please copy paste the header or use the exact upper and lower case letters, this makes it easier to reuse the data, even if your header is a placehoder like "Factor_1") and additionally write down the entity of the information of the column (e.g. N/mm^2 or g/mm^3...).

The next section is **Materials** the idea is to list every material that was used in the experiments but not necessarily to order it. After selection it can be added with the *Add Material(s)* button. The materials are displayed in the filed below.
<img width="1489" height="557" alt="image" src="https://github.com/user-attachments/assets/05dc5cd0-1f69-4e37-bd93-07eb38b1651a" />
The section *Category Description* gives a short descriptions what is meant with the selected material. it cannot be selected and has information purpose only.






