
# Aula 2 - Diferenças Finitas
## Método FTCS (Foward time centered spaces)  

Assim:  

$\dfrac{u_j^{n+1} - u_j^{n}}{\Delta t}$ = $-v \dfrac{u_{j+1}^{n} - u_{j-1}^{n}}{2 \Delta x}$  

$\boxed{u_j^{n+1} = u_j^n - \dfrac{v\Delta t}{2 \Delta x} \left(u_{j+1}^{n} - u_{j-1}^{n}\right)}$  

## Análise de estabilidade de Von Neumann  
-  Erros sistemáticos - devido ao **método**  
-  Erros numéricos - devido á precisão usada  
  
Para erros numéricos:  

$\varepsilon_{j}^{n} = N_j^n - n_j^n$ , onde  

$N_j^n$ é a solução numérica (aproximadamente) e $n_j^n$ a solução exata.

Tanto $N_n^j$ quanto $n_j^n$ satisfazem a mesma equação diferencial de diferença finita. Então $\varepsilon_j^n$ também satisfaz essa equação.  

Tanto para estabilidade numérica quanto para sistêmica, vamos considerar que os coeficentes da equação de diferença finita variam muito lentamente.   

**Expansão em uma série de Fourier.**  

$\boxed{\varepsilon(x, t) = \sum_{-M}^{M} E_m(t)e^{-ik_m x}}$  
com $k_m = \frac{\pi m}{L}$; $m=-M, -M+1,\dots, M$ e $M = \dfrac{L}{\Delta x}$.  

Como a equação é linear, cada termo da série terá que satisfazer a mesma equação de forma que basta analisar apenas 1 termo da série.  

### $\rightarrow$ Estabilidade do método FTCS  

$u_j^n = \xi_j^n e^{ik\Delta x}$  

$k$ é o vetor de onda e $\xi$ é um número complexo que depende apenas de $k$.  

A dependência temporal é dada por potências de $\xi$. Assim, modos com $|\xi| > 1$ divergem exponencialmente.  

$\xi$ é chamado *fator de amplificação*.  

Estabilidade implica $|\xi| < 1$.  

Substituindo na equação dif. do método FTCS: 

$\dfrac{u_j^{n+1} = u_j^n - \dfrac{v\Delta t}{2 \Delta x} \left(u_{j+1}^{n} - u_{j-1}^{n}\right)}{u_j^n}$  

$\dfrac{\xi_{j}^{n+1} e^{ik_j\Delta x}}{\xi_j^n e^{ik_j\Delta x}} = 1- iv\dfrac{ \Delta t}{\Delta x} sen(k \Delta x)$

Mas nesse caso, $|\xi| > 1$ para qualquer $k$. O método FTCS é instável.  

## Método de LAX  
-  Trocar $u_j^n$ por $\frac{1}{2}\left(u_{j+1}^{n} - u_j^{n}\right)$.  
Neste caso, a análise de estabilidade fornece:  
$\xi = cos(k\Delta x) - i\dfrac{v \Delta t}{\Delta x}sen(k\Delta x)$ e aqui vale $|\xi^2| \le 1$. 

$\Rightarrow$ $\boxed{\dfrac{|v|\Delta t}{\Delta x}\le 1}$ **Condição de Courant**  


#### Diferença entre os métodos  

$\dfrac{u_j^{n+1} - u_j^n}{\Delta t} = -v\left(\dfrac{u_{j+1}^{n} - u_{j-1}^n}{2 \Delta x}\right) + \dfrac{(\Delta x)^2}{\Delta x)^2} \dfrac{u_{j+1}^n - 2u_j^n + u_{j-1}^n}{2 \Delta t}$  

que se traduz em:  

$\dfrac{\partial u}{\partial t} = -v \dfrac{\partial u}{\partial x} + \dfrac{(\Delta x)^2}{2 \Delta t} \dfrac{\partial ^2 u}{ \partial x^2}$  

No método de Lax é introduzido *ad hoc* um termo de difusão! Temos dissipação ou "viscosidade numérica". Como estamos interssados em $k\Delta x \ll 1$ nos dois esquecemos $\rightarrow$ $\xi \approx 1$.  

No FTCS  $k \Delta x \approx 1$ e ele diverge. No LAX a viscosidade previne que isso aconteça.  

# Segunda ordem no tempo  

## Staggered Leapfrog

$\boxed{\dfrac{\partial u}{\partial t} =  - \dfrac{\partial f}{\partial x}}$  

