//  Written by hand on 2026-11-25 from
//  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegrationfactory_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt builds the class under QT_CONFIG(opengl), as its CMakeLists.txt
//  says.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegrationfactory_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList QtWayland::ClientBufferIntegrationFactory::keys()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN9QtWayland30ClientBufferIntegrationFactory4keysEv() {
  return new QList<QString>(
      QtWayland::ClientBufferIntegrationFactory::keys());
}

//  ClientBufferIntegration
//      *QtWayland::ClientBufferIntegrationFactory::create(const QString
//      &name, const QStringList &args)
extern "C" Q_DECL_EXPORT
QtWayland::ClientBufferIntegration *ritual_ZN9QtWayland30ClientBufferIntegrationFactory6createERK7QStringRK5QListIS1_E(
    const QString *name,
    const QList<QString> *args) {
  return QtWayland::ClientBufferIntegrationFactory::create(*name, *args);
}

//  QtWayland::ClientBufferIntegrationFactory::~ClientBufferIntegrationFactor
//      y()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland30ClientBufferIntegrationFactoryD1Ev(
    QtWayland::ClientBufferIntegrationFactory *self) {
  delete self;
}

#endif  // QT_CONFIG(opengl)
