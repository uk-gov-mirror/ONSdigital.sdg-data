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

# Use SDG Translations for translations
tag = '0.8.2'
translations = sdg.translations.TranslationInputSdgTranslations(tag=tag)

opensdg_output = sdg.outputs.OutputOpenSdg(
    inputs=inputs,
    schema=schema,
    output_folder='_site',
    translations=translations,
    reporting_status_extra_fields=['un_designated_tier'])

# Validate the indicators.
validation_successful = opensdg_output.validate()

# If everything was valid, perform the build.
if validation_successful:
    opensdg_output.execute()
