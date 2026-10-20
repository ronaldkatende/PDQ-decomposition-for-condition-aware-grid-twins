import numpy as np
from scripts.dce_real_validation import diagnostics, orth, recover, ridge_map


def test_orthogonal_coordinates_do_not_change_reconstruction():
    rng = np.random.default_rng(100)
    B = orth(rng.normal(size=(20, 5)))
    Q = orth(rng.normal(size=(5, 5)))
    idx = np.array([1, 2, 4, 8, 9, 12, 15, 19])
    X = rng.normal(size=(20, 10))
    Xhat1, _, _ = recover(B, idx, X, 0.1)
    Xhat2, _, _ = recover(B @ Q, idx, X, 0.1)
    assert np.allclose(Xhat1, Xhat2, atol=1e-10)


def test_exact_amplification_matches_operator_norm():
    rng = np.random.default_rng(101)
    B = orth(rng.normal(size=(15, 4)))
    idx = np.array([1, 2, 4, 5, 7, 8])
    gamma = 0.03
    R, _ = ridge_map(B, idx, gamma)
    reported = diagnostics(B, idx, gamma)['exact_amplification']
    assert np.isclose(reported, np.linalg.norm(R, ord=2), rtol=1e-10)


def test_rank_deficiency_gives_full_unobserved_direction_bias():
    rng = np.random.default_rng(102)
    B = orth(rng.normal(size=(15, 5)))
    d = diagnostics(B, np.array([1, 2]), gamma=0.2)
    assert d['rank_G'] <= 2
    assert d['sigma_min'] == 0.0
    assert np.isclose(d['ridge_bias_factor'], 1.0)
