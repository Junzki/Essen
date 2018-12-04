#!/bin/bash

CACHE_FILES=( "__pycache__" ".pytest_cache" )
ENV_FILE="local.env"

function clean_project {
    for pattern in ${CACHE_FILES[*]}
    do
        find . -name $pattern -exec rm -rfv {} +
    done
}

if [ -f $ENV_FILE ]; then
    echo "Load environments from $ENV_FILE"
    source $ENV_FILE
fi

if [[ -z "${ESSEN_SETTINGS_MODULE}" ]]; then
    echo "\$ESSEN_SETTINGS_MODULE not set, using default value."
    ESSEN_SETTINGS_MODULE="essen.settings"
fi

case $1 in
"clean")
    echo "Clean project."
    clean_project
    ;;

"test")
    pytest "${@:2}"
    ;;
*)
esac