$\rightarrow u_j^{n+1} - u_j^{n-1} = - \dfrac{\Delta t}{\Delta x} \left(f_{j+1}^n - f_{j-1}^n\right)$  

Para o caso que estamos analisando, $f = v \cdot u$ :

$u_j^{n+1} - u_j^{n-1} = -v \dfrac{\Delta t}{\Delta x} \left(u_{j+1}^{n} - u_{j-1}^{n}\right)$

Podemos dividir por $\Delta t$ em ambos os lados e somar um termo $2u_j^n$:

$\dfrac{u_j^{n+1} + 2u_j^n - u_j^{n-1}}{\Delta t} = -v \dfrac{\left(u_{j+1}^{n} + 2u_j^n - u_{j-1}^{n}\right)}{\Delta x}$

$v = \dfrac{\Delta x}{ \Delta t}$

$\boxed{\dfrac{\partial ^2 u}{\partial t^2} = v^2 \dfrac{\partial ^2 u}{\partial x^2}}$

---

# Aula 3: 26/03 - Numerical Recipes

Problemas com conservação de fluxo

$\dfrac{\partial u}{\partial t} = - \dfrac{\partial f}{\partial x}$ 

$u_j^{n+1} - u_j^{n-1} = - \dfrac{\Delta t}{\Delta x} \left(f_{j+1}^n - f_{j-1}^n\right)$ 

Na análise de estabilidade de Von Neumann:  

$u_j^n = \xi^n e^{ik\Delta x}$  

considerando $f = uv$ :

$\xi = -iv\dfrac{ \Delta t}{\Delta x} sen(k \Delta x) \pm \sqrt{1 - \left(\dfrac{v\Delta t}{\Delta x} sen(k\Delta x)\right)}$  

$|\xi|^2 = 1$ para qualquer $v\Delta t \le \Delta x$. 

Para gradientes grandes o método pode ficar instável. Podemos recuperar a estabilidade acoplando as subredes (**memo**: tabuleiro de xadrez) com adição de um termo de viscosidade numérica:  

$+ \eta \left(u_{j+1}^n - 2u_j^n + u_{j-1}^n\right)$ com  $\eta \ll 1$.

## Método de Lax-Wendroff de 2 passos 

- Método Lax (média de $u$) + passos intermediários  

$u_{j + 1/2}^{n + 1/2} = \dfrac{1}{2}\left(u_{j+1}^n + u_j^n\right) - \dfrac{\Delta t}{\Delta x}(f_{j+1}^n) - f_{j}^n$  

Podemos obter os **fluxos** intermediários:  

$f_{j + 1/2}^{n + 1/2}$ e $f_{j - 1/2}^{n + 1/2}$  

$u_{j+1}^n = u_j^n - \dfrac{\Delta t}{\Delta x}\left(f_{j + 1/2}^{n + 1/2} - f_{j - 1/2}^{n + 1/2}\right)$ 

Considerando $f = vu$ e definindo $\alpha = \dfrac{v\Delta t}{\Delta x}$.  

$u_{j+1}^n = u_j^n - \alpha\left[\dfrac{1}{2}\left(u_{j+1}^n - u_j^n\right) - \dfrac{\alpha}{2}\left(u_{j+1}^n - u_j^n\right) - \dfrac{1}{2}\left(u_{j}^n - u_j^{n-1}\right) - \dfrac{\alpha}{2}\left(u_{j}^n - u_{j-1}^n\right) \right]$  

A análise da estabilidade fornece  

$\xi = 1 -i\alpha sen(k\Delta x) - \alpha^2 \left(1-cosk\Delta x\right)$  
$|\xi|^2 = 1 -\alpha^2(1-\alpha^2)(1-cos(k\Delta x))$  

$\rightarrow$ Estável para $\alpha ^2 \le 1$  

$\boxed{v\Delta t \le \Delta x}$  

Temos $|\xi|^2 \le 1$ quando $\alpha = 1$. Para $\alpha = 1$ , $|\xi|^2 = 1.$.  

 **Recomendação:** usar o staggered leapfrog sempre que possível.
### Equação de Difusão  

$\dfrac{\partial u}{\partial t}  = \dfrac{\partial}{\partial x} \left(D \dfrac{\partial u}{\partial x}\right)$. 

