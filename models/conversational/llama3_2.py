import ollama
from transformers.pipelines import pipeline
import torch
from huggingface_hub import InferenceClient

class Llama3_2_Inference:
    def __init__(self):
        self.client = InferenceClient(
            provider="together",
            api_key="hf_xxxxxxxxxxxxxxxxxxxxxxxx"
        )

        self._model = 'meta-llama/Llama-3.2-3B-Instruct'

        self._instruction = 'Responde las consultas del usuario utilizando estrictamente el contexto proporcionado. Si no tienes contexto suficiente para responder la consulta, niegate politicamente a responder'

    def answer(self, query:str, context=[]) -> str:

        messages = [
            {"role": "system", "content": self._instruction},
            {"role": "system", "content": f"Responde la consulta del usuario utilizando el siguiente contexto: {context}"},
            {"role": "user", "content": query}
        ]

        completion = self.client.chat.completions.create(
            model= self._model,
            messages = messages,
            max_tokens=5000
        )

        return completion.choices[0].message

class Llama3_2:
    def __init__(self):
        self.pipe = pipeline(
            "text-generation",
            model='meta-llama/Llama-3.2-3B-Instruct',
            torch_dtype=torch.bfloat16,
            device_map="auto",
        )

        self._instruction = 'Responde las consultas del usuario utilizando estrictamente el contexto proporcionado. Si no tienes contexto suficiente para responder la consulta, niegate politicamente a responder'

    def answer(self, query:str, context=[]) -> str:

        messages = [
            {"role": "system", "content": self._instruction},
            {"role": "system", "content": f"Responde la consulta del usuario utilizando el siguiente contexto: {context}"},
            {"role": "user", "content": query}
        ]

        outputs = self.pipe(
            messages,
            max_new_tolens= 5000
        )

        return outputs[0]["generated_text"][-1]
