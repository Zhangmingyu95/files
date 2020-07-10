FROM registry.uih/library/java-base:8-jdk
ARG workdir=/home
WORKDIR ${workdir}
COPY robot-api-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8086
ENTRYPOINT ["java", "-jar", "app.jar"]
