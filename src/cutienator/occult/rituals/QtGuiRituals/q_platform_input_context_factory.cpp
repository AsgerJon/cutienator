//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatforminputcontextfactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatforminputcontextfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList QPlatformInputContextFactory::keys()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN28QPlatformInputContextFactory4keysEv() {
  return new QList<QString>(QPlatformInputContextFactory::keys());
}

//  QStringList QPlatformInputContextFactory::requested()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN28QPlatformInputContextFactory9requestedEv() {
  return new QList<QString>(QPlatformInputContextFactory::requested());
}

//  QPlatformInputContext *QPlatformInputContextFactory::create(const
//      QStringList &keys)
extern "C" Q_DECL_EXPORT
QPlatformInputContext *ritual_ZN28QPlatformInputContextFactory6createERK5QListI7QStringE(
    const QList<QString> *keys) {
  return QPlatformInputContextFactory::create(*keys);
}

//  QPlatformInputContext *QPlatformInputContextFactory::create(const QString
//      &key)
extern "C" Q_DECL_EXPORT
QPlatformInputContext *ritual_ZN28QPlatformInputContextFactory6createERK7QString(
    const QString *key) {
  return QPlatformInputContextFactory::create(*key);
}

//  QPlatformInputContext *QPlatformInputContextFactory::create()
extern "C" Q_DECL_EXPORT
QPlatformInputContext *ritual_ZN28QPlatformInputContextFactory6createEv() {
  return QPlatformInputContextFactory::create();
}

//  QPlatformInputContextFactory::~QPlatformInputContextFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformInputContextFactoryD1Ev(
    QPlatformInputContextFactory *self) {
  delete self;
}
