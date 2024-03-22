import pyrtl

# Declaration
a, b, cin = pyrtl.Input(1, "a"), pyrtl.Input(1, "b"), pyrtl.Input(1, "cin")
sum, cout = pyrtl.Output(1, "sum"), pyrtl.Output(1, "cout")

# Logic
sum <<= a ^ b ^ cin
cout <<= (a & b) | (cin & (a ^ b))


print("--- One Bit Full Adder Implementation ---")

# Simulation
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

for a_val in (0, 1):
    for b_val in (0, 1):
        for cin_val in (0, 1):
            sim.step({"a": a_val, "b": b_val, "cin": cin_val})
sim_trace.print_trace()
print("")
sim_trace.render_trace(["a", "b", "cin", "sum", "cout"])

exit(0)