Pode

 Poderíamos considerar o fluxo para $f = - D\dfrac{\partial u}{\partial x}$, mas vamos tratar esse problema separadamente.  

 Considere $D = \text{cte}$. Então:  

 $\dfrac{\partial u}{\partial t} = D\dfrac{\partial^2 u}{\partial x^2}$ 

 ### FTCS

 $\dfrac{u_j^{n+1} -  u_j^{n}}{\Delta t} = D \left[\dfrac{u_{j+1}^n - 2u_{j}^n + u_{j-1}^n}{(\Delta x)^2}\right]$   
 
 Análise de estabilidade retorna que:

 $\xi  = 1 - \dfrac{4D \Delta t}{\Delta x}sen^2(\dfrac{k \Delta x}{2})$. Desse modo, $|\xi|^2 \le 1 \Rightarrow \dfrac{2D \Delta t}{(\Delta x)^2} \le 1$ 

 $\Delta t \le \dfrac{(\Delta x)^2}{2D}$ 

 **Tempo característico de Difusão**  

 $\tau \approx \dfrac{\lambda^2}{D}$  

onde $\lambda$ é a **escala espacial** envolvida. "Difunde $\lambda$ num intervalo de tempo $\tau$. Em geral, $\lambda \gg \Delta x$ para ter estabilidade:  

$(\Delta t)_{max} = \dfrac{(\Delta x)^2}{2D}$

## Método Completamente Implícito

- Hipótese: $\dfrac{\partial u}{\partial t}$ é  Desprezível
  
### "Equilíbrio Espacial"  

$D \dfrac{\partial ^2 u}{\partial x^2} \approx 0$.  

Isto funciona para *escalas pequenas*.  

Aqui estamos calculando a parte espacial no tempo futuro.  

$\dfrac{u_j^{n+1} -  u_j^{n}}{\Delta t} =  D \left[\dfrac{u_{j+1}^{n+1} - 2u_{j}^{n+1} + u_{j-1}^{n+1}}{(\Delta x)^2}\right]$

Temos então um conjunto de equações algébricas para **cada passo de tempo**.  

$u_j^n = -\alpha u_{j-1}^{n+1} + (1+2\alpha)u_j^{n+1} - \alpha u_{j+1}^{n+1}$  

Para $j =0,1,2, \dotsm J-1$  
As condições de contornos são dadas para $j=0$ e $j=J$

### Estabilidade  

$\xi = \dfrac{1}{1 + 4\alpha sen^(\dfrac{k\Delta x}{2})}$  o que implica que $|\xi| \le 1 \forall \Delta t$.  

Conseguimos chegar a um tempo $t$ grande usando $\Delta t$ grande, **mas** $x$ fica "congelado".  

## Método de Crank-Nicholson  

$\dfrac{u_j^{n+1} -  u_j^{n}}{\Delta t} = \dfrac{D}{2} \left[\dfrac{u_{j+1}^{n+1} - 2u_{j}^{n+1} + u_{j-1}^{n+1}}{(\Delta x)^2} + \dfrac{u_{j+1}^{n} -2u_j^n + u_{j-1}^n}{(\Delta x)^2}\right]$  

os dois estão centrados em $n + \frac{1}{2}$. São de 2ª ordem no tempo e no espaço.


## Equação de Schrödinguer  

$i\dfrac{\partial \psi}{\partial t} = -\dfrac{\partial^2 \psi}{\partial x^2} + V(x)\psi$. 

Fazendo um esquema implícito de 1ª ordem no tempo o sistema tem a estabilidade ok mas a evolução temporal não é unitária como exigido pela mecânica quântica: 

$\int_{-\infty}^{+\infty}|\psi|^2dx \ne 1$.  

A solução então é escrever em termos de **operadores matriciais** e fazer evolução temporal de acordo:  

$i\dfrac{\partial \psi}{\partial t} = \hat{H}\psi$  

$\psi(x, t) = \psi(x, 0)e^{-i\hat{H}t}$  com $\hat{H} = \left(-\dfrac{\partial^2}{\partial x^2} + V(x) \right)$ 

### Fórmula de Cauley  
- Diferença finita **unitária**  

$e^{-i \hat{H}t} \approx \dfrac{1 - \frac{1}{2}iH\Delta t}{1 + \frac{1}{2}iH\Delta t}$  

Aplicando ao $\psi$:

$(1 + \frac{1}{2}iH\Delta t)\psi_{j}^{n+1} = (1 - \frac{1}{2}iH\Delta t) \psi_j^n$  

Devemos usar diferenças centradas em $x$ para $\hat{H}$.