import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="MyHttpTrigger", auth_level=func.AuthLevel.FUNCTION)
def MyHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    

@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="Hello_mcp",
    description="Hello mcpToolTrigger",
    toolProperties='[]',      
)
def hello_mcp(context) -> str:
    """
    A simple function that returns a greeting message.

    Args:
        context: The trigger context (not used in this function).

    Returns:
        str: A greeting message.
    """
    return "Hello I am MCPTool!"

class ToolProperty:
    def __init__(self, property_name: str, property_type: str, description: str):
        self.propertyName = property_name
        self.propertyType = property_type
        self.description = description

    def to_dict(self):
        return {
            "propertyName": self.propertyName,
            "propertyType": self.propertyType,  
            "description": self.description
        }
    
# Define the tool properties
toolProperties = [
    ToolProperty("destination", "string", "The destination for which to get recommendations.")
]

# Convert the tool properties to JSON
toolProperties_json = json.dumps([prop.to_dict() for prop in toolProperties])

@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="destination_recommendation",
    description="Get a recommendation for a destination.",
    toolProperties= toolProperties_json,
)   
@app.text_completion_input(arg_name="destination", prompt="Provide some recommendation for the {destination}?", max_tokens="100", model="gpt-4o-mini", description="The destination for which to get recommendations.")
@app.text_completion_output(arg_name="recommendation", description="Here are some recommendations for the destination.")
def destination_recommendation(destination: str, context) -> str:
    """
    A function that provides a recommendation based on the (destination).

    Args:
        destination (str): The destination for which to get recommendations.
        1. Lisbon
        2. Paris
        3. Rome
        4. New York
        5. Tokyo
        6. Sydney
        Use the trigger context to get the destination.

    Returns:
        str: A recommendation message. 
    """
    if not destination:
        return "Please provide a destination."

    # Define recommendations based on the destination   
    return f"Here are some recommendations for {destination}: \n1. Visit the local attractions.\n2. Try the local cuisine.\n3. Explore the culture and history.\n4. Enjoy outdoor activities.\n5. Relax and unwind at a local spa or wellness center."


