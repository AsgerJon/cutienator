//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qstyle_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  QCachedPainter::QCachedPainter(QPainter *painter, const QString
//      &cachePrefix, const QStyleOption *option, QSize size, QRect
//      paintRect)
extern "C" Q_DECL_EXPORT
QCachedPainter *ritual_ZN14QCachedPainterC1EP8QPainterRK7QStringPK12QStyleOption5QSize5QRect(
    QPainter *painter,
    const QString *cachePrefix,
    const QStyleOption *option,
    const QSize *size,
    const QRect *paintRect) {
  return new QCachedPainter(
      painter,
      *cachePrefix,
      option,
      *size,
      *paintRect);
}

//  QCachedPainter::~QCachedPainter()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCachedPainterD1Ev(QCachedPainter *self) {
  delete self;
}

//  void QCachedPainter::finish()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCachedPainter6finishEv(QCachedPainter *self) {
  self->finish();
}

//  bool QCachedPainter::needsPainting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QCachedPainter13needsPaintingEv(
    const QCachedPainter *self) {
  return self->needsPainting();
}

//  QRect QCachedPainter::pixmapRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QCachedPainter10pixmapRectEv(const QCachedPainter *self) {
  return new QRect(self->pixmapRect());
}

//  QPainter *QCachedPainter::operator->()
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZN14QCachedPainterptEv(QCachedPainter *self) {
  return self->operator->();
}

//  QPainter *QCachedPainter::painter()
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZN14QCachedPainter7painterEv(QCachedPainter *self) {
  return self->painter();
}

//  void QCachedPainter::cleanupPixmapCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCachedPainter18cleanupPixmapCacheEv() {
  QCachedPainter::cleanupPixmapCache();
}
