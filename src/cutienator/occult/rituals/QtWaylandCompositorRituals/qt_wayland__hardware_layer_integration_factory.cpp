//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlhardwarelayerintegrationfacto
//  ry_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlhardwarelayerintegrationfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList QtWayland::HardwareLayerIntegrationFactory::keys()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN9QtWayland31HardwareLayerIntegrationFactory4keysEv() {
  return new QList<QString>(
      QtWayland::HardwareLayerIntegrationFactory::keys());
}

//  HardwareLayerIntegration
//      *QtWayland::HardwareLayerIntegrationFactory::create(const QString
//      &name, const QStringList &args)
extern "C" Q_DECL_EXPORT
QtWayland::HardwareLayerIntegration *ritual_ZN9QtWayland31HardwareLayerIntegrationFactory6createERK7QStringRK5QListIS1_E(
    const QString *name,
    const QList<QString> *args) {
  return QtWayland::HardwareLayerIntegrationFactory::create(*name, *args);
}

//  QtWayland::HardwareLayerIntegrationFactory::~HardwareLayerIntegrationFact
//      ory()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland31HardwareLayerIntegrationFactoryD1Ev(
    QtWayland::HardwareLayerIntegrationFactory *self) {
  delete self;
}

#endif  // QT_CONFIG(opengl)
