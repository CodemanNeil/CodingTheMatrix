from vec import Vec


def project_along(b, v):
    sigma = ((b*v)/(v*v)) if v*v > 1e-20 else 0
    return sigma * v

def project_orthogonal(b, vlist):
    for v in vlist:
        b = b - project_along(b, v)
    return b

def aug_project_orthogonal(b, vlist):
    # Initialize coefficient for b-perpendicular to 1
    sigmadict = {len(vlist):1}
    for i,v in enumerate(vlist):
        sigma = ((b*v)/(v*v)) if v*v > 1e-20 else 0
        sigmadict[i] = sigma
        b = b - sigma*v
    return (b, sigmadict)

def orthogonalize(vlist):
    vstarlist = []
    for v in vlist:
        vstarlist.append(project_orthogonal(v, vstarlist))
    return vstarlist

def aug_orthogonalize(vlist):
    vstarlist = []
    sigma_vecs = []
    D = set(range(len(vlist)))
    for v in vlist:
        vstar, sigma_dict = aug_project_orthogonal(v, vstarlist)
        vstarlist.append(vstar)
        sigma_vecs.append(Vec(D, sigma_dict))
    return vstarlist, sigma_vecs

def find_basis(vlist):
    vstarlist = orthogonalize(vlist)
    return [vstar for vstar in vstarlist if not vstar.is_almost_zero()]

def find_orthogonal_complement(U_vecs, W_vecs):
    U_basis = find_basis(U_vecs)
    W_basis = find_basis(W_vecs)
    v_list = orthogonalize(U_basis + W_basis)
    k = len(U_basis)
    return [w_star for w_star in v_list[k:] if not w_star.is_almost_zero()]