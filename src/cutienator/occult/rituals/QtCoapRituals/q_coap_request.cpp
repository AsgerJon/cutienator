//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/qcoaprequest.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcoaprequest_p.h"
#include <QtCore/qmath.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 287, as _ZN12QCoapRequest6d_funcEv
inline QCoapRequestPrivate* QCoapRequest::d_func()
{
    return static_cast<QCoapRequestPrivate*>(d_ptr.data());
}
//  -----------------------------------------------------------------------

//  QCoapRequest::QCoapRequest(const QUrl &url, Type type, const QUrl
//      &proxyUrl)
extern "C" Q_DECL_EXPORT
QCoapRequest *ritual_ZN12QCoapRequestC1ERK4QUrlN12QCoapMessage4TypeES2_(
    const QUrl *url,
    QCoapMessage::Type type,
    const QUrl *proxyUrl) {
  return new QCoapRequest(*url, type, *proxyUrl);
}

//  QCoapRequest::QCoapRequest(const char *url, Type type)
extern "C" Q_DECL_EXPORT
QCoapRequest *ritual_ZN12QCoapRequestC1EPKcN12QCoapMessage4TypeE(
    const char *url,
    QCoapMessage::Type type) {
  return new QCoapRequest(url, type);
}

//  QCoapRequest::QCoapRequest(const QCoapRequest &other)
extern "C" Q_DECL_EXPORT
QCoapRequest *ritual_ZN12QCoapRequestC1ERKS_(const QCoapRequest *other) {
  return new QCoapRequest(*other);
}

//  QCoapRequest::~QCoapRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapRequestD1Ev(QCoapRequest *self) {
  delete self;
}

//  QUrl QCoapRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QCoapRequest3urlEv(const QCoapRequest *self) {
  return new QUrl(self->url());
}

//  QUrl QCoapRequest::proxyUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QCoapRequest8proxyUrlEv(const QCoapRequest *self) {
  return new QUrl(self->proxyUrl());
}

//  QtCoap::Method QCoapRequest::method() const
extern "C" Q_DECL_EXPORT
QtCoap::Method ritual_ZNK12QCoapRequest6methodEv(const QCoapRequest *self) {
  return self->method();
}

//  bool QCoapRequest::isObserve() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QCoapRequest9isObserveEv(const QCoapRequest *self) {
  return self->isObserve();
}

//  void QCoapRequest::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapRequest6setUrlERK4QUrl(
    QCoapRequest *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  void QCoapRequest::setProxyUrl(const QUrl &proxyUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapRequest11setProxyUrlERK4QUrl(
    QCoapRequest *self,
    const QUrl *proxyUrl) {
  self->setProxyUrl(*proxyUrl);
}

//  void QCoapRequest::enableObserve()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapRequest13enableObserveEv(QCoapRequest *self) {
  self->enableObserve();
}

//  QCoapRequestPrivate *QCoapRequest::d_func()
extern "C" Q_DECL_EXPORT
QCoapRequestPrivate *ritual_ZN12QCoapRequest6d_funcEv(QCoapRequest *self) {
  return self->d_func();
}

//  const QCoapRequestPrivate *QCoapRequest::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapRequestPrivate *ritual_ZNK12QCoapRequest6d_funcEv(
    const QCoapRequest *self) {
  return self->d_func();
}
