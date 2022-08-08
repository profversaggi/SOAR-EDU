#!/usr/bin/env bash

THISDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
echo $THISDIR

export SOAR_HOME="$THISDIR/SoarSuite_9.6.0-Multiplatform_64bit/bin"
export DYLD_LIBRARY_PATH="$SOAR_HOME"

pushd $THISDIR/test-domains > /dev/null
java -Djava.library.path="$SOAR_HOME" -jar Mario-Soar.jar $1 $2
popd > /dev/null
