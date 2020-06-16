from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
    meta['indicator_number'] = meta['indicator']
    return meta

open_sdg_build(config='config_data.yml', alter_meta=alter_meta)
