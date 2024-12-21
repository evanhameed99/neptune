# 🌑 Neptune

**Neptune** is an API that enables users to parse PDF documents and interact with their content using generative AI. Whether you're exploring lengthy reports, analyzing research papers, or organizing your notes, Neptune simplifies document understanding by making them conversational.


## 🌟 Features

- **Chat with Documents**: Use generative AI to ask questions and get insightful answers from your PDFs.
- **History-Aware Conversations**: Engage in contextually aware sessions, keeping track of the discussion history.
- **Efficient Parsing**: Break down large documents into manageable chunks for seamless processing.


## 🛠️ Techniques Utilized

- **RAG (Retrieval-Augmented Generation)**: Combines retrieval-based methods with generative AI to provide accurate and contextually enriched responses.
- **Vector Embedding**: Converts text into high-dimensional vectors for efficient similarity search.
- **Cosine Similarity**: Compares and ranks document chunks based on query relevance.
- **Prompt Engineering**: Designs optimized prompts for generative AI to ensure meaningful responses.
- **Document Splitting and Chunking**: Divides large documents into smaller segments for improved performance and accuracy.
- **LangChain Piping and Chaining**: Structures complex workflows for advanced query handling.
- **History-Aware Chat Sessions**: Maintains conversational context to provide accurate follow-ups.
- **Server-Side Event Streaming with FastAPI**: Implements real-time updates via server-sent events for a seamless user experience.
- **FastAPI Background Tasks**: Handles long-running processes asynchronously to enhance responsiveness and scalability.

## Packages/Tools Utilized

- pymupdf4llm
- langchain 
- ollama
- redis
- sentence-transformers 

## 🚀 Try it out

The service is dockerized, making it easy to set up and run. Ensure you have Docker installed and running on your system.

### ⚠️ Note for macOS M1 Users and newr chips

When using Ollama on macOS with M1 or newer chips, models will run on the CPU only due to current limitations in Docker.  
For Windows or Linux users, the Ollama image can be added as a service in the `docker-compose.yaml`. More details can be found [here](https://github.com/ollama/ollama/issues/3849#issuecomment-2075359242).

To avoid this limitation on macOS, Ollama should be pre-installed on your host machine.


#### Steps to run

1. Install Ollama on your host. https://ollama.com/download
2. Pull the desired LLM model using Ollama. By default, `llama3.2:3b-instruct-fp16` is set in the configuration file. If you plan to use this model, ensure it is installed by running:  
   ```bash
   ollama pull llama3.2:3b-instruct-fp16
   ```

3. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/neptune.git
   ```
4. Navigate to the Main Directory where `docker-compose.yaml` is located.
5. Run `docker compose up`



