**[![ ](https://github.com/senkawolf/Software-List/blob/main/media/icons/prev25.png?raw=true) Back](/README.md)**

# My [XBackBone](https://xbackbone.app) Config & Setup

Here’s how I’ve configured my self-hosted XBackBone setup. Some of my modifications may push the boundaries of their license agreement, but my intentions are entirely harmless. Please consider giving SergiX44 a [⭐ on GitHub](https://github.com/SergiX44/XBackBone) and supporting his project with a [donation](https://xbackbone.app/sponsor.html).


![---](https://github.com/senkawolf/Software-List/blob/main/media/icons/line.png?raw=true)

### Theme
My preferred theme is the Dracula theme from [theme-park.dev](https://docs.theme-park.dev/themes/xbackbone/).

![---](https://github.com/senkawolf/Software-List/blob/main/media/icons/line.png?raw=true)

### Additional config.php lines
To change the app install name, simply add the following line to the `config.php` file located in the root directory. Detailed documentation is available [here](https://xbackbone.app/configuration.html#change-app-install-name).

```php
    'app_name' => 'This line will overwrite "XBackBone"',
```

![---](https://github.com/senkawolf/Software-List/blob/main/media/icons/line.png?raw=true)

### Custom HTML Head content
On the system settings page, you can add custom HTML content to the `<header>`. I created a JavaScript file, hosted it, and referenced it in the header.

`<script src="https://example.com/assets/js/xbackbone-inject.js" defer></script>`

Be sure to include the `defer` attribute to ensure the JavaScript loads only after the page has fully loaded.

#### Contents of `xbackbone-inject.js` file:
```js
// Change the page's title
document.title = "Example Images";

// Change the favicon
let link = document.querySelector('link[rel="icon"]');
if (link) {
  link.href = 'https://example.com/favicon.ico'; // Replace with the path to your new favicon
} else {
  // If no favicon exists, you can create one
  let newFavicon = document.createElement('link');
  newFavicon.rel = 'icon';
  newFavicon.href = 'https://example.com/favicon.ico'; // Replace with the path to your new favicon
  document.head.appendChild(newFavicon);
}

// Hide the "Proudly powered by" div on public pages. Still shown in system settings page.
let divToHide = document.querySelector('.text-muted');
if (divToHide) {
  divToHide.style.display = 'none'; // Hides the div
}

// Change the 'og:description' meta tag
let ogDescription = document.querySelector('meta[property="og:description"]');
if (ogDescription) {
  ogDescription.setAttribute('content', "Example's Image Server");
}

// Change the 'description' meta tag
let descriptionMeta = document.querySelector('meta[name="description"]');
if (descriptionMeta) {
  descriptionMeta.setAttribute('content', "Example's Image Server");
}
```