import os
import sdg

# Input data from CSV files matching this pattern: tests/data/*-*.csv
data_pattern = os.path.join('data', '*-*.csv')
data_input = sdg.inputs.InputCsvData(path_pattern=data_pattern)

# Input metadata from YAML files matching this pattern: tests/meta/*-*.md
meta_pattern = os.path.join('meta', '*-*.md')
meta_input = sdg.inputs.InputYamlMdMeta(path_pattern=meta_pattern)

# Combine these inputs into one list.
inputs = [data_input, meta_input]

# Use a Prose.io file for the metadata schema.
schema_path = os.path.join('_prose.yml')
schema = sdg.schemas.SchemaInputOpenSdg(schema_path=schema_path)

# Pull in remote translations if needed.
    all_translations = []
    if 'translations' in options:
        for repo in options['translations']:
            # Support an "@" syntax for pinning to a git tag/branch/commit.
            parts = repo.split('@')
            tag = None
            if len(parts) == 2:
                repo = parts[0]
                tag = parts[1]
            all_translations.append(sdg.translations.TranslationInputSdgTranslations(
                source=repo, tag=tag
            ))
    # Also include local translations from a 'translation' folder if present.
    translation_dir = os.path.join(options['src_dir'], 'translations')
    if os.path.isdir(translation_dir):
        all_translations.append(sdg.translations.TranslationInputYaml(source=translation_dir))

    # Indicate any extra fields for the reporting stats, if needed.
    reporting_status_extra_fields = []
    if 'reporting_status_extra_fields' in options:
        reporting_status_extra_fields = options['reporting_status_extra_fields']

opensdg_output = sdg.outputs.OutputOpenSdg(
    inputs=inputs,
    schema=schema,
    output_folder='_site',
    translations=all_translations,
    reporting_status_extra_fields=reporting_status_extra_fields)

# Validate the indicators.
validation_successful = opensdg_output.validate()

# If everything was valid, perform the build.
if validation_successful:
    opensdg_output.execute()
