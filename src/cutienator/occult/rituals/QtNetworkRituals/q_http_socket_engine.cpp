//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpsocketengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpsocketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkinterface.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qabstractsocketengine_p.h>
#include <QtNetwork/private/qnativesocketengine_p.h>
#include <QtCore/qmutex.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/private/qhttpnetworkreply_p.h>
#include <QtNetwork/private/qhttpnetworkconnection_p.h>
#ifndef QT_NO_SSL
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#    include <QtNetwork/qsslconfiguration.h>
#endif
#include <QtNetwork/private/qdecompresshelper_p.h>
#include <QtNetwork/private/qhttpnetworkheader_p.h>
#include <QtNetwork/private/qhttpsocketengine_p.h>
#include <QtNetwork/qtcpsocket.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qurl.h>
#include <QtNetwork/private/qhttpnetworkreply_p.h>
#include <QtCore/private/qiodevice_p.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtNetwork/qnetworkinterface.h>
#if !defined(QT_NO_NETWORKPROXY)
#include <QtCore/qdebug.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/socket/qabstractsocketengine.cpp, line 120, as _ZN21QAbstractSocketEngine16readNotificationEv
inline void QAbstractSocketEngine::readNotification()
{
    if (QAbstractSocketEngineReceiver *receiver = d_func()->receiver)
        receiver->readNotification();
}

//  from src/network/socket/qabstractsocketengine.cpp, line 126, as _ZN21QAbstractSocketEngine17writeNotificationEv
inline void QAbstractSocketEngine::writeNotification()
{
    if (QAbstractSocketEngineReceiver *receiver = d_func()->receiver)
        receiver->writeNotification();
}

