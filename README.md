# OndasEletromagFDTD


O objetivo deste Projeto é desenvolver um código ou algoritmo que envolve a implementação do algoritmo FDTD (Finite-Difference Time-Domain) para visualização de tensão $V(z,t)$
e corrente $I(z,t)$ (transiente) em uma linha de transmissão sem perdas, baseado nas equações do
telegrafista.

# Executando
Para executar este código é necessário ter o interpretador python instalado, bem como os módulos que serão utilizados no código. É possível instalar os módulos através do comando pip:

pip install matplotlib
pip install numpy

Para executar:
python ondas.py

# Configurando Zl e a fonte de tensão:
Todos os parâmetros são configuráveis no código, Tais como Z0, Zg, Zl, fonte_1 e fonte_2.
Para adotar uma impedância infinita a Zl, basta atribuir Zl = math.inf.
Os demais parâmetros também estão explicados no código.
