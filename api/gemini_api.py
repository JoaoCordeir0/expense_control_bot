import os
import json
from google import genai
from google.genai import types

class GeminiApi:
    """
    A class to interact with the Gemini API.
    """

    client = None
    model = None

    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = "gemini-2.0-flash"
        
    def extract_info_from_user_text(self, user_text: str) -> str:
        """
        Extracts information from the user's text using the Gemini API.

        Args:
            user_text (str): The text input from the user.

        Returns:
            str: The response text from the Gemini API.
        """
        prompt = """
        Você é um assistente para controle financeiro, você deve extrair informações financeiras do texto e retornar as seguintes informações:
        - Valor total gasto
        - Descritivo do gasto
        - Se é parcelado ou à vista
        - Quantidade de parcelas

        Retorne em formato JSON, com as chaves: "total_value", "description", "is_installments", "quantity_installments".
        Exemplo de resposta:
        {
            "total_value": 100.00,
            "description": "Compra de supermercado",
            "is_installments": false,
            "quantity_installments": 0
        }
        """
        
        response = self.client.models.generate_content(
            model=self.model,
            config=types.GenerateContentConfig(
                system_instruction=prompt,
                max_output_tokens=1000
            ),
            contents=user_text
        )
        
        try:
            return json.loads(response.text.replace("```json", "").replace("```", "").strip())
        except:
            return "Falha ao processar a resposta do Gemini API."
        
    def create_response_with_user_message(self, user_text) -> str:
        """
        Creates a response based on the user's message using the Gemini API.

        Args:
            user_text (str): The text input from the user.

        Returns:
            str: The response text from the Gemini API.
        """
        prompt = f"""
        Você é um assistente para controle financeiro.        
        Responda de forma clara e objetiva, fornecendo uma resposta curta.
        Jamais recomende outros serviços financeiros, como bancos, cartões de crédito ou investimentos.
        Se o usuário parecer estar perdido ou confuso, ofereça ajuda para esclarecer suas dúvidas, diga que ele pode enviar /ajuda para ver os comandos disponíveis.
        Use emojis para tornar a resposta mais amigável e envolvente, mas lembresse que você é um bot.
        A seguir os comandos disponíveis para você ajudar o usuário, não informe nenhum alem desses comandos:
        /start - Inicia uma conversa
        /resumo - Mostro seus gastos do mês
        /grafico - Gero um gráfico com os seus gastos
        /calcular <seu-salário> - Calculo o quanto sobrou do seu salário
        /suporte - Mando o contato do suporte
        Para registar um novo gasto, basta enviar: `Gastei <valor> <descricao> <parcelas (opcional)>`
        Exemplos de uso:
        • /resumo
        • /resumo janeiro
        • /calcular 5.000 maio
        • /grafico
        • /grafico linha maio
        • /grafico pizza agosto
        • /grafico barra-vertical abril
        • Gastei 44.50 no Mercado
        • Gastei 250 reais no restaurante em 4 parcelas
        """
        
        response = self.client.models.generate_content(
            model=self.model,
            config=types.GenerateContentConfig(
                system_instruction=prompt,
                max_output_tokens=200
            ),
            contents=user_text
        )
        
        return response.text.strip()
