//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qglyphrun_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_RAWFONT)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qglyphrun_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qglyphrun.h>

//  QGlyphRunPrivate::QGlyphRunPrivate()
extern "C" Q_DECL_EXPORT
QGlyphRunPrivate *ritual_ZN16QGlyphRunPrivateC1Ev() {
  return new QGlyphRunPrivate();
}

//  QGlyphRunPrivate::QGlyphRunPrivate(const QGlyphRunPrivate &other)
extern "C" Q_DECL_EXPORT
QGlyphRunPrivate *ritual_ZN16QGlyphRunPrivateC1ERKS_(
    const QGlyphRunPrivate *other) {
  return new QGlyphRunPrivate(*other);
}

//  QGlyphRunPrivate *QGlyphRunPrivate::get(const QGlyphRun &glyphRun)
extern "C" Q_DECL_EXPORT
QGlyphRunPrivate *ritual_ZN16QGlyphRunPrivate3getERK9QGlyphRun(
    const QGlyphRun *glyphRun) {
  return QGlyphRunPrivate::get(*glyphRun);
}

//  QGlyphRunPrivate::~QGlyphRunPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGlyphRunPrivateD1Ev(QGlyphRunPrivate *self) {
  delete self;
}

#endif  // !defined(QT_NO_RAWFONT)
