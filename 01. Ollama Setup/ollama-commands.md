# Ollama Setup Commands
___
## Installation
Download the latest version of Ollama from the [official website](https://ollama.com/)

## Commands Overview
- `serve`: Start the Ollama service.
- `create`: Create a new model using a Modelfile.
- `show`: Display detail for a specific model.
- `run`: Execute aa model.
- `stop`: Stop a running model.
- `pull`: Download a model from a registry.
- `push`: Upload a model to a registry.
- `list`: List all available models.
- `ps`: Show currently running models
- `cp`: Copy a model to a new location.
- `rm`: Delete a model.
- `help`: Display help for commands.

## Flags
- `-h --help`: Show help information.
- `-v --version`: Show version details.

**Use `ollama [command]` to execute any command above.**

## Ollama Command Cheat Sheet
A quick reference for commands inside Ollama models:
- **/set**: Set session variables.
- **/show**: Display information about the current model.
- **/load** : Load a specific session or model.
- **/save** : Save your current session.
- **/clear**: Clear the session context.
- **/bye**: Exit the session.
- **/?**, **/help**: Show help for commands.
- **/?** shortcuts: Display help for keyboard shortcut

**Tip: ** Use `"""` to start a multi-line message.

## Ollama API Cheat Sheet [Link](https://github.com/ollama/ollama/blob/main/docs/api.md)
### Generate
```
POST /api/generate
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:1b",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

### Chat Completion
```
POST /api/chat
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2:1b",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": false
}'
```

## Create a New Model with Custom Settings [Link](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)
```ollama create sheldon -f .\mymodelfile.txt```