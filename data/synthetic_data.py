import json
import uuid
import lorem
from data_types import VectorDocument

def generate_synthetic_data(path='./data/data.json', total_docs=500):
    with open(path, 'w', encoding='utf-8') as output:
        
        data = {}
        for _ in range(total_docs):
            pregunta = '¿' + lorem.get_word(count=(5, 10)) + '?'
            respuesta = lorem.get_sentence(count=(2, 5))
            id = str(uuid.uuid4())

            data[id] = VectorDocument(
                document=pregunta,
                metadata={
                    "pregunta": pregunta,
                    "respuesta": respuesta
                },
                uuid=id
            ).model_dump()

        json.dump(data, output, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    generate_synthetic_data()
