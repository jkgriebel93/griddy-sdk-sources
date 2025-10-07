# TODO Comments in nfl-com-api.yaml

Total TODOs: 132

## BoxscoreSchedule

| Line | TODO Comment |
|------|--------------|
| 372 | Should there be a different enum for game types? |
| 381 | What is the difference between a BoxscoreTeam and a Team? |
| 407 | Is BoxscoreSite just a venue? |
| 422 | Should there be an enum defined for team abbreviations? |

## BoxscoreScore

| Line | TODO Comment |
|------|--------------|
| 440 | Should there be a phase enum? |

## BoxscoreSite

| Line | TODO Comment |
|------|--------------|
| 453 | Create roofType enum |

## BoxscoreTeam

| Line | TODO Comment |
|------|--------------|
| 482 | This example doesn't look correct. |

## BroadcastInfo

| Line | TODO Comment |
|------|--------------|
| 535 | Should there be a component for TV and Streaming channels? |

## CoachesFilmVideo

| Line | TODO Comment |
|------|--------------|
| 634 | Create a cameraSource enum |
| 673 | Shouldn't this be an integer? |
| 704 | Would this reference the proposed network component from earlier? |
| 820 | Create CoachesFileVideoSubType enum |
| 848 | Explore what this object actually looks like |

## CoverageMetrics

| Line | TODO Comment |
|------|--------------|
| 904 | Each of these properties has the same two fields. |

## CurrentGame

| Line | TODO Comment |
|------|--------------|
| 969 | Explore to find out what CurrentGame.extensions is |

## DefensiveMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 1066 | Similar to earlier, all of these fields have the same two properties. Consider how it might be refactored. |

## DefensiveOverviewMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 1092 | More metric explanation properties |

## DefensivePassMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 1157 | Metric explanations. Consider refactor |

## DefensivePassRushStats

| Line | TODO Comment |
|------|--------------|
| 1219 | Create a schema for this enum |
| 1227 | Ensure this position groups are correct |
| 1231 | Create a schema for this enum |

## DefensivePlayerOverviewStats

| Line | TODO Comment |
|------|--------------|
| 1360 | Refactor to use enum mentioned earlier |
| 1379 | Use enum |

## DefensivePlayerStats

| Line | TODO Comment |
|------|--------------|
| 1542 | Use enum |
| 1561 | Use enum |

## DefensiveRushMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 1644 | Metrics explanations |

## DefensiveSplitCategory

| Line | TODO Comment |
|------|--------------|
| 1687 | Consider moving this enum to a top level component |

## Drive

| Line | TODO Comment |
|------|--------------|
| 1880 | Create a DriveResultEnum component |

## FantasyPlayerStats

| Line | TODO Comment |
|------|--------------|
| 2004 | Create a FantasyPlayerPositionEnum component |
| 2016 | Create a FantasyPositionGroupEnum component |

## FantasyStatsResponse

| Line | TODO Comment |
|------|--------------|
| 2106 | Use the FantasyPositionEnum mentioned earlier here |
| 2134 | There is a week enum that can be used here |

## FantayScoringExplanation

| Line | TODO Comment |
|------|--------------|
| 2145 | More explanation fields, slightly different than the metrics though |

## FilmCard

| Line | TODO Comment |
|------|--------------|
| 2195 | Use the WeekEnum here |

## FilmroomPlay

| Line | TODO Comment |
|------|--------------|
| 2268 | Investigate what the selectedParamValues object can look like |
| 2289 | Use the week enum |

## FuturesMarket

| Line | TODO Comment |
|------|--------------|
| 2333 | Investigate what this fixture object looks like |

## Game

| Line | TODO Comment |
|------|--------------|
| 2412 | Investigate the Game.extensions object |
| 2422 | Surely there is a gameType enum |
| 2439 | Use or create a GamePhase enum |
| 2449 | If a game status enum doesn't exist, create it and use it here |
| 2472 | Is this the same as GameSite or whatever it was I saw earlier? |

## GameInsight

| Line | TODO Comment |
|------|--------------|
| 2551 | Investigate GameInsight.content object |

## GamePreviewResponse

| Line | TODO Comment |
|------|--------------|
| 2606 | Investigate the GamePreviewResponse.preview object |

## GameSchedule

| Line | TODO Comment |
|------|--------------|
| 2627 | Should there be a separate gameType enum? |

