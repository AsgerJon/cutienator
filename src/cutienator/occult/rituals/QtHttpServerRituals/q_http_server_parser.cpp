//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverparser_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/private/qhttpserverrequest_p.h>
#include <QtHttpServer/private/qhttpserverparser_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/qhttpheaders.h>
#if QT_CONFIG(http)
#include <QtNetwork/private/qhttp2connection_p.h>
#endif
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 23, as local:qhttpserverparser.cpp:parseRequestMethod
namespace {
inline QHttpServerRequest::Method parseRequestMethod(QByteArrayView str)
{
    if (str == "GET")
        return QHttpServerRequest::Method::Get;
    else if (str == "PUT")
        return QHttpServerRequest::Method::Put;
    else if (str == "DELETE")
        return QHttpServerRequest::Method::Delete;
    else if (str == "POST")
        return QHttpServerRequest::Method::Post;
    else if (str == "HEAD")
        return QHttpServerRequest::Method::Head;
    else if (str == "OPTIONS")
        return QHttpServerRequest::Method::Options;
    else if (str == "PATCH")
        return QHttpServerRequest::Method::Patch;
    else if (str == "CONNECT")
        return QHttpServerRequest::Method::Connect;
    else
        return QHttpServerRequest::Method::Unknown;
}
}  // namespace

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 45, as local:qhttpserverparser.cpp:getErrorString
namespace {
inline const char* getErrorString(QHttpServerResponder::StatusCode code)
{
    switch (code) {
    case QHttpServerResponder::StatusCode::PayloadTooLarge:
        return "Request Entity Too Large";
    case QHttpServerResponder::StatusCode::UriTooLong:
        return "Request-URI Too Long";
    case QHttpServerResponder::StatusCode::RequestHeaderFieldsTooLarge:
        return "Request Header Fields Too Large";
    default:
        return "Bad Request";
    };
}
}  // namespace

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 351, as _ZN17QHttpServerParserC1ERK12QHostAddresstS2_tP24QHttpServerRequestFilter
inline QHttpServerParser::QHttpServerParser(const QHostAddress &remoteAddress, quint16 remotePort,
                                     const QHostAddress &localAddress, quint16 localPort,
                                     QHttpServerRequestFilter *filter)
    : remoteAddress(remoteAddress),
      remotePort(remotePort),
      localAddress(localAddress),
      localPort(localPort),
      filter(filter)
{
    clear();
    headerParser.setMaxHeaderFieldSize(std::numeric_limits<qsizetype>::max());
    headerParser.setMaxTotalHeaderSize(std::numeric_limits<qsizetype>::max());
    headerParser.setMaxHeaderFields(std::numeric_limits<qsizetype>::max());
}

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 64, as _ZN17QHttpServerParser16parseRequestLineE14QByteArrayView
inline bool QHttpServerParser::parseRequestLine(QByteArrayView line)
{
    // Request-Line   = Method SP Request-URI SP HTTP-Version CRLF
    auto i = line.indexOf(' ');
    if (i == -1)
        return false;
    const auto requestMethod = line.first(i);
    i++;

    while (i < line.size() && line[i] == ' ')
        i++;

    auto j = line.indexOf(' ', i);
    if (j == -1)
        return false;

    const auto requestUrl = line.sliced(i, j - i);
    i = j + 1;

    while (i < line.size() && line[i] == ' ')
        i++;

    if (i >= line.size())
        return false;

    j = line.indexOf(' ', i);

    const auto protocol = j == -1 ? line.sliced(i) : line.sliced(i, j - i);
    if (protocol.size() != 8 || !protocol.startsWith("HTTP"))
        return false;

    headerParser.setMajorVersion(protocol[5] - '0');
    headerParser.setMinorVersion(protocol[7] - '0');
    majorVersion = protocol[5] - '0';
    minorVersion = protocol[7] - '0';

    method = parseRequestMethod(requestMethod);
    url = QUrl::fromEncoded(requestUrl.toByteArray());
    return true;
}

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 341, as _ZN17QHttpServerParser12sendContinueEP9QIODevice
inline qsizetype QHttpServerParser::sendContinue(QIODevice *socket)
{
    qsizetype ret = socket->write("HTTP/1.1 100 Continue\r\n\r\n");
    state = State::ReadingData;
    return ret;
}

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 483, as _ZN17QHttpServerParser12readBodyFastEP9QIODevice
inline qsizetype QHttpServerParser::readBodyFast(QIODevice *socket)
{

    qsizetype toBeRead = qMin(socket->bytesAvailable(), bodyLength - contentRead);
    if (!toBeRead)
        return 0;

    QByteArray bd;
    bd.resize(toBeRead);
    qsizetype haveRead = socket->read(bd.data(), toBeRead);
    if (haveRead == -1) {
        bd.clear();
        return 0; // ### error checking here;
    }
    bd.resize(haveRead);

    bodyBuffer.append(bd);

    contentRead += haveRead;

    if (contentRead == bodyLength)
        state = State::AllDone;

    return haveRead;
}

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 512, as _ZN17QHttpServerParser18readRequestBodyRawEP9QIODevicex
inline qsizetype QHttpServerParser::readRequestBodyRaw(QIODevice *socket, qsizetype size)
{
    // FIXME get rid of this function and just use readBodyFast and give it socket->bytesAvailable()
    qsizetype bytes = 0;
    Q_ASSERT(socket);

    int toBeRead = qMin<qsizetype>(128 * 1024, qMin<qint64>(size, socket->bytesAvailable()));

    while (toBeRead > 0) {
        QByteArray byteData;
        byteData.resize(toBeRead);
        qsizetype haveRead = socket->read(byteData.data(), byteData.size());
        if (haveRead <= 0) {
            // ### error checking here
            byteData.clear();
            return bytes;
        }

        byteData.resize(haveRead);
        bodyBuffer.append(byteData);
        bytes += haveRead;
        size -= haveRead;

        toBeRead = qMin<qsizetype>(128 * 1024, qMin<qsizetype>(size, socket->bytesAvailable()));
    }
    return bytes;
}

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 613, as _ZN17QHttpServerParser12getChunkSizeEP9QIODevicePx
inline qsizetype QHttpServerParser::getChunkSize(QIODevice *socket, qsizetype *chunkSize)
{
    qsizetype bytes = 0;
    char crlf[2];
    *chunkSize = -1;

    int bytesAvailable = socket->bytesAvailable();
    // FIXME rewrite to permanent loop without bytesAvailable
    while (bytesAvailable > bytes) {
        qsizetype sniffedBytes = socket->peek(crlf, 2);
        int fragmentSize = fragment.size();

        // check the next two bytes for a "\r\n", skip blank lines
        if ((fragmentSize && sniffedBytes == 2 && crlf[0] == '\r' && crlf[1] == '\n')
            || (fragmentSize > 1 && fragment.endsWith('\r') && crlf[0] == '\n')) {
            bytes += socket->read(crlf, 1); // read the \r or \n
            if (crlf[0] == '\r')
                bytes += socket->read(crlf, 1); // read the \n
            bool ok = false;
            // ignore the chunk-extension
            fragment = fragment.mid(0, fragment.indexOf(';')).trimmed();
            *chunkSize = fragment.toLong(&ok, 16);
            fragment.clear();
            break; // size done
        } else {
            // read the fragment to the buffer
            char c = 0;
            qsizetype haveRead = socket->read(&c, 1);
            if (haveRead < 0)
                return -1;

            bytes += haveRead;
            fragment.append(c);
        }
    }

    return bytes;
}

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 186, as _ZN17QHttpServerParser9sendErrorEP9QIODeviceN20QHttpServerResponder10StatusCodeE
inline void QHttpServerParser::sendError(QIODevice *socket, QHttpServerResponder::StatusCode error)
{
    QByteArray buffer;
    buffer.append("HTTP/1.1 ");
    buffer.append(QByteArray::number(int(error)));
    buffer.append(" ");
    buffer.append(getErrorString(error));
    buffer.append("\r\nConnection: close\r\n\r\n");
    socket->write(buffer);
}

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 161, as _ZN17QHttpServerParser16isUrlSizeAllowedE14QByteArrayView
inline bool QHttpServerParser::isUrlSizeAllowed(QByteArrayView requestLine)
{
    if (filter->isUrlSizeAllowed(requestLine.size()))
        return true; // Succeed if entire request line is not too long

    // Request-Line   = Method SP Request-URI SP HTTP-Version CRLF
    constexpr qsizetype shortestCaseExtraCharacters = 3 + 1 + 1 + 8 + 2;
    if (!filter->isUrlSizeAllowed(requestLine.size() - shortestCaseExtraCharacters))
        return false;

    qsizetype firstSpace = requestLine.indexOf(' ');
    if (firstSpace < 0)
        return false; // First space not read yet

    qsizetype uriStart = firstSpace;
    while (uriStart < requestLine.size() && requestLine[uriStart] == ' ')
        uriStart++;

    qsizetype secondSpace = requestLine.indexOf(' ', uriStart);
    if (secondSpace < 0)
        secondSpace = requestLine.size(); // Second space not read yet

    return filter->isUrlSizeAllowed(secondSpace - uriStart);
}

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 454, as _ZN17QHttpServerParser5clearEv
inline void QHttpServerParser::clear()
{
    headerParser.clear();
    bodyLength = -1;
    contentRead = 0;
    chunkedTransferEncoding = false;
    lastChunkRead = false;
    currentChunkRead = 0;
    currentChunkSize = 0;
    upgrade = false;
    majorVersion = 0;
    minorVersion = 0;

    fragment.clear();
    bodyBuffer.clear();

    url.clear();
    method = QHttpServerRequest::Method::Unknown;
    headers.clear();
    body.clear();
}

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 200, as _ZNK17QHttpServerParser13contentLengthEv
inline qint64 QHttpServerParser::contentLength() const
{
    bool ok = false;
    QByteArray value = headerParser.firstHeaderField("content-length");
    qint64 length = value.toULongLong(&ok);
    if (ok)
        return length;
    return -1; // the header field is not set
}

