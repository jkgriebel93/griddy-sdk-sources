# NFL API OpenAPI Spec Analysis Report

## Executive Summary

This analysis examines the `/home/jkgriebel/Repos/griddy-sdk-sources/openapi/nfl-com-api.yaml` file to determine how to split it into separate Pro API and Regular API specifications while maintaining a shared component library.

## Key Findings

- **Total Paths**: 63 endpoints
  - **Pro API Paths** (`/api/*`): 45 endpoints
  - **Regular API Paths**: 18 endpoints

- **Total Schemas**: 268 unique schemas
  - **Shared Schemas** (used by both): 45 schemas
  - **Pro API Exclusive**: 142 schemas
  - **Regular API Exclusive**: 35 schemas

## Path Breakdown

### Pro API Paths (45 total)

All paths starting with `/api/`:

1. `/api/content/game/preview`
2. `/api/content/home-film-cards`
3. `/api/content/insights/game`
4. `/api/content/insights/season`
5. `/api/players/player`
6. `/api/players/projectedStats`
7. `/api/players/search`
8. `/api/plays/summaryPlay`
9. `/api/schedules/current`
10. `/api/schedules/game`
11. `/api/schedules/game/matchup/rankings`
12. `/api/schedules/game/team/injuries`
13. `/api/schedules/games`
14. `/api/schedules/genius/future/odds`
15. `/api/schedules/standings`
16. `/api/schedules/week/odds`
17. `/api/schedules/weeks`
18. `/api/scores/live/games`
19. `/api/secured/plays/winProbability`
20. `/api/secured/plays/winProbabilityMin`
21. `/api/secured/stats/defense/nearest/season`
22. `/api/secured/stats/defense/overview/season`
23. `/api/secured/stats/defense/passRush/season`
24. `/api/secured/stats/fantasy/season`
25. `/api/secured/stats/players-offense/passing/season`
26. `/api/secured/stats/players-offense/passing/week`
27. `/api/secured/stats/players-offense/receiving/season`
28. `/api/secured/stats/players-offense/receiving/week`
29. `/api/secured/stats/players-offense/rushing/season`
30. `/api/secured/stats/players-offense/rushing/week`
31. `/api/secured/stats/team-defense/overview/season`
32. `/api/secured/stats/team-defense/pass/season`
33. `/api/secured/stats/team-defense/rush/season`
34. `/api/secured/stats/team-offense/overview/season`
35. `/api/secured/stats/team-offense/pass/season`
36. `/api/secured/videos/coaches`
37. `/api/secured/videos/filmroom/plays`
38. `/api/stats/boxscore`
39. `/api/stats/game/team-rankings`
40. `/api/stats/gamecenter`
41. `/api/stats/multiple-rankings/all-teams`
42. `/api/teams/all`
43. `/api/teams/roster`
44. `/api/teams/rosterWeek`
45. `/api/teams/schedule`

### Regular API Paths (18 total)

All paths NOT starting with `/api/`:

1. `/experience/v1/games`
2. `/experience/v1/teams`
3. `/football/v2/draft/{year}`
4. `/football/v2/experience/weekly-game-details`
5. `/football/v2/games/season/{season}/seasonType/{seasonType}/week/{week}`
6. `/football/v2/games/{gameId}/boxscore`
7. `/football/v2/games/{gameId}/playbyplay`
8. `/football/v2/injuries`
9. `/football/v2/players/teams/{teamId}/roster`
10. `/football/v2/players/{playerId}`
11. `/football/v2/standings`
12. `/football/v2/stats/live/game-summaries`
13. `/football/v2/stats/players/season`
14. `/football/v2/transactions`
15. `/football/v2/venues`
16. `/football/v2/weeks/season/{season}`
17. `/identity/v3/token`
18. `/identity/v3/token/refresh`

## Schema Dependencies

### Shared Schemas (45 total)

These schemas are used by **BOTH** Pro API and Regular API and should be placed in a shared specification:

