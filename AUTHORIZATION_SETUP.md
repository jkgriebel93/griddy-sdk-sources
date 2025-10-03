# Custom Authorization Setup

Since Speakeasy hooks are not available on the free tier, you'll need to implement custom authorization wrappers for both SDKs. The workflow preserves custom `auth.py` and `auth.ts` files during regeneration.

## Python SDK (griddy-nfl-python)

Create a file `griddy_nfl/auth.py` in your Python SDK repository:

```python
"""Custom authorization wrapper for NFL API."""
import os
from typing import Optional
import httpx
from datetime import datetime, timedelta


class NFLAuthenticator:
    """Handles NFL API authentication with token refresh."""

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        token_url: str = "https://api.nfl.com/v1/auth/token"
    ):
        """Initialize authenticator.

        Args:
            client_id: NFL API client ID (defaults to NFL_CLIENT_ID env var)
            client_secret: NFL API client secret (defaults to NFL_CLIENT_SECRET env var)
            token_url: Token endpoint URL
        """
        self.client_id = client_id or os.getenv("NFL_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("NFL_CLIENT_SECRET")
        self.token_url = token_url
        self._access_token: Optional[str] = None
        self._token_expires_at: Optional[datetime] = None

        if not self.client_id or not self.client_secret:
            raise ValueError(
                "NFL API credentials not provided. Set NFL_CLIENT_ID and "
                "NFL_CLIENT_SECRET environment variables or pass them explicitly."
            )

    def get_access_token(self) -> str:
        """Get a valid access token, refreshing if necessary."""
        if self._access_token and self._token_expires_at:
            if datetime.now() < self._token_expires_at - timedelta(minutes=5):
                return self._access_token

        # Fetch new token
        response = httpx.post(
            self.token_url,
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "client_credentials"
            }
        )
        response.raise_for_status()

        token_data = response.json()
        self._access_token = token_data["access_token"]
        expires_in = token_data.get("expires_in", 3600)
        self._token_expires_at = datetime.now() + timedelta(seconds=expires_in)

        return self._access_token


class AuthenticatedSDK:
    """Wrapper around the generated SDK that handles authentication."""

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        **sdk_kwargs
    ):
        """Initialize authenticated SDK wrapper.

        Args:
            client_id: NFL API client ID
            client_secret: NFL API client secret
            **sdk_kwargs: Additional arguments to pass to the SDK
        """
        from griddy_nfl import GriddyNFL

        self.authenticator = NFLAuthenticator(client_id, client_secret)

        # Initialize SDK with bearer token
        self.sdk = GriddyNFL(
            security={"bearer": self.authenticator.get_access_token()},
            **sdk_kwargs
        )

    def __getattr__(self, name):
        """Proxy attribute access to the underlying SDK."""
        return getattr(self.sdk, name)

    def refresh_token(self):
        """Manually refresh the authentication token."""
        self.sdk.sdk_configuration.security = {
            "bearer": self.authenticator.get_access_token()
        }
```

### Usage Example (Python)

```python
from griddy_nfl.auth import AuthenticatedSDK

# Initialize with credentials
client = AuthenticatedSDK(
    client_id="your_client_id",
    client_secret="your_client_secret"
)

# Or use environment variables
# export NFL_CLIENT_ID=your_client_id
# export NFL_CLIENT_SECRET=your_client_secret
client = AuthenticatedSDK()

# Use the SDK normally
games = client.schedules.get_schedules(season=2024, week=1)
```

## TypeScript SDK (griddy-nfl-typescript)

Create a file `src/auth.ts` in your TypeScript SDK repository:

