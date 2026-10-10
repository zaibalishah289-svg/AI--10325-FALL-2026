# Inputs: Initial data batches and system configuration constants
# Processing: Workflow orchestration connecting preprocessing and analysis modules
# Outputs: Comprehensive console report covering data validation, class distribution, and metrics

from preprocessing import filter_by_confidence, split_complete_records, normalize_labels
from analysis import (
    count_by_label,
    get_unique_labels,
    find_unexpected_labels,
    average_confidence,
    top_predictions
)

# --- Configuration Constants ---
MIN_CONFIDENCE = 0.80
ALLOWED_LABELS = {"spam", "ham", "promotion"}
REQUIRED_FIELDS = ("id", "label", "confidence")
TOP_COUNT = 3

# --- Datasets ---
initial_predictions = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72},
    {"id": 3, "label": "promotion", "confidence": 0.41},
    {"id": 4, "label": "spam", "confidence": 0.89},
    {"id": 5, "label": "ham", "confidence": 0.97},
    {"id": 6, "label": "promotion", "confidence": 0.83},
    {"id": 7, "label": "ham", "confidence": 0.58}
]

new_batch = [
    {"id": 8, "label": "Spam", "confidence": 0.91},
    {"id": 9, "label": "ham"},  # Missing confidence field
    {"id": 10, "label": "unknown", "confidence": 0.86},  # Unrecognized label
    {"id": 11, "label": " HAM ", "confidence": 0.66}  # Inconsistent casing & spacing
]

# Combine both batches into one master list
all_predictions = initial_predictions + new_batch

# --- Processing Pipeline ---
total_records = len(all_predictions)

# Split complete vs incomplete records
complete_records, skipped_ids = split_complete_records(all_predictions, REQUIRED_FIELDS)
valid_records_count = len(complete_records)

# Normalize labels for the complete set
normalized_records = normalize_labels(complete_records)

# Analysis branches (starting from normalized records)
high_confidence_preds = filter_by_confidence(normalized_records, MIN_CONFIDENCE)
high_confidence_count = len(high_confidence_preds)

labels_list = get_unique_labels(normalized_records)
label_counts = count_by_label(normalized_records)
unexpected_labels = find_unexpected_labels(normalized_records, ALLOWED_LABELS)
avg_conf = average_confidence(normalized_records)
top_ids = top_predictions(normalized_records, TOP_COUNT)

# --- Summary Dictionary & Readable Report ---
summary = {
    "total_records": total_records,
    "valid_records": valid_records_count,
    "skipped_ids": skipped_ids,
    "labels": labels_list,
    "label_counts": label_counts,
    "high_confidence_count": high_confidence_count,
    "unexpected_labels": unexpected_labels,
    "average_confidence": avg_conf,
    "top_ids": top_ids
}

print("=== Prediction Report ===")
print(f"Total records:           {summary['total_records']}")
print(f"Valid records:           {summary['valid_records']}")
print(f"Skipped (missing data):  {summary['skipped_ids']}")
print(f"Labels:                  {summary['labels']}")
print(f"Label counts:            {summary['label_counts']}")
print(f"High confidence (>= 0.8): {summary['high_confidence_count']}")
print(f"Unexpected labels:       {summary['unexpected_labels']}")
print(f"Average confidence:      {summary['average_confidence']:.3f}")
print(f"Top {TOP_COUNT} by confidence:     {summary['top_ids']}")

# Proof that normalization did not mutate the raw data of record 8 in new_batch
print(f"\nVerification - Record 8 label in raw new_batch: '{new_batch[0]['label']}' (must still be 'Spam')")