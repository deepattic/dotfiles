(){
	local file=
	for file in $HOME/.config/zsh/<->-*.zsh(n); do
		. $file
	done
} "$@"
