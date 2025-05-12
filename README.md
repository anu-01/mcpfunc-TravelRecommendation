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

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Note it is a best practice to create a Virtual Environment before doing the pip install to avoid dependency issues/collisions, or if you are running in CodeSpaces. See Python Environments in VS Code for more information.

3. Deploy to Azure for Remote MCP

   - Log in to Azure:
   ```bash
   az login
   ```
   - Deploy to function app resource you created earlier in Step 1
   ```bash
   az functionapp deployment source config-zip \  --resource-group <YourResourceGroup> \  --name <YourFunctionAppName> \  --src <path-to-your-zip-file>
   ```

### Step 3: Connect to your remote MCP server function app from a client

Your client will need a key in order to invoke the new hosted SSE endpoint, which will be of the form https://<funcappname>.azurewebsites.net/runtime/webhooks/mcp/sse. The hosted function requires a system key by default which can be obtained from the portal or the CLI (az functionapp keys list --resource-group <resource_group> --name <function_app_name>). Obtain the system key named mcp_extension.

#### Connect to remote MCP server in MCP Inspector
For MCP Inspector, you can include the key in the URL:
```bash
https://<funcappname>.azurewebsites.net/runtime/webhooks/mcp/sse?code=<your-mcp-extension-system-key>
```

#### Connect to remote MCP server in VS Code - GitHub Copilot
For GitHub Copilot within VS Code, you should instead set the key as the x-functions-key header in mcp.json, and you would just use https://<funcappname>.azurewebsites.net/runtime/webhooks/mcp/sse for the URL. The following example uses an input and will prompt you to provide the key when you start the server from VS Code. Note mcp.json has already been included in this repo and will be picked up by VS Code. Click Start on the server to be prompted for values including functionapp-name (in your /.azure/*/.env file) and functions-mcp-extension-system-key which can be obtained from CLI command above or API Keys in the portal for the Function App.

```json
{
    "inputs":[
        {
            "type": "promptString",
            "id": "functions-mcp-extension-system-key",
            "description": "Azure Functions Extension System Key",
            "password": true
        }
    ],
    "servers": {
        "my-mcp-server-13c2eec6": {
            "type": "sse",
            "url": "https://<funcappname>.azurewebsites.net/runtime/webhooks/mcp/sse",
            "headers": {
                "x-functions-key": "${input:functions-mcp-extension-system-key}",
            },
        }
    }
}
```
---


## Contributing

Feel free to fork the repo and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.


