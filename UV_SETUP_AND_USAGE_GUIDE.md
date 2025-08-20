# UV Setup and Usage Guide

This guide will walk you through the installation and usage of uv, a fast and efficient Python package manager written in Rust. It supports multiple installation methods and provides instructions on upgrading and managing your `uv` environment.

## Installing `uv`

There are multiple ways to install uv, depending on your platform and preference. Below are the available methods:

### Standalone Installer

The easiest way to install uv is through the standalone installer. This method is available for both **macOS** and **Linux** as well as **Windows**.

#### macOS and Linux

For **macOS** and **Linux**, use the following commands to download and install uv:

``` bash
curl -sSf https://astral.sh/uv/install.sh | bash
```

#### Windows

On **Windows**, use PowerShell to download and execute the installation script:

``` bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

You can request a specific version of uv by specifying it in the URL:

``` bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.8.12/install.ps1 | iex"
```

**Tip**: You can inspect the installation script before use by running the following:

``` bash
powershell -c "irm https://astral.sh/uv/install.ps1 | more"
```

Alternatively, you can download the installer or binaries directly from GitHub.

For more details, check the reference documentation on customizing your uv installation.

### PyPI (Python Package Index)

For Python-based environments, **uv** is available on **PyPI*** and can be installed using `pip` or `pipx`:

Using `pipx` (recommended for isolated environments):

``` bash
pipx install uv
```

Using `pip`:

``` bash
pip install uv
```

**Note**: If a prebuilt wheel is not available for your platform, uv will be built from source, which requires a Rust toolchain. If you need guidance on building from source, please refer to the contributing setup guide.

### Homebrew

If you are on **macOS** or **Linux**, you can install **uv** via **Homebrew**:

``` bash
brew install uv
```

### WinGet (Windows)

For **Windows**, **uv** can be installed via **WinGet**:

``` bash
winget install --id=astral-sh.uv -e
```

### Scoop (Windows)

Alternatively, **uv** can be installed via **Scoop** on **Windows**:

``` bash
scoop install main/uv
```

### Docker

For users working with **Docker**, **uv** provides a Docker image, which can be pulled from the GitHub container registry:

``` bash
docker pull ghcr.io/astral-sh/uv
```

For more details on using **uv** within **Docker**, refer to the [guide on Docker usage](https://docs.astral.sh/uv/guides/docker).

### GitHub Releases

You can also download uv release artifacts directly from [GitHub Releases](https://github.com/astral-sh/uv/releases). Each release page includes binaries for all supported platforms and instructions for using the standalone installer.

### Cargo (Rust users)

For **Rust** developers, **uv** can be installed via **Cargo**. Note that this method builds **uv** from source:

``` bash
cargo install --git https://github.com/astral-sh/uv uv
```

This method requires a compatible Rust toolchain to build the package from source.

## Upgrading `uv`

### Self-Update (Standalone Installer)

If **uv** was installed via the standalone installer, you can update it easily by running:

``` bash
uv self update
```

**Tip**: When updating uv, it will re-run the installer and may modify your shell profiles. To prevent this, set the environment variable `UV_NO_MODIFY_PATH`=1 before updating.

### Using a Package Manager (e.g., PyPI)

If **uv** was installed via a package manager like `pip`, use the following command to update it:

``` bash
pip install --upgrade uv
```

## Uninstalling `uv`

To uninstall **uv**, use the appropriate method for your installation:

- **Standalone Installer**: Use the uninstallation command provided in the installer script or follow the instructions in the documentation.

- **PyPI**: Run the following command:

``` bash
pip uninstall uv
```

- **Homebrew**: If installed via Homebrew, run:

``` bash
brew uninstall uv
```

- **WinGet/Scoop**: Follow the uninstallation steps for WinGet or Scoop depending on your installation method.

## Using `uv`

Once **uv** is installed, you can start using it to manage your Python project dependencies and environments. Here are some basic commands to get started:

### Creating a Virtual Environment

To create a new virtual environment with uv, run:

``` bash
uv venv
```

This will create a `.venv` in your project directory, allowing you to manage dependencies for the project in isolation.

### Installing Dependencies

To install dependencies defined in a `pyproject.toml` file or a `requirements.txt`, use the following:

``` bash
uv pip install -r requirements.txt
```

You can also install specific packages:

``` bash
uv pip install <package-name>
```

### Running Scripts

To run Python scripts within your uv-managed environment, use:

``` bash
uv run <script.py>
```

This will execute the specified script within the virtual environment, ensuring that all dependencies are available.

## Additional Features and Guides

- [UV Features Overview](https://docs.astral.sh/uv/getting-started/features/)

- [UV Guide: Install Python](https://docs.astral.sh/uv/guides/install-python/)

- [UV Guide: Running Scripts](https://docs.astral.sh/uv/guides/scripts/)

- [UV Guide: Tools & Commands](https://docs.astral.sh/uv/guides/tools/)

- [UV Guide: Managing Projects](https://docs.astral.sh/uv/guides/projects/)

## Conclusion

**uv** is a powerful tool for managing Python environments and dependencies efficiently. With its ease of use and flexibility, it can be integrated into any Python-based project, providing improved performance and simplicity.

For more information, explore the [official documentation](https://docs.astral.sh/uv)  or refer to the guides available in this repository.