//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdf/6.12.0/QtPdf/private/qpdfselection_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtPdf/6.12.0/QtPdf/private/qtpdfglobal_p.h>
#include <QtPdf/QtPdf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPdf/6.12.0/QtPdf/private/qpdfselection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpolygon.h>
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>

//  QPdfSelectionPrivate::QPdfSelectionPrivate()
extern "C" Q_DECL_EXPORT
QPdfSelectionPrivate *ritual_ZN20QPdfSelectionPrivateC1Ev() {
  return new QPdfSelectionPrivate();
}

//  QPdfSelectionPrivate::QPdfSelectionPrivate(const QString &text,
//      QList<QPolygonF> bounds, QRectF boundingRect, int startIndex, int
//      endIndex)
extern "C" Q_DECL_EXPORT
QPdfSelectionPrivate *ritual_ZN20QPdfSelectionPrivateC1ERK7QString5QListI9QPolygonFE6QRectFii(
    const QString *text,
    const QList<QPolygonF> *bounds,
    const QRectF *boundingRect,
    int startIndex,
    int endIndex) {
  return new QPdfSelectionPrivate(
      *text,
      *bounds,
      *boundingRect,
      startIndex,
      endIndex);
}

//  QPdfSelectionPrivate::~QPdfSelectionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPdfSelectionPrivateD1Ev(QPdfSelectionPrivate *self) {
  delete self;
}
