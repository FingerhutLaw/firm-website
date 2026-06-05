import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Single "pages" collection covering:
//   - homepage.md (uses the hero/portrait fields below)
//   - any new page files the team drops in (bio.md, practice-areas.md,
//     firm-values.md, etc.) — these may use just a few fields plus the body.
//
// All fields are optional and unknown fields are preserved (.passthrough())
// so multiple authors can add new fields without breaking the build.
const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pages' }),
  schema: z
    .object({
      // Generic page fields (use on any page)
      title: z.string().optional(),
      description: z.string().optional(),

      // Homepage hero
      heroHeadline: z.string().optional(),
      heroSubheadline: z.string().optional(),
      heroCTAText: z.string().optional(),
      heroCTAHref: z.string().optional(),

      // Phone (header / hero / footer)
      phone: z.string().optional(),
      phoneHref: z.string().optional(),

      // Homepage portrait / Steven section
      meetStevenName: z.string().optional(),
      meetStevenTitle: z.string().optional(),
      meetStevenTagline: z.string().optional(),
      portraitImage: z.string().optional(),
      portraitAlt: z.string().optional(),
    })
    .passthrough(),
});

export const collections = { pages };
