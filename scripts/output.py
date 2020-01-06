import sdg

opensdg_output = sdg.outputs.OutputOpenSdg(
    inputs=inputs,
    schema=schema,
    output_folder='_site',
    translations=translations,
    reporting_status_extra_fields=['un_designated_tier'])
