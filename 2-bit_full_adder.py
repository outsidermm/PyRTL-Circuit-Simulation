import pyrtl

# Declaration
a1 = pyrtl.Input(1, "a1")
a0 = pyrtl.Input(1, "a0")
b1 = pyrtl.Input(1, "b1")
b0 = pyrtl.Input(1, "b0")
cin = pyrtl.Input(1, "cin")


sum1 = pyrtl.Output(1, "sum1")
sum0 = pyrtl.Output(1, "sum0")
cout = pyrtl.Output(1, "cout")

# Logic
sum0 <<= a0 ^ b0 ^ cin
cout1 = (a0 & b0) | (cin & (a0 ^ b0))

sum1 <<= a1 ^ b1 ^ cout1
cout2 = (a1 & b1) | (cout1 & (a1 ^ b1))
cout <<= cout1 | cout2


print("--- Two Bit Full Adder Implementation ---")

# Simulation
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

for a1_val in range(2):
    for a0_val in range(2):
        for b1_val in range(2):
            for b0_val in range(2):
                for cin_val in range(2):
                    sim.step(
                        {
                            "a1": a1_val,
                            "a0": a0_val,
                            "b1": b1_val,
                            "b0": b0_val,
                            "cin": cin_val,
                        }
                    )


sim_trace.print_trace()
print("")
sim_trace.render_trace(["a1", "a0", "b1", "b0", "cin", "sum1", "sum0", "cout"])

exit(0)
