#!/bin/sh
if ps -ef | grep -v grep | grep as_filterer.py ; then
        exit 0
else
        python3 /home/danielpl/traffmon/as_filterer.py >> /home/danielpl/traffmon/as_filterer.log &
        exit 0
fi

