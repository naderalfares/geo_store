ABD = 'abd'
CAS = 'cas'
BRUTE_FORCE = 'brute_force'
MIN_COST = 'min_cost'
MIN_LATENCY = 'min_latency'

GEN_ABD = 'gen_abd_params'
GEN_CAS = 'gen_cas_params'

PLACEMENT_ABD = 'PlacementAbd'
PLACEMENT_CAS = 'PlacementCas'

GEN_PARAM_FUNC = {
    ABD: GEN_ABD,
    CAS: GEN_CAS
}

PLACEMENT_CLASS_MAPPER = {
    ABD: PLACEMENT_ABD,
    CAS: PLACEMENT_CAS
}

FUNC_HEURISTIC_MAP = {
    MIN_COST: MIN_COST,
    MIN_LATENCY: MIN_LATENCY,
    BRUTE_FORCE: BRUTE_FORCE
}
