import numpy as np
from scipy.stats import norm

def calculate_greeks(S, K, T, r, sigma, option_type="call"):
    """
    Calcule les grecques pour une option européenne selon le modèle Black-Scholes.
    
    Paramètres:
    S (float): Prix actuel du sous-jacent
    K (float): Prix d'exercice (strike)
    T (float): Temps avant maturité (en années)
    r (float): Taux d'intérêt sans risque
    sigma (float): Volatilité annualisée
    option_type (str): Type d'option ("call" ou "put")
    
    Retourne:
    dict: Dictionnaire contenant les grecques (delta, gamma, vega, theta, rho)
    """
    # Calcul des paramètres d1 et d2
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Calcul des grecques selon le type d'option
    if option_type.lower() == "call":
        delta = norm.cdf(d1)
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) 
                - r * K * np.exp(-r * T) * norm.cdf(d2))
        rho = K * T * np.exp(-r * T) * norm.cdf(d2)
    elif option_type.lower() == "put":
        delta = norm.cdf(d1) - 1
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) 
                + r * K * np.exp(-r * T) * norm.cdf(-d2))
        rho = -K * T * np.exp(-r * T) * norm.cdf(-d2)
    else:
        raise ValueError("Le type d'option doit être 'call' ou 'put'")
    
    # Grecques communes aux calls et puts
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * np.sqrt(T) * norm.pdf(d1)
    
    return {
        "delta": delta,
        "gamma": gamma,
        "vega": vega,
        "theta": theta,
        "rho": rho
    }
