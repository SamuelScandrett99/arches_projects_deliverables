## running koopjs docker

The docker image has been created ahead of time on the staging server.
To run the docker image run the following command


```
sudo docker run -dp 8080:8080 koopjs
```

## arcGIS

Once koopjs docker image is running its time connect arches to arcGIS


To do this download and install the following arches esri add in from the official arches [repo](https://github.com/archesproject/arches-esri-add-in/tree/stable/1.0.x/arches_arcgispro_addin/dist)


Once the plugin is installed, launch the project and connect arches app and finally add the following links as `data from path`

```
http://10.9.3.4:8080/arches/rcahmw/points/FeatureServer/0
http://10.9.3.4:8080/arches/rcahmw/polygons/FeatureServer/0
http://10.9.3.4:8080/arches/rcahmw/lines/FeatureServer/0
```
