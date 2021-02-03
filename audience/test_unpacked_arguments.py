class Unpacked_Arguments_Test1:

    def pour_from_sink(self, temperature="Warm", flow="Medium"):
        print(temperature)
        print(flow)

    # Our function takes two keyword arguments
    # If we make a dictionary with their parameter names...
    sink_open_kwargs = {
        'temperature': 'Super Hot',
        'flow': 'Super Slight',
    }

    # We can destructure them an pass to the function
    #pour_from_sink(**sink_open_kwargs)
    # Equivalent to the following:
    #pour_from_sink(temperature="Hot", flow="Slight")

if __name__ == '__main__':

    ua = Unpacked_Arguments_Test1()
    sink_open_kwargs = {
        'temperature': 'Super Hot',
        'flow': 'Super Slight',
    }
    ua.pour_from_sink(**sink_open_kwargs)