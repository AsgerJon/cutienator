//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

//  bool QMimeGlobPatternList::hasPattern(QStringView mimeType, QStringView
//      pattern) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMimeGlobPatternList10hasPatternE11QStringViewS0_(
    const QMimeGlobPatternList *self,
    const QString *mimeType,
    const QString *pattern) {
  return self->hasPattern(QStringView(*mimeType), QStringView(*pattern));
}

//  void QMimeGlobPatternList::removeMimeType(QStringView mimeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeGlobPatternList14removeMimeTypeE11QStringView(
    QMimeGlobPatternList *self,
    const QString *mimeType) {
  self->removeMimeType(QStringView(*mimeType));
}

//  QMimeGlobPatternList::~QMimeGlobPatternList()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeGlobPatternListD1Ev(QMimeGlobPatternList *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
