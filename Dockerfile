FROM semtech/mu-python-template:2.0.0-beta.2
LABEL maintainer="Sergio Fenoll <sergio@fenoll.be>"

# Microsoft fonts (used by the administration)
# and WeasyPrint dependency
RUN apt update && \
  apt install -y software-properties-common && \
  apt-add-repository contrib && \
  apt update && \
  apt install -y ttf-mscorefonts-installer libpango1.0-dev && \
  rm -rf /var/lib/apt/lists/*

# Flanders fonts
RUN mkdir /usr/share/fonts/truetype/flanders
ADD ./fonts/ /usr/share/fonts/truetype/flanders/
RUN fc-cache -fv
