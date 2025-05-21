def predict_next_match(results):
    if not results:
        return "No se encontraron partidos recientes."

    total_matches = len(results)
    wins = 0
    total_goals = 0

    for match in results:
        if match['intHomeScore'] is None or match['intAwayScore'] is None:
            continue
        home = match['strHomeTeam']
        away = match['strAwayTeam']
        home_score = int(match['intHomeScore'])
        away_score = int(match['intAwayScore'])

        # Contamos victoria si fue el ganador
        if (home_score > away_score and match['strHomeTeam'] == match['strTeam']) or \
        (away_score > home_score and match['strAwayTeam'] == match['strTeam']):
            wins += 1

        if match['strTeam'] == home:
            total_goals += home_score
        else:
            total_goals += away_score

    avg_goals = round(total_goals / total_matches, 2)
    win_ratio = wins / total_matches

    if win_ratio >= 0.6:
        confidence = "alta probabilidad de victoria"
    elif win_ratio >= 0.4:
        confidence = "partido parejo"
    else:
        confidence = "riesgo de derrota"

    return f"Victorias recientes: {wins}/{total_matches}\nPromedio de goles: {avg_goals}\n➡️ {confidence.capitalize()}."
