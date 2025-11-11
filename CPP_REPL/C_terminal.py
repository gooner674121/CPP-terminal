import os
import tempfile
import subprocess

print("Welcome to C-Terminal (created by Chase Stirling)!")
print("Type 'exit' to quit.")
print("Type 'run' to compile and execute your code.\n")
print("©2025 Dennis Ritchiem, Chase Stirling")
print("--------------------------------------------")

code_buffer = []

while True:
    line = input("C> ")

    # Exit command
    if line.strip() == "exit":
        break

    # Run command
    elif line.strip() == "run":
        if not code_buffer:
            print("No code to run!")
            continue

        # Create temporary C file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".c") as tmp:
            tmp.write("\n".join(code_buffer).encode())
            tmp_filename = tmp.name

        exe_filename = tmp_filename[:-2]  # remove .c extension

        # Compile the C code
        compile_cmd = ["gcc", tmp_filename, "-o", exe_filename]
        compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)

        if compile_result.returncode != 0:
            print("Compilation error:\n", compile_result.stderr)
        else:
            # Run compiled program
            run_result = subprocess.run([exe_filename], capture_output=True, text=True)
            print(run_result.stdout)
            if run_result.stderr:
                print(run_result.stderr)

        # Clear buffer after running
        code_buffer = []

        # Clean up temp files
        os.remove(tmp_filename)
        if os.path.exists(exe_filename):
            os.remove(exe_filename)

    # Add line to buffer
    else:
        code_buffer.append(line)
