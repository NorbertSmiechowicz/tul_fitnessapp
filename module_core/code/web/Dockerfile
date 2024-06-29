FROM maven:3.8.5-openjdk-17-slim as builder
WORKDIR /app
COPY pom.xml .
# Caching dependecies, so they're not downloaded with each build
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn clean package

FROM openjdk:17-slim
WORKDIR /app
COPY --from=builder /app/target/*.jar ./app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]