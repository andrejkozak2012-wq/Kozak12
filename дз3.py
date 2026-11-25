import inspect
import colorama
from colorama import Fore, Back, Style, init, deinit


def inspect_colorama():
    print("=== COLORAMA LIBRARY INTROSPECTION ===")

    # 1. Inspecting the main package contents using dir()
    # This reveals the core components exposed by the colorama library.
    print("\n--- 1. Main public attributes and classes in colorama ---")
    public_members = [m for m in dir(colorama) if not m.startswith("_")]
    for member in public_members:
        print(f"Public component: {member}")

    # 2. Inspecting Fore class (Foreground text colors)
    # Using introspection to list available text color attributes.
    print("\n--- 2. Inspecting Fore class attributes (Text Colors) ---")
    fore_colors = [
        attr for attr in dir(Fore)
        if not attr.startswith("_") and not inspect.isroutine(getattr(Fore, attr))
    ]
    for color in fore_colors:
        print(f"Available text color: {color}")

    # 3. Inspecting init function using the inspect module
    # Examining parameters and documentation of the initialization function.
    print("\n--- 3. Inspecting init() function details ---")
    init_signature = inspect.signature(init)
    print(f"init() signature: {init_signature}")

    if init.__doc__:
        doc_summary = init.__doc__.strip().splitlines()[0]
        print(f"init() description: {doc_summary}")

    # 4. Demonstrating functionality discovered through introspection
    print("\n--- 4. Demonstrating Colorama usage ---")
    init(autoreset=True)  # Automatically resets color after each print

    print(Fore.GREEN + "Success: Colorama is installed and working!")
    print(Back.CYAN + Fore.BLACK + "Info: Background and text colors applied successfully.")
    print(Style.BRIGHT + "Warning: Bright style text example.")


if __name__ == "__main__":
    inspect_colorama()