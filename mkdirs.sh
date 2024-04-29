#!/bin/bash
for i in {1..7}; do
  dir="lesson$i"

  if [ ! -d "$dir" ]; then
    mkdir "$dir"
  fi

  if [ ! -f "$dir/not-empty" ]; then
    touch "$dir/not-empty"
  fi
done

dir="bonus1"
if [ ! -d "$dir" ]; then
  mkdir "$dir"
fi

if [ ! -f "$dir/not-empty" ]; then
  touch "$dir/not-empty"
fi
