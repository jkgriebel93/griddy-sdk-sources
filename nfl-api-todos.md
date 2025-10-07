# TODO Comments in nfl-com-api.yaml

Original remaining TODOs: 77
Recently resolved: 22
**Current remaining: 55 TODOs**

## Completed Issues

The following issues have been addressed:
- ✅ [Issue #4](https://github.com/jkgriebel93/griddy-sdk-sources/issues/4): Create and consolidate position-related enums (16 TODOs)
- ✅ [Issue #5](https://github.com/jkgriebel93/griddy-sdk-sources/issues/5): Create game type, phase, and status enums (10 TODOs)
- ✅ [Issue #6](https://github.com/jkgriebel93/griddy-sdk-sources/issues/6): Consolidate week and week slug enum usage (10 TODOs)
- ✅ [Issue #10](https://github.com/jkgriebel93/griddy-sdk-sources/issues/10): Create and use roof type enum consistently (4 TODOs)
- ✅ [Issue #11](https://github.com/jkgriebel93/griddy-sdk-sources/issues/11): Refactor inline enums to top-level components (13 TODOs)
- ✅ [Issue #14](https://github.com/jkgriebel93/griddy-sdk-sources/issues/14): Fix data type inconsistencies (1 TODO)
- ✅ **StatsQueryMetadata Component**: Created standardized pagination/query metadata component for 14 stats response schemas (1 TODO)
- ✅ **Site Schema Consolidation**: Consolidated BoxscoreSite, GameSite, and Site into a single Site schema (3 TODOs)
- ✅ **Venue Schema Consolidation**: Consolidated TeamVenue into Venue schema (1 TODO)
- ✅ **Manual Enum Creation and Cleanup**: Created 11 new enum components and addressed 6 miscellaneous TODOs (17 TODOs)
  - CameraSourceEnum
  - CoachesFileVideoSubTypeEnum
  - DriveResultEnum
  - FantasyPlayerPositionEnum
  - FantasyPositionGroupEnum
  - InjuredPlayerGameStatusEnum
  - PlayDirectionEnum
  - PlayParticipantRoleEnum
  - DataTypeEnum
  - TransactionTypeEnum
  - CalculationMethodEnum
  - Renamed PlayPlayer to ParticipantPlayerInfo
  - Applied existing enums (SeasonTypeEnum, WeekTypeEnum, FantasyPositionGroupEnum)
  - Removed incorrect example comment
  - Addressed LiveGame Team component questions
- ✅ **Passing Stats Consolidation**: Consolidated WeeklyPlayerPassingStats to extend PlayerPassingStats using allOf composition (1 TODO)

**Total Completed: 77 TODOs across 11 items**

## Remaining Issues

The following issues have not yet been addressed:
- ⏸️ [Issue #7](https://github.com/jkgriebel93/griddy-sdk-sources/issues/7): Consolidate duplicate or similar components (23 TODOs) - *Research-heavy*
- ⏸️ [Issue #8](https://github.com/jkgriebel93/griddy-sdk-sources/issues/8): Investigate and define undefined object structures (17 TODOs) - *Research-heavy*
- ⏸️ [Issue #9](https://github.com/jkgriebel93/griddy-sdk-sources/issues/9): Refactor metrics explanation components (12 TODOs) - *Research-heavy*
- ⏸️ [Issue #12](https://github.com/jkgriebel93/griddy-sdk-sources/issues/12): Create miscellaneous missing enums (2 TODOs)
- ⏸️ [Issue #13](https://github.com/jkgriebel93/griddy-sdk-sources/issues/13): Address miscellaneous TODO comments (1 TODO)

**Total Remaining: 55 TODOs across 5 issues**

---

## BoxscoreSchedule

| Line | TODO Comment |
|------|--------------|
| 381 | What is the difference between a BoxscoreTeam and a Team? |
| 422 | Should there be an enum defined for team abbreviations? |

## BroadcastInfo

| Line | TODO Comment |
|------|--------------|
| 535 | Should there be a component for TV and Streaming channels? |

## CoachesFilmVideo

| Line | TODO Comment |
|------|--------------|
| 704 | Would this reference the proposed network component from earlier? |
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

## GameInsight

| Line | TODO Comment |
|------|--------------|
| 2551 | Investigate GameInsight.content object |

## GamePreviewResponse

| Line | TODO Comment |
|------|--------------|
| 2606 | Investigate the GamePreviewResponse.preview object |

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

## InsightContentExplanation

| Line | TODO Comment |
|------|--------------|
| 3110 | More explanation properties |

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

## Player

| Line | TODO Comment |
|------|--------------|
| 4122 | Surely this can be an enum |

## PlayerInjury

| Line | TODO Comment |
|------|--------------|
| 4182 | Investigate the PlayerInjury object |

## PlayerPassingStats

**Note:** WeeklyPlayerPassingStats has been consolidated to extend PlayerPassingStats using allOf composition.

| Line | TODO Comment |
|------|--------------|
| N/A | To what degree can this be consolidated with Passing/Passer Stats? (Partially addressed: WeeklyPlayerPassingStats now extends PlayerPassingStats) |

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

**Note:** BoxscoreSite, GameSite, and Site have been consolidated into a single Site schema.

| Line | TODO Comment |
|------|--------------|
| N/A | Compare this to Venue and see if they can be consolidated (Venue kept separate due to different field naming and structure) |

## Standings

| Line | TODO Comment |
|------|--------------|
| 6139 | Can this be replaced with one of the Team components? |

## Venue

**Note:** TeamVenue has been consolidated into Venue schema.

| Line | TODO Comment |
|------|--------------|
| N/A | Compare with Site and consolidate as possible (TeamVenue already consolidated; Site kept separate due to different field naming) |

## WeeklyGameDetail

| Line | TODO Comment |
|------|--------------|
| 8084 | Compare to Game component, consolidate if possible |
| 8097 | Investigate the WeeklyGameDetail.replays object, define spec |
| 8103 | Investigate the WeeklyGameDetail.summary object |
| 8108 | Investigate the WeeklyGameDetail.taggedVideos object. |
