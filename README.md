

# **News Classification Using Gemini LLMs**

## **Project Overview**
This project demonstrates the use of **Gemini Large Language Models (LLMs)** for **multi-class text classification** of news articles. The project focuses on leveraging **few-shot prompting** and **zero-shot testing** techniques, and implemented **fine-tuning** for enhanced model performance, using the BBC News Dataset to classify articles into 5 categories: **Business**, **Technology**, **Sports**, **Politics**, and **Entertainment**.



## **Key Objectives**
1. Evaluate the performance of Gemini LLMs, specifically **Gemini Flash 1.5 **, in text classification tasks.
2. Demonstrate the effectiveness of few-shot learning in real-world datasets utilising 5 samples from each categories.

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
We aim to fine-tune the Gemini Flash 1.5  model on the BBC News Dataset for:
- Enhanced task-specific performance.
- Efficient use of computational resources.
- PEFT approaches only fine-tune a small number of (extra) model parameters while freezing most parameters of the pretrained LLMs, thereby greatly decreasing the computational and storage costs
-  QLoRA, one of the latest methods that reduces the memory usage of LLM finetuning without performance tradeoffs, using the LoraConfig class from the peft library


---

## **Environment Setup**
### **1. Requirements**
- Python 3.11+
- Gemini API Key (Sign up for Google AI Studio)


### **2. Installation**
#### Create a Virtual Environment:
```bash
conda create -n gemini-news-classification python=3.11
conda activate gemini-news-classification
```



### **3. Configure Gemini API Key**
- Obtain the API key from [Google AI Studio](https://aistudio.google.com).
- Configure it in the environment:
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
```
![image](https://github.com/user-attachments/assets/e90c8520-4c88-4848-b2de-bf57db126ccd)

---

## **Running the Project**
### **Step-by-Step Execution**
1. **Dataset Preparation**:
   - Few-shot examples are selected, and the test dataset is prepared to avoid overlap.
   - Dataset files are saved in the `data/` directory.

2. **Text Classification**:
   - Few-shot and zero-shot classification are performed using **Gemini Flash 1.5 **.
   - Scripts: `Few-Shot Data.py` and `data/Dataset_Preparation.ipynb`.

3. **Output Cleaning**:
   - Clean raw outputs to standardize predictions.
   - Script: `model.py`.

4. **Model Evaluation**:
   - Evaluate model performance using classification reports and confusion matrices.
   - Script: `Tuning.ipynb`.

---



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