```typescript
/**
 * Custom authorization wrapper for NFL API.
 */
import axios, { AxiosInstance } from 'axios';
import { GriddyNFL } from './sdk';

interface TokenResponse {
  access_token: string;
  expires_in: number;
  token_type: string;
}

export class NFLAuthenticator {
  private clientId: string;
  private clientSecret: string;
  private tokenUrl: string;
  private accessToken?: string;
  private tokenExpiresAt?: Date;
  private httpClient: AxiosInstance;

  constructor(
    clientId?: string,
    clientSecret?: string,
    tokenUrl: string = 'https://api.nfl.com/v1/auth/token'
  ) {
    this.clientId = clientId || process.env.NFL_CLIENT_ID || '';
    this.clientSecret = clientSecret || process.env.NFL_CLIENT_SECRET || '';
    this.tokenUrl = tokenUrl;
    this.httpClient = axios.create();

    if (!this.clientId || !this.clientSecret) {
      throw new Error(
        'NFL API credentials not provided. Set NFL_CLIENT_ID and ' +
        'NFL_CLIENT_SECRET environment variables or pass them explicitly.'
      );
    }
  }

  async getAccessToken(): Promise<string> {
    // Return cached token if still valid
    if (this.accessToken && this.tokenExpiresAt) {
      const fiveMinutesFromNow = new Date(Date.now() + 5 * 60 * 1000);
      if (fiveMinutesFromNow < this.tokenExpiresAt) {
        return this.accessToken;
      }
    }

    // Fetch new token
    const response = await this.httpClient.post<TokenResponse>(
      this.tokenUrl,
      new URLSearchParams({
        client_id: this.clientId,
        client_secret: this.clientSecret,
        grant_type: 'client_credentials',
      }),
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }
    );

    this.accessToken = response.data.access_token;
    const expiresIn = response.data.expires_in || 3600;
    this.tokenExpiresAt = new Date(Date.now() + expiresIn * 1000);

    return this.accessToken;
  }
}

export class AuthenticatedSDK {
  private authenticator: NFLAuthenticator;
  public sdk: GriddyNFL;

  constructor(
    clientId?: string,
    clientSecret?: string,
    sdkOptions?: any
  ) {
    this.authenticator = new NFLAuthenticator(clientId, clientSecret);

    // We'll initialize the SDK after getting the first token
    this.sdk = new GriddyNFL({
      security: {
        bearer: '', // Will be set by init()
      },
      ...sdkOptions,
    });
  }

  async init(): Promise<void> {
    const token = await this.authenticator.getAccessToken();
    this.sdk = new GriddyNFL({
      security: {
        bearer: token,
      },
    });
  }

  async refreshToken(): Promise<void> {
    const token = await this.authenticator.getAccessToken();
    // Update the SDK configuration with new token
    (this.sdk as any).sdkConfiguration.security = {
      bearer: token,
    };
  }

  static async create(
    clientId?: string,
    clientSecret?: string,
    sdkOptions?: any
  ): Promise<AuthenticatedSDK> {
    const client = new AuthenticatedSDK(clientId, clientSecret, sdkOptions);
    await client.init();
    return client;
  }
}
```

### Usage Example (TypeScript)

```typescript
import { AuthenticatedSDK } from './auth';

// Initialize with credentials
const client = await AuthenticatedSDK.create(
  'your_client_id',
  'your_client_secret'
);

// Or use environment variables
// export NFL_CLIENT_ID=your_client_id
// export NFL_CLIENT_SECRET=your_client_secret
const client = await AuthenticatedSDK.create();

// Use the SDK normally
const games = await client.sdk.schedules.getSchedules({
  season: 2024,
  week: 1,
});
```

## GitHub Secrets Required

Add these secrets to your GitHub repository:

1. `SPEAKEASY_API_KEY` - Your Speakeasy API key (get from https://app.speakeasyapi.dev/)
2. `SDK_DEPLOY_TOKEN` - GitHub Personal Access Token with `repo` scope for pushing to SDK repositories

## Setting Up SDK Repositories

1. Create empty repositories:
   - `griddy-nfl-python`
   - `griddy-nfl-typescript`

2. After first workflow run, add the custom auth files to each repository

3. The workflow will preserve these files during subsequent regenerations

## Notes

- The workflow preserves `auth.py` and `auth.ts` during SDK regeneration
- Python SDK is configured to use uv-compatible build system (hatchling)
- Token refresh happens automatically when tokens are close to expiration
- Credentials can be passed explicitly or via environment variables
