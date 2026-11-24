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

//  QIconTheme::QIconTheme()
extern "C" Q_DECL_EXPORT
QIconTheme *ritual_ZN10QIconThemeC1Ev() {
  return new QIconTheme();
}

//  QList<QIconDirInfo> QIconTheme::keyList() const
extern "C" Q_DECL_EXPORT
QList<QIconDirInfo> *ritual_ZNK10QIconTheme7keyListEv(
    const QIconTheme *self) {
  return new QList<QIconDirInfo>(self->keyList());
}

//  QStringList QIconTheme::contentDirs() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QIconTheme11contentDirsEv(
    const QIconTheme *self) {
  return new QList<QString>(self->contentDirs());
}

//  bool QIconTheme::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QIconTheme7isValidEv(const QIconTheme *self) {
  return self->isValid();
}

//  QIconTheme::~QIconTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QIconThemeD1Ev(QIconTheme *self) {
  delete self;
}

#endif  // !defined(QT_NO_ICON)
