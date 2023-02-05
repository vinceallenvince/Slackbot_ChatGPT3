from google.cloud import secretmanager

class Secrets():
	def __init__(self, project_id):
		self.project_id = project_id
	
	def __str__(self):
		return f"project_id: {self.project_id}"

	def access_secret_version(self, secret_id, version_id="latest"):
    
    	# Create the Secret Manager client.
		client = secretmanager.SecretManagerServiceClient()
	
    	# Build the resource name of the secret version.
		name = f"projects/{self.project_id}/secrets/{secret_id}/versions/{version_id}"

    	# Access the secret version.
		response = client.access_secret_version(name=name)

   		# Return the decoded payload.
		return response.payload.data.decode('UTF-8')
