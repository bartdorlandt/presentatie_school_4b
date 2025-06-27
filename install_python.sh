#!/bin/bash
env \
  LDFLAGS="-L/opt/homebrew/opt/tcl-tk@8/lib" \
  CPPFLAGS="-I/opt/homebrew/opt/tcl-tk@8/include" \
  PKG_CONFIG_PATH="/opt/homebrew/opt/tcl-tk@8/lib/pkgconfig" \
  pyenv install 3.12.3