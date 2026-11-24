//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkreply_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkreply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhttpnetworkheader_p.h"
#include "qhttpnetworkrequest_p.h"
#include "private/qnoncontiguousbytedevice_p.h"
#include <QtCore/private/qtools_p.h>
#include "qhttpnetworkreply_p.h"
#include "qhttpnetworkconnection_p.h"
#ifndef QT_NO_SSL
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#    include <QtNetwork/qsslconfiguration.h>
#endif
#include <private/qdecompresshelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhttpnetworkheader.cpp, line 34, as _ZNK25QHttpNetworkHeaderPrivate11headerFieldE14QByteArrayViewRK10QByteArray
inline QByteArray QHttpNetworkHeaderPrivate::headerField(QByteArrayView name, const QByteArray &defaultValue) const
{
    QList<QByteArray> allValues = headerFieldValues(name);
    if (allValues.isEmpty())
        return defaultValue;
    else
        return allValues.join(", ");
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

//  from src/network/access/qhttpnetworkrequest.cpp, line 219, as _ZNK19QHttpNetworkRequest17isFollowRedirectsEv
inline bool QHttpNetworkRequest::isFollowRedirects() const
{
    return d->redirectPolicy != QNetworkRequest::ManualRedirectPolicy;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 291, as _ZNK19QHttpNetworkRequest9operationEv
inline QHttpNetworkRequest::Operation QHttpNetworkRequest::operation() const
{
    return d->operation;
}

//  from src/network/access/qhttpnetworkheader.cpp, line 43, as _ZNK25QHttpNetworkHeaderPrivate17headerFieldValuesE14QByteArrayView
inline QList<QByteArray> QHttpNetworkHeaderPrivate::headerFieldValues(QByteArrayView name) const
{
    return parser.headerFieldValues(name);
}

//  from src/network/access/qhttpnetworkreply.cpp, line 382, as _ZN24QHttpNetworkReplyPrivate10readStatusEP9QIODevice
inline qint64 QHttpNetworkReplyPrivate::readStatus(QIODevice *socket)
{
    if (fragment.isEmpty()) {
        // reserve bytes for the status line. This is better than always append() which reallocs the byte array
        fragment.reserve(32);
    }

    qint64 bytes = 0;
    char c;
    qint64 haveRead = 0;

    do {
        haveRead = socket->read(&c, 1);
        if (haveRead == -1)
            return -1; // unexpected EOF
        else if (haveRead == 0)
            break; // read more later
        else if (haveRead == 1 && fragment.size() == 0 && (c == 11 || c == '\n' || c == '\r' || c == ' ' || c == 31))
            continue; // Ignore all whitespace that was trailing froma previous request on that socket

        bytes++;

        // allow both CRLF & LF (only) line endings
        if (c == '\n') {
            // remove the CR at the end
            if (fragment.endsWith('\r')) {
                fragment.truncate(fragment.size()-1);
            }
            bool ok = parseStatus(fragment);
            state = ReadingHeaderState;
            fragment.clear();
            if (!ok) {
                return -1;
            }
            break;
        } else {
            fragment.append(c);
        }

        // is this a valid reply?
        if (fragment.size() == 5 && !fragment.startsWith("HTTP/")) {
            fragment.clear();
            return -1;
        }
    } while (haveRead == 1);

    return bytes;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 431, as _ZN24QHttpNetworkReplyPrivate11parseStatusE14QByteArrayView
inline bool QHttpNetworkReplyPrivate::parseStatus(QByteArrayView status)
{
    return parser.parseStatus(status);
}

//  from src/network/access/qhttpnetworkreply.cpp, line 436, as _ZN24QHttpNetworkReplyPrivate10readHeaderEP9QIODevice
inline qint64 QHttpNetworkReplyPrivate::readHeader(QIODevice *socket)
{
    if (fragment.isEmpty()) {
        // according to http://dev.opera.com/articles/view/mama-http-headers/ the average size of the header
        // block is 381 bytes.
        // reserve bytes. This is better than always append() which reallocs the byte array.
        fragment.reserve(512);
    }

    qint64 bytes = 0;
    char c = 0;
    bool allHeaders = false;
    qint64 haveRead = 0;
    do {
        haveRead = socket->read(&c, 1);
        if (haveRead == 0) {
            // read more later
            break;
        } else if (haveRead == -1) {
            // connection broke down
            return -1;
        } else {
            fragment.append(c);
            bytes++;

            if (c == '\n') {
                // check for possible header endings. As per HTTP rfc,
                // the header endings will be marked by CRLFCRLF. But
                // we will allow CRLFCRLF, CRLFLF, LFCRLF, LFLF
                if (fragment.endsWith("\n\r\n")
                    || fragment.endsWith("\n\n"))
                    allHeaders = true;

                // there is another case: We have no headers. Then the fragment equals just the line ending
                if ((fragment.size() == 2 && fragment.endsWith("\r\n"))
                    || (fragment.size() == 1 && fragment.endsWith("\n")))
                    allHeaders = true;
            }
        }
    } while (!allHeaders && haveRead > 0);

    // we received all headers now parse them
    if (allHeaders) {
        parseHeader(fragment);
        state = ReadingDataState;
        fragment.clear(); // next fragment
        bodyLength = contentLength(); // cache the length

        // cache isChunked() since it is called often
        chunkedTransferEncoding = headerField("transfer-encoding").toLower().contains("chunked");

        // cache isConnectionCloseEnabled since it is called often
        QByteArray connectionHeaderField = headerField("connection");
        // check for explicit indication of close or the implicit connection close of HTTP/1.0
        connectionCloseEnabled = (connectionHeaderField.toLower().contains("close") ||
            headerField("proxy-connection").toLower().contains("close")) ||
            (parser.getMajorVersion() == 1 && parser.getMinorVersion() == 0 &&
            (connectionHeaderField.isEmpty() && !headerField("proxy-connection").toLower().contains("keep-alive")));
    }
    return bytes;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 498, as _ZN24QHttpNetworkReplyPrivate11parseHeaderE14QByteArrayView
inline void QHttpNetworkReplyPrivate::parseHeader(QByteArrayView header)
{
    parser.parseHeaders(header);
}

//  from src/network/access/qhttpnetworkreply.cpp, line 503, as _ZN24QHttpNetworkReplyPrivate17appendHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkReplyPrivate::appendHeaderField(const QByteArray &name, const QByteArray &data)
{
    parser.appendHeaderField(name, data);
}

//  from src/network/access/qhttpnetworkreply.cpp, line 569, as _ZN24QHttpNetworkReplyPrivate8readBodyEP9QIODeviceP15QByteDataBuffer
inline qint64 QHttpNetworkReplyPrivate::readBody(QIODevice *socket, QByteDataBuffer *out)
{
    qint64 bytes = 0;

    if (isChunked()) {
        // chunked transfer encoding (rfc 2616, sec 3.6)
        bytes += readReplyBodyChunked(socket, out);
    } else if (bodyLength > 0) {
        // we have a Content-Length
        bytes += readReplyBodyRaw(socket, out, bodyLength - contentRead);
        if (contentRead + bytes == bodyLength)
            state = AllDoneState;
    } else {
        // no content length. just read what's possible
        bytes += readReplyBodyRaw(socket, out, socket->bytesAvailable());
    }
    contentRead += bytes;
    return bytes;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 539, as _ZN24QHttpNetworkReplyPrivate12readBodyFastEP9QIODeviceP15QByteDataBuffer
inline qint64 QHttpNetworkReplyPrivate::readBodyFast(QIODevice *socket, QByteDataBuffer *rb)
{

    qint64 toBeRead = qMin(socket->bytesAvailable(), bodyLength - contentRead);
    if (readBufferMaxSize)
        toBeRead = qMin(toBeRead, readBufferMaxSize);

    if (!toBeRead)
        return 0;

    QByteArray bd;
    bd.resize(toBeRead);
    qint64 haveRead = socket->read(bd.data(), toBeRead);
    if (haveRead == -1) {
        bd.clear();
        return 0; // ### error checking here;
    }
    bd.resize(haveRead);

    rb->append(bd);

    if (contentRead + haveRead == bodyLength) {
        state = AllDoneState;
    }

    contentRead += haveRead;
    return haveRead;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 343, as _ZN24QHttpNetworkReplyPrivate5clearEv
inline void QHttpNetworkReplyPrivate::clear()
{
    connection = nullptr;
    connectionChannel = nullptr;
    autoDecompress = false;
    clearHttpLayerInformation();
}

//  from src/network/access/qhttpnetworkreply.cpp, line 329, as _ZN24QHttpNetworkReplyPrivate25clearHttpLayerInformationEv
inline void QHttpNetworkReplyPrivate::clearHttpLayerInformation()
{
    state = NothingDoneState;
    bodyLength = 0;
    contentRead = 0;
    totalProgress = 0;
    currentChunkSize = 0;
    currentChunkRead = 0;
    lastChunkRead = false;
    connectionCloseEnabled = true;
    parser.clear();
}

//  from src/network/access/qhttpnetworkreply.cpp, line 589, as _ZN24QHttpNetworkReplyPrivate16readReplyBodyRawEP9QIODeviceP15QByteDataBufferx
inline qint64 QHttpNetworkReplyPrivate::readReplyBodyRaw(QIODevice *socket, QByteDataBuffer *out, qint64 size)
{
    // FIXME get rid of this function and just use readBodyFast and give it socket->bytesAvailable()
    qint64 bytes = 0;
    Q_ASSERT(socket);
    Q_ASSERT(out);

    int toBeRead = qMin<qint64>(128*1024, qMin<qint64>(size, socket->bytesAvailable()));

    if (readBufferMaxSize)
        toBeRead = qMin<qint64>(toBeRead, readBufferMaxSize);

    while (toBeRead > 0) {
        QByteArray byteData;
        byteData.resize(toBeRead);
        qint64 haveRead = socket->read(byteData.data(), byteData.size());
        if (haveRead <= 0) {
            // ### error checking here
            byteData.clear();
            return bytes;
        }

        byteData.resize(haveRead);
        out->append(byteData);
        bytes += haveRead;
        size -= haveRead;

        toBeRead = qMin<qint64>(128*1024, qMin<qint64>(size, socket->bytesAvailable()));
    }
    return bytes;

}

//  from src/network/access/qhttpnetworkreply.cpp, line 622, as _ZN24QHttpNetworkReplyPrivate20readReplyBodyChunkedEP9QIODeviceP15QByteDataBuffer
inline qint64 QHttpNetworkReplyPrivate::readReplyBodyChunked(QIODevice *socket, QByteDataBuffer *out)
{
    qint64 bytes = 0;
    while (socket->bytesAvailable()) {

        if (readBufferMaxSize && (bytes > readBufferMaxSize))
            break;

        if (!lastChunkRead && currentChunkRead >= currentChunkSize) {
            // For the first chunk and when we're done with a chunk
            currentChunkSize = 0;
            currentChunkRead = 0;
            if (bytes) {
                // After a chunk
                char crlf[2];
                // read the "\r\n" after the chunk
                qint64 haveRead = socket->read(crlf, 2);
                // FIXME: This code is slightly broken and not optimal. What if the 2 bytes are not available yet?!
                // For nice reasons (the toLong in getChunkSize accepting \n at the beginning
                // it right now still works, but we should definitely fix this.

                if (haveRead != 2)
                    return bytes; // FIXME
                bytes += haveRead;
            }
            // Note that chunk size gets stored in currentChunkSize, what is returned is the bytes read
            bytes += getChunkSize(socket, &currentChunkSize);
            if (currentChunkSize == -1)
                break;
        }
        // if the chunk size is 0, end of the stream
        if (currentChunkSize == 0 || lastChunkRead) {
            lastChunkRead = true;
            // try to read the "\r\n" after the chunk
            char crlf[2];
            qint64 haveRead = socket->read(crlf, 2);
            if (haveRead > 0)
                bytes += haveRead;

            if ((haveRead == 2 && crlf[0] == '\r' && crlf[1] == '\n') || (haveRead == 1 && crlf[0] == '\n'))
                state = AllDoneState;
            else if (haveRead == 1 && crlf[0] == '\r')
                break; // Still waiting for the last \n
            else if (haveRead > 0) {
                // If we read something else then CRLF, we need to close the channel.
                forceConnectionCloseEnabled = true;
                state = AllDoneState;
            }
            break;
        }

        // otherwise, try to begin reading this chunk / to read what is missing for this chunk
        qint64 haveRead = readReplyBodyRaw (socket, out, currentChunkSize - currentChunkRead);
        currentChunkRead += haveRead;
        bytes += haveRead;

        // ### error checking here

    }
    return bytes;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 684, as _ZN24QHttpNetworkReplyPrivate12getChunkSizeEP9QIODevicePx
inline qint64 QHttpNetworkReplyPrivate::getChunkSize(QIODevice *socket, qint64 *chunkSize)
{
    qint64 bytes = 0;
    char crlf[2];
    *chunkSize = -1;

    int bytesAvailable = socket->bytesAvailable();
    // FIXME rewrite to permanent loop without bytesAvailable
    while (bytesAvailable > bytes) {
        qint64 sniffedBytes = socket->peek(crlf, 2);
        int fragmentSize = fragment.size();

        // check the next two bytes for a "\r\n", skip blank lines
        if ((fragmentSize && sniffedBytes == 2 && crlf[0] == '\r' && crlf[1] == '\n')
           ||(fragmentSize > 1 && fragment.endsWith('\r')  && crlf[0] == '\n'))
        {
            bytes += socket->read(crlf, 1);     // read the \r or \n
            if (crlf[0] == '\r')
                bytes += socket->read(crlf, 1); // read the \n
            bool ok = false;
            // ignore the chunk-extension
            const auto fragmentView = QByteArrayView(fragment).mid(0, fragment.indexOf(';')).trimmed();
            *chunkSize = fragmentView.toLong(&ok, 16);
            fragment.clear();
            break; // size done
        } else {
            // read the fragment to the buffer
            char c = 0;
            qint64 haveRead = socket->read(&c, 1);
            if (haveRead < 0) {
                return -1; // FIXME
            }
            bytes += haveRead;
            fragment.append(c);
        }
    }

    return bytes;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 724, as _ZNK24QHttpNetworkReplyPrivate13isRedirectingEv
inline bool QHttpNetworkReplyPrivate::isRedirecting() const
{
    // We're in the process of redirecting - if the HTTP status code says so and
    // followRedirect is switched on
    return (QHttpNetworkReply::isHttpRedirect(parser.getStatusCode())
            && request.isFollowRedirects());
}

//  from src/network/access/qhttpnetworkreply.cpp, line 732, as _ZN24QHttpNetworkReplyPrivate17shouldEmitSignalsEv
inline bool QHttpNetworkReplyPrivate::shouldEmitSignals()
{
    // for 401 & 407 don't emit the data signals. Content along with these
    // responses are sent only if the authentication fails.
    return parser.getStatusCode() != 401 && parser.getStatusCode() != 407;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 739, as _ZN24QHttpNetworkReplyPrivate13expectContentEv
inline bool QHttpNetworkReplyPrivate::expectContent()
{
    int statusCode = parser.getStatusCode();
    // check whether we can expect content after the headers (rfc 2616, sec4.4)
    if ((statusCode >= 100 && statusCode < 200)
        || statusCode == 204 || statusCode == 304)
        return false;
    if (request.operation() == QHttpNetworkRequest::Head)
        return false; // no body expected for HEAD request
    qint64 expectedContentLength = contentLength();
    if (expectedContentLength == 0)
        return false;
    if (expectedContentLength == -1 && bodyLength == 0) {
        // The content-length header was stripped, but its value was 0.
        // This would be the case for an explicitly zero-length compressed response.
        return false;
    }
    return true;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 759, as _ZN24QHttpNetworkReplyPrivate9eraseDataEv
inline void QHttpNetworkReplyPrivate::eraseData()
{
    responseData.clear();
}

//  from src/network/access/qhttpnetworkreply.cpp, line 352, as _ZNK24QHttpNetworkReplyPrivate14bytesAvailableEv
inline qint64 QHttpNetworkReplyPrivate::bytesAvailable() const
{
    return (state != ReadingDataState ? 0 : fragment.size());
}

//  from src/network/access/qhttpnetworkreply.cpp, line 508, as _ZN24QHttpNetworkReplyPrivate9isChunkedEv
inline bool QHttpNetworkReplyPrivate::isChunked()
{
    return chunkedTransferEncoding;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 513, as _ZN24QHttpNetworkReplyPrivate24isConnectionCloseEnabledEv
inline bool QHttpNetworkReplyPrivate::isConnectionCloseEnabled()
{
    return connectionCloseEnabled || forceConnectionCloseEnabled;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 357, as _ZNK24QHttpNetworkReplyPrivate12isCompressedEv
inline bool QHttpNetworkReplyPrivate::isCompressed() const
{
    return QDecompressHelper::isSupportedEncoding(headerField("content-encoding"));
}

//  from src/network/access/qhttpnetworkreply.cpp, line 368, as _ZN24QHttpNetworkReplyPrivate26removeAutoDecompressHeaderEv
inline void QHttpNetworkReplyPrivate::removeAutoDecompressHeader()
{
    // The header "Content-Encoding  = gzip" is retained.
    // Content-Length is removed since the actual one sent by the server is for compressed data
    constexpr auto name = QByteArrayView("content-length");
    QByteArray contentLength = parser.firstHeaderField(name);
    bool parseOk = false;
    qint64 value = contentLength.toLongLong(&parseOk);
    if (parseOk) {
        removedContentLength = value;
        parser.removeHeaderField(name);
    }
}
//  -----------------------------------------------------------------------

//  qint64 QHttpNetworkReplyPrivate::readStatus(QIODevice *socket)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN24QHttpNetworkReplyPrivate10readStatusEP9QIODevice(
    QHttpNetworkReplyPrivate *self,
    QIODevice *socket) {
  return self->readStatus(socket);
}

//  bool QHttpNetworkReplyPrivate::parseStatus(QByteArrayView status)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QHttpNetworkReplyPrivate11parseStatusE14QByteArrayView(
    QHttpNetworkReplyPrivate *self,
    const QByteArrayView *status) {
  return self->parseStatus(*status);
}

//  qint64 QHttpNetworkReplyPrivate::readHeader(QIODevice *socket)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN24QHttpNetworkReplyPrivate10readHeaderEP9QIODevice(
    QHttpNetworkReplyPrivate *self,
    QIODevice *socket) {
  return self->readHeader(socket);
}

//  void QHttpNetworkReplyPrivate::parseHeader(QByteArrayView header)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpNetworkReplyPrivate11parseHeaderE14QByteArrayView(
    QHttpNetworkReplyPrivate *self,
    const QByteArrayView *header) {
  self->parseHeader(*header);
}

//  void QHttpNetworkReplyPrivate::appendHeaderField(const QByteArray &name,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpNetworkReplyPrivate17appendHeaderFieldERK10QByteArrayS2_(
    QHttpNetworkReplyPrivate *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->appendHeaderField(*name, *data);
}

//  qint64 QHttpNetworkReplyPrivate::readBody(QIODevice *socket,
//      QByteDataBuffer *out)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN24QHttpNetworkReplyPrivate8readBodyEP9QIODeviceP15QByteDataBuffer(
    QHttpNetworkReplyPrivate *self,
    QIODevice *socket,
    QByteDataBuffer *out) {
  return self->readBody(socket, out);
}

//  qint64 QHttpNetworkReplyPrivate::readBodyFast(QIODevice *socket,
//      QByteDataBuffer *rb)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN24QHttpNetworkReplyPrivate12readBodyFastEP9QIODeviceP15QByteDataBuffer(
    QHttpNetworkReplyPrivate *self,
    QIODevice *socket,
    QByteDataBuffer *rb) {
  return self->readBodyFast(socket, rb);
}

//  void QHttpNetworkReplyPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpNetworkReplyPrivate5clearEv(
    QHttpNetworkReplyPrivate *self) {
  self->clear();
}

//  void QHttpNetworkReplyPrivate::clearHttpLayerInformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpNetworkReplyPrivate25clearHttpLayerInformationEv(
    QHttpNetworkReplyPrivate *self) {
  self->clearHttpLayerInformation();
}

//  qint64 QHttpNetworkReplyPrivate::readReplyBodyRaw(QIODevice *in,
//      QByteDataBuffer *out, qint64 size)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN24QHttpNetworkReplyPrivate16readReplyBodyRawEP9QIODeviceP15QByteDataBufferx(
    QHttpNetworkReplyPrivate *self,
    QIODevice *in,
    QByteDataBuffer *out,
    qint64 size) {
  return self->readReplyBodyRaw(in, out, size);
}

//  qint64 QHttpNetworkReplyPrivate::readReplyBodyChunked(QIODevice *in,
//      QByteDataBuffer *out)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN24QHttpNetworkReplyPrivate20readReplyBodyChunkedEP9QIODeviceP15QByteDataBuffer(
    QHttpNetworkReplyPrivate *self,
    QIODevice *in,
    QByteDataBuffer *out) {
  return self->readReplyBodyChunked(in, out);
}

//  qint64 QHttpNetworkReplyPrivate::getChunkSize(QIODevice *in, qint64
//      *chunkSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN24QHttpNetworkReplyPrivate12getChunkSizeEP9QIODevicePx(
    QHttpNetworkReplyPrivate *self,
    QIODevice *in,
    qint64 *chunkSize) {
  return self->getChunkSize(in, chunkSize);
}

