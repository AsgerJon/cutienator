//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkheader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if (defined(Q_OS_WASM)) || (QT_CONFIG(http))
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkheader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhttpnetworkheader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhttpnetworkheader.cpp, line 12, as _ZN25QHttpNetworkHeaderPrivateC1ERK4QUrl
inline QHttpNetworkHeaderPrivate::QHttpNetworkHeaderPrivate(const QUrl &newUrl)
    :url(newUrl)
{
}

//  from src/network/access/qhttpnetworkheader.cpp, line 17, as _ZNK25QHttpNetworkHeaderPrivate13contentLengthEv
inline qint64 QHttpNetworkHeaderPrivate::contentLength() const
{
    bool ok = false;
    // We are not using the headerField() method here because servers might send us multiple content-length
    // headers which is crap (see QTBUG-15311). Therefore just take the first content-length header field.
    QByteArray value = parser.firstHeaderField("content-length");
    qint64 length = value.toULongLong(&ok);
    if (ok)
        return length;
    return -1; // the header field is not set
}

//  from src/network/access/qhttpnetworkheader.cpp, line 29, as _ZN25QHttpNetworkHeaderPrivate16setContentLengthEx
inline void QHttpNetworkHeaderPrivate::setContentLength(qint64 length)
{
    setHeaderField("Content-Length", QByteArray::number(length));
}

//  from src/network/access/qhttpnetworkheader.cpp, line 34, as _ZNK25QHttpNetworkHeaderPrivate11headerFieldE14QByteArrayViewRK10QByteArray
inline QByteArray QHttpNetworkHeaderPrivate::headerField(QByteArrayView name, const QByteArray &defaultValue) const
{
    QList<QByteArray> allValues = headerFieldValues(name);
    if (allValues.isEmpty())
        return defaultValue;
    else
        return allValues.join(", ");
}

//  from src/network/access/qhttpnetworkheader.cpp, line 43, as _ZNK25QHttpNetworkHeaderPrivate17headerFieldValuesE14QByteArrayView
inline QList<QByteArray> QHttpNetworkHeaderPrivate::headerFieldValues(QByteArrayView name) const
{
    return parser.headerFieldValues(name);
}

//  from src/network/access/qhttpnetworkheader.cpp, line 48, as _ZN25QHttpNetworkHeaderPrivate14setHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkHeaderPrivate::setHeaderField(const QByteArray &name, const QByteArray &data)
{
    parser.setHeaderField(name, data);
}

//  from src/network/access/qhttpnetworkheader.cpp, line 53, as _ZN25QHttpNetworkHeaderPrivate18prependHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkHeaderPrivate::prependHeaderField(const QByteArray &name, const QByteArray &data)
{
    parser.prependHeaderField(name, data);
}

//  from src/network/access/qhttpnetworkheader.cpp, line 63, as _ZN25QHttpNetworkHeaderPrivate12clearHeadersEv
inline void QHttpNetworkHeaderPrivate::clearHeaders()
{
    parser.clearHeaders();
}

//  from src/network/access/qhttpnetworkheader.cpp, line 58, as _ZNK25QHttpNetworkHeaderPrivate7headersEv
inline QHttpHeaders QHttpNetworkHeaderPrivate::headers() const
{
    return parser.headers();
}
//  -----------------------------------------------------------------------

//  QHttpNetworkHeaderPrivate::QHttpNetworkHeaderPrivate(const QUrl &newUrl)
extern "C" Q_DECL_EXPORT
QHttpNetworkHeaderPrivate *ritual_ZN25QHttpNetworkHeaderPrivateC1ERK4QUrl(
    const QUrl *newUrl) {
  return new QHttpNetworkHeaderPrivate(*newUrl);
}

//  QHttpNetworkHeaderPrivate::QHttpNetworkHeaderPrivate(const
//      QHttpNetworkHeaderPrivate &other)
extern "C" Q_DECL_EXPORT
QHttpNetworkHeaderPrivate *ritual_ZN25QHttpNetworkHeaderPrivateC1ERKS_(
    const QHttpNetworkHeaderPrivate *other) {
  return new QHttpNetworkHeaderPrivate(*other);
}

//  qint64 QHttpNetworkHeaderPrivate::contentLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK25QHttpNetworkHeaderPrivate13contentLengthEv(
    const QHttpNetworkHeaderPrivate *self) {
  return self->contentLength();
}

//  void QHttpNetworkHeaderPrivate::setContentLength(qint64 length)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QHttpNetworkHeaderPrivate16setContentLengthEx(
    QHttpNetworkHeaderPrivate *self,
    qint64 length) {
  self->setContentLength(length);
}

//  QByteArray QHttpNetworkHeaderPrivate::headerField(QByteArrayView name,
//      const QByteArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK25QHttpNetworkHeaderPrivate11headerFieldE14QByteArrayViewRK10QByteArray(
    const QHttpNetworkHeaderPrivate *self,
    const QByteArrayView *name,
    const QByteArray *defaultValue) {
  return new QByteArray(self->headerField(*name, *defaultValue));
}

//  QList<QByteArray>
//      QHttpNetworkHeaderPrivate::headerFieldValues(QByteArrayView name)
//      const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK25QHttpNetworkHeaderPrivate17headerFieldValuesE14QByteArrayView(
    const QHttpNetworkHeaderPrivate *self,
    const QByteArrayView *name) {
  return new QList<QByteArray>(self->headerFieldValues(*name));
}

//  void QHttpNetworkHeaderPrivate::setHeaderField(const QByteArray &name,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QHttpNetworkHeaderPrivate14setHeaderFieldERK10QByteArrayS2_(
    QHttpNetworkHeaderPrivate *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->setHeaderField(*name, *data);
}

//  void QHttpNetworkHeaderPrivate::prependHeaderField(const QByteArray
//      &name, const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QHttpNetworkHeaderPrivate18prependHeaderFieldERK10QByteArrayS2_(
    QHttpNetworkHeaderPrivate *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->prependHeaderField(*name, *data);
}

//  void QHttpNetworkHeaderPrivate::clearHeaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QHttpNetworkHeaderPrivate12clearHeadersEv(
    QHttpNetworkHeaderPrivate *self) {
  self->clearHeaders();
}

//  QHttpHeaders QHttpNetworkHeaderPrivate::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK25QHttpNetworkHeaderPrivate7headersEv(
    const QHttpNetworkHeaderPrivate *self) {
  return new QHttpHeaders(self->headers());
}

//  QHttpNetworkHeaderPrivate::~QHttpNetworkHeaderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QHttpNetworkHeaderPrivateD1Ev(
    QHttpNetworkHeaderPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
#endif  // (defined(Q_OS_WASM)) || (QT_CONFIG(http))