//  from src/network/socket/qabstractsocketengine.cpp, line 144, as _ZN21QAbstractSocketEngine22connectionNotificationEv
inline void QAbstractSocketEngine::connectionNotification()
{
    if (QAbstractSocketEngineReceiver *receiver = d_func()->receiver)
        receiver->connectionNotification();
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

//  from src/network/socket/qabstractsocketengine.cpp, line 184, as _ZN21QAbstractSocketEngine11setProtocolEN15QAbstractSocket20NetworkLayerProtocolE
inline void QAbstractSocketEngine::setProtocol(QAbstractSocket::NetworkLayerProtocol protocol)
{
    d_func()->socketProtocol = protocol;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 174, as _ZN21QAbstractSocketEngine13setSocketTypeEN15QAbstractSocket10SocketTypeE
inline void QAbstractSocketEngine::setSocketType(QAbstractSocket::SocketType socketType)
{
    d_func()->socketType = socketType;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 498, as _ZN24QHttpNetworkReplyPrivate11parseHeaderE14QByteArrayView
inline void QHttpNetworkReplyPrivate::parseHeader(QByteArrayView header)
{
    parser.parseHeaders(header);
}

//  from src/network/access/qhttpnetworkreply.cpp, line 431, as _ZN24QHttpNetworkReplyPrivate11parseStatusE14QByteArrayView
inline bool QHttpNetworkReplyPrivate::parseStatus(QByteArrayView status)
{
    return parser.parseStatus(status);
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

//  from src/network/access/qhttpnetworkheader.cpp, line 43, as _ZNK25QHttpNetworkHeaderPrivate17headerFieldValuesE14QByteArrayView
inline QList<QByteArray> QHttpNetworkHeaderPrivate::headerFieldValues(QByteArrayView name) const
{
    return parser.headerFieldValues(name);
}

//  from src/network/socket/qhttpsocketengine.cpp, line 28, as _ZN17QHttpSocketEngineD1Ev
#if !defined(QT_NO_NETWORKPROXY)
inline QHttpSocketEngine::~QHttpSocketEngine()
{
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 32, as _ZN17QHttpSocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::initialize(QAbstractSocket::SocketType type, QAbstractSocket::NetworkLayerProtocol protocol)
{
    Q_D(QHttpSocketEngine);
    if (type != QAbstractSocket::TcpSocket)
        return false;

    setProtocol(protocol);
    setSocketType(type);
    d->socket = new QTcpSocket(this);
    d->reply = new QHttpNetworkReply(QUrl(), this);

    // Explicitly disable proxying on the proxy socket itself to avoid
    // unwanted recursion.
    d->socket->setProxy(QNetworkProxy::NoProxy);

    // Intercept all the signals.
    connect(d->socket, SIGNAL(connected()),
            this, SLOT(slotSocketConnected()),
            Qt::DirectConnection);
    connect(d->socket, SIGNAL(disconnected()),
            this, SLOT(slotSocketDisconnected()),
            Qt::DirectConnection);
    connect(d->socket, SIGNAL(readyRead()),
            this, SLOT(slotSocketReadNotification()),
            Qt::DirectConnection);
    connect(d->socket, SIGNAL(bytesWritten(qint64)),
            this, SLOT(slotSocketBytesWritten()),
            Qt::DirectConnection);
    connect(d->socket, SIGNAL(errorOccurred(QAbstractSocket::SocketError)),
            this, SLOT(slotSocketError(QAbstractSocket::SocketError)),
            Qt::DirectConnection);
    connect(d->socket, SIGNAL(stateChanged(QAbstractSocket::SocketState)),
            this, SLOT(slotSocketStateChanged(QAbstractSocket::SocketState)),
            Qt::DirectConnection);

    return true;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 70, as _ZN17QHttpSocketEngine10initializeExN15QAbstractSocket11SocketStateE
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::initialize(qintptr, QAbstractSocket::SocketState)
{
    return false;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 75, as _ZN17QHttpSocketEngine8setProxyERK13QNetworkProxy
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::setProxy(const QNetworkProxy &proxy)
{
    Q_D(QHttpSocketEngine);
    d->proxy = proxy;
    QString user = proxy.user();
    if (!user.isEmpty())
        d->authenticator.setUser(user);
    QString password = proxy.password();
    if (!password.isEmpty())
        d->authenticator.setPassword(password);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 87, as _ZNK17QHttpSocketEngine16socketDescriptorEv
#if !defined(QT_NO_NETWORKPROXY)
inline qintptr QHttpSocketEngine::socketDescriptor() const
{
    Q_D(const QHttpSocketEngine);
    return d->socket ? d->socket->socketDescriptor() : -1;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 93, as _ZNK17QHttpSocketEngine7isValidEv
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::isValid() const
{
    Q_D(const QHttpSocketEngine);
    return d->socket;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 131, as _ZN17QHttpSocketEngine13connectToHostERK12QHostAddresst
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::connectToHost(const QHostAddress &address, quint16 port)
{
    Q_D(QHttpSocketEngine);

    setPeerAddress(address);
    setPeerPort(port);
    d->peerName.clear();

    return connectInternal();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 142, as _ZN17QHttpSocketEngine19connectToHostByNameERK7QStringt
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::connectToHostByName(const QString &hostname, quint16 port)
{
    Q_D(QHttpSocketEngine);

    setPeerAddress(QHostAddress());
    setPeerPort(port);
    d->peerName = hostname;

    return connectInternal();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 175, as _ZN17QHttpSocketEngine5closeEv
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::close()
{
    Q_D(QHttpSocketEngine);
    if (d->socket) {
        d->socket->close();
        delete d->socket;
        d->socket = nullptr;
    }
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 185, as _ZNK17QHttpSocketEngine14bytesAvailableEv
#if !defined(QT_NO_NETWORKPROXY)
inline qint64 QHttpSocketEngine::bytesAvailable() const
{
    Q_D(const QHttpSocketEngine);
    return d->socket ? d->socket->bytesAvailable() : 0;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 213, as _ZN17QHttpSocketEngine5writeEPKcx
#if !defined(QT_NO_NETWORKPROXY)
inline qint64 QHttpSocketEngine::write(const char *data, qint64 len)
{
    Q_D(QHttpSocketEngine);
    return d->socket->write(data, len);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 237, as _ZNK17QHttpSocketEngine18multicastInterfaceEv
#if !defined(QT_NO_NETWORKPROXY)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
inline QNetworkInterface QHttpSocketEngine::multicastInterface() const
{
    return QNetworkInterface();
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 250, as _ZNK17QHttpSocketEngine19hasPendingDatagramsEv
#if !defined(QT_NO_NETWORKPROXY)
#if !defined(QT_NO_UDPSOCKET)
inline bool QHttpSocketEngine::hasPendingDatagrams() const
{
    qWarning("Operation is not supported");
    return false;
}
#endif  // !defined(QT_NO_UDPSOCKET)
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 256, as _ZNK17QHttpSocketEngine19pendingDatagramSizeEv
#if !defined(QT_NO_NETWORKPROXY)
#if !defined(QT_NO_UDPSOCKET)
inline qint64 QHttpSocketEngine::pendingDatagramSize() const
{
    qWarning("Operation is not supported");
    return -1;
}
#endif  // !defined(QT_NO_UDPSOCKET)
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 277, as _ZNK17QHttpSocketEngine12bytesToWriteEv
#if !defined(QT_NO_NETWORKPROXY)
inline qint64 QHttpSocketEngine::bytesToWrite() const
{
    Q_D(const QHttpSocketEngine);
    if (d->socket) {
        return d->socket->bytesToWrite();
    } else {
        return 0;
    }
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 287, as _ZNK17QHttpSocketEngine6optionEN21QAbstractSocketEngine12SocketOptionE
#if !defined(QT_NO_NETWORKPROXY)
inline int QHttpSocketEngine::option(SocketOption option) const
{
    Q_D(const QHttpSocketEngine);
    if (d->socket) {
        // convert the enum and call the real socket
        if (option == QAbstractSocketEngine::LowDelayOption)
            return d->socket->socketOption(QAbstractSocket::LowDelayOption).toInt();
        if (option == QAbstractSocketEngine::KeepAliveOption)
            return d->socket->socketOption(QAbstractSocket::KeepAliveOption).toInt();
    }
    return -1;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 300, as _ZN17QHttpSocketEngine9setOptionEN21QAbstractSocketEngine12SocketOptionEi
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::setOption(SocketOption option, int value)
{
    Q_D(QHttpSocketEngine);
    if (d->socket) {
        // convert the enum and call the real socket
        if (option == QAbstractSocketEngine::LowDelayOption)
            d->socket->setSocketOption(QAbstractSocket::LowDelayOption, value);
        if (option == QAbstractSocketEngine::KeepAliveOption)
            d->socket->setSocketOption(QAbstractSocket::KeepAliveOption, value);
        return true;
    }
    return false;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 314, as _ZN17QHttpSocketEngine11waitForReadE14QDeadlineTimerPb
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::waitForRead(QDeadlineTimer deadline, bool *timedOut)
{
    Q_D(const QHttpSocketEngine);

    if (!d->socket || d->socket->state() == QAbstractSocket::UnconnectedState)
        return false;

    // Wait for more data if nothing is available.
    if (!d->socket->bytesAvailable()) {
        if (!d->socket->waitForReadyRead(deadline.remainingTime())) {
            if (d->socket->state() == QAbstractSocket::UnconnectedState)
                return true;
            setError(d->socket->error(), d->socket->errorString());
            if (timedOut && d->socket->error() == QAbstractSocket::SocketTimeoutError)
                *timedOut = true;
            return false;
        }
    }

    waitForProtocolHandshake(deadline);

    // Report any error that may occur.
    if (d->state != Connected) {
        setError(d->socket->error(), d->socket->errorString());
        if (timedOut && d->socket->error() == QAbstractSocket::SocketTimeoutError)
            *timedOut = true;
        return false;
    }
    return true;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 345, as _ZN17QHttpSocketEngine12waitForWriteE14QDeadlineTimerPb
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::waitForWrite(QDeadlineTimer deadline, bool *timedOut)
{
    Q_D(const QHttpSocketEngine);

    // If we're connected, just forward the call.
    if (d->state == Connected) {
        if (d->socket->bytesToWrite()) {
            if (!d->socket->waitForBytesWritten(deadline.remainingTime())) {
                if (d->socket->error() == QAbstractSocket::SocketTimeoutError && timedOut)
                    *timedOut = true;
                return false;
            }
        }
        return true;
    }

    waitForProtocolHandshake(deadline);

    // Report any error that may occur.
    if (d->state != Connected) {
//        setError(d->socket->error(), d->socket->errorString());
        if (timedOut && d->socket->error() == QAbstractSocket::SocketTimeoutError)
            *timedOut = true;
    }

    return true;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 373, as _ZN17QHttpSocketEngine18waitForReadOrWriteEPbS0_bb14QDeadlineTimerS0_
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::waitForReadOrWrite(bool *readyToRead, bool *readyToWrite,
                                           bool checkRead, bool checkWrite,
                                           QDeadlineTimer deadline, bool *timedOut)
{
    Q_UNUSED(checkRead);

    if (!checkWrite) {
        // Not interested in writing? Then we wait for read notifications.
        bool canRead = waitForRead(deadline, timedOut);
        if (readyToRead)
            *readyToRead = canRead;
        return canRead;
    }

    // Interested in writing? Then we wait for write notifications.
    bool canWrite = waitForWrite(deadline, timedOut);
    if (readyToWrite)
        *readyToWrite = canWrite;
    return canWrite;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 394, as _ZNK17QHttpSocketEngine24waitForProtocolHandshakeE14QDeadlineTimer
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::waitForProtocolHandshake(QDeadlineTimer deadline) const
{
    Q_D(const QHttpSocketEngine);

    // If we're not connected yet, wait until we are (and until bytes have
    // been received, i.e. the socket has connected, we have sent the
    // greeting, and then received the response), or until an error occurs.
    while (d->state != Connected && d->socket->waitForReadyRead(deadline.remainingTime())) {
        // Loop while the protocol handshake is taking place.
    }
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 406, as _ZNK17QHttpSocketEngine25isReadNotificationEnabledEv
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::isReadNotificationEnabled() const
{
    Q_D(const QHttpSocketEngine);
    return d->readNotificationEnabled;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 412, as _ZN17QHttpSocketEngine26setReadNotificationEnabledEb
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::setReadNotificationEnabled(bool enable)
{
    Q_D(QHttpSocketEngine);
    if (d->readNotificationEnabled == enable) {
        // When already enabled, we still need to check for
        // buffered data. The inner socket may have data in its user-space
        // buffer that won't trigger a new OS-level read notification.
        // Without this check, partial reads leave data stranded forever.
        if (enable && bytesAvailable() > 0)
            emitReadNotification();
        return;
    }

    d->readNotificationEnabled = enable;
    if (enable) {
        // Enabling read notification can trigger a notification.
        if (bytesAvailable()) {
            slotSocketReadNotification();
        } else if (d->socket && d->socket->state() == QAbstractSocket::UnconnectedState) {
            emitReadNotification();
        }
    }
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 436, as _ZNK17QHttpSocketEngine26isWriteNotificationEnabledEv
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::isWriteNotificationEnabled() const
{
    Q_D(const QHttpSocketEngine);
    return d->writeNotificationEnabled;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 442, as _ZN17QHttpSocketEngine27setWriteNotificationEnabledEb
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::setWriteNotificationEnabled(bool enable)
{
    Q_D(QHttpSocketEngine);
    d->writeNotificationEnabled = enable;
    if (enable && d->state == Connected && d->socket->state() == QAbstractSocket::ConnectedState)
        QMetaObject::invokeMethod(this, "writeNotification", Qt::QueuedConnection);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 450, as _ZNK17QHttpSocketEngine30isExceptionNotificationEnabledEv
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::isExceptionNotificationEnabled() const
{
    Q_D(const QHttpSocketEngine);
    return d->exceptNotificationEnabled;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 456, as _ZN17QHttpSocketEngine31setExceptionNotificationEnabledEb
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::setExceptionNotificationEnabled(bool enable)
{
    Q_D(QHttpSocketEngine);
    d->exceptNotificationEnabled = enable;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 462, as _ZN17QHttpSocketEngine19slotSocketConnectedEv
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::slotSocketConnected()
{
    Q_D(QHttpSocketEngine);

    // Send the greeting.
    const char method[] = "CONNECT";
    QByteArray peerAddress = d->peerName.isEmpty() ?
                             d->peerAddress.toString().toLatin1() :
                             QUrl::toAce(d->peerName);
    QByteArray path = peerAddress + ':' + QByteArray::number(d->peerPort);
    QByteArray data = method;
    data += ' ';
    data += path;
    data += " HTTP/1.1\r\n";
    data += "Proxy-Connection: keep-alive\r\n";
    data += "Host: " + peerAddress + "\r\n";
    const auto headers = d->proxy.headers();
    if (!headers.contains(QHttpHeaders::WellKnownHeader::UserAgent))
        data += "User-Agent: Mozilla/5.0\r\n";
    for (qsizetype i = 0; i < headers.size(); ++i) {
        const auto name = headers.nameAt(i);
        data += QByteArrayView(name.data(), name.size()) + ": "
                + headers.valueAt(i) + "\r\n";
    }
    QAuthenticatorPrivate *priv = QAuthenticatorPrivate::getPrivate(d->authenticator);
    //qDebug() << "slotSocketConnected: priv=" << priv << (priv ? (int)priv->method : -1);
    if (priv && priv->method != QAuthenticatorPrivate::None) {
        d->credentialsSent = true;
        data += "Proxy-Authorization: " + priv->calculateResponse(method, path, d->proxy.hostName());
        data += "\r\n";
    }
    data += "\r\n";
//     qDebug() << ">>>>>>>> sending request" << this;
//     qDebug() << data;
//     qDebug(">>>>>>>");
    d->socket->write(data);
    d->state = ConnectSent;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 501, as _ZN17QHttpSocketEngine22slotSocketDisconnectedEv
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::slotSocketDisconnected()
{
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 701, as _ZN17QHttpSocketEngine22slotSocketBytesWrittenEv
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::slotSocketBytesWritten()
{
    Q_D(QHttpSocketEngine);
    if (d->state == Connected && d->writeNotificationEnabled)
        emitWriteNotification();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 740, as _ZN17QHttpSocketEngine22slotSocketStateChangedEN15QAbstractSocket11SocketStateE
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::slotSocketStateChanged(QAbstractSocket::SocketState state)
{
    Q_UNUSED(state);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 745, as _ZN17QHttpSocketEngine27emitPendingReadNotificationEv
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::emitPendingReadNotification()
{
    Q_D(QHttpSocketEngine);
    d->readNotificationPending = false;
    if (d->readNotificationEnabled)
        readNotification();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 753, as _ZN17QHttpSocketEngine28emitPendingWriteNotificationEv
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::emitPendingWriteNotification()
{
    Q_D(QHttpSocketEngine);
    d->writeNotificationPending = false;
    if (d->writeNotificationEnabled)
        writeNotification();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 761, as _ZN17QHttpSocketEngine33emitPendingConnectionNotificationEv
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::emitPendingConnectionNotification()
{
    Q_D(QHttpSocketEngine);
    d->connectionNotificationPending = false;
    connectionNotification();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 768, as _ZN17QHttpSocketEngine20emitReadNotificationEv
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::emitReadNotification()
{
    Q_D(QHttpSocketEngine);
    // if there is a connection notification pending we have to emit the readNotification
    // in case there is connection error. This is only needed for Windows, but it does not
    // hurt in other cases.
    if ((d->readNotificationEnabled && !d->readNotificationPending) || d->connectionNotificationPending) {
        d->readNotificationPending = true;
        QMetaObject::invokeMethod(this, "emitPendingReadNotification", Qt::QueuedConnection);
    }
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 780, as _ZN17QHttpSocketEngine21emitWriteNotificationEv
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::emitWriteNotification()
{
    Q_D(QHttpSocketEngine);
    if (d->writeNotificationEnabled && !d->writeNotificationPending) {
        d->writeNotificationPending = true;
        QMetaObject::invokeMethod(this, "emitPendingWriteNotification", Qt::QueuedConnection);
    }
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 789, as _ZN17QHttpSocketEngine26emitConnectionNotificationEv
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::emitConnectionNotification()
{
    Q_D(QHttpSocketEngine);
    if (!d->connectionNotificationPending) {
        d->connectionNotificationPending = true;
        QMetaObject::invokeMethod(this, "emitPendingConnectionNotification", Qt::QueuedConnection);
    }
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 668, as _ZN17QHttpSocketEngine14readHttpHeaderEv
#if !defined(QT_NO_NETWORKPROXY)
inline bool QHttpSocketEngine::readHttpHeader()
{
    Q_D(QHttpSocketEngine);

    if (d->state != ReadResponseHeader)
        return false;

    bool ok = true;
    if (d->reply->d_func()->state == QHttpNetworkReplyPrivate::NothingDoneState) {
        // do not keep old content sizes, status etc. around
        d->reply->d_func()->clearHttpLayerInformation();
        d->reply->d_func()->state = QHttpNetworkReplyPrivate::ReadingStatusState;
    }
    if (d->reply->d_func()->state == QHttpNetworkReplyPrivate::ReadingStatusState) {
        ok = d->reply->d_func()->readStatus(d->socket) != -1;
        if (ok && d->reply->d_func()->state == QHttpNetworkReplyPrivate::ReadingStatusState)
            return true; //Not done parsing headers yet, wait for more data
    }
    if (ok && d->reply->d_func()->state == QHttpNetworkReplyPrivate::ReadingHeaderState) {
        ok = d->reply->d_func()->readHeader(d->socket) != -1;
        if (ok && d->reply->d_func()->state == QHttpNetworkReplyPrivate::ReadingHeaderState)
            return true; //Not done parsing headers yet, wait for more data
    }
    if (ok) {
        bool contentLengthOk;
        int contentLength = d->reply->headerField("Content-Length").toInt(&contentLengthOk);
        if (contentLengthOk && contentLength > 0)
            d->pendingResponseData = contentLength;
        d->state = ReadResponseContent; // we are done reading the header
    }
    return ok;
}
#endif  // !defined(QT_NO_NETWORKPROXY)
//  -----------------------------------------------------------------------

//  A QHttpSocketEngine that Python can take functions over in. Every QHttpSocketEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall0)(const void *, int, int, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall1)(const void *, qintptr, int, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef qintptr (*CuteQHttpSocketEngineCall2)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall3)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall4)(const void *, const QHostAddress *, quint16, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall5)(const void *, const QString *, quint16, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall6)(const void *, const QHostAddress *, quint16, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall7)(const void *, int, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef qintptr (*CuteQHttpSocketEngineCall8)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQHttpSocketEngineCall9)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef qint64 (*CuteQHttpSocketEngineCall10)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall11)(const void *, const QHostAddress *, const QNetworkInterface *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall12)(const void *, const QHostAddress *, const QNetworkInterface *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef const QNetworkInterface * (*CuteQHttpSocketEngineCall13)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall14)(const void *, const QNetworkInterface *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall15)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef qint64 (*CuteQHttpSocketEngineCall16)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef qint64 (*CuteQHttpSocketEngineCall17)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef int (*CuteQHttpSocketEngineCall18)(const void *, int, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall19)(const void *, int, int, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall20)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQHttpSocketEngineCall21)(const void *, bool, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall22)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQHttpSocketEngineCall23)(const void *, bool, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQHttpSocketEngineCall24)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQHttpSocketEngineCall25)(const void *, bool, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpSocketEngineCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpSocketEngineCall27)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpSocketEngineCall28)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpSocketEngineCall29)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpSocketEngineCall30)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpSocketEngineCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpSocketEngineCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHttpSocketEngine : public QHttpSocketEngine {
public:
  using QHttpSocketEngine::QHttpSocketEngine;
  void *taken[33] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine10initializeExN15QAbstractSocket11SocketStateE")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine16socketDescriptorEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine7isValidEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine13connectToHostERK12QHostAddresst")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine19connectToHostByNameERK7QStringt")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine4bindERK12QHostAddresst")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine6listenEi")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine6acceptEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine5closeEv")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine14bytesAvailableEv")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine18joinMulticastGroupERK12QHostAddressRK17QNetworkInterface")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine19leaveMulticastGroupERK12QHostAddressRK17QNetworkInterface")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine18multicastInterfaceEv")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine21setMulticastInterfaceERK17QNetworkInterface")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine19hasPendingDatagramsEv")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine19pendingDatagramSizeEv")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine12bytesToWriteEv")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine6optionENS_12SocketOptionE")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine9setOptionENS_12SocketOptionEi")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine25isReadNotificationEnabledEv")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine26setReadNotificationEnabledEb")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine26isWriteNotificationEnabledEv")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine27setWriteNotificationEnabledEb")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine30isExceptionNotificationEnabledEv")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine31setExceptionNotificationEnabledEb")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::initialize(QAbstractSocket::SocketType type,
  //      QAbstractSocket::NetworkLayerProtocol protocol)
  bool initialize(
      QAbstractSocket::SocketType type,
      QAbstractSocket::NetworkLayerProtocol protocol) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHttpSocketEngineCall0 call = reinterpret_cast<CuteQHttpSocketEngineCall0>(taken[0]);
      bool given = call(this, static_cast<int>(type), static_cast<int>(protocol), &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::initialize(type, protocol);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::initialize(qintptr socketDescriptor,
  //      QAbstractSocket::SocketState socketState)
  bool initialize(
      qintptr socketDescriptor,
      QAbstractSocket::SocketState socketState) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHttpSocketEngineCall1 call = reinterpret_cast<CuteQHttpSocketEngineCall1>(taken[1]);
      bool given = call(this, socketDescriptor, static_cast<int>(socketState), &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::initialize(socketDescriptor, socketState);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  qintptr QHttpSocketEngine::socketDescriptor() const
  qintptr socketDescriptor() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQHttpSocketEngineCall2 call = reinterpret_cast<CuteQHttpSocketEngineCall2>(taken[2]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::socketDescriptor();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::isValid() const
  bool isValid() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHttpSocketEngineCall3 call = reinterpret_cast<CuteQHttpSocketEngineCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::isValid();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::connectToHost(const QHostAddress &address,
  //      quint16 port)
  bool connectToHost(const QHostAddress &address, quint16 port) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHttpSocketEngineCall4 call = reinterpret_cast<CuteQHttpSocketEngineCall4>(taken[4]);
      bool given = call(this, &address, port, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::connectToHost(address, port);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::connectToHostByName(const QString &name,
  //      quint16 port)
  bool connectToHostByName(const QString &name, quint16 port) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHttpSocketEngineCall5 call = reinterpret_cast<CuteQHttpSocketEngineCall5>(taken[5]);
      bool given = call(this, &name, port, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::connectToHostByName(name, port);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::bind(const QHostAddress &address, quint16
  //      port)
  bool bind(const QHostAddress &address, quint16 port) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHttpSocketEngineCall6 call = reinterpret_cast<CuteQHttpSocketEngineCall6>(taken[6]);
      bool given = call(this, &address, port, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::bind(address, port);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::listen(int backlog)
  bool listen(int backlog) override {
    if (taken[7]) {
      int handled = 0;
      CuteQHttpSocketEngineCall7 call = reinterpret_cast<CuteQHttpSocketEngineCall7>(taken[7]);
      bool given = call(this, backlog, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::listen(backlog);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  qintptr QHttpSocketEngine::accept()
  qintptr accept() override {
    if (taken[8]) {
      int handled = 0;
      CuteQHttpSocketEngineCall8 call = reinterpret_cast<CuteQHttpSocketEngineCall8>(taken[8]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::accept();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  void QHttpSocketEngine::close()
  void close() override {
    if (taken[9]) {
      int handled = 0;
      CuteQHttpSocketEngineCall9 call = reinterpret_cast<CuteQHttpSocketEngineCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QHttpSocketEngine::close();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  qint64 QHttpSocketEngine::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQHttpSocketEngineCall10 call = reinterpret_cast<CuteQHttpSocketEngineCall10>(taken[10]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::bytesAvailable();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::joinMulticastGroup(const QHostAddress
  //      &groupAddress, const QNetworkInterface &iface)
  bool joinMulticastGroup(
      const QHostAddress &groupAddress,
      const QNetworkInterface &iface) override {
    if (taken[11]) {
      int handled = 0;
      CuteQHttpSocketEngineCall11 call = reinterpret_cast<CuteQHttpSocketEngineCall11>(taken[11]);
      bool given = call(this, &groupAddress, &iface, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::joinMulticastGroup(groupAddress, iface);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::leaveMulticastGroup(const QHostAddress
  //      &groupAddress, const QNetworkInterface &iface)
  bool leaveMulticastGroup(
      const QHostAddress &groupAddress,
      const QNetworkInterface &iface) override {
    if (taken[12]) {
      int handled = 0;
      CuteQHttpSocketEngineCall12 call = reinterpret_cast<CuteQHttpSocketEngineCall12>(taken[12]);
      bool given = call(this, &groupAddress, &iface, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::leaveMulticastGroup(groupAddress, iface);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  QNetworkInterface QHttpSocketEngine::multicastInterface() const
  QNetworkInterface multicastInterface() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQHttpSocketEngineCall13 call = reinterpret_cast<CuteQHttpSocketEngineCall13>(taken[13]);
      const QNetworkInterface * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QHttpSocketEngine::multicastInterface();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::setMulticastInterface(const QNetworkInterface
  //      &iface)
  bool setMulticastInterface(const QNetworkInterface &iface) override {
    if (taken[14]) {
      int handled = 0;
      CuteQHttpSocketEngineCall14 call = reinterpret_cast<CuteQHttpSocketEngineCall14>(taken[14]);
      bool given = call(this, &iface, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::setMulticastInterface(iface);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::hasPendingDatagrams() const
  bool hasPendingDatagrams() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQHttpSocketEngineCall15 call = reinterpret_cast<CuteQHttpSocketEngineCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::hasPendingDatagrams();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  qint64 QHttpSocketEngine::pendingDatagramSize() const
  qint64 pendingDatagramSize() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQHttpSocketEngineCall16 call = reinterpret_cast<CuteQHttpSocketEngineCall16>(taken[16]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::pendingDatagramSize();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // !defined(QT_NO_UDPSOCKET)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  qint64 QHttpSocketEngine::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQHttpSocketEngineCall17 call = reinterpret_cast<CuteQHttpSocketEngineCall17>(taken[17]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::bytesToWrite();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  int QHttpSocketEngine::option(SocketOption option) const
  int option(QAbstractSocketEngine::SocketOption option) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQHttpSocketEngineCall18 call = reinterpret_cast<CuteQHttpSocketEngineCall18>(taken[18]);
      int given = call(this, static_cast<int>(option), &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::option(option);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::setOption(SocketOption option, int value)
  bool setOption(
      QAbstractSocketEngine::SocketOption option,
      int value) override {
    if (taken[19]) {
      int handled = 0;
      CuteQHttpSocketEngineCall19 call = reinterpret_cast<CuteQHttpSocketEngineCall19>(taken[19]);
      bool given = call(this, static_cast<int>(option), value, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::setOption(option, value);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::isReadNotificationEnabled() const
  bool isReadNotificationEnabled() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQHttpSocketEngineCall20 call = reinterpret_cast<CuteQHttpSocketEngineCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::isReadNotificationEnabled();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  void QHttpSocketEngine::setReadNotificationEnabled(bool enable)
  void setReadNotificationEnabled(bool enable) override {
    if (taken[21]) {
      int handled = 0;
      CuteQHttpSocketEngineCall21 call = reinterpret_cast<CuteQHttpSocketEngineCall21>(taken[21]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QHttpSocketEngine::setReadNotificationEnabled(enable);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::isWriteNotificationEnabled() const
  bool isWriteNotificationEnabled() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQHttpSocketEngineCall22 call = reinterpret_cast<CuteQHttpSocketEngineCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::isWriteNotificationEnabled();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  void QHttpSocketEngine::setWriteNotificationEnabled(bool enable)
  void setWriteNotificationEnabled(bool enable) override {
    if (taken[23]) {
      int handled = 0;
      CuteQHttpSocketEngineCall23 call = reinterpret_cast<CuteQHttpSocketEngineCall23>(taken[23]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QHttpSocketEngine::setWriteNotificationEnabled(enable);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  bool QHttpSocketEngine::isExceptionNotificationEnabled() const
  bool isExceptionNotificationEnabled() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQHttpSocketEngineCall24 call = reinterpret_cast<CuteQHttpSocketEngineCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpSocketEngine::isExceptionNotificationEnabled();
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  void QHttpSocketEngine::setExceptionNotificationEnabled(bool enable)
  void setExceptionNotificationEnabled(bool enable) override {
    if (taken[25]) {
      int handled = 0;
      CuteQHttpSocketEngineCall25 call = reinterpret_cast<CuteQHttpSocketEngineCall25>(taken[25]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QHttpSocketEngine::setExceptionNotificationEnabled(enable);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQHttpSocketEngineCall26 call = reinterpret_cast<CuteQHttpSocketEngineCall26>(taken[26]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQHttpSocketEngineCall27 call = reinterpret_cast<CuteQHttpSocketEngineCall27>(taken[27]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQHttpSocketEngineCall28 call = reinterpret_cast<CuteQHttpSocketEngineCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQHttpSocketEngineCall29 call = reinterpret_cast<CuteQHttpSocketEngineCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQHttpSocketEngineCall30 call = reinterpret_cast<CuteQHttpSocketEngineCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQHttpSocketEngineCall31 call = reinterpret_cast<CuteQHttpSocketEngineCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[32]) {
      int handled = 0;
      CuteQHttpSocketEngineCall32 call = reinterpret_cast<CuteQHttpSocketEngineCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHttpSocketEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QHttpSocketEngine10metaObjectEv(
    const QHttpSocketEngine *self) {
  return self->metaObject();
}

//  QHttpSocketEngine::~QHttpSocketEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngineD1Ev(QHttpSocketEngine *self) {
  delete self;
}

//  bool QHttpSocketEngine::initialize(QAbstractSocket::SocketType type,
//      QAbstractSocket::NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpSocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE(
    QHttpSocketEngine *self,
    QAbstractSocket::SocketType type,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  return self->initialize(type, protocol);
}

//  bool QHttpSocketEngine::initialize(qintptr socketDescriptor,
//      QAbstractSocket::SocketState socketState)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpSocketEngine10initializeExN15QAbstractSocket11SocketStateE(
    QHttpSocketEngine *self,
    qintptr socketDescriptor,
    QAbstractSocket::SocketState socketState) {
  return self->initialize(socketDescriptor, socketState);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::setProxy(const QNetworkProxy &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine8setProxyERK13QNetworkProxy(
    QHttpSocketEngine *self,
    const QNetworkProxy *networkProxy) {
  self->setProxy(*networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  qintptr QHttpSocketEngine::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK17QHttpSocketEngine16socketDescriptorEv(
    const QHttpSocketEngine *self) {
  return self->socketDescriptor();
}

//  bool QHttpSocketEngine::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpSocketEngine7isValidEv(const QHttpSocketEngine *self) {
  return self->isValid();
}

//  bool QHttpSocketEngine::connectToHost(const QHostAddress &address,
//      quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpSocketEngine13connectToHostERK12QHostAddresst(
    QHttpSocketEngine *self,
    const QHostAddress *address,
    quint16 port) {
  return self->connectToHost(*address, port);
}

//  bool QHttpSocketEngine::connectToHostByName(const QString &name, quint16
//      port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpSocketEngine19connectToHostByNameERK7QStringt(
    QHttpSocketEngine *self,
    const QString *name,
    quint16 port) {
  return self->connectToHostByName(*name, port);
}

//  void QHttpSocketEngine::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine5closeEv(QHttpSocketEngine *self) {
  self->close();
}

//  qint64 QHttpSocketEngine::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QHttpSocketEngine14bytesAvailableEv(
    const QHttpSocketEngine *self) {
  return self->bytesAvailable();
}

//  qint64 QHttpSocketEngine::write(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN17QHttpSocketEngine5writeEPKcx(
    QHttpSocketEngine *self,
    const char *data,
    qint64 len) {
  return self->write(data, len);
}

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  QNetworkInterface QHttpSocketEngine::multicastInterface() const
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_ZNK17QHttpSocketEngine18multicastInterfaceEv(
    const QHttpSocketEngine *self) {
  return new QNetworkInterface(self->multicastInterface());
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
//  bool QHttpSocketEngine::hasPendingDatagrams() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpSocketEngine19hasPendingDatagramsEv(
    const QHttpSocketEngine *self) {
  return self->hasPendingDatagrams();
}
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
//  qint64 QHttpSocketEngine::pendingDatagramSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QHttpSocketEngine19pendingDatagramSizeEv(
    const QHttpSocketEngine *self) {
  return self->pendingDatagramSize();
}
#endif  // !defined(QT_NO_UDPSOCKET)

//  qint64 QHttpSocketEngine::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QHttpSocketEngine12bytesToWriteEv(
    const QHttpSocketEngine *self) {
  return self->bytesToWrite();
}

//  int QHttpSocketEngine::option(SocketOption option) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHttpSocketEngine6optionEN21QAbstractSocketEngine12SocketOptionE(
    const QHttpSocketEngine *self,
    QAbstractSocketEngine::SocketOption option) {
  return self->option(option);
}

//  bool QHttpSocketEngine::setOption(SocketOption option, int value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpSocketEngine9setOptionEN21QAbstractSocketEngine12SocketOptionEi(
    QHttpSocketEngine *self,
    QAbstractSocketEngine::SocketOption option,
    int value) {
  return self->setOption(option, value);
}

//  bool QHttpSocketEngine::waitForRead(QDeadlineTimer deadline, bool
//      *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpSocketEngine11waitForReadE14QDeadlineTimerPb(
    QHttpSocketEngine *self,
    const QDeadlineTimer *deadline,
    bool *timedOut) {
  return self->waitForRead(*deadline, timedOut);
}

//  bool QHttpSocketEngine::waitForWrite(QDeadlineTimer deadline, bool
//      *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpSocketEngine12waitForWriteE14QDeadlineTimerPb(
    QHttpSocketEngine *self,
    const QDeadlineTimer *deadline,
    bool *timedOut) {
  return self->waitForWrite(*deadline, timedOut);
}

//  bool QHttpSocketEngine::waitForReadOrWrite(bool *readyToRead, bool
//      *readyToWrite, bool checkRead, bool checkWrite, QDeadlineTimer
//      deadline, bool *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpSocketEngine18waitForReadOrWriteEPbS0_bb14QDeadlineTimerS0_(
    QHttpSocketEngine *self,
    bool *readyToRead,
    bool *readyToWrite,
    bool checkRead,
    bool checkWrite,
    const QDeadlineTimer *deadline,
    bool *timedOut) {
  return self->waitForReadOrWrite(
      readyToRead,
      readyToWrite,
      checkRead,
      checkWrite,
      *deadline,
      timedOut);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::waitForProtocolHandshake(QDeadlineTimer deadline)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QHttpSocketEngine24waitForProtocolHandshakeE14QDeadlineTimer(
    const QHttpSocketEngine *self,
    const QDeadlineTimer *deadline) {
  self->waitForProtocolHandshake(*deadline);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  bool QHttpSocketEngine::isReadNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpSocketEngine25isReadNotificationEnabledEv(
    const QHttpSocketEngine *self) {
  return self->isReadNotificationEnabled();
}

//  void QHttpSocketEngine::setReadNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine26setReadNotificationEnabledEb(
    QHttpSocketEngine *self,
    bool enable) {
  self->setReadNotificationEnabled(enable);
}

//  bool QHttpSocketEngine::isWriteNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpSocketEngine26isWriteNotificationEnabledEv(
    const QHttpSocketEngine *self) {
  return self->isWriteNotificationEnabled();
}

//  void QHttpSocketEngine::setWriteNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine27setWriteNotificationEnabledEb(
    QHttpSocketEngine *self,
    bool enable) {
  self->setWriteNotificationEnabled(enable);
}

//  bool QHttpSocketEngine::isExceptionNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpSocketEngine30isExceptionNotificationEnabledEv(
    const QHttpSocketEngine *self) {
  return self->isExceptionNotificationEnabled();
}

//  void QHttpSocketEngine::setExceptionNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine31setExceptionNotificationEnabledEb(
    QHttpSocketEngine *self,
    bool enable) {
  self->setExceptionNotificationEnabled(enable);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::slotSocketConnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine19slotSocketConnectedEv(
    QHttpSocketEngine *self) {
  self->slotSocketConnected();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::slotSocketDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine22slotSocketDisconnectedEv(
    QHttpSocketEngine *self) {
  self->slotSocketDisconnected();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::slotSocketBytesWritten()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine22slotSocketBytesWrittenEv(
    QHttpSocketEngine *self) {
  self->slotSocketBytesWritten();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void
//      QHttpSocketEngine::slotSocketStateChanged(QAbstractSocket::SocketStat
//      e state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine22slotSocketStateChangedEN15QAbstractSocket11SocketStateE(
    QHttpSocketEngine *self,
    QAbstractSocket::SocketState state) {
  self->slotSocketStateChanged(state);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::emitPendingReadNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine27emitPendingReadNotificationEv(
    QHttpSocketEngine *self) {
  self->emitPendingReadNotification();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::emitPendingWriteNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine28emitPendingWriteNotificationEv(
    QHttpSocketEngine *self) {
  self->emitPendingWriteNotification();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::emitPendingConnectionNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine33emitPendingConnectionNotificationEv(
    QHttpSocketEngine *self) {
  self->emitPendingConnectionNotification();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::emitReadNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine20emitReadNotificationEv(
    QHttpSocketEngine *self) {
  self->emitReadNotification();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::emitWriteNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine21emitWriteNotificationEv(
    QHttpSocketEngine *self) {
  self->emitWriteNotification();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::emitConnectionNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpSocketEngine26emitConnectionNotificationEv(
    QHttpSocketEngine *self) {
  self->emitConnectionNotification();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  bool QHttpSocketEngine::readHttpHeader()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpSocketEngine14readHttpHeaderEv(
    QHttpSocketEngine *self) {
  return self->readHttpHeader();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  QHttpSocketEnginePrivate *QHttpSocketEngine::d_func()
extern "C" Q_DECL_EXPORT
QHttpSocketEnginePrivate *ritual_ZN17QHttpSocketEngine6d_funcEv(
    QHttpSocketEngine *self) {
  return self->d_func();
}

//  const QHttpSocketEnginePrivate *QHttpSocketEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QHttpSocketEnginePrivate *ritual_ZNK17QHttpSocketEngine6d_funcEv(
    const QHttpSocketEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQHttpSocketEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpSocketEngine(
    QHttpSocketEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpSocketEngine *>(self)->take(key, call);
}

#if !defined(QT_NO_NETWORKPROXY)
//  bool QHttpSocketEngine::initialize(QAbstractSocket::SocketType type,
//      QAbstractSocket::NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QHttpSocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE(
    QHttpSocketEngine *self,
    QAbstractSocket::SocketType type,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  return self->QHttpSocketEngine::initialize(type, protocol);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  bool QHttpSocketEngine::initialize(qintptr socketDescriptor,
//      QAbstractSocket::SocketState socketState)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QHttpSocketEngine10initializeExN15QAbstractSocket11SocketStateE(
    QHttpSocketEngine *self,
    qintptr socketDescriptor,
    QAbstractSocket::SocketState socketState) {
  return self->QHttpSocketEngine::initialize(socketDescriptor, socketState);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  qintptr QHttpSocketEngine::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK17QHttpSocketEngine16socketDescriptorEv(
    const QHttpSocketEngine *self) {
  return self->QHttpSocketEngine::socketDescriptor();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  bool QHttpSocketEngine::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QHttpSocketEngine7isValidEv(
    const QHttpSocketEngine *self) {
  return self->QHttpSocketEngine::isValid();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QHttpSocketEngine5closeEv(QHttpSocketEngine *self) {
  self->QHttpSocketEngine::close();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  qint64 QHttpSocketEngine::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK17QHttpSocketEngine14bytesAvailableEv(
    const QHttpSocketEngine *self) {
  return self->QHttpSocketEngine::bytesAvailable();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkInterface QHttpSocketEngine::multicastInterface() const
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_own_ZNK17QHttpSocketEngine18multicastInterfaceEv(
    const QHttpSocketEngine *self) {
  return new QNetworkInterface(
      self->QHttpSocketEngine::multicastInterface());
}
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKPROXY)
//  bool QHttpSocketEngine::hasPendingDatagrams() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QHttpSocketEngine19hasPendingDatagramsEv(
    const QHttpSocketEngine *self) {
  return self->QHttpSocketEngine::hasPendingDatagrams();
}
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKPROXY)
//  qint64 QHttpSocketEngine::pendingDatagramSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK17QHttpSocketEngine19pendingDatagramSizeEv(
    const QHttpSocketEngine *self) {
  return self->QHttpSocketEngine::pendingDatagramSize();
}
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_NETWORKPROXY)
//  qint64 QHttpSocketEngine::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK17QHttpSocketEngine12bytesToWriteEv(
    const QHttpSocketEngine *self) {
  return self->QHttpSocketEngine::bytesToWrite();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  int QHttpSocketEngine::option(SocketOption option) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QHttpSocketEngine6optionEN21QAbstractSocketEngine12SocketOptionE(
    const QHttpSocketEngine *self,
    QAbstractSocketEngine::SocketOption option) {
  return self->QHttpSocketEngine::option(option);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  bool QHttpSocketEngine::setOption(SocketOption option, int value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QHttpSocketEngine9setOptionEN21QAbstractSocketEngine12SocketOptionEi(
    QHttpSocketEngine *self,
    QAbstractSocketEngine::SocketOption option,
    int value) {
  return self->QHttpSocketEngine::setOption(option, value);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  bool QHttpSocketEngine::isReadNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QHttpSocketEngine25isReadNotificationEnabledEv(
    const QHttpSocketEngine *self) {
  return self->QHttpSocketEngine::isReadNotificationEnabled();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  bool QHttpSocketEngine::isWriteNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QHttpSocketEngine26isWriteNotificationEnabledEv(
    const QHttpSocketEngine *self) {
  return self->QHttpSocketEngine::isWriteNotificationEnabled();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::setWriteNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QHttpSocketEngine27setWriteNotificationEnabledEb(
    QHttpSocketEngine *self,
    bool enable) {
  self->QHttpSocketEngine::setWriteNotificationEnabled(enable);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  bool QHttpSocketEngine::isExceptionNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QHttpSocketEngine30isExceptionNotificationEnabledEv(
    const QHttpSocketEngine *self) {
  return self->QHttpSocketEngine::isExceptionNotificationEnabled();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpSocketEngine::setExceptionNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QHttpSocketEngine31setExceptionNotificationEnabledEb(
    QHttpSocketEngine *self,
    bool enable) {
  self->QHttpSocketEngine::setExceptionNotificationEnabled(enable);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
