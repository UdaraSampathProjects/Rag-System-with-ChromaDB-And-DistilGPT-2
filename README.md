<h1> <strong>RAG System for Semantic Retrieval and Query Answering</strong> 📚</h1>

<h2><strong>📌️ Overview:</strong></h2>
The project implements a <strong>Retrieval-Augmented Generation (RAG)</strong> system designed to handle user queries efficiently by combining <strong>semantic search</strong> 🔍 with a <strong>generative model</strong> ✍️. It uses <strong>ChromaDB</strong> for storing and retrieving text semantically, ensuring that responses are relevant and contextually appropriate. For answering queries, the system employs the <strong>DistilGPT-2</strong> model, a lightweight version of GPT-2, to generate accurate and coherent responses based on the retrieved text.</p>

<h2><strong>📌️ Key Features:</strong></h2>

<ul>
  <li><strong>Text Extraction</strong> 📄: Raw text data is extracted from <code>.txt</code> files and preprocessed to ensure clean input for the retrieval system.</li>
  <li><strong>Semantic Storage</strong> 💾: Text data is stored in <strong>ChromaDB</strong>, an optimized database for semantic search, enabling efficient retrieval of contextually relevant documents.</li>
  <li><strong>Semantic Search</strong> 🔎: Upon receiving a user query, the system performs a semantic search using <strong>ChromaDB</strong>, identifying the most relevant text snippets based on the query’s context.</li>
  <li><strong>Answer Generation</strong> 💬: After retrieving the best matching text, the <strong>DistilGPT-2</strong> model generates a response, utilizing the retrieved information to provide accurate and relevant answers.</li>
  <li><strong>Efficiency</strong> ⚡: The system balances fast semantic retrieval and quick answer generation, ensuring smooth and responsive user interactions.</li>
</ul>

<h2><strong>📌️ Technologies Used:</strong></h2>
<ul>
  <li><strong>ChromaDB</strong> 🔒: A database optimized for semantic text retrieval.</li>
  <li><strong>DistilGPT-2</strong> 🤖: A compact version of GPT-2 for generating text-based answers.</li>
  <li><strong>Python</strong> 🐍: For building the system and integrating components.</li>
</ul>

<h2><strong>📌️ Impact:</strong></h2>
<p>This RAG system enables quick, accurate, and context-aware responses, making it ideal for applications like document search 📑, customer support 💬, and automated information retrieval 🧠. Its scalability allows it to handle large datasets and provide meaningful interactions in real-time.</p>
