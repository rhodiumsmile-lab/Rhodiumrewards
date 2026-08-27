# Rhodium Rewards

Rhodium Rewards is an Android rewards and promotions project for presenting loyalty offers, balances, and redemption experiences under the Rhodium Rewards brand. This repository snapshot currently contains top-level Gradle configuration, exported Android/UI artifacts, and shared brand assets used for documentation and app packaging work.

## Project Overview

The project is organized around a mobile rewards experience where users can:

- browse promotions and featured offers
- track reward-related screens and flows
- package the app with branded launcher and marketing assets

This checkout appears to be a partial snapshot rather than a complete application source tree: Gradle is configured for Android modules such as `:app` and `:baseline-profile`, but those module directories are not present in the repository at the moment.

## Key Features

- **Rewards branding assets** for product marketing and app packaging
- **Android Gradle configuration** using Kotlin DSL
- **Promo banner artwork** for storefront, web, or release collateral
- **Launcher icon asset** for the Rhodium Rewards app identity
- **UI export artifacts** such as XML layouts, screenshots, and logs for inspection

## Tech Stack

Detected tooling and platform details from the repository:

- **Android / Gradle** via `build.gradle.kts` and `settings.gradle.kts`
- **Kotlin-based Android build setup** with the Kotlin Android and Compose plugins configured
- **AndroidX Baseline Profiles**
- **Google Services plugin**
- **KSP and Hilt plugin configuration**
- **Unity Ads-related Android manifest entries** in `AndroidManifest.xml`

## Setup and Installation

### Prerequisites

- JDK 17 or newer
- Android Studio (recommended for Android builds and emulator runs)
- Android SDK configured locally
- Node.js 18+ only if you want to use the lightweight helper scripts in `package.json`

### Clone the repository

```bash
git clone https://github.com/rhodiumsmile-lab/Rhodiumrewards.git
cd Rhodiumrewards
```

### Install optional Node metadata tooling

The root `package.json` is provided for project metadata and convenience scripts. There are currently no npm dependencies to install.

```bash
npm install
```

## Run and Build Instructions

Because the checked-in snapshot does not currently include the Android module directories referenced by Gradle, the commands below describe the intended workflow once the missing modules are available.

### Convenience scripts

```bash
npm start
npm run build
npm run test
npm run lint
```

### Gradle commands

```bash
./gradlew build
./gradlew test
./gradlew lint
```

If the `app/` module is restored in a future checkout, open the project in Android Studio to run it on a device or emulator.

## Project Structure

Current top-level files of note:

```text
.
├── AndroidManifest.xml     # Android manifest fragment with ads/startup configuration
├── build.gradle.kts        # Root Android Gradle plugin configuration
├── settings.gradle.kts     # Declares the Android modules expected by the build
├── promo-banner.svg        # Promotional banner artwork for Rhodium Rewards
├── ic_launcher.png         # Launcher-style PNG icon for branding/app packaging
├── rewardapp_*.xml|png     # Exported UI layouts and screenshots
├── README.md               # Project documentation
└── package.json            # Root metadata and helper scripts
```

## Asset Notes

- **`promo-banner.svg`** is the canonical promotional banner asset in this repository. It is a valid SVG with Rhodium Rewards branding, marketing copy, and a clear call to action.
- **`ic_launcher.png`** is a valid PNG launcher-style icon sized for branding and packaging workflows.
- No malformed duplicate `promo-banner.svg` filename using Windows-style path characters should remain in the repository tree.

## Contribution Guidelines

1. Keep changes focused and repository-specific.
2. Preserve existing file placement conventions unless a stronger project convention is introduced.
3. Validate branding assets after edits:
   - confirm SVG/XML syntax is well formed
   - confirm PNG assets open as valid images
4. For Android build work, prefer Gradle and Android Studio workflows over ad hoc scripts.
5. Document any assumptions when the repository snapshot is missing modules or generated sources.

## License

No standalone license file is currently present in this repository snapshot. Treat the project license as **unspecified** unless repository owners publish one separately.
