//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlserverbufferintegrationfactor
//  y_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlserverbufferintegrationfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList QtWayland::ServerBufferIntegrationFactory::keys()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN9QtWayland30ServerBufferIntegrationFactory4keysEv() {
  return new QList<QString>(
      QtWayland::ServerBufferIntegrationFactory::keys());
}

//  ServerBufferIntegration
//      *QtWayland::ServerBufferIntegrationFactory::create(const QString
//      &name, const QStringList &args)
extern "C" Q_DECL_EXPORT
QtWayland::ServerBufferIntegration *ritual_ZN9QtWayland30ServerBufferIntegrationFactory6createERK7QStringRK5QListIS1_E(
    const QString *name,
    const QList<QString> *args) {
  return QtWayland::ServerBufferIntegrationFactory::create(*name, *args);
}

//  QtWayland::ServerBufferIntegrationFactory::~ServerBufferIntegrationFactor
//      y()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland30ServerBufferIntegrationFactoryD1Ev(
    QtWayland::ServerBufferIntegrationFactory *self) {
  delete self;
}

#endif  // QT_CONFIG(opengl)
