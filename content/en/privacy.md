# PillowBook Privacy Policy

Effective date: September 13, 2026  
Last updated: October 12, 2026  
Version: 1.1

This Privacy Policy applies to the iOS application PillowBook (the “App”) and the public support pages directly associated with the App.

The controller responsible for the App’s processing described in this policy is PillowBook’s independent developer, identified in the Developer or Seller field on the App Store product page (the “Developer”). Contact: **pillowbook2026@gmail.com**.

## 1. Privacy summary

The current version of the App:

- does not require an account or sign-in;
- does not operate a Developer cloud server for uploading or syncing books;
- contains no third-party advertising, behavioral analytics, or cross-app tracking SDKs;
- does not sell personal data or use it for targeted advertising or data brokerage;
- processes books, reading history, bookmarks, underlines and notes, generated speech audio, translations, and reading preferences on the device by default; and
- may cause information to leave the App’s local container only when you choose to contact support, use Apple’s purchase services, or use system features such as device backup.

“Stored on device” does not mean that information can never leave the device. iOS backup, device migration, file sharing, your chosen email service, and Apple’s store services may process information according to your settings and their own privacy policies, as explained below.

## 2. Information processed on your device

The App may process and store the following information locally to provide features you request. The Developer has no server or administrative console through which to access this information remotely.

### 2.1 Books and reading information

- TXT and EPUB files you import, including parsed text, images, chapters, and notes, together with a copy of the original file kept at import;
- file names, book titles, authors, languages, text encodings, covers, and content hashes;
- reading position, time and date of reading, reading-speed statistics, favorites, archive status, bookmarks, and bookmarked excerpts;
- underlines and notes you write (text and images), and unsaved note drafts;
- chapter-detection results, layout, fonts, themes, narration language, and other reading settings; and
- per-book reading statistics kept separately for each device. To tell statistics from different devices apart, the App records in the book’s folder the device identifier that iOS provides to the App (identifierForVendor) and the device-type name (such as “iPhone”).

Content hashes are used only to detect duplicate imports and to repair damaged books, and the device identifier is used only to distinguish this device’s statistics records. Neither is used to identify you, and neither is sent to the Developer by the App.

### 2.2 Images you select from Photos

If you use the iOS photo picker to choose a reading background, a custom cover, or an image for a note, the App receives only the image you expressly select; it does not request access to browse your entire photo library or request camera access. A resized, cropped, and processed copy remains locally until you replace or delete that image, delete the related book, or delete the App.

### 2.3 Speech and on-device intelligence

- The App uses Apple’s system speech-synthesis features to generate narration audio on the device and stores generated audio as a local cache.
- On systems and devices that support Apple’s on-device language model, smart chapter detection provides the model with a small set of candidate chapter-heading examples. The App does not upload the full book for this feature.
- Translate a Selection uses Apple’s system translation framework to translate on the device. The App does not send the text you select to the Developer or any other third party. The first time you translate a language, iOS may need to download that language’s translation resources from Apple.
- The App does not record your voice.

Downloads of Apple system components, voice resources, or translation resources may be handled by Apple according to your device settings and Apple’s policies.

### 2.4 Device authentication

The “Vault” uses iOS device-owner authentication. Face ID, Touch ID, or device-passcode verification is performed by the operating system. The App receives only a success, cancellation, or failure result; it does not receive or store your face image, fingerprint, passcode, or biometric template.

### 2.5 Purchase status

The App locally stores whether the library limit has been unlocked, the number of tips recorded on that device, and a limited set of transaction identifiers used to avoid counting the same tip twice. StoreKit verifies entitlement and transaction authenticity. The App does not create a purchase profile on a Developer server.

### 2.6 Home Screen widgets

So that its Home Screen widgets can show content, the App writes the following to a shared container (App Group) that only the App and its widgets can access: the title, current chapter name, reading progress, and cover image of up to three recently read books, plus today’s reading time, daily goal, reading streak, and appearance settings. This information stays on the device and is not sent to the Developer.

Books in the “Vault” and archived books are not written there and do not appear in widgets. Widgets are shown on your Home Screen, so anyone who can see your device’s screen can also see those titles and covers. You can remove a widget at any time if you do not want them shown.

## 3. Information that may leave your device

### 3.1 Support email you choose to send

If you select Feedback in the App and affirmatively send an email, the Developer may receive:

- your sending email address and the name shown by your email account;
- the message and any attachment you choose to include; and
- App version and build, device model, iOS version, and interface language that the App pre-fills and that you can see and edit before sending.

This information is used only to respond to your request, diagnose the reported problem, maintain security, improve functionality directly related to the request, comply with law, or handle a dispute. Sending a support email does not add you to a marketing list. The Developer will not ask you to send a complete book, password, payment-card information, or unnecessary sensitive information.

Your message passes through your chosen email provider and is delivered to a Developer mailbox provided by Google Gmail. Those providers process email and transmission data under their own policies. Unless specifically needed to investigate an issue, do not send book contents, identity documents, financial or health information, or other sensitive material.

### 3.2 Apple App Store and in-app purchases

