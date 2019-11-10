FROM python:3.8

RUN apt-get update && \
    # добавляем пользователя megafon
    useradd megafon && \
    usermod -aG sudo megafon && \
#    echo megafon:megafon1 | chpasswd && \
    git clone https://github.com/BaldrOdinson/mgf.git /home/megafon/mgf


# устанавливаем модули Python
RUN pip3 install --no-cache-dir -r /home/megafon/mgf/requirements.txt && \
    cat /home/ubuntu/build_info/build_no.txt > /home/megafon/mgf/test_app/core/build_info/build_no.txt && \
    export LC_ALL=C.UTF-8 && \
    export LANG=C.UTF-8

# порт
EXPOSE 9000
# запускаем gunicorn
CMD gunicorn --bind 0.0.0.0:9000 --chdir /home/megafon/mgf wsgi
