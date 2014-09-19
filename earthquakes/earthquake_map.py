from glue import custom_viewer

GREEN = (229 / 255., 245 / 255., 224 / 255.)
BLUE = (222 / 255., 235 / 255., 247 / 255.)

earthquake_map = custom_viewer('Earthquake Map',
                               longitude='att(longitude)',
                               latitude='att(latitude)',
                               magnitude='att(mag)')


@earthquake_map.plot_data
def show_data(longitude, latitude, magnitude, style, state):
    x, y = state.m(longitude, latitude)
    return state.m.scatter(x, y, c=style.color, s=magnitude ** 3,
                           alpha=0.5, edgecolor='none')


@earthquake_map.plot_subset
def show_subset(longitude, latitude, magnitude, style, state):
    x, y = state.m(longitude, latitude)
    return state.m.scatter(x, y, c=style.color, s=magnitude ** 3,
                           alpha=1.0, edgecolor='none')


@earthquake_map.setup
def show_world(axes, state):
    from mpl_toolkits.basemap import Basemap

    m = Basemap(projection='mill', llcrnrlat=-80, urcrnrlat=80,
                llcrnrlon=-180, urcrnrlon=180, lat_ts=20,
                resolution='c', ax=axes)
    m.drawcoastlines(zorder=-1)
    m.fillcontinents(color=GREEN, lake_color=BLUE, zorder=-2)
    m.drawmapboundary(fill_color=BLUE, zorder=-3)
    state.m = m


@earthquake_map.select
def select(roi, latitude, longitude, state):
    x, y = state.m(longitude, latitude)
    return roi.contains(x, y)
