//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qabstractfileiconprovider_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qabstractfileiconprovider.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qabstractfileiconprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qicon.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qstring.h>

//  QAbstractFileIconProvider *QAbstractFileIconProviderPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractFileIconProvider *ritual_ZN32QAbstractFileIconProviderPrivate6q_funcEv(
    QAbstractFileIconProviderPrivate *self) {
  return self->q_func();
}

//  const QAbstractFileIconProvider
//      *QAbstractFileIconProviderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractFileIconProvider *ritual_ZNK32QAbstractFileIconProviderPrivate6q_funcEv(
    const QAbstractFileIconProviderPrivate *self) {
  return self->q_func();
}

//  QAbstractFileIconProviderPrivate::QAbstractFileIconProviderPrivate(QAbstr
//      actFileIconProvider *q)
extern "C" Q_DECL_EXPORT
QAbstractFileIconProviderPrivate *ritual_ZN32QAbstractFileIconProviderPrivateC1EP25QAbstractFileIconProvider(
    QAbstractFileIconProvider *q) {
  return new QAbstractFileIconProviderPrivate(q);
}

//  QAbstractFileIconProviderPrivate::~QAbstractFileIconProviderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAbstractFileIconProviderPrivateD1Ev(
    QAbstractFileIconProviderPrivate *self) {
  delete self;
}

//  QIcon QAbstractFileIconProviderPrivate::getPlatformThemeIcon(QAbstractFil
//      eIconProvider::IconType type) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK32QAbstractFileIconProviderPrivate20getPlatformThemeIconEN25QAbstractFileIconProvider8IconTypeE(
    const QAbstractFileIconProviderPrivate *self,
    QAbstractFileIconProvider::IconType type) {
  return new QIcon(self->getPlatformThemeIcon(type));
}

//  QIcon QAbstractFileIconProviderPrivate::getIconThemeIcon(QAbstractFileIco
//      nProvider::IconType type) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK32QAbstractFileIconProviderPrivate16getIconThemeIconEN25QAbstractFileIconProvider8IconTypeE(
    const QAbstractFileIconProviderPrivate *self,
    QAbstractFileIconProvider::IconType type) {
  return new QIcon(self->getIconThemeIcon(type));
}

//  QIcon QAbstractFileIconProviderPrivate::getPlatformThemeIcon(const
//      QFileInfo &info) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK32QAbstractFileIconProviderPrivate20getPlatformThemeIconERK9QFileInfo(
    const QAbstractFileIconProviderPrivate *self,
    const QFileInfo *info) {
  return new QIcon(self->getPlatformThemeIcon(*info));
}

//  QIcon QAbstractFileIconProviderPrivate::getIconThemeIcon(const QFileInfo
//      &info) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK32QAbstractFileIconProviderPrivate16getIconThemeIconERK9QFileInfo(
    const QAbstractFileIconProviderPrivate *self,
    const QFileInfo *info) {
  return new QIcon(self->getIconThemeIcon(*info));
}

//  void QAbstractFileIconProviderPrivate::clearIconTypeCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAbstractFileIconProviderPrivate18clearIconTypeCacheEv() {
  QAbstractFileIconProviderPrivate::clearIconTypeCache();
}

//  QString QAbstractFileIconProviderPrivate::getFileType(const QFileInfo
//      &info)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QAbstractFileIconProviderPrivate11getFileTypeERK9QFileInfo(
    const QFileInfo *info) {
  return new QString(QAbstractFileIconProviderPrivate::getFileType(*info));
}
