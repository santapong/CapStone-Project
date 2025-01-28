{
  "api": {
    "name": "KMITLBOT",
    "version": "1.0",
    "base_url": "https://api.example.com/chatbot",
    "endpoints": [
      {
        "endpoint": "/chat",
        "method": "POST",
        "description": "Send a user message and get a chatbot response",
        "headers": {
          "Content-Type": "application/json",
          "Authorization": "Bearer <token>"
        },
        "request_body": {
          "user_id": {
            "type": "string",
            "description": "Unique identifier for the user"
          },
          "message": {
            "type": "string",
            "description": "The user's input message"
          },
          "context": {
            "type": "object",
            "description": "Conversation context for maintaining continuity",
            "optional": true,
            "example": {
              "previous_message": "string",
              "conversation_state": "object"
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful response with chatbot message",
            "body": {
              "response_message": "string",
              "context": {
                "type": "object",
                "description": "Updated conversation context for the next message"
              },
              "suggestions": {
                "type": "array",
                "description": "Optional quick reply suggestions",
                "example": ["string"]
              }
            }
          },
          "400": {
            "description": "Bad request",
            "body": {
              "error": "string"
            }
          },
          "401": {
            "description": "Unauthorized",
            "body": {
              "error": "string"
            }
          }
        }
      },
      {
        "endpoint": "/user/{user_id}",
        "method": "GET",
        "description": "Fetch user profile for personalization",
        "headers": {
          "Authorization": "Bearer <token>"
        },
        "path_parameters": {
          "user_id": {
            "type": "string",
            "description": "Unique identifier for the user"
          }
        },
        "responses": {
          "200": {
            "description": "Successful response with user data",
            "body": {
              "user_id": "string",
              "name": "string",
              "preferences": {
                "type": "object",
                "description": "User preferences for personalized responses"
              }
            }
          },
          "404": {
            "description": "User not found",
            "body": {
              "error": "string"
            }
          }
        }
      }
    ]
  }
}