1. Award
2. BroadcastInfo
3. CareerStats
4. Clinched
5. ConferenceEnum
6. ContractInfo
7. DefensiveStats
8. ExternalId
9. Game
10. GamePhaseEnum
11. GameResultEnum
12. GameStatusEnum
13. InjuredPlayerGameStatusEnum
14. InjuryEntry
15. InjuryReportResponse
16. KickingStats
17. MeridiemEnum
18. NextGenStatsPositionEnum
19. NextGenStatsPositionGroupEnum
20. OverallRecord
21. Pagination
22. PassingStats
23. PlayTypeEnum
24. Player
25. PlayerDetail
26. PointsRecord
27. PracticeStatusEnum
28. PrimetimeGameCategoryEnum
29. ReceivingStats
30. Record
31. RushingStats
32. SeasonStats
33. SeasonTypeEnum
34. SocialMedia
35. Standings
36. StandingsRecord
37. StandingsResponse
38. Team
39. TeamInjuryReport
40. TeamTypeEnum
41. TicketVendor
42. Venue
43. Week
44. WeekSlugEnum
45. WeekTypeEnum

### Pro API Exclusive Schemas (142 total)

These schemas are ONLY used by Pro API paths:

1. BinaryFlagEnum
2. BoxScorePlayerExtraPointsStatistic
3. BoxScorePlayerFieldGoalsStatistic
4. BoxScorePlayerFumblesStatistic
5. BoxScorePlayerKickReturnStatistic
6. BoxScorePlayerKickingStatistic
7. BoxScorePlayerPassingStatistic
8. BoxScorePlayerPuntReturnStatistic
9. BoxScorePlayerPuntingStatistic
10. BoxScorePlayerReceivingStatistic
11. BoxScorePlayerRushingStatistic
12. BoxScorePlayerTacklesStatistic
13. BoxscoreSchedule
14. BoxscoreScore
15. BoxscoreTeam
16. CameraSourceEnum
17. CoachesFileVideoSubTypeEnum
18. CoachesFilmResponse
19. CoachesFilmVideo
20. Conference
21. CurrentGame
22. CurrentGamesResponse
23. DefensiveOverviewStatsResponse
24. DefensivePassRushStats
25. DefensivePlayerOverviewStats
26. DefensivePlayerStats
27. DefensivePositionEnum
28. DefensivePositionGroupEnum
29. DefensiveStatsResponse
30. Division
31. FantasyPlayerPositionEnum
32. FantasyPlayerStats
33. FantasyPositionGroupEnum
34. FantasyStatsResponse
35. FilmCard
36. FilmroomPlay
37. FilmroomPlaysResponse
38. FuturesMarket
39. FuturesOddsResponse
40. GameDetail
41. GameInsight
42. GameOdds
43. GamePreviewResponse
44. GameSchedule
45. GameScore
46. GameTeam
47. GamecenterResponse
48. GamecenterSchedule
49. GamesResponse
50. HomeFilmCardsResponse
51. Insight
52. LeaderEntryBaseSchema
53. LineOfScrimmageDistanceEnum
54. LiveGame
55. LiveScoresResponse
56. MatchupRankingsResponse
57. MoneyLine
58. MultipleRankingsCategory
59. OddsSelection
60. OffensivePlayerPositionEnum
61. OffensiveSkillPositionEnum
62. ParticipantPlayerInfo
63. PassDistanceLeaderEntry
64. PassRushStatsResponse
65. PassRusherStats
66. PasserStats
67. PassingSectionEnum
68. PassingStatsCategoryEnum
69. PassingStatsResponse
70. PassingZone
71. PassingZoneStats
72. PlayDetail
73. PlayDirectionEnum
74. PlayStateEnum
75. PlayStat
76. PlaySummaryResponse
77. PlayWinProbability
78. PlayerPassingStats
79. PlayerProjection
80. PlayerReceivingStats
81. PlayerRushingStats
82. PlayerSearchResponse
83. PlayerSearchResult
84. PlayerStatisticBaseSchema
85. PlayerWeekProjectedPoints
86. PlayerWeekProjectedStats
87. PointSpread
88. PositionGroupEnum
89. ProTeam
90. ProjectedStatsResponse
91. ReceiverStats
92. ReceivingStatsCategoryEnum
93. ReceivingStatsResponse
94. ResponseMetadata
95. RoofTypeEnum
96. RushLocationMapEntry
97. RusherStats
98. RushingInfo
99. RushingMap
100. RushingStatsResponse
101. ScheduledGame
102. SeasonWeeksResponse
103. Site
104. SortOrderEnum
105. SpeedLeaderEntry
106. StatisticRanking
107. StatsQueryMetadata
108. SuccessLevelEnum
109. TeamBoxScore
110. TeamBoxscore
111. TeamDefensePassStats
112. TeamDefensePassStatsResponse
113. TeamDefenseRushStats
114. TeamDefenseRushStatsResponse
115. TeamDefenseStats
116. TeamDefenseStatsResponse
117. TeamInfo
118. TeamMatchupRankings
119. TeamOffenseOverviewStats
120. TeamOffenseOverviewStatsResponse
121. TeamOffensePassStats
122. TeamOffensePassStatsResponse
123. TeamRankingEntry
124. TeamRankings
125. TeamRankingsResponse
126. TeamRosterResponse
127. TeamScore
128. TimeToSackLeaderEntry
129. Totals
130. VenueInfo
131. VideoAuthorizations
132. VideoGamePlayIds
133. VideoTag
134. VideoThumbnail
135. WeeklyOddsResponse
136. WeeklyPassingStatsResponse
137. WeeklyPlayer
138. WeeklyPlayerPassingStats
139. WeeklyPlayerRushingStats
140. WeeklyRosterResponse
141. WeeklyRushingStatsResponse
142. WinProbabilityResponse

