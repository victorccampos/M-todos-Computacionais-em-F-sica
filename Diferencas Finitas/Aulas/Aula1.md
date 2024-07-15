# Problemas lineares

$u'' _ d(x) u' + q(x)u = S(x)$  

Por ser linear de 2ª ordem precisamos de duas soluções. Qualquer outra solução pode ser obtida por uma combinação linear destas duas soluções.  

$u(x) = a u_{\alpha_0}(x) + b u_{\alpha_1}(x)$  

**Condinções Iniciais**  
$u(0) = u_0 \ \ u(1)= u_1$  

onde $u_{\alpha_0}$ e $u_{\alpha_1}$ são sol. obtidas pelo *shooting-method* usando parâmetros diferentes.  

Como $u_{\alpha_0}(0)$ = $u_{\alpha_1}(0)$ =$u_0$ $\rightarrow$ $a + b = 1$. Então:  

$u_1 = au_{\alpha_0}(1) + bu_{\alpha_1}(1)$  

$\Rightarrow a = \dfrac{u_{\alpha_1}(1) - u_1}{u_{\alpha_1}(1)- u_{\alpha_0}(1)}$  
$\Rightarrow b = \dfrac{u_1 -u_{u_{\alpha_0}(1)}}{u_{\alpha_1}(1) - u_{\alpha_0}(1)}$.  

## Problema de Sturm-Liouville  

$\left[p(x)u'(x)\right]' + g(x)u(x) = S(x)$  

Quando $S(x) = 0$:  
$q(x) = -r(x) + \lambda \omega(x)$ onde $\lambda$ são os autovalores da equação.  
**Exemplos**: Eq. Bessel, Eq. Legendre, ... 


## Equação de Schrodinger 1D   

$\dfrac{-\hbar}{2m} \dfrac{d^2\phi}{dx^2} + V(x)\phi(x) = E \phi(x)$  

**Método de Numerov**  
#### Diferenças finitas centradas.  

$u(x+h) = u(x) + h \dfrac{du}{dx} + \dfrac{h^2}{2}\dfrac{d^2u}{dx^2} + \dfrac{h}{3!}\dfrac{d^3u}{dx^3} + \cal{O}(h^4)$  

$u(x-h) = u(x) - h \dfrac{du}{dx} + \dfrac{h^2}{2}\dfrac{d^2u}{dx^2} - \dfrac{h^3}{3!}\dfrac{d^3u}{dx^3} + \cal{O}(h^4)$   

$u(x+h) - u(x-h)$ = $2h\dfrac{du}{dx} + \dfrac{2h^3}{3!}\dfrac{d^3u}{dx^3}$  

$\boxed{\dfrac{du}{dx} = \dfrac{u(x+h)-u(x-h)}{2h} + \cal{O}(h^4)}$  

$u(x+h) + u(x-h)$ = $2u(x) + h^2\dfrac{d^2u}{dx^2} + \dfrac{h^4}{4!}\dfrac{d^4u}{dx^4} + \cal{O}(h^6)$  

$\boxed{\dfrac{d^2u}{dx^2} = \dfrac{u(x+h)-2u(x) + u(x-h)}{h^2} + \cal{O}(h^4)}$  

$\Rightarrow \Delta_2 = u'' +\dfrac{2}{h^2}\dfrac{h^4}{4!}u^{(4)}$   

Tendo a equação (1) $u'' = S - qu$, define-se esse $\Delta_2$. De (1):  

$u^{(4)}(x) = \dfrac{d^2}{dx^2} \left[S(x) - q(x)u(x)\right]$  

$u^{(4)}(x) = \dfrac{(S_{i+1} - q_{i+1}u_{i+1}) - 2S_{i} - q_{i}u_{i} + (S_{i-1} - q_{i-1}u_{i-1})}{h^2}$  

$\dfrac{u_{i+1}-2u_i - u_{i-1}}{h^2} = (S_{i} - q_{i}u_{i})  + \dfrac{h^2}{12}\left[\dfrac{(S_{i+1} - q_{i+1}u_{i+1}) - 2(S_{i} - q_{i}u_{i}) + (S_{i-1} - q_{i-1}u_{i-1})}{h^2}\right]$  


# Equações Diferenciais Parciais  

Matematicamente dividimos em 3 tipos:  
- Hiperbólicas: Equação da Onda  
- Parabólicas: Equação da Difusão  
- Elípticas: Equação de Poisson  

Do ponto de vista computacional, é mais conveniente em dividir em:  
- Valores inicias (evolução temporal)  
- Condições de contorno (solução estática)   
  
### Problema de Valor Inicial.  
- Quais  são as variáveis que se propagam no tempo?  
- Qual a equação que rege a evolução temporal?  
- Qual a maior ordem de $\frac{\partial}{\partial t}$  
- **Condiçõies de contorno especiais**:  
  - Dirichlet: Valores nas fronteiras como função do tempo  
  - Von Neumann: Gradientes nas fronteiras
  - Outgoing wave boundary condition  
  
  O grande problema neste caso é a estabilidade numérica das soluções.  

  ### Problema de valores de contorno  
- Quais são as variáveis? 
- Quais equações são satisfeitas?
- Quais são as condições de fronteira? (Dirichlet, Neumman).  
  $\rightarrow$ Foco na eficiência ao invés da estabilidade.  
  $\rightarrow$ O problema se reduz à solução de um grande nº de equações algébricas.  

  **Exemplo:** Equação de Poisson  

  $\boxed{\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} = \rho(x,y)}$  

  #### Solução através de diferenças finitas  
  $u(x_j, y_l) = u_{j,l}$  

  $x_j =x_o + j*\Delta$ com $j = 0,1,2,..., J$  
  $y_j =y_o + l*\Delta$ com $l = 0,1,2,..., L$  

  Conforme vimos:  

  $\dfrac{d^2u}{dx^2} = \dfrac{u_{i+1} -2u_{i} + u_{i-1}}{h}$  

$\dfrac{\partial^2u}{\partial x^2} = \dfrac{u_{j+1, l} -2u_{j, l} + u_{j+1, l}}{\Delta^2}$

$\dfrac{\partial^2u}{\partial y^2} = \dfrac{u_{j, l+1} +2u_{j, l} + u_{j, l-1}}{\Delta^2}$  

$\Rightarrow  \dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2} = \rho(j,l)$  

$\boxed{u_{j+1,l} + u_{j-1, l} + u_{j, l+1} + u_{j, l-1} - 4u_{j,l}= \rho(j,l)}$


Definindo $i = j(L+1) + l$:  

$u_{i+(L+1)} + u_{i-(L+1)} + u_{i+1} + u_{i-1} - 4u_i = \Delta^2 \rho_i$  

Apenas no interior:  
        $j = 1, ..., J-1$
        $l = 1, ..., L-1$  
    
As condições de contorno, j= 0 e J e l=0 e L são incorporadas. Ao lado direito da equação: $\vec{A} \cdot \vec{u} = \vec{b}$.



