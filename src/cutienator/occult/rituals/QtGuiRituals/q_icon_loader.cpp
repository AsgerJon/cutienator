//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qiconloader_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_ICON)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qiconloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QIconLoader::QIconLoader()
extern "C" Q_DECL_EXPORT
QIconLoader *ritual_ZN11QIconLoaderC1Ev() {
  return new QIconLoader();
}

//  QThemeIconInfo QIconLoader::loadIcon(const QString &iconName) const
extern "C" Q_DECL_EXPORT
QThemeIconInfo *ritual_ZNK11QIconLoader8loadIconERK7QString(
    const QIconLoader *self,
    const QString *iconName) {
  return new QThemeIconInfo(self->loadIcon(*iconName));
}

//  uint QIconLoader::themeKey() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK11QIconLoader8themeKeyEv(const QIconLoader *self) {
  return self->themeKey();
}

//  QString QIconLoader::themeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QIconLoader9themeNameEv(const QIconLoader *self) {
  return new QString(self->themeName());
}

//  void QIconLoader::setThemeName(const QString &themeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconLoader12setThemeNameERK7QString(
    QIconLoader *self,
    const QString *themeName) {
  self->setThemeName(*themeName);
}

//  QString QIconLoader::fallbackThemeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QIconLoader17fallbackThemeNameEv(
    const QIconLoader *self) {
  return new QString(self->fallbackThemeName());
}

//  void QIconLoader::setFallbackThemeName(const QString &themeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconLoader20setFallbackThemeNameERK7QString(
    QIconLoader *self,
    const QString *themeName) {
  self->setFallbackThemeName(*themeName);
}

//  QIconTheme QIconLoader::theme()
extern "C" Q_DECL_EXPORT
QIconTheme *ritual_ZN11QIconLoader5themeEv(QIconLoader *self) {
  return new QIconTheme(self->theme());
}

//  void QIconLoader::setThemeSearchPath(const QStringList &searchPaths)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconLoader18setThemeSearchPathERK5QListI7QStringE(
    QIconLoader *self,
    const QList<QString> *searchPaths) {
  self->setThemeSearchPath(*searchPaths);
}

//  QStringList QIconLoader::themeSearchPaths() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QIconLoader16themeSearchPathsEv(
    const QIconLoader *self) {
  return new QList<QString>(self->themeSearchPaths());
}

//  void QIconLoader::setFallbackSearchPaths(const QStringList &searchPaths)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconLoader22setFallbackSearchPathsERK5QListI7QStringE(
    QIconLoader *self,
    const QList<QString> *searchPaths) {
  self->setFallbackSearchPaths(*searchPaths);
}

//  QStringList QIconLoader::fallbackSearchPaths() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QIconLoader19fallbackSearchPathsEv(
    const QIconLoader *self) {
  return new QList<QString>(self->fallbackSearchPaths());
}

//  QIconLoader *QIconLoader::instance()
extern "C" Q_DECL_EXPORT
QIconLoader *ritual_ZN11QIconLoader8instanceEv() {
  return QIconLoader::instance();
}

//  void QIconLoader::updateSystemTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconLoader17updateSystemThemeEv(QIconLoader *self) {
  self->updateSystemTheme();
}

//  void QIconLoader::invalidateKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconLoader13invalidateKeyEv(QIconLoader *self) {
  self->invalidateKey();
}

//  void QIconLoader::ensureInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconLoader17ensureInitializedEv(QIconLoader *self) {
  self->ensureInitialized();
}

//  bool QIconLoader::hasUserTheme() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QIconLoader12hasUserThemeEv(const QIconLoader *self) {
  return self->hasUserTheme();
}

//  QIconEngine *QIconLoader::iconEngine(const QString &iconName) const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK11QIconLoader10iconEngineERK7QString(
    const QIconLoader *self,
    const QString *iconName) {
  return self->iconEngine(*iconName);
}

//  QThemeIconInfo QIconLoader::lookupFallbackIcon(const QString &iconName)
//      const
extern "C" Q_DECL_EXPORT
QThemeIconInfo *ritual_ZNK11QIconLoader18lookupFallbackIconERK7QString(
    const QIconLoader *self,
    const QString *iconName) {
  return new QThemeIconInfo(self->lookupFallbackIcon(*iconName));
}

//  QIconLoader::~QIconLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconLoaderD1Ev(QIconLoader *self) {
  delete self;
}

#endif  // !defined(QT_NO_ICON)
