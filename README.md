# Sistema de Predição de Preferência de Gênero de Filme com Redes Neurais

## Descrição
Este projeto explora redes neurais do tipo Single Layer Perceptron (SLP) para prever preferências de gênero de filme de usuários baseado em características pessoais. O relatório detalha a implementação e os resultados alcançados, demonstrando a aplicabilidade dessas redes em tarefas de classificação.

## Funcionalidades
- **Método 1**: Classificação em quatro grupos usando dois neurônios.
- **Método 2**: Classificação detalhada com quatro neurônios, cada um representando uma preferência específica.

## Tecnologias Utilizadas
- Python
- Implementações específicas de rede neural de perceptron.

## Dataset
- **Origem**: Dados improvisados, não provenientes de bases de dados públicas.
- **Atributos**: Problemas cardíacos, senso de humor, empatia, gênero, idade, entre outros.

## Estrutura da Rede Neural
- Implementações com dois e quatro neurônios.
- Uso de função de ativação do tipo degrau.

## Resultados
- Acurácias de 69.23% e 61.53% para os dois métodos.
- Discussão sobre a não linearidade do dataset e a proposta de implementar um Multi Layer Perceptron para melhorar os resultados.

### Pré-requisitos
- Python 3.x

### Instalação
- Nenhuma instalação de biblioteca adicional necessária.

### Execução
- `python método1_4_sl_perceptrons_4_classes.py`
- `python método2_perceptron_sl_duas_saídas.py`

