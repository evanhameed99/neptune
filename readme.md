# 🌑 Neptune

Neptune is a simple API that enables users to chat with their notes or docs by leveraging Ollama, a local large language model (LLM) provider.

## Techniques Utilized

- **Ollama**: A platform for managing and running large language models locally with ease.
- **LangChain Piping and Chaining**: Structures complex workflows for advanced query handling.
- **Vector Embedding**: Converts text into high-dimensional vectors for efficient similarity search.
- **Cosine Similarity**: Compares and ranks document chunks based on query relevance.
- **Prompt Engineering**: Designs optimized prompts for generative AI to ensure meaningful responses.


## Packages/Tools Utilized

- ollama
- langchain 
- pymupdf4llm
- redis
- sentence-transformers 

##  Try it out

The service is dockerized, making it easy to set up and run. Ensure you have Docker installed and running on your system.

###  Note for macOS users with Applle Sillicon chips

When using Ollama on the Sillicon chips, models will run on the CPU only due to current limitations in Docker.  
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
5. Run `docker compose up` (Make sure you have Docker daemon installed and running).



#### Swagger
Swagger can be accessed by visiting `http://localhost:8040/docs` after you have followed above steps. 

