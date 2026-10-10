# Inputs: Cleaned prediction records and allowed label vocabularies
# Processing: Label counting, set operations for unexpected classes, confidence averages, and sorting
# Outputs: Frequency dictionaries, unique sets, unseen lists, confidence metrics, and top-k selections

def count_by_label(predictions):
    """Returns a dictionary counting occurrences of each label across all predictions."""
    counts = {}
    for pred in predictions:
        label = pred.get("label")
        if label:
            counts[label] = counts.get(label, 0) + 1
    return counts


def get_unique_labels(predictions):
    """Returns a sorted list of unique labels found in predictions."""
    return sorted(list({pred.get("label") for pred in predictions if "label" in pred}))


def find_unexpected_labels(predictions, allowed_labels):
    """Uses set difference to find labels present in predictions that are not in allowed_labels."""
    received_labels = {pred.get("label") for pred in predictions if "label" in pred}
    return sorted(list(received_labels - allowed_labels))


def average_confidence(predictions):
    """Returns the average confidence score across predictions, or None if the list is empty."""
    if not predictions:
        return None
    confidences = [pred.get("confidence", 0) for pred in predictions if "confidence" in pred]
    if not confidences:
        return 0.0
    return sum(confidences) / len(confidences)


def top_predictions(predictions, count):
    """Returns the IDs of the top N predictions ordered by confidence (highest first)."""
    sorted_preds = sorted(predictions, key=lambda x: x.get("confidence", 0), reverse=True)
    return [pred.get("id") for pred in sorted_preds[:count]]