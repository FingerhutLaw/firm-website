// Build-time Google rating lookup.
//
// Runs once per `npm run build` (Netlify rebuilds daily via
// .github/workflows/daily-rebuild.yml). Calls Google Places API (New)
// Place Details, asking ONLY for `rating` and `userRatingCount` via the
// X-Goog-FieldMask header so nothing else is billed.
//
// Env vars (set in Netlify → Site configuration → Environment variables,
// or in a local site/.env that is never committed):
//   GOOGLE_PLACES_API_KEY
//   GOOGLE_PLACE_ID
//
// If either is missing or the call fails, we log a warning and fall back
// to the values below. This never fails the build.

export interface GoogleRating {
  /** Rating formatted with one decimal, e.g. "5.0". */
  rating: string;
  /** Number of Google reviews. */
  count: number;
  /** True when the values came from Google on this build. */
  live: boolean;
}

const FALLBACK = { rating: 5.0, count: 23 };

/** Public Google reviews page for the firm (Google Business Profile). */
export const GOOGLE_REVIEWS_URL = 'https://maps.app.goo.gl/9eoZnsizUBWS5knEA';

function env(name: string): string | undefined {
  const fromVite = (import.meta.env as Record<string, string | undefined>)[name];
  return fromVite || process.env[name] || undefined;
}

function format(rating: number, count: number, live: boolean): GoogleRating {
  return { rating: rating.toFixed(1), count, live };
}

async function fetchRating(): Promise<GoogleRating> {
  const key = env('GOOGLE_PLACES_API_KEY');
  const placeId = env('GOOGLE_PLACE_ID');

  if (!key || !placeId) {
    console.warn(
      '[googleRating] GOOGLE_PLACES_API_KEY or GOOGLE_PLACE_ID not set; using fallback rating.',
    );
    return format(FALLBACK.rating, FALLBACK.count, false);
  }

  try {
    const res = await fetch(
      `https://places.googleapis.com/v1/places/${encodeURIComponent(placeId)}`,
      {
        headers: {
          'X-Goog-Api-Key': key,
          'X-Goog-FieldMask': 'rating,userRatingCount',
        },
        signal: AbortSignal.timeout(10_000),
      },
    );
    if (!res.ok) {
      throw new Error(`HTTP ${res.status}: ${(await res.text()).slice(0, 200)}`);
    }
    const data = (await res.json()) as { rating?: number; userRatingCount?: number };
    if (typeof data.rating !== 'number' || typeof data.userRatingCount !== 'number') {
      throw new Error(`unexpected response: ${JSON.stringify(data).slice(0, 200)}`);
    }
    return format(data.rating, data.userRatingCount, true);
  } catch (err) {
    console.warn(
      `[googleRating] Places API call failed; using fallback rating. ${(err as Error).message}`,
    );
    return format(FALLBACK.rating, FALLBACK.count, false);
  }
}

// Memoized so every page in one build shares a single API call.
let cached: Promise<GoogleRating> | undefined;
export function getGoogleRating(): Promise<GoogleRating> {
  cached ??= fetchRating();
  return cached;
}
