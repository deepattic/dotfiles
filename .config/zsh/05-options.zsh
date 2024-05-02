env=(
    'EDITOR=nvim'
    )

for env in "${env[@]}"; do
    export $env
done

. "$HOME/.cargo/env"
eval "$(starship init zsh)"
