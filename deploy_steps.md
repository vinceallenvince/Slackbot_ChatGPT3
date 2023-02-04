### How to build and deploy to Google Cloud

* Create an image repository with [Google Cloud Artifact Registry](https://cloud.google.com/artifact-registry)

* Create [Dockerfile](https://docs.docker.com/engine/reference/builder/), .dockerignore

    * Follow these [instructions](https://stackoverflow.com/questions/31198835/can-we-pass-env-variables-through-cmd-line-while-building-a-docker-image-through) to pass environment vars when building the Docker image

* Create a Cloud Build [config file](https://cloud.google.com/build/docs/build-push-docker-image#build_an_image_using_a_build_config_file)

    Follow these [instructions](https://stackoverflow.com/questions/66223475/google-cloud-build-pass-environment-variable-for-dockerfile) to pass environment vars from the command line to the cloudbuild YAML file. More [info](https://cloud.google.com/sdk/gcloud/reference/builds/submit#--substitutions) on the substitions flag.

* Run the cloud build command
	
	```
    gcloud builds submit --region=us-west2 --config cloudbuild.yaml --substitutions _SLACK_APP_GPT3_TOKEN=$SLACK_APP_GPT3_TOKEN,_SLACK_BOT_GPT3_TOKEN=$SLACK_BOT_GPT3_TOKEN,_OPENAI_API_KEY=$OPENAI_API_KEY
    ```

* If you get a "failed_precondition: due to quota restrictions, cannot run builds in this region" error, change the build region. For a list, https://cloud.google.com/build/docs/locations

