<H1> Doctor assistant bot </H1>
<img src ="https://github.com/teamUBUNTU/Doc-Assist-BOT/blob/main/static/logo.jpg"></img>
<H3> A disease prediction bot that provides assistance to doctors for better disease accuracy and prediction bot. </H3>

Augmenting clinical practice with data and AI. We try to empower the doctor with ever-growing medical literature, statistics in time bound situations. The system learns over time post deployment. 

<b>What it does</B>
Doc Assit Bot is a chatbot that listens to your symptoms and predicts the most probable infection or disease you might have that would assist the doctor give his final report of the patient he is diagnosing 

<b>How we built it</B>

<li>Backend: Python + Flask 
<li>Frontend: Html,css
<li>Model : RandomForest from sklearn library for the disease prediction. The model has been pretrained on a dataset of 4920 trials with 132 symptoms and 41 diseases.NLP librabry was used for the pre processing for the user input 

<li>Dataset: https://www.kaggle.com/rabisingh/symptom-checker
  
<b>Instructions to run it</B>
<li> git clone https://github.com/teamUBUNTU/Disease_chatbot.git
<li> Or u could access Collab link :https://colab.research.google.com/drive/1iy0yRoLSxwoYgDCXyvx9CzolZY9YzbWq?usp=sharing
  
Objective : Ever increasing patient load and decreasing patient doctor interaction duration often results in misdiagnosis. Apart from wrong diagnosis, a constant learning AI based assistant can also help general practitioners and junior doctors to derive insights from latest clinical advancements, treatment protocols and medical literature in real time. 

The problem it solves : 
A doctor whether experienced or fresh is sufficiently equipped to utilize the latest information and development in medical sciences in his practice.
Moreover, during emergency situations, there is substantial pressure and the chances of missing out a point of view are more pronounced. At the same time there limit to the amount of information a doctor can remember and recollect in real scenarios,
Much experience and time are required to get good at this. 
Also, the disease and human response are biased by the demographics, age group, etc. Per patient time available to a doctor is reducing due to a high caseload.
Often the vast experience itself of a clinician may result in bias while making a diagnosis towards a more prevalent disorder or pathology. Per patient time available to a doctor is reducing due to a high caseload.
Often the vast experience itself of a clinician may result in bias while making a diagnosis towards a more prevalent disorder or pathology.
We do not address the patients, but doctors in order to help the expert and not encouraging self-medication. 
It's scalable as well, on one end the information repositories may keep increasing which can be directly utilized by the system for dispensing the same information to the doctor as well. The Covid19 pandemic has made it realize that there is a lack of technology, which allows doctors to access the information from literature and statistics quickly enough to be integrated into daily practice.
