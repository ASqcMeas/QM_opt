
from qm.qua import *
import matplotlib.pyplot as plt
import warnings
from exp.readout_optimization import *
warnings.filterwarnings("ignore")

from datetime import datetime
import sys


# Dynamic config
from OnMachine.SetConfig.ConfigBuildUp_new import spec_loca, config_loca
from config_component.configuration import import_config
from config_component.channel_info import import_spec
from ab.QM_config_dynamic import initializer

spec = import_spec( spec_loca )
config = import_config( config_loca ).get_config()
qmm, _ = spec.buildup_qmm()
init_macro = initializer(100000,mode='wait')

ro_elements = ['q1_ro']
operate_qubit = ['q1_xy']
n_avg = 500

dfs = np.arange(-5e6, 5e6, 0.1e6)
output_data = freq_dep_signal( dfs, operate_qubit, ro_elements, n_avg, config, qmm, initializer=init_macro)
for r in ro_elements:
    fig = plt.figure()
    ax = fig.subplots(3,1)
    plot_freq_signal( dfs, output_data[r], r, ax )
    fig.suptitle(f"{r} RO freq")

plt.show()

#   Data Saving   # 
save_data = False
if save_data:
    from exp.save_data import save_npz
    import sys
    save_progam_name = sys.argv[0].split('\\')[-1].split('.')[0]  # get the name of current running .py program
    # save_npz(save_dir, save_progam_name, output_data)
