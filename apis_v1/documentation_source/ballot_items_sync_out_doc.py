# apis_v1/documentation_source/ballot_items_sync_out_doc.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-


def ballot_items_sync_out_doc_template_values(url_root):
    """
    Show documentation about ballotItemsSyncOut
    """
    required_query_parameter_list = [
        {
            'name':         'format',
            'value':        'string',  # boolean, integer, long, string
            'description':  'Currently must be \'json\' to work.',
        },
    ]
    optional_query_parameter_list = [
        {
            'name':         'google_civic_election_id',
            'value':        'integer',  # boolean, integer, long, string
            'description':  'Limit the ballot_items retrieved to those for this google_civic_election_id.',
        },
    ]

    potential_status_codes_list = [
    ]

    try_now_link_variables_dict = {
        'format': 'json',
    }

    api_response = '[{\n' \
                   '  "we_vote_id": string,\n' \
                   '  "ballot_item_display_name": string,\n' \
                   '  "contest_office_we_vote_id": string,\n' \
                   '  "contest_measure_we_vote_id": string,\n' \
                   '  "google_ballot_placement": string,\n' \
                   '  "google_civic_election_id": string,\n' \
                   '  "local_ballot_order": string,\n' \
                   '  "measure_subtitle": string,\n' \
                   '  "polling_location_we_vote_id": string,\n' \
                   '}]'

    template_values = {
        'api_name': 'ballotItemsSyncOut',
        'api_slug': 'ballotItemsSyncOut/?format=json',
        'api_introduction':
            "",
        'try_now_link': 'apis_v1:ballotItemsSyncOutView',
        'try_now_link_variables_dict': try_now_link_variables_dict,
        'url_root': url_root,
        'get_or_post': 'GET',
        'required_query_parameter_list': required_query_parameter_list,
        'optional_query_parameter_list': optional_query_parameter_list,
        'api_response': api_response,
        'api_response_notes':
            "",
        'potential_status_codes_list': potential_status_codes_list,
    }
    return template_values
