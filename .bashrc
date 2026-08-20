cat << 'EOF' >> ~/.bashrc

# Auto-activate .venv if present in directory
cd() {
    builtin cd "$@" || return
    if [ -f ".venv/bin/activate" ]; then
        source .venv/bin/activate
    fi
}

# Auto-activate at shell startup if .venv exists in current folder
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi
EOF