## GameScore

| Line | TODO Comment |
|------|--------------|
| 2692 | Refactor this out to a top level enum component |

## GameSite

| Line | TODO Comment |
|------|--------------|
| 2709 | Again, what is the difference between GameSite and Venue? |
| 2715 | Add roofType enum |

## GameStatsResponse

| Line | TODO Comment |
|------|--------------|
| 2764 | Investigate the GameStatsResponse.data object |

## GamecenterResponse

| Line | TODO Comment |
|------|--------------|
| 2798 | Investigate the GamecenterResponse.leaders.passDistanceLeaders object |
| 2801 | Investigate the GamecenterResponse.leaders.speedLeaders object |
| 2804 | Investigate the GamecenterResponse.leaders.timeToSackLeaders object |

## InjuryEntry

| Line | TODO Comment |
|------|--------------|
| 2919 | create an enum for InjuryEntry.gameStatus |

## Insight

| Line | TODO Comment |
|------|--------------|
| 3015 | Use or create player position enum |

## InsightContentExplanation

| Line | TODO Comment |
|------|--------------|
| 3110 | More explanation properties |

## LiveGame

| Line | TODO Comment |
|------|--------------|
| 3164 | Can the Team component not be used here? |
| 3177 | Can the Team component not be used here? |
| 3199 | Use or create game status enum |

## OffensiveMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 3318 | Metrics explanation properties |

## OffensiveSplitCategory

| Line | TODO Comment |
|------|--------------|
| 3353 | Consider making this enum a top level component |

## OverallRecord

| Line | TODO Comment |
|------|--------------|
| 3374 | There is a game result enum component that can be used here |

## PassRushMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 3396 | Metrics explanation properties |

## PassRushStatsResponse

| Line | TODO Comment |
|------|--------------|
| 3426 | Are some of these *Response properties standardized enough that a component can be created? |

## PassRusherStats

| Line | TODO Comment |
|------|--------------|
| 3462 | Investigate the PassRusherStats object |

## PassingStats

| Line | TODO Comment |
|------|--------------|
| 3484 | Investigate the difference(s) between PasserStats and PassingStats, consolidate if possible |

## Play

| Line | TODO Comment |
|------|--------------|
| 3590 | Refactor this into a top level component |

## PlayDetail

| Line | TODO Comment |
|------|--------------|
| 3692 | Use or create a PlayDirectionEnum conponent |
| 3702 | Refactor this out to be a top level enum component |
| 3715 | Use the PlayTypeEnum |

## PlayParticipant

| Line | TODO Comment |
|------|--------------|
| 3782 | Use or create a PlayParticipantRoleEnum component |

## PlayPlayer

| Line | TODO Comment |
|------|--------------|
| 3797 | PlayPlayer is a horrible name |

## Player

| Line | TODO Comment |
|------|--------------|
| 4088 | Use or create the next gen stats position enum |
| 4093 | Use or create the next gen stats position group enum |
| 4098 | Use or create the position enum |
| 4103 | Use or create the position group enum |
| 4122 | Surely this can be an enum |

## PlayerInjury

| Line | TODO Comment |
|------|--------------|
| 4182 | Investigate the PlayerInjury object |

## PlayerPassingStats

| Line | TODO Comment |
|------|--------------|
| 4187 | To what degree can this be consolidated with Passing/Passer Stats? |

## PlayerProjection

| Line | TODO Comment |
|------|--------------|
| 4468 | What other values can this enum have? |
| 4481 | What values can this enum have? |
| 4489 | What values can this have? |

## PlayerStatistic

| Line | TODO Comment |
|------|--------------|
| 5039 | Can this be defined any more specifically? Perhaps not given that it can be completely different based on category |

## PlayerStatsResponse

| Line | TODO Comment |
|------|--------------|
| 5057 | Can the be specified in any more detail? |
| 5067 | Use the seasonType enum |
| 5070 | Use or create a statCategory enum |

## PlayerWeekProjectedPoints

| Line | TODO Comment |
|------|--------------|
| 5090 | See if this can be an enum. It would probably be PPR, Half-PPR, STD |
| 5101 | What values can this have? |

## PlayerWeekProjectedStats

| Line | TODO Comment |
|------|--------------|
| 5242 | Are all these type fields truly enums? |

## ProGame

