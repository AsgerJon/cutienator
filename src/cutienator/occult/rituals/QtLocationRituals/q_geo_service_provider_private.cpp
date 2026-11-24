//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeoserviceprovider_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeoserviceprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qgeoserviceprovider.h>
#include <QtLocation/private/qgeoserviceprovider_p.h>
#include <QtLocation/qgeoserviceproviderfactory.h>
#include <QtLocation/qgeocodingmanager.h>
#include <QtLocation/private/qgeomappingmanager_p.h>
#include <QtLocation/qgeoroutingmanager.h>
#include <QtLocation/qplacemanager.h>
#include <QtLocation/qgeocodingmanagerengine.h>
#include <QtLocation/private/qgeomappingmanagerengine_p.h>
#include <QtLocation/qgeoroutingmanagerengine.h>
#include <QtLocation/qplacemanagerengine.h>
#include <QtLocation/private/qplacemanagerengine_p.h>
#include <QtCore/QList>
#include <QtCore/QString>
#include <QtCore/QVariant>
#include <QtCore/QCborArray>
#include <QtCore/QDebug>
#include <QtCore/QStringList>
#include <QtCore/QCoreApplication>
#include <QtCore/QObject>
#include <QtCore/QMetaObject>
#include <QtCore/QMetaEnum>
#include <QtCore/private/qfactoryloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeoserviceprovider.cpp, line 797, as _ZN26QGeoServiceProviderPrivate7pluginsEb
inline QMultiHash<QString, QCborMap> QGeoServiceProviderPrivate::plugins(bool reload)
{
    static QMultiHash<QString, QCborMap> plugins;
    static bool alreadyDiscovered = false;

    if (reload == true)
        alreadyDiscovered = false;

    if (!alreadyDiscovered) {
        loadPluginMetadata(plugins);
        alreadyDiscovered = true;
    }
    return plugins;
}

//  from ../qtlocation/src/location/maps/qgeoserviceprovider.cpp, line 691, as _ZN26QGeoServiceProviderPrivateC1Ev
inline QGeoServiceProviderPrivate::QGeoServiceProviderPrivate()
{
    metaData.insert(QStringLiteral("index"), -1);
}

//  from ../qtlocation/src/location/maps/qgeoserviceprovider.cpp, line 696, as _ZN26QGeoServiceProviderPrivateD1Ev
inline QGeoServiceProviderPrivate::~QGeoServiceProviderPrivate()
{
}

//  from ../qtlocation/src/location/maps/qgeoserviceprovider.cpp, line 700, as _ZN26QGeoServiceProviderPrivate6unloadEv
inline void QGeoServiceProviderPrivate::unload()
{
    geocodingManager.reset();
    routingManager.reset();
    mappingManager.reset();
    placeManager.reset();

    factory = nullptr;
    error = QGeoServiceProvider::NoError;
    errorString = QLatin1String("");
    metaData = QCborMap();
    metaData.insert(QStringLiteral("index"), -1);
}
//  -----------------------------------------------------------------------

//  QGeoServiceProviderPrivate::QGeoServiceProviderPrivate()
extern "C" Q_DECL_EXPORT
QGeoServiceProviderPrivate *ritual_ZN26QGeoServiceProviderPrivateC1Ev() {
  return new QGeoServiceProviderPrivate();
}

//  QGeoServiceProviderPrivate::~QGeoServiceProviderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGeoServiceProviderPrivateD1Ev(
    QGeoServiceProviderPrivate *self) {
  delete self;
}

//  void QGeoServiceProviderPrivate::unload()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGeoServiceProviderPrivate6unloadEv(
    QGeoServiceProviderPrivate *self) {
  self->unload();
}
