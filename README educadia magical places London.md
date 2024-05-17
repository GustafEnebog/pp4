


























































![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Gustaf Enebog,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **April 26, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!







# Magical Places - London

![amiresponsive-screenshot.png](documentation/amiresponsive-screenshot.png)

View the live site [here](https://magical-places-london-7d2df0d61638.herokuapp.com/).

## Introduction

**Magical Places - London** is site for sharing recommendations on hidden gems - the sometimes under-the-radar places that inspire joy and wonder.

It’s aimed at people that, for example, have a free afternoon and are looking for something inspiring to do; they can quickly look at the map at which interesting places are near, and save a favourites list to remind them of what to see in the future.

### Project Goals

The goals for the site’s functionality were:

- Map view: users can view all ‘places’ on a map on the home page.
- User authentication: users can create an account, sign in and have permissions to edit and delete the comments that they create.
- Commenting: users have the ability to create, read, update and delete (CRUD) comments.
- Favouriting: users can favourite and unfavourite a place, and view a list of their favourite places.
- Create place: users can create a ‘place’ by filling out an autocomplete form powered by the Google Places API.

## Agile Development

### User Stories

A Kanban board in Github projects was used for the Agile development process - see the board [here](https://github.com/users/timgoalen/projects/3).

‘Epics’ were broken down into ‘User Stories’, which were further broken down into ‘Tasks’.

## User Experience (UX) Design

### Wireframes

Low-fidelity wireframes were used to test the design before building the site.

Home page:

![home-page-wireframe.png](documentation/home-page-wireframe.png)

List page:

![list-page-wireframe.png](documentation/list-page-wireframe.png)

Detail page (mobile):

![detail-page-wireframe.png](documentation/detail-page-wireframe.png)

Detail page (tablet):

![detail-page-tablet-wireframe.png](documentation/detail-page-tablet-wireframe.png)

Add a Place page:

![add-place-page-wireframe.png](documentation/add-place-page-wireframe.png)

### Navigation

![navigation-diagram.png](documentation/navigation-diagram.png)

### Data Schema

![data-schema.png](documentation/data-schema.png)

note: a separate 'Favourite' model was created for the purpose of being able to sort the users Favourites chronologically.

### Google Maps JavaScript Flow Diagrams

One of the biggest challenges faced while building this site is the implementation of the Google Places photos. 

The first approach was to save to the database a URL obtained with the `getURL()` method.
That problem in this approach is that these URLs would expire after a few days,  giving a 403 error message when trying to display the photo. 

Google `photo_reference` data is no longer supplied with the JavaScript API, and there are new Google terms and conditions that don’t allow a `photo_reference` to be cached, and instruct the developer get a new link every time, using a `PlaceDetails` request.  

I then had to design a JavaScript system that used the Google `place_id` stored in the database to send a new `PlaceDetails` request every time the page is loaded to get the photos, and dynamically add them to the page.

I used a loading-spinner div (without the spinner) to cover a section of the page as the photos were being fetched.

**Add a Place functionality - *‘place-add-form.js’***

The search field in the Add a Place page uses the Google Autocomplete class and the Place Details service:

![add-place-google-maps-schema.png](documentation/add-place-google-maps-schema.png)

**Home page - *‘script.js’***

The Places objects are sent to the HTML template as a JSON array of objects. JavaScript picks them up and uses the `google_place_id` to send requests to Google Places API for the photos. It then re-attaches each newly fetched photo to the corresponding Place object using the `id` as a reference.

![home-page-google-api-schema.png](documentation/home-page-google-api-schema.png)

### Colour Scheme

![colour-scheme.png](documentation/colour-scheme.png)

The colour scheme was chosen to give an earthy and inviting impression to the user.

Contrast accessibility was checked for with [Eightshapes Contrast Grid](https://contrast-grid.eightshapes.com/) and some of the originally chosen colours were darkened to improve their contrast ratio.

![eight-shapes-contrast-grid.png](documentation/eight-shapes-contrast-grid.png)

('Does Not Pass' combinations are hidden in this example)

### Typography

![font-example.png](documentation/font-example.png)

It was used in the light 300 weight, and the regular 400 weight. It was chosen for its strong personality yet good readability.

### Google Maps Custom Styles

The custom appearance of the map was created with Map Styles in Google Maps Platform on the Google Cloud Console. The colours were chosen from the site’s colour scheme. 

The custom pin appearance was created in the site’s main red (#BF553B), directly in the JavaScript code:

`const customPin = new PinElement({
background: "#BF553B",
scale: 0.9,
borderColor: "#fff",
glyphColor: "#fff",
});`

## Features

### Home page

![home-page-screenshot.png](documentation/home-page-screenshot.png)

The main map page, where users can click on map pins to see an info box with photo and place name:

![map-page-screencapture.gif](documentation/map-page-screencapture.gif)

The ‘Add’ icon is on the bottom right is only shown for logged in users.

The display or either ’Log In’ or ‘Log Out’ icons in the top right reflect the users state.

### Add a Place

Where users can add a place by typing in to a search field that uses the Google Places Autocomplete to suggest existing places. Once the user clicks on a suggested place, the hidden form is automatically filled in by JavaScript, from the data provided by the Google Places API.

![add-place-screencapture.gif](documentation/add-place-screencapture.gif)

notes:

- The ability for a user to edit or delete a Place that they have added wasn't implemented:
    - As the form data is not user-generated, and rather supplied by the Google Places API, there is a low chance or user error that would justify ‘edit’ functionality.
    - If the user had the ability to delete places that were already commented on, other users would lose their comments and lose access to the place if it was in their favourites list.
- A fallback image was added for places that don’t have a corresponding Google image.

### List page

![list-page-screenshot.png](documentation/list-page-screenshot.png)

Places can be favourited/unfavourited by clicking on the heart icon.

The user can sort the list by ‘Newest’, ‘A-Z’ and ‘My Favourites’.

If a user doesn’t have any favourites yet, this message is displayed:

![list-page-no-favourites-dialogue.png](documentation/list-page-no-favourites-dialogue.png)

Sorted by ‘Favourites’:

![list-page-favourites-screenshot.png](documentation/list-page-favourites-screenshot.png)

### Detail page

The detail page is where the user can:

- create, read, update and delete a comment
- favourite/unfavourite a place
- view the place address
- view the number of comments

Desktop layout:

![detail-page-screenshot.png](documentation/detail-page-screenshot.png)

Mobile layout:

![detail-page-mobile-screenshot.png](documentation/detail-page-mobile-screenshot.png)
### Add comment

![add-comment-form-screenshot.png](documentation/add-comment-form-screenshot.png)

### Edit comment

![edit-comment-screenshot.png](documentation/edit-comment-screenshot.png)

### Delete comment

![delete-comment-screenshot.png](documentation/delete-comment-screenshot.png)

### Log In

![log-in-screenshot.png](documentation/log-in-screenshot.png)

### Log Out

![log-out-screenshot.png](documentation/log-out-screenshot.png)

### Sign Up

![sign-up-screenshot.png](documentation/sign-up-screenshot.png)

### 404 Page

![404-page-screenshot.png](documentation/404-page-screenshot.png)

### 500 Page

![500-page-screenshot.png](documentation/500-page-screenshot.png)

## Features to Implement in the Future

- Pagination: add pagination to the list page and detail page comments.
- Geolocation: add ‘locate user on the map’ functionality.
- New list-page sort option: sort by most commented place.
- Password reset: add ability to reset password.
- Social sign-in: allow users to sign in with their Google/Apples/etc. accounts.
- Google Places API (new): update to the new version of the API.
- Google ‘place_ids’ can, in theory, expire; a system would be needed for if this happens.
- User’s created places: allow users to view a list or map of all the places they have created.
- User profiles: a user page with a list of places created and comments left, either private to the user or publicly accessible.
- Jest testing: create a suite of JavaScript test using JEST.

In general, the code could easily be repurposed to create similar sites with a different focus in the places being shared (e.g. cycling-cafes/kids activities/rock-climbing centres etc.).

## Technologies Used

- Languages:
    - Python
    - JavaScript
    - HTML5
    - CSS3
- Framework:
    - Django
- Database:
    - PostgreSQL
- [Visual Studio Code](https://code.visualstudio.com/) - as the code editor.
- [Git](https://git-scm.com/) - for version control, using the Gitpod IDE.
- [GitHub](https://github.com/) - for storing the project.
- [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL as a service.
- [Heroku](https://www.heroku.com/) - to deploy the application.
- [Cloudinary](https://cloudinary.com/) - to host the static files.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - to test responsiveness, edit CSS code, debug JavaScript and generate Lighthouse reports.
- [Google Fonts](https://fonts.google.com/) - to import the site font, ‘Oswald’.
- [Figma](http://figma.com) - to create the wireframes.
- [Font Awesome](https://fontawesome.com/) - for all the site icons.
- [Gauger Fonticon](https://gauger.io/fonticon/) - for the favicon.
- [Coolers](https://coolers.co/) - for an overview of the chosen colour palette.
- [Am I Responsive](https://ui.dev/amiresponsive) - to create the responsive demo image at the top of the Readme.
- [Excalidraw](https://excalidraw.com/) - to create the navigation diagram.
- [Lucidchart](https://www.lucidchart.com/pages/) - to create the database schemas.
- [TinyPNG](https://tinypng.com/) - to compress the Readme images.
- [Quicktime](https://support.apple.com/en-gb/guide/quicktime-player/welcome/mac) - to record the screen capture for GIFs in the readme.
- [Ezgif](https://ezgif.com/) - to convert the Readme GIFs.
- [Quillbot](https://quillbot.com/) - for rephrasing demo comments.
- [WebAIM WAVE](https://wave.webaim.org/) - for automated testing of accessibility.
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) - to check colour contrast accessibility.
- [Eightshapes Contrast Grid](https://contrast-grid.eightshapes.com/) - to visualise the contrast accessibility of the whole site colour palette.
- [Code Institute’s Python Linter](https://pep8ci.herokuapp.com/) - for automated testing of the Python code.
- [JSHint](https://jshint.com/) - to test the JavaScript code.
- [W3C Markup Validator](https://validator.w3.org/) - to test the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator) - to test the CSS code.

### APIs Used

- [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/overview) - to run the home page map.
- [Google Places API](https://developers.google.com/maps/documentation/places/web-service/overview) - to get details and photos from place searches.

### Python Packages Used

- [django-allauth](https://docs.allauth.org/en/latest/index.html) - for user authentication.
- [gunicorn](https://gunicorn.org/) - as the HTTP server that allows Django to run on Heroku.
- [psycopg2](https://pypi.org/project/psycopg2/) - as the PostgreSQL database adapter for Python.
- [dj_database_url](https://pypi.org/project/dj-database-url/) - to allow the use of the `DATABASE_URL` environment variable inside Django.
- [Coverage.py](http://Coverage.py) - to measure test coverage of the Python code.

## Testing

### Automated Testing

**Python Unit Tests**

Extensive unit tests were written for the Python code in Django, achieving a 94% coverage.

![coverage-results.png](documentation/coverage-results.png)

**Python Linting**

Python linting was carried out with https://pep8ci.herokuapp.com/.

There were no warnings left in the production code apart from the ‘line too long’ errors on the boilerplate Django code in ‘settings.py’.

**JavaScript Linting**

All JavaScript files were tested with [JSHint](https://jshint.com/). There were no warnings left in the production code apart from the ones detailed below -

script.js:

- The ‘google’ and  ‘Places’ variables are defined in a separate script in the HTML template.

![script-js-jshint-results.png](documentation/script-js-jshint-results.png)

list-view.js:

- The ’USER_SORT_SELECTION’ and ‘google’ variables are defined in a separate script in the HTML template.

![list-view-js-jshint-results.png](documentation/list-view-js-jshint-results.png)

place-detail.js:

- The ’GOOGLE_PLACE_ID’ and ‘google’ variables are defined in a separate script in the HTML template.

![place-detail-js-jshint-results.png](documentation/place-detail-js-jshint-results.png)

place-add-form.js:

- The ‘google’ variable are defined in a separate script in the HTML template.

![place-add-form-js-jshint-results.png](documentation/place-add-form-js-jshint-results.png)

**JavaScript Chrome Dev Tools Console:**

All pages with JavaScript files were tested for errors with the Dev Tools console. Only one remains.

Warning on home page - 

This code suggested didn’t work in our context, so was left as is.

![homepage-devtools-warning.png](documentation/homepage-devtools-warning.png)

A previous console warning - `Loading the Google Maps JavaScript API without a callback is not supported` - for the JavaScript in ‘place-add.html’ was fixed with the help of this Stack Overflow [post](https://stackoverflow.com/questions/75179573/how-to-fix-loading-the-google-maps-javascript-api-without-a-callback-is-not-supp), which suggested the code: `callback=Function.prototype`

**CSS Validation**

The CSS file was validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator). No errors are present in the production code.

**HTML Validation**

All pages were validated by the [W3C Markup Validator](https://validator.w3.org/). No errors are in the production code.

To overcome the errors that the Django tags would bring up, the pages were tested by selecting ‘View Page Source’ in Chrome and copying the rendered HTML into the validator.

**Lighthouse Testing**

All pages were tested with Google Chrome’s Lighthouse.

Home Page (desktop):

![lighthouse-homepage-desktop.png](documentation/lighthouse-homepage-desktop.png)

Home Page (mobile):

![lighthouse-homepage-mobile.png](documentation/lighthouse-homepage-mobile.png)

List Page (desktop):

![lighthouse-listpage-desktop.png](documentation/lighthouse-listpage-desktop.png)

List Page (mobile):

![lighthouse-listpage-mobile.png](documentation/lighthouse-listpage-mobile.png)

Detail Page (desktop):

![lighthouse-detailpage-desktop.png](documentation/lighthouse-detailpage-desktop.png)

Detail Page (mobile):

![lighthouse-detailpage-mobile.png](documentation/lighthouse-detailpage-mobile.png)

Add a Place Page (desktop):

![lighthouse-addplace-desktop.png](documentation/lighthouse-addplace-desktop.png)

Add a Place Page (mobile):

![lighthouse--addplace-mobile.png](documentation/lighthouse-addplace-mobile.png)

**WebAIM WAVE Accessibility Testing**

All pages were tested with the [WAVE tool](https://wave.webaim.org/).

A single ‘redundant link’ error was left in the place-detail.html: if is a user is signed out, they are given a link to log in to leave a comment, which has a duplicate path to the ‘Log In’ link in the header.

Early testing with the WAVE tool flagged up insufficient contrast in some of the colours, which were then changed to meet the guidelines.

### User Stories Testing

All user stories were tested to confirm that they meet their Acceptance Criteria. The following have all PASSED.

(View the EPICS, User Stories, Acceptance Criteria and Tasks on the GitHub [Kanban Board](https://github.com/users/timgoalen/projects/3)).

---

EPIC: USER ACCOUNT

---

As a **user** I can **sign up and log in** to the site to **leave comments and add places**.

- Acceptance Criteria - PASSED:
    - Users can create an account with a Sign Up page
    - Users can log in with a Log In page
    - Users can log out with a Log Out Page

---

EPIC: NAVIGATION

---

As a **user** I can **view all places on a map** to easily **see which places are nearby**.

- Acceptance Criteria - PASSED:
    - Map page
    - Saved places to show up as pins on the map
    - Saved places to have photo and title in map popup info box

---

As a **user** I can **view a list of the places** to see **titles**, **pictures** and how many **comments** have been left.

- Acceptance Criteria - PASSED:
    - List view page
    - Photo is displayed
    - Title is displayed
    - Comment count is displayed

---

As a **user** I can **sort the list of places by date**, to **see which places have been recently created**.

- Acceptance Criteria - PASSED:
    - User can sort place list by date (newest first)
    - Sort-by-date is the default option

---

As a **user** I can **sort the list of places alphabetically**, to easily **find a place by its name**.

- Acceptance Criteria - PASSED:
    - User can sort the place list alphabetically (A-Z)

---

EPIC: COMMENTS

---

As a **user** I can **leave a comment on a place**, to **share my experience with other users**.

- Acceptance Criteria - PASSED:
    - Once signed in, a user can leave a comment on a place.
    - User receives successful feedback message
    - Comment form is in the detail view

---

As a **user** I can **read my and other people's comments**, to be **inspired to visit a place**.

- Acceptance Criteria - PASSED:
    - Comments are displayed in the detail page
    - Comment form submission redirects to detail page, so it can be read

---

As a **user** I can **edit my comments**, to **correct or add information**.

- Acceptance Criteria - PASSED:
    - User can edit their own comments (not others)

---

As a **user** I can **delete my comments**, to allow me to **change my mind**.

- Acceptance Criteria - PASSED:
    - User can delete ONLY their own comments

---

EPIC: FAVOURITES

---

As a **user** I can **favourite and unfavourite a place**, to **keep a record of places to visit in the future**.

- Acceptance Criteria - PASSED:
    - User can click an icon to toggle the 'favourite' status of a place.
    - 'Favourite' status is shown in the icon display.

---

As a **user** I can **view a list of my favourite places**, to easily **see which places I plan to visit**.

- Acceptance Criteria - PASSED:
    - User can select 'Favourites' in the list page to view all of their favourites

---

EPIC: ADD A PLACE

---

As a **user** I can easily **add a place** by typing its name, to **share my recommendation with other users**.

- Acceptance Criteria - PASSED:
    - Search bar with autocomplete
    - Selected place is shown with name, address and photo
    - User has the option to Save or Cancel

---

EPIC: ADMIN

---

As a site **developer** I can **view a list of all data: places, comments and favourites**, so I can **moderate content**.

- Acceptance Criteria - PASSED:
    - Django admin panel with Places, Comments and Favourites

---

As a **developer** I can **create, read, update and delete (CRUD) places**, to **create the initial content for the site, and moderate the Places added by users**.

- Acceptance Criteria - PASSED:
    - Places can be updated & deleted in Django Admin panel

---

EPIC: TESTING

---

As a **developer** I can **create a suite of tests**, to easily **be able to find out if site updates create issues in the codebase**.

- Acceptance Criteria - PASSED:
    - Django unit tests with 90%+ coverage

---

EPIC: DEPLOYMENT

---

As a **developer** I can **deploy to a hosting service**, so that **the site is available to the public**.

- Acceptance Criteria - PASSED:
    - Functioning deployment to Heroku

---

### Manual Testing

The following devices and browsers were used for manual & responsive UI testing.

- iPhone SE (2020)
    - Safari (v16)
    - Chrome (v114)
- iPad (6th Generation)
    - Chrome (v111)
    - Safari (v15)
- Mac Pro (Mid 2012)
    - Chrome (v116)
    - Firefox (v115)
- Dell Chromebook 3120
    - Chrome (v103)

## Bugs

### Fixed Bugs

| Bug | Fix |
| --- | --- |
| ‘Add a Place’ error bug: if a user tried to add a duplicate place they would receive an error in the form and an error modal. | Using the CSS shown below to hide any form validation messages, and just have the main modal message. |

```css
/* To hide the form error list (validation is done in the View) */
#place-add-form ul {
    display: none;
}
```

### Unfixed Bugs

| Bug |
| --- |
| ‘Add a Place’ page: even though the input fields are hidden from user, they could potentially open developer tools and manually modify the form entries, leading to incorrect data. being submitted. |
| The comments are displayed at the moment without showing any paragraph breaks that can be seen inside the Django admin panel. |

## Deployment

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/timgoalen/command-line-coffee)
2. At the top right of the Repository, just below the GitHub navbar, click on the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/timgoalen/command-line-coffee)
2. Above the list of files, click "Code".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

```

1. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.

```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

1. For changes you've made to reflect on the live site*:
    - Type `git add <files changed>`
    - Type `git commit -m <description of change>`
    - Type `git push`
    - In Heroku, after pushing to Github - if 'automatic deploys' aren't enabled, manually deploy by clicking 'Deploy Branch' in the Manual Deploy section.

### Set up the Google Maps API

Follow the steps outlined in the Google [documentation](https://developers.google.com/maps/get-started), to:

- Create a Google Cloud account
- Create a project
- Get a Google Maps API key
- Enable the Maps API and Places API

### Cloudinary

1. Create a [Cloudinary](http://cloudinary.com) account, to host the static files.
2. Copy your ‘API Environment variable’**.**

### ElephantSQL

1. Create an [ElephantSQL](https://www.elephantsql.com/) account.
2. Create a new instance.
3. Copy the database URL.

You will also need to add the database to your Django [settings.py](http://seetings.py) file:

`DATABASES = {`

`'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))`

`}`

### Deploy to Heroku

1. Create a [Heroku](https://www.heroku.com/) account.
2. In the dashboard, click on ‘Create new app’ from the ‘New’ dropdown menu in the top right.
3. Name the app and choose a region.
4. In the ‘Settings’ tab, click on 'Reveal Config Vars’.
5. Enter the details for these Variables [you will also need these variables in your ‘env.py’ file for local use]:
    1. CLOUDINARY_URL
    2. DATABASE_URL (from ElephantSQL)
    3. GOOGLE_MAPS_API_KEY
    4. SECRET_KEY (from Django)
6. In the 'Buildpacks' section click 'Add buildpack'.
7. Select ‘Python’, and click 'save changes'.
8. In the 'Deploy' tab, select GitHub as the deployment method, and click 'Connect to GitHub'.
9. In the 'App Connected to GitHub' section, search for the GitHub repository name, select it then click 'connect'.
10. Finally, either click ‘Enable Automatic Deploys’, or ‘Deploy Branch’ in the ‘Manual deploy’ section.

## Credits

### Content

The original idea for this site was inspired by a [mumsnet thread](https://www.mumsnet.com/talk/_chat/4775974-most-magical-places-in-london-feeling-so-depressed-to-be-back-help-me-find-some-joy-and-wonder?page=1) asking for recommendations of things to do in London. Some of the demo comments were rephrased from this thread.

All photos come from the Google Places API.

### Code

The following docs and tutorials were consulted.

************Django************

General Django tutorials:

- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)
- [Django for Beginners](https://djangoforbeginners.com/) [book]

Django ‘favouriting’ functionality:

- [Codemy - Create Blog Like Button](https://www.youtube.com/watch?app=desktop&v=PXqRPqDjDgc)

Django messages:

- [Ordinary Coders](https://ordinarycoders.com/blog/article/django-messages-framework)
- [Simple Is Better Than Complex](https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html)

Getting data from a Django model into javascript:

- [Bugbytes](https://www.youtube.com/watch?v=h39eMGWmEV4&t=36s)
- [Official Django docs](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#json-script)
- [adamj.eu](https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/)

**Google Maps API/JavaScript**

(Official Google)

- [Adding a map](https://developers.google.com/maps/documentation/javascript/adding-a-google-map#maps_add_map-javascript)
- [Adding markers](https://developers.google.com/maps/documentation/javascript/advanced-markers/accessible-markers)
- [Places Autocomplete](https://developers.google.com/maps/documentation/javascript/examples/places-autocomplete)
- [Retrieving response data](https://developers.google.com/maps/documentation/javascript/place-autocomplete)
- [Adding multiple markers](https://jsfiddle.net/gh/get/library/pure/googlemaps/js-samples/tree/master/dist/samples/advanced-markers-accessibility/jsfiddle)
- [Places photos](https://developers.google.com/maps/documentation/javascript/places#places_photos)

(3rd Party)

- W3 Schools - [Google Maps Intro](https://www.w3schools.com/graphics/google_maps_intro.asp)
- WittCode - [Google Maps JavaScript tutorial](https://www.youtube.com/watch?v=tmdtH1hwlDo)
- Stack Overflow - [close info window when user clicks anywhere on the map](https://stackoverflow.com/questions/10022873/closing-info-windows-in-google-maps-by-clicking-the-map)

### Acknowledgements

- My mentor Brian Macharia for his invaluable guidance.










































# Educadia: Full-Stack Development Milestone Project


This is my final project at the Code Institute Full-Stack Web Developer course. The purpose of the project is to demonstrate my practical skilled that I gined in Django framework and and back-end development. The idea of the project is to serve an actual local school in my home country. Giving them a way to facilitate remote learning in the COVID times.

## Table of contents

* [Live](#Live)
* [User stories](#user-stories)
* [UX](#ux)
  * [Strategy plane](#strategy-plane)
  * [Scope plane](#scope-plane)
  * [Structure plane](#structure-plane)
  * [Skeleton plane](#skeleton-plane)
  * [Surface plane](#surface-plane)
* [Wireframes](#wireframes)
* [Features](#features)
* [Future implementations](#future-implementations)
* [Technologies](#technologies)
* [Challenges](#Challenges)
* [Deployment](#Deployment)
* [Testing](#Testing)
* [Credits](#credits)

## Live

The live educadia project is hosted on Heroku. you can access it [here](https://educadia-test.herokuapp.com/).

The following accounts are available for testing:

* teacher1 (for a teacher user type)
* student1 (for a student user type)


The password is learnonline for both accounts.

## User stories

The following user stories were considered:

* As a user, I want to register an account, so I can log in to the website.
* As a user, I want to reset my password if I forget it, so I can log in to the account.
  * Acceptance criteria: build a an authentication system based on the Django's allauth system

* As a user, I want to be able to add my full name, bio, and picture and edit them if I want to change any.
  * Acceptance criteria: build a user account model with add and edit functionality.

* As a teacher, I want to add/edit/delete classes.
  * Acceptance criteria: build class model and give CRUD access to teachers

* As a teacher, I want to add/edit/delete materials.
  * Acceptance criteria: build materials model and give CRUD access to teachers

* As a student, I want to view available classes to join.
  * Acceptance criteria: build a join class functionality

* As a student, I want to view class materials available in the classes I joined.
  * Acceptance criteria: have an access restriction to view each class materials for students

## UX

### Strategy plane

> What am I aiming to achieve in the first place, and for whom?

The project is for the teachers and the students. It includes one main functionality, everything else is to facilitate that functionality

The funtionality of the project is to give teachers a place online to share class materials with students, and to give the students organized views to access these materials. This function would serve 2 purposes; One, to have one place where all teachers add their classes and materials and for students to access them. Two, to have that virtual space go byond the physical space limitations allowing students from anywhere to join the class of a teacher they are interested in.
 

The initial registration for all users would make the user type a student, for a teacher to be registered a manual tracking from the admin would change the user type for that particular user to a teacher. This will prevent teachers outside of the school to register for this site.

### Scope plane

> What features do I want to include in my design?

The following features were for teachers:

* to be able to edit/update user details.
* to be able to add classes, where teacher can set a customized join code to share with any potential student.
* to be able to edit/delete classes.
* to be able to add/edit/delete materials from classes.

For students:

* to be able to edit/update user details.
* to join classes which I have the join code from the teacher.
* to be able to view and download class materials for the joined classes.


### Structure plane

> How is the information structured?

The landing page lists all the available classes, with teachers name on the top for ease to spot if looking for a particular teacher (if he/she exists on this site). if logged in, there will a join class button on each class. the point of that button is to inform the student of how to join a class, that he first needs to have the join code from the teacher of that class. When logged in (for both teachers and students), the user will be able to access classes and materials associated with that user in the database.

The structure of the database as follows:

* The User model is a built-in Django model coming from allauth.

* The UserAccount model for myaccount application, includes basic info about user:
  * user = OneToOneField(...) with the allauth model
  * first_names = CharField(...)
  * last_name = CharField(...)
  * user_type = CharField(...) auto set to student unless changed by the admin
  * bio = CharField(...)
  * image = ImageField(...)

* The AllClasses model for myclasses application, includes the details about a class:
  * added_by = ForeignKey(...) with the UserAccount model
  * class_name = CharField(...)
  * class_join_code = CharField(...)
  * class_subject = CharField(...)
  * class_university = CharField(...)
  * class_collage = CharField(...)
  * class_department = CharField(...)
  * class_level = CharField(...)
  * class_division = CharField(...)
  * class_year = CharField(...)

* The AllMaterials model for myclasses application, includes details about a material:
  * added_by = ForeignKey(...) with the UserAccount model
  * for_class = ForeignKey(...) with the AllClasses moddel
  * name = CharField(...)
  * doc = FileField(...)
  * link = CharField(...)
  * desc = CharField(...)

* The ClassRegister model for myclasses application, serves as a general register for classes:
  * student_name = ForeignKey(...) with the UserAccount model
  * registered_for = ForeignKey(...) with the AllClasses moddel
  * join_code = CharField(...)

* The Donate model for donate application, to store donation information:
  * name = CharField(...)
  * phone = CharField(...)
  * email = EmailField(...)
  * amount = DecimalField(...)
  * date = DateTimeField(...)

### Skeleton plane

> How is the information implemented, and how will the user navigate through the features?

For the landing page, the navigation bar is self explanatory to guide the user in the right direction. The mobile view has a simple navigation bar that slides down on click. Only the login, the registration, resources view is available when the user is not logged in. The my classes, my account, and logout becomes visible on the navigation bar after the successful authentication. The views are mostly one level so there was no need to include a button to take the user back a step, since clicking on the navigation links will do similar action.

### Surface plane

> What will the product look like?

The mobile-first approach design was implemented on this website to maintain the user experience from mobile devices to desktop computers. Bootstrap was used to achive the responsiveness.

Each page is divided into three sections: the navbar, the actual page that contains the information, and the footer.

The footer is made to be sticky to the bottom, as in it will remains hidden until the user scrolls down to the bottom of the page. If the contents of the page is short, the footer remains in the bottom of the page. it displays the copyright and the donation link where payments can be taken as a donation to the school

The navbar is simple. The colours are light but separated from each other. There is not much typography on the website yet. The default font was used for this reason. There is an slide down form which opens upon user click for both my account and my classes applications, used to keep the page contents organized and to keep the list of existing classes/materials seperated from the forms.

## Wireframes

* The wireframe was created to show an estimated look and feel of the website on mobile, tablet, and pc.

  * You can see the initial look of the pages as below:
    * Classes/home page:
        ![Classes/home](https://user-images.githubusercontent.com/63303440/116648121-30811b00-a974-11eb-8f98-e90566d005b7.png)
    * Login page:
        ![Login](https://user-images.githubusercontent.com/63303440/116648137-3676fc00-a974-11eb-8d2f-63077a79c625.png)
    * Registration page:
        ![Registration](https://user-images.githubusercontent.com/63303440/116648145-3ecf3700-a974-11eb-9464-7e9f958e1f8d.png)
    * Student classes page:
        ![Student](https://user-images.githubusercontent.com/63303440/116648150-4262be00-a974-11eb-896d-11615cbf21ec.png)
    * Teacher classes page:
        ![Teacher](https://user-images.githubusercontent.com/63303440/116648161-455dae80-a974-11eb-8e33-2efccf9e05f9.png)



## Features

There are also a few hidden features in the backend,which is the heart of the project. It gathers all the information for the views and stores all the information that comes from the frontend. It is connected to a free Postgres database hosted by Heroku. The dj-database-url and the psycopg2-binary applications are connecting the database to the backend. The gunicorn application is responsible for running the Django website on the Heroku server. The static files and media content are hosted by the AWS S3 Cloud Storage API. The Stripe application ensures a smooth, secure, and convenient card payment. A short JavaScript code guarantees the real-time connection to [stripe.com](https://stripe.com/ie) for the enhanced user experience and the immediate card data validation.

In addition, because the main users (students in particular) of this project have limited knowledge, the teachers asked to have all verifications to be done by admin to avoid unwaned users. which will be done with the standard django admin panel by the head teacher of the school.

## Future implementations

I am planning to implement the following features in the future:

* to add a second language (Arabic) to the project, Making it easier for the users since it will be in their native language.
* to create webhooks for Stripe to ensure that every payment (donation) is stored in the database and every confirmation email is sent after a successful payment
* to add ability to chat between teachers and students
* to write more code for the backend to strengthen the defensive design
* to add contents for the dashboard and resources in the my account view that is pulled from the database for better UX
* to add ability for students to upload homework and assignemtns if a teacher assigns any.
* to include a new view as a library for small publications by the teachers

## Technologies

### Languages

Required technologies:

* HTML 5
* CSS 3
* JavaScript
* Python
* Django
* Relational database (MySQL or Postgres)
* Stripe payment
* Additional libraries and APIs

Technologies used in the project:

* HTML5
* CSS3
* JavaScript
* Python (3.8)
* Django 3.1
* AWS S3 Storage API

### Libraries and frameworks

* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) framework for developing responsive websites
* [jQuery (3.5.1)](https://jquery.com/) library to use JavaScript easier on the website
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) to handle forms in the project
* [dj-database-url](https://pypi.org/project/dj-database-url/) to use database URL in Django applications
* [Pillow](https://pypi.org/project/Pillow/) for Python Imaging/file Library
* [stripe](https://pypi.org/project/stripe/) to handle secure card payments
* [gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX
* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) Python-PostgreSQL Database Adapter


### Challenges

I faced several challenges during the project, including the tight deadline and dealing with the complexity of django having no prior exposure to anything similar until my enrolment in CI. Few of the most difficult challenges I faced are:

* When I wrote the CRUD functionality for adding the materials, the old files were not deleted when instance is deleted. I looked for a solution a lot and could not find one that I can understand and implement. However, when I expressed this to my mentor he gave me some guidance on a simple way to override the delete functionality to make sure that it also deletes the file.

* allauth, while it offers great ease for the log in system, I found it to be quite comlicated to style, as well as to predict its behaviour. I used dev tools thoroughly and managed to have some styling, but its not the exact way I wanted it to look like. Plus, the model itself is standard, so I initially envisioned my UserAccount model to be part of the basic user model from allauth. But in reality it was too complicated for me to customize the allauth model, which is why I decided to use a secondary user model (UserAccount) to add the fields that suit this project (which is why the user is redirected to profile page right after successful authentication). Lastly, the messages in the allauth was also challenging to place in a toast, this issue I was not able to fix. You can see that when a new user is registered, a message will appear at the ttop of the page (that the confirmation email was sent) instead of it appearing in the toast like the other messages.

* UniqueConstraint for the class register model, because I wanted to prevent joining an already joined class (creating a duplicate instance for the student). I tried to use a unique constraint in the model, however, it proved to be quite complicated. Instead, I created a check in my classes view to perform that function.

* View class details for a student type user. Because the form to join a class will be submitted to class register model, I needed to somehow use the foreign key field with the User Account model to know if that student have already registered for a particular class. The way I was able to soleve that is by relying on the join code field in class register model, so first I created filter to check if the combination of that (student) user with that join code already exists in the database. Then only allow the join functionality if there is no prior registration for this class. This way can be problematic if 2 classes or more have the same join code. 

* Stripe website change. Therefore, I had to rely on code snippets from the CI BA project to move forward with setting up stripe. Plus, in this particular school, the donations will be handeled by the finance department which will have no access to this site. The solution to this was to give the financial department the backend of stripe to handle the payments receipts.

### Deployment

#### Running Code Locally


1. Follow this link to my [Repository on Github](https://github.com/AwsSG/educadia) and open it.

2. Click `Clone or Download`.

3. In the Clone with HTTPs section, click the `copy` icon.

4. In your local IDE open Git Bash.

5. Change the current working directory to where you want the cloned directory to be made.

6. Type `git clone`, and then paste the URL you copied earlier.

7. Press enter and your local clone will be ready.

8. Create and start a new environment:  
`python -m .venv venv`  
`source env/bin/activate`

9. Install the project dependencies:  
pip install -r requirements.txt

10. Create a new file, called `env.py` and add your environment variables:

`import os`  
`os.environ.setdefault("STRIPE_PUBLISHABLE", "secret key here")`\
`os.environ.setdefault("STRIPE_SECRET", "secret key here")`\
`os.environ.setdefault("DATABASE_URL", "secret key here")`\
`os.environ.setdefault("SECRET_KEY", "secret key here")`\
`os.environ.setdefault("AWS_ACCESS_KEY_ID", "secret key here")`\
`os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "secret key here")`

11. Go to `settings.py` file and add your environment variables.

12. Add `env.py` to .gitignore file

13. Go to terminal and run the following: `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

14. Create a superuser: `python3 manage.py createsuperuser`

15. Run it with the following command:  
`python manage.py runserver`

16. Open `localhost:8000` on your browser

17.  Add `/admin` to the end of the url address and login with your superuser account and create new products.

#### Deployment to Heroku

The following steps were taken in order to deploy this site to Heroku:

1. Created a new app in `Heroku` with a unique name, chose my region

2. Went to `Resources`, within Add-ons searched `Heroku Postgres`, chose Hobby Dev - Free version, then clicked `Provision` button.

3. In `Settings` clicked on `Reveal Config Vars` button, and copied the value of `DATABASE_URL`

4. Returned to terminal window and run `sudo pip3 install dj_database_url`

5. Also run `sudo pip3 install psycopg2`. Created a requirements.txt file using the terminal command `pip3 freeze > requirements.txt`

6. Went to `settings.py` and added `import dj_database_url` and updated `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}` also updated `env.py` with `os.environ.setdefault("DATABASE_URL", "postgres://postgres key - copied earlier from Heroku")`

7. I run `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

8. I created a superuser: `python3 manage.py createsuperuser`

9. Logged in to `Amazon AWS`, went to `S3` and created a new `S3` bucket.

10. Returned to terminal window and run `sudo pip3 install django-storages` and `sudo pip3 install boto3`. Went to `settings.py` and added `storages` to `INSTALLED_APPS`.

11. Also in `settings.py` the following lines are added:

`AWS_STORAGE_BUCKET_NAME = 'educadia-test'`\
`AWS_S3_REGION_NAME = 'eu-west-1'`\
`AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")`  
`AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")`  
`AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME`

12. Updated `env.py` with `AWS` keys (these keys are from `S3`).

13. Created `custom_storages.py` at the top level:

`from django.conf import settings`  
`from storages.backends.s3boto3 import S3Boto3Storage`


`class StaticStorage(S3Boto3Storage):`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`location = settings.STATICFILES_LOCATION`

`class MediaStorage(S3Boto3Storage):`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`location = settings.MEDIAFILES_LOCATION`

14. Went to `settings.py` and added:

`STATICFILES_LOCATION = 'static'`  
`STATICFILES_STORAGE = 'custom_storages.StaticStorage'`

`MEDIAFILES_LOCATION = 'media'`  
`DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'`

15. Returned to terminal window and run `python3 manage.py collectstatic`

16. Returned to `Heroku`. In `Settings` clicked on `Reveal Config Vars` button, and added all the following config vars from `env.py`:

| Key         | Value | 
|:-------------:| :----: | 
|  AWS_ACCESS_KEY_ID | secret key here  |
|  AWS_SECRET_ACCESS_KEY | secret key here |
|  DATABASE_URL | secret key here |
|  DISABLE_COLLECTSTATIC| 1 |
|  SECRET_KEY | secret key here |
|  STRIPE_PUBLISHABLE | secret key here |
|  STRIPE_SECRET| secret key here |

17. Clicked to `Deploy`, then `GitHub`, searched for my repository and clicked to `Connect` button.

18. Returned to terminal window and run `sudo pip3 install gunicorn` and added to `requirements.txt`

19. Created a `Procfile` using the following command: `echo web: gunicorn ms4.wsgi:application`

20. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

20. Returned to `Heroku` and hit `Deploy Branch`

21. Once the build is complete, click on `Open app`

22. Went to `settings.py` and added `educadia-test.herokuapp.com` to `ALLOWED_HOSTS`

23. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

24. Returned to `Heroku` and hit `Deploy Branch` again.

### Testing

* During the development of the project I carried out testing, I used Google Chrome Developer Tools consistently to check each changes.

* I have tested the site on Google Chrome, Safari and Firefox. And on the following mobile devices: Samsung note20, iPhone11 and iPhone6. And on iPad tablet.

* Testing was done to ensure that all available (clickable) button are working properly and the links are liked correctly.

* A sample of teachers (3 teachers) and students (5 students) from the school were asked to review the site and documentation to point out any bugs and/or user experience issues. the following was found:

* The website was also tested manually thoroughly. The desktop and the mobile modes were both checked for any errors. Manual (logical) testing of all elements and functionality on every page:

| Action         | Expected result | Outcome | 
|:------------- | :---- | :----: | 
|  open landing/home page | home page loads with available classes cards and basic navigation  | SUCCESS |
|  attemt to sign up by navigating to sign up | sign up page loads and accepts user inputs / user gets email for confirmation  | SUCCESS |
|  attemt to login by navigating to login | login page loads and accepts user input / user is logged in only if both username and password are correct  | SUCCESS  |
|  attemt to signup / login from the inline link on login / sign up page | user can sign up / log in successfully exactly like the previous two tests  | SUCCESS  |
|  attemt to recover passowrd by clicking on forgot password | user can recover password by entering the account associated email  | SUCCESS  |
|  attemt to navigate as a logged in user | user have access to my classes & profile & log out in the navigation  | SUCCESS  |
|  attemt to fill profile details | user input is accepted in the profile page and the view reflects the changes after save | SUCCESS  |
|  attemt to update profile details | user input is accepted in the profile page and the view reflects the changes after save | SUCCESS  |
|  attemt to log in as a teacher | user can add classes by navigating to myclasses  | SUCCESS  |
|  attemt to add a class as a teacher | user can add classes successfully and the added class show up on home page  | SUCCESS  |
|  attemt to edit a class as a teacher | user can edit only a class that was added by the user successfully and the edited class details reflect on myclasses & home views  | SUCCESS  |
|  attemt to delete a class as a teacher | user can delete only a class that was added by the user successfully and the deleted class no longer show on myclasses & home views  | SUCCESS  |
|  attemt to add material to a class as a teacher | user can add material and attach a file to a class that was added by the user successfully and the added materials show on class view  | SUCCESS  |
|  attemt to edit material to a class as a teacher | user can edit material and attach a new file to a class that was added by the user successfully and the updated materials show on class view  | SUCCESS  |
|  attemt to delete material from a class as a teacher | user can delete material from a class nd the deleted material no longer show on class view  | SUCCESS  |
|  attemt to log in as a student | user can join classes  | SUCCESS  |
|  attemt to join a class as a student | user can join a class with the correct join code and the joined class show on my classes view  | SUCCESS  |
|  attemt to join same class again as a student | a message show up iforming user that this class is already joined / prevent duplicate join classes | SUCCESS  |
|  attemt to view materials in a class as a student | user can view materials in classes | SUCCESS  |
|  attemt to download a material as a student | user can download the selected material by clicking the download button | SUCCESS |
|  attemt to join a class from home page as a student | user redirected to my classes view where the user can join a class | SUCCESS |
|  attemt to join a class from home page as a student | user redirected to my classes view where the user can join a class | SUCCESS |
|  attemt to unjoin a class | cannot be done by normal user / only admin user can perform this action | SUCCESS |
|  attemt to donate any amount with valid card number | user input is accepted when clicking pay if card details are valid | SUCCESS |
|  attemt to donate any amount with invalid card number | user input is not accepted and a message show underneath the card number field to inform user of invalid card number | SUCCESS |

* Tested the site using Chrome Lighthouse (for both desktop and mobile) and below are the scores:
  * Mobile
    * Performance: 87
    * Accessibility: 100
    * Best Practices: 87
    * SEO: 90
  * Desktop
    * Performance: 91
    * Accessibility: 100
    * Best Practices: 87
    * SEO: 92

#### Known issues found by users

* When a user logges in he/she is directed to the my account page (originally to fill the user details). However, users prefer if it only directed them to my account when loggin in for the first time.

* Teachers want the class join code to be visable on home and my classes views, which is not visable now.


## Credits

### Content

The project was inspired by websites like google classroom and by the need of the school for a custom online solution.

### Acknowledgements

I'd like to thank

* Teachers of the school for their support and understanding of the long development process, especially the head teacher.
* Code Institute for the tutorials all the help I got to progress and finish the website, and
* Mentor Brian Macharia for his advice and guiding me through this project.
