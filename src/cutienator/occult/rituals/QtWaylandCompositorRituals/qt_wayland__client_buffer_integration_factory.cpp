//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegrationfactor
//  y_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegrationfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList QtWayland::ClientBufferIntegrationFactory::keys()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN9QtWayland30ClientBufferIntegrationFactory4keysEv() {
  return new QList<QString>(
      QtWayland::ClientBufferIntegrationFactory::keys());
}

//  QtWayland::ClientBufferIntegrationFactory::~ClientBufferIntegrationFactor
//      y()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland30ClientBufferIntegrationFactoryD1Ev(
    QtWayland::ClientBufferIntegrationFactory *self) {
  delete self;
}

#endif  // QT_CONFIG(opengl)
