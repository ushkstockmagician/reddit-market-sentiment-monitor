# Reddit Market Sentiment Monitor

A private, non-commercial, read-only Python application for personal market-sentiment research.

## Purpose

The application retrieves a small number of recent public submissions from selected finance-related subreddits and produces a private local daily market-sentiment summary.

It is not a public product, commercial service, social-media management tool, or data-collection platform.

## Reddit API scope

- OAuth-authenticated Reddit API requests only
- Read-only access only
- No posting, commenting, voting, messaging, reporting, moderation, or account actions
- No private communities, private messages, user-profile harvesting, or moderator data
- One scheduled run per day
- Up to 6 recent public submissions per subreddit per run
- Token caching, rate-limit handling, and exponential backoff
- Only minimum data required for the immediate report: title, permalink, timestamp, score, comment count, and subreddit name
- No resale, publication, redistribution, or third-party sharing of Reddit data
- No use of Reddit data for AI/ML training, fine-tuning, or evaluation
- No credentials, tokens, personal data, or private endpoints are stored in this repository

## Intended subreddits

- r/wallstreetbets
- r/stocks
- r/investing
- r/StockMarket
- r/options

## Technical model

This is a private external local Python script, not a community-facing Devvit application. It runs outside Reddit on a local schedule and is intended only for low-volume, read-only personal research.
