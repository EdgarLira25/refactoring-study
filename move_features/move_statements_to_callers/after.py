from datetime import datetime
from move_features.move_statements_to_callers.shared import Person, Photo, Stream


class BillingServiceAfter:

    def render_person(self, out_stream: Stream, person: Person):
        out_stream.write(f"<p>{person.name}</p>\n")

    def render_photo(self, out_stream: Stream, photo: Photo):
        self.emit_photo_data(out_stream, photo)
        out_stream.write(f"<p>location: {photo.location}</p>\n")

    def list_recent_photos(self, out_stream: Stream, photos: list[Photo]):
        for photo in photos:
            if photo.date < datetime(2026, 1, 1):
                continue
            out_stream.write("<div>\n")
            self.emit_photo_data(out_stream, photo)
            out_stream.write(f"<p>location: {photo.location}</p>\n")
            out_stream.write("</div>\n")

    def emit_photo_data(self, out_stream: Stream, photo: Photo):
        out_stream.write(f"<p>title: {photo.title}</p>\n")
        out_stream.write(f"<p>date: {photo.date}</p>\n")
        
