# EduPath – AI Based Student Career Guidance System  

This project analyzes students’ marks in 7 subjects and predicts their suitable career stream (Science, Commerce, Arts, or Computer Science) using Python and Machine Learning.  

## Subjects  
- Math  
- Science  
- English  
- Logical Thinking  
- Computer Science  
- Social Studies  
- Arts  

## Dataset (10 Students)  

| Roll No | Name    | Math | Science | English | Logical Thinking | Computer Science | Social Studies | Arts |
|---------|---------|------|---------|---------|-----------------|------------------|----------------|------|
| 1       | Janhavi | 92   | 88      | 75      | 85              | 90               | 60             | 40   |
| 2       | Aakash  | 75   | 70      | 80      | 72              | 68               | 70             | 45   |
| 3       | Priya   | 60   | 65      | 88      | 68              | 55               | 80             | 70   |
| ...     | ...     | ...  | ...     | ...     | ...             | ...              | ...            | ...  |
| 10      | Sameer  | 58   | 55      | 60      | 58              | 50               | 65             | 52   |

*(Full dataset is in **students.xlsx**)*  

## Steps  
1. Dataset created in Excel with 10 students and 7 subjects.  
2. Data preprocessing (cleaning and normalization).  
3. Model trained using Decision Tree Classifier.  
4. Predictions made for suitable student streams.  
5. Model accuracy ~80–90%.  

## Files  
- edupath.py – Main Python script  
- edupath.ipynb – Jupyter Notebook version  
- students.xlsx – Dataset  
- predictions.csv – Model predictions  
- requirements.txt – Required libraries  
- README.md – Project documentation  

## Run Instructions  
Install requirements:  
```
pip install -r requirements.txt
```

Run Python script:  
```
python edupath.py
```

Or run Jupyter Notebook:  
```
jupyter notebook edupath.ipynb
```

## Note  
It demonstrates how Machine Learning can be applied for **career guidance**.  
The project is simple but effective, and can be improved in the future with more data and advanced models.  
