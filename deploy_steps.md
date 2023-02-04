### How to build and deploy to Google Cloud

* Create an image repository with [Google Cloud Artifact Registry](https://cloud.google.com/artifact-registry)

* Create [Dockerfile](https://docs.docker.com/engine/reference/builder/), .dockerignore

    * Follow these [instructions](https://stackoverflow.com/questions/31198835/can-we-pass-env-variables-through-cmd-line-while-building-a-docker-image-through) to pass environment vars when building the Docker image

* Create a Cloud Build [config file](https://cloud.google.com/build/docs/build-push-docker-image#build_an_image_using_a_build_config_file)

    Follow these [instructions](https://stackoverflow.com/questions/66223475/google-cloud-build-pass-environment-variable-for-dockerfile) to pass environment vars from the command line to the cloudbuild YAML file. More [info](https://cloud.google.com/sdk/gcloud/reference/builds/submit#--substitutions) on the substitions flag.

* After the build pushes the image to Artifact Registry, deploy the image to GCE. When creating a VM Instance:

    * Create in the same region as the artifactory repo
    * Allow full access to all Cloud APIs

