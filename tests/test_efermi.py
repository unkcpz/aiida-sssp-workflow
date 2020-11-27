from sssp.efermi_module import efermi

import numpy as np

def test_efermi_import():
    bands = np.array([[-85.39990157, -36.73700546, -36.73700543, -36.7370054 ,
          9.76035271,  15.16638246,  15.16638247,  15.16638248,
         16.60627013,  16.60627015,  33.44912684,  37.11647673,
         37.11647674,  37.11647675],
       [-85.39125695, -36.91325724, -36.7641251 , -36.76412506,
         12.52166417,  15.13221622,  15.13221624,  17.72172404,
         17.72172407,  18.2509223 ,  22.09837349,  32.84238067,
         35.66056113,  35.66056114],
       [-85.39125695, -36.9132572 , -36.76412512, -36.76412509,
         12.52166418,  15.13221621,  15.13221622,  17.72172406,
         17.72172408,  18.2509223 ,  22.0983735 ,  32.84238068,
         35.66056113,  35.66056114],
       [-85.38839039, -36.9050697 , -36.80543399, -36.80543397,
         12.8329073 ,  13.20528077,  17.68836536,  18.01799658,
         18.01799659,  20.15672333,  24.52935083,  28.80586708,
         28.80586709,  35.514056  ],
       [-85.39125695, -36.91325725, -36.76412509, -36.76412507,
         12.52166418,  15.13221623,  15.13221624,  17.72172405,
         17.72172407,  18.25092229,  22.09837348,  32.84238068,
         35.66056113,  35.66056113],
       [-85.38839039, -36.90506969, -36.80543401, -36.80543396,
         12.8329073 ,  13.20528076,  17.68836534,  18.01799658,
         18.0179966 ,  20.15672334,  24.52935084,  28.80586708,
         28.80586709,  35.51405601],
       [-85.38839039, -36.90506971, -36.80543399, -36.80543397,
         12.83290729,  13.20528076,  17.68836536,  18.01799658,
         18.01799659,  20.15672334,  24.52935083,  28.80586708,
         28.8058671 ,  35.514056  ],
       [-85.39125695, -36.91325722, -36.76412512, -36.76412507,
         12.52166418,  15.13221622,  15.13221623,  17.72172405,
         17.72172408,  18.2509223 ,  22.09837349,  32.84238068,
         35.66056113,  35.66056114]])
    bands = bands - 18.3253
    bands = np.asfortranarray(bands)
    nelectrons = 19
    nbands = 14
    nkps = 8
    weight = np.ones(nkps) / nkps
    smearing = 0.2721
    print(bands)
    print(efermi.__doc__)
    res = efermi(nelectrons, nbands, smearing, nkps, weight, 0.0, bands, 2)
    print(res[1])