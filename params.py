# TODO: Make a run with different parameters and plot results
parameters = {
    'learning_rate': 0.1,
    'training_iters': 1000000,
    'display_step': int(100000 / 128 / 100) + 1,
    # Should not put too many display steps here, because accumulation of data takes memory. Doing ~100 print outs.
    'decay': 1.0, #0.99995,
    # 16 input layer size (against the size 12 input) seems to be too little to capture the necessary features.
    # None seems to work better.
    'input_layer': None,
    # 6, 3 leads to high variance (difference between training and testing), so at least those are too large.
    # For single-layer LSTMs seem more stable.
    # [12] also has too much variance.
    # [6] has too big bias, and doesn't learn well.
    'lstm_layers': [7],
    # How many targets are there
    'n_targets': 22,
    'n_peers': 2,
    # x, y for 3 targets
    # TODO: Add enabled flag
    'n_input': 3*4,
    # The minibatch is 2048 * 4 sequences of 5 steps.
    'batch_size': 2048 * 4,
    'n_steps': 5, # timesteps
    # x, y mixtures for 1 target. TODO: Add enabled flag.
    # Note: This must currently always be two because of bivariate gaussian mixture network
    'n_output': 2,
    'lstm_clip': 10.0,
    # For the mixture density network, how many mixtures we use per variable.
    'n_mixtures': 3
}
