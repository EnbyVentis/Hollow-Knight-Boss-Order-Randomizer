import random
 
VengeflyKing = "Vengefly King"
VfKi = 0
#can be done first

GruzMother = "Gruz Mother"
GrMo = 1
#can be done first

FalseKnight = "False Knight"
FaKn = 2
#can be done first

MassiveMossCharger = "Massive Moss Charger"
MMCh = 3
#can be done first

HornetProtector = "Hornet (Protector)"
HoPr = 4
#can be done first

Gorb = "Gorb"
GORB = 5
#can be done first, get dashless mantis claw, then climb from King's Pass

DungDefender = "Dung Defender"
DuDe = 6
#Not certain, but your probably need Dash

SoulWarrior = "Soul Warrior"
SoWa = 7

BroodingMawlek = "Brooding Mawlek"
BrMa = 8

Xero = "Xero"
XERO = 9

CrystalGuardian = "Crystal Guardian"
CrGu = 10

SoulMaster = "Soul Master"
SoMa = 11

Oblobble = "Oblobbles"
Oblo = 12
#not certain what all you need to get there, will say dash is needed to be safe

MantisLords = "The Mantis Lords"
MaLo = 13

Marmu = "Marmu"
Marm = 14

Flukemarm = "Flukemarm"
Fluk = 15

BrokenVessel = "Broken Vessel"
BrVe = 16

Galien = "Galien"
Gali = 17

HiveKnight = "Hive Knight"
HiKn = 18

ElderHu = "Elder Hu"
ElHu = 19

Collector = "The Collector"
Coll = 20

GodTamer = "God Tamer"
GoTa = 21

TroupeMasterGrimm = "Troupe Master Grimm"
TMGr = 22

WatcherKnight = "The Watcher Knights"
WaKn = 23

Uumuu = "Uumuu"
Uumu = 24

Nosk = "Nosk"
NOSK = 25

HornetSentinel = "Hornet (Sentinel)"
HoSe = 26

EnragedGuardian = "Enraged Guardian"
EnGu = 27

LostKin = "Lost Kin"
LoKi = 28

NoEyes = "No Eyes"
NoEy = 29

TraitorLord = "Traitor Lord"
TrLo = 30

WhiteDefender = "White Defender"
WhDe = 31

SoulTyrant = "Soul Tyrant"
SoTy = 32

Markoth = "Markoth"
Mark = 33

GreyPrinceZote = "Grey Prince Zote"
GPZo = 34

FailedChampion = "Failed Champion"
FaCh = 35

NightmareKingGrimm = "Nightmare King Grimm"
NKGr = 36

HollowKnight = "The Hollow Knight"
HoKn = 37

Radiance = "Radiance"
Radi = 38

BossOrder = [VengeflyKing, GruzMother, FalseKnight, MassiveMossCharger, HornetProtector, Gorb, DungDefender, SoulWarrior, BroodingMawlek, Xero, CrystalGuardian, SoulMaster, Oblobble, MantisLords, Marmu, Flukemarm, BrokenVessel, Galien, HiveKnight, ElderHu, Collector, GodTamer, TroupeMasterGrimm, WatcherKnight, Uumuu, Nosk, HornetSentinel, EnragedGuardian, LostKin, NoEyes, TraitorLord, WhiteDefender, SoulTyrant, Markoth, GreyPrinceZote, FailedChampion, NightmareKingGrimm, HollowKnight, Radiance]

i = 0


while i == 0:
    random.shuffle(BossOrder)
    VfKi = BossOrder.index(VengeflyKing)
    GrMo = BossOrder.index(GruzMother)
    FaKn = BossOrder.index(FalseKnight)
    MMCh = BossOrder.index(MassiveMossCharger)
    HoPr = BossOrder.index(HornetProtector)
    GORB = BossOrder.index(Gorb)
    DuDe = BossOrder.index(DungDefender)
    SoWa = BossOrder.index(SoulWarrior)
    BrMa = BossOrder.index(BroodingMawlek)
    XERO = BossOrder.index(Xero)
    CrGu = BossOrder.index(CrystalGuardian)
    SoMa = BossOrder.index(SoulMaster)
    Oblo = BossOrder.index(Oblobble)
    MaLo = BossOrder.index(MantisLords)
    Marm = BossOrder.index(Marmu)
    Fluk = BossOrder.index(Flukemarm)
    BrVe = BossOrder.index(BrokenVessel)
    Gali = BossOrder.index(Galien)
    HiKn = BossOrder.index(HiveKnight)
    ElHu = BossOrder.index(ElderHu)
    Coll = BossOrder.index(Collector)
    GoTa = BossOrder.index(GodTamer)
    TMGr = BossOrder.index(TroupeMasterGrimm)
    WaKn = BossOrder.index(WatcherKnight)
    Uumu = BossOrder.index(Uumuu)
    NOSK = BossOrder.index(Nosk)
    HoSe = BossOrder.index(HornetSentinel)
    EnGu = BossOrder.index(EnragedGuardian)
    LoKi = BossOrder.index(LostKin)
    NoEy = BossOrder.index(NoEyes)
    TrLo = BossOrder.index(TraitorLord)
    WhDe = BossOrder.index(WhiteDefender)
    SoTy = BossOrder.index(SoulTyrant)
    Mark = BossOrder.index(Markoth)
    GPZo = BossOrder.index(GreyPrinceZote)
    FaCh = BossOrder.index(FailedChampion)
    NKGr = BossOrder.index(NightmareKingGrimm)
    HoKn = BossOrder.index(HollowKnight)
    Radi = BossOrder.index(Radiance)
    if TrLo < Radi and HoPr < DuDe and SoWa < SoMa and HoPr < Oblo and HoPr < MaLo and HoPr < Marm and DuDe < Fluk and HoPr < BrVe and HoPr < Gali and BrVe < HiKn and HoPr < Coll and Oblo < GoTa and BrVe < TMGr and HoPr < NOSK and BrVe < EnGu and CrGu < EnGu and BrVe < LoKi and GrMo < NoEy and HoSe < TrLo and WaKn < WhDe and Uumu < WhDe and DuDe < WhDe and SoMa < SoTy and HoSe < Mark and BrVe < GPZo and FaKn < FaCh and TMGr < NKGr and WaKn < HoKn and Uumu < HoKn and HoKn < Radi:
        print(BossOrder)
        break
    else:
        pass
