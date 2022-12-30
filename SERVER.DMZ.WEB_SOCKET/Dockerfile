FROM alpine:3.17

RUN mkdir -p /app /scripts /logs \
    /assets/sound/speech_content \
    /usr/local/etc/AUTOME_AI/DMZ.WEB_SOCKET/.config \
    /usr/local/etc/AUTOME_AI/DMZ.WEB_SOCKET/.info \
    /usr/local/etc/AUTOME_AI/DMZ.WEB_SOCKET/.keys \
    /usr/local/etc/AUTOME_AI/DMZ.WEB_SOCKET/.cert \
    /usr/local/include/AUTOME_AI/DMZ.WEB_SOCKET/.dump \
    /usr/local/bin/AUTOME_AI/DMZ.WEB_SOCKET/

COPY app_data/config/* /usr/local/etc/AUTOME_AI/DMZ.WEB_SOCKET/.config/
COPY app_data/key_pair/cert /usr/local/etc/AUTOME_AI/DMZ.WEB_SOCKET/.cert
COPY app_data/key_pair/keys /usr/local/etc/AUTOME_AI/DMZ.WEB_SOCKET/.keys
COPY app_data/bin /usr/local/bin/AUTOME_AI/DMZ.WEB_SOCKET/
COPY app_data/scripts /scripts

RUN addgroup -S app_group && adduser -S app_user -G app_group
USER app_user

WORKDIR /app

# CMD /scripts/init.sh
