ZSH_PLUGINS_PATH=$HOME/.local/share/zsh/plugins
fpath=($ZSH_PLUGINS_PATH/.local/share/zsh/plugins/zsh-completions/src $fpath)

autoload -U compinit && compinit

source $ZSH_PLUGINS_PATH/zsh-autosuggestions/zsh-autosuggestions.zsh
source $ZSH_PLUGINS_PATH/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $ZSH_PLUGINS_PATH/zsh-history-substring-search/zsh-history-substring-search.zsh

eval "$(starship init zsh)"
