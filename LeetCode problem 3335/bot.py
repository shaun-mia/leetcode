from telegram import Update, ChatMemberUpdated
from telegram.ext import ApplicationBuilder, ContextTypes, ChatMemberHandler

# Manager list
manager_list = ["@manager1", "@manager2", "@manager3", "@manager4", "@manager5"]
manager_index = 0
client_queue = []

# Function to detect new members
async def new_member_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global manager_index
    chat_member: ChatMemberUpdated = update.chat_member

    # Detect only if someone joins the group (not leaves)
    if chat_member.new_chat_member.status == "member":
        user = chat_member.from_user
        username = f"@{user.username}" if user.username else f"{user.full_name}"

        if username not in client_queue:
            client_queue.append(username)

        # When we have 5 clients, assign a manager
        if len(client_queue) >= 5:
            assigned_clients = client_queue[:5]
            client_queue[:] = client_queue[5:]
            assigned_manager = manager_list[manager_index]

            message = (
                f"👤 New clients assigned to {assigned_manager}:\n"
                f"{' '.join(assigned_clients)}\n\n"
                f"📞 Please contact {assigned_manager} for support."
            )
            await context.bot.send_message(chat_id=chat_member.chat.id, text=message)
            manager_index = (manager_index + 1) % len(manager_list)

# Set up bot
app = ApplicationBuilder().token("7844034403:AAGK5fJPEaLG-QlpH1moBR6baGuvRWLVcko").build()
app.add_handler(ChatMemberHandler(new_member_handler, ChatMemberHandler.CHAT_MEMBER))
app.run_polling()
