import json

TEMPLATE = r"""
\begin{{table*}}[t]
\centering
\small
\setlength{{\tabcolsep}}{{6pt}}
\renewcommand{{\arraystretch}}{{1.15}}

\caption{{{}}}
\label{{{}}}

\begin{{tabularx}}{{\textwidth}}{{{}}}
\toprule

{}\\

\midrule

{}

\bottomrule
\end{{tabularx}}
\end{{table*}}
"""

def to_latex_symbol(value):
    if value is True:
        return r"\textcolor{xgreen}{\ding{51}}"
    elif value is False:
        return r"\textcolor{xred}{\ding{55}}"
    else:
        return str(value)
    

def generate_lemma_results_table(json_file, latex_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    columns = [
      "Assumption",
      "Provider",
      "Scenario",
      "Model",
      "\\; IA-O1 \\;",
      "\\; IA-O2 \\;",
      "\\; IA-UA \\;",
      "\\; IA-R1 \\;",
      "\\; IA-R2 \\;",
      "Time (s)"
    ]

    label = "tab:lemma-results"
    cation = r"""
      \textbf{Security Property Satisfaction of Third‑Party Online Payment Protocols.}
      Each protocol is evaluated under three channel security assumptions. 
      IA-O1/O2, IA-UA, IA-R1/R2 denote the security properties defined in Section~\ref{sec:security_properties}.
      \textcolor{xgreen}{\ding{51}} indicates that the security property is satisfied, while \textcolor{xred}{\ding{55}} indicates a violation.
      Time reports the total analysis time.
    """
    header = " & ".join(["\\textbf{" + c + "}" for c in columns]) 
    alignment = "XXXXcccccr"

    lines = []
    for entry in data:
        if entry["Assumption"] != "Base" and entry["Protocol"] == "Alipay-In-App":
            lines.append("\\midrule")
        line = ""
        line += entry["Assumption"] + " & "
        line += "Alipay" + " & " if "Alipay" in entry["Protocol"] else "WeChatPay" + " & "
        line += "-".join(entry["Protocol"].split("-")[1:]) + " & "
        line += entry["Model"] + " & "
        line += to_latex_symbol(entry["IA-O1"]) + " & "
        line += to_latex_symbol(entry["IA-O2"]) + " & "
        line += to_latex_symbol(entry["IA-UA"]) + " & "
        line += to_latex_symbol(entry["IA-R1"]) + " & "
        line += to_latex_symbol(entry["IA-R2"]) + " & "
        line += str(entry["Time"])
        lines.append(line + " \\\\")

    with open(latex_file, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(cation, label, alignment, header, "\n".join(lines)))

if __name__ == "__main__":
    generate_lemma_results_table("lemma_results.json", "lemma_results.tex")
