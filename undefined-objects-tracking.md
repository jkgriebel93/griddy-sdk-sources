# Undefined Object Structures Tracking

**Related Issue:** [#8 - Investigate and define undefined object structures](https://github.com/jkgriebel93/griddy-sdk-sources/issues/8)

**Total TODOs:** 20
**Completed:** 11
**Remaining:** 9

This document tracks all schema components in the NFL API OpenAPI specification that contain undefined object structures requiring investigation and proper schema definition.

---

## Table of Contents

1. [CoachesFilmVideo.videos](#coachesfilmvideovideos)
2. [CurrentGame.extensions](#currentgameextensions)
3. [FilmroomPlay.selectedParamValues](#filmroomplayselectedparamvalues)
4. [FuturesMarket.fixture](#futuresmarketfixture)
5. [Game.extensions](#gameextensions)
6. ~~[GameInsight.content](#gameinsightcontent)~~
7. [GamePreviewResponse.preview](#gamepreviewresponsepreview)
8. ~~[GameStatsResponse.data](#gamestatsresponsedata)~~
9. ~~[GamecenterResponse.leaders (3 properties)](#gamecenterresponseleaders)~~
10. ~~[PassRusherStats](#passrusherstats)~~
11. [PlayerInjury](#playerinjury)
12. ~~[PlayerStatistic](#playerstatistic)~~
13. [PlayerStatsResponse.players.stats](#playerstatsresponseplayersstats)
14. ~~[ReceiverStats](#receiverstats)~~
15. ~~[RusherStats](#rusherstats)~~
16. [WeeklyGameDetail (3 properties)](#weeklygamedetail)
    - ~~replays~~
    - ~~summary~~
    - taggedVideos

---

## Schema Details

### CoachesFilmVideo.videos

**Note: ** This array has been empty in all requests I've seen.

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

So far API responses only seem to be including empty arrays for this


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

### GameInsight.content ✅ RESOLVED

**Schema Location:** `openapi/nfl-com-api.yaml:2440`

**Status:** **COMPLETED** - False TODO; schema was already complete

**Resolution:** This was a tracking error. No `content` field with a TODO comment exists in the `GameInsight` schema. The schema is comprehensive and well-defined with 20+ properties.

**Actual GameInsight Schema:**
The `GameInsight` schema (line 2440) is fully defined with the following properties:
- **Player Identification**: nflId, playerName, esbId, gsisId, smartId, jerseyNumber, position, headshot
- **Team Info**: teamId, teamAbbr
- **Game Context**: season, seasonType, week, gameId, date
- **Insight Content**: title, subNote1 (the actual content fields)
- **Metadata**: tags, id, evergreen, createdAt, createdBy, updatedAt, updatedBy

**Referenced By:**
- Used directly as array response schema

**API Endpoint:**
- `GET /api/content/insights/game` (line 8057)
  - Operation ID: `getGameInsights`
  - Returns: `array of GameInsight`

**Note:** The insight content is stored in `title` (short description) and `subNote1` (longer elaboration), not in a separate `content` object.

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

### GameStatsResponse.data ✅ RESOLVED

**Schema Location:** `openapi/nfl-com-api.yaml:2713`

**Status:** **COMPLETED** - Now references WeeklyGameDetailSummary schema

**Resolution:** Discovered that GameStatsResponse.data items have identical structure to WeeklyGameDetailSummary (live game state with scores, possession, field position, etc.).

**Current Definition:**
```yaml
data:
  description: Array of live game state summaries
  items:
    $ref: '#/components/schemas/WeeklyGameDetailSummary'
  type: array
```

**API Endpoint:**
- `GET /football/v2/stats/live/game-summaries` (line 12236)
  - Operation ID: `getLiveGameStatsSummaries`
  - Returns: `GameStatsResponse`

**Note:** Reuses existing WeeklyGameDetailSummary schema created for WeeklyGameDetail.summary

---

### GamecenterResponse.leaders ✅ RESOLVED

**Schema Location:** Multiple properties in GamecenterResponse (lines 2713-2745)

**Status:** **COMPLETED** - All three leader properties now have proper schema definitions

**Resolution:** Defined comprehensive schemas for all leader leaderboard types with supporting entry schemas.

**New Schema Components Created:**
- `PassDistanceLeaderEntry` (line 2698) - Extends LeaderEntryBaseSchema with passInfo.airDistance
- `SpeedLeaderEntry` (line 2678) - Extends LeaderEntryBaseSchema with maxSpeed
- `TimeToSackLeaderEntry` (line 2687) - Extends LeaderEntryBaseSchema with tackleInfo.timeToTackle

#### 1. passDistanceLeaders ✅

**Current Definition:**
```yaml
passDistanceLeaders:
  type: object
  properties:
    home:
      items:
        $ref: '#/components/schemas/PassDistanceLeaderEntry'
      type: array
    visitor:
      items:
        $ref: '#/components/schemas/PassDistanceLeaderEntry'
      type: array
```

#### 2. speedLeaders ✅

**Current Definition:**
```yaml
speedLeaders:
  type: object
  properties:
    home:
      items:
        $ref: '#/components/schemas/SpeedLeaderEntry'
      type: array
    visitor:
      items:
        $ref: '#/components/schemas/SpeedLeaderEntry'
      type: array
```

#### 3. timeToSackLeaders ✅

**Current Definition:**
```yaml
timeToSackLeaders:
  type: object
  properties:
    home:
      items:
        $ref: '#/components/schemas/TimeToSackLeaderEntry'
      type: array
    visitor:
      items:
        $ref: '#/components/schemas/TimeToSackLeaderEntry'
      type: array
```

**API Endpoint:**
- `GET /api/stats/gamecenter` (line 11418)
  - Operation ID: `getGamecenter`
  - Returns: `GamecenterResponse`

---

### PassRusherStats ✅ RESOLVED

**Schema Location:** `openapi/nfl-com-api.yaml:3361`

**Status:** **COMPLETED** - Comprehensive schema with player identification and pass rush statistics

**Resolution:** Defined complete schema for pass rusher statistics including player info and performance metrics.

**Current Definition:**
```yaml
PassRusherStats:
  properties:
    esbId:
      type: string
      example: 'VER641394'
    gsisId:
      type: string
      example: '00-0039852'
    teamId:
      type: string
      example: '2510'
    playerName:
      type: string
      example: 'Jared Verse'
    shortName:
      type: string
      example: 'J. Verse'
    jerseyNumber:
      type: integer
      example: 8
    position:
      $ref: '#/components/schemas/NextGenStatsPositionEnum'
    blitzCount:
      type: integer
      example: 37
    avgSeparationToQb:
      type: number
      format: float
      example: 4.797052221914545
    headshot:
      description: URL to player headshot image
      format: uri
      type: string
    tackles:
      type: integer
      example: 4
    assists:
      type: integer
      example: 2
    sacks:
      type: number
      format: float
      example: 1.5
    forcedFumbles:
      type: integer
      example: 1
  type: object
```

**Referenced By:**
- `GamecenterResponse.passRushers` (lines 2750, 2761) - Used in both home and visitor arrays

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

### PlayerStatistic ✅ RESOLVED

**Schema Location:** `openapi/nfl-com-api.yaml:5019`

**Status:** **COMPLETED** - Created comprehensive schemas for all player statistic categories

**Resolution:** Defined a base schema (`PlayerStatisticBaseSchema`) with common player identification fields, and created 11 specific statistic schemas that extend this base for different statistical categories.

**New Schema Components Created:**
- `PlayerStatisticBaseSchema` (line 6066) - Base schema with nflId, jerseyNumber, playerName, position
- `BoxScorePlayerPassingStatistic` (line 6080) - Passing statistics with completion percentage, QB rating, etc.
- `BoxScorePlayerRushingStatistic` (line 6125) - Rushing statistics with attempts, yards, touchdowns
- `BoxScorePlayerReceivingStatistic` (line 6143) - Receiving statistics with receptions, yards after catch
- `BoxScorePlayerKickingStatistic` (line 6168) - Kickoff statistics
- `BoxScorePlayerKickReturnStatistic` (line 6187) - Kick return statistics
- `BoxScorePlayerPuntReturnStatistic` (line 6207) - Punt return statistics
- `BoxScorePlayerTacklesStatistic` (line 6228) - Defensive statistics with tackles, sacks, QB hits
- `BoxScorePlayerFumblesStatistic` (line 6261) - Fumble-related statistics
- `BoxScorePlayerFieldGoalsStatistic` (line 6294) - Field goal statistics
- `BoxScorePlayerPuntingStatistic` (line 6312) - Punting statistics
- `BoxScorePlayerExtraPointsStatistic` (line 6335) - Extra point statistics

**Current Definition:**
```yaml
PlayerStatistic:
  additionalProperties: true
  description: Individual player statistics (structure varies by category)
  type: object
```

**Referenced By:**
- `TeamBoxscore` now uses specific statistic schemas:
  - `extraPoints` → `BoxScorePlayerExtraPointsStatistic`
  - `fieldGoals` → `BoxScorePlayerFieldGoalsStatistic`
  - `fumbles` → `BoxScorePlayerFumblesStatistic`
  - `kickReturn` → `BoxScorePlayerKickReturnStatistic`
  - `kicking` → `BoxScorePlayerKickingStatistic`
  - `passing` → `BoxScorePlayerPassingStatistic`
  - `puntReturn` → `BoxScorePlayerPuntReturnStatistic`
  - `punting` → `BoxScorePlayerPuntingStatistic`
  - `receiving` → `BoxScorePlayerReceivingStatistic`
  - `rushing` → `BoxScorePlayerRushingStatistic`
  - `tackles` → `BoxScorePlayerTacklesStatistic`

**Parent Schema:**
- `TeamBoxScore` - References `TeamBoxscore` for both away and home teams

**API Endpoint:**
- `GET /api/stats/boxscore` (line 11316)
  - Operation ID: `getStatsBoxscore`
  - Returns: `TeamBoxScore`

---

### PlayerStatsResponse.players.stats

I can't find the page that triggers this request

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

### ReceiverStats ✅ RESOLVED

**Schema Location:** `openapi/nfl-com-api.yaml:5501`

**Status:** **COMPLETED** - Comprehensive schema for Next Gen Stats receiving statistics

**Resolution:** Defined a complete schema extending `PlayerStatisticBaseSchema` with receiving metrics including targets, receptions, yards, touchdowns, and advanced Next Gen Stats metrics for separation, air yards, and cushion.

**Current Definition:**
```yaml
ReceiverStats:
  type: object
  allOf:
    - $ref: '#/components/schemas/PlayerStatisticBaseSchema'
    - properties:
        recYards:
          type: integer
          example: 85
        targets:
          type: integer
          example: 12
        receptions:
          type: integer
          example: 10
        touchdowns:
          type: integer
          example: 1
        receptionInfo:
          type: object
          properties:
            avgAirYards:
              type: number
              format: float
              example: 9.5725
            avgCushion:
              type: number
              format: float
              example: 6.998333333333334
            avgSeparation:
              type: number
              format: float
              example: 3.486743522705502
```

**Key Properties:**
- **recYards**: Total receiving yards
- **targets**: Number of times targeted
- **receptions**: Number of receptions
- **touchdowns**: Receiving touchdowns
- **receptionInfo.avgAirYards**: Average air yards (distance ball travels in air)
- **receptionInfo.avgCushion**: Average cushion (defender distance at snap)
- **receptionInfo.avgSeparation**: Average separation (defender distance at target)

**Referenced By:**
- `GamecenterResponse.receivers` (lines 2692, 2702) - Used in both home and visitor arrays

**API Endpoint:**
- `GET /api/stats/gamecenter` (line 11418)
  - Operation ID: `getGamecenter`
  - Returns: `GamecenterResponse`

---

### RusherStats ✅ RESOLVED

**Schema Location:** `openapi/nfl-com-api.yaml:5766`

**Status:** **COMPLETED** - Comprehensive schema for Next Gen Stats rushing statistics

**Resolution:** Defined a complete schema extending `PlayerStatisticBaseSchema` with rushing metrics including attempts, yards, touchdowns, and advanced Next Gen Stats metrics for distance traveled, time to line of scrimmage, and rush location maps.

**Current Definition:**
```yaml
RusherStats:
  type: object
  allOf:
    - $ref: '#/components/schemas/PlayerStatisticBaseSchema'
    - properties:
        yards:
          type: integer
          example: 131
        attempts:
          type: integer
          example: 14
        touchdowns:
          type: integer
          example: 2
        rushInfo:
          $ref: '#/components/schemas/RushingInfo'
```

**Key Properties:**
- **yards**: Total rushing yards
- **attempts**: Number of rushing attempts
- **touchdowns**: Rushing touchdowns
- **rushInfo**: Advanced Next Gen Stats metrics:
  - `distance`: Total distance traveled (e.g., 190.79 yards on 14 carries)
  - `avgYards`: Average yards per carry
  - `avgDistance`: Average distance traveled per carry
  - `avgTimeToLos`: Average time to reach line of scrimmage
  - `rushLocationMap`: Rush location distribution map
  - `preSnapRushLocationMap`: Pre-snap rush location distribution

**Referenced By:**
- `GamecenterResponse.rushers` (lines 2709, 2713) - Used in both home and visitor arrays

**API Endpoint:**
- `GET /api/stats/gamecenter` (line 11418)
  - Operation ID: `getGamecenter`
  - Returns: `GamecenterResponse`

**Note:** `RusherStats` is used by the Gamecenter endpoint with Next Gen Stats metrics, while the separate `RushingStats` schema is used by traditional stats endpoints. These serve different purposes and are intentionally kept separate.

---

### WeeklyGameDetail

**Schema Location:** Multiple properties in WeeklyGameDetail

#### 1. replays ✅ RESOLVED

**Line:** `openapi/nfl-com-api.yaml:7787`

**Status:** **COMPLETED** - Created `WeeklyGameDetailReplay` schema component

**Resolution:** Defined comprehensive schema for replay video information based on example API response data.

**New Schema Components Created:**
- `WeeklyGameDetailReplay` - Main replay object with 50+ properties including video metadata, authorization requirements, tags, and playback information

**Current Definition:**
```yaml
replays:
  description: Replay video information (populated when includeReplays=true)
  items:
    $ref: '#/components/schemas/WeeklyGameDetailReplay'
  nullable: true
  type: array
```

#### 2. summary ✅ RESOLVED

**Line:** `openapi/nfl-com-api.yaml:7793`

**Status:** **COMPLETED** - Created `WeeklyGameDetailSummary` schema component with supporting schemas

**Resolution:** Defined comprehensive schema for live game state summary based on example API response data.

**New Schema Components Created:**
- `WeeklyGameDetailSummary` - Main summary object with game state information
- `WeeklyGameDetailSummaryTeam` - Team-specific game state (possession, score, timeouts)
- `WeeklyGameDetailSummaryScore` - Quarter-by-quarter score breakdown
- `WeeklyGameDetailSummaryTimeouts` - Timeout tracking

**Current Definition:**
```yaml
summary:
  $ref: '#/components/schemas/WeeklyGameDetailSummary'
  description: Live game state summary including score, possession, and game situation
  nullable: true
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

**Game-Related Objects (3 TODOs, 4 completed):**
- CurrentGame.extensions
- Game.extensions
- GameInsight.content
- GamePreviewResponse.preview
- ✅ GameStatsResponse.data (COMPLETED)
- ✅ GamecenterResponse.leaders.passDistanceLeaders (COMPLETED)
- ✅ GamecenterResponse.leaders.speedLeaders (COMPLETED)
- ✅ GamecenterResponse.leaders.timeToSackLeaders (COMPLETED)

**Player Statistics (4 TODOs, 1 completed):**
- ✅ PassRusherStats (COMPLETED)
- ReceiverStats
- RusherStats
- PlayerStatistic
- PlayerStatsResponse.players.stats

**Video/Film Content (2 TODOs):**
- CoachesFilmVideo.videos
- FilmroomPlay.selectedParamValues

**Weekly Game Details (1 TODO, 2 completed):**
- ✅ WeeklyGameDetail.replays (COMPLETED)
- ✅ WeeklyGameDetail.summary (COMPLETED)
- WeeklyGameDetail.taggedVideos

**Other (3 TODOs):**
- FuturesMarket.fixture
- PlayerInjury (unused schema)

### Investigation Priority

**High Priority** (Used by multiple endpoints or core functionality):
- Game.extensions (used in 3 different response schemas)
- PlayerStatistic (used across 11 different stat categories in boxscores)

**Medium Priority** (Single endpoint, frequently accessed):
- GameInsight.content
- GamePreviewResponse.preview
- WeeklyGameDetail.taggedVideos (1 TODO remaining, 2 completed)

**Low Priority** (Specialized or unused):
- PlayerInjury (schema defined but not referenced by any endpoint)
- FilmroomPlay.selectedParamValues (specialized film room feature)
- CoachesFilmVideo.videos (secured endpoint)

---

## Completed Items

### WeeklyGameDetail.replays ✅

**Completed:** 2025-10-07

**Schema Components Created:**
- `WeeklyGameDetailReplay` (line 7448)

**Description:** Comprehensive schema for replay video metadata including authorization requirements, video properties, tags, thumbnails, and playback information. Contains 50+ properties covering all aspects of NFL+ replay content.

### WeeklyGameDetail.summary ✅

**Completed:** 2025-10-07

**Schema Components Created:**
- `WeeklyGameDetailSummary` (line 7657)
- `WeeklyGameDetailSummaryTeam` (line 7719)
- `WeeklyGameDetailSummaryScore` (line 7734)
- `WeeklyGameDetailSummaryTimeouts` (line 7762)

**Description:** Complete schema for live game state including score by quarter, possession status, timeouts, field position, game clock, weather, and other real-time game situation data. Uses composition pattern with separate schemas for team state, scoring, and timeout tracking.

### GamecenterResponse.leaders (3 properties) ✅

**Completed:** Previously (before 2025-10-07)

**Schema Components Created:**
- `PassDistanceLeaderEntry` (line 2698) - Pass distance leader with airDistance property
- `SpeedLeaderEntry` (line 2678) - Speed leader with maxSpeed property
- `TimeToSackLeaderEntry` (line 2687) - Time to sack leader with timeToTackle property

**Description:** All three leader leaderboard types (passDistanceLeaders, speedLeaders, timeToSackLeaders) now have proper schema definitions. Each extends `LeaderEntryBaseSchema` and adds sport-specific metrics. All three follow the same pattern with home/visitor arrays for each team.

### PassRusherStats ✅

**Completed:** Previously (before 2025-10-07)

**Schema Component:** `PassRusherStats` (line 3361)

**Description:** Complete schema for pass rusher statistics including player identification (esbId, gsisId, playerName, etc.) and performance metrics (blitzCount, avgSeparationToQb, tackles, assists, sacks, forcedFumbles). Used in GamecenterResponse for both home and visitor pass rush statistics.

### GameStatsResponse.data ✅

**Completed:** 2025-10-07

**Resolution:** Reuses existing `WeeklyGameDetailSummary` schema

**Description:** Discovered that GameStatsResponse.data items have the exact same structure as WeeklyGameDetailSummary (live game state with scores by quarter, possession status, timeouts, field position, game clock, weather, etc.). Updated to reference the existing schema instead of leaving it as a generic object.

---

**Last Updated:** 2025-10-07
