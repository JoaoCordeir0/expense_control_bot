START = '👋 Olá! Bem-vindo ao BOT de Controle de Gastos.\n\nPara registrar um gasto, envie: `Gastei <valor> <descricao>`\n\n'
START_INACTIVE = 'Seu acesso está *inativo* no momento. Entre em contato com [suporte](https://t.me/Cordeirovsk) para liberar.'
UNKNOWN_COMMAND = '❓ Comando não reconhecido. Use /ajuda.'
UNKNOWN_MESSAGE = '🤖 Não entendi. Tente /ajuda.'
SUPPORT = '🤖 Entre em contato com o [suporte](https://t.me/Cordeirovsk) para esclarecer sua dúvida'
HELP = """📌 Comandos disponíveis:\n
/start - Inicia a conversa
/resumo - Visualiza os gastos do mês
/grafico - Gera um gráfico com os gastos
/suporte - É disponibilizado o contato para suporte\n
Para registar um novo gasto envie: Gastei <valor> <descricao>\n

↘️ Exemplos de uso:
• /resumo
• /resumo janeiro
• /grafico
• /grafico linha maio
• /grafico pizza agosto
• /grafico barra-horizontal abril
• Gastei 44.50 no Mercado"""

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

STATIC_RESPONSES = {
    'oi': START,
    'opa': START,
    'eae': START,
    'ola': START,
    'saudacoes': START,
    'bom dia': '🌅 Bom dia! Registre um novo gasto ou consulte os existentes.',
    'boa tarde': '🌇 Boa tarde! Registre um novo gasto ou consulte os existentes.',
    'boa noite': '🌃 Boa noite! Registre um novo gasto ou consulte os existentes.',
    'obrigado': '😊 De nada! Se precisar de mais algo, é só mandar mensagem.',
    'obrigada': '💖 Por nada! Estou aqui para ajudar.',
    'valeu': '👍 Valeu você! Manda ver.',
    'tchau': '👋 Até logo! Volte quando quiser.',
    'flw': '✌️ Até logo! Volte quando quiser.',
    'ate mais': '✨ Até mais! Qualquer dúvida, estou aqui.',
    'como vai': '🤖 Eu sou um bot, então estou sempre 100%!',
    'tudo bem': '🤖 Eu sou um bot, então estou sempre 100%!',
    'quem e voce': '🤖 Sou seu assistente virtual! Meu objetivo é te ajudar a organizar seus gastos.',
}