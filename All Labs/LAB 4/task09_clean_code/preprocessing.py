# Inputs: Raw prediction records and required schema fields
# Processing: Confidence filtering, missing record splitting, and label normalization
# Outputs: Filtered selections, complete/incomplete record tuples, and cleaned lowercase labels

def filter_by_confidence(predictions, min_confidence):
    """Returns predictions with confidence at or above the threshold."""
    return [pred for pred in predictions if pred.get("confidence", 0) >= min_confidence]


def split_complete_records(predictions, required_fields):
    """Splits predictions into a tuple of (complete_records, incomplete_ids)."""
    complete = []
    incomplete_ids = []
    
    for pred in predictions:
        # Check if all required fields are present and not None/empty
        if all(field in pred and pred[field] is not None for field in required_fields):
            complete.append(pred)
        else:
            incomplete_ids.append(pred.get("id"))
            
    return complete, incomplete_ids


def normalize_labels(predictions):
    """Returns a new list of records with normalized (stripped and lowercased) labels without mutating originals."""
    normalized_list = []
    for pred in predictions:
        # Create a shallow copy of the record dictionary to protect original raw data
        record_copy = pred.copy()
        if "label" in record_copy and isinstance(record_copy["label"], str):
            record_copy["label"] = record_copy["label"].strip().lower()
        normalized_list.append(record_copy)
    return normalized_list