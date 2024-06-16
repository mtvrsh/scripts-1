install_dir := env_var("HOME") / ".local/bin"

install file:
	cp -t "{{install_dir}}" "{{file}}"

uninstall file:
	rm -f "{{install_dir / file}}"
