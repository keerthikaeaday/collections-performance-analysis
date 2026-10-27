
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_DIR = PROJECT_DIR / "golden_dataset" / "data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

quality_records = []
key_columns = {
    "accounts": "account_id",
    "borrowers": "borrower_id",
    "agents": "agent_id",
    "agent_sessions": "session_id",
    "calls": "call_id",
    "call_attempts": "attempt_id",
    "call_dispositions": "disposition_id",
    "payments": "payment_id",
    "promises_to_pay": "ptp_id",
    "field_visits": "visit_id",
    "sms_events": "sms_event_id",
    "whatsapp_events": "whatsapp_event_id",
    "complaints": "complaint_id",
    "account_status_history": "history_id",
    "daily_targeting": "target_id"
}

for file_path in sorted(RAW_DIR.glob("*.csv")):
    if file_path.name == "data_dictionary.csv":
        continue

    dataset_name = file_path.stem
    df = pd.read_csv(file_path, low_memory=False)
    original_rows = len(df)
    exact_duplicates = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()
    key = key_columns.get(dataset_name)

    quality_records.append({
        "dataset": dataset_name,
        "raw_rows": original_rows,
        "exact_duplicate_rows_removed": exact_duplicates,
        "rows_after_exact_deduplication": len(df),
        "candidate_key": key,
        "missing_candidate_key": int(df[key].isna().sum()) if key and key in df.columns else None,
        "duplicate_candidate_key_rows": int(df[key].duplicated(keep=False).sum()) if key and key in df.columns else None
    })

    df.to_csv(OUTPUT_DIR / f"{dataset_name}_clean.csv", index=False)

quality_report = pd.DataFrame(quality_records)
quality_report.to_csv(OUTPUT_DIR / "pipeline_quality_report.csv", index=False)

print("Pipeline completed.")
print("Cleaned datasets:", len(quality_records))
print("Output directory:", OUTPUT_DIR)
print(quality_report.to_string(index=False))
