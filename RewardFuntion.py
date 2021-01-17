def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle']) 
    
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    reward = 1e-3 #Reward por default muy pequeño
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3 
    ABS_STEERING_THRESHOLD = 15
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    return float(reward)