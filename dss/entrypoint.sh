#!/bin/sh
DIR="/home/dataiku/dss/lib/jdbc/"
if [ -d "$DIR" ]; then
  # Take action if $DIR exists. #
  cp /home/dataiku/mysql-connector-java-8.0.29/mysql-connector-java-8.0.29.jar /home/dataiku/dss/lib/jdbc/mysql-connector-java-8.0.29.jar
  echo "Installing config files in ${DIR}..."
else
  ###  Control will jump here if $DIR does NOT exists ###
  echo "Error: ${DIR} not found. Can not continue."
  exit 1
fi

exec "$@"