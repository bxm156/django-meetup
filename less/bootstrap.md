---
published: true
layout: index
---

### Setting up Bootstrap

#### Get the code
There are many ways to get the bootstrap code. Most people just downloaded it to their project, but I prefer using a git submodule
```bash
git submodule add git@github.com:twbs/bootstrap.git Project/static/bootstrap
```
That way you can stay up to date and pull in the latest fixes easily if you so choose.
#### Setup
1. Copy the bootstrap.less file from Project/static/bootstrap/less/bootstrap.less to the static directory and update the paths inside the file. Call it theme.less. Put your new stuff at the bottom of the file

2. Create a new variable.less file in the static folder, and use it instead of the Project/static/bootstrap/less/variables.less
You can override any Bootstrap variables in this file

4. Load the the compress tag
```html
{% load compress %}
```

5. Include the Bootstrap LESS and another other CSS/LESS files in the template and surrounded them with the {% compress css %} tag.
```html
{% load static %}
<!DOCTYPE html>
<html>
	<head>
    	{% compress css %}
		<link rel="stylesheet" type="text/less" href="{% get_static_prefix %}theme.less" media="screen">
        {% endcompress %}
    </head>
</html>
```
6. Include the required javascript files from the bootstrap/js folder. You can add these in the <head> or at the end of the <body>. You may also optionally surround them in {% compress js %} tags.

```html
{% compress js %}
	<script type="text/javascript" src="{% get_static_prefix %}js/jquery-1.10.1.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-affix.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-alert.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-button.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-carousel.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-collapse.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-dropdown.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-modal.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-tooltip.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-popover.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-scrollspy.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-tab.js"></script>
	<script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-transition.js"></script>
    <script type="text/javascript" src="{% get_static_prefix %}bootstrap/js/bootstrap-typeahead.js"></script>
{% endcompress %}
```