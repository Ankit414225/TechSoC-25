class Pokemon:
    def __init__(self,name,hp,attack,defence,speed,moves):
        self.name=name
        self.hp=hp
        self.att=attack
        self.defc=defence
        self.spd=speed
        self.mov=moves
    def attack(self,Pok2,i):
        if(i==0):
            print("Pikachu use Thundershock")
            Pok2.hp=Pok2.hp-(30+self.att-Pok2.defc)
            print(f"Charmander took {30+self.att-Pok2.defc} damage")
        elif (i==1):
            print("Pikachu use Quick attack")
            Pok2.hp=Pok2.hp-(20+self.att-Pok2.defc)
            print(f"Charmander took {20+self.att-Pok2.defc} damage")  
        elif (i==2):
            print("Pikachu use Thunderbolt")
            Pok2.hp=Pok2.hp-(80+self.att-Pok2.defc)
            print(f"Charmander took {80+self.att-Pok2.defc} damage")  
        elif (i==3):
            print("Pikachu use Thunder")
            Pok2.hp=Pok2.hp-(50+self.att-Pok2.defc)
            print(f"Charmander took {50+self.att-Pok2.defc} damage")
    def display_stats(self):
        if self.hp<0:
            self.hp=0
        print(f"{self.name}-HP:{self.hp},  Attack:{self.att},  Defence:{self.defc},  Speed:{self.spd},  Moves:{self.mov}")    
    def is_fainted(self):
        return self.hp==0
        

    
        

Pok1=Pokemon("Pikachu",100,55,40,90,["Thunder_shock(30)","Quick_Attack(20)","Thunderbolt(80)","Thunder(50)"])
Pok2=Pokemon("Charmander",90,52,43,65,["Ember(20)","Scratch(15)","Blaze(30)","Flamethrower(60)"])
Pok2.display_stats()
Pok1.attack(Pok2,2)
Pok2.display_stats()
print(f"Charmander fainted:{Pok2.is_fainted()}")
