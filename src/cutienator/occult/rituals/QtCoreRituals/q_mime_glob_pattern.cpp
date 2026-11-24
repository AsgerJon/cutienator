//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QString &QMimeGlobPattern::pattern() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QMimeGlobPattern7patternEv(
    const QMimeGlobPattern *self) {
  return new QString(self->pattern());
}

//  unsigned int QMimeGlobPattern::weight() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK16QMimeGlobPattern6weightEv(
    const QMimeGlobPattern *self) {
  return self->weight();
}

//  const QString &QMimeGlobPattern::mimeType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QMimeGlobPattern8mimeTypeEv(
    const QMimeGlobPattern *self) {
  return new QString(self->mimeType());
}

//  bool QMimeGlobPattern::isCaseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMimeGlobPattern15isCaseSensitiveEv(
    const QMimeGlobPattern *self) {
  return self->isCaseSensitive();
}

//  QMimeGlobPattern::~QMimeGlobPattern()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeGlobPatternD1Ev(QMimeGlobPattern *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