//  bool QHttpNetworkReplyPrivate::isRedirecting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QHttpNetworkReplyPrivate13isRedirectingEv(
    const QHttpNetworkReplyPrivate *self) {
  return self->isRedirecting();
}

//  bool QHttpNetworkReplyPrivate::shouldEmitSignals()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QHttpNetworkReplyPrivate17shouldEmitSignalsEv(
    QHttpNetworkReplyPrivate *self) {
  return self->shouldEmitSignals();
}

//  bool QHttpNetworkReplyPrivate::expectContent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QHttpNetworkReplyPrivate13expectContentEv(
    QHttpNetworkReplyPrivate *self) {
  return self->expectContent();
}

//  void QHttpNetworkReplyPrivate::eraseData()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpNetworkReplyPrivate9eraseDataEv(
    QHttpNetworkReplyPrivate *self) {
  self->eraseData();
}

//  qint64 QHttpNetworkReplyPrivate::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QHttpNetworkReplyPrivate14bytesAvailableEv(
    const QHttpNetworkReplyPrivate *self) {
  return self->bytesAvailable();
}

//  bool QHttpNetworkReplyPrivate::isChunked()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QHttpNetworkReplyPrivate9isChunkedEv(
    QHttpNetworkReplyPrivate *self) {
  return self->isChunked();
}

//  bool QHttpNetworkReplyPrivate::isConnectionCloseEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QHttpNetworkReplyPrivate24isConnectionCloseEnabledEv(
    QHttpNetworkReplyPrivate *self) {
  return self->isConnectionCloseEnabled();
}

//  bool QHttpNetworkReplyPrivate::isCompressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QHttpNetworkReplyPrivate12isCompressedEv(
    const QHttpNetworkReplyPrivate *self) {
  return self->isCompressed();
}

//  void QHttpNetworkReplyPrivate::removeAutoDecompressHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpNetworkReplyPrivate26removeAutoDecompressHeaderEv(
    QHttpNetworkReplyPrivate *self) {
  self->removeAutoDecompressHeader();
}

//  QHttpNetworkReplyPrivate as the QHttpNetworkHeaderPrivate it is built on
extern "C" Q_DECL_EXPORT
QHttpNetworkHeaderPrivate *ritual_cast_QHttpNetworkReplyPrivate_QHttpNetworkHeaderPrivate(
    QHttpNetworkReplyPrivate *self) {
  return static_cast<QHttpNetworkHeaderPrivate *>(self);
}

#endif  // QT_CONFIG(http)
