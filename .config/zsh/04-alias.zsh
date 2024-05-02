my_alias=(
    "ls=eza --icons -h"
    "lt=eza -h --tree "
    )

for alias in "${my_alias[@]}"; do
    alias $alias
done
