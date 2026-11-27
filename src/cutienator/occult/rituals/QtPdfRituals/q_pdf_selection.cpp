//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdf/qpdfselection.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtPdf/6.12.0/QtPdf/private/qtpdfglobal_p.h>
#include <QtPdf/qpdfselection.h>
#include <QtGui/qpolygon.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPdf/qpdfselection.h>
#include <QtPdf/private/qpdfselection_p.h>
#include <QtGui/QGuiApplication>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/pdf/qpdfselection.cpp, line 26, as _ZN13QPdfSelectionC1Ev
inline QPdfSelection::QPdfSelection()
  : d(new QPdfSelectionPrivate())
{
}

//  from ../qtwebengine/src/pdf/qpdfselection.cpp, line 37, as _ZN13QPdfSelectionC1ERK7QString5QListI9QPolygonFE6QRectFii
inline QPdfSelection::QPdfSelection(const QString &text, QList<QPolygonF> bounds, QRectF boundingRect, int startIndex, int endIndex)
  : d(new QPdfSelectionPrivate(text, bounds, boundingRect, startIndex, endIndex))
{
}

//  from ../qtwebengine/src/pdf/qpdfselection.cpp, line 42, as _ZN13QPdfSelectionC1EP20QPdfSelectionPrivate
inline QPdfSelection::QPdfSelection(QPdfSelectionPrivate *d)
  : d(d)
{
}
//  -----------------------------------------------------------------------

//  QPdfSelection::~QPdfSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPdfSelectionD1Ev(QPdfSelection *self) {
  delete self;
}

//  QPdfSelection::QPdfSelection(const QPdfSelection &other)
extern "C" Q_DECL_EXPORT
QPdfSelection *ritual_ZN13QPdfSelectionC1ERKS_(const QPdfSelection *other) {
  return new QPdfSelection(*other);
}

//  QPdfSelection &QPdfSelection::operator=(const QPdfSelection &other)
extern "C" Q_DECL_EXPORT
QPdfSelection *ritual_ZN13QPdfSelectionaSERKS_(
    QPdfSelection *self,
    const QPdfSelection *other) {
  return &(self->operator=(*other));
}

//  QPdfSelection::QPdfSelection(QPdfSelection &&other)
extern "C" Q_DECL_EXPORT
QPdfSelection *ritual_ZN13QPdfSelectionC1EOS_(QPdfSelection *other) {
  return new QPdfSelection(std::move(*other));
}

//  QPdfSelection &QPdfSelection::operator=(QPdfSelection &&other)
extern "C" Q_DECL_EXPORT
QPdfSelection *ritual_ZN13QPdfSelectionaSEOS_(
    QPdfSelection *self,
    QPdfSelection *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QPdfSelection::swap(QPdfSelection &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPdfSelection4swapERS_(
    QPdfSelection *self,
    QPdfSelection *other) {
  self->swap(*other);
}

//  bool QPdfSelection::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPdfSelection7isValidEv(const QPdfSelection *self) {
  return self->isValid();
}

//  QList<QPolygonF> QPdfSelection::bounds() const
extern "C" Q_DECL_EXPORT
QList<QPolygonF> *ritual_ZNK13QPdfSelection6boundsEv(
    const QPdfSelection *self) {
  return new QList<QPolygonF>(self->bounds());
}

//  QString QPdfSelection::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPdfSelection4textEv(const QPdfSelection *self) {
  return new QString(self->text());
}

//  QRectF QPdfSelection::boundingRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QPdfSelection17boundingRectangleEv(
    const QPdfSelection *self) {
  return new QRectF(self->boundingRectangle());
}

//  int QPdfSelection::startIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPdfSelection10startIndexEv(const QPdfSelection *self) {
  return self->startIndex();
}

//  int QPdfSelection::endIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPdfSelection8endIndexEv(const QPdfSelection *self) {
  return self->endIndex();
}

#if QT_CONFIG(clipboard)
//  void QPdfSelection::copyToClipboard(QClipboard::Mode mode) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QPdfSelection15copyToClipboardEN10QClipboard4ModeE(
    const QPdfSelection *self,
    QClipboard::Mode mode) {
  self->copyToClipboard(mode);
}
#endif  // QT_CONFIG(clipboard)

//  QPdfSelection::QPdfSelection()
extern "C" Q_DECL_EXPORT
QPdfSelection *ritual_ZN13QPdfSelectionC1Ev() {
  return new QPdfSelection();
}

//  QPdfSelection::QPdfSelection(const QString &text, QList<QPolygonF>
//      bounds, QRectF boundingRect, int startIndex, int endIndex)
extern "C" Q_DECL_EXPORT
QPdfSelection *ritual_ZN13QPdfSelectionC1ERK7QString5QListI9QPolygonFE6QRectFii(
    const QString *text,
    const QList<QPolygonF> *bounds,
    const QRectF *boundingRect,
    int startIndex,
    int endIndex) {
  return new QPdfSelection(
      *text,
      *bounds,
      *boundingRect,
      startIndex,
      endIndex);
}

//  QPdfSelection::QPdfSelection(QPdfSelectionPrivate *d)
extern "C" Q_DECL_EXPORT
QPdfSelection *ritual_ZN13QPdfSelectionC1EP20QPdfSelectionPrivate(
    QPdfSelectionPrivate *d) {
  return new QPdfSelection(d);
}
