from bs_pricer import black_scholes_price
from greeks import calculate_greeks
from plot_payoff import plot_payoff, plot_greek_vs_spot
import numpy as np

def get_float_input(prompt, default_value):
    while True:
        try:
            user_input = input(f"{prompt} [{default_value}]: ").strip()
            if user_input == "":
                return default_value
            return float(user_input)
        except ValueError:
            print("Erreur: Veuillez entrer un nombre valide")

def get_option_type():
    while True:
        option_type = input("Type d'option (call/put) [call]: ").strip().lower()
        if option_type == "":
            return "call"
        if option_type in ["call", "put"]:
            return option_type
        print("Erreur: Le type doit être 'call' ou 'put'")

def main():
    print("\n=== Black-Scholes Pricer & Greeks Visualizer ===\n")
    
    # Saisie des paramètres
    S = get_float_input("Prix actuel du sous-jacent (S)", 100)
    K = get_float_input("Prix d'exercice (K)", 100)
    T = get_float_input("Temps avant maturité en années (T)", 1.0)
    r = get_float_input("Taux d'intérêt sans risque (r)", 0.05)
    sigma = get_float_input("Volatilité annualisée (sigma)", 0.2)
    option_type = get_option_type()
    
    print("\nParamètres choisis:")
    print(f"S = {S:.2f}")
    print(f"K = {K:.2f}")
    print(f"T = {T:.2f}")
    print(f"r = {r:.2%}")
    print(f"sigma = {sigma:.2%}")
    print(f"Type = {option_type.upper()}")
    
    # Calcul du prix
    price = black_scholes_price(S, K, T, r, sigma, option_type)
    print(f"\nPrix de l'option {option_type.upper()}: {price:.4f}")
    
    # Calcul des grecques
    greeks = calculate_greeks(S, K, T, r, sigma, option_type)
    print("\nGrecques:")
    for greek, value in greeks.items():
        print(f"{greek.upper()}: {value:.4f}")
    
    # Visualisation du payoff
    print("\nAffichage du payoff...")
    plot_payoff(K, option_type)
    
    # Visualisation du delta en fonction du spot
    print("\nAffichage de l'évolution du delta...")
    S_range = np.linspace(S * 0.5, S * 1.5, 100)
    plot_greek_vs_spot(S_range, K, T, r, sigma, "delta", option_type)

if __name__ == "__main__":
    main()
