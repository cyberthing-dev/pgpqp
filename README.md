# Pretty Good Post Quantum Privacy (PGPQP)

PGP does not currently implement post quantum cryptography. This project aims to provide a PGP-like system that does.

## Motivation
I wrote a [paper](./docs/cryptography%20paper.pdf) on post quantum cryptography during my sophomore year of my Bachelor's degree in cybersecurity. For the same class--about a week prior--I wrote another [paper](./docs/E2EE%20Case%20Study.pdf) discussing the importance of consumer end-to-end encryption (E2EE). I thought it would be a good idea to combine the two ideas and create a post quantum cryptography system that could be used in place of PGP.

## Technologies
| Technology | Cryptographic Function | Description |
|------------|------------------------|-------------|
| [Kyber](https://pq-crystals.org/kyber/) | Key Encapsulation Mechanism | Lattice-based |
| [SPHINCS+](https://sphincs.org/) | Digital Signature | Hash-based |
| [AES](https://wikipedia.org/wiki/Advanced_Encryption_Standard) | Symmetric Encryption | Block cipher |

## Relevant Links
- [NIST Post Quantum Cryptography Standardization](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy)
- [Post Quantum Cryptography](https://en.wikipedia.org/wiki/Post-quantum_cryptography)

## Project Goal
Either establish a good post quantum cryptography public key infrastructure or integrate into PGP.

### Compliance
- [ ] FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard
- [ ] FIPS 205: Stateless Hash-Based Digital Signature Standard
