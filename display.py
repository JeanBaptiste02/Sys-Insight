import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from system_info import get_system_info
from cpu_info import get_cpu_info
from storage_info import get_storage_info
from network_info import get_network_info
from gpu_info import get_gpu_info
from additional_info import get_additional_info
from memory_info import get_memory_info

def display_info():
    system_info = get_system_info()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    storage_info = get_storage_info()
    network_info = get_network_info()
    gpu_info = get_gpu_info()
    additional_info = get_additional_info()

    info_window = tk.Tk()
    info_window.title("PC Information")

    # Conteneur principal
    main_frame = tk.Frame(info_window)
    main_frame.pack(padx=10, pady=10)

    # Frame pour les informations textuelles à gauche
    text_frame = tk.Frame(main_frame)
    text_frame.pack(side=tk.LEFT, padx=10)

    info_label = tk.Label(text_frame, text="System Information:\n", justify=tk.LEFT)
    info_label.grid(row=0, column=0, sticky=tk.W)

    for i, (key, value) in enumerate(system_info.items(), start=1):
        label = tk.Label(text_frame, text=f"{key}: {value}", justify=tk.LEFT)
        label.grid(row=i, column=0, sticky=tk.W)

    for i, (key, value) in enumerate(cpu_info.items(), start=len(system_info) + 2):
        label = tk.Label(text_frame, text=f"{key}: {value}", justify=tk.LEFT)
        label.grid(row=i, column=0, sticky=tk.W)

    for i, (key, value) in enumerate(memory_info.items(), start=len(system_info) + len(cpu_info) + 3):
        label = tk.Label(text_frame, text=f"{key}: {value} bytes", justify=tk.LEFT)
        label.grid(row=i, column=0, sticky=tk.W)
        
    for i, (key, value) in enumerate(additional_info.items(), start=len(system_info) + len(cpu_info) + len(memory_info) + len(storage_info) + len(network_info) + len(gpu_info) + 7):
        label = tk.Label(text_frame, text=f"{key}: {value}", justify=tk.LEFT)
        label.grid(row=i, column=0, sticky=tk.W)


    # Frame pour les graphiques à droite
    graph_frame = tk.Frame(main_frame)
    graph_frame.pack(side=tk.RIGHT)

    # Création du graphique CPU
    cpu_figure = Figure(figsize=(5, 4), dpi=100)
    cpu_subplot = cpu_figure.add_subplot(111)
    cpu_subplot.bar(['Logical CPUs', 'CPU Cores'], [cpu_info['Logical CPUs'], cpu_info['CPU Cores']])
    cpu_subplot.set_title('CPU Information')

    # Intégration du graphique CPU dans Tkinter
    cpu_canvas = FigureCanvasTkAgg(cpu_figure, master=graph_frame)
    cpu_canvas.draw()
    cpu_canvas.get_tk_widget().pack()

    # Création du graphique de la mémoire
    memory_figure = Figure(figsize=(5, 4), dpi=100)
    memory_subplot = memory_figure.add_subplot(111)
    memory_subplot.bar(['Used RAM', 'Available RAM'], [memory_info['Used RAM'], memory_info['Available RAM']])
    memory_subplot.set_title('Memory Information')

    # Intégration du graphique de la mémoire dans Tkinter
    memory_canvas = FigureCanvasTkAgg(memory_figure, master=graph_frame)
    memory_canvas.draw()
    memory_canvas.get_tk_widget().pack()

    info_window.mainloop()