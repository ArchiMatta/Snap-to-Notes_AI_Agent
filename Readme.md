# ✨ **Snap-to-Notes**
### *Convert screenshots into clean, structured notes using OCR + AI + workflow automation.*

---

## 🚀 **Overview**

**Snap-to-Notes** is an AI-powered agent that converts **screenshots or long text** into concise, high-quality notes.  
It includes **OCR extraction**, **multi-turn memory**, **AI summarization**, and a **human-approval workflow** for long documents.

---

## 🔥 **Key Features**

### 🖼️ **OCR — Screenshot → Text**
- Extracts text from screenshots using **Tesseract OCR**
- Works with **PNG, JPG, scanned documents**
- Handles noisy or low-quality images

### 🧠 **AI Summaries (Google Gemini)**
- High-quality bullet-point summaries  
- Insight-based improvements  
- Memory-driven refinement: “**improve the summary**” works automatically

### 🔁 **Multi-Turn Memory (Agent-Style)**
- Remembers previous user messages  
- Enables follow-up refinement  
- Tracks context across turns  

### 🟢 **Workflow Automation**
For long inputs (> **3000 chars**):
- Auto-detects long content  
- Starts a **long workflow**  
- Requests **human approval**  
- Resumes and generates final summary  

### 🔌 **Modular ADK-Inspired Architecture**
- Tools: **OCR, memory, context**
- Runtime: **workflow manager, approval handler**
- Clean, extensible architecture

---

## 🏗️ **Project Structure**
```
snap-to-notes/
│
├── agent/
│   ├── smartnote_agent.py
│   ├── memory_manager.py
│   ├── context_manager.py
│   └── agent_main.py
│
├── mcp_server/
│   ├── tools/
│   │   └── ocr_tool.py
│   └── runtime/
│       ├── operations/
│       │   ├── workflow_manager.py
│       │   └── approval_handler.py
│
├── screens/
│   └── sample.png
│
├── README.md
└── requirements.txt
```
---

## ⚙️ **How It Works**

### **1️⃣ Provide Input**
- A screenshot file path  
  Example: `D:\snap-to-notes\screens\image.png`  
**OR**
- Raw text (e.g., `"Summarize AI in education"`)

### **2️⃣ System Decision**
- Text **< 3000 chars** → instant summary  
- Text **> 3000 chars** → approval workflow

### **3️⃣ Screenshot Handling**
- OCR text extraction  
- Length detection  
- Human approval  
- Final summary  

### **4️⃣ Multi-Turn Memory**
You: *Summarize AI in education*  
You: *Improve the summary*  
→ Memory enhances results without repeated context

---

## 🧪 **Run Locally**

### **1. Install dependencies**
```bash
pip install -r requirements.txt
```

### **2. Create `.env` file**
```env
GOOGLE_API_KEY=your_key
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
```
### **3. Run the Agent**
```bash
python -m agent.agent_main
```
## 📌 Example Usage

### **Case 1: Short Text**
```
You: Summarize AI in education
→ Returns bullet-point summary
```
### **Case 2: Screenshot**
```
You: D:\snap-to-notes\screens\image.png
→ OCR → workflow → approval → summary
```
### **Case 3: Follow-Up**
```
You: improve it further
→ Memory-based refinement
```
## 🛠️ Tech Stack
- **Python**
- **Google Gemini 2.0 Flash**
- **Tesseract OCR**
- **ADK-style Modular Architecture**
- **Multi-Turn Memory & Workflows**

---

## 📚 Use Cases
- **Study notes from screenshots**
- **Summarizing long PDFs (via screenshots)**
- **Clean summaries for research**
- **Quick revision notes**
- **Productivity automation**

