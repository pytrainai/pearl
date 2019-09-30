# OpenAI envs

from gym import envs
envids = [spec.id for spec in envs.registry.all()]
for envid in sorted(envids):
    print(envid)

'''
 Output:

 Acrobot-v1
Adventure-ram-v0
Adventure-ram-v4
Adventure-ramDeterministic-v0
Adventure-ramDeterministic-v4
Adventure-ramNoFrameskip-v0
Adventure-ramNoFrameskip-v4
Adventure-v0
Adventure-v4
AdventureDeterministic-v0
AdventureDeterministic-v4
AdventureNoFrameskip-v0
AdventureNoFrameskip-v4
AirRaid-ram-v0
AirRaid-ram-v4
AirRaid-ramDeterministic-v0
AirRaid-ramDeterministic-v4
AirRaid-ramNoFrameskip-v0
AirRaid-ramNoFrameskip-v4
AirRaid-v0
AirRaid-v4
AirRaidDeterministic-v0
AirRaidDeterministic-v4
AirRaidNoFrameskip-v0
AirRaidNoFrameskip-v4
Alien-ram-v0
Alien-ram-v4
Alien-ramDeterministic-v0
Alien-ramDeterministic-v4
Alien-ramNoFrameskip-v0
Alien-ramNoFrameskip-v4
Alien-v0
Alien-v4
AlienDeterministic-v0
AlienDeterministic-v4
AlienNoFrameskip-v0
AlienNoFrameskip-v4
Amidar-ram-v0
Amidar-ram-v4
Amidar-ramDeterministic-v0
Amidar-ramDeterministic-v4
Amidar-ramNoFrameskip-v0
Amidar-ramNoFrameskip-v4
Amidar-v0
Amidar-v4
AmidarDeterministic-v0
AmidarDeterministic-v4
AmidarNoFrameskip-v0
AmidarNoFrameskip-v4
Ant-v2
Ant-v3
Assault-ram-v0
Assault-ram-v4
Assault-ramDeterministic-v0
Assault-ramDeterministic-v4
Assault-ramNoFrameskip-v0
Assault-ramNoFrameskip-v4
Assault-v0
Assault-v4
AssaultDeterministic-v0
AssaultDeterministic-v4
AssaultNoFrameskip-v0
AssaultNoFrameskip-v4
Asterix-ram-v0
Asterix-ram-v4
Asterix-ramDeterministic-v0
Asterix-ramDeterministic-v4
Asterix-ramNoFrameskip-v0
Asterix-ramNoFrameskip-v4
Asterix-v0
Asterix-v4
AsterixDeterministic-v0
AsterixDeterministic-v4
AsterixNoFrameskip-v0
AsterixNoFrameskip-v4
Asteroids-ram-v0
Asteroids-ram-v4
Asteroids-ramDeterministic-v0
Asteroids-ramDeterministic-v4
Asteroids-ramNoFrameskip-v0
Asteroids-ramNoFrameskip-v4
Asteroids-v0
Asteroids-v4
AsteroidsDeterministic-v0
AsteroidsDeterministic-v4
AsteroidsNoFrameskip-v0
AsteroidsNoFrameskip-v4
Atlantis-ram-v0
Atlantis-ram-v4
Atlantis-ramDeterministic-v0
Atlantis-ramDeterministic-v4
Atlantis-ramNoFrameskip-v0
Atlantis-ramNoFrameskip-v4
Atlantis-v0
Atlantis-v4
AtlantisDeterministic-v0
AtlantisDeterministic-v4
AtlantisNoFrameskip-v0
AtlantisNoFrameskip-v4
BankHeist-ram-v0
BankHeist-ram-v4
BankHeist-ramDeterministic-v0
BankHeist-ramDeterministic-v4
BankHeist-ramNoFrameskip-v0
BankHeist-ramNoFrameskip-v4
BankHeist-v0
BankHeist-v4
BankHeistDeterministic-v0
BankHeistDeterministic-v4
BankHeistNoFrameskip-v0
BankHeistNoFrameskip-v4
BattleZone-ram-v0
BattleZone-ram-v4
BattleZone-ramDeterministic-v0
BattleZone-ramDeterministic-v4
BattleZone-ramNoFrameskip-v0
BattleZone-ramNoFrameskip-v4
BattleZone-v0
BattleZone-v4
BattleZoneDeterministic-v0
BattleZoneDeterministic-v4
BattleZoneNoFrameskip-v0
BattleZoneNoFrameskip-v4
BeamRider-ram-v0
BeamRider-ram-v4
BeamRider-ramDeterministic-v0
BeamRider-ramDeterministic-v4
BeamRider-ramNoFrameskip-v0
BeamRider-ramNoFrameskip-v4
BeamRider-v0
BeamRider-v4
BeamRiderDeterministic-v0
BeamRiderDeterministic-v4
BeamRiderNoFrameskip-v0
BeamRiderNoFrameskip-v4
Berzerk-ram-v0
Berzerk-ram-v4
Berzerk-ramDeterministic-v0
Berzerk-ramDeterministic-v4
Berzerk-ramNoFrameskip-v0
Berzerk-ramNoFrameskip-v4
Berzerk-v0
Berzerk-v4
BerzerkDeterministic-v0
BerzerkDeterministic-v4
BerzerkNoFrameskip-v0
BerzerkNoFrameskip-v4
BipedalWalker-v2
BipedalWalkerHardcore-v2
Blackjack-v0
Bowling-ram-v0
Bowling-ram-v4
Bowling-ramDeterministic-v0
Bowling-ramDeterministic-v4
Bowling-ramNoFrameskip-v0
Bowling-ramNoFrameskip-v4
Bowling-v0
Bowling-v4
BowlingDeterministic-v0
BowlingDeterministic-v4
BowlingNoFrameskip-v0
BowlingNoFrameskip-v4
Boxing-ram-v0
Boxing-ram-v4
Boxing-ramDeterministic-v0
Boxing-ramDeterministic-v4
Boxing-ramNoFrameskip-v0
Boxing-ramNoFrameskip-v4
Boxing-v0
Boxing-v4
BoxingDeterministic-v0
BoxingDeterministic-v4
BoxingNoFrameskip-v0
BoxingNoFrameskip-v4
Breakout-ram-v0
Breakout-ram-v4
Breakout-ramDeterministic-v0
Breakout-ramDeterministic-v4
Breakout-ramNoFrameskip-v0
Breakout-ramNoFrameskip-v4
Breakout-v0
Breakout-v4
BreakoutDeterministic-v0
BreakoutDeterministic-v4
BreakoutNoFrameskip-v0
BreakoutNoFrameskip-v4
CarRacing-v0
Carnival-ram-v0
Carnival-ram-v4
Carnival-ramDeterministic-v0
Carnival-ramDeterministic-v4
Carnival-ramNoFrameskip-v0
Carnival-ramNoFrameskip-v4
Carnival-v0
Carnival-v4
CarnivalDeterministic-v0
CarnivalDeterministic-v4
CarnivalNoFrameskip-v0
CarnivalNoFrameskip-v4
CartPole-v0
CartPole-v1
Centipede-ram-v0
Centipede-ram-v4
Centipede-ramDeterministic-v0
Centipede-ramDeterministic-v4
Centipede-ramNoFrameskip-v0
Centipede-ramNoFrameskip-v4
Centipede-v0
Centipede-v4
CentipedeDeterministic-v0
CentipedeDeterministic-v4
CentipedeNoFrameskip-v0
CentipedeNoFrameskip-v4
ChopperCommand-ram-v0
ChopperCommand-ram-v4
ChopperCommand-ramDeterministic-v0
ChopperCommand-ramDeterministic-v4
ChopperCommand-ramNoFrameskip-v0
ChopperCommand-ramNoFrameskip-v4
ChopperCommand-v0
ChopperCommand-v4
ChopperCommandDeterministic-v0
ChopperCommandDeterministic-v4
ChopperCommandNoFrameskip-v0
ChopperCommandNoFrameskip-v4
CliffWalking-v0
Copy-v0
CrazyClimber-ram-v0
CrazyClimber-ram-v4
CrazyClimber-ramDeterministic-v0
CrazyClimber-ramDeterministic-v4
CrazyClimber-ramNoFrameskip-v0
CrazyClimber-ramNoFrameskip-v4
CrazyClimber-v0
CrazyClimber-v4
CrazyClimberDeterministic-v0
CrazyClimberDeterministic-v4
CrazyClimberNoFrameskip-v0
CrazyClimberNoFrameskip-v4
CubeCrash-v0
CubeCrashScreenBecomesBlack-v0
CubeCrashSparse-v0
Defender-ram-v0
Defender-ram-v4
Defender-ramDeterministic-v0
Defender-ramDeterministic-v4
Defender-ramNoFrameskip-v0
Defender-ramNoFrameskip-v4
Defender-v0
Defender-v4
DefenderDeterministic-v0
DefenderDeterministic-v4
DefenderNoFrameskip-v0
DefenderNoFrameskip-v4
DemonAttack-ram-v0
DemonAttack-ram-v4
DemonAttack-ramDeterministic-v0
DemonAttack-ramDeterministic-v4
DemonAttack-ramNoFrameskip-v0
DemonAttack-ramNoFrameskip-v4
DemonAttack-v0
DemonAttack-v4
DemonAttackDeterministic-v0
DemonAttackDeterministic-v4
DemonAttackNoFrameskip-v0
DemonAttackNoFrameskip-v4
DoubleDunk-ram-v0
DoubleDunk-ram-v4
DoubleDunk-ramDeterministic-v0
DoubleDunk-ramDeterministic-v4
DoubleDunk-ramNoFrameskip-v0
DoubleDunk-ramNoFrameskip-v4
DoubleDunk-v0
DoubleDunk-v4
DoubleDunkDeterministic-v0
DoubleDunkDeterministic-v4
DoubleDunkNoFrameskip-v0
DoubleDunkNoFrameskip-v4
DuplicatedInput-v0
ElevatorAction-ram-v0
ElevatorAction-ram-v4
ElevatorAction-ramDeterministic-v0
ElevatorAction-ramDeterministic-v4
ElevatorAction-ramNoFrameskip-v0
ElevatorAction-ramNoFrameskip-v4
ElevatorAction-v0
ElevatorAction-v4
ElevatorActionDeterministic-v0
ElevatorActionDeterministic-v4
ElevatorActionNoFrameskip-v0
ElevatorActionNoFrameskip-v4
Enduro-ram-v0
Enduro-ram-v4
Enduro-ramDeterministic-v0
Enduro-ramDeterministic-v4
Enduro-ramNoFrameskip-v0
Enduro-ramNoFrameskip-v4
Enduro-v0
Enduro-v4
EnduroDeterministic-v0
EnduroDeterministic-v4
EnduroNoFrameskip-v0
EnduroNoFrameskip-v4
FetchPickAndPlace-v1
FetchPickAndPlaceDense-v1
FetchPush-v1
FetchPushDense-v1
FetchReach-v1
FetchReachDense-v1
FetchSlide-v1
FetchSlideDense-v1
FishingDerby-ram-v0
FishingDerby-ram-v4
FishingDerby-ramDeterministic-v0
FishingDerby-ramDeterministic-v4
FishingDerby-ramNoFrameskip-v0
FishingDerby-ramNoFrameskip-v4
FishingDerby-v0
FishingDerby-v4
FishingDerbyDeterministic-v0
FishingDerbyDeterministic-v4
FishingDerbyNoFrameskip-v0
FishingDerbyNoFrameskip-v4
Freeway-ram-v0
Freeway-ram-v4
Freeway-ramDeterministic-v0
Freeway-ramDeterministic-v4
Freeway-ramNoFrameskip-v0
Freeway-ramNoFrameskip-v4
Freeway-v0
Freeway-v4
FreewayDeterministic-v0
FreewayDeterministic-v4
FreewayNoFrameskip-v0
FreewayNoFrameskip-v4
Frostbite-ram-v0
Frostbite-ram-v4
Frostbite-ramDeterministic-v0
Frostbite-ramDeterministic-v4
Frostbite-ramNoFrameskip-v0
Frostbite-ramNoFrameskip-v4
Frostbite-v0
Frostbite-v4
FrostbiteDeterministic-v0
FrostbiteDeterministic-v4
FrostbiteNoFrameskip-v0
FrostbiteNoFrameskip-v4
FrozenLake-v0
FrozenLake8x8-v0
Gopher-ram-v0
Gopher-ram-v4
Gopher-ramDeterministic-v0
Gopher-ramDeterministic-v4
Gopher-ramNoFrameskip-v0
Gopher-ramNoFrameskip-v4
Gopher-v0
Gopher-v4
GopherDeterministic-v0
GopherDeterministic-v4
GopherNoFrameskip-v0
GopherNoFrameskip-v4
Gravitar-ram-v0
Gravitar-ram-v4
Gravitar-ramDeterministic-v0
Gravitar-ramDeterministic-v4
Gravitar-ramNoFrameskip-v0
Gravitar-ramNoFrameskip-v4
Gravitar-v0
Gravitar-v4
GravitarDeterministic-v0
GravitarDeterministic-v4
GravitarNoFrameskip-v0
GravitarNoFrameskip-v4
GuessingGame-v0
HalfCheetah-v2
HalfCheetah-v3
HandManipulateBlock-v0
HandManipulateBlockDense-v0
HandManipulateBlockFull-v0
HandManipulateBlockFullDense-v0
HandManipulateBlockRotateParallel-v0
HandManipulateBlockRotateParallelDense-v0
HandManipulateBlockRotateParallelTouchSensors-v0
HandManipulateBlockRotateParallelTouchSensors-v1
HandManipulateBlockRotateParallelTouchSensorsDense-v0
HandManipulateBlockRotateParallelTouchSensorsDense-v1
HandManipulateBlockRotateXYZ-v0
HandManipulateBlockRotateXYZDense-v0
HandManipulateBlockRotateXYZTouchSensors-v0
HandManipulateBlockRotateXYZTouchSensors-v1
HandManipulateBlockRotateXYZTouchSensorsDense-v0
HandManipulateBlockRotateXYZTouchSensorsDense-v1
HandManipulateBlockRotateZ-v0
HandManipulateBlockRotateZDense-v0
HandManipulateBlockRotateZTouchSensors-v0
HandManipulateBlockRotateZTouchSensors-v1
HandManipulateBlockRotateZTouchSensorsDense-v0
HandManipulateBlockRotateZTouchSensorsDense-v1
HandManipulateBlockTouchSensors-v0
HandManipulateBlockTouchSensors-v1
HandManipulateBlockTouchSensorsDense-v0
HandManipulateBlockTouchSensorsDense-v1
HandManipulateEgg-v0
HandManipulateEggDense-v0
HandManipulateEggFull-v0
HandManipulateEggFullDense-v0
HandManipulateEggRotate-v0
HandManipulateEggRotateDense-v0
HandManipulateEggRotateTouchSensors-v0
HandManipulateEggRotateTouchSensors-v1
HandManipulateEggRotateTouchSensorsDense-v0
HandManipulateEggRotateTouchSensorsDense-v1
HandManipulateEggTouchSensors-v0
HandManipulateEggTouchSensors-v1
HandManipulateEggTouchSensorsDense-v0
HandManipulateEggTouchSensorsDense-v1
HandManipulatePen-v0
HandManipulatePenDense-v0
HandManipulatePenFull-v0
HandManipulatePenFullDense-v0
HandManipulatePenRotate-v0
HandManipulatePenRotateDense-v0
HandManipulatePenRotateTouchSensors-v0
HandManipulatePenRotateTouchSensors-v1
HandManipulatePenRotateTouchSensorsDense-v0
HandManipulatePenRotateTouchSensorsDense-v1
HandManipulatePenTouchSensors-v0
HandManipulatePenTouchSensors-v1
HandManipulatePenTouchSensorsDense-v0
HandManipulatePenTouchSensorsDense-v1
HandReach-v0
HandReachDense-v0
Hero-ram-v0
Hero-ram-v4
Hero-ramDeterministic-v0
Hero-ramDeterministic-v4
Hero-ramNoFrameskip-v0
Hero-ramNoFrameskip-v4
Hero-v0
Hero-v4
HeroDeterministic-v0
HeroDeterministic-v4
HeroNoFrameskip-v0
HeroNoFrameskip-v4
Hopper-v2
Hopper-v3
HotterColder-v0
Humanoid-v2
Humanoid-v3
HumanoidStandup-v2
IceHockey-ram-v0
IceHockey-ram-v4
IceHockey-ramDeterministic-v0
IceHockey-ramDeterministic-v4
IceHockey-ramNoFrameskip-v0
IceHockey-ramNoFrameskip-v4
IceHockey-v0
IceHockey-v4
IceHockeyDeterministic-v0
IceHockeyDeterministic-v4
IceHockeyNoFrameskip-v0
IceHockeyNoFrameskip-v4
InvertedDoublePendulum-v2
InvertedPendulum-v2
Jamesbond-ram-v0
Jamesbond-ram-v4
Jamesbond-ramDeterministic-v0
Jamesbond-ramDeterministic-v4
Jamesbond-ramNoFrameskip-v0
Jamesbond-ramNoFrameskip-v4
Jamesbond-v0
Jamesbond-v4
JamesbondDeterministic-v0
JamesbondDeterministic-v4
JamesbondNoFrameskip-v0
JamesbondNoFrameskip-v4
JourneyEscape-ram-v0
JourneyEscape-ram-v4
JourneyEscape-ramDeterministic-v0
JourneyEscape-ramDeterministic-v4
JourneyEscape-ramNoFrameskip-v0
JourneyEscape-ramNoFrameskip-v4
JourneyEscape-v0
JourneyEscape-v4
JourneyEscapeDeterministic-v0
JourneyEscapeDeterministic-v4
JourneyEscapeNoFrameskip-v0
JourneyEscapeNoFrameskip-v4
Kangaroo-ram-v0
Kangaroo-ram-v4
Kangaroo-ramDeterministic-v0
Kangaroo-ramDeterministic-v4
Kangaroo-ramNoFrameskip-v0
Kangaroo-ramNoFrameskip-v4
Kangaroo-v0
Kangaroo-v4
KangarooDeterministic-v0
KangarooDeterministic-v4
KangarooNoFrameskip-v0
KangarooNoFrameskip-v4
KellyCoinflip-v0
KellyCoinflipGeneralized-v0
Krull-ram-v0
Krull-ram-v4
Krull-ramDeterministic-v0
Krull-ramDeterministic-v4
Krull-ramNoFrameskip-v0
Krull-ramNoFrameskip-v4
Krull-v0
Krull-v4
KrullDeterministic-v0
KrullDeterministic-v4
KrullNoFrameskip-v0
KrullNoFrameskip-v4
KungFuMaster-ram-v0
KungFuMaster-ram-v4
KungFuMaster-ramDeterministic-v0
KungFuMaster-ramDeterministic-v4
KungFuMaster-ramNoFrameskip-v0
KungFuMaster-ramNoFrameskip-v4
KungFuMaster-v0
KungFuMaster-v4
KungFuMasterDeterministic-v0
KungFuMasterDeterministic-v4
KungFuMasterNoFrameskip-v0
KungFuMasterNoFrameskip-v4
LunarLander-v2
LunarLanderContinuous-v2
MemorizeDigits-v0
MontezumaRevenge-ram-v0
MontezumaRevenge-ram-v4
MontezumaRevenge-ramDeterministic-v0
MontezumaRevenge-ramDeterministic-v4
MontezumaRevenge-ramNoFrameskip-v0
MontezumaRevenge-ramNoFrameskip-v4
MontezumaRevenge-v0
MontezumaRevenge-v4
MontezumaRevengeDeterministic-v0
MontezumaRevengeDeterministic-v4
MontezumaRevengeNoFrameskip-v0
MontezumaRevengeNoFrameskip-v4
MountainCar-v0
MountainCarContinuous-v0
MsPacman-ram-v0
MsPacman-ram-v4
MsPacman-ramDeterministic-v0
MsPacman-ramDeterministic-v4
MsPacman-ramNoFrameskip-v0
MsPacman-ramNoFrameskip-v4
MsPacman-v0
MsPacman-v4
MsPacmanDeterministic-v0
MsPacmanDeterministic-v4
MsPacmanNoFrameskip-v0
MsPacmanNoFrameskip-v4
NChain-v0
NameThisGame-ram-v0
NameThisGame-ram-v4
NameThisGame-ramDeterministic-v0
NameThisGame-ramDeterministic-v4
NameThisGame-ramNoFrameskip-v0
NameThisGame-ramNoFrameskip-v4
NameThisGame-v0
NameThisGame-v4
NameThisGameDeterministic-v0
NameThisGameDeterministic-v4
NameThisGameNoFrameskip-v0
NameThisGameNoFrameskip-v4
Pendulum-v0
Phoenix-ram-v0
Phoenix-ram-v4
Phoenix-ramDeterministic-v0
Phoenix-ramDeterministic-v4
Phoenix-ramNoFrameskip-v0
Phoenix-ramNoFrameskip-v4
Phoenix-v0
Phoenix-v4
PhoenixDeterministic-v0
PhoenixDeterministic-v4
PhoenixNoFrameskip-v0
PhoenixNoFrameskip-v4
Pitfall-ram-v0
Pitfall-ram-v4
Pitfall-ramDeterministic-v0
Pitfall-ramDeterministic-v4
Pitfall-ramNoFrameskip-v0
Pitfall-ramNoFrameskip-v4
Pitfall-v0
Pitfall-v4
PitfallDeterministic-v0
PitfallDeterministic-v4
PitfallNoFrameskip-v0
PitfallNoFrameskip-v4
Pong-ram-v0
Pong-ram-v4
Pong-ramDeterministic-v0
Pong-ramDeterministic-v4
Pong-ramNoFrameskip-v0
Pong-ramNoFrameskip-v4
Pong-v0
Pong-v4
PongDeterministic-v0
PongDeterministic-v4
PongNoFrameskip-v0
PongNoFrameskip-v4
Pooyan-ram-v0
Pooyan-ram-v4
Pooyan-ramDeterministic-v0
Pooyan-ramDeterministic-v4
Pooyan-ramNoFrameskip-v0
Pooyan-ramNoFrameskip-v4
Pooyan-v0
Pooyan-v4
PooyanDeterministic-v0
PooyanDeterministic-v4
PooyanNoFrameskip-v0
PooyanNoFrameskip-v4
PrivateEye-ram-v0
PrivateEye-ram-v4
PrivateEye-ramDeterministic-v0
PrivateEye-ramDeterministic-v4
PrivateEye-ramNoFrameskip-v0
PrivateEye-ramNoFrameskip-v4
PrivateEye-v0
PrivateEye-v4
PrivateEyeDeterministic-v0
PrivateEyeDeterministic-v4
PrivateEyeNoFrameskip-v0
PrivateEyeNoFrameskip-v4
Pusher-v2
Qbert-ram-v0
Qbert-ram-v4
Qbert-ramDeterministic-v0
Qbert-ramDeterministic-v4
Qbert-ramNoFrameskip-v0
Qbert-ramNoFrameskip-v4
Qbert-v0
Qbert-v4
QbertDeterministic-v0
QbertDeterministic-v4
QbertNoFrameskip-v0
QbertNoFrameskip-v4
Reacher-v2
RepeatCopy-v0
Reverse-v0
ReversedAddition-v0
ReversedAddition3-v0
Riverraid-ram-v0
Riverraid-ram-v4
Riverraid-ramDeterministic-v0
Riverraid-ramDeterministic-v4
Riverraid-ramNoFrameskip-v0
Riverraid-ramNoFrameskip-v4
Riverraid-v0
Riverraid-v4
RiverraidDeterministic-v0
RiverraidDeterministic-v4
RiverraidNoFrameskip-v0
RiverraidNoFrameskip-v4
RoadRunner-ram-v0
RoadRunner-ram-v4
RoadRunner-ramDeterministic-v0
RoadRunner-ramDeterministic-v4
RoadRunner-ramNoFrameskip-v0
RoadRunner-ramNoFrameskip-v4
RoadRunner-v0
RoadRunner-v4
RoadRunnerDeterministic-v0
RoadRunnerDeterministic-v4
RoadRunnerNoFrameskip-v0
RoadRunnerNoFrameskip-v4
Robotank-ram-v0
Robotank-ram-v4
Robotank-ramDeterministic-v0
Robotank-ramDeterministic-v4
Robotank-ramNoFrameskip-v0
Robotank-ramNoFrameskip-v4
Robotank-v0
Robotank-v4
RobotankDeterministic-v0
RobotankDeterministic-v4
RobotankNoFrameskip-v0
RobotankNoFrameskip-v4
Roulette-v0
Seaquest-ram-v0
Seaquest-ram-v4
Seaquest-ramDeterministic-v0
Seaquest-ramDeterministic-v4
Seaquest-ramNoFrameskip-v0
Seaquest-ramNoFrameskip-v4
Seaquest-v0
Seaquest-v4
SeaquestDeterministic-v0
SeaquestDeterministic-v4
SeaquestNoFrameskip-v0
SeaquestNoFrameskip-v4
Skiing-ram-v0
Skiing-ram-v4
Skiing-ramDeterministic-v0
Skiing-ramDeterministic-v4
Skiing-ramNoFrameskip-v0
Skiing-ramNoFrameskip-v4
Skiing-v0
Skiing-v4
SkiingDeterministic-v0
SkiingDeterministic-v4
SkiingNoFrameskip-v0
SkiingNoFrameskip-v4
Solaris-ram-v0
Solaris-ram-v4
Solaris-ramDeterministic-v0
Solaris-ramDeterministic-v4
Solaris-ramNoFrameskip-v0
Solaris-ramNoFrameskip-v4
Solaris-v0
Solaris-v4
SolarisDeterministic-v0
SolarisDeterministic-v4
SolarisNoFrameskip-v0
SolarisNoFrameskip-v4
SpaceInvaders-ram-v0
SpaceInvaders-ram-v4
SpaceInvaders-ramDeterministic-v0
SpaceInvaders-ramDeterministic-v4
SpaceInvaders-ramNoFrameskip-v0
SpaceInvaders-ramNoFrameskip-v4
SpaceInvaders-v0
SpaceInvaders-v4
SpaceInvadersDeterministic-v0
SpaceInvadersDeterministic-v4
SpaceInvadersNoFrameskip-v0
SpaceInvadersNoFrameskip-v4
StarGunner-ram-v0
StarGunner-ram-v4
StarGunner-ramDeterministic-v0
StarGunner-ramDeterministic-v4
StarGunner-ramNoFrameskip-v0
StarGunner-ramNoFrameskip-v4
StarGunner-v0
StarGunner-v4
StarGunnerDeterministic-v0
StarGunnerDeterministic-v4
StarGunnerNoFrameskip-v0
StarGunnerNoFrameskip-v4
Striker-v2
Swimmer-v2
Swimmer-v3
Taxi-v2
Tennis-ram-v0
Tennis-ram-v4
Tennis-ramDeterministic-v0
Tennis-ramDeterministic-v4
Tennis-ramNoFrameskip-v0
Tennis-ramNoFrameskip-v4
Tennis-v0
Tennis-v4
TennisDeterministic-v0
TennisDeterministic-v4
TennisNoFrameskip-v0
TennisNoFrameskip-v4
Thrower-v2
TimePilot-ram-v0
TimePilot-ram-v4
TimePilot-ramDeterministic-v0
TimePilot-ramDeterministic-v4
TimePilot-ramNoFrameskip-v0
TimePilot-ramNoFrameskip-v4
TimePilot-v0
TimePilot-v4
TimePilotDeterministic-v0
TimePilotDeterministic-v4
TimePilotNoFrameskip-v0
TimePilotNoFrameskip-v4
Tutankham-ram-v0
Tutankham-ram-v4
Tutankham-ramDeterministic-v0
Tutankham-ramDeterministic-v4
Tutankham-ramNoFrameskip-v0
Tutankham-ramNoFrameskip-v4
Tutankham-v0
Tutankham-v4
TutankhamDeterministic-v0
TutankhamDeterministic-v4
TutankhamNoFrameskip-v0
TutankhamNoFrameskip-v4
UpNDown-ram-v0
UpNDown-ram-v4
UpNDown-ramDeterministic-v0
UpNDown-ramDeterministic-v4
UpNDown-ramNoFrameskip-v0
UpNDown-ramNoFrameskip-v4
UpNDown-v0
UpNDown-v4
UpNDownDeterministic-v0
UpNDownDeterministic-v4
UpNDownNoFrameskip-v0
UpNDownNoFrameskip-v4
Venture-ram-v0
Venture-ram-v4
Venture-ramDeterministic-v0
Venture-ramDeterministic-v4
Venture-ramNoFrameskip-v0
Venture-ramNoFrameskip-v4
Venture-v0
Venture-v4
VentureDeterministic-v0
VentureDeterministic-v4
VentureNoFrameskip-v0
VentureNoFrameskip-v4
VideoPinball-ram-v0
VideoPinball-ram-v4
VideoPinball-ramDeterministic-v0
VideoPinball-ramDeterministic-v4
VideoPinball-ramNoFrameskip-v0
VideoPinball-ramNoFrameskip-v4
VideoPinball-v0
VideoPinball-v4
VideoPinballDeterministic-v0
VideoPinballDeterministic-v4
VideoPinballNoFrameskip-v0
VideoPinballNoFrameskip-v4
Walker2d-v2
Walker2d-v3
WizardOfWor-ram-v0
WizardOfWor-ram-v4
WizardOfWor-ramDeterministic-v0
WizardOfWor-ramDeterministic-v4
WizardOfWor-ramNoFrameskip-v0
WizardOfWor-ramNoFrameskip-v4
WizardOfWor-v0
WizardOfWor-v4
WizardOfWorDeterministic-v0
WizardOfWorDeterministic-v4
WizardOfWorNoFrameskip-v0
WizardOfWorNoFrameskip-v4
YarsRevenge-ram-v0
YarsRevenge-ram-v4
YarsRevenge-ramDeterministic-v0
YarsRevenge-ramDeterministic-v4
YarsRevenge-ramNoFrameskip-v0
YarsRevenge-ramNoFrameskip-v4
YarsRevenge-v0
YarsRevenge-v4
YarsRevengeDeterministic-v0
YarsRevengeDeterministic-v4
YarsRevengeNoFrameskip-v0
YarsRevengeNoFrameskip-v4
Zaxxon-ram-v0
Zaxxon-ram-v4
Zaxxon-ramDeterministic-v0
Zaxxon-ramDeterministic-v4
Zaxxon-ramNoFrameskip-v0
Zaxxon-ramNoFrameskip-v4
Zaxxon-v0
Zaxxon-v4
ZaxxonDeterministic-v0
ZaxxonDeterministic-v4
ZaxxonNoFrameskip-v0
ZaxxonNoFrameskip-v4

'''