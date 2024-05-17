env=(
    'EDITOR=nvim'
    )

for env in "${env[@]}"; do
    export $env
done

. "$HOME/.cargo/env"
eval "$(zoxide init --cmd cd zsh)"
eval "$(fzf --zsh)"
eval "$(starship init zsh)"