### Regular API Exclusive Schemas (35 total)

These schemas are ONLY used by Regular API paths:

1. BoxScoreResponse
2. DraftPick
3. DraftResponse
4. Drive
5. DriveResultEnum
6. ExperienceGamesResponse
7. ExperienceTeamsResponse
8. FootballGamesResponse
9. GameStatsResponse
10. NetworkTypeEnum
11. Penalty
12. Play
13. PlayByPlayResponse
14. PlayParticipant
15. PlayParticipantRoleEnum
16. PlayerGameStats
17. PlayerStatsResponse
18. RefreshTokenRequest
19. Replay
20. RosterResponse
21. ScoreTypeEnum
22. ScoringPlay
23. Summary
24. TeamGameStats
25. TokenRequest
26. TokenResponse
27. Transaction
28. TransactionTypeEnum
29. TransactionsResponse
30. VenuesResponse
31. WeeklyGameDetail
32. WeeklyGameDetailSummaryScore
33. WeeklyGameDetailSummaryTeam
34. WeeklyGameDetailSummaryTimeouts
35. WeeksResponse

## Recommended Split Strategy

Based on this analysis, here's the recommended approach for splitting the specification:

### 1. Create Shared Specification (`nfl-shared.yaml`)

- Contains the 45 shared schemas that are used by both APIs
- Includes common enums and base types
- Can be referenced by both Pro and Regular API specs using `$ref`

### 2. Create Pro API Specification (`nfl-pro-api.yaml`)

- Contains all 45 `/api/*` paths
- References the shared spec for common schemas
- Contains 142 Pro-exclusive schemas
- Total schemas: 187 (45 shared + 142 exclusive)

### 3. Create Regular API Specification (`nfl-regular-api.yaml`)

- Contains all 18 non-`/api/*` paths (including authentication endpoints)
- References the shared spec for common schemas
- Contains 35 Regular-exclusive schemas
- Total schemas: 80 (45 shared + 35 exclusive)

## Benefits of This Approach

1. **Reduced Duplication**: Shared schemas are defined once and referenced by both specs
2. **Easier Maintenance**: Updates to shared schemas automatically propagate to both APIs
3. **Clear Separation**: Pro and Regular API functionality is clearly delineated
4. **SDK Generation**: Can generate separate SDKs for Pro and Regular APIs
5. **Type Safety**: Shared types ensure consistency across both API implementations

## Implementation Notes

- Use OpenAPI's `$ref` mechanism to reference the shared specification
- Consider using relative file references: `$ref: './nfl-shared.yaml#/components/schemas/SchemaName'`
- Maintain consistent versioning across all three specifications
- Update all three specs together when making changes to shared components

## Generated Files

The following analysis files have been generated in `/home/jkgriebel/Repos/griddy-sdk-sources/`:

- `pro_api_paths.txt` - List of all Pro API endpoints
- `regular_api_paths.txt` - List of all Regular API endpoints
- `shared_schemas.txt` - List of schemas to place in shared spec
- `pro_exclusive_schemas.txt` - List of schemas exclusive to Pro API
- `regular_exclusive_schemas.txt` - List of schemas exclusive to Regular API
- `schema_analysis_summary.txt` - Summary statistics
- `analyze_schemas.py` - The Python script used for this analysis
