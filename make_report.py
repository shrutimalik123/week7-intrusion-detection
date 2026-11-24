from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH as A
from docx.oxml.ns import qn

d = Document()
for s in d.sections:
    s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Inches(1)
st = d.styles['Normal']
st.font.name = 'Times New Roman'
st.font.size = Pt(12)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
st.paragraph_format.line_spacing = 2
st.paragraph_format.space_after = Pt(0)


def P(t, c=False, b=False, ind=True, hang=False):
    p = d.add_paragraph()
    r = p.add_run(t)
    r.bold = b
    if c:
        p.alignment = A.CENTER
    if ind:
        p.paragraph_format.first_line_indent = Inches(0.5)
    if hang:
        p.paragraph_format.left_indent = Inches(0.5)
        p.paragraph_format.first_line_indent = Inches(-0.5)
    return p


P('Week 7 Assignment: Simulated Intrusion Detection Using Cloud-Based Tools', True, True, False)
for t in ['Shruti Malik', 'Capella University', 'IAS5201', 'Stuart McCubbrey', 'November 29, 2026']:
    P(t, True, ind=False)
d.add_page_break()
P('Simulated Intrusion Detection Using Cloud-Based Tools', True, True, False)

body = [
 (None, 'The Colab notebook downloaded a preprocessed sample of the UNSW-NB15 dataset (Moustafa & Slay, 2015) containing 5,000 network flows, of which 4,796 were benign and 204 were malicious. The program loaded the data into a Pandas DataFrame and dropped the source and destination IP addresses because they carry little value as numeric features. It then converted text fields such as protocol and connection state into numbers with label encoding, removed rows with missing values, and kept only numeric columns. The data were divided into 70% training and 30% testing sets. A Random Forest classifier, an ensemble of decision trees (Breiman, 2001), was trained to separate benign from malicious flows and then evaluated on the unseen test set.'),
 ('Model Accuracy', 'The model performed very well. On the 1,500 test flows, overall accuracy was about 100%. The confusion matrix showed 1,440 true negatives, 59 true positives, 0 false negatives, and only 1 false positive. Precision for malicious traffic was 0.98, recall was 1.00, and the F1-score was 0.99. In security terms, no attacks were missed, and analysts would have received just one false alarm. Because false negatives are the most dangerous error, the zero-miss result is encouraging.'),
 ('Suspicious Patterns and Behaviors', 'The model flagged flows whose characteristics deviated from normal behavior. Feature importance values showed that the source and destination time-to-live values (sttl and dttl) were the strongest indicators, together accounting for nearly 80% of the decisions. Connection state, flow duration, and the bytes sent and received contributed smaller amounts. This suggests that attack traffic, such as scanning, unusual login attempts, or data exfiltration with abnormal transfer volumes, left measurable differences in packet and session characteristics that the model learned to recognize.'),
 ('Limitations', 'Despite the near-perfect score, several limitations apply. First, the data set is small and imbalanced, with malicious flows making up only about 4% of records, so the results may not generalize to production networks. Second, the model relies heavily on two features, and an attacker who manipulates TTL values could evade detection. Third, supervised learning only recognizes attack types resembling its training labels, so novel zero-day attacks may be missed (Sommer & Paxson, 2010). Fourth, the evaluation used a single random split with default settings and no cross-validation, which can overstate performance. Finally, Random Forests are harder to interpret than a single rule, and real-world concept drift and false-alarm volumes would require regular retraining and human review.'),
 ('Conclusion', 'Claude (Anthropic, 2026) was used to help run the code and draft this report. The exercise showed that AI models can detect intrusions by learning statistical deviations in network behavior, but strong lab accuracy should be validated with realistic, current, and diverse data before deployment.'),
]
for h, t in body:
    if h:
        P(h, True, True, False)
    P(t)
P('References', True, True, False)
for t in [
 'Anthropic. (2026). Claude Sonnet 5.5 [Large language model]. https://www.anthropic.com',
 'Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5\u201332. https://doi.org/10.1023/A:1010933404324',
 'Moustafa, N., & Slay, J. (2015). UNSW-NB15: A comprehensive data set for network intrusion detection systems. In 2015 Military Communications and Information Systems Conference (MilCIS) (pp. 1\u20136). IEEE. https://doi.org/10.1109/MilCIS.2015.7348942',
 'Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. In 2010 IEEE Symposium on Security and Privacy (pp. 305\u2013316). IEEE. https://doi.org/10.1109/SP.2010.25']:
    P(t, ind=False, hang=True)
d.save('Week7_Intrusion_Detection_Report.docx')
print(sum(len(t.split()) for _, t in body))
