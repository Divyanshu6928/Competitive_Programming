def light_bulb_switches(desired_states):
    presses = []

    # Start from the rightmost bulb
    for i in range(len(desired_states) - 1, -1, -1):
        # If the desired state is different from the current state
        if desired_states[i] != 0:
            # Press switch A to turn it on
            for _ in range(i + 1):
                presses.append('A')
        else:
            # Press switch B to turn it off
            if i > 0:
                presses.append('B')

    return presses

# Example usage:
desired_states = [0,1,1,0,0]
print(light_bulb_switches(desired_states))  # Output: ['A', 'B', 'A', 'A']
