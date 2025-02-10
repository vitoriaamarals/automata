from fastapi import FastAPI

from automata.tm.dtm import DTM  #MT deterministica
from automata.pda.dpda import DPDA  #Automato pilha
from automata.fa.dfa import DFA  # Automato finito deterministico

from models import FiniteAutomataDeterministic, TuringMachine, PushdownAutomata

app = FastAPI()

# Rota principal para verificar se a API está rodando
@app.get("/")
def read_root():
    return {"message": "API de Autômatos em funcionamento!"}

# Rota para validar palavras em um Autômato Finito Determinístico (DFA)
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

# Rota para validar palavras em uma Máquina de Turing Determinística (DTM)
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

# Rota para validar palavras em um Autômato com Pilha Determinístico (DPDA)
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

