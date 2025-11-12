#!/usr/bin/python3

import os 

def generate_invitations(template, attendees):

    """
    Foncion qui permet de contrôler le type de valeur
    dans les paramètres :
    
      => templates / string.
      => attenddees / list.
    
    La fonction contrôle également les valeurs dans la base de
    donnée afin de chercher des correspondance, de remplir les
    valeurs vides par 'N/A'.
    """

    if not isinstance(template, str):
        print("Template is not a string")
        return
    if not isinstance (attendees, list):
        print("Attendees is not a list")
        return
    if not template:    
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return


    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        name_value = attendee.get("name", "N/A")
        if name_value is None:
            name_value = "N/A"
        invitation = invitation.replace("{name}", name_value)


        event_title_value = attendee.get("event_title", "N/A")
        if event_title_value is None:
            event_title_value = "N/A"
        invitation = invitation.replace("{event_title}", event_title_value)


        event_date_value = attendee.get("event_date", "N/A")
        if event_date_value is None:
            event_date_value = "N/A"
        invitation = invitation.replace("{event_date}", event_date_value)


        event_location_value = attendee.get("event_location", "N/A")
        if event_location_value is None:
            event_location_value = "N/A"
        invitation = invitation.replace("{event_location}", event_location_value)

        with open(f"output_{index}.txt", "w") as file:
            file.write(invitation)

