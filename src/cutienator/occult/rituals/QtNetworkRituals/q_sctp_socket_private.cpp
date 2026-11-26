//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsctpsocket_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(sctp)
#if !defined(QT_NO_SCTP)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qsctpsocket.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsctpsocket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsctpsocket.h>
#include <QtNetwork/private/qsctpsocket_p.h>
#include <QtNetwork/private/qabstractsocketengine_p.h>
#ifdef QSCTPSOCKET_DEBUG
#include <QtCore/qdebug.h>
#endif
#include <QtNetwork/private/qabstractsocketengine_p.h>
#include <QtNetwork/private/qnativesocketengine_p.h>
#include <QtCore/qmutex.h>
#include <QtNetwork/qnetworkproxy.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/socket/qsctpsocket.cpp, line 207, as _ZN18QSctpSocketPrivate13writeToSocketEv
inline bool QSctpSocketPrivate::writeToSocket()
{
    Q_Q(QSctpSocket);
#if defined (QSCTPSOCKET_DEBUG)
    qDebug("QSctpSocketPrivate::writeToSocket()");
#endif

    // Handle TCP emulation mode in the base implementation.
    if (!q->isInDatagramMode())
        return QTcpSocketPrivate::writeToSocket();

    if (!socketEngine)
        return false;

    QIpPacketHeader defaultHeader;
    const int savedCurrentChannel = currentWriteChannel;
    bool currentChannelWritten = false;
    bool transmitting;
    do {
        transmitting = false;

        for (int channel = 0; channel < writeBuffers.size(); ++channel) {
            QRingBuffer &channelBuffer = writeBuffers[channel];

            if (channelBuffer.isEmpty())
                continue;

            const bool hasHeader = (channel < writeHeaders.size())
                                   && !writeHeaders[channel].empty();
            QIpPacketHeader &header = hasHeader ? writeHeaders[channel].front() : defaultHeader;
            header.streamNumber = channel;
            qint64 sent = socketEngine->writeDatagram(channelBuffer.readPointer(),
                                                      channelBuffer.nextDataBlockSize(),
                                                      header);
            if (sent < 0) {
                if (sent == -2) // temporary error in writeDatagram
                    return currentChannelWritten;

                socketEngine->close();
#if defined (QSCTPSOCKET_DEBUG)
                qDebug("QSctpSocketPrivate::writeToSocket() write error, aborting. %s",
                       socketEngine->errorString().toLatin1().constData());
#endif
                setErrorAndEmit(socketEngine->error(), socketEngine->errorString());
                // An unexpected error so close the socket.
                q->disconnectFromHost();
                return currentChannelWritten;
            }
            Q_ASSERT(sent == channelBuffer.nextDataBlockSize());
#if defined (QSCTPSOCKET_DEBUG)
            qDebug("QSctpSocketPrivate::writeToSocket() sent datagram of size %lli to channel %i",
                   sent, channel);
#endif
            transmitting = true;

            // Remove datagram from the buffer
            channelBuffer.read();
            if (hasHeader)
                writeHeaders[channel].pop_front();

            // Emit notifications.
            if (channel == savedCurrentChannel)
                currentChannelWritten = true;
            emitBytesWritten(sent, channel);

            // If we were closed as a result of the bytesWritten() signal, return.
            if (state == QAbstractSocket::UnconnectedState) {
#if defined (QSCTPSOCKET_DEBUG)
                qDebug("QSctpSocketPrivate::writeToSocket() socket is closing - returning");
#endif
                return currentChannelWritten;
            }
        }
    } while (transmitting);

    // At this point socket is either in Connected or Closing state,
    // write buffers are empty.
    if (state == QAbstractSocket::ClosingState)
        q->disconnectFromHost();
    else
        socketEngine->setWriteNotificationEnabled(false);

    return currentChannelWritten;
}

