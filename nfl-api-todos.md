# TODO Comments in nfl-com-api.yaml

Total TODOs: 77 (55 completed, 77 remaining)

## Completed Issues

The following issues have been addressed:
- ✅ [Issue #4](https://github.com/jkgriebel93/griddy-sdk-sources/issues/4): Create and consolidate position-related enums (16 TODOs)
- ✅ [Issue #5](https://github.com/jkgriebel93/griddy-sdk-sources/issues/5): Create game type, phase, and status enums (10 TODOs)
- ✅ [Issue #6](https://github.com/jkgriebel93/griddy-sdk-sources/issues/6): Consolidate week and week slug enum usage (10 TODOs)
- ✅ [Issue #10](https://github.com/jkgriebel93/griddy-sdk-sources/issues/10): Create and use roof type enum consistently (4 TODOs)
- ✅ [Issue #11](https://github.com/jkgriebel93/griddy-sdk-sources/issues/11): Refactor inline enums to top-level components (13 TODOs)
- ✅ [Issue #14](https://github.com/jkgriebel93/griddy-sdk-sources/issues/14): Fix data type inconsistencies (1 TODO)
- ✅ **StatsQueryMetadata Component**: Created standardized pagination/query metadata component for 14 stats response schemas (1 TODO)

**Total Completed: 55 TODOs across 7 items**

## Remaining Issues

The following issues have not yet been addressed:
- ⏸️ [Issue #7](https://github.com/jkgriebel93/griddy-sdk-sources/issues/7): Consolidate duplicate or similar components (28 TODOs) - *Research-heavy*
- ⏸️ [Issue #8](https://github.com/jkgriebel93/griddy-sdk-sources/issues/8): Investigate and define undefined object structures (17 TODOs) - *Research-heavy*
- ⏸️ [Issue #9](https://github.com/jkgriebel93/griddy-sdk-sources/issues/9): Refactor metrics explanation components (12 TODOs) - *Research-heavy*
- ⏸️ [Issue #12](https://github.com/jkgriebel93/griddy-sdk-sources/issues/12): Create miscellaneous missing enums (13 TODOs)
- ⏸️ [Issue #13](https://github.com/jkgriebel93/griddy-sdk-sources/issues/13): Address miscellaneous TODO comments (7 TODOs)

**Total Remaining: 77 TODOs across 5 issues**

---

## BoxscoreSchedule

| Line | TODO Comment |
|------|--------------|
| 381 | What is the difference between a BoxscoreTeam and a Team? |
| 407 | Is BoxscoreSite just a venue? |
| 422 | Should there be an enum defined for team abbreviations? |

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

## DefensiveRushMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 1644 | Metrics explanations |

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

## FantayScoringExplanation

| Line | TODO Comment |
|------|--------------|
| 2145 | More explanation fields, slightly different than the metrics though |

## FilmroomPlay

| Line | TODO Comment |
|------|--------------|
| 2268 | Investigate what the selectedParamValues object can look like |

## FuturesMarket

| Line | TODO Comment |
|------|--------------|
| 2333 | Investigate what this fixture object looks like |

## Game

| Line | TODO Comment |
|------|--------------|
| 2412 | Investigate the Game.extensions object |
| 2472 | Is this the same as GameSite or whatever it was I saw earlier? |

## GameInsight

| Line | TODO Comment |
|------|--------------|
| 2551 | Investigate GameInsight.content object |

## GamePreviewResponse

| Line | TODO Comment |
|------|--------------|
| 2606 | Investigate the GamePreviewResponse.preview object |

## GameSite

| Line | TODO Comment |
|------|--------------|
| 2709 | Again, what is the difference between GameSite and Venue? |

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

## InsightContentExplanation

| Line | TODO Comment |
|------|--------------|
| 3110 | More explanation properties |

## LiveGame

| Line | TODO Comment |
|------|--------------|
| 3164 | Can the Team component not be used here? |
| 3177 | Can the Team component not be used here? |

## OffensiveMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 3318 | Metrics explanation properties |

## OverallRecord

| Line | TODO Comment |
|------|--------------|
| 3374 | There is a game result enum component that can be used here |

## PassRushMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 3396 | Metrics explanation properties |

## PassRusherStats

| Line | TODO Comment |
|------|--------------|
| 3462 | Investigate the PassRusherStats object |

## PassingStats

| Line | TODO Comment |
|------|--------------|
| 3484 | Investigate the difference(s) between PasserStats and PassingStats, consolidate if possible |

## PlayDetail

| Line | TODO Comment |
|------|--------------|
| 3692 | Use or create a PlayDirectionEnum conponent |

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

## ProInjuryReportResponse

| Line | TODO Comment |
|------|--------------|
| 5388 | How does this compare to regular injury report response (if there is one) |

## ProTeam

| Line | TODO Comment |
|------|--------------|
| 5406 | How does this compare to the Team component? How much can it be consolidated? |

## ProWeek

| Line | TODO Comment |
|------|--------------|
| 5528 | How does this compare to a regular Week, and how can it be consolidated? |

## ReceiverStats

| Line | TODO Comment |
|------|--------------|
| 5651 | Investigate and define the ReceiverStats object |

## ReceivingMetricsExplanation

| Line | TODO Comment |
|------|--------------|
| 5657 | Metrics explanation properties |

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

## Site

| Line | TODO Comment |
|------|--------------|
| 6084 | Compare this to Venue and see if they can be consolidated |

## Standings

| Line | TODO Comment |
|------|--------------|
| 6139 | Can this be replaced with one of the Team components? |

## StatisticalCategory

| Line | TODO Comment |
|------|--------------|
| 6220 | Use or create a dataType enum component |

## TeamVenue

| Line | TODO Comment |
|------|--------------|
| 7708 | Compare to Site, Venue, other similar components. Consolidate as and if possible |

## Transaction

| Line | TODO Comment |
|------|--------------|
| 7826 | Use or create a TransactionTypeEnum component |

## Venue

| Line | TODO Comment |
|------|--------------|
| 7848 | Compare with Site, TeamVenue, etc. and consolidate as possible |

## WeeklyGameDetail

| Line | TODO Comment |
|------|--------------|
| 8084 | Compare to Game component, consolidate if possible |
| 8097 | Investigate the WeeklyGameDetail.replays object, define spec |
| 8103 | Investigate the WeeklyGameDetail.summary object |
| 8108 | Investigate the WeeklyGameDetail.taggedVideos object. |

## WinProbabilityMetadata

| Line | TODO Comment |
|------|--------------|
| 8813 | Use or create a CalculationMethodEnum component |
