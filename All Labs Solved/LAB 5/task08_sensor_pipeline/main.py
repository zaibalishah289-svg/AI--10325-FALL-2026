import numpy as np
from sensor_utils import (
    clean_sensor_rows,
    summarize_features,
    minmax_scale,
    flag_for_review
)

def main():
    raw_sensor_data = np.array([
        [21.0, 42.0, 0.30],
        [24.0, 51.0, 0.55],
        [-10.0, 40.0, 0.45],  # invalid temperature
        [26.0, 68.0, 0.80],
        [32.0, 110.0, 0.95], # invalid humidity
        [28.0, 59.0, 0.72],
        [23.0, 48.0, -0.20], # invalid vibration
        [30.0, 74.0, 1.00]
    ], dtype=float)

    print("Input Shape:", raw_sensor_data.shape)

    # Clean rows
    clean_data = clean_sensor_rows(raw_sensor_data)
    print("Cleaned Shape:", clean_data.shape)

    # Summarize & scale
    summary = summarize_features(clean_data)
    scaled_data = minmax_scale(clean_data)
    review_flags = flag_for_review(clean_data)

    total_readings = len(raw_sensor_data)
    valid_readings = len(clean_data)
    invalid_readings = total_readings - valid_readings
    flagged_count = int(np.sum(review_flags))

    print("\n--- SENSOR PIPELINE SUMMARY ---")
    print(f"Total Readings: {total_readings}")
    print(f"Valid Readings: {valid_readings}")
    print(f"Invalid Readings: {invalid_readings}")
    print(f"Rows Flagged for Review: {flagged_count}")
    print("\nFeature-wise Means (Temp, Hum, Vib):", summary["mean"])
    print("\nScaled Data (First 3 rows):\n", scaled_data[:3])

if __name__ == "__main__":
    main()