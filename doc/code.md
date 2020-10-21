---
title: Informações para o TCC - Isabela

papersize: a4
fontsize: 10pt
geometry:
- top=30mm
- left=20mm
---

# Modelos termodinâmicos de acordo com o modelo CALPHAD

Neste trabalho usaremos modelos para fases do tipo solução e fases estequiométricas, descritos a seguir.

## Fases do tipo solução

A energia molar de Gibbs de uma fase to tipo solução é 
$$
G^\phi_m = G^\phi_\text{ref} + G^\phi_\text{id} + G^\phi_\text{ex}
$$
sendo $G^\phi_\text{ref}$ a energia molar de Gibbs de referência:
$$
G^\phi_\text{ref} = x_\text{Mo}^\phi {^\text{°}}G^\phi_\text{Mo} + 
 x^\phi_\text{Zr} {^\text{°}}G^\phi_\text{Zr}
$$
onde $x_i^\phi$ é a fração molar do elemento $i$ na fase $\phi$ e ${^\text{°}}G^\phi_i$ a energia molar de Gibbs do elemento $i$ puro em relação ao estado de referência escolhido. $G^\phi_\text{id}$ a energia molar de Gibbs ideal:
$$
G^\phi_\text{id} = R T \left( 
x^\phi_\text{Mo} \ln x^\phi_\text{Mo} + 
x^\phi_\text{Zr} \ln x^\phi_\text{Zr}
\right)
$$
sendo $R=8,31451\,$J/mol/K e $T$ a temperatura absoluta. Finalmente, $G^\phi_\text{ex}$ a energia molar de Gibbs de excesso:
$$
G^\phi_\text{ex} = x^\phi_\text{Mo} x^\phi_\text{Zr}
\left[
L_0^\phi + L_1^\phi (x^\phi_\text{Mo} - x^\phi_\text{Zr})
+
L_2^\phi (x^\phi_\text{Mo} - x^\phi_\text{Zr})^2 + \ldots
\right]
$$
onde os parâmetros $L_i^\phi$ são geralmente funções lineares da temperatura na forma
$$
L_i^\phi = A_i^\phi + B_i^\phi T
$$
sendo que frequentemente adota-se $B_i^\phi=0$.

## Fases estequiométricas

O modelo para fases estequiométricas é parecido com o modelo de fases do tipo solução, mas o termo ideal se anula.

# Descrição termodinâmica do sistema Mo-Zr

Segundo (KAUFMAN e BERNSTEIN, 1970), o sistema binário Mo-Zr é descrito usando o conjunto de equações abaixo para as fases de equiĺíbrio. 

## Fases do tipo solução

Neste caso, o estado padrão de referência para os elementos puros é sempre a fase líquida e todas as fases são descritas como soluções regulares, ou seja, apenas os termos $L_0^\phi$ estão presentes.

### Líquido

Como o líquido é a fase de referência para os elementos puros, temos que
$$
G^\text{liq}_\text{ref} = 0
$$
e o termo de excesso é 
$$
G^\text{liq}_\text{ex} = 1512 x_\text{Mo}^\text{liq} x_\text{Zr}^\text{liq}
$$

### Fase CCC

$$
{^\text{°}}G^\text{CCC}_\text{Mo} = -5800 + 2 T
$$

$$
{^\text{°}}G^\text{CCC}_\text{Zr} = -4250 + 2 T
$$

$$
G^\text{CCC}_\text{ex} = 6551 x_\text{Mo}^\text{CCC} x_\text{Zr}^\text{CCC}
$$

### Fase HCP

$$
{^\text{°}}G^\text{HCP}_\text{Mo} = -3800+2 T
$$

$$
{^\text{°}}G^\text{HCP}_\text{Zr} = -5280+2.9 T
$$

$$
G^\text{HCP}_\text{ex} = 8981 x_\text{Mo}^\text{HCP} x_\text{Zr}^\text{HCP}
$$

## Fases estequiométricas

### Fase de Laves

Apenas a fase de Laves Mo$_2$Zr é considerada estequiométrica no sistema. A referência para os elementos puros é neste caso a fase HCP, de forma que

$$
{^\text{°}}G^\text{Laves}_\text{Mo} = -3800+2 T
$$

$$
{^\text{°}}G^\text{Laves}_\text{Zr} = -5280+2.9 T
$$

$$
G^\text{Laves}_\text{ex} = -16488 x_\text{Mo}^\text{Laves} x_\text{Zr}^\text{Laves}
$$

# Anexo: códigos

## Algoritmos para a determinação do envoltório convexo e das tielines

_inserir comentários sobre o código_

---

<<< @/../src/convexhull.py


## Definições de modelos de fases segundo o método CALPHAD

_inserir comentários sobre o código_

---

<<< @/../src/thermo.py

## Código para gerar curvas de energia livre molar vs. composição

_inserir comentários sobre o código_

---

<<< @/../src/Gcurves.py

## Código para calcular um diagrama de fases binário

_inserir comentários sobre o código_

---

<<< @/../src/ph_diag.py

## Código auxiliar para a geração de marcadores nos gráficos

_inserir comentários sobre o código_

---

<<< @/../src/markers.py

## Exemplo de um sistema: Mo-Zr (KAUFMAN e BERNSTEIN, 1970)

_inserir comentários sobre o código_

---

<<< @/../src/MoZr.py
