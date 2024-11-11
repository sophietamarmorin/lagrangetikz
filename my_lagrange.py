def my_lagrange(xvals, yvals):

    num_coeffs = len(xvals)
    interp_coeffs = []

    ####
    # make the lagrange polys

    polys = make_lagrange_polys(xvals)

    ####
    # get the coeffs on the individual lagrange polys

    poly_coeffs = []

    ## get the diagonal lagrange poly values

    diag_vals = []

    for diag_index in range(num_coeffs):
        diag_val = 0
        for k in range(num_coeffs):
            diag_val += polys[diag_index][k]*(xvals[diag_index]**(num_coeffs - 1 - k))
        diag_vals.append(diag_val)

    ## fit to the yvals

    for diag_index_2 in range(num_coeffs):
        poly_coeffs.append(yvals[diag_index_2]/diag_vals[diag_index_2])

    #####
    # add up the rescaled individual lagrange polys

    for interp_degree_comp in range(num_coeffs):
        interp_coeff = 0
        for poly_index in range(num_coeffs):
            interp_coeff += poly_coeffs[poly_index]*polys[poly_index][interp_degree_comp]
        interp_coeffs.append(interp_coeff)
    return interp_coeffs
    
def make_lagrange_polys(xvals):

    num_roots = len(xvals)
    polys = []
    binomials = []

    for center_index in range(num_roots):
        polys.append([1])
        binomials.append([1,-xvals[center_index]])

    for center_index in range(num_roots):
        for root_index in range(num_roots):
            if root_index != center_index:
                polys[center_index] = bi_times_poly(binomials[root_index], polys[center_index])

    return polys


def bi_times_poly(bi, input_poly):

    # bi is a float list of length 2, 0th entry linear coeff, 1th entry constant term
    # input_poly is a float list of any length, 0th entry highest-order coeff, last entry constant term

    num_coeffs = len(input_poly)
    output_poly = [0]*(num_coeffs + 1)

    linear_coeff = bi[0]
    const_term = bi[1]

    for pos in range(num_coeffs):
        output_poly[pos] += linear_coeff*input_poly[pos]
        output_poly[pos + 1] += const_term*input_poly[pos]

    return output_poly