{pkgs}: {
  deps = [
    pkgs.xcbuild
    pkgs.swig
    pkgs.openjpeg
    pkgs.mupdf
    pkgs.libjpeg_turbo
    pkgs.jbig2dec
    pkgs.harfbuzz
    pkgs.gumbo
    pkgs.freetype
    pkgs.python310Packages.openai         # OpenAI package for Python 3.10
    pkgs.python                           # Python interpreter
    pkgs.run                              # Run command (assuming a utility or package)
    pkgs.bash                             # Bash shell
    pkgs.python310                         # Python 3.10 interpreter
    pkgs.python310Packages.pip            # Python package installer
    pkgs.python310Packages.virtualenv     # Python virtual environment
    pkgs.python310Packages.wheel          # Python wheel package format support
    pkgs.python310Packages.setuptools     # Python package management
    pkgs.python310Packages.pymupdf        # PyMuPDF package for Python 3.10
    pkgs.ghostscript                      # Ghostscript for handling PDFs
  ];
}
