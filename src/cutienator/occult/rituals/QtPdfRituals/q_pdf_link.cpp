//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdf/qpdflink.h, Qt 6.12.0. Changes made here are lost.
#include <QtPdf/6.12.0/QtPdf/private/qtpdfglobal_p.h>
#include <QtPdf/qpdflink.h>
#include <QtCore/qpoint.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPdf/qpdflink.h>
#include <QtPdf/private/qpdflink_p.h>
#include <QtPdf/private/qpdflinkmodel_p.h>
#include <QtGui/QGuiApplication>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/pdf/qpdflink.cpp, line 35, as _ZN8QPdfLinkC1Ei5QListI6QRectFE7QStringS3_
inline QPdfLink::QPdfLink(int page, QList<QRectF> rects,
                                   QString contextBefore, QString contextAfter)
    : QPdfLink(new QPdfLinkPrivate(page, std::move(rects),
                                                   std::move(contextBefore),
                                                   std::move(contextAfter)))
{
}

//  from ../qtwebengine/src/pdf/qpdflink.cpp, line 43, as _ZN8QPdfLinkC1EP15QPdfLinkPrivate
inline QPdfLink::QPdfLink(QPdfLinkPrivate *d) : d(d) {}
//  -----------------------------------------------------------------------

//  QPdfLink::QPdfLink()
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_ZN8QPdfLinkC1Ev() {
  return new QPdfLink();
}

//  QPdfLink::~QPdfLink()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfLinkD1Ev(QPdfLink *self) {
  delete self;
}

//  QPdfLink &QPdfLink::operator=(const QPdfLink &other)
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_ZN8QPdfLinkaSERKS_(QPdfLink *self, const QPdfLink *other) {
  return &(self->operator=(*other));
}

//  QPdfLink::QPdfLink(const QPdfLink &other)
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_ZN8QPdfLinkC1ERKS_(const QPdfLink *other) {
  return new QPdfLink(*other);
}

//  QPdfLink::QPdfLink(QPdfLink &&other)
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_ZN8QPdfLinkC1EOS_(QPdfLink *other) {
  return new QPdfLink(std::move(*other));
}

//  QPdfLink &QPdfLink::operator=(QPdfLink &&other)
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_ZN8QPdfLinkaSEOS_(QPdfLink *self, QPdfLink *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QPdfLink::swap(QPdfLink &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfLink4swapERS_(QPdfLink *self, QPdfLink *other) {
  self->swap(*other);
}

//  bool QPdfLink::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPdfLink7isValidEv(const QPdfLink *self) {
  return self->isValid();
}

//  int QPdfLink::page() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPdfLink4pageEv(const QPdfLink *self) {
  return self->page();
}

//  QPointF QPdfLink::location() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8QPdfLink8locationEv(const QPdfLink *self) {
  return new QPointF(self->location());
}

//  qreal QPdfLink::zoom() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QPdfLink4zoomEv(const QPdfLink *self) {
  return self->zoom();
}

//  QUrl QPdfLink::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8QPdfLink3urlEv(const QPdfLink *self) {
  return new QUrl(self->url());
}

//  QString QPdfLink::contextBefore() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QPdfLink13contextBeforeEv(const QPdfLink *self) {
  return new QString(self->contextBefore());
}

//  QString QPdfLink::contextAfter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QPdfLink12contextAfterEv(const QPdfLink *self) {
  return new QString(self->contextAfter());
}

//  QList<QRectF> QPdfLink::rectangles() const
extern "C" Q_DECL_EXPORT
QList<QRectF> *ritual_ZNK8QPdfLink10rectanglesEv(const QPdfLink *self) {
  return new QList<QRectF>(self->rectangles());
}

//  QString QPdfLink::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QPdfLink8toStringEv(const QPdfLink *self) {
  return new QString(self->toString());
}

//  void QPdfLink::copyToClipboard(QClipboard::Mode mode) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QPdfLink15copyToClipboardEN10QClipboard4ModeE(
    const QPdfLink *self,
    QClipboard::Mode mode) {
  self->copyToClipboard(mode);
}

//  QPdfLink::QPdfLink(int page, QPointF location, qreal zoom)
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_ZN8QPdfLinkC1Ei7QPointFd(
    int page,
    const QPointF *location,
    qreal zoom) {
  return new QPdfLink(page, *location, zoom);
}

//  QPdfLink::QPdfLink(int page, QList<QRectF> rects, QString contextBefore,
//      QString contextAfter)
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_ZN8QPdfLinkC1Ei5QListI6QRectFE7QStringS3_(
    int page,
    const QList<QRectF> *rects,
    const QString *contextBefore,
    const QString *contextAfter) {
  return new QPdfLink(page, *rects, *contextBefore, *contextAfter);
}

//  QPdfLink::QPdfLink(QPdfLinkPrivate *d)
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_ZN8QPdfLinkC1EP15QPdfLinkPrivate(QPdfLinkPrivate *d) {
  return new QPdfLink(d);
}

//  QList<QPdfLink>::QList()
extern "C" Q_DECL_EXPORT
QList<QPdfLink> *ritual_list_make_QPdfLink() {
  return new QList<QPdfLink>();
}

//  void QList<QPdfLink>::append(const QPdfLink &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPdfLink(
    QList<QPdfLink> *self,
    const QPdfLink *element) {
  self->append(*element);
}

//  qsizetype QList<QPdfLink>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPdfLink(const QList<QPdfLink> *self) {
  return self->size();
}

//  const QPdfLink &QList<QPdfLink>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_list_at_QPdfLink(
    const QList<QPdfLink> *self,
    long long index) {
  return new QPdfLink(self->at(index));
}

//  QList<QPdfLink>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPdfLink(QList<QPdfLink> *self) {
  delete self;
}
