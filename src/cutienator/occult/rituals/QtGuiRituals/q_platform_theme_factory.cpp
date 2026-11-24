//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformthemefactory_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformthemefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList QPlatformThemeFactory::keys(const QString
//      &platformPluginPath)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN21QPlatformThemeFactory4keysERK7QString(
    const QString *platformPluginPath) {
  return new QList<QString>(
      QPlatformThemeFactory::keys(
          *platformPluginPath));
}

//  QPlatformTheme *QPlatformThemeFactory::create(const QString &key, const
//      QString &platformPluginPath)
extern "C" Q_DECL_EXPORT
QPlatformTheme *ritual_ZN21QPlatformThemeFactory6createERK7QStringS2_(
    const QString *key,
    const QString *platformPluginPath) {
  return QPlatformThemeFactory::create(*key, *platformPluginPath);
}

//  QPlatformThemeFactory::~QPlatformThemeFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformThemeFactoryD1Ev(QPlatformThemeFactory *self) {
  delete self;
}
