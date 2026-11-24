//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpprotocolhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpprotocolhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qabstractprotocolhandler_p.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#include <QtNetwork/private/qhttpprotocolhandler_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#include <QtNetwork/private/qsocketabstraction_p.h>
#include <QtNetwork/private/qhttpnetworkreply_p.h>
#include <QtNetwork/private/qhttpnetworkconnection_p.h>
#ifndef QT_NO_SSL
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#    include <QtNetwork/qsslconfiguration.h>
#endif
#include <QtNetwork/private/qdecompresshelper_p.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#include <QtNetwork/private/qhttpnetworkconnection_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/qdebug.h>
#include <QtNetwork/private/qhttp2protocolhandler_p.h>
#include <QtNetwork/private/qhttpprotocolhandler_p.h>
#include <QtNetwork/private/http2protocol_p.h>
#include <QtNetwork/private/qsocketabstraction_p.h>
#ifndef QT_NO_SSL
#    include <QtNetwork/private/qsslsocket_p.h>
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#endif
#include <QtNetwork/private/qtnetworkglobal_p.h>
#include <memory>
#include <utility>
#include <QtNetwork/private/qhttpnetworkconnection_p.h>
#include <QtNetwork/private/qabstractsocket_p.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#include <QtNetwork/private/qhttp2protocolhandler_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtNetwork/private/qnetworkrequest_p.h>
#include <QtCore/private/qobject_p.h>
#include <QtNetwork/private/qauthenticator_p.h>
#include <QtNetwork/private/qhostinfo_p.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qauthenticator.h>
#include <QtCore/qcoreapplication.h>
#include <QtNetwork/private/qdecompresshelper_p.h>
#include <QtNetwork/private/qsocketabstraction_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qdebug.h>
#include <QtCore/qspan.h>
#include <QtCore/qvarlengtharray.h>
#ifndef QT_NO_SSL
#    include <QtNetwork/private/qsslsocket_p.h>
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#    include <QtNetwork/qsslconfiguration.h>
#    include <QtNetwork/qsslerror.h>
#endif
#include <QtNetwork/private/qhttpnetworkrequest_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtNetwork/private/qhttpnetworkconnection_p.h>
#include <QtNetwork/private/qhttp2protocolhandler_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtNetwork/private/qsocketabstraction_p.h>
#include <QtNetwork/qabstractsocket.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qendian.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qhttp2configuration.h>
#ifndef QT_NO_NETWORKPROXY
#  include <QtNetwork/qnetworkproxy.h>
#endif
#include <QtCore/qcoreapplication.h>
#include <algorithm>
#include <vector>
#include <optional>
#include <QtNetwork/private/qhttpnetworkheader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qabstractprotocolhandler.cpp, line 10, as _ZN24QAbstractProtocolHandlerC2EP29QHttpNetworkConnectionChannel
inline QAbstractProtocolHandler::QAbstractProtocolHandler(QHttpNetworkConnectionChannel *channel)
    : m_channel(channel), m_reply(nullptr), m_socket(m_channel->socket), m_connection(m_channel->connection)
{
    Q_ASSERT(m_channel);
    Q_ASSERT(m_socket);
    Q_ASSERT(m_connection);
}

//  from src/network/access/qhttpprotocolhandler.cpp, line 20, as _ZN20QHttpProtocolHandler15_q_receiveReplyEv
inline void QHttpProtocolHandler::_q_receiveReply()
{
    Q_ASSERT(m_socket);

    if (!m_reply) {
        if (m_socket->bytesAvailable() > 0)
            qWarning() << "QAbstractProtocolHandler::_q_receiveReply() called without QHttpNetworkReply,"
                       << m_socket->bytesAvailable() << "bytes on socket.";
        m_channel->close();
        return;
    }

    // only run when the QHttpNetworkConnection is not currently being destructed, e.g.
    // this function is called from _q_disconnected which is called because
    // of ~QHttpNetworkConnectionPrivate
    if (!qobject_cast<QHttpNetworkConnection*>(m_connection)) {
        return;
    }

    // connection might be closed to signal the end of data
    if (QSocketAbstraction::socketState(m_socket) == QAbstractSocket::UnconnectedState) {
        if (m_socket->bytesAvailable() <= 0) {
            if (m_reply->d_func()->state == QHttpNetworkReplyPrivate::ReadingDataState) {
                // finish this reply. this case happens when the server did not send a content length
                m_reply->d_func()->state = QHttpNetworkReplyPrivate::AllDoneState;
                m_channel->allDone();
                return;
            } else {
                m_channel->handleUnexpectedEOF();
                return;
            }
        } else {
            // socket not connected but still bytes for reading.. just continue in this function
        }
    }

    // read loop for the response
    qint64 bytes = 0;
    qint64 lastBytes = bytes;
    do {
        lastBytes = bytes;

        QHttpNetworkReplyPrivate::ReplyState state = m_reply->d_func()->state;
        switch (state) {
        case QHttpNetworkReplyPrivate::NothingDoneState: {
            m_reply->d_func()->state = QHttpNetworkReplyPrivate::ReadingStatusState;
            Q_FALLTHROUGH();
        }
        case QHttpNetworkReplyPrivate::ReadingStatusState: {
            qint64 statusBytes = m_reply->d_func()->readStatus(m_socket);
            if (statusBytes == -1) {
                // connection broke while reading status. also handled if later _q_disconnected is called
                m_channel->handleUnexpectedEOF();
                return;
            }
            bytes += statusBytes;
            m_channel->lastStatus = m_reply->statusCode();
            break;
        }
        case QHttpNetworkReplyPrivate::ReadingHeaderState: {
            QHttpNetworkReplyPrivate *replyPrivate = m_reply->d_func();
            qint64 headerBytes = replyPrivate->readHeader(m_socket);
            if (headerBytes == -1) {
                // connection broke while reading headers. also handled if later _q_disconnected is called
                m_channel->handleUnexpectedEOF();
                return;
            }
            bytes += headerBytes;
            // If headers were parsed successfully now it is the ReadingDataState
            if (replyPrivate->state == QHttpNetworkReplyPrivate::ReadingDataState) {
                if (replyPrivate->isCompressed() && replyPrivate->autoDecompress) {
                    // remove the Content-Length from header
                    replyPrivate->removeAutoDecompressHeader();
                } else {
                    replyPrivate->autoDecompress = false;
                }
                const int statusCode = m_reply->statusCode();
                if (statusCode == 100 || (102 <= statusCode && statusCode <= 199)) {
                    replyPrivate->clearHttpLayerInformation();
                    replyPrivate->state = QHttpNetworkReplyPrivate::ReadingStatusState;
                    break; // ignore
                }
                if (replyPrivate->shouldEmitSignals())
                    emit m_reply->headerChanged();
                // After headerChanged had been emitted
                // we can suddenly have a replyPrivate->userProvidedDownloadBuffer
                // this is handled in the ReadingDataState however

                if (!replyPrivate->expectContent()) {
                    replyPrivate->state = QHttpNetworkReplyPrivate::AllDoneState;
                    m_channel->allDone();
                    break;
                }
            }
            break;
        }
        case QHttpNetworkReplyPrivate::ReadingDataState: {
           QHttpNetworkReplyPrivate *replyPrivate = m_reply->d_func();
           if (QSocketAbstraction::socketState(m_socket) == QAbstractSocket::ConnectedState &&
               replyPrivate->downstreamLimited && !replyPrivate->responseData.isEmpty() && replyPrivate->shouldEmitSignals()) {
               // (only do the following when still connected, not when we have already been disconnected and there is still data)
               // We already have some HTTP body data. We don't read more from the socket until
               // this is fetched by QHttpNetworkAccessHttpBackend. If we would read more,
               // we could not limit our read buffer usage.
               // We only do this when shouldEmitSignals==true because our HTTP parsing
               // always needs to parse the 401/407 replies. Therefore they don't really obey
               // to the read buffer maximum size, but we don't care since they should be small.
               return;
           }

           if (replyPrivate->userProvidedDownloadBuffer) {
               // the user provided a direct buffer where we should put all our data in.
               // this only works when we can tell the user the content length and he/she can allocate
               // the buffer in that size.
               // note that this call will read only from the still buffered data
               qint64 haveRead = replyPrivate->readBodyVeryFast(m_socket, replyPrivate->userProvidedDownloadBuffer + replyPrivate->totalProgress);
               if (haveRead > 0) {
                   bytes += haveRead;
                   replyPrivate->totalProgress += haveRead;
                   // the user will get notified of it via progress signal
                   emit m_reply->dataReadProgress(replyPrivate->totalProgress, replyPrivate->bodyLength);
               } else if (haveRead == 0) {
                   // Happens since this called in a loop. Currently no bytes available.
               } else if (haveRead < 0) {
                   m_connection->d_func()->emitReplyError(m_socket, m_reply, QNetworkReply::RemoteHostClosedError);
                   break;
               }
           } else if (!replyPrivate->isChunked() && replyPrivate->bodyLength > 0) {
                 // bulk files like images should fulfill these properties and
                 // we can therefore save on memory copying
                qint64 haveRead = replyPrivate->readBodyFast(m_socket, &replyPrivate->responseData);
                bytes += haveRead;
                replyPrivate->totalProgress += haveRead;
                if (replyPrivate->shouldEmitSignals()) {
                    emit m_reply->readyRead();
                    emit m_reply->dataReadProgress(replyPrivate->totalProgress, replyPrivate->bodyLength);
                }
            }
            else
            {
                // use the traditional slower reading (for compressed encoding, chunked encoding,
                // no content-length etc)
                qint64 haveRead = replyPrivate->readBody(m_socket, &replyPrivate->responseData);
                if (haveRead > 0) {
                    bytes += haveRead;
                    replyPrivate->totalProgress += haveRead;
                    if (replyPrivate->shouldEmitSignals()) {
                        emit m_reply->readyRead();
                        emit m_reply->dataReadProgress(replyPrivate->totalProgress, replyPrivate->bodyLength);
                    }
                } else if (haveRead == -1) {
                    // Some error occurred
                    m_connection->d_func()->emitReplyError(m_socket, m_reply, QNetworkReply::ProtocolFailure);
                    break;
                }
            }
            // still in ReadingDataState? This function will be called again by the socket's readyRead
            if (replyPrivate->state == QHttpNetworkReplyPrivate::ReadingDataState)
                break;

            // everything done
            Q_FALLTHROUGH();
            }
      case QHttpNetworkReplyPrivate::AllDoneState:
            m_channel->allDone();
            if (state == QHttpNetworkReplyPrivate::AllDoneState)
                lastBytes = bytes; // No need to loop more just to call m_channel->allDone again.
            break;
        default:
            break;
        }
    } while (bytes != lastBytes && m_reply);
}

