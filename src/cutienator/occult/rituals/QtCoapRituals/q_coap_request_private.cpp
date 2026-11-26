//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoaprequest_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoaprequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCoap/qcoaprequest.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtCoap/private/qcoaprequest_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 18, as local:qcoaprequest.cpp:CoapScheme
namespace {
const auto CoapScheme = QLatin1String("coap");
}  // namespace

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 19, as local:qcoaprequest.cpp:CoapSecureScheme
namespace {
const auto CoapSecureScheme = QLatin1String("coaps");
}  // namespace

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 14, as _Z14lcCoapExchangev
inline const QLoggingCategory &lcCoapExchange()
{
    static const QLoggingCategory category("qt.coap.exchange");
    return category;
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 254, as _ZN19QCoapRequestPrivate11adjustedUrlERK4QUrlb
inline QUrl QCoapRequestPrivate::adjustedUrl(const QUrl &url, bool secure)
{
    if (url.isEmpty() || !url.isValid())
        return QUrl();

    QUrl finalizedUrl = url;
    const auto scheme = secure ? CoapSecureScheme : CoapScheme;
    if (url.host().isEmpty() && url.isRelative()) {
        // In some cases host address is mistaken for part of the relative path,
        // prepending the scheme fixes this.
        finalizedUrl = QUrl{scheme + "://"_L1 + url.toString()};
    } else if (url.scheme().isEmpty()) {
        finalizedUrl.setScheme(scheme);
    }

    if (finalizedUrl.host().isEmpty()) {
        qCWarning(lcCoapExchange) << "The requested URL" << url << "is not a valid CoAP URL.";
        return QUrl();
    }

    if (url.port() == -1) {
        const auto port = secure ? QtCoap::DefaultSecurePort : QtCoap::DefaultPort;
        finalizedUrl.setPort(port);
    }

    return finalizedUrl;
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 287, as _ZN12QCoapRequest6d_funcEv
inline QCoapRequestPrivate* QCoapRequest::d_func()
{
    return static_cast<QCoapRequestPrivate*>(d_ptr.data());
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 34, as _ZNK19QCoapRequestPrivate5cloneEv
inline QCoapRequestPrivate *QCoapRequestPrivate::clone() const
{
    return new QCoapRequestPrivate(*this);
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 30, as _ZN19QCoapRequestPrivateD1Ev
inline QCoapRequestPrivate::~QCoapRequestPrivate()
{
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 44, as _ZN19QCoapRequestPrivate6setUrlERK4QUrl
inline void QCoapRequestPrivate::setUrl(const QUrl &url)
{
    // Print no warning when clearing URL
    if (url.isEmpty()) {
        uri = url;
        return;
    }

    // Make first checks before editing the URL, to avoid editing it
    // in a wrong way (e.g. when adding the scheme)
    if (!url.isValid()) {
        qCWarning(lcCoapExchange) << "Invalid CoAP url" << url.toString();
        return;
    }

    // If the port is unknown, try to set it based on scheme
    QUrl finalizedUrl = url;
    if (!url.scheme().isEmpty()) {
        if (url.scheme() == CoapScheme) {
            if (url.port() == -1)
                finalizedUrl.setPort(QtCoap::DefaultPort);
        } else if (url.scheme() == CoapSecureScheme) {
            if (url.port() == -1)
                finalizedUrl.setPort(QtCoap::DefaultSecurePort);
        } else {
            qCWarning(lcCoapExchange) << "QCoapRequest: Request URL's scheme" << url.scheme()
                                      << "isn't valid for CoAP";
            return;
        }
    }

    uri = finalizedUrl;
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 217, as _ZN19QCoapRequestPrivate9adjustUrlEb
inline void QCoapRequestPrivate::adjustUrl(bool secure)
{
    uri = adjustedUrl(uri, secure);
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 298, as _ZN19QCoapRequestPrivate13createRequestERK12QCoapRequestN6QtCoap6MethodEb
inline QCoapRequest
QCoapRequestPrivate::createRequest(const QCoapRequest &other, QtCoap::Method method, bool isSecure)
{
    QCoapRequest request(other);
    request.d_func()->method = method;
    request.d_func()->adjustUrl(isSecure);
    return request;
}
//  -----------------------------------------------------------------------

//  A QCoapRequestPrivate that Python can take functions over in. Every QCoapRequestPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCoapRequestPrivateCall0)(const void *, int *);
class CuteQCoapRequestPrivate : public QCoapRequestPrivate {
public:
  using QCoapRequestPrivate::QCoapRequestPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QCoapMessagePrivate5cloneEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QCoapRequestPrivate *QCoapRequestPrivate::clone() const
  QCoapRequestPrivate *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapRequestPrivateCall0 call = reinterpret_cast<CuteQCoapRequestPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCoapRequestPrivate *>(given);
    }
    return QCoapRequestPrivate::clone();
  }
};

//  QCoapRequestPrivate::~QCoapRequestPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapRequestPrivateD1Ev(QCoapRequestPrivate *self) {
  delete self;
}

//  QCoapRequestPrivate *QCoapRequestPrivate::clone() const
extern "C" Q_DECL_EXPORT
QCoapRequestPrivate *ritual_ZNK19QCoapRequestPrivate5cloneEv(
    const QCoapRequestPrivate *self) {
  return self->clone();
}

//  void QCoapRequestPrivate::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapRequestPrivate6setUrlERK4QUrl(
    QCoapRequestPrivate *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  void QCoapRequestPrivate::adjustUrl(bool secure)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapRequestPrivate9adjustUrlEb(
    QCoapRequestPrivate *self,
    bool secure) {
  self->adjustUrl(secure);
}

//  QCoapRequest QCoapRequestPrivate::createRequest(const QCoapRequest
//      &other, QtCoap::Method method, bool isSecure)
extern "C" Q_DECL_EXPORT
QCoapRequest *ritual_ZN19QCoapRequestPrivate13createRequestERK12QCoapRequestN6QtCoap6MethodEb(
    const QCoapRequest *other,
    QtCoap::Method method,
    bool isSecure) {
  return new QCoapRequest(
      QCoapRequestPrivate::createRequest(
          *other,
          method,
          isSecure));
}

//  a Python function taken by a CuteQCoapRequestPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapRequestPrivate(
    QCoapRequestPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapRequestPrivate *>(self)->take(key, call);
}
