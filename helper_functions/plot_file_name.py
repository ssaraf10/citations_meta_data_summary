from pathlib import Path


def create_plot_file_name(filename):
    subfolder_name = "plots"

    # Get the root directory of PyCharm project
    root_dir = Path(__file__).parent.parent

    # Construct the full file path using pathlib
    file_path = root_dir / subfolder_name / filename

    return file_path