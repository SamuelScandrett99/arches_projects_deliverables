# Adding persistent overlay order

## Notes

- Currently all users with edit permissoins can edit the overlay order
- There is not need to add an sort order to already existing maps, the code will add it after they are rearranged once
- Currently only works on overlays

## Step 1
### Adjusting `Map Layer` Model

In `models.py` of your core Arches folder add the following line to `MapLayer` class below `searchonly`
```
sortorder = models.IntegerField(blank=True, null=True, default=None)
```


## Step 2
### Migrate the model change

One the model has been altered run the following commands in your `venv` to apply model changes

```
(env) python manage.py makemigrations
(env) python manage.py migrate
```


## Step 3
### Add a new view

After migrations, add `reorder_maps.py` to core Arches views folder


## Step 4
### New URL

Add the following url path to the bottom of `urlpatterns` in `urls.py` in your core Arches folder
```
url(r"^reorder_maps", ReorderMaps.as_view(), name ="reorder_maps"),
```


## Step 5
### Map changes

In `map.js` found in `media > js > viewmodels` in your core Arches folder add the following handler
```
        ko.bindingHandlers.sortable.afterMove = function(e) {
            const map_order = e.sourceParent()
            $.ajax({
                type: "POST",
                data: JSON.stringify({
                    map_order: map_order
                }),
                url: arches.urls.root + "reorder_maps",
            })
         }
```

and a sorting function below `var mapLayers` found on line `135`
```
mapLayers = mapLayers.sort((a, b) => b.sortorder - a.sortorder)
```


## Step 6
### Javascript changes

In the  `javascript.htm` file found in core arches `templates` folder add the following to the bottom of `mapLayers` definition
```
'sortorder': {{map_layer.sortorder|default_if_none:"null"|unlocalize}}
```

# TODOs

- Pull the view out of core arches
- Pull the url out of core arches urls
- Change the ajax call to update rather than post
- Make it work on basemaps and overlays
- Make it feel like it isn't bodged 
- Wrap the view in try/catch
- Worked on dev without js template changes - needs looking into
- Worked on dev without sorting function - needs looking into
