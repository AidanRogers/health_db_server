from brian2 import *
tau_ = 20*ms
tau_e = 5*ms
tau_i = 10*ms
V_th = -50*mV
E_L = -60*mV
I_const = 11*mV
eqs = '''
dv/dt = (-(v-E_L) + I_const + g_e + g_i)/ tau_m : volt
dg_e/dt = -g_e/tau_e : volt
dg_i/dt = -g_i/tau_i : volt
'''

P = NeuronGroup(4000, model=eqs,
                threshold = 'v>V_th', reset = 'v=E__L')
P.v = 'E_L+10*mV*rand()'
Pe = P[:3200]
Pi = P[3200:]

w_e = 1.62*mV
w_i = 9*mv
Ce = Synapses(Pe, P, pre='g_e+=w_e')
Ci = Synapses(Po, P, pre='g_i-=w_i')
Ce.connect(True, p=0.02)
Ci.connect(True, p=0.02)

M = SpikeMonitor(P)

run(1*second)
plot(M.t/ms, M.i, '.')
xlabel('Time(in ms)'); ylabel('NeuronNumber')
show()