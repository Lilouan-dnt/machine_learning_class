import os
import subprocess

def generate_pdf():
    # Contenu LaTeX de la fiche avec mise en page optimisée
    latex_content = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{amsmath, amssymb, bm}
\usepackage{geometry}
\geometry{hmargin=2cm, vmargin=2.5cm}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{fancyhdr}

\pagestyle{fancy}
\fancyhf{}
\rhead{FYS-2009 - Introduction to Plasma Physics}
\lhead{Fiche de synthèse}
\cfoot{\thepage}

\setlength{\parindent}{0pt}
\setlength{\parskip}{1em}

\begin{document}

\begin{center}
    \Large\textbf{FICHE DE SYNTHÈSE : PHYSIQUE DES PLASMAS (FYS-2009)}
\end{center}
\vspace{0.5cm}

\section*{1. Constantes et Équivalences Fondamentales}
\renewcommand{\arraystretch}{1.5}
\begin{tabularx}{\textwidth}{l l X l}
\toprule
\textbf{Grandeur / Constante} & \textbf{Symbole} & \textbf{Valeur numérique} & \textbf{Unité SI} \\
\midrule
Charge élémentaire & $e$ & $1{,}602 \times 10^{-19}$ & $\text{C}$ \\
Permittivité du vide & $\epsilon_0$ & $8{,}854 \times 10^{-12}$ & $\text{F}\cdot\text{m}^{-1}$ \\
Perméabilité du vide & $\mu_0$ & $4\pi \times 10^{-7} \approx 1{,}257 \times 10^{-6}$ & $\text{H}\cdot\text{m}^{-1}$ \\
Constante de Boltzmann & $k_B$ & $1{,}381 \times 10^{-23}$ & $\text{J}\cdot\text{K}^{-1}$ \\
Masse de l'électron & $m_e$ & $9{,}109 \times 10^{-31}$ & $\text{kg}$ \\
Masse du proton & $m_p$ & $1{,}673 \times 10^{-27}$ ($m_p/m_e \approx 1836$) & $\text{kg}$ \\
Conversion thermique & $1\text{ eV}$ & $1{,}602 \times 10^{-19}\text{ J} \iff 11\,600\text{ K}$ & $T_{\text{eV}} = \frac{T_K}{11600}$ \\
\bottomrule
\end{tabularx}

