# running metabase locally

metabase-directory := .metabase
metabase-version := v0.35.4
metabase-db := example_project_1_metabase
metabase-connection-uri := postgres://127.0.0.1:5432/$(metabase-db)?user=root


run-metabase: $(metabase-directory)/metabase-$(metabase-version).jar
	cd $(metabase-directory); MB_DB_CONNECTION_URI=$(metabase-connection-uri) java -jar metabase-$(metabase-version).jar

$(metabase-directory)/metabase-$(metabase-version).jar:
	mkdir -pv $(metabase-directory)
	DISABLE_MAKESHELL wget --output-document=$@ --show-progress https://downloads.metabase.com/$(metabase-version)/metabase.jar

migrate-metabase-db: $(metabase-directory)/metabase-$(metabase-version).jar
	cd $(metabase-directory); MB_DB_CONNECTION_URI=$(metabase-connection-uri) java -jar metabase-$(metabase-version).jar migrate up

setup-metabase: migrate-metabase-db
	source .venv/bin/activate; flask app.metabase.setup

