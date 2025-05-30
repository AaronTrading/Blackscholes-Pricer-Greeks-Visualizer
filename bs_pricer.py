import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Calcule le prix d'une option européenne selon le modèle Black-Scholes.
    
    Paramètres:
    S (float): Prix actuel du sous-jacent
    K (float): Prix d'exercice (strike)
    T (float): Temps avant maturité (en années)
    r (float): Taux d'intérêt sans risque
    sigma (float): Volatilité annualisée
    option_type (str): Type d'option ("call" ou "put")
    
    Retourne:
    float: Prix de l'option
    """
    # Calcul des paramètres d1 et d2
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Calcul du prix selon le type d'option
    if option_type.lower() == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type.lower() == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Le type d'option doit être 'call' ou 'put'")
    
    return price
