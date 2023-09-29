import openai
from docx import Document  
#from googleapiclient.discovery import build
#from google.oauth2 import service_account

# Configurar la clave de API de OpenAI
openai.api_key = "tu api key aqui"



def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
             messages=[
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": ""}
            ],      
            temperature=0.5,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
        message = response.choices[0].message['content']
        print(message)
        return message
    except Exception as e:
        print("Error al obtener respuesta de OpenAI:", e)
        return None




def create_docx(content, filename):
    try:
        doc = Document()
        doc.add_paragraph(content)

        # Guardar el documento como un archivo .docx
        doc.save(filename + '.docx')

        return filename + '.docx'
    except Exception as e:
        print("Error al crear el documento .docx:", e)
        return None



def main():
    while True:
        prompt = input("Escribe tu pregunta (o 'salir' para detener): ")

        if prompt.lower() == "salir":
            break
        
        chatgpt_response = get_chatgpt_response(prompt)
        
        if chatgpt_response:
            document_content = chatgpt_response
            document_filename = input("Introduce un nombre para el documento: ")
            document_path = create_docx(document_content, document_filename)
            
            if document_path:
                print(f"Respuesta guardada en el documento .docx: {document_path}")

if __name__ == "__main__":
    main()
