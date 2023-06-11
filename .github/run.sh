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

bin_dir=""
if [[ "$OSTYPE" == "darwin"* ]]; then
	bin_dir="./venv/bin/"
fi

basedir="${1:-.}"

if (( no_test == 0 )); then
  "$bin_dir"pytest "$basedir"
fi

if (( no_lint == 0 )); then
  "$bin_dir"flake8 "$basedir"
  "$bin_dir"pylint \
  --score n \
  --ignore-paths '^.*_test.py$' \
  --disable C0103,C0104,C0114,C0115,C0116 \
  "$basedir"/**/*.py
fi
