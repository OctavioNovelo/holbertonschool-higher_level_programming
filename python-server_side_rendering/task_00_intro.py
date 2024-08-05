import logging
import os

def generate_invitations(template, attendees):
    # Configurar el logger
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Verificar tipos de entrada
    if not isinstance(template, str):
        logging.error("Invalid input: template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Invalid input: attendees should be a list of dictionaries.")
        return
    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return
    for i, attendee in enumerate(attendees, start=1):
        try:
            # Reemplazar placeholders
            name = attendee.get("name", "N/A")
            event_title = attendee.get("event_title", "N/A")
            event_date = attendee.get("event_date", "N/A")
            event_location = attendee.get("event_location", "N/A")

            # Generar el contenido del archivo
            invitation = template.format(
                name=name,
                event_title=event_title,
                event_date=event_date,
                event_location=event_location
            )

            filename = f"output_{i}.txt"
            with open(filename, 'w') as file:
                file.write(invitation)
            
            print(f"Invitation {i} created: {filename}")

        except Exception as e:
            logging.error(f"Error processing attendee {i}: {e}")
            continue
