import pyrtl

# Declaration
input0 = pyrtl.Input(1, "input0")
input1 = pyrtl.Input(1, "input1")
input2 = pyrtl.Input(1, "input2")
input3 = pyrtl.Input(1, "input3")
s0 = pyrtl.Input(1, "selector0")
s1 = pyrtl.Input(1, "selector1")
out = pyrtl.Output(1, "out")

# MUX logic
out <<= (
    (input0 & ~s1 & ~s0)
    | (input1 & ~s1 & s0)
    | (input2 & s1 & ~s0)
    | (input3 & s1 & s0)
)

print("--- 4 x 1 MUX Implementation ---")

# Simulation
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

# Test one case of an input set: "input0": 1, "input1": 0, "input2": 1, "input3": 0


for s0_val in range(2):
    for s1_val in range(2):
        sim.step(
            {
                "input0": 1,
                "input1": 0,
                "input2": 1,
                "input3": 0,
                "selector0": s0_val,
                "selector1": s1_val,
            }
        )

sim_trace.print_trace()
print("")
sim_trace.render_trace(
    ["input0", "input1", "input2", "input3", "selector0", "selector1"]
)

exit(0)
