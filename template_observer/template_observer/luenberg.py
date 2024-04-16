#!/usr/bin/env python3

import numpy as np
from template_observer.wrap import wrap

def luenberg(eta, tau, observer, L1, L2, L3):
    
    eta_hat = observer.eta
    nu_hat = observer.nu
    bias_hat = observer.bias

    # Log the incoming information
    print("=== Luenberg Observer ===")
    print("eta: ", eta)
    print("tau: ", tau)
    print("observer", observer)
    print("L1: ", L1)
    print("L2: ", L2)
    print("L3: ", L3)


    # Enter your code here



    return eta_hat, nu_hat, bias_hat
