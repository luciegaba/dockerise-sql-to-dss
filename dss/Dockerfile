
FROM dataiku/dss:10.0.5
# download mysql-connector
RUN curl https://cdn.mysql.com//Downloads/Connector-J/mysql-connector-java-8.0.29.tar.gz -o mysql-connector.tar.gz
RUN tar -xvzf mysql-connector.tar.gz

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /home/dataiku/entrypoint.sh
RUN chmod +x /home/dataiku/entrypoint.sh