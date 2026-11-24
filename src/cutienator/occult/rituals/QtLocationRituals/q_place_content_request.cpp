//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacecontentrequest.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/qplacecontentrequest.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplacecontentrequest_p.h"
#include "qplacecontentrequest.h"
#include "qgeocoordinate.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplacecontentrequest.cpp, line 192, as _ZN20QPlaceContentRequest6d_funcEv
inline QPlaceContentRequestPrivate *QPlaceContentRequest::d_func()
{
    return static_cast<QPlaceContentRequestPrivate *>(d_ptr.data());
}

//  from ../qtlocation/src/location/places/qplacecontentrequest.cpp, line 197, as _ZNK20QPlaceContentRequest6d_funcEv
inline const QPlaceContentRequestPrivate *QPlaceContentRequest::d_func() const
{
    return static_cast<const QPlaceContentRequestPrivate *>(d_ptr.constData());
}
//  -----------------------------------------------------------------------

//  QPlaceContentRequest::QPlaceContentRequest()
extern "C" Q_DECL_EXPORT
QPlaceContentRequest *ritual_ZN20QPlaceContentRequestC1Ev() {
  return new QPlaceContentRequest();
}

//  QPlaceContentRequest::QPlaceContentRequest(const QPlaceContentRequest
//      &other)
extern "C" Q_DECL_EXPORT
QPlaceContentRequest *ritual_ZN20QPlaceContentRequestC1ERKS_(
    const QPlaceContentRequest *other) {
  return new QPlaceContentRequest(*other);
}

//  QPlaceContentRequest::~QPlaceContentRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlaceContentRequestD1Ev(QPlaceContentRequest *self) {
  delete self;
}

//  bool operator==(const QPlaceContentRequest &lhs, const
//      QPlaceContentRequest &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QPlaceContentRequestS1_(
    const QPlaceContentRequest *lhs,
    const QPlaceContentRequest *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceContentRequest &lhs, const
//      QPlaceContentRequest &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QPlaceContentRequestS1_(
    const QPlaceContentRequest *lhs,
    const QPlaceContentRequest *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QPlaceContent::Type QPlaceContentRequest::contentType() const
extern "C" Q_DECL_EXPORT
QPlaceContent::Type ritual_ZNK20QPlaceContentRequest11contentTypeEv(
    const QPlaceContentRequest *self) {
  return self->contentType();
}

//  void QPlaceContentRequest::setContentType(QPlaceContent::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlaceContentRequest14setContentTypeEN13QPlaceContent4TypeE(
    QPlaceContentRequest *self,
    QPlaceContent::Type type) {
  self->setContentType(type);
}

//  QString QPlaceContentRequest::placeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QPlaceContentRequest7placeIdEv(
    const QPlaceContentRequest *self) {
  return new QString(self->placeId());
}

//  void QPlaceContentRequest::setPlaceId(const QString &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlaceContentRequest10setPlaceIdERK7QString(
    QPlaceContentRequest *self,
    const QString *identifier) {
  self->setPlaceId(*identifier);
}

//  QVariant QPlaceContentRequest::contentContext() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QPlaceContentRequest14contentContextEv(
    const QPlaceContentRequest *self) {
  return new QVariant(self->contentContext());
}

//  void QPlaceContentRequest::setContentContext(const QVariant &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlaceContentRequest17setContentContextERK8QVariant(
    QPlaceContentRequest *self,
    const QVariant *context) {
  self->setContentContext(*context);
}

//  int QPlaceContentRequest::limit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QPlaceContentRequest5limitEv(
    const QPlaceContentRequest *self) {
  return self->limit();
}

//  void QPlaceContentRequest::setLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlaceContentRequest8setLimitEi(
    QPlaceContentRequest *self,
    int limit) {
  self->setLimit(limit);
}

//  void QPlaceContentRequest::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlaceContentRequest5clearEv(QPlaceContentRequest *self) {
  self->clear();
}

//  bool QPlaceContentRequest::isEqual(const QPlaceContentRequest &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlaceContentRequest7isEqualERKS_(
    const QPlaceContentRequest *self,
    const QPlaceContentRequest *other) {
  return self->isEqual(*other);
}

//  QPlaceContentRequestPrivate *QPlaceContentRequest::d_func()
extern "C" Q_DECL_EXPORT
QPlaceContentRequestPrivate *ritual_ZN20QPlaceContentRequest6d_funcEv(
    QPlaceContentRequest *self) {
  return self->d_func();
}

//  const QPlaceContentRequestPrivate *QPlaceContentRequest::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceContentRequestPrivate *ritual_ZNK20QPlaceContentRequest6d_funcEv(
    const QPlaceContentRequest *self) {
  return self->d_func();
}
