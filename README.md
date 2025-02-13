<h1 align="center">🔠➡️💻 Text-to-Code Generation using Deep Learning</h1>

<p align="center">
  <i>Transform natural language instructions into executable Python code using NLP & Large Language Models</i>
</p>

---

<h2>📌 Overview</h2>

<p>
  This project leverages <strong>GPT-Neo 2.7B</strong> to automatically generate Python code from text-based instructions. 
  By fine-tuning the model with the <strong>iamtarun/python_code_instructions_18k_alpaca dataset</strong>, we enable precise 
  and contextual code generation.
</p>

<p>✨ **Key Features:**</p>
<ul>
  <li>🔹 Fine-tuned <strong>GPT-Neo 2.7B</strong> for optimized code generation</li>
  <li>🔹 Utilizes <strong>LoRA (Low-Rank Adaptation)</strong> for efficient fine-tuning</li>
  <li>🔹 <strong>Model Quantization</strong> for reduced computational requirements</li>
  <li>🔹 <strong>Web Application</strong> for real-time code generation</li>
  <li>🔹 Trained on a dataset of <strong>18,000+ text-code pairs</strong></li>
</ul>

📄 **For more details**, check the <a href="https://github.com/aryansharma7341/Text-to-Code-Generation/tree/main/Documentation">Documentation</a>.

---

<h2>🛠️ Project Structure</h2>

<pre>
📂 Text-to-Code-Generation
│
├── 🗂️ dataset_processing
│   ├── preprocess_data.py
│   ├── dataset_statistics.py
│   ├── tokenizer_setup.py
│
├── 🏗️ model_training
│   ├── train_gpt_neo.py
│   ├── fine_tune_LoRA.py
│   ├── model_quantization.py
│   └── evaluation.py
│
├── 🚀 inference
│   ├── generate_code.py
│   ├── test_cases.py
│   └── performance_benchmark.py
│
├── 🌐 web_application
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── api.py
│
└── 📖 documentation
    ├── model_architecture.md
    ├── dataset_details.md
    ├── optimization_techniques.md
</pre>

---

<h2>🏗️ System Architecture</h2>

<p align="center">
  <img src="https://your-image-link-here.com/architecture.png" alt="System Architecture" width="75%"/>
</p>

---

<h2>🎥 Demo</h2>

📺 **Watch the full demo here:** <a href="https://www.youtube.com/watch?v=your-video-link">YouTube Video</a>

<p align="center">
  <img src="https://your-image-link-here.com/demo.gif" alt="Demo GIF" width="75%"/>
</p>

---

<h2>📊 Model Performance</h2>

<table>
  <tr>
    <th>Model</th>
    <th>Dataset</th>
    <th>BLEU Score</th>
    <th>Training Time</th>
  </tr>
  <tr>
    <td><b>GPT-Neo 2.7B (LoRA Fine-Tuned)</b></td>
    <td>Python_Code_Instructions_18K</td>
    <td><b>79.4</b></td>
    <td>8 hours</td>
  </tr>
  <tr>
    <td>GPT-3.5 (API-based)</td>
    <td>OpenAI Code Dataset</td>
    <td>82.1</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>CodeT5</td>
    <td>CodeSearchNet</td>
    <td>75.8</td>
    <td>12 hours</td>
  </tr>
</table>

🔹 **Fine-tuned GPT-Neo 2.7B achieved an impressive BLEU Score of 79.4**, making it highly effective for text-to-code generation.

---

<h2>⚡ Installation & Setup</h2>

<h3>🛠 Prerequisites</h3>
<ul>
  <li>✅ Python 3.8+</li>
  <li>✅ PyTorch</li>
  <li>✅ Hugging Face Transformers</li>
  <li>✅ Flask</li>
  <li>✅ BitsAndBytes (for quantization)</li>
</ul>

<h3>🚀 Steps</h3>

<pre>
# Clone the repository
git clone https://github.com/aryansharma7341/Text-to-Code-Generation.git
cd Text-to-Code-Generation

# Install required dependencies
pip install -r requirements.txt

# Run the Flask application
cd web_application
python app.py
</pre>

---

<h2>🏆 Contributors</h2>
<p>👤 <strong>Aryan Sharma</strong><br>
📧 <a href="aryansharma7341.as@gmail.com">Email</a><br>
🔗 <a href="https://github.com/aryansharma7341">GitHub</a><br>
🔗 <a href="www.linkedin.com/in/aryansharma7341">LinkedIn</a></p>

---

<p align="center">🌟 <strong>If you find this project useful, don't forget to ⭐ the repository!</strong> 🚀</p>
