import numpy as np
import matplotlib.pyplot as plt
from bs_pricer import black_scholes_price
from greeks import calculate_greeks

def plot_payoff(K, option_type="call"):
    """
    Trace le payoff à maturité d'une option.
    
    Paramètres:
    K (float): Prix d'exercice (strike)
    option_type (str): Type d'option ("call" ou "put")
    """
    S_range = np.linspace(0, 2*K, 1000)
    
    if option_type.lower() == "call":
        payoff = np.maximum(S_range - K, 0)
    else:
        payoff = np.maximum(K - S_range, 0)
    
    plt.figure(figsize=(10, 6))
    plt.plot(S_range, payoff, 'b-', label=f'Payoff {option_type}')
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=K, color='r', linestyle='--', alpha=0.5, label='Strike')
    plt.xlabel('Prix du sous-jacent (S)')
    plt.ylabel('Payoff')
    plt.title(f'Payoff à maturité - {option_type.upper()}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

def plot_greek_vs_spot(S_range, K, T, r, sigma, greek_name="delta", option_type="call"):
    """
    Trace l'évolution d'une grecque en fonction du prix du sous-jacent.
    
    Paramètres:
    S_range (array): Plage de prix du sous-jacent
    K (float): Prix d'exercice (strike)
    T (float): Temps avant maturité (en années)
    r (float): Taux d'intérêt sans risque
    sigma (float): Volatilité annualisée
    greek_name (str): Nom de la grecque à tracer ("delta" ou "vega")
    option_type (str): Type d'option ("call" ou "put")
    """
    greek_values = []
    
    for S in S_range:
        greeks = calculate_greeks(S, K, T, r, sigma, option_type)
        greek_values.append(greeks[greek_name.lower()])
    
    plt.figure(figsize=(10, 6))
    plt.plot(S_range, greek_values, 'b-', label=f'{greek_name.upper()} - {option_type.upper()}')
    plt.axvline(x=K, color='r', linestyle='--', alpha=0.5, label='Strike')
    plt.xlabel('Prix du sous-jacent (S)')
    plt.ylabel(f'{greek_name.upper()}')
    plt.title(f'Évolution du {greek_name.upper()} en fonction du prix du sous-jacent')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
