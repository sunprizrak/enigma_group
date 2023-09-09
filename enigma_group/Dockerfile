FROM python:3.12.0rc1-alpine3.18 as builder

WORKDIR /usr/src/enigma_group

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY . .

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/enigma_group/wheels -r requirements.txt



FROM python:3.12.0rc1-alpine3.18

# create directory for the app
RUN mkdir -p /home/enigma_group

# create the app user
RUN addgroup -S enigma_group && adduser -S enigma_group -G enigma_group

# create the appropriate directories
ENV HOME=/home/enigma_group
ENV APP_HOME=/home/enigma_group/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/enigma_group/wheels /wheels
COPY --from=builder /usr/src/enigma_group/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R enigma_group:enigma_group $APP_HOME

# change to the app user
USER enigma_group

ENTRYPOINT ["sh", "/home/enigma_group/web/entrypoint.sh"]