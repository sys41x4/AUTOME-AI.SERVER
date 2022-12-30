FROM alpine:3.17

RUN apk update
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip

RUN mkdir -p /app /scripts \
    /assets/sound/speech_content \
    /usr/local/etc/AUTOME_AI/MASS_STORAGE/.config \
    /usr/local/etc/AUTOME_AI/MASS_STORAGE/.info \
    /usr/local/etc/AUTOME_AI/MASS_STORAGE/.keys \
    /usr/local/etc/AUTOME_AI/MASS_STORAGE/.cert \
    /usr/local/include/AUTOME_AI/MASS_STORAGE/.dump \
    /usr/local/bin/AUTOME_AI/MASS_STORAGE/

COPY app_data/config/* /usr/local/etc/AUTOME_AI/MASS_STORAGE/.config/
COPY app_data/key_pair/cert /usr/local/etc/AUTOME_AI/MASS_STORAGE/.cert
COPY app_data/key_pair/keys /usr/local/etc/AUTOME_AI/MASS_STORAGE/.keys
COPY app_data/bin /usr/local/bin/AUTOME_AI/MASS_STORAGE/
COPY app_data/scripts /scripts

RUN addgroup -S app_group && adduser -S app_user -G app_group

USER app_user

RUN pip install -r /usr/local/etc/AUTOME_AI/MASS_STORAGE/.config/mass_storage.requirements.txt

WORKDIR /app

CMD /bin/sh /scripts/init.sh
