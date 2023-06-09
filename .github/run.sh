#!/bin/bash

set -e

no_test=0
no_lint=0

while (( $# > 0 )); do
   case "$1" in
   	--help)
			printf "run.sh [OPTION]... [DIR]\n"
			printf "options:\n"
			printf "\t--help			Show help\n"
			printf "\t--no-test		Skip tests\n"
			printf "\t--no-lint		Skip linting\n"
			exit 0
      	;;
      --no-test)
			no_test=1
			shift
      	;;
      --no-lint)
			no_lint=1
			shift
			;;
		*)
			break
	      ;;
   esac
done

manifests=()
if [[ -z "$1" ]]; then
	manifests=(**/*_test.py)
else
	manifests+=("$1"/*_test.py)
fi

green='\033[1;32m'
no_color='\033[0m'
for m in "${manifests[@]}"; do
	name="$(dirname "$(readlink -f "$m")")"
	name="$(basename "$name")"

	printf "Project dir: %b%s%b\n" "$green" "$name" "$no_color"

	if (( no_test == 0 )); then
	  PYTHONPATH="$name" python3 -m unittest -v "$m"
	fi

	if (( no_lint == 0 )); then
		if [[ -x "$(command -v flake8)" ]]; then
			flake8
		else
			printf "flake8 not found\n"
		fi
	fi
done