import numpy as np

def clean_sensor_rows(readings):
    """
    Validates all 3 columns:
    0 <= temperature_C <= 50
    0 <= humidity_percent <= 100
    0 <= vibration_score <= 1
    Returns a new NumPy array containing only valid rows.
    """
    temp_valid = (readings[:, 0] >= 0.0) & (readings[:, 0] <= 50.0)
    hum_valid = (readings[:, 1] >= 0.0) & (readings[:, 1] <= 100.0)
    vib_valid = (readings[:, 2] >= 0.0) & (readings[:, 2] <= 1.0)
    
    valid_mask = temp_valid & hum_valid & vib_valid
    return readings[valid_mask].copy()

def summarize_features(readings):
    """
    Returns a dictionary containing feature-wise mean, minimum, and maximum.
    Raises ValueError if there are no rows to summarize.
    """
    if readings.shape[0] == 0:
        raise ValueError("No valid rows available to summarize.")
        
    return {
        "mean": np.mean(readings, axis=0),
        "minimum": np.min(readings, axis=0),
        "maximum": np.max(readings, axis=0)
    }

def minmax_scale(readings):
    """
    Scales features column-wise using NumPy broadcasting.
    Handles constant features safely. Raises ValueError if empty.
    """
    if readings.shape[0] == 0:
        raise ValueError("No valid rows available to scale.")
        
    col_min = np.min(readings, axis=0)
    col_max = np.max(readings, axis=0)
    spans = col_max - col_min
    
    safe_spans = np.where(spans == 0, 1.0, spans)
    scaled = (readings - col_min) / safe_spans
    scaled = np.where(spans == 0, 0.0, scaled)
    return scaled

def flag_for_review(readings):
    """
    Returns 1D Boolean array where a row is marked True if:
    temperature_C > 27 OR vibration_score >= 0.70
    """
    if readings.shape[0] == 0:
        return np.array([], dtype=bool)
        
    temp_flag = readings[:, 0] > 27.0
    vib_flag = readings[:, 2] >= 0.70
    return temp_flag | vib_flag