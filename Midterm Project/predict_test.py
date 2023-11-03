import requests

url = 'http://localhost:1616/predict'

data = {'baseline_value': 133.0,
 'accelerations': 0.002,
 'fetal_movement': 0.01,
 'uterine_contractions': 0.003,
 'light_decelerations': 0.002,
 'severe_decelerations': 0.0,
 'prolongued_decelerations': 0.0,
 'abnormal_short_term_variability': 46.0,
 'mean_value_of_short_term_variability': 1.1,
 'percentage_of_time_with_abnormal_long_term_variability': 0.0,
 'mean_value_of_long_term_variability': 15.4,
 'histogram_width': 69.0,
 'histogram_min': 95.0,
 'histogram_max': 164.0,
 'histogram_mode': 139.0,
 'histogram_mean': 135.0,
 'histogram_median': 138.0,
 'histogram_variance': 9.0,
 'histogram_tendency': 0.0}

response = requests.post(url, json=data).json()
print(response)