//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsockethandshakerequest_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsockethandshakerequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtWebSockets/QWebSocketProtocol>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/private/qwebsockethandshakerequest_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QString>
#include <QtCore/QMap>
#include <QtCore/QTextStream>
#include <QtCore/QUrl>
#include <QtCore/QList>
#include <QtCore/QStringList>
#include <functional>   //for std::greater
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 171, as local:qwebsockethandshakerequest.cpp:readLine
static QByteArrayView readLine(QByteArrayView &header, int maxHeaderLineLength)
{
    qsizetype length = qMin(maxHeaderLineLength, header.size());
    QByteArrayView line = header.first(length);
    qsizetype end = line.indexOf('\n');
    if (end != -1) {
        line = line.first(end);
        if (line.endsWith('\r'))
            line.chop(1);
        header = header.sliced(end + 1);
        return line;
    }
    return QByteArrayView();
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 189, as local:qwebsockethandshakerequest.cpp:appendCommmaSeparatedLineToList
static void appendCommmaSeparatedLineToList(QStringList &list, QByteArrayView line)
{
    for (auto &c : QLatin1String(line).tokenize(QLatin1String(","), Qt::SkipEmptyParts))
        list << c.trimmed().toString();
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 40, as _ZN26QWebSocketHandshakeRequestD1Ev
inline QWebSocketHandshakeRequest::~QWebSocketHandshakeRequest()
{
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 23, as _ZN26QWebSocketHandshakeRequestC1Eib
inline QWebSocketHandshakeRequest::QWebSocketHandshakeRequest(int port, bool isSecure) :
    m_port(port),
    m_isSecure(isSecure),
    m_isValid(false),
    m_parser(),
    m_versions(),
    m_key(),
    m_origin(),
    m_protocols(),
    m_extensions(),
    m_requestUrl()
{
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 48, as _ZN26QWebSocketHandshakeRequest5clearEv
inline void QWebSocketHandshakeRequest::clear()
{
    m_isValid = false;
    m_parser.clear();
    m_versions.clear();
    m_key.clear();
    m_origin.clear();
    m_protocols.clear();
    m_extensions.clear();
    m_requestUrl.clear();
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 63, as _ZNK26QWebSocketHandshakeRequest4portEv
inline int QWebSocketHandshakeRequest::port() const
{
    return m_requestUrl.port(m_port);
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 71, as _ZNK26QWebSocketHandshakeRequest8isSecureEv
inline bool QWebSocketHandshakeRequest::isSecure() const
{
    return m_isSecure;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 79, as _ZNK26QWebSocketHandshakeRequest7isValidEv
inline bool QWebSocketHandshakeRequest::isValid() const
{
    return m_isValid;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 87, as _ZNK26QWebSocketHandshakeRequest7headersEv
inline QHttpHeaders QWebSocketHandshakeRequest::headers() const
{
    return m_parser.headers();
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 95, as _ZNK26QWebSocketHandshakeRequest9hasHeaderERK10QByteArray
inline bool QWebSocketHandshakeRequest::hasHeader(const QByteArray &name) const
{
    return !m_parser.firstHeaderField(name).isEmpty();
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 103, as _ZNK26QWebSocketHandshakeRequest8versionsEv
inline QList<QWebSocketProtocol::Version> QWebSocketHandshakeRequest::versions() const
{
    return m_versions;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 119, as _ZNK26QWebSocketHandshakeRequest3keyEv
inline QString QWebSocketHandshakeRequest::key() const
{
    return m_key;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 135, as _ZNK26QWebSocketHandshakeRequest6originEv
inline QString QWebSocketHandshakeRequest::origin() const
{
    return m_origin;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 143, as _ZNK26QWebSocketHandshakeRequest9protocolsEv
inline QList<QString> QWebSocketHandshakeRequest::protocols() const
{
    return m_protocols;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 151, as _ZNK26QWebSocketHandshakeRequest10extensionsEv
inline QList<QString> QWebSocketHandshakeRequest::extensions() const
{
    return m_extensions;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 159, as _ZNK26QWebSocketHandshakeRequest10requestUrlEv
inline QUrl QWebSocketHandshakeRequest::requestUrl() const
{
    return m_requestUrl;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 111, as _ZNK26QWebSocketHandshakeRequest12resourceNameEv
inline QString QWebSocketHandshakeRequest::resourceName() const
{
    return m_requestUrl.path();
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 127, as _ZNK26QWebSocketHandshakeRequest4hostEv
inline QString QWebSocketHandshakeRequest::host() const
{
    return m_requestUrl.host();
}
//  -----------------------------------------------------------------------

//  QWebSocketHandshakeRequest::QWebSocketHandshakeRequest(int port, bool
//      isSecure)
extern "C" Q_DECL_EXPORT
QWebSocketHandshakeRequest *ritual_ZN26QWebSocketHandshakeRequestC1Eib(
    int port,
    bool isSecure) {
  return new QWebSocketHandshakeRequest(port, isSecure);
}

//  QWebSocketHandshakeRequest::~QWebSocketHandshakeRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebSocketHandshakeRequestD1Ev(
    QWebSocketHandshakeRequest *self) {
  delete self;
}

//  void QWebSocketHandshakeRequest::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebSocketHandshakeRequest5clearEv(
    QWebSocketHandshakeRequest *self) {
  self->clear();
}

//  int QWebSocketHandshakeRequest::port() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QWebSocketHandshakeRequest4portEv(
    const QWebSocketHandshakeRequest *self) {
  return self->port();
}

//  bool QWebSocketHandshakeRequest::isSecure() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWebSocketHandshakeRequest8isSecureEv(
    const QWebSocketHandshakeRequest *self) {
  return self->isSecure();
}

//  bool QWebSocketHandshakeRequest::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWebSocketHandshakeRequest7isValidEv(
    const QWebSocketHandshakeRequest *self) {
  return self->isValid();
}

//  QHttpHeaders QWebSocketHandshakeRequest::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK26QWebSocketHandshakeRequest7headersEv(
    const QWebSocketHandshakeRequest *self) {
  return new QHttpHeaders(self->headers());
}

//  bool QWebSocketHandshakeRequest::hasHeader(const QByteArray &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWebSocketHandshakeRequest9hasHeaderERK10QByteArray(
    const QWebSocketHandshakeRequest *self,
    const QByteArray *name) {
  return self->hasHeader(*name);
}

//  QList<QWebSocketProtocol::Version> QWebSocketHandshakeRequest::versions()
//      const
extern "C" Q_DECL_EXPORT
QList<QWebSocketProtocol::Version> *ritual_ZNK26QWebSocketHandshakeRequest8versionsEv(
    const QWebSocketHandshakeRequest *self) {
  return new QList<QWebSocketProtocol::Version>(self->versions());
}

//  QString QWebSocketHandshakeRequest::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QWebSocketHandshakeRequest3keyEv(
    const QWebSocketHandshakeRequest *self) {
  return new QString(self->key());
}

//  QString QWebSocketHandshakeRequest::origin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QWebSocketHandshakeRequest6originEv(
    const QWebSocketHandshakeRequest *self) {
  return new QString(self->origin());
}

//  QList<QString> QWebSocketHandshakeRequest::protocols() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QWebSocketHandshakeRequest9protocolsEv(
    const QWebSocketHandshakeRequest *self) {
  return new QList<QString>(self->protocols());
}

//  QList<QString> QWebSocketHandshakeRequest::extensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QWebSocketHandshakeRequest10extensionsEv(
    const QWebSocketHandshakeRequest *self) {
  return new QList<QString>(self->extensions());
}

//  QUrl QWebSocketHandshakeRequest::requestUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK26QWebSocketHandshakeRequest10requestUrlEv(
    const QWebSocketHandshakeRequest *self) {
  return new QUrl(self->requestUrl());
}

//  QString QWebSocketHandshakeRequest::resourceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QWebSocketHandshakeRequest12resourceNameEv(
    const QWebSocketHandshakeRequest *self) {
  return new QString(self->resourceName());
}

//  QString QWebSocketHandshakeRequest::host() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QWebSocketHandshakeRequest4hostEv(
    const QWebSocketHandshakeRequest *self) {
  return new QString(self->host());
}

//  a QList<QWebSocketProtocol::Version> a ritual of
//      QWebSocketHandshakeRequest gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWebSocketHandshakeRequest__QList_QWebSocketProtocol_Version(
    QList<QWebSocketProtocol::Version> *self) {
  delete self;
}
