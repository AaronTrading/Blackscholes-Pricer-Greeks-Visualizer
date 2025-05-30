# Black-Scholes Pricer & Greeks Visualizer

Ce projet permet de calculer le prix d'options européennes selon le modèle Black-Scholes et de visualiser leurs grecques.

## Fonctionnalités

- Calcul du prix d'options européennes (call/put)
- Calcul des grecques (delta, gamma, vega, theta, rho)
- Visualisation du payoff à maturité
- Visualisation de l'évolution des grecques en fonction du prix du sous-jacent

## Formules utilisées

### Prix de l'option

- Call: C = S _ N(d1) - K _ e^(-rT) \* N(d2)
- Put: P = K _ e^(-rT) _ N(-d2) - S \* N(-d1)

où:

- d1 = (ln(S/K) + (r + σ²/2)T) / (σ√T)
- d2 = d1 - σ√T

### Grecques

- Delta (call) = N(d1)
- Delta (put) = N(d1) - 1
- Gamma = N'(d1) / (S _ σ _ √T)
- Vega = S _ √T _ N'(d1)
- Theta (call) = -S _ N'(d1) _ σ / (2√T) - r _ K _ e^(-rT) \* N(d2)
- Theta (put) = -S _ N'(d1) _ σ / (2√T) + r _ K _ e^(-rT) \* N(-d2)
- Rho (call) = K _ T _ e^(-rT) \* N(d2)
- Rho (put) = -K _ T _ e^(-rT) \* N(-d2)

## Installation

1. Clonez ce dépôt
2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

Pour exécuter l'application principale :

```bash
python app.py
```

## Structure du projet

- `bs_pricer.py` : Fonctions de pricing Black-Scholes
- `greeks.py` : Calcul des grecques
- `plot_payoff.py` : Visualisation des payoffs et grecques
- `app.py` : Application principale
- `requirements.txt` : Dépendances du projet

## Capture d'écran

https://media.discordapp.net/attachments/1280431720679870475/1377959762322264084/screen2.png?ex=683adc88&is=68398b08&hm=15e7f4434a2e91daa0c7b14e7deb55639ca8c6ab0eb34100e7e39b384b9e3afa&=&format=webp&quality=lossless&width=1249&height=783
https://media.discordapp.net/attachments/1280431720679870475/1377959762574180524/screen1.png?ex=683adc88&is=68398b08&hm=c760adef8929143e5aa28117e57c77838d577970ae32cc85c24a06c2bf43d41b&=&format=webp&quality=lossless&width=1248&height=785
## Dépendances

- numpy
- scipy
- matplotlib
- streamlit (optionnel)
