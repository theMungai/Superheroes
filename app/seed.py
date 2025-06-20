from app.models import Hero, Power, HeroPower

def seed_data(db):
    if Hero.query.first():
        return  

    h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    p1 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
    hp = HeroPower(strength="Strong", hero=h1, power=p1)

    db.session.add_all([h1, p1, hp])
    db.session.commit()
