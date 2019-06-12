#!/usr/bin/python3

import requests
import config
import html2text

def get_releasenote_from_gitlab():
    res = requests.get('{}/api/v4/projects/{}/releases'.format(config.GITLAB_URL,config.CI_PROJECT_ID), headers={"PRIVATE-TOKEN": config.PRIVATE_TOKEN})
    return res.json()
    
def get_releasenote_tag_description():
    releases = get_releasenote_from_gitlab()
    if not releases:
        return
    for tag in releases : 
        if config.CI_COMMIT_TAG == tag['tag_name']:
            return tag['description_html']
    
def convert_html_to_txt(html):
    convert = html2text.HTML2Text()
    return convert.handle(html)

html_release_notes = get_releasenote_tag_description()
if not html_release_notes: 
    print ("please add Release notes to your tag")
    exit (1)

clear_text_release_notes = convert_html_to_txt(html_release_notes)
print (clear_text_release_notes)