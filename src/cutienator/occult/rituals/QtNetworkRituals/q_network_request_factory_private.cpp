//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkrequestfactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkrequestfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtNetwork/qnetworkrequest.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkrequestfactory.h>
#include <QtNetwork/private/qnetworkrequestfactory_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslconfiguration.h>
#endif
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmap.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qnetworkrequestfactory.cpp, line 599, as _ZN29QNetworkRequestFactoryPrivateC1ERK4QUrl
inline QNetworkRequestFactoryPrivate::QNetworkRequestFactoryPrivate(const QUrl &baseUrl)
    : baseUrl(baseUrl)
{
}

//  from src/network/access/qnetworkrequestfactory.cpp, line 604, as _ZNK29QNetworkRequestFactoryPrivate10newRequestERK4QUrl
inline QNetworkRequest QNetworkRequestFactoryPrivate::newRequest(const QUrl &url) const
{
    QNetworkRequest request;
    request.setUrl(url);
#if QT_CONFIG(ssl)
    if (!sslConfig.isNull())
        request.setSslConfiguration(sslConfig);
#endif
    auto h = headers;
    constexpr char Bearer[] = "Bearer ";
    if (!bearerToken.isEmpty())
        h.replaceOrAppend(QHttpHeaders::WellKnownHeader::Authorization, Bearer + bearerToken);
    request.setHeaders(std::move(h));

    request.setTransferTimeout(transferTimeout);
    request.setPriority(priority);

    for (const auto &[attribute, value] : attributes.asKeyValueRange())
        request.setAttribute(attribute, value);

    return request;
}
//  -----------------------------------------------------------------------

//  QNetworkRequestFactoryPrivate::QNetworkRequestFactoryPrivate(const QUrl
//      &baseUrl)
extern "C" Q_DECL_EXPORT
QNetworkRequestFactoryPrivate *ritual_ZN29QNetworkRequestFactoryPrivateC1ERK4QUrl(
    const QUrl *baseUrl) {
  return new QNetworkRequestFactoryPrivate(*baseUrl);
}

//  QNetworkRequest QNetworkRequestFactoryPrivate::newRequest(const QUrl
//      &url) const
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZNK29QNetworkRequestFactoryPrivate10newRequestERK4QUrl(
    const QNetworkRequestFactoryPrivate *self,
    const QUrl *url) {
  return new QNetworkRequest(self->newRequest(*url));
}

//  QNetworkRequestFactoryPrivate::~QNetworkRequestFactoryPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QNetworkRequestFactoryPrivateD1Ev(
    QNetworkRequestFactoryPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
