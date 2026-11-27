//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdf/6.12.0/QtPdf/private/qpdflink_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtPdf/6.12.0/QtPdf/private/qtpdfglobal_p.h>
#include <QtPdf/QtPdf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPdf/6.12.0/QtPdf/private/qpdflink_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QPdfLinkPrivate::QPdfLinkPrivate()
extern "C" Q_DECL_EXPORT
QPdfLinkPrivate *ritual_ZN15QPdfLinkPrivateC1Ev() {
  return new QPdfLinkPrivate();
}

//  QPdfLinkPrivate::QPdfLinkPrivate(int page, QPointF location, qreal zoom)
extern "C" Q_DECL_EXPORT
QPdfLinkPrivate *ritual_ZN15QPdfLinkPrivateC1Ei7QPointFd(
    int page,
    const QPointF *location,
    qreal zoom) {
  return new QPdfLinkPrivate(page, *location, zoom);
}

//  QPdfLinkPrivate::QPdfLinkPrivate(int page, QList<QRectF> rects, QString
//      contextBefore, QString contextAfter)
extern "C" Q_DECL_EXPORT
QPdfLinkPrivate *ritual_ZN15QPdfLinkPrivateC1Ei5QListI6QRectFE7QStringS3_(
    int page,
    const QList<QRectF> *rects,
    const QString *contextBefore,
    const QString *contextAfter) {
  return new QPdfLinkPrivate(page, *rects, *contextBefore, *contextAfter);
}

//  QPdfLinkPrivate::~QPdfLinkPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfLinkPrivateD1Ev(QPdfLinkPrivate *self) {
  delete self;
}
