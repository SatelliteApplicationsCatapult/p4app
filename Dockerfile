FROM p4lang/p4app:latest

# Install the scripts we use to run and test P4 apps.
COPY docker/scripts /scripts
WORKDIR /scripts

ENTRYPOINT ["./p4apprunner.py"]
