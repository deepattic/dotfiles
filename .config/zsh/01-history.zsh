setopt extended_glob

HISTFILE=${XDG_DATA_HOME:=~/.local/share}/zsh/history
# Just in case: If the parent directory doesn't exist, create it.
[[ -d $HISTFILE:h ]] ||
    mkdir -p $HISTFILE:h

# Max number of entries to keep in history file.
SAVEHIST=$(( 100 * 1000 ))      # Use multiplication for readability.

# Max number of history entries to keep in memory.
HISTSIZE=$(( 1.2 * SAVEHIST ))  # Zsh recommended value


setopt HIST_FCNTL_LOCK # Use modern file-locking mechanisms, for better safety & performance.
setopt HIST_IGNORE_ALL_DUPS # Keep only the most recent copy of each duplicate entry in history.
setopt SHARE_HISTORY # Auto-sync history between concurrent sessions.