| Line | TODO Comment |
|------|--------------|
| 5283 | Compare how this differs from Game |
| 5316 | Investigate the ProGame.extensions object |
| 5325 | Use or create the gameType enum |
| 5342 | Use or create the game phase enum |
| 5352 | Use or create the game status enum |
| 5383 | Use or create the week type enum |

## ProInjuryReportResponse

| Line | TODO Comment |
|------|--------------|
| 5388 | How does this compare to regular injury report response (if there is one) |

## ProTeam

| Line | TODO Comment |
|------|--------------|
| 5406 | How does this compare to the Team component? How much can it be consolidated? |
| 5427 | use or create the conference abbr enum |
| 5508 | Make this a top level enum component |

## ProWeek

| Line | TODO Comment |
|------|--------------|
| 5528 | How does this compare to a regular Week, and how can it be consolidated? |
| 5564 | Use the week slug enum component |
| 5569 | Use or create a week type enum |

## ReceiverStats

| Line | TODO Comment |
|------|--------------|
| 5651 | Investigate and define the ReceiverStats object |

## ReceivingMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 5657 | Metrics explanation properties |

## ReceivingStatsResponse

| Line | TODO Comment |
|------|--------------|
| 5740 | Use the week slug enum |

## RusherStats

| Line | TODO Comment |
|------|--------------|
| 5848 | Investigate the RusherStats object. Note that it may be very similar if not identical to RushingStats |

## ScheduleTeam

| Line | TODO Comment |
|------|--------------|
| 5907 | How is this different from Team? Can it be consolidated? |

## ScheduledGame

| Line | TODO Comment |
|------|--------------|
| 5933 | How is this different from Game? Can it be consolidated? |

## ScoringPlay

| Line | TODO Comment |
|------|--------------|
| 6038 | Refactor this out to a top level enum component |

## Site

| Line | TODO Comment |
|------|--------------|
| 6084 | Compare this to Venue and see if they can be consolidated |
| 6090 | Use or create a roof type enum |

## Standings

| Line | TODO Comment |
|------|--------------|
| 6139 | Can this be replaced with one of the Team components? |

## StatisticalCategory

| Line | TODO Comment |
|------|--------------|
| 6220 | Use or create a dataType enum component |

## Team

| Line | TODO Comment |
|------|--------------|
| 6248 | Refactor this out to a top level enum component? |
| 6319 | Consider refactoring this out to a top level enum component |

## TeamVenue

| Line | TODO Comment |
|------|--------------|
| 7708 | Compare to Site, Venue, other similar components. Consolidate as and if possible |

## TokenRequest

| Line | TODO Comment |
|------|--------------|
| 7757 | Refactor this out to a top level enum component |

## Transaction

| Line | TODO Comment |
|------|--------------|
| 7826 | Use or create a TransactionTypeEnum component |

## Venue

| Line | TODO Comment |
|------|--------------|
| 7848 | Compare with Site, TeamVenue, etc. and consolidate as possible |

## VenueInfo

| Line | TODO Comment |
|------|--------------|
| 7885 | Use or create roof type enum |

## Week

| Line | TODO Comment |
|------|--------------|
| 8069 | use the week slug enum |
| 8074 | Use or create the top level week type enum component |

## WeeklyGameDetail

| Line | TODO Comment |
|------|--------------|
| 8084 | Compare to Game component, consolidate if possible |
| 8097 | Investigate the WeeklyGameDetail.replays object, define spec |
| 8103 | Investigate the WeeklyGameDetail.summary object |
| 8108 | Investigate the WeeklyGameDetail.taggedVideos object. |

## WeeklyPlayerPassingStats

| Line | TODO Comment |
|------|--------------|
| 8347 | Use or create the next gen stats position enum |
| 8352 | Use or create the next gen stats position group enum |
| 8366 | Use or create the position enum |
| 8371 | Use or create the position group enum |

## WeeklyPlayerRushingStats

| Line | TODO Comment |
|------|--------------|
| 8587 | Verify the possible values where this OffensivePlayerPositionEnum is being used. |

## WeeklyRushingStatsResponse

| Line | TODO Comment |
|------|--------------|
| 8795 | Use the week slug enum |

## WinProbabilityMetadata

| Line | TODO Comment |
|------|--------------|
| 8813 | Use or create a CalculationMethodEnum component |
