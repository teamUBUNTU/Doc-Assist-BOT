<H1> Doctor Assistant Bot </H1>
<img src ="https://github.com/teamUBUNTU/Doc-Assist-BOT/blob/main/static/logo.jpg"></img>
<H3> A disease prediction bot that provides assistance to doctors for better and faster diagnostics.</H3>

Augmenting clinical practice with data and AI. We try to empower the doctor with ever-growing medical literature, statistics in time bound situations. The system learns over time, post deployment. 

<b>What it does</B>
Doc Assit Bot is a chatbot that listens to a patient's symptoms and predicts the most probable infection or disease, hence assisting in diagnosing a patient.

<b>Framework:</B>
<li>Backend: Python + Flask 
<li>Frontend: Bootstrap (Barebones, for demo only)
<li>Machine Learning Model : RandomForest and Naive Bayes from Sklearn for the disease prediction. The model has been pretrained on a dataset of 4920 trials with 132 symptoms and 41 diseases. NLTK was used for pre-processing of the input description.

<li>Dataset: https://www.kaggle.com/rabisingh/symptom-checker
  https://www.kaggle.com/sulianova/cardiovascular-disease-dataset
  
<b>How to run:</B>
<li> Have a look at our Colab notebook. Everything is clearly shown there:https://colab.research.google.com/drive/1iy0yRoLSxwoYgDCXyvx9CzolZY9YzbWq?usp=sharing</li><br>

<b>Objective:</b> 

Ever increasing patient load and decreasing patient doctor interaction duration often results in misdiagnosis. Apart from wrong diagnosis, a constant learning AI based assistant can also help general practitioners and junior doctors to derive insights from latest clinical advancements, treatment protocols and medical literature in real time. 

<b>The problem it solves:</b> 
<p>A doctor whether experienced or fresh is sufficiently equipped to utilize the latest information and development in medical sciences in his practice.
Moreover, during emergency situations, there is substantial pressure and the chances of missing out a point of view are more pronounced. At the same time there limit to the amount of information a doctor can remember and recollect in real scenarios,
Much experience and time are required to get good at this. </p>
<p>Also, the disease and human response are biased by the demographics, age group, etc. Per patient time available to a doctor is reducing due to a high caseload.
Often the vast experience itself of a clinician may result in bias while making a diagnosis towards a more prevalent disorder or pathology. Per patient time available to a doctor is reducing due to a high caseload.
Often the vast experience itself of a clinician may result in bias while making a diagnosis towards a more prevalent disorder or pathology.</p>
<p>
We do not address the patients, but doctors in order to help the expert and not encouraging self-medication. 
It's scalable as well, on one end the information repositories may keep increasing which can be directly utilized by the system for dispensing the same information to the doctor as well. The Covid19 pandemic has made it realize that there is a lack of technology, which allows doctors to access the information from literature and statistics quickly enough to be integrated into daily practice.
</p>