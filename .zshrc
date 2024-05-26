# Set the directory we want to store zinit and plugins
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"

# Download Zinit, if it's not there yet
if [ ! -d "$ZINIT_HOME" ]; then
   mkdir -p "$(dirname $ZINIT_HOME)"
   git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi

# Source/Load zinit
source "${ZINIT_HOME}/zinit.zsh"

setopt extended_glob

HISTFILE=${XDG_DATA_HOME:-~/.local/share}/zsh/history
[[ -d $HISTFILE:h ]] || mkdir -p $HISTFILE:h
SAVEHIST=$(( 100 * 1000 ))
HISTSIZE=$(( 1.2 * SAVEHIST ))

setopt EXTENDED_HISTORY HIST_EXPIRE_DUPS_FIRST  HIST_IGNORE_ALL_DUPS HIST_IGNORE_DUPS  HIST_IGNORE_SPACE HIST_REDUCE_BLANKS HIST_SAVE_NO_DUPS INC_APPEND_HISTORY INC_APPEND_HISTORY SHARE_HISTORY

zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions

zinit snippet OMZP::git

zinit load 'zsh-users/zsh-history-substring-search'
zinit ice wait atload'_history_substring_search_config'

autoload -Uz compinit && compinit
zinit cdreplay -q


bindkey -v
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down
bindkey '^E' autosuggest-accept

export KEYTIMEOUT=1
echo -ne '\e[5 q'

zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"

my_alias=(
    "ls=eza --icons -h"
    "lt=eza -h --tree "
    )

for alias in "${my_alias[@]}"; do
    alias $alias
done


env=(
    'EDITOR=nvim'
    )

for env in "${env[@]}"; do
    export $env
done

# if [ -z "$TMUX" ]; then
#     tmux new
# else
#     tmux a
# fi



. "$HOME/.cargo/env"
eval "$(zoxide init --cmd cd zsh)"
eval "$(fzf --zsh)"
eval "$(starship init zsh)"

export GPG_TTY=$(tty)
