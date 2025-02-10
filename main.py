from fastapi import FastAPI
from pydantic import BaseModel
from typing import Set, Tuple, Dict, List, Union

from automata.tm.dtm import DTM  #MT deterministica
from automata.pda.dpda import DPDA  #Automato pilha
from automata.fa.dfa import DFA  # Automato finito deterministico

class FiniteAutomataDeterministic(BaseModel):
    states: Set[str]
    input_symbols: Set[str]
    transitions: Dict[str, Dict[str, str]]
    initial_state: str
    final_states: Set[str]
    word: str  # Palavra para ser testada


class TuringMachine(BaseModel):
    states: Set[str]
    input_symbols: Set[str]
    tape_symbols: Set[str]
    transitions: Dict[str, Dict[str, Tuple[str, str, str]]]
    initial_state: str
    blank_symbol: str
    final_states: Set[str]
    word: str  # Palavra para ser testada
    
class PushdownAutomata(BaseModel):
    states: Set[str]
    input_symbols: Set[str]
    stack_symbols: Set[str]
    transitions: Dict[str, Dict[str, Dict[str, Tuple[str, Union[Tuple[str, ...], str]]]]]
    initial_state: str
    initial_stack_symbol: str
    final_states: Set[str]
    acceptance_mode: str
    word: str  # Palavra para ser testada

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de Autômatos em funcionamento!"}

@app.post("/turing/")
def validate_turing_machine(turing: TuringMachine): 
    dtm = DTM(
        states=turing.states,
        input_symbols=turing.input_symbols,
        tape_symbols=turing.tape_symbols,
        transitions=turing.transitions,
        initial_state=turing.initial_state,
        blank_symbol=turing.blank_symbol,
        final_states=turing.final_states,
    )
    
    aceita = dtm.accepts_input(turing.word)
    return {
        "states": turing.states,
        "input_symbols": turing.input_symbols,
        "tape_symbols": turing.tape_symbols,
        "transitions": turing.transitions,
        "initial_state": turing.initial_state,
        "blank_symbol": turing.blank_symbol,
        "final_states": turing.final_states,
        "word": turing.word, 
        "result": "aceita" if aceita else "rejeitada"
    }

@app.post("/finite/")
def validate_finite_automata_deterministic(finite: FiniteAutomataDeterministic): 
    dfa = DFA(
        states=finite.states,
        input_symbols=finite.input_symbols,
        transitions=finite.transitions,
        initial_state=finite.initial_state,
        final_states=finite.final_states,
    )
    
    aceita = dfa.accepts_input(finite.word)
    return {
        "states": finite.states,
        "input_symbols": finite.input_symbols,
        "transitions": finite.transitions,
        "initial_state": finite.initial_state,
        "final_states": finite.final_states,
        "word": finite.word, 
        "result": "aceita" if aceita else "rejeitada"
    }

@app.post("/pushdown/")
def validate_pushdown_automata(pushdown: PushdownAutomata): 
    dpda = DPDA(
        states = pushdown.states,
        input_symbols = pushdown.input_symbols,
        stack_symbols = pushdown.stack_symbols,
        transitions = pushdown.transitions,
        initial_state = pushdown.initial_state,
        initial_stack_symbol = pushdown.initial_stack_symbol,
        final_states = pushdown.final_states,
        acceptance_mode = pushdown.acceptance_mode,
    )
    
    aceita = dpda.accepts_input(pushdown.word)
    return {
        "states": pushdown.states,
        "input_symbols": pushdown.input_symbols,
        "stack_symbols": pushdown.stack_symbols,
        "transitions": pushdown.transitions,
        "initial_state": pushdown.initial_state,
        "final_states": pushdown.final_states,
        "word": pushdown.word, 
        "result": "aceita" if aceita else "rejeitada",
    }