//  from ../qthttpserver/src/httpserver/qhttpserverparser.cpp, line 655, as _ZNK17QHttpServerParser25getClientIpAddressAndPortEv
inline QString QHttpServerParser::getClientIpAddressAndPort() const
{
    using namespace Qt::StringLiterals;
    QString result;
    if (remoteAddress.protocol() != QAbstractSocket::IPv4Protocol)
        result.append(u"["_s);
    result.append(remoteAddress.toString());
    if (remoteAddress.protocol() != QAbstractSocket::IPv4Protocol)
        result.append(u"]"_s);
    result.append(u":"_s);
    result.append(QString::number(remotePort));
    return result;
}
//  -----------------------------------------------------------------------

//  QHttpServerParser::QHttpServerParser(const QHostAddress &remoteAddress,
//      quint16 remotePort, const QHostAddress &localAddress, quint16
//      localPort, QHttpServerRequestFilter *filter)
extern "C" Q_DECL_EXPORT
QHttpServerParser *ritual_ZN17QHttpServerParserC1ERK12QHostAddresstS2_tP24QHttpServerRequestFilter(
    const QHostAddress *remoteAddress,
    quint16 remotePort,
    const QHostAddress *localAddress,
    quint16 localPort,
    QHttpServerRequestFilter *filter) {
  return new QHttpServerParser(
      *remoteAddress,
      remotePort,
      *localAddress,
      localPort,
      filter);
}

