# Installation 

1. Media folder
place each file in corresponding folders.

2. Partials folder
place the partial folders in corresponding `template` folder

3. Connect `index.html`

In your `index.html` add the following lines of code below the `<body>` 

```
  {% include 'partials/site-header.htm' %}
```

4. Connect `base-manager.htm`
In your `base-manger.htm` add the following code above `{% block nody %}`
```
{% block css %}
  {{ block.super }}
  <link rel="stylesheet" href="{% static 'css/layout-tweaks.css' %}" />
  <link rel="stylesheet" href="{% static 'css/header.css' %}" />

{% endblock css%}
```
and finally the following code under `{% block body %}`
```
{% include 'partials/site-header.htm' %}
```
5. Adjust `search.htm`

In `search.htm`change `max-heigh` for Historic Themes, Date Interval, Download Results to `50px`
