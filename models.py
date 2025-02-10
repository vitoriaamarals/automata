from pydantic import BaseModel
from typing import Set, Tuple, Dict, List, Union

# Definição do modelo de dados para Autômato Finito Determinístico (DFA)
class FiniteAutomataDeterministic(BaseModel):
    states: Set[str]  # Conjunto de estados
    input_symbols: Set[str]  # Conjunto de símbolos de entrada
    transitions: Dict[str, Dict[str, str]]  # Função de transição
    initial_state: str  # Estado inicial
    final_states: Set[str]  # Conjunto de estados finais
    word: str  # Palavra a ser testada no autômato

# Definição do modelo de dados para Máquina de Turing Determinística (DTM)
class TuringMachine(BaseModel):
    states: Set[str]  # Conjunto de estados
    input_symbols: Set[str]  # Conjunto de símbolos de entrada
    tape_symbols: Set[str]  # Conjunto de símbolos da fita
    transitions: Dict[str, Dict[str, Tuple[str, str, str]]]  # Função de transição 
    initial_state: str  # Estado inicial
    blank_symbol: str  # Símbolo em branco da fita
    final_states: Set[str]  # Conjunto de estados finais
    word: str  # Palavra a ser testada na máquina de Turing

# Definição do modelo de dados para Autômato com Pilha Determinístico (DPDA)
class PushdownAutomata(BaseModel):
    states: Set[str]  # Conjunto de estados
    input_symbols: Set[str]  # Conjunto de símbolos de entrada
    stack_symbols: Set[str]  # Conjunto de símbolos da pilha
    transitions: Dict[str, Dict[str, Dict[str, Tuple[str, Union[Tuple[str, ...], str]]]]]  # Função de transição
    initial_state: str  # Estado inicial
    initial_stack_symbol: str  # Símbolo inicial da pilha
    final_states: Set[str]  # Conjunto de estados finais
    acceptance_mode: str  # Modo de aceitação (por estado final ou pilha vazia)
    word: str  # Palavra a ser testada no autômato com pilha