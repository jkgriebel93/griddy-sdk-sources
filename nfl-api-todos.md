# TODO Comments in nfl-com-api.yaml

Original remaining TODOs: 77
Total resolved: 61
**Current remaining: 16 TODOs**

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
- ✅ **Game Schema Consolidation**: Consolidated ProGame into Game schema (1 TODO)
- ✅ **Week Schema Consolidation**: Consolidated ProWeek into Week schema (1 TODO)
- ✅ **Team Schema Cleanup**: Deleted unused ByeTeam schema and consolidated ScheduleTeam into BoxscoreTeam (1 TODO)
- ✅ **Additional Manual Cleanup**: Resolved 3 additional TODOs through manual review and spec updates
- ✅ **WeeklyGameDetail Schema Definition**: Created comprehensive schemas for replays and summary objects (2 TODOs)
  - Created WeeklyGameDetailReplay with 50+ properties for video metadata
  - Created WeeklyGameDetailSummary with supporting schemas (WeeklyGameDetailSummaryTeam, WeeklyGameDetailSummaryScore, WeeklyGameDetailSummaryTimeouts)
  - Based on actual API response data from scratch/football_v2_experience_weekly-game-details.json
- ✅ **GamecenterResponse Leaders Schema Definition**: Previously defined all three leader leaderboard types (3 TODOs)
  - Created PassDistanceLeaderEntry schema extending LeaderEntryBaseSchema
  - Created SpeedLeaderEntry schema extending LeaderEntryBaseSchema
  - Created TimeToSackLeaderEntry schema extending LeaderEntryBaseSchema
  - All follow consistent pattern with home/visitor arrays
- ✅ **PassRusherStats Schema Definition**: Previously defined comprehensive pass rusher statistics schema (1 TODO)
  - Complete schema with player identification and pass rush performance metrics
  - Includes blitzCount, avgSeparationToQb, tackles, assists, sacks, and forcedFumbles

**Total Completed: 61 TODOs across 18 items**

## Remaining Issues

The following issues have not yet been addressed:
- ⏸️ [Issue #8](https://github.com/jkgriebel93/griddy-sdk-sources/issues/8): Investigate and define undefined object structures (14 TODOs, 6 completed) - *Research-heavy*
- ⏸️ [Issue #12](https://github.com/jkgriebel93/griddy-sdk-sources/issues/12): Create miscellaneous missing enums (2 TODOs)

**Total Remaining: 16 TODOs across 2 issues**

Note: Issues #7 (Consolidate duplicate or similar components), #9 (Refactor metrics explanation components), and #13 (Address miscellaneous TODO comments) have been fully resolved.

---

## CoachesFilmVideo

| Line | TODO Comment |
|------|--------------|
| 901 | Investigate the CoachesFilmVideo.videos object |

## CurrentGame

| Line | TODO Comment |
|------|--------------|
| 1033 | Investigate the CurrentGame.extensions object |

## FilmroomPlay

| Line | TODO Comment |
|------|--------------|
| 2177 | Investigate what the selectedParamValues object can look like |

## FuturesMarket

| Line | TODO Comment |
|------|--------------|
| 2239 | Investigate what this fixture object looks like |

## Game

**Note:** ProGame has been consolidated into Game schema. Game now uses Team (instead of ProTeam) and WeekTypeEnum.

| Line | TODO Comment |
|------|--------------|
| 2319 | Investigate the Game.extensions object |

## GameInsight

| Line | TODO Comment |
|------|--------------|
| 2444 | Investigate GameInsight.content object |

## GamePreviewResponse

| Line | TODO Comment |
|------|--------------|
| 2499 | Investigate the GamePreviewResponse.preview object |

## GameStatsResponse

| Line | TODO Comment |
|------|--------------|
| 2621 | Investigate the GameStatsResponse.data object |

## GamecenterResponse

**Note:** All three leader properties (passDistanceLeaders, speedLeaders, timeToSackLeaders) have been defined with proper schemas (PassDistanceLeaderEntry, SpeedLeaderEntry, TimeToSackLeaderEntry).

## PassRusherStats

**Note:** PassRusherStats schema has been fully defined with player identification and pass rush performance metrics.

## PlayerInjury

| Line | TODO Comment |
|------|--------------|
| 3952 | Investigate the PlayerInjury object |

## PlayerStatistic

| Line | TODO Comment |
|------|--------------|
| 4805 | Investigate the PlayerStatistic object |

## PlayerStatsResponse

| Line | TODO Comment |
|------|--------------|
| 4823 | Investigate the PlayerStatsResponse.players.stats object |
| 4835 | Investigate PlayerStatsResponse.statCategory; find out if it can be an enum |

## PlayerWeekProjectedPoints

| Line | TODO Comment |
|------|--------------|
| 4855 | Investigate PlayerWeekProjectedPoints.settingsCode, create enum |

## ReceiverStats

| Line | TODO Comment |
|------|--------------|
| 5248 | Investigate and define the ReceiverStats object |

## RusherStats

| Line | TODO Comment |
|------|--------------|
| 5427 | Investigate the RusherStats object. Note that it may be very similar if not identical to RushingStats |

## WeeklyGameDetail

**Note:** WeeklyGameDetailReplay and WeeklyGameDetailSummary schemas have been created with supporting components (WeeklyGameDetailSummaryTeam, WeeklyGameDetailSummaryScore, WeeklyGameDetailSummaryTimeouts).

| Line | TODO Comment |
|------|--------------|
| 7797 | Investigate the WeeklyGameDetail.taggedVideos object |