//  bool QHttpServerParser::parseRequestLine(QByteArrayView line)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpServerParser16parseRequestLineE14QByteArrayView(
    QHttpServerParser *self,
    const QByteArrayView *line) {
  return self->parseRequestLine(*line);
}

//  qsizetype QHttpServerParser::sendContinue(QIODevice *socket)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN17QHttpServerParser12sendContinueEP9QIODevice(
    QHttpServerParser *self,
    QIODevice *socket) {
  return self->sendContinue(socket);
}

//  qsizetype QHttpServerParser::readBodyFast(QIODevice *socket)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN17QHttpServerParser12readBodyFastEP9QIODevice(
    QHttpServerParser *self,
    QIODevice *socket) {
  return self->readBodyFast(socket);
}

//  qsizetype QHttpServerParser::readRequestBodyRaw(QIODevice *socket,
//      qsizetype size)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN17QHttpServerParser18readRequestBodyRawEP9QIODevicex(
    QHttpServerParser *self,
    QIODevice *socket,
    qsizetype size) {
  return self->readRequestBodyRaw(socket, size);
}

//  qsizetype QHttpServerParser::getChunkSize(QIODevice *socket, qsizetype
//      *chunkSize)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN17QHttpServerParser12getChunkSizeEP9QIODevicePx(
    QHttpServerParser *self,
    QIODevice *socket,
    qsizetype *chunkSize) {
  return self->getChunkSize(socket, chunkSize);
}

//  void QHttpServerParser::sendError(QIODevice *socket,
//      QHttpServerResponder::StatusCode error)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerParser9sendErrorEP9QIODeviceN20QHttpServerResponder10StatusCodeE(
    QHttpServerParser *self,
    QIODevice *socket,
    QHttpServerResponder::StatusCode error) {
  self->sendError(socket, error);
}

//  bool QHttpServerParser::isUrlSizeAllowed(QByteArrayView requestLine)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpServerParser16isUrlSizeAllowedE14QByteArrayView(
    QHttpServerParser *self,
    const QByteArrayView *requestLine) {
  return self->isUrlSizeAllowed(*requestLine);
}

//  void QHttpServerParser::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerParser5clearEv(QHttpServerParser *self) {
  self->clear();
}

//  qint64 QHttpServerParser::contentLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QHttpServerParser13contentLengthEv(
    const QHttpServerParser *self) {
  return self->contentLength();
}

//  QByteArray QHttpServerParser::headerField(const QByteArray &name) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QHttpServerParser11headerFieldERK10QByteArray(
    const QHttpServerParser *self,
    const QByteArray *name) {
  return new QByteArray(self->headerField(*name));
}

//  QString QHttpServerParser::getClientIpAddressAndPort() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QHttpServerParser25getClientIpAddressAndPortEv(
    const QHttpServerParser *self) {
  return new QString(self->getClientIpAddressAndPort());
}

//  QHttpServerParser::~QHttpServerParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerParserD1Ev(QHttpServerParser *self) {
  delete self;
}
