ZSH_PLUGINS_PATH=$HOME/.local/share/zsh/plugins
fpath=($ZSH_PLUGINS_PATH/.local/share/zsh/plugins/zsh-completions/src $fpath)

autoload -U compinit && compinit
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"

plugins=(
    'zsh-autosuggestions/zsh-autosuggestions.zsh'
    'zsh-syntax-highlighting/zsh-syntax-highlighting.zsh'
    'zsh-history-substring-search/zsh-history-substring-search.zsh'
    )

for plugins in "${plugins[@]}"; do
    source $ZSH_PLUGINS_PATH/"$plugins"
done
