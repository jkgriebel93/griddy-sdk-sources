# NFL OpenAPI Spec Refactoring Summary

## Overview

The original NFL OpenAPI specification (`nfl-com-api.yaml`) has been successfully refactored into three separate, well-organized files:

1. **nfl-shared.yaml** - Shared schema definitions used by both APIs
2. **nfl-pro-api.yaml** - Pro API endpoints and exclusive schemas
3. **nfl-regular-api.yaml** - Regular API endpoints and exclusive schemas

## File Details

### 1. nfl-shared.yaml

- **File Size**: 25,673 bytes (25.1 KB)
- **Line Count**: 990 lines
- **Schemas**: 45 shared schemas
- **OpenAPI Version**: 3.0.3
- **Structure**: Contains only the `components/schemas` section
- **Purpose**: Provides common schema definitions referenced by both Pro and Regular APIs

**Key Shared Schemas**:
- Award, BroadcastInfo, CareerStats, Clinched, ConferenceEnum
- DefensiveStats, PassingStats, ReceivingStats, RushingStats, KickingStats
- Game, GamePhaseEnum, GameResultEnum, GameStatusEnum
- Player, PlayerDetail, Team, Venue, Week
- SeasonTypeEnum, SeasonStats, Standings, StandingsResponse
- InjuryEntry, InjuryReportResponse, TeamInjuryReport
- And 25 more...

### 2. nfl-pro-api.yaml

- **File Size**: 286,226 bytes (279.5 KB)
- **Line Count**: 9,852 lines
- **Server URL**: https://pro.nfl.com
- **Paths**: 45 API endpoints
- **Exclusive Schemas**: 142 schemas
- **Tags**: 27 tags
- **External References**: 94 references to `nfl-shared.yaml`
- **OpenAPI Version**: 3.0.3

**Description**: NFL's Pro API for accessing advanced statistics, film room content, player data, and fantasy information. Provides comprehensive access to NFL Pro features including Next Gen Stats, Film Room analysis, player projections, and game insights.

**Sample Endpoints**:
- `/api/content/game/preview` - Game previews and insights
- `/api/content/home-film-cards` - Film room card content
- `/api/players/search` - Player search functionality
- `/api/plays/summaryPlay` - Play-by-play summaries
- `/api/schedules/current` - Current game schedules
- `/api/scores/live/games` - Live game scores
- `/api/secured/stats/fantasy/season` - Fantasy statistics
- `/api/secured/stats/players-offense/passing/season` - Passing stats
- `/api/secured/videos/coaches` - Coaches film content
- `/api/teams/roster` - Team rosters

**Key Pro-Exclusive Schemas**:
- BoxScorePlayerStatistics (multiple types)
- CoachesFilmResponse, CoachesFilmVideo
- DefensivePlayerOverviewStats, DefensivePassRushStats
- FantasyPlayerStats, FantasyStatsResponse
- FilmroomPlay, FilmroomPlaysResponse
- GamecenterResponse, GameDetail, GameInsight
- PasserStats, ReceiverStats, RusherStats
- PlayerProjection, ProjectedStatsResponse
- TeamBoxScore, TeamOffensePassStats, TeamDefensePassStats
- WinProbabilityResponse

### 3. nfl-regular-api.yaml

- **File Size**: 50,806 bytes (49.6 KB)
- **Line Count**: 1,767 lines
- **Server URL**: https://api.nfl.com
- **Paths**: 18 API endpoints
- **Exclusive Schemas**: 35 schemas
- **Tags**: 3 tags (Authentication, Experience, Football)
- **External References**: 53 references to `nfl-shared.yaml`
- **OpenAPI Version**: 3.0.3

**Description**: NFL's public API for accessing game schedules, team information, standings, statistics, and venue data. Provides comprehensive access to NFL data including real-time game information, team rosters, seasonal statistics, and historical data.

**Sample Endpoints**:
- `/experience/v1/games` - Game information by season/week
- `/experience/v1/teams` - All NFL teams
- `/football/v2/draft/{year}` - Draft information
- `/football/v2/games/{gameId}/boxscore` - Game box scores
- `/football/v2/games/{gameId}/playbyplay` - Play-by-play data
- `/football/v2/injuries` - Injury reports
- `/football/v2/players/{playerId}` - Player details
- `/football/v2/standings` - Team standings
- `/football/v2/stats/players/season` - Season player stats
- `/football/v2/transactions` - Player transactions
- `/football/v2/venues` - Stadium/venue information
- `/identity/v3/token` - Authentication token generation

