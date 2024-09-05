# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| templates | account.html | ![screenshot](documentation/testingScreenshots/accountHtmlValidation.jpeg) | Errors due to validator unable to interpret jinja |
| templates | index.html | ![screenshot](documentation/testingScreenshots/indexHtmlValidation.jpeg) | Errors due to validator unable to interpret jinja |
| templates | base.html | ![screenshot](documentation/testingScreenshots/baseHtmlValidation.jpeg) | Errors due to validator unable to interpret jinja |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/testingScreenshots/stylesCssValidator.jpeg) | One warning due to validator unable to interpret @import links |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| templates | account.html | ![screenshot](documentation/testingScreenshots/jsAccountValidation.jpeg) | |
| templates | index.html | ![screenshot](documentation/testingScreenshots/jsIndexValidation.jpeg) | |
| static | script.js | ![screenshot](documentation/testingScreenshots/jsScriptValidation.jpeg) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| root | app.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/patrickaod/CineVault/main/app.py) | ![screenshot](documentation/testingScreenshots/pythonValidator.jpeg) | Unfortunately, seperating the mongodb queries prevented the code base from running. To retain stability further investigation is require to resolve these linting issue. |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Account | Notes |
| --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testingScreenshots/indexChrome.png) | ![screenshot](documentation/testingScreenshots/accountChrome.png) | Works as expected |
| Firefox | ![screenshot](documentation/testingScreenshots/indexFirefox.png) | ![screenshot](documentation/testingScreenshots/accountFirefox.png)| Works as expected |
| Edge | ![screenshot](documentation/testingScreenshots/indexEdge.jpeg) | ![screenshot](documentation/testingScreenshots/accountEdge.jpeg) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Notes |
| --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/testingScreenshots/indexMobile.png) | ![screenshot](documentation/testingScreenshots/accountPhone.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/testingScreenshots/indexTablet.png) | ![screenshot](documentation/testingScreenshots/accountTablet.png) | Works as expected |
| Desktop | ![screenshot](documentation/testingScreenshots/indexLaptop.png) | ![screenshot](documentation/testingScreenshots/accountLaptop.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/testingScreenshots/indexXlaptop.png) | ![screenshot](documentation/testingScreenshots/accountXlaptop.png) |  Works as expected |
| Google Pixel 7 Pro | ![screenshot](documentation/testingScreenshots/indexPixel7.png) | ![screenshot](documentation/testingScreenshots/accountPixel7.png) |  Works as expected |


## Lighthouse Audit

Lighthouse is a tool for auditing web pages, assessing performance, accessibility, best practices, and SEO. To test your live site, you can use Chrome DevTools, the Lighthouse CLI, PageSpeed Insights, or Web.dev Measure. Key areas to analyse performance metrics like loading speed and visual stability, accessibility, and SEO. Integrating Lighthouse into your project can helps enhance your site's user experience and search engine visibility.

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Index | ![screenshot](documentation/testingScreenshots/googleLighthouseMobile.png) | ![screenshot](documentation/testingScreenshots/googleLighthouseDesktop.png) | postive results |
| Account | ![screenshot](documentation/testingScreenshots/googleLighthouseMobileAccount.png) | ![screenshot](documentation/testingScreenshots/googleLighthouseDesktopAccount.png) | postive results |


