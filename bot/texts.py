START = '👋 Olá! Bem-vindo ao BOT de Controle de Gastos\n\n'
START_INACTIVE = 'Seu acesso está Inativo 🚫\n\nEntre em contato com o suporte para liberar. 👊'
START_ACTIVE = 'Seu acesso está Ativo ✅\n\nEnvie `Gastei 50.40 no mercado` para registra uma nova despesa. 💲'
ERROR_MESSAGE = '🤖 Ocorreu um erro inesperado. Por favor, tente novamente mais tarde.'
UNKNOWN_COMMAND = '❓ Comando não reconhecido. Use /ajuda.'
UNKNOWN_MESSAGE = '🤖 Não entendi. Tente /ajuda.'
EDITED_MESSAGE = '🤖 Mensagem editada. Não posso processar mensagens editadas.'
SUPPORT = '🤖 Entre em contato com o [suporte](https://t.me/Cordeirovsk) para esclarecer sua dúvida'

NOT_ACCESS = '❌ Você não possui acesso para ativar usuários.'

ACTIVE_INSTRUCTIONS = 'Use: /ativar <telegram_id>'

USER_NOTFOUND = '❕ Usuário não encontrado.'
USER_NOTREGISTRED = '❌ Você ainda não está registrado. Use /start primeiro.'
USER_INACTIVE = '🔒 Seu acesso está inativo. Entre em contato para liberar.'
USER_SUCCESS = '✅ {name} ativado.'

EXPENSE_INSTRUCTIONS = '❌ Formato inválido. Use: Gastei 44.50 no Mercado'
EXPENSE_SUCCESS = '✅ Maravilha {name}!\n\n💲 {value:.2f} reais com {description}\n\nSeu gasto foi registrado com sucesso!'
EXPENSE_NONE = "✅ Nenhum gasto registrado no mês de {month}."

MONTH_SUMMARY = "📊 Gasto do mês ({month}): R${total:.2f}"

CALLBACK_ADD_EXPENSE = '💡 Para registar um novo gasto, basta me enviar:\n\n`Gastei <valor> <descricao>`'
CALLBACK_SUMMARY = '💡 Para visualizar seus gastos, basta me enviar:\n\n/resumo\n\nVocê pode enviar `/resumo junho` para mudar o mês de consulta.'
CALLBACK_SUMMARY_CHART = '💡 Para visualizar seus gastos em gráfico, basta me enviar:\n\n/grafico\n\nVocê pode enviar `/grafico pizza junho` para mudar o estilo de gráfico e mês de consulta.'

CALCULATE_INSTRUCTIONS = '💡 Para calcular um gasto, basta me enviar:\n\n`/calcular <seu-salário>`\n\nVocê pode enviar `/calcular 5.000` para calcular o quanto sobrou do seu salário.'
CALCULATE_INVALID = '❌ Formato inválido. Use: /calcular 5.000'
REMAINING_SALARY_POSITIVE = '💰 Seu salário informado é de R$ {salary:.2f}\n\n💱 Seu gasto no mês de {month} foi de R$ {total:.2f}\n\n💲 Seu salário restante é: R$ {remaining:.2f}'
REMAINING_SALARY_NEGATIVE = '💰 Seu salário informado é de R$ {salary:.2f}\n\n💱 Seu gasto no mês de {month} foi de R$ {total:.2f}\n\n❗ Você está negativo em: R$ {remaining:.2f}'