import customtkinter as ctk

ctk.set_appearance_mode("default")
ctk.set_default_color_theme("blue")


    #Temporary function
def submit_info():
    pass
    #Temporary function
    
    
    
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("900x750")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)

        self.input_message_label = ctk.CTkLabel(self, text="Message Input")
        self.input_message_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.output_message_label = ctk.CTkLabel(self, text="Response")
        self.output_message_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.my_answer = ctk.CTkTextbox(self, wrap="word")
        self.my_answer.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.output_textbox = ctk.CTkTextbox(self, state="disabled", wrap="word")
        self.output_textbox.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.submit_button = ctk.CTkButton(self, text="Sumbmit Asnswer", command= submit_info)
        self.submit_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")   
        
        self.ppron_label = ctk.CTkLabel(self, text="Personal Pronouns")
        self.ppron_label.grid(row=3, column=0, padx=0, pady=0, sticky="nws")
        
        self.ipron_label = ctk.CTkLabel(self, text="Impersonal Pronouns")
        self.ipron_label.grid(row=3, column=0, padx=0, pady=0, sticky="nw")
        
        self.aux_label = ctk.CTkLabel(self, text="Auxiliary verbs")
        self.aux_label.grid(row=3, column=0, padx=0, pady=0, sticky="sw")
        
        self.negations_label = ctk.CTkLabel(self, text="Negations")
        self.negations_label.grid(row=3, column=0, padx=150, pady=5, sticky="nw")
        
        self.adverb_label = ctk.CTkLabel(self, text="Adverbs")
        self.adverb_label.grid(row=3, column=0, padx=150, pady=0, sticky="nws")
        
        self.conjunctions_label = ctk.CTkLabel(self, text="Conjunctions")
        self.conjunctions_label.grid(row=3, column=0, padx=150, pady=0, sticky="sw")

if __name__ == "__main__":
    app = App()
    app.mainloop()

'''
import customtkinter as ctk

# Initialize the main window
app = ctk.CTk()
app.title("Custom Tkinter GUI")
app.geometry("600x400")

# Message Input Frame
message_input_frame = ctk.CTkFrame(app, width=280, height=350)
message_input_frame.grid(row=0, column=0, padx=10, pady=10)
message_input_label = ctk.CTkLabel(message_input_frame, text="Message Input")
message_input_label.pack(pady=5)
message_input_textbox = ctk.CTkTextbox(message_input_frame, width=260, height=200)
message_input_textbox.pack(pady=10)
submit_button = ctk.CTkButton(message_input_frame, text="Submit")
submit_button.pack(pady=10)

# Score Labels
ipr_label_input = ctk.CTkLabel(message_input_frame, text="IPR = 0")
ipr_label_input.pack(anchor="w")
pp_label_input = ctk.CTkLabel(message_input_frame, text="PP = 0")
pp_label_input.pack(anchor="w")
aux_label_input = ctk.CTkLabel(message_input_frame, text="AUX = 0")
aux_label_input.pack(anchor="w")
ns_label_input = ctk.CTkLabel(message_input_frame, text="NS = 0")
ns_label_input.pack(anchor="w")
apv_label_input = ctk.CTkLabel(message_input_frame, text="APV = 0")
apv_label_input.pack(anchor="w")
con_label_input = ctk.CTkLabel(message_input_frame, text="CON = 0")
con_label_input.pack(anchor="w")

# Response Frame
response_frame = ctk.CTkFrame(app, width=280, height=350)
response_frame.grid(row=0, column=1, padx=10, pady=10)
response_label = ctk.CTkLabel(response_frame, text="Response")
response_label.pack(pady=5)
response_textbox = ctk.CTkTextbox(response_frame, width=260, height=200)
response_textbox.pack(pady=10)

# Score Labels
ipr_label_response = ctk.CTkLabel(response_frame, text="IPR = 0")
ipr_label_response.pack(anchor="w")
pp_label_response = ctk.CTkLabel(response_frame, text="PP = 0")
pp_label_response.pack(anchor="w")
aux_label_response = ctk.CTkLabel(response_frame, text="AUX = 0")
aux_label_response.pack(anchor="w")
ns_label_response = ctk.CTkLabel(response_frame, text="NS = 0")
ns_label_response.pack(anchor="w")
apv_label_response = ctk.CTkLabel(response_frame, text="APV = 0")
apv_label_response.pack(anchor="w")
con_label_response = ctk.CTkLabel(response_frame, text="CON = 0")
con_label_response.pack(anchor="w")

# Run the app
app.mainloop()

'''