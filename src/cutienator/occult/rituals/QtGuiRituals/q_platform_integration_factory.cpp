//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformintegrationfactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformintegrationfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList QPlatformIntegrationFactory::keys(const QString
//      &platformPluginPath)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN27QPlatformIntegrationFactory4keysERK7QString(
    const QString *platformPluginPath) {
  return new QList<QString>(
      QPlatformIntegrationFactory::keys(
          *platformPluginPath));
}

//  QPlatformIntegration *QPlatformIntegrationFactory::create(const QString
//      &name, const QStringList &args, int &argc, char **argv, const QString
//      &platformPluginPath)
extern "C" Q_DECL_EXPORT
QPlatformIntegration *ritual_ZN27QPlatformIntegrationFactory6createERK7QStringRK5QListIS0_ERiPPcS2_(
    const QString *name,
    const QList<QString> *args,
    int *argc,
    char **argv,
    const QString *platformPluginPath) {
  return QPlatformIntegrationFactory::create(
      *name,
      *args,
      *argc,
      argv,
      *platformPluginPath);
}

//  QPlatformIntegrationFactory::~QPlatformIntegrationFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QPlatformIntegrationFactoryD1Ev(
    QPlatformIntegrationFactory *self) {
  delete self;
}
