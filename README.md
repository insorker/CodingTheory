# Coding Theory

Simulation of error correction coding.

- [x] channel
- [x] galois field
- [x] encoding and decoding algorithm 
- [x] auto test
- [ ] c code

## Setup

```shell
python -m venv venv
source venv/bin/activate
pip install
npm install
```

## Run test

```shell
# overall test
python test/test.py

# single test
python test/test_ecc_golay.py
```

## Develop

1. Write an error correction code class inheriting from `EccBase`.

2. Add custom test or auto test in `test` folder. The test file must start with "test_".