//  from src/network/socket/qsctpsocket.cpp, line 109, as _ZN18QSctpSocketPrivate19canReadNotificationEv
inline bool QSctpSocketPrivate::canReadNotification()
{
    Q_Q(QSctpSocket);
#if defined (QSCTPSOCKET_DEBUG)
    qDebug("QSctpSocketPrivate::canReadNotification()");
#endif

    // Handle TCP emulation mode in the base implementation.
    if (!q->isInDatagramMode())
        return QTcpSocketPrivate::canReadNotification();

    const int savedCurrentChannel = currentReadChannel;
    bool currentChannelRead = false;
    do {
        qsizetype datagramSize = incomingDatagram.size();
        QIpPacketHeader header;

        do {
            // Determine the size of the pending datagram.
            qint64 bytesToRead = socketEngine->bytesAvailable();
            if (bytesToRead == 0) {
                // As a corner case, if we can't determine the size of the pending datagram,
                // try to read 4K of data from the socket. Subsequent ::recvmsg call either
                // fails or returns the actual length of the datagram.
                bytesToRead = 4096;
            }

            Q_ASSERT((datagramSize + qsizetype(bytesToRead)) < QByteArray::maxSize());
            incomingDatagram.resize(datagramSize + int(bytesToRead));

#if defined (QSCTPSOCKET_DEBUG)
            qDebug("QSctpSocketPrivate::canReadNotification() about to read %lli bytes",
                   bytesToRead);
#endif
            qint64 readBytes = socketEngine->readDatagram(
                        incomingDatagram.data() + datagramSize, bytesToRead, &header,
                        QAbstractSocketEngine::WantAll);
            if (readBytes <= 0) {
                if (readBytes == -2) { // no data available for reading
                    incomingDatagram.resize(datagramSize);
                    return currentChannelRead;
                }

                socketEngine->close();
                if (readBytes == 0) {
                    setErrorAndEmit(QAbstractSocket::RemoteHostClosedError,
                                    QSctpSocket::tr("The remote host closed the connection"));
                } else {
#if defined (QSCTPSOCKET_DEBUG)
                    qDebug("QSctpSocketPrivate::canReadNotification() read failed: %s",
                           socketEngine->errorString().toLatin1().constData());
#endif
                    setErrorAndEmit(socketEngine->error(), socketEngine->errorString());
                }

#if defined (QSCTPSOCKET_DEBUG)
                qDebug("QSctpSocketPrivate::canReadNotification() disconnecting socket");
#endif
                q->disconnectFromHost();
                return currentChannelRead;
            }
            datagramSize += int(readBytes); // update datagram size
        } while (!header.endOfRecord);

#if defined (QSCTPSOCKET_DEBUG)
        qDebug("QSctpSocketPrivate::canReadNotification() got datagram from channel %i, size = %i",
               header.streamNumber, datagramSize);
#endif

        // Drop the datagram, if opened only for writing
        if (!q->isReadable()) {
            incomingDatagram.clear();
            continue;
        }

        // Store datagram in the channel buffer
        Q_ASSERT(header.streamNumber < readBuffers.size());
        incomingDatagram.resize(datagramSize);
        readBuffers[header.streamNumber].setChunkSize(0); // set packet mode on channel buffer
        readBuffers[header.streamNumber].append(incomingDatagram);
        incomingDatagram = QByteArray();

        if (readHeaders.size() != readBuffers.size())
            readHeaders.resize(readBuffers.size());
        readHeaders[header.streamNumber].push_back(header);

        // Emit notifications.
        if (header.streamNumber == savedCurrentChannel)
            currentChannelRead = true;
        emitReadyRead(header.streamNumber);

    } while (state == QAbstractSocket::ConnectedState);

    return currentChannelRead;
}

//  from src/network/socket/qsctpsocket.cpp, line 294, as _ZN18QSctpSocketPrivate22configureCreatedSocketEv
inline void QSctpSocketPrivate::configureCreatedSocket()
{
    if (socketEngine)
        socketEngine->setOption(QAbstractSocketEngine::MaxStreamsSocketOption,
                                maximumChannelCount < 0 ? 1 : maximumChannelCount);
}

//  from src/network/socket/qsctpsocket.cpp, line 103, as _ZN18QSctpSocketPrivateD2Ev
inline QSctpSocketPrivate::~QSctpSocketPrivate()
{
}

