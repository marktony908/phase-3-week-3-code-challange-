
from db_setup import session, setup_database
from models import Band, Venue, Concert

setup_database()

# Create some bands and venues
band1 = Band(name="The Rolling Stones", hometown="London")
band2 = Band(name="Coldplay", hometown="London")

venue1 = Venue(title="Madison Square Garden", city="New York")
venue2 = Venue(title="O2 Arena", city="London")


session.add_all([band1, band2, venue1, venue2])
session.commit()

# Add concerts
concert1 = band1.play_in_venue(venue1, "2024-09-16")
concert2 = band2.play_in_venue(venue2, "2024-09-17")
session.add_all([concert1, concert2])
session.commit()

print(band1.venues)  
print(venue1.bands)  
print(concert1.introduction())  

print(Band.most_performances(session).name)  
