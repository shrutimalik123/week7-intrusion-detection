# Simulated Intrusion Detection Using Cloud-Based Tools

Week 7 project for IAS5201 (Capella University). It trains a Random Forest classifier on a sample of the UNSW-NB15 network traffic dataset to separate benign from malicious flows.

## Contents

| File | Description |
|------|-------------|
| `cf_week_7_assignment_code.docx` | Provided Colab code (data download, preprocessing, model training, evaluation) |
| `UNSW_NB15.csv` | Preprocessed sample: 5,000 flows (4,796 benign, 204 malicious) |
| `Week7_Intrusion_Detection_Report.docx` | Analysis report (APA format) |
| `make_report.py` | Script that generates the report with python-docx |

## Method

1. Download and load the dataset with `gdown` and Pandas.
2. Drop IP address columns and label-encode categorical fields.
3. Remove missing values and keep numeric columns.
4. Split 70% train and 30% test.
5. Train a `RandomForestClassifier`.
6. Evaluate with a classification report and confusion matrix.

## Results

- Accuracy about 100% on 1,500 test flows.
- Confusion matrix: 1,440 TN, 1 FP, 0 FN, 59 TP.
- Malicious class: precision 0.98, recall 1.00, F1 0.99.
- Top features: source and destination TTL (`sttl`, `dttl`).

## Limitations

Small, imbalanced data; heavy reliance on two features; weak against novel attacks; single train/test split.

## Run it

Paste the code into a new [Google Colab](https://colab.research.google.com/) notebook and run it, or run locally with `pip install gdown pandas scikit-learn seaborn matplotlib`.

## Reference

Moustafa, N., & Slay, J. (2015). UNSW-NB15: A comprehensive data set for network intrusion detection systems. *2015 MilCIS*. https://doi.org/10.1109/MilCIS.2015.7348942
