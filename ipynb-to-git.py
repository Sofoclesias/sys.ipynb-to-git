import os
import tkinter as tk
import shutil
import subprocess

def add_git():
    config_file = os.path.expanduser("~/.jupyter/jupyter_notebook_config.py")

    if os.path.exists(config_file):
        print('Existe config file.')
        name = os.path.basename(config_file)
        shutil.copyfile(config_file, os.path.join('backup',name))
    else:
        batch_script_path = os.path.join(os.getcwd(), 'files/run_command.bat')
        process = subprocess.run(['cmd.exe', '/C', batch_script_path], capture_output=True, text=True)
        print('Output:', process.stdout)
        config_file = os.path.expanduser("~/.jupyter/jupyter_notebook_config.py")

    agregar = [
        """c.InteractiveShellApp.exec_lines = ["""
        """'exec(open(os.path.expanduser("~/files/jupyter_startup.py")).read())'"""
    """]"""   
    ]
    
    with open(config_file, 'a') as file:
        file.writelines(agregar)
        
    print('Excepción creada con éxito.')

def purge():
    config_file = os.path.expanduser("~/.jupyter/jupyter_notebook_config.py")

    if os.path.exists(r'backup\jupyter_notebook_config.py'):
        os.remove(config_file)
        shutil.move(r'backup\jupyter_notebook_config.py', config_file)
    else:
        os.remove(config_file)
        
    print('Reseteado a configuraciones iniciales.')
        
def gui():
    """
    Create the GUI.
    """
    root = tk.Tk()
    root.title("Optiones")

    add_button = tk.Button(root, text="Agregar .git a sys.path", command=add_git)
    add_button.pack(pady=10)

    purge_button = tk.Button(root, text="Purgar", command=purge)
    purge_button.pack(pady=10)

    root.mainloop()
    
if __name__ == "__main__":
    gui()