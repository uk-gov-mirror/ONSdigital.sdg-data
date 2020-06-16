from sdg.open_sdg import open_sdg_check

# alter meta
def alter_meta(meta):
    meta['indicator_number'] = meta['indicator']
    return meta

# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml', alter_meta=alter_meta)

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
