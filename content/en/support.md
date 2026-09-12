# PillowBook Help and Support

Last updated: September 13, 2026  
App: PillowBook  
System requirement: iPhone running iOS 18.0 or later

PillowBook is a local ebook reader made by an independent developer. It does not operate a bookstore or sell, download, or distribute book content.

## Contact support

- Support email: **pillowbook2026@gmail.com**
- Suggested subject: `PillowBook Feedback`

In the App, go to Settings > Send Feedback to create an unsent email. The draft includes the App version and build, device model, iOS version, and App interface language. You can see and edit this information before sending, and nothing is sent until you confirm.

Describe what happened, what you expected, and whether it happens consistently. Do not send a complete book, password, payment-card details, identity document, or other unnecessary sensitive information. The Developer will make reasonable efforts to reply but does not promise a fixed response time or compatibility with every device, file, or third-party service.

For information about data handling, read the [PillowBook Privacy Policy](privacy.html).

## Supported files

- TXT: up to 120 MB per file;
- EPUB: up to 400 MB per file;
- PDF, MOBI, AZW/AZW3, and other formats are not supported; and
- EPUB files with digital-rights-management (DRM), encrypted book content, or invalid structure are not supported. Standard EPUB font obfuscation does not necessarily prevent import.

Import only files you have the right to access and use. PillowBook does not bypass DRM or remove protection from Kindle, Apple Books, or another store.

## Importing books

### Import on iPhone

Use PillowBook’s import option to select a TXT or EPUB from the Files app. You can also use the system Share sheet on a supported file in another app and select PillowBook. After a successful import, PillowBook stores the files needed for reading on the device.

### Wi-Fi Transfer

1. Connect the iPhone and your computer or other device to the same trusted private Wi-Fi network.
2. Open Wi-Fi Transfer in PillowBook and keep that screen open.
3. Enter the address displayed on the iPhone into the other device’s browser address bar.
4. Select one TXT or EPUB, enter the four-digit pairing code shown on the iPhone, and transfer it.
5. Confirm that the book appears in the library, then close the transfer screen when finished.

Wi-Fi Transfer sends the file directly between devices on the local network; it does not use a Developer server. The current connection uses ordinary HTTP, not TLS encryption, and the four-digit code cannot prevent interception or repeated attempts on a hostile network. Do not transfer sensitive files on public, hotel, workplace guest, or other untrusted Wi-Fi, and do not share the address or code with anyone else.

If the browser cannot connect, check that:

- both devices are on the same Wi-Fi and the network does not isolate guests;
- Wi-Fi Transfer is still open on the iPhone;
- PillowBook has Local Network permission;
- you entered the complete address in the browser address bar rather than a search box; and
- a VPN, proxy, firewall, or router rule is not blocking device-to-device traffic.

If it still fails, turn Wi-Fi off and on or import through the Files app instead.

## Common import problems

### Garbled or unrecognized TXT text

PillowBook attempts to detect common text encodings but cannot guarantee every legacy or uncommon encoding. Use a trusted text editor to save the original file as UTF-8 plain text, then import it again. Renaming a Word, PDF, or webpage file with a `.txt` extension does not convert it into plain text.

### EPUB does not open

Typical causes include an incomplete download, invalid EPUB structure, encrypted book content, or DRM. Download a complete, DRM-free EPUB again from a lawful source. PillowBook cannot remove DRM applied by a store or publisher.

### The library is full

The free version holds up to five books. Archived books and books in the Vault also count. Delete a book before importing another, or make the one-time Unlimited Library purchase.

## Common reading questions

### Chapters are split wrong

In the reader: Contents → “Redetect” in the top right, and pick a heading pattern that fits.

### How do I turn on vertical reading?

In the reader, top right → Reading Settings → Text Direction. This applies to the current book only.

### Read-aloud is silent or lacks my language

Read-aloud uses the voices built into iOS. In Settings › Accessibility › Spoken Content › Voices, download a voice for your language, then choose it on PillowBook's listening screen.

## Purchases, restoration, and refunds

Apple’s App Store processes all purchases. Apple and your App Store region determine price, taxes, payment, billing, and refunds.

- **Unlimited Library** is a non-consumable, one-time purchase that removes the five-book limit. On a device using the same Apple Account, select Restore Purchase in the App.
- **One Coffee** is an optional, repeatable tip. It unlocks no feature or content. As a consumable, it cannot be restored. The displayed tip count is stored only on the current device and may disappear after reinstalling the App or changing devices.
- **Redeem Code** uses Apple’s Offer Code interface. Apple verifies whether a code is valid and what entitlement it grants.

A transaction shown as pending may be awaiting payment authorization or family approval. Check again later. For billing, duplicate-charge, or refund requests, use Apple’s [Report a Problem](https://reportaproblem.apple.com/) service. The Developer does not receive your complete payment credentials and cannot issue an App Store refund directly.

## Narration and audio cache

PillowBook uses iOS system voices to generate narration on the device. Voice availability, pronunciation, and downloads depend on iOS, the selected language, and installed system voice resources.

Generated audio is stored as a local cache. You can review storage and clear all narration audio under Settings > Storage, and adjust the number of cached chapters per book. Clearing the cache does not delete books or reading progress; audio is generated again when needed.

## Vault, security, and local files

The Vault uses Face ID, Touch ID, or the device passcode to restrict access through PillowBook’s interface. iOS performs authentication; PillowBook does not receive biometric data.

Despite its name, the Vault is not an encrypted storage container: it does not separately encrypt book files. Imported books and generated narration audio are in the App’s Documents directory and may be visible through Files > On My iPhone > PillowBook, Finder file sharing, device migration, or backups to someone who can access the unlocked device. Protect sensitive material with a strong device passcode and secure backup settings.

## Deleting data

- Deleting a book removes its content and the reading position, per-book statistics, bookmarks, and related narration cache managed for that book. The aggregate daily reading-activity log remains until its rolling retention period expires or the App is deleted.
- Settings > Storage > Clear Narration Cache removes only reproducible audio.
- A selected reading background can be replaced or cleared in the background settings.
- To remove all PillowBook data from the current device, choose Delete App in iOS, not only Offload App.
- Manage iCloud or computer backups and files you copied elsewhere separately in those services or locations.

PillowBook has no Developer-operated account or cloud library. The Developer therefore cannot remotely view, recover, or delete books and reading history stored only on your device.

## App Store reviews

You are welcome to share your experience in an App Store review, but do not post an email address, order information, or other personal details publicly. Use the support email above when a particular issue needs investigation.