**Key Regular-Exclusive Schemas**:
- BoxScoreResponse, DraftPick, DraftResponse
- Drive, DriveResultEnum, Play, PlayByPlayResponse
- PlayParticipant, PlayParticipantRoleEnum
- PlayerGameStats, PlayerStatsResponse, TeamGameStats
- Replay, ScoringPlay, ScoreTypeEnum
- TokenRequest, TokenResponse, RefreshTokenRequest
- Transaction, TransactionTypeEnum, TransactionsResponse
- WeeklyGameDetail, Summary, VenuesResponse

## Schema Distribution

| Category | Count | Percentage |
|----------|-------|------------|
| **Total Schemas** | **222** | **100%** |
| Shared Schemas | 45 | 20.3% |
| Pro Exclusive | 142 | 64.0% |
| Regular Exclusive | 35 | 15.8% |

## Path Distribution

| API | Paths | Percentage |
|-----|-------|------------|
| **Total Paths** | **63** | **100%** |
| Pro API | 45 | 71.4% |
| Regular API | 18 | 28.6% |

## Technical Implementation

### External References

Both API specs use external references to shared schemas following the format:
```yaml
$ref: './nfl-shared.yaml#/components/schemas/SchemaName'
```

**Reference Counts**:
- Pro API: 94 external references to shared schemas
- Regular API: 53 external references to shared schemas

### Server Configuration

**Pro API**:
```yaml
servers:
  - url: https://pro.nfl.com
    description: Production NFL Pro API
```

**Regular API**:
```yaml
servers:
  - url: https://api.nfl.com
    description: Production Regular NFL API
```

### Security

Both API specs include the `NFLAuth` security scheme:
```yaml
security:
  - NFLAuth: []

components:
  securitySchemes:
    NFLAuth:
      type: http
      scheme: bearer
```

### Tags

Tags have been distributed based on actual path usage:
- **Pro API**: 27 tags including Betting, Content, Fantasy Statistics, Filmroom, Win Probability, etc.
- **Regular API**: 3 tags - Authentication, Experience, Football

## Validation Results

All refactored specs have been validated:

- Valid YAML syntax
- Correct external reference format
- Proper server URL configuration
- Security schemes preserved
- Tags correctly distributed
- All 45 shared schemas correctly extracted
- All 142 Pro exclusive schemas included
- All 35 Regular exclusive schemas included
- All 45 Pro API paths included
- All 18 Regular API paths included

## Issues Encountered

**Minor Issue**:
- One line in `shared_schemas.txt` ("and should go in the shared spec") was incorrectly parsed as a schema name
- **Impact**: None - this non-existent schema was ignored during processing
- All 45 valid shared schemas were correctly extracted

**No other issues encountered.**

## Benefits of Refactoring

1. **Separation of Concerns**: Pro and Regular APIs are now clearly separated with distinct purposes
2. **Reduced Duplication**: Shared schemas are defined once and referenced by both APIs
3. **Better Organization**: Each API spec is focused and easier to understand
4. **Improved Maintainability**: Changes to shared schemas automatically propagate to both APIs
5. **Clearer Documentation**: Each API has its own description and relevant tags
6. **Smaller File Sizes**: Individual specs are smaller and easier to work with
7. **API-Specific Configuration**: Each API has its own server URL and metadata

## Usage

### Viewing Shared Schemas
```bash
cat nfl-shared.yaml
```

### Viewing Pro API Spec
```bash
cat nfl-pro-api.yaml
```

### Viewing Regular API Spec
```bash
cat nfl-regular-api.yaml
```

### Validating Specs
```bash
# Using OpenAPI validators
openapi-generator-cli validate -i nfl-pro-api.yaml
openapi-generator-cli validate -i nfl-regular-api.yaml
```

## File Locations

All refactored files are located in:
```
/home/jkgriebel/Repos/griddy-sdk-sources/openapi/refactored/
├── nfl-shared.yaml
├── nfl-pro-api.yaml
├── nfl-regular-api.yaml
└── REFACTORING_SUMMARY.md (this file)
```

## Original Source

The original combined specification:
```
/home/jkgriebel/Repos/griddy-sdk-sources/openapi/nfl-com-api.yaml
```

## Conclusion

The refactoring has been completed successfully with all requirements met:
- Shared schemas isolated in a dedicated file
- Pro API and Regular API properly separated
- External references correctly configured
- Server URLs appropriately set
- All schemas, paths, and metadata preserved
- Valid OpenAPI 3.0.3 specifications

The refactored specifications are production-ready and can be used for:
- SDK generation
- API documentation
- Client library development
- API testing and validation
- Development tooling integration
