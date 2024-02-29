from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import JSON  # Import JSON type specific to MySQL
from database import db

class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    animal_type = db.Column(db.String(20), nullable=False)  # Type of animal (e.g., cat, dog, bird)
    breed = db.Column(db.String(20), nullable=True)  # Optional, as not all animals have specific breeds
    tracking_device_id = db.Column(db.String(60), nullable=True)  # Not all animals may have a tracking device
    created_at = db.Column(db.DateTime, nullable=True)  # Optional creation timestamp
    last_seen_location = db.Column(db.String(500), nullable=True)  # To store the last known location
    last_seen_time = db.Column(db.DateTime, nullable=True)  # Timestamp of the last known location
    tracking_events = relationship("TrackingEvent", backref="animal")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'animal_type': self.animal_type,
            'breed': self.breed,
            'tracking_device_id': self.tracking_device_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_seen_location': self.last_seen_location,
            'last_seen_time': self.last_seen_time.isoformat() if self.last_seen_time else None,
            'tracking_events': [event.to_dict() for event in self.tracking_events] if self.tracking_events else None
        }

class TrackingEvent(db.Model):
    __tablename__ = 'tracking_events'
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'), nullable=False)
    event_type = db.Column(db.String(20), nullable=False)  # Differentiate inputs (e.g., 'location', 'image_capture', 'sensor_reading', 'eeg')
    event_data = db.Column(JSON, nullable=True)  # Store structured data for the event
    event_time = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'animal_id': self.animal_id,
            'event_type': self.event_type,
            'event_data': self.event_data,
            'event_time': self.event_time.isoformat()
        }
