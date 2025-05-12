# Travel Recommendation using Model Context Protocol (MCP)

## Overview

This repository contains the implementation of a travel recommendation system using Model Context Protocol (MCP). MCP enables seamless communication between models and remote servers, allowing for efficient, scalable, and modular deployment of AI services.

## What is Model Context Protocol (MCP)?

Model Context Protocol (MCP) is a lightweight, structured protocol designed to facilitate communication between AI models and remote execution environments. It allows models to offload tasks, retrieve context, and interact with external systems in a standardised way. MCP is particularly useful for:

- Decoupling model logic from infrastructure
- Enabling remote execution of model components
- Supporting scalable, cloud-native AI workflows

## Leveraging Azure Functions to Configure Remote MCP Servers

Azure Functions is a serverless compute platform that allows you to run small pieces of code (functions) without worrying about infrastructure. You can use Azure Functions to host MCP-compatible endpoints that your models can call remotely.

### Benefits:
- **Scalability**: Automatically scales based on demand.
- **Cost-effective**: Pay only for the time your code runs.
- **Integration**: Easily integrates with other Azure services like Blob Storage, Cosmos DB, and Event Grid.

## How to Create and Deploy to Azure Function App

### Step 1: Create a Function App

1. Go to the https://portal.azure.com/.
2. Click on **Create a resource** > **Compute** > **Function App**.
3. Fill in the required fields:
   - **Subscription** and **Resource Group**
   - **Function App name**
   - **Runtime stack** (e.g., Python, Node.js)
   - **Region**
4. Click **Review + create**, then **Create**.

### Step 2: Deploy the Code

1. Clone this repository:
   ```bash
   git clone https://github.com/anu-01/mcpfunc-TravelRecommendation.git
   cd mcpfunc-TravelRecommendation
   ```

2. Install the Azure Functions Core Tools if not already installed:
   ```bash
   npm install -g azure-functions-core-tools@4 --unsafe-perm true
   ```

3. Log in to Azure:
   ```bash
   az login
   ```

4. Deploy the function:
   ```bash
   func azure functionapp publish <YourFunctionAppName>
   ```

### Step 3: Test the Function

Once deployed, you can test the function by sending HTTP requests to the function endpoint. Make sure to include the appropriate payload expected by the MCP handler.

---

## Contributing

Feel free to fork the repo and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
