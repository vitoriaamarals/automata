## EXEMPLOS DE TESTE

DFA
```
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
```
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
```
{
  "states": ["q0", "q1", "q2", "q3"],
  "input_symbols": ["a", "b"],
  "stack_symbols": ["0", "1"],
  "transitions": {
    "q0": {
      "a": ["q1", "1", "0"]
    },
    "q1": {
      "a": ["q1", "1", "1"],
      "b": ["q2", "", "1"]
    },
    "q2": {
      "b": ["q2", "", "1"],
      "": ["q3", "0", ""]
    }
  },
  "initial_state": "q0",
  "initial_stack_symbol": "0",
  "final_states": ["q3"],
  "acceptance_mode": "final_state",
  "word": "aabb"
}
```


