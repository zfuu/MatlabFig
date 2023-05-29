import numpy as np
import matplotlib.pyplot as plt

import module_locator



Fs = 1000
f = 10
sample = 200
# x = np.arange(sample)
# y1 = np.sin(2 * np.pi * f * x / Fs)
# y2 = -3*np.sin((2 * np.pi * f * x / Fs))

# print(list(y2))
y1 = [0.0, 0.06279051952931337, 0.12533323356430426, 0.1873813145857246, 0.2486898871648548, 0.3090169943749474, 0.3681245526846779, 0.42577929156507266, 0.4817536741017153, 0.5358267949789967, 0.5877852522924731, 0.6374239897486897, 0.6845471059286886, 0.7289686274214114, 0.7705132427757893, 0.8090169943749475, 0.8443279255020151, 0.8763066800438636, 0.9048270524660196, 0.9297764858882515, 0.9510565162951535, 0.9685831611286311, 0.9822872507286887, 0.9921147013144779, 0.9980267284282716, 1.0, 0.9980267284282716, 0.9921147013144779, 0.9822872507286887, 0.9685831611286312, 0.9510565162951536, 0.9297764858882515, 0.9048270524660195, 0.8763066800438637, 0.8443279255020152, 0.8090169943749475, 0.7705132427757893, 0.7289686274214118, 0.6845471059286885, 0.6374239897486899, 0.5877852522924732, 0.5358267949789967, 0.4817536741017152, 0.4257792915650729, 0.36812455268467775, 0.3090169943749475, 0.24868988716485482, 0.18738131458572457, 0.12533323356430454, 0.06279051952931358, 1.2246467991473532e-16, -0.06279051952931335, -0.12533323356430384, -0.18738131458572477, -0.24868988716485457, -0.3090169943749473, -0.3681245526846779, -0.42577929156507266, -0.481753674101715, -0.5358267949789968, -0.587785252292473, -0.6374239897486896, -0.6845471059286887, -0.7289686274214116, -0.7705132427757894, -0.8090169943749473, -0.8443279255020147, -0.8763066800438636, -0.9048270524660194, -0.9297764858882515, -0.9510565162951535, -0.968583161128631, -0.9822872507286887, -0.9921147013144779, -0.9980267284282716, -1.0, -0.9980267284282716, -0.9921147013144779, -0.9822872507286887, -0.9685831611286311, -0.9510565162951536, -0.9297764858882516, -0.9048270524660196, -0.8763066800438638, -0.844327925502015, -0.8090169943749476, -0.7705132427757896, -0.7289686274214116, -0.6845471059286883, -0.6374239897486903, -0.5877852522924734, -0.5358267949789963, -0.4817536741017153, -0.425779291565073, -0.36812455268467786, -0.3090169943749477, -0.24868988716485535, -0.18738131458572468, -0.12533323356430465, -0.06279051952931326, -2.4492935982947064e-16, 0.06279051952931278, 0.12533323356430418, 0.18738131458572507, 0.24868988716485402, 0.3090169943749472, 0.3681245526846782, 0.42577929156507255, 0.4817536741017149, 0.5358267949789967, 0.5877852522924729, 0.63742398974869, 0.6845471059286886, 0.7289686274214112, 0.7705132427757893, 0.8090169943749472, 0.8443279255020147, 0.8763066800438636, 0.9048270524660197, 0.9297764858882511, 0.9510565162951535, 0.9685831611286312, 0.9822872507286886, 0.9921147013144778, 0.9980267284282716, 1.0, 0.9980267284282716, 0.9921147013144779, 0.9822872507286886, 0.9685831611286311, 0.9510565162951536, 0.9297764858882517, 0.90482705246602, 0.8763066800438634, 0.8443279255020151, 0.8090169943749476, 0.7705132427757897, 0.7289686274214122, 0.6845471059286884, 0.6374239897486897, 0.5877852522924734, 0.5358267949789972, 0.4817536741017162, 0.4257792915650723, 0.368124552684678, 0.3090169943749478, 0.24868988716485377, 0.18738131458572568, 0.12533323356430567, 0.06279051952931339, 3.6739403974420594e-16, -0.06279051952931265, -0.12533323356430492, -0.1873813145857232, -0.24868988716485477, -0.30901699437494706, -0.36812455268467725, -0.42577929156507327, -0.48175367410171555, -0.5358267949789951, -0.5877852522924728, -0.6374239897486892, -0.6845471059286878, -0.7289686274214118, -0.7705132427757891, -0.8090169943749472, -0.8443279255020146, -0.876306680043863, -0.9048270524660197, -0.9297764858882513, -0.9510565162951534, -0.968583161128631, -0.9822872507286885, -0.9921147013144779, -0.9980267284282716, -1.0, -0.9980267284282714, -0.992114701314478, -0.9822872507286889, -0.9685831611286312, -0.9510565162951538, -0.9297764858882517, -0.9048270524660192, -0.8763066800438644, -0.8443279255020152, -0.8090169943749477, -0.7705132427757898, -0.7289686274214111, -0.6845471059286885, -0.6374239897486912, -0.5877852522924735, -0.5358267949789973, -0.4817536741017163, -0.42577929156507244, -0.3681245526846781, -0.3090169943749479, -0.2486898871648556, -0.1873813145857258, -0.125333233564304, -0.06279051952931351]
y2 = [-0.0, -0.18837155858794014, -0.3759997006929128, -0.5621439437571738, -0.7460696614945643, -0.9270509831248421, -1.1043736580540338, -1.277337874695218, -1.445261022305146, -1.60748038493699, -1.7633557568774194, -1.9122719692460692, -2.0536413177860657, -2.1869058822642344, -2.311539728327368, -2.4270509831248424, -2.532983776506045, -2.628920040131591, -2.7144811573980587, -2.7893294576647545, -2.8531695488854605, -2.9057494833858932, -2.946861752186066, -2.9763441039434335, -2.9940801852848145, -3.0, -2.9940801852848145, -2.9763441039434335, -2.946861752186066, -2.9057494833858937, -2.853169548885461, -2.7893294576647545, -2.7144811573980583, -2.6289200401315913, -2.5329837765060454, -2.4270509831248424, -2.311539728327368, -2.1869058822642353, -2.0536413177860657, -1.9122719692460697, -1.7633557568774196, -1.60748038493699, -1.4452610223051456, -1.2773378746952186, -1.1043736580540333, -0.9270509831248426, -0.7460696614945644, -0.5621439437571737, -0.3759997006929136, -0.18837155858794075, -3.6739403974420594e-16, 0.18837155858794002, 0.37599970069291155, 0.5621439437571742, 0.7460696614945637, 0.9270509831248419, 1.1043736580540338, 1.277337874695218, 1.445261022305145, 1.6074803849369903, 1.7633557568774192, 1.9122719692460688, 2.053641317786066, 2.1869058822642344, 2.311539728327368, 2.427050983124842, 2.532983776506044, 2.628920040131591, 2.7144811573980583, 2.7893294576647545, 2.8531695488854605, 2.905749483385893, 2.946861752186066, 2.9763441039434335, 2.9940801852848145, 3.0, 2.9940801852848145, 2.9763441039434335, 2.946861752186066, 2.9057494833858932, 2.853169548885461, 2.7893294576647545, 2.7144811573980587, 2.6289200401315913, 2.532983776506045, 2.427050983124843, 2.311539728327369, 2.1869058822642344, 2.053641317786065, 1.912271969246071, 1.76335575687742, 1.607480384936989, 1.445261022305146, 1.277337874695219, 1.1043736580540335, 0.927050983124843, 0.7460696614945661, 0.562143943757174, 0.37599970069291394, 0.1883715585879398, 7.347880794884119e-16, -0.18837155858793833, -0.37599970069291255, -0.5621439437571752, -0.7460696614945621, -0.9270509831248415, -1.1043736580540346, -1.2773378746952178, -1.4452610223051447, -1.60748038493699, -1.7633557568774187, -1.91227196924607, -2.0536413177860657, -2.1869058822642335, -2.311539728327368, -2.4270509831248415, -2.532983776506044, -2.628920040131591, -2.714481157398059, -2.7893294576647536, -2.8531695488854605, -2.9057494833858937, -2.9468617521860656, -2.9763441039434335, -2.9940801852848145, -3.0, -2.9940801852848145, -2.9763441039434335, -2.9468617521860656, -2.9057494833858932, -2.853169548885461, -2.789329457664755, -2.71448115739806, -2.62892004013159, -2.532983776506045, -2.427050983124843, -2.311539728327369, -2.1869058822642367, -2.0536413177860653, -1.9122719692460692, -1.76335575687742, -1.6074803849369916, -1.4452610223051487, -1.2773378746952169, -1.104373658054034, -0.9270509831248434, -0.7460696614945613, -0.562143943757177, -0.375999700692917, -0.18837155858794016, -1.102182119232618e-15, 0.18837155858793797, 0.3759997006929148, 0.5621439437571696, 0.7460696614945643, 0.9270509831248412, 1.1043736580540318, 1.2773378746952198, 1.4452610223051465, 1.6074803849369852, 1.7633557568774183, 1.9122719692460675, 2.0536413177860635, 2.1869058822642353, 2.3115397283273675, 2.4270509831248415, 2.532983776506044, 2.628920040131589, 2.714481157398059, 2.789329457664754, 2.85316954888546, 2.905749483385893, 2.9468617521860656, 2.9763441039434335, 2.9940801852848145, 3.0, 2.9940801852848145, 2.976344103943434, 2.946861752186067, 2.9057494833858937, 2.8531695488854614, 2.789329457664755, 2.714481157398058, 2.628920040131593, 2.5329837765060454, 2.4270509831248432, 2.3115397283273693, 2.1869058822642335, 2.0536413177860657, 1.9122719692460737, 1.7633557568774205, 1.6074803849369919, 1.445261022305149, 1.2773378746952173, 1.1043736580540342, 0.9270509831248437, 0.7460696614945668, 0.5621439437571774, 0.375999700692912, 0.18837155858794052]

r = 0
x = []
for i in range(0,200):
    x.append(r + i*0.001)



fig,ax = plt.subplots()
ax.plot(x, y1, linestyle='--', label="input signal")
ax.plot(x, y2, label="output signal")

plt.legend(loc="upper left")

plt.xticks((0, 0.1, 0.2))

plt.xlabel('time[s]')
plt.ylabel('voltage[V]')
plt.show()

