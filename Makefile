.PHONY: *

all: speakeasy


speakeasy: check-speakeasy
	speakeasy generate sdk --lang python -o . -s ./openapi.yaml

speakeasy-validate: check-speakeasy
	speakeasy validate openapi -s ./openapi.yaml

openapi:
	curl https://raw.githubusercontent.com/speakeasy-sdks-dev/apideck-sample-sdk/main/openapi.yaml > ./openapi.yaml

# This will replace the generation source in your workflow file with your local schema path
generate-from-local:
	@if ! which sed >/dev/null; then \
		echo "sed is not installed. Please install it using the following command:"; \
		echo "For Ubuntu/Debian: apt-get install sed"; \
		echo "For macOS: sed is pre-installed"; \
		exit 1; \
	fi
	@sed -i '' '/openapi_docs: |/{n;s|-.*|- ./openapi.yaml|;}' ./.github/workflows/speakeasy_sdk_generation.yml

check-speakeasy:
	@command -v speakeasy >/dev/null 2>&1 || { echo >&2 "speakeasy CLI is not installed. Please install before continuing."; exit 1; }
