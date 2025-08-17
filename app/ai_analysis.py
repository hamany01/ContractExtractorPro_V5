import pandas as pd


def analyze_document(path: str) -> dict:
    """تحليل مبدئي للملفات المرفوعة."""
    try:
        if path.lower().endswith(".xlsx"):
            df = pd.read_excel(path)
            return {"rows": len(df), "columns": list(map(str, df.columns))}
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        return {"content_preview": content[:100]}
    except Exception as exc:
        return {"error": str(exc)}
