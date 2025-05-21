from discord.ext import commands
from services import get_last_results
from predictor import predict_next_match

@bot.command(name='predecir')
async def predecir(ctx, *, team_name):
    await ctx.send(f"🔍 Buscando datos para {team_name}...")
    team, results = get_last_results(team_name)

    if team is None:
        await ctx.send("❌ No se encontró el equipo.")
        return

    prediction = predict_next_match(results)
    await ctx.send(f"🔮 Predicción para {team['strTeam']}:\n{prediction}")
