

# Music-Player

This is a multi-page music portal built using *HTML, CSS, and JavaScript* that provides an interactive experience to explore artists, albums, and songs. The website supports search, filtering, rating, and dynamic features powered by the iTunes API.

---

## Features & Functionalities

### HTML & CSS Interface
- *Home Page*
  - Showcases top 3 artists, top 3 albums, and top 3 songs.
  - Clickable items redirect to respective artist or album pages.

- *Artists Page*
  - Displays a list of at least 5 favorite artists.
  - Each artist is clickable and redirects to a page listing their albums.

- *Albums Page*
  - Shows at least 5 albums per artist.
  - Each album includes: name, image, song count, and release year.
  - Albums are clickable and redirect to a songs page.

- *Songs Page*
  - Lists at least 5 songs per album.
  - Each song includes: name and duration.

- *About Page*
  - Describes the purpose of the site and introduces the developers.

- *Persistent Navigation Bar*
  - Always visible at the top.
  - Includes links to Home, Artists, About.
  - Highlights the active page.
  
- *Consistent Footer*
  - Visible on every page.
  - Includes custom footer text and a link to the About page.

---

### JavaScript Integration
- *Navbar Hover Effects*
  - Color change on hover over navbar links.

- *Typing Animation*
  - A typing effect implemented using JavaScript.

- *Search Page*
  - Uses the iTunes Search API to display top 10 results for user queries.
  - Each result includes:
    - Track Name
    - Artist Name
    - Album Artwork
    - Audio Preview (if available)
  - Filters:
    - Filter by song duration (in minutes).
    - Filter explicit vs. non-explicit content.
    - Combine or clear all filters.

- *Artist Spotlight Page*
  - Highlights a favorite artist with image and description.
  - Includes:
    - Zoom-in/zoom-out image animation.
    - Review system:
      - Users can rate (1-5 stars) and leave feedback.
      - Reviews are stored temporarily and shown in a table.
    - Countdown timer to a future album/song release.

---

## 📌 Note
- No external JS/CSS libraries used.
- Built fully with HTML, CSS, and JavaScript.
- iTunes API is used for real-time music data.
- Review data is not persisted after refresh.

---