//  from src/network/socket/qabstractsocketengine.cpp, line 103, as _ZNK21QAbstractSocketEngine11errorStringEv
inline QString QAbstractSocketEngine::errorString() const
{
    return d_func()->socketErrorString;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 98, as _ZNK21QAbstractSocketEngine5errorEv
inline QAbstractSocket::SocketError QAbstractSocketEngine::error() const
{
    return d_func()->socketError;
}
//  -----------------------------------------------------------------------

//  A QSctpSocketPrivate that Python can take functions over in. Every QSctpSocketPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_SCTP)
typedef bool (*CuteQSctpSocketPrivateCall0)(const void *, int *);
#endif  // !defined(QT_NO_SCTP)
#if !defined(QT_NO_SCTP)
typedef bool (*CuteQSctpSocketPrivateCall1)(const void *, int *);
#endif  // !defined(QT_NO_SCTP)
#if !defined(QT_NO_SCTP)
typedef void (*CuteQSctpSocketPrivateCall2)(const void *, int *);
#endif  // !defined(QT_NO_SCTP)
typedef void (*CuteQSctpSocketPrivateCall3)(const void *, int *);
typedef void (*CuteQSctpSocketPrivateCall4)(const void *, int *);
typedef void (*CuteQSctpSocketPrivateCall5)(const void *, int *);
typedef void (*CuteQSctpSocketPrivateCall6)(const void *, int *);
typedef void (*CuteQSctpSocketPrivateCall7)(const void *, int *);
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQSctpSocketPrivateCall8)(const void *, const QNetworkProxy *, QAuthenticator *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQSctpSocketPrivateCall9)(const void *, const QHostAddress *, quint16, int, const QNetworkInterface *, int *);
typedef bool (*CuteQSctpSocketPrivateCall10)(const void *, int *);
typedef bool (*CuteQSctpSocketPrivateCall11)(const void *, char, int *);
typedef qint64 (*CuteQSctpSocketPrivateCall12)(const void *, char *, qint64, int *);
typedef const QByteArray * (*CuteQSctpSocketPrivateCall13)(const void *, qint64, int *);
class CuteQSctpSocketPrivate : public QSctpSocketPrivate {
public:
  using QSctpSocketPrivate::QSctpSocketPrivate;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_SCTP)
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate19canReadNotificationEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_SCTP)
#if !defined(QT_NO_SCTP)
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate13writeToSocketEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_SCTP)
#if !defined(QT_NO_SCTP)
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate22configureCreatedSocketEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_SCTP)
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver16readNotificationEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17writeNotificationEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver21exceptionNotificationEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17closeNotificationEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver22connectionNotificationEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate4bindERK12QHostAddresst6QFlagsIN15QAbstractSocket8BindFlagEEPK17QNetworkInterface")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate5flushEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEPcx")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[13] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_SCTP)
  //  bool QSctpSocketPrivate::canReadNotification()
  bool canReadNotification() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall0 call = reinterpret_cast<CuteQSctpSocketPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSctpSocketPrivate::canReadNotification();
  }
#endif  // !defined(QT_NO_SCTP)

#if !defined(QT_NO_SCTP)
  //  bool QSctpSocketPrivate::writeToSocket()
  bool writeToSocket() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall1 call = reinterpret_cast<CuteQSctpSocketPrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSctpSocketPrivate::writeToSocket();
  }
#endif  // !defined(QT_NO_SCTP)

#if !defined(QT_NO_SCTP)
  //  void QSctpSocketPrivate::configureCreatedSocket()
  void configureCreatedSocket() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall2 call = reinterpret_cast<CuteQSctpSocketPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSctpSocketPrivate::configureCreatedSocket();
  }
#endif  // !defined(QT_NO_SCTP)

  //  void QAbstractSocketPrivate::readNotification()
  void readNotification() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall3 call = reinterpret_cast<CuteQSctpSocketPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::readNotification();
  }

  //  void QAbstractSocketPrivate::writeNotification()
  void writeNotification() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall4 call = reinterpret_cast<CuteQSctpSocketPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::writeNotification();
  }

  //  void QAbstractSocketPrivate::exceptionNotification()
  void exceptionNotification() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall5 call = reinterpret_cast<CuteQSctpSocketPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::exceptionNotification();
  }

  //  void QAbstractSocketPrivate::closeNotification()
  void closeNotification() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall6 call = reinterpret_cast<CuteQSctpSocketPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::closeNotification();
  }

  //  void QAbstractSocketPrivate::connectionNotification()
  void connectionNotification() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall7 call = reinterpret_cast<CuteQSctpSocketPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::connectionNotification();
  }

