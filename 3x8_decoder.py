import pyrtl

# Declaration
a = pyrtl.Input(1, "a")
b = pyrtl.Input(1, "b")
c = pyrtl.Input(1, "c")
d0 = pyrtl.Output(1, "d0")
d1 = pyrtl.Output(1, "d1")
d2 = pyrtl.Output(1, "d2")
d3 = pyrtl.Output(1, "d3")
d4 = pyrtl.Output(1, "d4")
d5 = pyrtl.Output(1, "d5")
d6 = pyrtl.Output(1, "d6")
d7 = pyrtl.Output(1, "d7")

# Decoder logic
d0 <<= ~a & ~b & ~c
d1 <<= ~a & ~b & c
d2 <<= ~a & b & ~c
d3 <<= ~a & b & c
d4 <<= a & ~b & ~c
d5 <<= a & ~b & c
d6 <<= a & b & ~c
d7 <<= a & b & c

print("--- 3 x 8 Decoder Implementation ---")

# Simulation
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

for a_val in range(2):
    for b_val in range(2):
        for c_val in range(2):
            sim.step({"a": a_val, "b": b_val, "c": c_val})

sim_trace.print_trace()
print("")
sim_trace.render_trace()

exit(0)
