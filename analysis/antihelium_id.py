def calculate_mass_to_charge(momentum, charge):
    """Calculate mass-to-charge ratio for antihelium-4."""
    # simple non-relativistic approximation
    mass = 3.727  # GeV/c^2
    return mass / charge

def identify_antihelium4(momentum, charge, detector_signals):
    """Identify antihelium-4 nuclei based on mass-to-charge and detector signals."""
    m_over_q = calculate_mass_to_charge(momentum, charge)
    # placeholder identification logic
    if abs(m_over_q - 3.727) < 0.1:
        return True
    else:
        return False