class Computer:
    name: str

    def input_data_from_keyboard(self):
        print("Inputing data from a keyboard...")

    def store_data_to_internal_memory(self):
        print("Storing data to internal memory...")


    def retrieve_data_from_internal_memory(self):
        print("Retrieving data from internal memory...")


    def process_data_using_default_processing_unit(self):
        print("Processing data using default processing unit...")

    def output_data_on_screen(self):
        print("Outputting data on screen...")



    def connect_to_wifi(self):
        print("Connecting to Wi-Fi...")


    def connect_bluetooth_device(self):
        print("Connecting to Bluetooth device...")

 #computer object
computer = Computer()

#testing computer functionality
computer.input_data_from_keyboard()
computer.store_data_to_internal_memory()