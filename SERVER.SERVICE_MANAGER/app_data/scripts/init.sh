#!/bin/sh

/usr/local/bin/ai_comm >> /logs/ai_comm.log &
/usr/local/bin/nlp_comm >> /logs/nlp_comm.log &

/usr/local/bin/usr_comm >> /logs/usr_comm.log &
/usr/local/bin/usr_iot_slaves_comm >> /logs/usr_iot_slaves_comm.log &
