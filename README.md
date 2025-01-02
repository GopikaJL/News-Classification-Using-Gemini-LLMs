

# **News Classification Using Gemini LLMs**

## **Project Overview**
This project demonstrates the use of **Gemini Large Language Models (LLMs)** for **multi-class text classification** of news articles. The project focuses on leveraging **few-shot prompting** and **zero-shot testing** techniques, using the BBC News Dataset to classify articles into categories: **Business**, **Technology**, **Sports**, **Politics**, and **Entertainment**.

In future iterations, we plan to integrate **LangChain** for dynamic prompt engineering and implement **fine-tuning** for enhanced model performance.

---

## **Key Objectives**
1. Evaluate the performance of Gemini LLMs, specifically **Gemini Flash 1.5 Pro**, in text classification tasks.
2. Demonstrate the effectiveness of few-shot learning in real-world datasets.
3. Establish a robust framework for future advancements, including LangChain integration and fine-tuning.

---

## **Results and Interpretations**
### **Performance Metrics**
The model was tested using a **150-sample unseen test dataset**. Below is a summary of key metrics:

| **Metric**       | **Score**  |
|-------------------|------------|
| **Accuracy**      | 98.33%     |
| **Precision**     | 97.5%      |
| **Recall**        | 97.8%      |
| **F1 Score**      | 97.6%      |

---

### **Graphical Representation**
Visualizations of the classification performance will be included for better interpretability. Key metrics like precision, recall, and confusion matrices provide insights into the model's strengths and weaknesses.

---

## **Future Work**
### **LangChain Integration**
LangChain will be utilized for:
- **Dynamic Few-Shot Prompting**: Retrieve relevant examples dynamically from a vector database.
- **Advanced Prompt Chaining**: Enable multi-step workflows, such as summarizing articles before classification.

### **Fine-Tuning**
We aim to fine-tune the Gemini Flash 1.5 Pro model on the BBC News Dataset for:
- Enhanced task-specific performance.
- Efficient use of computational resources.

### **Dynamic Few-Shot Selection**
Embedding models (e.g., `e5-mistral-7b-instruct`) and vector databases (e.g., Pinecone, Qdrant) will be employed to select examples dynamically for few-shot prompting.

---

## **Environment Setup**
### **1. Requirements**
- Python 3.11+
- Gemini API Key (Sign up for Google AI Studio)
- Dependencies: Listed in `requirements.txt`.

### **2. Installation**
#### Create a Virtual Environment:
```bash
conda create -n gemini-news-classification python=3.11
conda activate gemini-news-classification
```

#### Install Dependencies:
```bash
pip install -r requirements.txt
```

### **3. Configure Gemini API Key**
- Obtain the API key from [Google AI Studio](https://aistudio.google.com).
- Configure it in the environment:
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
```

---

## **Running the Project**
### **Step-by-Step Execution**
1. **Dataset Preparation**:
   - Few-shot examples are selected, and the test dataset is prepared to avoid overlap.
   - Dataset files are saved in the `data/` directory.

2. **Text Classification**:
   - Few-shot and zero-shot classification are performed using **Gemini Flash 1.5 Pro**.
   - Scripts: `01_Dataset_Preparation.ipynb` and `02_Text_Classification.ipynb`.

3. **Output Cleaning**:
   - Clean raw outputs to standardize predictions.
   - Script: `03_Data_Cleaning_of_Outputs.ipynb`.

4. **Model Evaluation**:
   - Evaluate model performance using classification reports and confusion matrices.
   - Script: `04_Evaluation.ipynb`.

---


## Files and Workflow
1. **Dataset Preparation** ([01_Dataset_Preparation.ipynb](workflow/01_Dataset_Preparation.ipynb)):
   - Prepares few-shot and test datasets.

2. **Text Classification** ([02_Text_Classification.ipynb](workflow/02_Text_Classification.ipynb)):
   - Performs few-shot and zero-shot classification using Gemini Flash 1.5 Pro.

3. **Data Cleaning** ([03_Data_Cleaning_of_Outputs.ipynb](workflow/03_Data_Cleaning_of_Outputs.ipynb)):
   - Cleans raw outputs from the model.

4. **Evaluation** ([04_Evaluation.ipynb](workflow/04_Evaluation.ipynb)):
   - Computes classification metrics and plots confusion matrices.

5. **Fine-Tuning** ([05_Fine_Tuning.ipynb](workflow/05_Fine_Tuning.ipynb)):
   - Fine-tunes the model using the provided `fine_tune` function.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/news-classification.git
   cd news-classification

## **Future Enhancements**
1. **Dynamic Few-Shot Prompting**:
   - Use embedding-based similarity search for example selection.
2. **Hybrid Workflows with LangChain**:
   - Integrate LangChain for complex reasoning and multi-step workflows.
3. **Fine-Tuning**:
   - Fine-tune the Gemini Flash 1.5 Pro model for domain-specific tasks.

---

## **References**
1. [Google AI Studio](https://aistudio.google.com)
2. [LangChain Documentation](https://langchain.readthedocs.io/en/latest/)
3. [BBC News Dataset](https://www.kaggle.com/datasets)

---

Let me know if you'd like to further customize this README!
