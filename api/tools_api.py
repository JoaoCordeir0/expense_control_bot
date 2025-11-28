import requests

class ToolsApi:

    @staticmethod
    def get_exchange_rate(currency: str):
        response = requests.get(f"https://economia.awesomeapi.com.br/json/last/{currency}-BRL")

        result = response.json()["USDBRL"]

        bid = float(result["bid"])
        high = float(result["high"])
        low = float(result["low"])

        return (
            f"💱 Cotação do {currency}/BRL\n"
            f"• Valor atual: R$ {bid:.2f}\n"
            f"• Mínimo do dia: R$ {high:.2f}\n"
            f"• Máximo do dia: R$ {low:.2f}"
        )
