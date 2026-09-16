export VENV="$HOME/minstallation/.venvs/KKIK_parse"
echo "Variable "VENV" refers to $VENV"
export  UV_PROJECT_ENVIRONMENT=$VENV
source "$VENV/bin/activate"
echo "uv project $VIRTUAL_ENV has been activated"