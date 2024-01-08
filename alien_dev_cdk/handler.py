
def handler(event: dict):
    """
    This is the handler function for the application.

    Args:
        event (dict): The event data passed to the handler.
        context (object): The context object passed to the handler.

    Returns:
        dict: The response object with statusCode and body.
    """

    return {
        'statusCode': 200,
        'body': 'Hello, world!'
    }