#if !defined(QT_NO_NETWORKPROXY)
  //  void QAbstractSocketPrivate::proxyAuthenticationRequired(const
  //      QNetworkProxy &proxy, QAuthenticator *authenticator)
  void proxyAuthenticationRequired(
      const QNetworkProxy &proxy,
      QAuthenticator *authenticator) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall8 call = reinterpret_cast<CuteQSctpSocketPrivateCall8>(taken[8]);
      call(this, &proxy, authenticator, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::proxyAuthenticationRequired(proxy, authenticator);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)

  //  bool QAbstractSocketPrivate::bind(const QHostAddress &address,
  //      quint16 port, QAbstractSocket::BindMode mode, const
  //      QNetworkInterface *iface)
  bool bind(
      const QHostAddress &address,
      quint16 port,
      QAbstractSocket::BindMode mode,
      const QNetworkInterface *iface) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall9 call = reinterpret_cast<CuteQSctpSocketPrivateCall9>(taken[9]);
      bool given = call(this, &address, port, static_cast<int>(mode.toInt()), iface, &handled);
      if (handled) return given;
    }
    return QAbstractSocketPrivate::bind(address, port, mode, iface);
  }

  //  bool QAbstractSocketPrivate::flush()
  bool flush() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall10 call = reinterpret_cast<CuteQSctpSocketPrivateCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocketPrivate::flush();
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall11 call = reinterpret_cast<CuteQSctpSocketPrivateCall11>(taken[11]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  qint64 QIODevicePrivate::peek(char *data, qint64 maxSize)
  qint64 peek(char *data, qint64 maxSize) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall12 call = reinterpret_cast<CuteQSctpSocketPrivateCall12>(taken[12]);
      qint64 given = call(this, data, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::peek(data, maxSize);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSctpSocketPrivateCall13 call = reinterpret_cast<CuteQSctpSocketPrivateCall13>(taken[13]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QSctpSocket *QSctpSocketPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSctpSocket *ritual_ZN18QSctpSocketPrivate6q_funcEv(
    QSctpSocketPrivate *self) {
  return self->q_func();
}

//  const QSctpSocket *QSctpSocketPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSctpSocket *ritual_ZNK18QSctpSocketPrivate6q_funcEv(
    const QSctpSocketPrivate *self) {
  return self->q_func();
}

//  QSctpSocketPrivate::~QSctpSocketPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSctpSocketPrivateD1Ev(QSctpSocketPrivate *self) {
  delete self;
}

//  bool QSctpSocketPrivate::canReadNotification()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSctpSocketPrivate19canReadNotificationEv(
    QSctpSocketPrivate *self) {
  return self->canReadNotification();
}

//  bool QSctpSocketPrivate::writeToSocket()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSctpSocketPrivate13writeToSocketEv(
    QSctpSocketPrivate *self) {
  return self->writeToSocket();
}

//  void QSctpSocketPrivate::configureCreatedSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSctpSocketPrivate22configureCreatedSocketEv(
    QSctpSocketPrivate *self) {
  self->configureCreatedSocket();
}

//  a Python function taken by a CuteQSctpSocketPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSctpSocketPrivate(
    QSctpSocketPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSctpSocketPrivate *>(self)->take(key, call);
}

//  bool QSctpSocketPrivate::canReadNotification()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QSctpSocketPrivate19canReadNotificationEv(
    QSctpSocketPrivate *self) {
  return self->QSctpSocketPrivate::canReadNotification();
}

//  bool QSctpSocketPrivate::writeToSocket()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QSctpSocketPrivate13writeToSocketEv(
    QSctpSocketPrivate *self) {
  return self->QSctpSocketPrivate::writeToSocket();
}

//  void QSctpSocketPrivate::configureCreatedSocket()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QSctpSocketPrivate22configureCreatedSocketEv(
    QSctpSocketPrivate *self) {
  self->QSctpSocketPrivate::configureCreatedSocket();
}

#endif  // !defined(QT_NO_SCTP)
#endif  // QT_CONFIG(sctp)