//  from src/network/access/qhttpprotocolhandler.cpp, line 194, as _ZN20QHttpProtocolHandler12_q_readyReadEv
inline void QHttpProtocolHandler::_q_readyRead()
{
    if (QSocketAbstraction::socketState(m_socket) == QAbstractSocket::ConnectedState
        && m_socket->bytesAvailable() == 0) {
        // We got a readyRead but no bytes are available..
        // This happens for the Unbuffered QTcpSocket
        // Also check if socket is in ConnectedState since
        // this function may also be invoked via the event loop.
        char c;
        qint64  ret = m_socket->peek(&c, 1);
        if (ret < 0) {
            m_channel->_q_error(QSocketAbstraction::socketError(m_socket));
            // We still need to handle the reply so it emits its signals etc.
            if (m_reply)
                _q_receiveReply();
            return;
        }
    }

    if (m_channel->isSocketWaiting() || m_channel->isSocketReading()) {
        if (m_socket->bytesAvailable()) {
            // We might get a spurious call from readMoreLater()
            // call of the QHttpNetworkConnection even while the socket is disconnecting.
            // Therefore check if there is actually bytes available before changing the channel state.
            m_channel->state = QHttpNetworkConnectionChannel::ReadingState;
        }
        if (m_reply)
            _q_receiveReply();
    }
}