Apple processes purchases of the non-consumable library-limit unlock, repeatable coffee tips, Apple Offer Code redemptions, purchase restoration, and App Store ratings. The App may receive verified product, transaction, entitlement, or revocation status, and the Developer may receive sales and financial reports that Apple makes available through App Store Connect.

The Developer does not receive your payment-card number, Apple Account password, or complete payment credentials. Apple is responsible for its own processing. See [Apple’s Privacy Policy](https://www.apple.com/legal/privacy/).

### 3.3 Wi-Fi Transfer

The App starts a temporary local-network web service only when you open the Wi-Fi Transfer screen. A browser transfers a file directly to the iPhone without using a Developer server. The App does not retain the other device’s IP address or create a transfer log. A successfully imported book remains locally as described in this policy.

Wi-Fi Transfer currently uses local HTTP rather than a TLS-encrypted connection and uses the four-digit pairing code shown on the iPhone to restrict uploads. The code reduces accidental transfers but is not a defense against a hostile local network. Use this feature only on a private Wi-Fi network you trust, share the address and code only with a device you control, and close the transfer screen when finished. Public or guest networks, including networks that monitor or isolate clients, are not appropriate for sensitive books.

### 3.4 Content you choose to share

When you use note share images, cover share images, or other sharing features, the App creates the images and text on the device and then hands them to the iOS share sheet. The content is sent to the app, contact, or location you choose in the share sheet and is handled by that recipient under its own policies; neither the App nor the Developer handles or stores this shared content.

### 3.5 Public privacy and support pages

This policy and the support pages are intended to be published as static webpages that require no sign-in. The hosting provider may automatically process an IP address, request time, requested path, browser or device type, response status, and similar technical logs to deliver the pages, maintain security, and prevent abuse. The Developer does not intentionally add advertising, behavioral analytics, cross-site tracking, or non-essential cookies to these pages. Processing that the host determines for its own purposes is governed by the terms shown for the hosting domain. When selecting or changing the host, the Developer will verify the actual configuration and add provider, retention, and international-transfer details where applicable law requires them.

## 4. Files, backups, and device migration

The App has no Developer-operated cloud-sync feature. Books (including the original files kept at import), underlines and notes, note images, custom covers, and generated narration audio are stored in the App’s Documents directory and may be visible in the Files app, Finder file sharing, or device migration to a person who can access your unlocked device.

Depending on your iOS, iCloud, and device-backup settings, Apple may include local App data in iCloud Backup or a computer backup and restore that data during migration or recovery; the reproducible narration-audio cache is excluded from backups. These backups are controlled by you and Apple; they are not a Developer-operated sync service. Deleting the App normally removes its current on-device container. Offloading the App may retain its data, and copies already present in a backup or another location may remain.

## 5. Purposes and legal bases

Where applicable law requires a legal basis, the Developer relies on:

- **Performance of a service you request or steps taken at your request** to import, display, narrate, and manage books on your device, process purchase entitlements, and answer support requests;
- **Legitimate interests** in maintaining the App’s security and reliability, diagnosing reported problems, avoiding duplicate transaction handling, and protecting legal rights, but only where those interests are not overridden by your rights and freedoms;
- **Legal obligations** to comply with binding law, tax or accounting duties, and lawful requests from competent authorities; and
- **Consent** only where applicable law requires it and the App expressly requests it. Withdrawal does not affect processing that was lawful before withdrawal.

The App does not use personal data to make solely automated decisions that produce legal or similarly significant effects, and it does not create advertising profiles.

## 6. Disclosure, sale, and tracking

The Developer does not sell personal data, “share” it for cross-context behavioral advertising, exchange it with data brokers, or track your activity across other companies’ apps or websites.

Information may be processed or disclosed only in these limited circumstances:

- Apple provides purchases, Offer Codes, App Store ratings, system backup, downloads of system voice and translation resources, and related platform services;
- the app, contact, or service you choose in the system share sheet receives content you elect to share;
- your chosen email provider and Google Gmail transmit and store a support message you elect to send;
- the hosting provider for the public privacy and support pages delivers the static pages, maintains security, and stores necessary technical logs;
- disclosure is necessary and proportionate to comply with binding legal process or to protect the safety and lawful rights of users, the Developer, or others; or
- if ownership of the App changes, records actually held by the Developer (principally, potentially, support correspondence) may be transferred where lawful, with appropriate notice and a requirement that the recipient continue to protect them.

The current App contains no third-party advertising or analytics SDK. Before releasing a feature that materially changes processing — such as accounts, cloud sync, analytics, crash reporting, advertising, online AI, or another backend — the Developer will update this policy, the App Store privacy disclosures, and any required consent flow.

## 7. Retention and deletion

- Books, original files, bookmarks, underlines and notes, note images, custom covers, reading position, per-book reading statistics, and preferences normally remain until you delete the relevant content, book, or setting, or delete the App. Deleting a book also deletes all of the above that relates to that book, together with that book’s note draft.
- The local daily reading-activity log rolls forward and retains approximately one year.
- Shared data used by Home Screen widgets is rewritten from the current library at each refresh; books that are deleted, archived, or moved to the Vault are removed from it. It is deleted when you delete the App.
- Generated narration is a reproducible cache. The App removes it according to cache settings, and you can clear it for one book or all books. Deleting a book also removes its associated narration cache.
- A selected background image remains until you replace or clear it, or delete the App.
- Local purchase markers remain until App or system data is removed. Apple retains its own transaction records under Apple’s policies.
- Support correspondence is ordinarily deleted or de-identified no later than 24 months after the last substantive communication. It may be retained longer where reasonably necessary for legal, accounting, security-investigation, fraud-prevention, or dispute purposes.
- Technical logs for the public pages are retained according to the host’s and Developer’s actual security configuration and are used only as long as needed to deliver the pages, prevent abuse, or meet legal duties. The production configuration will be checked and a more specific period published where required by law.

You can delete individual books, bookmarks, underlines, notes, a selected background, and narration caches within the App. To remove all local App data from the device, use Delete App in iOS rather than only Offload App, and manage iCloud or computer backups as appropriate.

To ask about or request deletion of support correspondence actually held by the Developer, email **pillowbook2026@gmail.com** and provide enough information to locate the correspondence. Because the Developer cannot access your device, the Developer cannot remotely view, export, or delete books and reading information stored only on that device.

## 8. Security measures and important limitations

The App relies on controls such as the iOS sandbox, App Group permissions, system file protection, and system authentication, and is designed to minimize information leaving the device. The Developer also applies access and retention limits proportionate to the risk of support correspondence received.

No storage or transmission method can be guaranteed completely secure. In particular:

- Wi-Fi Transfer uses unencrypted local HTTP; see Section 3.3 for safe-use conditions.
- The “Vault” restricts access through the App’s interface (books in it also do not appear in Home Screen widgets). Despite its name, it does not separately encrypt book files and is not a substitute for a device passcode, system file protection, or secure backups.
- A person able to unlock your device or access Files, Finder file sharing, or backups may be able to reach files in the App’s Documents directory.

If you believe a security or privacy incident involving the App has occurred, contact the Developer promptly, but do not attach sensitive files to your first message.

## 9. Your privacy rights

Subject to applicable law, you may have rights to request information, access, correction, deletion, restriction, objection, or portability regarding personal data held by the Developer; to withdraw consent; and to complain to a competent data-protection authority. You will not receive discriminatory treatment for exercising a privacy right. Rights may be limited by reasonable identity verification, the rights of others, legal retention duties, and other statutory exceptions.

For people in the European Economic Area, United Kingdom, or Switzerland, the Developer will honor applicable GDPR or equivalent rights. Support information is generally processed to carry out a request you initiated or under legitimate interests in support and security. You may also complain to the data-protection authority where you live.

For California residents, to the extent the CCPA applies, categories the Developer may have processed in the preceding twelve months are limited to identifiers/contact details, customer-support content, and limited diagnostic information you provide when contacting support. The source is you; purposes are support, security, and legal compliance; recipient categories are email-service providers and legally authorized authorities. The Developer does not sell or share this information for cross-context behavioral advertising and does not use or disclose sensitive personal information to infer characteristics.

For people in Japan, the Developer handles personal information within the stated purposes under the applicable Act on the Protection of Personal Information and accepts inquiries and requests concerning disclosure, correction, cessation of use, or deletion at the contact address below.

To exercise a right, email **pillowbook2026@gmail.com**. The Developer may request information matching the original support correspondence to reasonably verify identity and will respond within the period required by applicable law.

## 10. Children and teens

The App is a general-purpose reading tool. It is not designed to collect children’s personal data and contains no advertising, social network, or public-posting feature. The Developer does not knowingly ask children to provide personal data. A minor who needs support should have a parent or guardian contact the Developer where appropriate and should not send unnecessary sensitive information. If the Developer learns that children’s personal data was received without an appropriate legal basis, reasonable steps will be taken to delete it.

The App does not provide or sell book content. Material a user imports may have varying age suitability and should be managed by the user or the user’s guardian.

## 11. International processing

A support email, or necessary technical information generated when you visit the public privacy and support pages, may be processed by your email provider, Google, the webpage host, and the Developer outside your country or region. Where applicable law requires it, the Developer will use reasonable contractual, organizational, or other safeguards. Processing locations depend on the services you choose and their infrastructure; review the relevant provider notices, including the [Google Privacy Policy](https://policies.google.com/privacy).

## 12. Changes to this policy

The Developer may update this policy to reflect changes in features, law, or operations. The revised policy will show a new “Last updated” date. If a change materially affects user rights or processing, the Developer will provide more prominent notice where reasonably practicable, such as an in-App notice, the support page, or App Store release notes. Because the App has no account system, the Developer generally cannot email every user proactively.

## 13. Contact

For privacy, data-rights, or security questions:

- Controller: PillowBook’s independent developer as identified on the App Store product page
- Email: **pillowbook2026@gmail.com**
- App: PillowBook

Do not attach a complete book, identity document, payment-card information, password, or other unnecessary sensitive material to your first message.
