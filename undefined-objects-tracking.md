# Undefined Object Structures Tracking

**Related Issue:** [#8 - Investigate and define undefined object structures](https://github.com/jkgriebel93/griddy-sdk-sources/issues/8)

**Total TODOs:** 20

This document tracks all schema components in the NFL API OpenAPI specification that contain undefined object structures requiring investigation and proper schema definition.

---

## Table of Contents

1. [CoachesFilmVideo.videos](#coachesfilmvideovideos)
2. [CurrentGame.extensions](#currentgameextensions)
3. [FilmroomPlay.selectedParamValues](#filmroomplayselectedparamvalues)
4. [FuturesMarket.fixture](#futuresmarketfixture)
5. [Game.extensions](#gameextensions)
6. [GameInsight.content](#gameinsightcontent)
7. [GamePreviewResponse.preview](#gamepreviewresponsepreview)
8. [GameStatsResponse.data](#gamestatsresponsedata)
9. [GamecenterResponse.leaders (3 properties)](#gamecenterresponseleaders)
10. [PassRusherStats](#passrusherstats)
11. [PlayerInjury](#playerinjury)
12. [PlayerStatistic](#playerstatistic)
13. [PlayerStatsResponse.players.stats](#playerstatsresponseplayersstats)
14. [ReceiverStats](#receiverstats)
15. [RusherStats](#rusherstats)
16. [WeeklyGameDetail (3 properties)](#weeklygamedetail)

---

## Schema Details

### CoachesFilmVideo.videos

**Schema Location:** `openapi/nfl-com-api.yaml:901`

**TODO Comment:** `Investigate the CoachesFilmVideo.videos object`

**Current Definition:**
```yaml
videos:
  items:
    # TODO: Investigate the CoachesFilmVideo.videos object
    type: object
  type: array
```

**Referenced By:**
- `CoachesFilmResponse` (line 677)

**API Endpoint:**
- `GET /api/secured/videos/coaches` (line 10799)
  - Operation ID: `getCoaches`
  - Returns: `CoachesFilmResponse`

---

### CurrentGame.extensions

**Schema Location:** `openapi/nfl-com-api.yaml:1033`

**TODO Comment:** `Investigate the CurrentGame.extensions object`

**Current Definition:**
```yaml
extensions:
  items:
    # TODO: Investigate the CurrentGame.extensions object
    type: object
  type: array
```

**Referenced By:**
- `CurrentGamesResponse` (line 1090)

**API Endpoint:**
- `GET /api/schedules/current` (line 8394)
  - Operation ID: `getCurrentWeekGames`
  - Returns: `CurrentGamesResponse`

---

### FilmroomPlay.selectedParamValues

**Schema Location:** `openapi/nfl-com-api.yaml:2177`

**TODO Comment:** `Investigate what the selectedParamValues object can look like`

**Current Definition:**
```yaml
selectedParamValues:
  description: Filter parameters applied to select this play
  # TODO: Investigate what the selectedParamValues object can look like
  type: object
```

**Referenced By:**
- `FilmroomPlaysResponse` (line 2217)

**API Endpoint:**
- `GET /api/secured/videos/filmroom/plays` (line 10867)
  - Operation ID: `getFilmroomPlays`
  - Returns: `FilmroomPlaysResponse`

---

### FuturesMarket.fixture

**Schema Location:** `openapi/nfl-com-api.yaml:2239`

**TODO Comment:** `Investigate what this fixture object looks like`

**Current Definition:**
```yaml
fixture:
  description: Fixture information for the betting market
  # TODO: Investigate what this fixture object looks like
  type: object
```

**Referenced By:**
- `FuturesOddsResponse` (lines 2274, 2278, 2282) - Used in conference, division, and superBowl arrays

**API Endpoint:**
- `GET /api/schedules/genius/future/odds` (line 8603)
  - Operation ID: `getFutureBettingOdds`
  - Returns: `FuturesOddsResponse`

---

### Game.extensions

**Schema Location:** `openapi/nfl-com-api.yaml:2319`

**TODO Comment:** `Investigate the Game.extensions object`

**Current Definition:**
```yaml
extensions:
  items:
    # TODO: Investigate the Game.extensions object
    type: object
  type: array
```

**Referenced By:**
- `ExperienceGamesResponse` (line 1852)
- `FilmroomPlaysResponse` (line 2224)
- `GamesResponse` (line 2748)

**API Endpoints:**
- `GET /experience/v1/games` (line 11698)
  - Operation ID: `getExperienceGames`
  - Returns: `ExperienceGamesResponse`
- `GET /api/secured/videos/filmroom/plays` (line 10867)
  - Operation ID: `getFilmroomPlays`
  - Returns: `FilmroomPlaysResponse`

**Note:** The `Game` schema is also extended by `WeeklyGameDetail` using `allOf` composition.

---

### GameInsight.content

**Schema Location:** `openapi/nfl-com-api.yaml:2444`

**TODO Comment:** `Investigate GameInsight.content object`

**Current Definition:**
```yaml
content:
  description: Content body of the insight
  # TODO: Investigate GameInsight.content object
  type: object
```

**Referenced By:**
- Used directly as array response schema

**API Endpoint:**
- `GET /api/content/insights/game` (line 8057)
  - Operation ID: `getGameInsights`
  - Returns: `array of GameInsight`

---

### GamePreviewResponse.preview

**Schema Location:** `openapi/nfl-com-api.yaml:2499`

**TODO Comment:** `Investigate the GamePreviewResponse.preview object`

**Current Definition:**
```yaml
preview:
  description: Game preview and matchup information
  # TODO: Investigate the GamePreviewResponse.preview object
  type: object
```

**API Endpoint:**
- `GET /api/content/game/preview` (line 7984)
  - Operation ID: `getGamePreview`
  - Returns: `GamePreviewResponse`

---

### GameStatsResponse.data

**Schema Location:** `openapi/nfl-com-api.yaml:2621`

**TODO Comment:** `Investigate the GameStatsResponse.data object`

**Current Definition:**
```yaml
data:
  items:
    description: Game statistics data
    # TODO: Investigate the GameStatsResponse.data object
    type: object
  type: array
```

**API Endpoint:**
- `GET /football/v2/stats/live/game-summaries` (line 12236)
  - Operation ID: `getLiveGameStatsSummaries`
  - Returns: `GameStatsResponse`

---

### GamecenterResponse.leaders

**Schema Location:** Multiple properties in GamecenterResponse

#### 1. passDistanceLeaders

**Line:** `openapi/nfl-com-api.yaml:2655`

**TODO Comment:** `Investigate the GamecenterResponse.leaders.passDistanceLeaders object`

**Current Definition:**
```yaml
passDistanceLeaders:
  description: Top pass distance leaders for the game
  # TODO: Investigate the GamecenterResponse.leaders.passDistanceLeaders object
  type: object
```

#### 2. speedLeaders

**Line:** `openapi/nfl-com-api.yaml:2658`

**TODO Comment:** `Investigate the GamecenterResponse.leaders.speedLeaders object`

**Current Definition:**
```yaml
speedLeaders:
  description: Top speed leaders for the game
  # TODO: Investigate the GamecenterResponse.leaders.speedLeaders object
  type: object
```

#### 3. timeToSackLeaders

**Line:** `openapi/nfl-com-api.yaml:2661`

**TODO Comment:** `Investigate the GamecenterResponse.leaders.timeToSackLeaders object`

**Current Definition:**
```yaml
timeToSackLeaders:
  description: Time to sack leaders for the game
  # TODO: Investigate the GamecenterResponse.leaders.timeToSackLeaders object
  type: object
```

**API Endpoint:**
- `GET /api/stats/gamecenter` (line 11418)
  - Operation ID: `getGamecenter`
  - Returns: `GamecenterResponse`

---

### PassRusherStats

**Schema Location:** `openapi/nfl-com-api.yaml:3280`

**TODO Comment:** `Investigate the PassRusherStats object`

**Current Definition:**
```yaml
PassRusherStats:
  # TODO: Investigate the PassRusherStats object
  type: object
```

**Referenced By:**
- `GamecenterResponse.passRushers` (lines 2668, 2678) - Used in both home and visitor arrays

**API Endpoint:**
- `GET /api/stats/gamecenter` (line 11418)
  - Operation ID: `getGamecenter`
  - Returns: `GamecenterResponse`

---

### PlayerInjury

**Schema Location:** `openapi/nfl-com-api.yaml:3952`

**TODO Comment:** `Investigate the PlayerInjury object`

**Current Definition:**
```yaml
PlayerInjury:
  # TODO: Investigate the PlayerInjury object
  type: object
```

**Referenced By:**
- `ProInjuryReportResponse` (line 5050)

**API Endpoint:**
- **NOT CURRENTLY REFERENCED** by any API endpoint in the specification
- `ProInjuryReportResponse` schema is defined but unused

**Note:** There is a separate `InjuryReportResponse` used by `GET /api/schedules/game/team/injuries` (line 8496) which references `TeamInjuryReport` instead.

---

### PlayerStatistic

**Schema Location:** `openapi/nfl-com-api.yaml:4805`

**TODO Comment:** `Investigate the PlayerStatistic object`

**Current Definition:**
```yaml
PlayerStatistic:
  # TODO: Investigate the PlayerStatistic object
  type: object
```

**Referenced By:**
- `TeamBoxscore` (lines 5852, 5856, 5860, 5864, 5868, 5872, 5876, 5880, 5884, 5888, 5892)
  - Used for: extraPoints, fieldGoals, fumbles, kickReturn, kicking, passing, puntReturn, punting, receiving, rushing, tackles

**Parent Schema:**
- `TeamBoxScore` (lines 465, 471) - References `TeamBoxscore` for both away and home teams

**API Endpoint:**
- `GET /api/stats/boxscore` (line 11316)
  - Operation ID: `getStatsBoxscore`
  - Returns: `TeamBoxScore`

---

### PlayerStatsResponse.players.stats

**Schema Location:** `openapi/nfl-com-api.yaml:4823`

**TODO Comment:** `Investigate the PlayerStatsResponse.players.stats object`

**Current Definition:**
```yaml
stats:
  # TODO: Investigate the PlayerStatsResponse.players.stats object
  type: object
```

**API Endpoint:**
- `GET /football/v2/stats/players/season` (line 12282)
  - Operation ID: `getPlayerSeasonStats`
  - Returns: `PlayerStatsResponse`

---

### ReceiverStats

**Schema Location:** `openapi/nfl-com-api.yaml:5248`

**TODO Comment:** `Investigate and define the ReceiverStats object`

**Current Definition:**
```yaml
ReceiverStats:
  # TODO: Investigate and define the ReceiverStats object
  type: object
```

**Referenced By:**
- `GamecenterResponse.receivers` (lines 2692, 2702) - Used in both home and visitor arrays

**API Endpoint:**
- `GET /api/stats/gamecenter` (line 11418)
  - Operation ID: `getGamecenter`
  - Returns: `GamecenterResponse`

---

### RusherStats

**Schema Location:** `openapi/nfl-com-api.yaml:5427`

**TODO Comment:** `Investigate the RusherStats object. Note that it may be very similar if not identical to RushingStats`

**Current Definition:**
```yaml
RusherStats:
  # TODO: Investigate the RusherStats object. Note that it may be very similar if not identical to RushingStats
  type: object
```

**Referenced By:**
- `GamecenterResponse.rushers` (lines 2709, 2713) - Used in both home and visitor arrays

**API Endpoint:**
- `GET /api/stats/gamecenter` (line 11418)
  - Operation ID: `getGamecenter`
  - Returns: `GamecenterResponse`

**Note:** A `RushingStats` schema exists separately. Comparison needed to determine if consolidation is possible.

---

### WeeklyGameDetail

**Schema Location:** Multiple properties in WeeklyGameDetail

#### 1. replays

**Line:** `openapi/nfl-com-api.yaml:7461`

**TODO Comment:** `Investigate the WeeklyGameDetail.replays object, define spec`

**Current Definition:**
```yaml
replays:
  description: Replay video information (populated when includeReplays=true)
  items:
    # TODO: Investigate the WeeklyGameDetail.replays object, define spec
    type: object
  nullable: true
  type: array
```

#### 2. summary

**Line:** `openapi/nfl-com-api.yaml:7467`

**TODO Comment:** `Investigate the WeeklyGameDetail.summary object`

**Current Definition:**
```yaml
summary:
  description: Game summary information
  # TODO: Investigate the WeeklyGameDetail.summary object
  nullable: true
  type: object
```

#### 3. taggedVideos

**Line:** `openapi/nfl-com-api.yaml:7472`

**TODO Comment:** `Investigate the WeeklyGameDetail.taggedVideos object`

**Current Definition:**
```yaml
taggedVideos:
  description: Tagged video content (populated when includeTaggedVideos=true)
  # TODO: Investigate the WeeklyGameDetail.taggedVideos object
  nullable: true
  type: object
```

**API Endpoint:**
- `GET /football/v2/experience/weekly-game-details` (line 11837)
  - Operation ID: `getWeeklyGameDetails`
  - Returns: `array of WeeklyGameDetail`

**Note:** The `WeeklyGameDetail` schema extends `Game` using `allOf` composition.

---

## Summary

### By Category

**Game-Related Objects (7 TODOs):**
- CurrentGame.extensions
- Game.extensions
- GameInsight.content
- GamePreviewResponse.preview
- GameStatsResponse.data
- GamecenterResponse.leaders (3 properties)

**Player Statistics (5 TODOs):**
- PassRusherStats
- ReceiverStats
- RusherStats
- PlayerStatistic
- PlayerStatsResponse.players.stats

**Video/Film Content (2 TODOs):**
- CoachesFilmVideo.videos
- FilmroomPlay.selectedParamValues

**Weekly Game Details (3 TODOs):**
- WeeklyGameDetail.replays
- WeeklyGameDetail.summary
- WeeklyGameDetail.taggedVideos

**Other (3 TODOs):**
- FuturesMarket.fixture
- PlayerInjury (unused schema)

### Investigation Priority

**High Priority** (Used by multiple endpoints or core functionality):
- Game.extensions (used in 3 different response schemas)
- GamecenterResponse.leaders (3 properties, core stats endpoint)
- PlayerStatistic (used across 11 different stat categories in boxscores)

**Medium Priority** (Single endpoint, frequently accessed):
- GameInsight.content
- GamePreviewResponse.preview
- WeeklyGameDetail properties (3 TODOs)

**Low Priority** (Specialized or unused):
- PlayerInjury (schema defined but not referenced by any endpoint)
- FilmroomPlay.selectedParamValues (specialized film room feature)
- CoachesFilmVideo.videos (secured endpoint)

---

**Last Updated:** 2025-10-07