//  from src/network/access/qhttpprotocolhandler.cpp, line 225, as _ZN20QHttpProtocolHandler11sendRequestEv
inline bool QHttpProtocolHandler::sendRequest()
{
    m_reply = m_channel->reply;

    if (!m_reply) {
        // heh, how should that happen!
        qWarning("QAbstractProtocolHandler::sendRequest() called without QHttpNetworkReply");
        return false;
    }

    switch (m_channel->state) {
    case QHttpNetworkConnectionChannel::IdleState: { // write the header
        if (!m_channel->ensureConnection()) {
            // wait for the connection (and encryption) to be done
            // sendRequest will be called again from either
            // _q_connected or _q_encrypted
            return false;
        }
        if (m_channel->request.isPreConnect()) {
            m_channel->state = QHttpNetworkConnectionChannel::IdleState;
            m_reply->d_func()->state = QHttpNetworkReplyPrivate::AllDoneState;
            m_channel->allDone();
            m_connection->preConnectFinished(); // will only decrease the counter
            m_reply = nullptr; // so we can reuse this channel
            return true; // we have a working connection and are done
        }

        m_channel->written = 0; // excluding the header
        m_channel->bytesTotal = 0;

        QHttpNetworkReplyPrivate *replyPrivate = m_reply->d_func();
        replyPrivate->clear();
        replyPrivate->connection = m_connection;
        replyPrivate->connectionChannel = m_channel;
        replyPrivate->autoDecompress = m_channel->request.d->autoDecompress;
        replyPrivate->pipeliningUsed = false;

        // if the url contains authentication parameters, use the new ones
        // both channels will use the new authentication parameters
        if (!m_channel->request.url().userInfo().isEmpty() && m_channel->request.withCredentials()) {
            QUrl url = m_channel->request.url();
            QAuthenticator &auth = m_channel->authenticator;
            if (url.userName() != auth.user()
                || (!url.password().isEmpty() && url.password() != auth.password())) {
                auth.setUser(url.userName());
                auth.setPassword(url.password());
                m_connection->d_func()->copyCredentials(m_connection->d_func()->indexOf(m_socket), &auth, false);
            }
            // clear the userinfo,  since we use the same request for resending
            // userinfo in url can conflict with the one in the authenticator
            url.setUserInfo(QString());
            m_channel->request.setUrl(url);
        }
        // Will only be false if Qt WebKit is performing a cross-origin XMLHttpRequest
        // and withCredentials has not been set to true.
        if (m_channel->request.withCredentials())
            m_connection->d_func()->createAuthorization(m_socket, m_channel->request);
#ifndef QT_NO_NETWORKPROXY
        m_header = QHttpNetworkRequestPrivate::header(m_channel->request,
            (m_connection->d_func()->networkProxy.type() != QNetworkProxy::NoProxy));
#else
        m_header = QHttpNetworkRequestPrivate::header(m_channel->request, false);
#endif

        // flushing is dangerous (QSslSocket calls transmit which might read or error)
//        m_socket->flush();
        QNonContiguousByteDevice* uploadByteDevice = m_channel->request.uploadByteDevice();
        if (uploadByteDevice) {
            // connect the signals so this function gets called again
            QObject::connect(uploadByteDevice, SIGNAL(readyRead()), m_channel, SLOT(_q_uploadDataReadyRead()));

            m_channel->bytesTotal = m_channel->request.contentLength();

            m_channel->state = QHttpNetworkConnectionChannel::WritingState; // start writing data
            sendRequest(); //recurse
        } else {
            // no data to send: just send the HTTP headers
            m_socket->write(std::exchange(m_header, {}));
            QMetaObject::invokeMethod(m_reply, "requestSent", Qt::QueuedConnection);
            m_channel->state = QHttpNetworkConnectionChannel::WaitingState; // now wait for response
            sendRequest(); //recurse
        }

        break;
    }
    case QHttpNetworkConnectionChannel::WritingState:
    {
        // write the data
        QNonContiguousByteDevice* uploadByteDevice = m_channel->request.uploadByteDevice();
        if (!uploadByteDevice || m_channel->bytesTotal == m_channel->written) {
            // the upload device might have no data to send, but we still have to send the headers,
            // do it now.
            if (!m_header.isEmpty())
                m_socket->write(std::exchange(m_header, {}));
            if (uploadByteDevice)
                emit m_reply->dataSendProgress(m_channel->written, m_channel->bytesTotal);
            m_channel->state = QHttpNetworkConnectionChannel::WaitingState; // now wait for response
            sendRequest(); // recurse
            break;
        }

        // only feed the QTcpSocket buffer when there is less than 32 kB in it;
        // note that the headers do not count towards these limits.
        const qint64 socketBufferFill = 32*1024;
        const qint64 socketWriteMaxSize = 16*1024;

        // if it is really an ssl socket, check more than just bytesToWrite()
#ifndef QT_NO_SSL
        QSslSocket *sslSocket = qobject_cast<QSslSocket*>(m_socket);
        const auto encryptedBytesToWrite = [sslSocket]() -> qint64
        {
            return sslSocket ? sslSocket->encryptedBytesToWrite() : 0;
        };
#else
        const auto encryptedBytesToWrite = [](){ return qint64(0); };
#endif

        // throughout this loop, we want to send the data coming from uploadByteDevice.
        // we also need to send the headers, as we try to coalesce their write with the data.
        // we won't send more than the limits above, excluding the headers
        while ((m_socket->bytesToWrite() + encryptedBytesToWrite()) <= socketBufferFill
               && m_channel->bytesTotal != m_channel->written)
        {
            // get pointer to upload data
            qint64 currentReadSize = 0;
            const qint64 desiredReadSize = qMin(socketWriteMaxSize, m_channel->bytesTotal - m_channel->written);
            const char *readPointer = uploadByteDevice->readPointer(desiredReadSize, currentReadSize);

            if (currentReadSize == -1) {
                // premature eof happened
                m_connection->d_func()->emitReplyError(m_socket, m_reply, QNetworkReply::UnknownNetworkError);
                return false;
            } else if (readPointer == nullptr || currentReadSize == 0) {
                // nothing to read currently, break the loop
                break;
            } else {
                if (m_channel->written != uploadByteDevice->pos()) {
                    // Sanity check. This was useful in tracking down an upload corruption.
                    qWarning() << "QHttpProtocolHandler: Internal error in sendRequest. Expected to write at position" << m_channel->written << "but read device is at" << uploadByteDevice->pos();
                    Q_ASSERT(m_channel->written == uploadByteDevice->pos());
                    m_connection->d_func()->emitReplyError(m_socket, m_reply, QNetworkReply::ProtocolFailure);
                    return false;
                }
                qint64 currentWriteSize;
                if (m_header.isEmpty()) {
                    currentWriteSize = m_socket->write(readPointer, currentReadSize);
                } else {
                    // assemble header and data and send them together
                    const qint64 headerSize = m_header.size();
                    m_header.append(readPointer, currentReadSize);
                    currentWriteSize = m_socket->write(std::exchange(m_header, {}));
                    if (currentWriteSize != -1)
                        currentWriteSize -= headerSize;
                    QMetaObject::invokeMethod(m_reply, "requestSent", Qt::QueuedConnection);
                }
                if (currentWriteSize == -1 || currentWriteSize != currentReadSize) {
                    // socket broke down
                    m_connection->d_func()->emitReplyError(m_socket, m_reply, QNetworkReply::UnknownNetworkError);
                    return false;
                } else {
                    m_channel->written += currentWriteSize;
                    uploadByteDevice->advanceReadPointer(currentWriteSize);

                    emit m_reply->dataSendProgress(m_channel->written, m_channel->bytesTotal);

                    if (m_channel->written == m_channel->bytesTotal) {
                        // make sure this function is called once again
                        m_channel->state = QHttpNetworkConnectionChannel::WaitingState;
                        sendRequest();
                        break;
                    }
                }
            }
        }
        break;
    }

    case QHttpNetworkConnectionChannel::WaitingState:
    {
        QNonContiguousByteDevice* uploadByteDevice = m_channel->request.uploadByteDevice();
        if (uploadByteDevice) {
            QObject::disconnect(uploadByteDevice, SIGNAL(readyRead()), m_channel, SLOT(_q_uploadDataReadyRead()));
        }

        // HTTP pipelining
        //m_connection->d_func()->fillPipeline(m_socket);
        //m_socket->flush();

        // ensure we try to receive a reply in all cases, even if _q_readyRead_ hat not been called
        // this is needed if the sends an reply before we have finished sending the request. In that
        // case receiveReply had been called before but ignored the server reply
        if (m_socket->bytesAvailable())
            QMetaObject::invokeMethod(m_channel, "_q_receiveReply", Qt::QueuedConnection);
        break;
    }
    case QHttpNetworkConnectionChannel::ReadingState:
        // ignore _q_bytesWritten in these states
        Q_FALLTHROUGH();
    default:
        break;
    }
    return true;
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

//  from src/network/access/qhttpnetworkreply.cpp, line 520, as _ZN24QHttpNetworkReplyPrivate16readBodyVeryFastEP9QIODevicePc
inline qint64 QHttpNetworkReplyPrivate::readBodyVeryFast(QIODevice *socket, char *b)
{
    // This first read is to flush the buffer inside the socket
    qint64 haveRead = 0;
    haveRead = socket->read(b, bodyLength - contentRead);
    if (haveRead == -1) {
        return -1;
    }
    contentRead += haveRead;

    if (contentRead == bodyLength) {
        state = AllDoneState;
    }

    return haveRead;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 732, as _ZN24QHttpNetworkReplyPrivate17shouldEmitSignalsEv
inline bool QHttpNetworkReplyPrivate::shouldEmitSignals()
{
    // for 401 & 407 don't emit the data signals. Content along with these
    // responses are sent only if the authentication fails.
    return parser.getStatusCode() != 401 && parser.getStatusCode() != 407;
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

//  from src/network/access/qhttpnetworkreply.cpp, line 508, as _ZN24QHttpNetworkReplyPrivate9isChunkedEv
inline bool QHttpNetworkReplyPrivate::isChunked()
{
    return chunkedTransferEncoding;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 279, as _ZN29QHttpNetworkConnectionChannel19handleUnexpectedEOFEv
inline void QHttpNetworkConnectionChannel::handleUnexpectedEOF()
{
    Q_ASSERT(reply);
    if (reconnectAttempts <= 0 || !request.methodIsIdempotent()) {
        // too many errors reading/receiving/parsing the status, close the socket and emit error
        requeueCurrentlyPipelinedRequests();
        close();
        reply->d_func()->errorString = connection->d_func()->errorDetail(QNetworkReply::RemoteHostClosedError, socket);
        emit reply->finishedWithError(QNetworkReply::RemoteHostClosedError, reply->d_func()->errorString);
        reply = nullptr;
        if (protocolHandler)
            protocolHandler->setReply(nullptr);
        request = QHttpNetworkRequest();
        QMetaObject::invokeMethod(connection, "_q_startNextRequest", Qt::QueuedConnection);
    } else {
        reconnectAttempts--;
        reply->d_func()->clear();
        reply->d_func()->connection = connection;
        reply->d_func()->connectionChannel = this;
        closeAndResendCurrentRequest();
    }
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 186, as _ZN29QHttpNetworkConnectionChannel5closeEv
inline void QHttpNetworkConnectionChannel::close()
{
    if (state == QHttpNetworkConnectionChannel::ClosingState)
        return;

    if (!socket)
        state = QHttpNetworkConnectionChannel::IdleState;
    else if (QSocketAbstraction::socketState(socket) == QAbstractSocket::UnconnectedState)
        state = QHttpNetworkConnectionChannel::IdleState;
    else
        state = QHttpNetworkConnectionChannel::ClosingState;

    // pendingEncrypt must only be true in between connected and encrypted states
    pendingEncrypt = false;

    if (socket) {
        // socket can be 0 since the host lookup is done from qhttpnetworkconnection.cpp while
        // there is no socket yet.
        socket->close();
    }
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 357, as _ZN29QHttpNetworkConnectionPrivate14emitReplyErrorEP9QIODeviceP17QHttpNetworkReplyN13QNetworkReply12NetworkErrorE
inline void QHttpNetworkConnectionPrivate::emitReplyError(QIODevice *socket,
                                                   QHttpNetworkReply *reply,
                                                   QNetworkReply::NetworkError errorCode)
{
    Q_Q(QHttpNetworkConnection);

    int i = 0;
    if (socket)
        i = indexOf(socket);

    if (reply) {
        // this error matters only to this reply
        reply->d_func()->errorString = errorDetail(errorCode, socket);
        emit reply->finishedWithError(errorCode, reply->d_func()->errorString);
        // remove the corrupt data if any
        reply->d_func()->eraseData();

        // Clean the channel
        channels[i].close();
        channels[i].reply = nullptr;
        if (channels[i].protocolHandler)
            channels[i].protocolHandler->setReply(nullptr);
        channels[i].request = QHttpNetworkRequest();
        if (socket)
            channels[i].requeueCurrentlyPipelinedRequests();

        // send the next request
        QMetaObject::invokeMethod(q, "_q_startNextRequest", Qt::QueuedConnection);
    }
}

//  from src/network/access/qhttpnetworkreply.cpp, line 357, as _ZNK24QHttpNetworkReplyPrivate12isCompressedEv
inline bool QHttpNetworkReplyPrivate::isCompressed() const
{
    return QDecompressHelper::isSupportedEncoding(headerField("content-encoding"));
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 1074, as _ZN29QHttpNetworkConnectionChannel8_q_errorEN15QAbstractSocket11SocketErrorE
inline void QHttpNetworkConnectionChannel::_q_error(QAbstractSocket::SocketError socketError)
{
    if (!socket)
        return;
    QNetworkReply::NetworkError errorCode = QNetworkReply::UnknownNetworkError;

    switch (socketError) {
    case QAbstractSocket::HostNotFoundError:
        errorCode = QNetworkReply::HostNotFoundError;
        break;
    case QAbstractSocket::ConnectionRefusedError:
        errorCode = QNetworkReply::ConnectionRefusedError;
#ifndef QT_NO_NETWORKPROXY
        if (connection->d_func()->networkProxy.type() != QNetworkProxy::NoProxy && !ssl)
            errorCode = QNetworkReply::ProxyConnectionRefusedError;
#endif
        break;
    case QAbstractSocket::RemoteHostClosedError:
        // This error for SSL comes twice in a row, first from SSL layer ("The TLS/SSL connection has been closed") then from TCP layer.
        // Depending on timing it can also come three times in a row (first time when we try to write into a closing QSslSocket).
        // The reconnectAttempts handling catches the cases where we can re-send the request.
        if (!reply && state == QHttpNetworkConnectionChannel::IdleState) {
            // Not actually an error, it is normal for Keep-Alive connections to close after some time if no request
            // is sent on them. No need to error the other replies below. Just bail out here.
            // The _q_disconnected will handle the possibly pipelined replies. HTTP/2 is special for now,
            // we do not resend, but must report errors if any request is in progress (note, while
            // not in its sendRequest(), protocol handler switches the channel to IdleState, thus
            // this check is under this condition in 'if'):
            if (auto *h2Handler = h2ProtocolHandler())
                h2Handler->handleConnectionClosure();
            return;
        } else if (state != QHttpNetworkConnectionChannel::IdleState && state != QHttpNetworkConnectionChannel::ReadingState) {
            // Try to reconnect/resend before sending an error.
            // While "Reading" the _q_disconnected() will handle this.
            // If we're using ssl then the protocolHandler is not initialized until
            // "encrypted" has been emitted, since retrying requires the protocolHandler (asserted)
            // we will not try if encryption is not done.
            if (!pendingEncrypt && reconnectAttempts-- > 0) {
                resendCurrentRequest();
                return;
            } else {
                errorCode = QNetworkReply::RemoteHostClosedError;
            }
        } else if (state == QHttpNetworkConnectionChannel::ReadingState) {
            if (!reply)
                break;

            if (!reply->d_func()->expectContent()) {
                // No content expected, this is a valid way to have the connection closed by the server
                // We need to invoke this asynchronously to make sure the state() of the socket is on QAbstractSocket::UnconnectedState
                QMetaObject::invokeMethod(this, "_q_receiveReply", Qt::QueuedConnection);
                return;
            }
            if (reply->contentLength() == -1 && !reply->d_func()->isChunked()) {
                // There was no content-length header and it's not chunked encoding,
                // so this is a valid way to have the connection closed by the server
                // We need to invoke this asynchronously to make sure the state() of the socket is on QAbstractSocket::UnconnectedState
                QMetaObject::invokeMethod(this, "_q_receiveReply", Qt::QueuedConnection);
                return;
            }
            // ok, we got a disconnect even though we did not expect it
            // Try to read everything from the socket before we emit the error.
            if (socket->bytesAvailable()) {
                // Read everything from the socket into the reply buffer.
                // we can ignore the readbuffersize as the data is already
                // in memory and we will not receive more data on the socket.
                reply->setReadBufferSize(0);
                reply->setDownstreamLimited(false);
                _q_receiveReply();
                if (!reply) {
                    // No more reply assigned after the previous call? Then it had been finished successfully.
                    requeueCurrentlyPipelinedRequests();
                    state = QHttpNetworkConnectionChannel::IdleState;
                    QMetaObject::invokeMethod(connection, "_q_startNextRequest", Qt::QueuedConnection);
                    return;
                }
            }

            errorCode = QNetworkReply::RemoteHostClosedError;
        } else {
            errorCode = QNetworkReply::RemoteHostClosedError;
        }
        break;
    case QAbstractSocket::SocketTimeoutError:
        // try to reconnect/resend before sending an error.
        if (state == QHttpNetworkConnectionChannel::WritingState && (reconnectAttempts-- > 0)) {
            resendCurrentRequest();
            return;
        }
        errorCode = QNetworkReply::TimeoutError;
        break;
    case QAbstractSocket::ProxyConnectionRefusedError:
        errorCode = QNetworkReply::ProxyConnectionRefusedError;
        break;
    case QAbstractSocket::ProxyAuthenticationRequiredError:
        errorCode = QNetworkReply::ProxyAuthenticationRequiredError;
        break;
    case QAbstractSocket::SslHandshakeFailedError:
        errorCode = QNetworkReply::SslHandshakeFailedError;
        break;
    case QAbstractSocket::ProxyConnectionClosedError:
        // try to reconnect/resend before sending an error.
        if (reconnectAttempts-- > 0) {
            resendCurrentRequest();
            return;
        }
        errorCode = QNetworkReply::ProxyConnectionClosedError;
        break;
    case QAbstractSocket::ProxyConnectionTimeoutError:
        // try to reconnect/resend before sending an error.
        if (reconnectAttempts-- > 0) {
            resendCurrentRequest();
            return;
        }
        errorCode = QNetworkReply::ProxyTimeoutError;
        break;
    default:
        // all other errors are treated as NetworkError
        errorCode = QNetworkReply::UnknownNetworkError;
        break;
    }
    QPointer<QHttpNetworkConnection> that = connection;
    QString errorString = connection->d_func()->errorDetail(errorCode, socket, socket->errorString());

    // In the HostLookupPending state the channel should not emit the error.
    // This will instead be handled by the connection.
    if (!connection->d_func()->shouldEmitChannelError(socket))
        return;

    // emit error for all waiting replies
    do {
        // First requeue the already pipelined requests for the current failed reply,
        // then dequeue pending requests so we can also mark them as finished with error
        if (reply)
            requeueCurrentlyPipelinedRequests();
        else
            connection->d_func()->dequeueRequest(socket);

        if (reply) {
            reply->d_func()->errorString = errorString;
            reply->d_func()->httpErrorCode = errorCode;
            emit reply->finishedWithError(errorCode, errorString);
            reply = nullptr;
            if (protocolHandler)
                protocolHandler->setReply(nullptr);
        }
    } while (!connection->d_func()->highPriorityQueue.isEmpty()
             || !connection->d_func()->lowPriorityQueue.isEmpty());

    if (connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2
        || connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2Direct) {
        const auto h2RequestsToSendCopy = std::exchange(h2RequestsToSend, {});
        for (const auto &httpMessagePair : h2RequestsToSendCopy) {
            // emit error for all replies
            QHttpNetworkReply *currentReply = httpMessagePair.second;
            currentReply->d_func()->errorString = errorString;
            currentReply->d_func()->httpErrorCode = errorCode;
            Q_ASSERT(currentReply);
            emit currentReply->finishedWithError(errorCode, errorString);
        }
    }

    // send the next request
    QMetaObject::invokeMethod(that, "_q_startNextRequest", Qt::QueuedConnection);

    if (that) {
        //signal emission triggered event loop
        if (!socket)
            state = QHttpNetworkConnectionChannel::IdleState;
        else if (QSocketAbstraction::socketState(socket) == QAbstractSocket::UnconnectedState)
            state = QHttpNetworkConnectionChannel::IdleState;
        else
            state = QHttpNetworkConnectionChannel::ClosingState;

        // pendingEncrypt must only be true in between connected and encrypted states
        pendingEncrypt = false;
    }
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 838, as _ZNK29QHttpNetworkConnectionChannel15isSocketReadingEv
inline bool QHttpNetworkConnectionChannel::isSocketReading() const
{
    return (state & QHttpNetworkConnectionChannel::ReadingState);
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 833, as _ZNK29QHttpNetworkConnectionChannel15isSocketWaitingEv
inline bool QHttpNetworkConnectionChannel::isSocketWaiting() const
{
    return (state & QHttpNetworkConnectionChannel::WaitingState);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 196, as _ZN19QHttpNetworkRequest6setUrlERK4QUrl
inline void QHttpNetworkRequest::setUrl(const QUrl &url)
{
    d->url = url;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 343, as _ZN24QHttpNetworkReplyPrivate5clearEv
inline void QHttpNetworkReplyPrivate::clear()
{
    connection = nullptr;
    connectionChannel = nullptr;
    autoDecompress = false;
    clearHttpLayerInformation();
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 118, as _ZN26QHttpNetworkRequestPrivate6headerERK19QHttpNetworkRequestb
inline QByteArray QHttpNetworkRequestPrivate::header(const QHttpNetworkRequest &request, bool throughProxy)
{
    const QHttpHeaders headers = request.header();
    QByteArray ba;
    ba.reserve(40 + headers.size() * 25); // very rough lower bound estimation

    ba += request.methodName();
    ba += ' ';
    ba += request.uri(throughProxy);

    ba += " HTTP/";
    ba += QByteArray::number(request.majorVersion());
    ba += '.';
    ba += QByteArray::number(request.minorVersion());
    ba += "\r\n";

    constexpr auto titlecase = [](QByteArrayView name) {
        std::string n;
        n.reserve(size_t(name.size()));
        bool toUpperNext = true;
        for (char c : name) {
            n += toUpperNext ? QtMiscUtils::toAsciiUpper(c) : c;
            toUpperNext = c == '-';
        }
        return n;
    };

    for (qsizetype i = 0; i < headers.size(); ++i) {
        ba += titlecase(headers.nameAt(i));
        ba += ": ";
        ba += headers.valueAt(i);
        ba += "\r\n";
    }
    if (request.d->operation == QHttpNetworkRequest::Post) {
        // add content type, if not set in the request
        if (request.headerField("content-type").isEmpty() && ((request.d->uploadByteDevice && request.d->uploadByteDevice->size() > 0) || request.d->url.hasQuery())) {
            //Content-Type is mandatory. We can't say anything about the encoding, but x-www-form-urlencoded is the most likely to work.
            //This warning indicates a bug in application code not setting a required header.
            //Note that if using QHttpMultipart, the content-type is set in QNetworkAccessManagerPrivate::prepareMultipart already
            qWarning("content-type missing in HTTP POST, defaulting to application/x-www-form-urlencoded. Use QNetworkRequest::setHeader() to fix this problem.");
            ba += "Content-Type: application/x-www-form-urlencoded\r\n";
        }
        if (!request.d->uploadByteDevice && request.d->url.hasQuery()) {
            QByteArray query = request.d->url.query(QUrl::FullyEncoded).toLatin1();
            ba += "Content-Length: ";
            ba += QByteArray::number(query.size());
            ba += "\r\n\r\n";
            ba += query;
        } else {
            ba += "\r\n";
        }
    } else {
        ba += "\r\n";
    }
     return ba;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 23, as _ZN26QHttpNetworkRequestPrivateC1ERKS_
inline QHttpNetworkRequestPrivate::QHttpNetworkRequestPrivate(const QHttpNetworkRequestPrivate &other) // = default
    : QHttpNetworkHeaderPrivate(other),
      operation(other.operation),
      customVerb(other.customVerb),
      fullLocalServerName(other.fullLocalServerName),
      priority(other.priority),
      uploadByteDevice(other.uploadByteDevice),
      autoDecompress(other.autoDecompress),
      pipeliningAllowed(other.pipeliningAllowed),
      http2Allowed(other.http2Allowed),
      http2Direct(other.http2Direct),
      h2cAllowed(other.h2cAllowed),
      withCredentials(other.withCredentials),
      ssl(other.ssl),
      preConnect(other.preConnect),
      needResendWithCredentials(other.needResendWithCredentials),
      redirectCount(other.redirectCount),
      redirectPolicy(other.redirectPolicy),
      peerVerifyName(other.peerVerifyName)
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 45, as _ZN26QHttpNetworkRequestPrivateD1Ev
inline QHttpNetworkRequestPrivate::~QHttpNetworkRequestPrivate()
{
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 302, as _ZN29QHttpNetworkConnectionChannel16ensureConnectionEv
inline bool QHttpNetworkConnectionChannel::ensureConnection()
{
    if (!isInitialized)
        init();

    QAbstractSocket::SocketState socketState = QSocketAbstraction::socketState(socket);

    // resend this request after we receive the disconnected signal
    // If !socket->isOpen() then we have already called close() on the socket, but there was still a
    // pending connectToHost() for which we hadn't seen a connected() signal, yet. The connected()
    // has now arrived (as indicated by socketState != ClosingState), but we cannot send anything on
    // such a socket anymore.
    if (socketState == QAbstractSocket::ClosingState ||
            (socketState != QAbstractSocket::UnconnectedState && !socket->isOpen())) {
        if (reply)
            resendCurrent = true;
        return false;
    }

    // already trying to connect?
    if (socketState == QAbstractSocket::HostLookupState ||
        socketState == QAbstractSocket::ConnectingState) {
        return false;
    }

    // make sure that this socket is in a connected state, if not initiate
    // connection to the host.
    if (socketState != QAbstractSocket::ConnectedState) {
        // connect to the host if not already connected.
        state = QHttpNetworkConnectionChannel::ConnectingState;
        pendingEncrypt = ssl;

        // reset state
        pipeliningSupported = PipeliningSupportUnknown;
        authenticationCredentialsSent = false;
        proxyCredentialsSent = false;
        authenticator.detach();
        QAuthenticatorPrivate *priv = QAuthenticatorPrivate::getPrivate(authenticator);
        priv->hasFailed = false;
        proxyAuthenticator.detach();
        priv = QAuthenticatorPrivate::getPrivate(proxyAuthenticator);
        priv->hasFailed = false;

        // This workaround is needed since we use QAuthenticator for NTLM authentication. The "phase == Done"
        // is the usual criteria for emitting authentication signals. The "phase" is set to "Done" when the
        // last header for Authorization is generated by the QAuthenticator. Basic & Digest logic does not
        // check the "phase" for generating the Authorization header. NTLM authentication is a two stage
        // process & needs the "phase". To make sure the QAuthenticator uses the current username/password
        // the phase is reset to Start.
        priv = QAuthenticatorPrivate::getPrivate(authenticator);
        if (priv && priv->phase == QAuthenticatorPrivate::Done)
            priv->phase = QAuthenticatorPrivate::Start;
        priv = QAuthenticatorPrivate::getPrivate(proxyAuthenticator);
        if (priv && priv->phase == QAuthenticatorPrivate::Done)
            priv->phase = QAuthenticatorPrivate::Start;

        QString connectHost = connection->d_func()->hostName;
        quint16 connectPort = connection->d_func()->port;

        QHttpNetworkReply *potentialReply = connection->d_func()->predictNextRequestsReply();
        if (potentialReply) {
            QMetaObject::invokeMethod(potentialReply, "socketStartedConnecting", Qt::QueuedConnection);
        } else if (!h2RequestsToSend.isEmpty()) {
            QMetaObject::invokeMethod(std::as_const(h2RequestsToSend).first().second, "socketStartedConnecting", Qt::QueuedConnection);
        }

#ifndef QT_NO_NETWORKPROXY
        // HTTPS always use transparent proxy.
        if (connection->d_func()->networkProxy.type() != QNetworkProxy::NoProxy && !ssl) {
            connectHost = connection->d_func()->networkProxy.hostName();
            connectPort = connection->d_func()->networkProxy.port();
        }
        if (auto *abSocket = qobject_cast<QAbstractSocket *>(socket);
            abSocket && abSocket->proxy().type() == QNetworkProxy::HttpProxy) {
            // Make user-agent field available to HTTP proxy socket engine (QTBUG-17223)
            QByteArray value;
            // ensureConnection is called before any request has been assigned, but can also be
            // called again if reconnecting
            if (request.url().isEmpty()) {
                if (connection->connectionType()
                            == QHttpNetworkConnection::ConnectionTypeHTTP2Direct
                    || (connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2
                        && !h2RequestsToSend.isEmpty())) {
                    value = std::as_const(h2RequestsToSend).first().first.headerField("user-agent");
                } else {
                    value = connection->d_func()->predictNextRequest().headerField("user-agent");
                }
            } else {
                value = request.headerField("user-agent");
            }
            if (!value.isEmpty()) {
                QNetworkProxy proxy(abSocket->proxy());
                auto h = proxy.headers();
                h.replaceOrAppend(QHttpHeaders::WellKnownHeader::UserAgent, value);
                proxy.setHeaders(std::move(h));
                abSocket->setProxy(proxy);
            }
        }
#endif
        if (ssl) {
#ifndef QT_NO_SSL
            QSslSocket *sslSocket = qobject_cast<QSslSocket*>(socket);

            // check whether we can re-use an existing SSL session
            // (meaning another socket in this connection has already
            // performed a full handshake)
            if (auto ctx = connection->sslContext())
                QSslSocketPrivate::checkSettingSslContext(sslSocket, std::move(ctx));

            sslSocket->setPeerVerifyName(connection->d_func()->peerVerifyName);
            sslSocket->connectToHostEncrypted(connectHost, connectPort, QIODevice::ReadWrite, networkLayerPreference);
            // AXIVION DISABLE Qt-Security-QSslSocketIgnoreSslErrors: intentional behavior
            if (ignoreAllSslErrors)
                sslSocket->ignoreSslErrors();
            sslSocket->ignoreSslErrors(ignoreSslErrorsList);
            // AXIVION ENABLE Qt-Security-QSslSocketIgnoreSslErrors

            // limit the socket read buffer size. we will read everything into
            // the QHttpNetworkReply anyway, so let's grow only that and not
            // here and there.
            sslSocket->setReadBufferSize(64*1024);
#else
            // Need to dequeue the request so that we can emit the error.
            if (!reply)
                connection->d_func()->dequeueRequest(socket);
            connection->d_func()->emitReplyError(socket, reply, QNetworkReply::ProtocolUnknownError);
#endif
        } else {
            // In case of no proxy we can use the Unbuffered QTcpSocket
#ifndef QT_NO_NETWORKPROXY
            if (connection->d_func()->networkProxy.type() == QNetworkProxy::NoProxy
                    && connection->cacheProxy().type() == QNetworkProxy::NoProxy
                    && connection->transparentProxy().type() == QNetworkProxy::NoProxy) {
#endif
                if (auto *s = qobject_cast<QAbstractSocket *>(socket)) {
                    s->connectToHost(connectHost, connectPort,
                                     QIODevice::ReadWrite | QIODevice::Unbuffered,
                                     networkLayerPreference);
                    // For an Unbuffered QTcpSocket, the read buffer size has a special meaning.
                    s->setReadBufferSize(1 * 1024);
#if QT_CONFIG(localserver)
                } else if (auto *s = qobject_cast<QLocalSocket *>(socket)) {
                    s->connectToServer(connectHost);
#endif
                }
#ifndef QT_NO_NETWORKPROXY
            } else {
                auto *s = qobject_cast<QAbstractSocket *>(socket);
                Q_ASSERT(s);
                // limit the socket read buffer size. we will read everything into
                // the QHttpNetworkReply anyway, so let's grow only that and not
                // here and there.
                s->connectToHost(connectHost, connectPort, QIODevice::ReadWrite, networkLayerPreference);
                s->setReadBufferSize(64 * 1024);
            }
#endif
        }
        return false;
    }

    // This code path for ConnectedState
    if (pendingEncrypt) {
        // Let's only be really connected when we have received the encrypted() signal. Else the state machine seems to mess up
        // and corrupt the things sent to the server.
        return false;
    }

    return true;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 388, as _ZN29QHttpNetworkConnectionPrivate15copyCredentialsEiP14QAuthenticatorb
inline void QHttpNetworkConnectionPrivate::copyCredentials(int fromChannel, QAuthenticator *auth, bool isProxy)
{
    Q_ASSERT(auth);

    // NTLM and Negotiate do multi-phase authentication.
    // Copying credentialsbetween authenticators would mess things up.
    if (fromChannel >= 0) {
        QAuthenticatorPrivate *priv = QAuthenticatorPrivate::getPrivate(*auth);
        if (priv
            && (priv->method == QAuthenticatorPrivate::Ntlm
                || priv->method == QAuthenticatorPrivate::Negotiate)) {
            return;
        }
    }

    // select another channel
    QAuthenticator* otherAuth = nullptr;
    for (int i = 0; i < activeChannelCount; ++i) {
        if (i == fromChannel)
            continue;
        if (isProxy)
            otherAuth = &channels[i].proxyAuthenticator;
        else
            otherAuth = &channels[i].authenticator;
        // if the credentials are different, copy them
        if (otherAuth->user().compare(auth->user()))
            otherAuth->setUser(auth->user());
        if (otherAuth->password().compare(auth->password()))
            otherAuth->setPassword(auth->password());
    }
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 590, as _ZN29QHttpNetworkConnectionPrivate19createAuthorizationEP9QIODeviceR19QHttpNetworkRequest
inline void QHttpNetworkConnectionPrivate::createAuthorization(QIODevice *socket, QHttpNetworkRequest &request)
{
    Q_ASSERT(socket);

    QHttpNetworkConnectionChannel &channel = channels[indexOf(socket)];

    QAuthenticator *authenticator = &channel.authenticator;
    QAuthenticatorPrivate *priv = QAuthenticatorPrivate::getPrivate(*authenticator);
    // Send "Authorization" header, but not if it's NTLM and the socket is already authenticated.
    if (priv && priv->method != QAuthenticatorPrivate::None) {
        const bool ntlmNego = priv->method == QAuthenticatorPrivate::Ntlm
                || priv->method == QAuthenticatorPrivate::Negotiate;
        const bool authNeeded = channel.lastStatus == 401;
        const bool ntlmNegoOk = ntlmNego && authNeeded
                && (priv->phase != QAuthenticatorPrivate::Done
                    || !channel.authenticationCredentialsSent);
        const bool otherOk =
                !ntlmNego && (authNeeded || request.headerField("Authorization").isEmpty());
        if (ntlmNegoOk || otherOk) {
            QByteArray response = priv->calculateResponse(request.methodName(), request.uri(false),
                                                          request.url().host());
            request.setHeaderField("Authorization", response);
            channel.authenticationCredentialsSent = true;
        }
    }

#if QT_CONFIG(networkproxy)
    authenticator = &channel.proxyAuthenticator;
    priv = QAuthenticatorPrivate::getPrivate(*authenticator);
    // Send "Proxy-Authorization" header, but not if it's NTLM and the socket is already authenticated.
    if (priv && priv->method != QAuthenticatorPrivate::None) {
        const bool ntlmNego = priv->method == QAuthenticatorPrivate::Ntlm
                || priv->method == QAuthenticatorPrivate::Negotiate;
        const bool proxyAuthNeeded = channel.lastStatus == 407;
        const bool ntlmNegoOk = ntlmNego && proxyAuthNeeded
                && (priv->phase != QAuthenticatorPrivate::Done || !channel.proxyCredentialsSent);
        const bool otherOk = !ntlmNego;
        if (ntlmNegoOk || otherOk) {
            QByteArray response = priv->calculateResponse(request.methodName(), request.uri(false),
                                                          networkProxy.hostName());
            request.setHeaderField("Proxy-Authorization", response);
            channel.proxyCredentialsSent = true;
        }
    }
#endif // QT_CONFIG(networkproxy)
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 210, as _ZNK19QHttpNetworkRequest12isPreConnectEv
inline bool QHttpNetworkRequest::isPreConnect() const
{
    return d->preConnect;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 244, as _ZNK19QHttpNetworkRequest13contentLengthEv
inline qint64 QHttpNetworkRequest::contentLength() const
{
    return d->contentLength();
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 361, as _ZNK19QHttpNetworkRequest15withCredentialsEv
inline bool QHttpNetworkRequest::withCredentials() const
{
    return d->withCredentials;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 376, as _ZNK19QHttpNetworkRequest16uploadByteDeviceEv
inline QNonContiguousByteDevice* QHttpNetworkRequest::uploadByteDevice() const
{
    return d->uploadByteDevice;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 192, as _ZNK19QHttpNetworkRequest3urlEv
inline QUrl QHttpNetworkRequest::url() const
{
    return d->url;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 156, as _ZNK29QHttpNetworkConnectionPrivate7indexOfEP9QIODevice
inline int QHttpNetworkConnectionPrivate::indexOf(QIODevice *socket) const
{
    for (int i = 0; i < activeChannelCount; ++i)
        if (channels[i].socket == socket)
            return i;

    qFatal("Called with unknown socket object.");
    return 0;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 178, as _ZN19QHttpNetworkRequestC1ERK4QUrlNS_9OperationENS_8PriorityE
inline QHttpNetworkRequest::QHttpNetworkRequest(const QUrl &url, Operation operation, Priority priority)
    : d(new QHttpNetworkRequestPrivate(operation, priority, url))
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 188, as _ZN19QHttpNetworkRequestD1Ev
inline QHttpNetworkRequest::~QHttpNetworkRequest()
{
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 150, as _ZN21QHttp2ProtocolHandler23handleConnectionClosureEv
inline void QHttp2ProtocolHandler::handleConnectionClosure()
{
    // The channel has just received RemoteHostClosedError and since it will
    // not try (for HTTP/2) to re-connect, it's time to finish all replies
    // with error.

    // Maybe we still have some data to read and can successfully finish
    // a stream/request?
    _q_receiveReply();
    h2Connection->handleConnectionClosure();
}

//  from src/network/access/qabstractprotocolhandler.cpp, line 22, as _ZN24QAbstractProtocolHandler8setReplyEP17QHttpNetworkReply
inline void QAbstractProtocolHandler::setReply(QHttpNetworkReply *reply)
{
    m_reply = reply;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 258, as _ZN29QHttpNetworkConnectionChannel15_q_receiveReplyEv
inline void QHttpNetworkConnectionChannel::_q_receiveReply()
{
    Q_ASSERT(protocolHandler);
    if (waitingForPotentialAbort) {
        needInvokeReceiveReply = true;
        return;
    }
    protocolHandler->_q_receiveReply();
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 814, as _ZN29QHttpNetworkConnectionChannel20resendCurrentRequestEv
inline void QHttpNetworkConnectionChannel::resendCurrentRequest()
{
    requeueCurrentlyPipelinedRequests();
    if (reply)
        resendCurrent = true;
    if (qobject_cast<QHttpNetworkConnection*>(connection))
        QMetaObject::invokeMethod(connection, "_q_startNextRequest", Qt::QueuedConnection);
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 615, as _ZN29QHttpNetworkConnectionChannel33requeueCurrentlyPipelinedRequestsEv
inline void QHttpNetworkConnectionChannel::requeueCurrentlyPipelinedRequests()
{
    for (int i = 0; i < alreadyPipelinedRequests.size(); i++)
        connection->d_func()->requeueRequest(alreadyPipelinedRequests.at(i));
    alreadyPipelinedRequests.clear();

    // only run when the QHttpNetworkConnection is not currently being destructed, e.g.
    // this function is called from _q_disconnected which is called because
    // of ~QHttpNetworkConnectionPrivate
    if (qobject_cast<QHttpNetworkConnection*>(connection))
        QMetaObject::invokeMethod(connection, "_q_startNextRequest", Qt::QueuedConnection);
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 726, as _ZN29QHttpNetworkConnectionPrivate14dequeueRequestEP9QIODevice
inline bool QHttpNetworkConnectionPrivate::dequeueRequest(QIODevice *socket)
{
    int i = 0;
    if (socket)
        i = indexOf(socket);

    if (!highPriorityQueue.isEmpty()) {
        // remove from queue before sendRequest! else we might pipeline the same request again
        HttpMessagePair messagePair = highPriorityQueue.takeLast();
        if (!messagePair.second->d_func()->requestIsPrepared)
            prepareRequest(messagePair);
        updateChannel(i, messagePair);
        return true;
    }

    if (!lowPriorityQueue.isEmpty()) {
        // remove from queue before sendRequest! else we might pipeline the same request again
        HttpMessagePair messagePair = lowPriorityQueue.takeLast();
        if (!messagePair.second->d_func()->requestIsPrepared)
            prepareRequest(messagePair);
        updateChannel(i, messagePair);
        return true;
    }
    return false;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 170, as _ZN29QHttpNetworkConnectionPrivate22shouldEmitChannelErrorEP9QIODevice
inline bool QHttpNetworkConnectionPrivate::shouldEmitChannelError(QIODevice *socket)
{
    Q_Q(QHttpNetworkConnection);

    bool emitError = true;
    int i = indexOf(socket);
    int otherSocket = (i == 0 ? 1 : 0);

    // If the IPv4 connection still isn't started we need to start it now.
    if (delayedConnectionTimer.isActive()) {
        delayedConnectionTimer.stop();
        channels[otherSocket].ensureConnection();
    }

    if (activeChannelCount < channelCount) {
        if (networkLayerState == HostLookupPending || networkLayerState == IPv4or6)
            networkLayerState = QHttpNetworkConnectionPrivate::Unknown;
        channels[0].close();
        emitError = true;
    } else {
        if (networkLayerState == HostLookupPending || networkLayerState == IPv4or6) {
            if (channels[otherSocket].isSocketBusy() && (channels[otherSocket].state != QHttpNetworkConnectionChannel::ClosingState)) {
                // this was the first socket to fail.
                channels[i].close();
                emitError = false;
            }
            else {
                // Both connection attempts has failed.
                networkLayerState = QHttpNetworkConnectionPrivate::Unknown;
                channels[i].close();
                emitError = true;
            }
        } else {
            if (((networkLayerState == QHttpNetworkConnectionPrivate::IPv4) && (channels[i].networkLayerPreference != QAbstractSocket::IPv4Protocol))
                || ((networkLayerState == QHttpNetworkConnectionPrivate::IPv6) && (channels[i].networkLayerPreference != QAbstractSocket::IPv6Protocol))) {
                // First connection worked so this is the second one to complete and it failed.
                channels[i].close();
                QMetaObject::invokeMethod(q, "_q_startNextRequest", Qt::QueuedConnection);
                emitError = false;
            }
            if (networkLayerState == QHttpNetworkConnectionPrivate::Unknown)
                qWarning("We got a connection error when networkLayerState is Unknown");
        }
    }
    return emitError;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 291, as _ZNK19QHttpNetworkRequest9operationEv
inline QHttpNetworkRequest::Operation QHttpNetworkRequest::operation() const
{
    return d->operation;
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

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 843, as _ZNK29QHttpNetworkConnectionChannel17h2ProtocolHandlerEv
inline QHttp2ProtocolHandler *QHttpNetworkConnectionChannel::h2ProtocolHandler() const noexcept
{
    if (!protocolHandler)
        return nullptr;
    const auto type = connection->connectionType();
    if (type == QHttpNetworkConnection::ConnectionTypeHTTP2Direct
        || (type == QHttpNetworkConnection::ConnectionTypeHTTP2 && switchedToHttp2)) {
        return static_cast<QHttp2ProtocolHandler *>(protocolHandler.get());
    }
    return nullptr;
}
//  -----------------------------------------------------------------------

//  void QHttpProtocolHandler::_q_receiveReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpProtocolHandler15_q_receiveReplyEv(
    QHttpProtocolHandler *self) {
  self->_q_receiveReply();
}

//  void QHttpProtocolHandler::_q_readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpProtocolHandler12_q_readyReadEv(
    QHttpProtocolHandler *self) {
  self->_q_readyRead();
}

//  bool QHttpProtocolHandler::sendRequest()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QHttpProtocolHandler11sendRequestEv(
    QHttpProtocolHandler *self) {
  return self->sendRequest();
}

//  QHttpProtocolHandler::~QHttpProtocolHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpProtocolHandlerD1Ev(QHttpProtocolHandler *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
