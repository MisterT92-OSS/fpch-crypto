# arXiv Submission Guide — FPCH

**Paper:** `arxiv/fpch_arxiv.tex`
**Date:** 2026-05-14

---

## 1. Prerequisites

- arXiv account: [https://arxiv.org/user/register](https://arxiv.org/user/register)
- LaTeX source ready (single `.tex` file preferred for simplicity)

## 2. Quick Submit

```bash
cd arxiv/
pdflatex fpch_arxiv.tex
# Fix any errors, then re-run until stable
pdflatex fpch_arxiv.tex
```

Upload to arXiv:
- **Primary category:** cs.CR (Cryptography and Security)
- **Secondary categories:** math.NT (Number Theory), cs.DC (Distributed/Parallel/Cluster Computing) if GPU section is emphasized.

## 3. Title / Abstract Checklist

| Item | Status |
|---|---|
| Title under 150 characters | ✅ |
| Abstract under 1920 characters | ✅ |
| No LaTeX macros in abstract | ✅ (verify manually) |
| Keywords included | ✅ |
| Comment field: "Preprint, invitation to cryptanalysis" | Add at submission |

## 4. Files to Upload

```
fpch_arxiv.tex      (main source)
fpch_arxiv.bbl      (if using BibTeX; we use thebibliography, so not needed)
fpch_arxiv.pdf      (compiled preview)
```

**No .bst file needed** because we use `\begin{thebibliography}`.

## 5. After Submission

- Post the arXiv link on the GitHub README.
- Announce on Cryptography StackExchange, /r/crypto, and IACR News if appropriate.
- Email the link to eprint-editor@iacr.org with a polite note that this is a revised, expanded version of the earlier ePrint submission.

## 6. Versioning

If cryptanalytic feedback leads to changes, submit a revision:
- v1: Initial arXiv upload
- v2: Address first round of community feedback
- etc.

---

*Generated for FPCH v6.0*
