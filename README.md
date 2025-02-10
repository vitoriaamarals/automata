# TRABALHO PRÁTICO DE TEORIA DA COMPUTAÇÃO 

## :hammer_and_wrench: COMO RODAR
1. Clone o repositório
   ```
   git clone https://github.com/vitoriaamarals/automata
   ```
2. Crie o ambiente virtual e instale as dependências
   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r fastapi uvicorn automata-lib
   ```
3. Execute:
   ```
   uvicorn main:app --reload
   ```

A API é executada em ```localhost:8000```. 
Em ```localhost:8000/docs```, é possível ver os endpoints e testá-los usando os exemplos abaixo.

## :computer: EXEMPLOS DE TESTE EM JSON

DFA
```json
{
  "states": ["q0", "q1", "q2"],
  "input_symbols": ["0", "1"],
  "transitions": {
    "q0": {"0": "q0", "1": "q1"},
    "q1": {"0": "q0", "1": "q2"},
    "q2": {"0": "q2", "1": "q1"}
  },
  "initial_state": "q0",
  "final_states": ["q1"],
  "word": "000111"
}
```

MT 
```json
{
  "states": ["q0", "q1", "q2", "q3", "q4"],
  "input_symbols": ["0", "1"],
  "tape_symbols": ["0", "1", "x", "y", "."],
  "transitions": {
    "q0": {
      "0": ["q1", "x", "R"],
      "y": ["q3", "y", "R"]
    },
    "q1": {
      "0": ["q1", "0", "R"],
      "1": ["q2", "y", "L"],
      "y": ["q1", "y", "R"]
    },
    "q2": {
      "0": ["q2", "0", "L"],
      "x": ["q0", "x", "R"],
      "y": ["q2", "y", "L"]
    },
    "q3": {
      "y": ["q3", "y", "R"],
      ".": ["q4", ".", "R"]
    }
  },
  "initial_state": "q0",
  "blank_symbol": ".",
  "final_states": ["q4"],
  "word": "0011"
}
```

PDA
```json
{
  "states": ["q0", "q1", "q2", "q3"],
  "input_symbols": ["a", "b"],
  "stack_symbols": ["0", "1"],
  "transitions": {
    "q0": {
      "a": {
        "0": ["q1", ["1", "0"]]
      }
    },
    "q1": {
      "a": {
        "1": ["q1", ["1", "1"]]
      },
      "b": {
        "1": ["q2", ""]
      }
    },
    "q2": {
      "b": {
        "1": ["q2", ""]
      },
      "": {
        "0": ["q3", ["0"]]
      }
    }
  },
  "initial_state": "q0",
  "initial_stack_symbol": "0",
  "final_states": ["q3"],
  "acceptance_mode": "final_state",
  "word": "aabb"
}
```


