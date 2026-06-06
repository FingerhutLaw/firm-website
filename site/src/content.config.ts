import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// ---------------------------------------------------------------
// pages collection
// One markdown file per page (homepage.md, content-results-page.md,
// content-practice-areas.md, firm-values.md, etc.).
// All fields optional; .passthrough() so authors can add fields freely.
// ---------------------------------------------------------------
const resultCard = z.object({
  outcome: z.string(),
  date: z.string().optional(),
  caption: z.string(),
  court: z.string().optional(),
  summary: z.string(),
  tags: z.string().optional(),
});

const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pages' }),
  schema: z
    .object({
      // Generic page fields
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

      // Site-wide fee note — canonical lives in homepage.md, pulled everywhere
      feeNote: z.string().optional(),

      // Press strip
      pressLabel: z.string().optional(),
      pressLogos: z.array(z.string()).optional(),

      // Practice areas grid (homepage 6-tile preview)
      practiceAreasLabel: z.string().optional(),
      practiceAreasHeading: z.string().optional(),
      practiceAreasCTA: z.string().optional(),
      practiceAreasCTAHref: z.string().optional(),
      practiceAreas: z
        .array(
          z.object({
            name: z.string(),
            tagline: z.string(),
            href: z.string(),
          }),
        )
        .optional(),

      // Results strip (homepage)
      resultsLabel: z.string().optional(),
      resultsHeading: z.string().optional(),
      resultsCTA: z.string().optional(),
      resultsCTAHref: z.string().optional(),
      results: z
        .array(
          z.object({
            figure: z.string(),
            description: z.string(),
          }),
        )
        .optional(),

      // Homepage portrait / Steven section
      meetStevenName: z.string().optional(),
      meetStevenTitle: z.string().optional(),
      meetStevenTagline: z.string().optional(),
      portraitImage: z.string().optional(),
      portraitAlt: z.string().optional(),

      // In the news (homepage)
      newsLabel: z.string().optional(),
      newsHeading: z.string().optional(),
      newsCTA: z.string().optional(),
      newsCTAHref: z.string().optional(),
      news: z
        .array(
          z.object({
            publication: z.string(),
            date: z.string().optional(),
            headline: z.string(),
            excerpt: z.string(),
            href: z.string(),
          }),
        )
        .optional(),

      // Final CTA (homepage)
      finalCtaHeading: z.string().optional(),
      finalCtaBody: z.string().optional(),
      finalCtaButton: z.string().optional(),
      finalCtaHref: z.string().optional(),

      // Results page
      resultsHeroLabel: z.string().optional(),
      resultsHeroHeadline: z.string().optional(),
      resultsHeroSubheadline: z.string().optional(),
      resultsIntro: z.string().optional(),
      resultsDisclaimer: z.string().optional(),
      verdictsSectionLabel: z.string().optional(),
      verdicts: z.array(resultCard).optional(),
      trialSettlementsSectionLabel: z.string().optional(),
      trialSettlements: z.array(resultCard).optional(),
      motionsSectionLabel: z.string().optional(),
      motions: z.array(resultCard).optional(),
      discoverySectionLabel: z.string().optional(),
      discoveryDecisions: z.array(resultCard).optional(),
      settlementsSectionLabel: z.string().optional(),
      settlements: z
        .array(
          z.object({
            figure: z.string(),
            description: z.string(),
          }),
        )
        .optional(),
      resultsClosing: z.string().optional(),
      resultsCTAHeading: z.string().optional(),
      resultsCTABody: z.string().optional(),
      resultsCTAButton: z.string().optional(),

      // Practice areas overview page (intro + scenarios + CTA;
      // tile list now comes from the practiceAreas collection)
      practiceHeroLabel: z.string().optional(),
      practiceHeroHeadline: z.string().optional(),
      practiceHeroSubheadline: z.string().optional(),
      practiceIntro: z.string().optional(),
      practiceAreasList: z
        .array(
          z.object({
            name: z.string(),
            tagline: z.string(),
            summary: z.string(),
            href: z.string(),
          }),
        )
        .optional(),
      scenariosHeading: z.string().optional(),
      scenariosIntro: z.string().optional(),
      scenarios: z.array(z.string()).optional(),
      practiceCTAHeading: z.string().optional(),
      practiceCTABody: z.string().optional(),
      practiceCTAButton: z.string().optional(),
      practiceCTAHref: z.string().optional(),

      // About page (/about)
      aboutHeroName: z.string().optional(),
      aboutHeroSubhead: z.string().optional(),
      aboutPortraitImage: z.string().optional(),
      aboutPortraitAlt: z.string().optional(),
      aboutBio: z.array(z.string()).optional(),
      trialRecordHeading: z.string().optional(),
      trialRecordIntro: z.string().optional(),
      trialRecord: z
        .array(
          z.object({
            date: z.string().optional(),
            summary: z.string(),
            caption: z.string().optional(),
            court: z.string().optional(),
          }),
        )
        .optional(),
      pretrialWinsHeading: z.string().optional(),
      pretrialWinsIntro: z.string().optional(),
      pretrialWins: z
        .array(
          z.object({
            date: z.string().optional(),
            summary: z.string(),
            caption: z.string().optional(),
            court: z.string().optional(),
          }),
        )
        .optional(),
      aboutSettlementsHeading: z.string().optional(),
      aboutSettlements: z
        .array(
          z.object({
            figure: z.string(),
            description: z.string(),
          }),
        )
        .optional(),
      aboutPracticeAreasHeading: z.string().optional(),
      aboutPracticeAreasIntro: z.string().optional(),
      aboutPracticeAreasList: z.array(z.string()).optional(),
      aboutPracticeAreasOutro: z.string().optional(),
      commentaryHeading: z.string().optional(),
      commentary: z
        .array(
          z.object({
            date: z.string().optional(),
            outlet: z.string(),
            headline: z.string(),
            author: z.string().optional(),
            summary: z.string(),
            pullQuotes: z.array(z.string()).optional(),
            href: z.string().optional(),
          }),
        )
        .optional(),
      speakingHeading: z.string().optional(),
      speakingEngagements: z
        .array(
          z.object({
            event: z.string(),
            session: z.string().optional(),
            location: z.string().optional(),
            date: z.string().optional(),
            summary: z.string(),
            image: z.string().optional(),
            imageCaption: z.string().optional(),
          }),
        )
        .optional(),
      credentialsHeading: z.string().optional(),
      credentialsEducation: z.array(z.string()).optional(),
      educationFootnote: z.string().optional(),
      credentialsAdmissions: z.array(z.string()).optional(),
      credentialsMemberships: z.array(z.string()).optional(),
      credentialsRecognition: z.array(z.string()).optional(),
      badges: z
        .array(
          z.object({
            image: z.string(),
            alt: z.string(),
          }),
        )
        .optional(),
      aboutCTAHeading: z.string().optional(),
      aboutCTABody: z.string().optional(),
      aboutCTAButton: z.string().optional(),
      aboutCTAHref: z.string().optional(),

      // Contact page (/contact)
      contactHeroLabel: z.string().optional(),
      contactHeroHeadline: z.string().optional(),
      contactHeroSubheadline: z.string().optional(),
      contactIntro: z.string().optional(),

      // Form backend — change formAction to swap providers
      // (Formspree today: https://formspree.io/f/<id>;
      //  custom Astro endpoint later: /api/contact)
      formAction: z.string().optional(),
      formSubject: z.string().optional(),
      formSuccessRedirect: z.string().optional(),
      formSubmitLabel: z.string().optional(),

      whatHappensHeading: z.string().optional(),
      whatHappens: z.array(z.string()).optional(),

      contactSidebarHeading: z.string().optional(),
      contactDisclaimer: z.string().optional(),

      // Press page (/press)
      pressHeroLabel: z.string().optional(),
      pressHeroHeadline: z.string().optional(),
      pressHeroSubheadline: z.string().optional(),
      featuredArticlesHeading: z.string().optional(),
      featuredArticles: z
        .array(
          z.object({
            publication: z.string(),
            date: z.string().optional(),
            headline: z.string(),
            summary: z.string(),
            href: z.string().optional(),
            pullQuote: z.string().optional(),
            pullQuotes: z.array(z.string()).optional(),
          }),
        )
        .optional(),
      pressSpeakingHeading: z.string().optional(),
      pressSpeaking: z
        .array(
          z.object({
            event: z.string(),
            session: z.string().optional(),
            location: z.string().optional(),
            date: z.string().optional(),
            summary: z.string(),
          }),
        )
        .optional(),
      pressInquiriesHeading: z.string().optional(),
      pressInquiriesBody: z.string().optional(),
      pressInquiriesEmail: z.string().optional(),
      pressInquiriesCTAText: z.string().optional(),
      pressInquiriesCTAHref: z.string().optional(),
    })
    .passthrough(),
});

// ---------------------------------------------------------------
// practiceAreas collection
// One markdown file per practice area in src/content/practice-areas/.
// Filename (without .md) is the URL slug: /practice-areas/<slug>.
//
// Vincent's workflow: drop a fully-written article as <slug>.md.
// Frontmatter required; body is the SEO article copy.
// ---------------------------------------------------------------
const practiceAreas = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/practice-areas' }),
  schema: z.object({
    name: z.string(),
    tagline: z.string(),
    intakeSummary: z.string(),
    priority: z.number(),
    featured: z.boolean().optional().default(false),
    statutes: z.array(z.string()).optional(),
    caseCallout: z
      .object({
        figure: z.string(),
        description: z.string(),
      })
      .optional(),
    draft: z.boolean().optional().default(true),
    seoTitle: z.string().optional(),
    seoDescription: z.string().optional(),
  }),
});

export const collections = { pages, practiceAreas };