\vspace{0.5cm}
\section*{2. Équations de Maxwell \& Électrodynamique}
\begin{itemize}
    \item \textbf{Loi de Gauss (Électricité)} : $\nabla \cdot \bm{E} = \frac{\rho}{\epsilon_0}$
    \item \textbf{Loi de Gauss (Magnétisme)} : $\nabla \cdot \bm{B} = 0$
    \item \textbf{Loi de Faraday (Induction)} : $\nabla \times \bm{E} = -\frac{\partial \bm{B}}{\partial t}$
    \item \textbf{Loi d'Ampère-Maxwell} : $\nabla \times \bm{B} = \mu_0 \left( \bm{J} + \epsilon_0 \frac{\partial \bm{E}}{\partial t} \right)$
    \item \textbf{Sources microscopiques discrètes} : 
    $$ \rho(\bm{x},t) = \sum_{i=1}^N q_i \delta(\bm{x}-\bm{x}_i), \qquad \bm{J}(\bm{x},t) = \sum_{i=1}^N q_i \bm{v}_i \delta(\bm{x}-\bm{x}_i) $$
    \item \textbf{Force de Lorentz} : $\bm{F} = m \frac{d\bm{v}}{dt} = q(\bm{E} + \bm{v} \times \bm{B})$
    \item \textbf{Équation d'onde (vide)} : $\nabla^2 \bm{E} - \frac{1}{c^2} \frac{\partial^2 \bm{E}}{\partial t^2} = \bm{0} \quad \text{avec } c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}$
\end{itemize}

\newpage
\section*{3. Bilans Globaux et Lois de Conservation}
\begin{itemize}
    \item \textbf{Conservation de la charge} :
    $$ \frac{\partial \rho}{\partial t} + \nabla \cdot \bm{J} = 0 \implies \frac{dQ_{\text{tot}}}{dt} = 0 \quad (\text{système fermé}) $$
    \item \textbf{Théorème de Poynting} :
    $$ \frac{d}{dt}\int_{V}\frac{1}{2}\left(\epsilon_{0}E^{2}+\frac{B^{2}}{\mu_{0}}\right)dV = -\int_{V}\bm{E}\cdot\bm{J}~dV - \frac{1}{\mu_{0}}\oint_{\partial V}(\bm{E}\times\bm{B})\cdot d\bm{S} $$
    \item \textbf{Vecteur de Poynting} : $\bm{S}_P = \frac{\bm{E} \times \bm{B}}{\mu_0}$
\end{itemize}

\section*{4. Écrantage de Debye \& Critères du Plasma}
\begin{itemize}
    \item \textbf{Distribution de Boltzmann} : $n_e(r) \approx n_0\left(1 + \frac{e\phi(r)}{k_B T_e}\right)$
    \item \textbf{Équation de Poisson linéarisée} : $\nabla^2 \phi(r) = \frac{\phi(r)}{\lambda_D^2} - \frac{Q}{\epsilon_0}\delta(\bm{r})$
    \item \textbf{Longueur de Debye} : $\lambda_D = \sqrt{\frac{\epsilon_0 k_B T_e}{n_0 e^2}}$
    \item \textbf{Potentiel écranté} : $\phi(r) = \frac{Q}{4\pi\epsilon_0 r}\exp\left(-\frac{r}{\lambda_D}\right)$
    \item \textbf{Pulsation plasma électronique} : $\omega_{pe} = \sqrt{\frac{n_0 e^2}{m_e \epsilon_0}}$
    \item \textbf{Critères d'existence d'un plasma} :
    \begin{enumerate}
        \item $\mathcal{L} \gg \lambda_D$ (Quasi-neutralité)
        \item $N_D = \frac{4}{3}\pi n_0 \lambda_D^3 \gg 1$ (Comportement collectif)
        \item $\omega_{pe} > \nu_{en}$ (Dominance sur les collisions)
    \end{enumerate}
\end{itemize}

\newpage
\section*{5. Dynamique Particulaire en Champs Statiques}
\begin{itemize}
    \item \textbf{Décomposition de vitesse} : $\bm{v}_\parallel = (\bm{v}\cdot\hat{\bm{B}})\hat{\bm{B}} \quad \text{et } \bm{v}_\perp = \hat{\bm{B}} \times (\bm{v} \times \hat{\bm{B}})$
    \item \textbf{Angle d'attaque (Pitch angle)} : $\alpha = \arctan\left(\frac{v_\perp}{v_\parallel}\right)$
    \item \textbf{Pulsation cyclotron} : $\Omega_c = \frac{|q|B}{m}$
    \item \textbf{Rayon de Larmor} : $r_c = \frac{v_\perp}{\Omega_c} = \frac{m v_\perp}{|q|B}$
    \item \textbf{Centre-guide} : $\bm{r}(t) = \bm{x}_c(t) + \bm{r}_c(t) \quad \text{avec } \frac{d^2\bm{r}_c}{dt^2} + \Omega_c^2 \bm{r}_c = \bm{0}$
    \item \textbf{Moment magnétique} : $\bm{\mu} = -\frac{m v_\perp^2}{2B}\hat{\bm{B}}$
    \item \textbf{Aimantation et Courant lié} : $\bm{\mathcal{M}} = n\bm{\mu} \implies \bm{J}_{\mathcal{M}} = \nabla \times \bm{\mathcal{M}}$
\end{itemize}

\vspace{0.5cm}
\section*{6. Boîte à Outils Mathématique}
\begin{itemize}
    \item \textbf{Identités d'ordre 2} : $\nabla \cdot (\nabla \times \bm{A}) = 0 \quad \text{et} \quad \nabla \times (\nabla \phi) = \bm{0}$
    \item \textbf{Double rotationnel} : $\nabla \times (\nabla \times \bm{A}) = \nabla(\nabla \cdot \bm{A}) - \nabla^2 \bm{A}$
    \item \textbf{Formule BAC-CAB} : $\bm{a} \times (\bm{b} \times \bm{c}) = \bm{b}(\bm{a}\cdot\bm{c}) - \bm{c}(\bm{a}\cdot\bm{b})$
    \item \textbf{Divergence d'un produit vectoriel} : $\nabla \cdot (\bm{A} \times \bm{B}) = \bm{B} \cdot (\nabla \times \bm{A}) - \bm{A} \cdot (\nabla \times \bm{B})$
    \item \textbf{Théorème de Green-Ostrogradski} : $\int_V (\nabla \cdot \bm{A})\,dV = \oint_{\partial V} \bm{A}\cdot d\bm{S}$
    \item \textbf{Règle de Leibniz} : $\int_V \frac{\partial f}{\partial t} \, dV = \frac{d}{dt} \int_V f \, dV$
\end{itemize}

\end{document}
"""

    filename_tex = "fiche_plasma.tex"
    
    # Écriture du fichier .tex
    with open(filename_tex, "w", encoding="utf-8") as f:
        f.write(latex_content)
    
    print(f"Fichier '{filename_tex}' généré avec succès.")

    # Tentative de compilation avec pdflatex
    try:
        print("Lancement de la compilation PDF...")
        # L'option -interaction=nonstopmode évite que le script bloque s'il y a un warning LaTeX
        subprocess.run(["pdflatex", "-interaction=nonstopmode", filename_tex], check=True)
        print("Compilation terminée. Le fichier 'fiche_plasma.pdf' est prêt.")
    except FileNotFoundError:
        print("\nErreur : 'pdflatex' n'est pas installé ou n'est pas dans le PATH.")
        print("Tu peux utiliser le fichier .tex généré et le compiler sur Overleaf.")
    except subprocess.CalledProcessError:
        print("\nErreur lors de la compilation LaTeX. Vérifie le log généré.")

if __name__ == "__main__":
    generate_pdf()
