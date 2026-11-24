//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocket_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/qwebsocket.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsocket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtWebSockets/qwebsockethandshakeoptions.h>
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QString>
#include <QtCore/QSet>
#include <QtCore/QtEndian>
#include <QtWebSockets/private/qwebsocketdataprocessor_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtWebSockets/private/qwebsocketframe_p.h>
#include <QtCore/QtEndian>
#include <QtCore/QDebug>
#include <QtCore/QIODevice>
#include <QtCore/QStringDecoder>
#include <limits.h>
#include <QtWebSockets/private/qwebsocketframe_p.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QtEndian>
#include <QtCore/QDebug>
#include <QtCore/QIODevice>
#include <QtWebSockets/qwebsocket.h>
#include <QtWebSockets/private/qwebsocket_p.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtWebSockets/private/qwebsockethandshakerequest_p.h>
#include <QtWebSockets/private/qwebsockethandshakeresponse_p.h>
#include <QtWebSockets/private/qdefaultmaskgenerator_p.h>
#include <QtCore/QUrl>
#include <QtNetwork/QAuthenticator>
#include <QtNetwork/QTcpSocket>
#include <QtCore/QByteArray>
#include <QtCore/QtEndian>
#include <QtCore/QCryptographicHash>
#include <QtCore/QRegularExpression>
#include <QtCore/QStringList>
#include <QtNetwork/QHostAddress>
#include <QtCore/QStringBuilder>   //for more efficient string concatenation
#ifndef QT_NONETWORKPROXY
#include <QtNetwork/QNetworkProxy>
#endif
#ifndef QT_NO_SSL
#include <QtNetwork/QSslConfiguration>
#include <QtNetwork/QSslError>
#include <QtNetwork/QSslPreSharedKeyAuthenticator>
#endif
#include <QtNetwork/private/qhttpheaderparser_p.h>
#include <QtNetwork/private/qauthenticator_p.h>
#include <QtCore/QDebug>
#include <QtCore/QTimer>
#include <limits>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebsockets/src/websockets/qwebsocketprotocol.cpp, line 158, as _ZN18QWebSocketProtocol4maskEP10QByteArrayj
inline void QWebSocketProtocol::mask(QByteArray *payload, quint32 maskingKey)
{
    Q_ASSERT(payload);
    mask(payload->data(), quint64(payload->size()), maskingKey);
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 68, as _ZN23QWebSocketDataProcessor22setMaxAllowedFrameSizeEy
inline void QWebSocketDataProcessor::setMaxAllowedFrameSize(quint64 maxAllowedFrameSize)
{
    frame.setMaxAllowedFrameSize(maxAllowedFrameSize);
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 73, as _ZNK23QWebSocketDataProcessor19maxAllowedFrameSizeEv
inline quint64 QWebSocketDataProcessor::maxAllowedFrameSize() const
{
    return frame.maxAllowedFrameSize();
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 81, as _ZN23QWebSocketDataProcessor24setMaxAllowedMessageSizeEy
inline void QWebSocketDataProcessor::setMaxAllowedMessageSize(quint64 maxAllowedMessageSize)
{
    if (maxAllowedMessageSize <= maxMessageSize())
        m_maxAllowedMessageSize = maxAllowedMessageSize;
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 90, as _ZNK23QWebSocketDataProcessor21maxAllowedMessageSizeEv
inline quint64 QWebSocketDataProcessor::maxAllowedMessageSize() const
{
    return m_maxAllowedMessageSize;
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 98, as _ZN23QWebSocketDataProcessor14maxMessageSizeEv
inline quint64 QWebSocketDataProcessor::maxMessageSize()
{
    return MAX_MESSAGE_SIZE_IN_BYTES;   //COV_NF_LINE
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 106, as _ZN23QWebSocketDataProcessor12maxFrameSizeEv
inline quint64 QWebSocketDataProcessor::maxFrameSize()
{
   return QWebSocketFrame::maxFrameSize();
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 135, as _ZN23QWebSocketDataProcessor7processEP9QIODevice
inline bool QWebSocketDataProcessor::process(QIODevice *pIoDevice)
{
    if (Q_UNLIKELY(m_hasFailed))
        return false;

    bool isDone = false;

    while (!isDone) {
        frame.readFrame(pIoDevice);
        if (!frame.isDone()) {
            // waiting for more data available
            QObject::connect(pIoDevice, &QIODevice::readyRead,
                             m_waitTimer, &QChronoTimer::stop, Qt::UniqueConnection);
            m_waitTimer->start();
            return false;
        } else if (Q_LIKELY(frame.isValid())) {
            if (frame.isControlFrame()) {
                isDone = processControlFrame(frame);
            } else {
                //we have a dataframe; opcode can be OC_CONTINUE, OC_TEXT or OC_BINARY
                if (Q_UNLIKELY(!m_isFragmented && frame.isContinuationFrame())) {
                    reportError(QWebSocketProtocol::CloseCodeProtocolError,
                                tr("Received Continuation frame, while there is " \
                                   "nothing to continue."));
                    return false;
                }
                if (Q_UNLIKELY(m_isFragmented && frame.isDataFrame() &&
                               !frame.isContinuationFrame())) {
                    reportError(QWebSocketProtocol::CloseCodeProtocolError,
                                tr("All data frames after the initial data frame " \
                                   "must have opcode 0 (continuation)."));
                    return false;
                }
                if (!frame.isContinuationFrame()) {
                    m_opCode = frame.opCode();
                    m_isFragmented = !frame.isFinalFrame();
                }
                quint64 messageLength = m_opCode == QWebSocketProtocol::OpCodeText
                        ? quint64(m_textMessage.size())
                        : quint64(m_binaryMessage.size());
                if (Q_UNLIKELY((messageLength + quint64(frame.payload().size())) >
                               maxAllowedMessageSize())) {
                    reportError(QWebSocketProtocol::CloseCodeTooMuchData,
                                tr("Received message is too big."));
                    return false;
                }

                bool isFinalFrame = frame.isFinalFrame();
                if (m_opCode == QWebSocketProtocol::OpCodeText) {
                    QString frameTxt = m_decoder(frame.payload());
                    bool decoderHadError = m_decoder.hasError();
                    if (!decoderHadError && isFinalFrame) {
                        auto r = m_decoder.finalize();
                        decoderHadError = r.error != QStringDecoder::FinalizeResult::Error::NoError;
                    }
                    if (Q_UNLIKELY(decoderHadError)) {
                        reportError(QWebSocketProtocol::CloseCodeWrongDatatype,
                                    tr("Invalid UTF-8 code encountered."));
                        return false;
                    } else {
                        m_textMessage.append(frameTxt);
                        frame.clear();
                        Q_EMIT textFrameReceived(frameTxt, isFinalFrame);
                    }
                } else {
                    m_binaryMessage.append(frame.payload());
                    QByteArray payload = frame.payload();
                    frame.clear();
                    Q_EMIT binaryFrameReceived(payload, isFinalFrame);
                }

                if (isFinalFrame) {
                    isDone = true;
                    if (m_opCode == QWebSocketProtocol::OpCodeText) {
                        const QString textMessage(m_textMessage);
                        clear();
                        Q_EMIT textMessageReceived(textMessage);
                    } else {
                        const QByteArray binaryMessage(m_binaryMessage);
                        clear();
                        Q_EMIT binaryMessageReceived(binaryMessage);
                    }
                }
            }
        } else {
            reportError(frame.closeCode(), frame.closeReason());
            return false;
        }
        frame.clear();
    }
    return true;
}

//  from ../qtwebsockets/src/websockets/qwebsocketprotocol.cpp, line 170, as _ZN18QWebSocketProtocol4maskEPcyj
inline void QWebSocketProtocol::mask(char *payload, quint64 size, quint32 maskingKey)
{
    Q_ASSERT(payload);
    const quint8 mask[] = { quint8((maskingKey & 0xFF000000u) >> 24),
                            quint8((maskingKey & 0x00FF0000u) >> 16),
                            quint8((maskingKey & 0x0000FF00u) >> 8),
                            quint8((maskingKey & 0x000000FFu))
                          };
    quint64 i = 0;
    while (size-- > 0)
        *payload++ ^= mask[i++ % 4];
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 33, as _ZN15QWebSocketFrame22setMaxAllowedFrameSizeEy
inline void QWebSocketFrame::setMaxAllowedFrameSize(quint64 maxAllowedFrameSize)
{
    if (maxAllowedFrameSize <= maxFrameSize())
        m_maxAllowedFrameSize = maxAllowedFrameSize;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 42, as _ZNK15QWebSocketFrame19maxAllowedFrameSizeEv
inline quint64 QWebSocketFrame::maxAllowedFrameSize() const
{
    return m_maxAllowedFrameSize;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 50, as _ZN15QWebSocketFrame12maxFrameSizeEv
inline quint64 QWebSocketFrame::maxFrameSize()
{
    return MAX_FRAME_SIZE_IN_BYTES;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 140, as _ZN15QWebSocketFrame5clearEv
inline void QWebSocketFrame::clear()
{
    m_closeCode = QWebSocketProtocol::CloseCodeNormal;
    m_closeReason.clear();
    m_isFinalFrame = true;
    m_mask = 0;
    m_rsv1 = false;
    m_rsv2 = false;
    m_rsv3 = false;
    m_opCode = QWebSocketProtocol::OpCodeReservedC;
    m_length = 0;
    m_payload.clear();
    m_isValid = false;
    m_processingState = PS_READ_HEADER;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 175, as _ZN15QWebSocketFrame9readFrameEP9QIODevice
inline void QWebSocketFrame::readFrame(QIODevice *pIoDevice)
{
    while (true)
    {
        switch (m_processingState) {
        case PS_READ_HEADER:
            m_processingState = readFrameHeader(pIoDevice);
            if (m_processingState == PS_WAIT_FOR_MORE_DATA) {
                m_processingState = PS_READ_HEADER;
                return;
            }
            break;

        case PS_READ_PAYLOAD_LENGTH:
            m_processingState = readFramePayloadLength(pIoDevice);
            if (m_processingState == PS_WAIT_FOR_MORE_DATA) {
                m_processingState = PS_READ_PAYLOAD_LENGTH;
                return;
            }
            break;

        case PS_READ_MASK:
            m_processingState = readFrameMask(pIoDevice);
            if (m_processingState == PS_WAIT_FOR_MORE_DATA) {
                m_processingState = PS_READ_MASK;
                return;
            }
            break;

        case PS_READ_PAYLOAD:
            m_processingState = readFramePayload(pIoDevice);
            if (m_processingState == PS_WAIT_FOR_MORE_DATA) {
                m_processingState = PS_READ_PAYLOAD;
                return;
            }
            break;

        case PS_DISPATCH_RESULT:
            return;

        default:
            Q_UNREACHABLE_RETURN();
        }
    }
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 179, as _ZN17QWebSocketPrivateD1Ev
#if defined(Q_OS_LINUX)
inline QWebSocketPrivate::~QWebSocketPrivate()
{
#ifdef Q_OS_WASM
    if (m_socketContext) {
        uint16_t m_readyState;
        emscripten_websocket_get_ready_state(m_socketContext, &m_readyState);
        if (m_readyState == 1 || m_readyState == 0) {
            emscripten_websocket_close(m_socketContext, 1000,"");
        }
        emscripten_websocket_delete(m_socketContext);
    }
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 208, as _ZN17QWebSocketPrivate5abortEv
inline void QWebSocketPrivate::abort()
{
    if (m_pSocket)
        m_pSocket->abort();
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 217, as _ZNK17QWebSocketPrivate5errorEv
inline QAbstractSocket::SocketError QWebSocketPrivate::error() const
{
    QAbstractSocket::SocketError err = QAbstractSocket::UnknownSocketError;
    if (Q_LIKELY(m_pSocket))
        err = m_pSocket->error();
    return err;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 228, as _ZNK17QWebSocketPrivate11errorStringEv
inline QString QWebSocketPrivate::errorString() const
{
    QString errMsg;
    if (!m_errorString.isEmpty())
        errMsg = m_errorString;
    else if (m_pSocket)
        errMsg = m_pSocket->errorString();
    return errMsg;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 241, as _ZN17QWebSocketPrivate5flushEv
inline bool QWebSocketPrivate::flush()
{
    bool result = true;
    if (Q_LIKELY(m_pSocket))
        result = m_pSocket->flush();
    return result;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1627, as _ZNK17QWebSocketPrivate12localAddressEv
inline QHostAddress QWebSocketPrivate::localAddress() const
{
    QHostAddress address;
    if (Q_LIKELY(m_pSocket))
        address = m_pSocket->localAddress();
    return address;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1638, as _ZNK17QWebSocketPrivate9localPortEv
inline quint16 QWebSocketPrivate::localPort() const
{
    quint16 port = 0;
    if (Q_LIKELY(m_pSocket))
        port = m_pSocket->localPort();
    return port;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1649, as _ZNK17QWebSocketPrivate9pauseModeEv
inline QAbstractSocket::PauseModes QWebSocketPrivate::pauseMode() const
{
    return m_pauseMode;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1657, as _ZNK17QWebSocketPrivate11peerAddressEv
inline QHostAddress QWebSocketPrivate::peerAddress() const
{
    QHostAddress address;
    if (Q_LIKELY(m_pSocket))
        address = m_pSocket->peerAddress();
    return address;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1668, as _ZNK17QWebSocketPrivate8peerNameEv
inline QString QWebSocketPrivate::peerName() const
{
    QString name;
    if (Q_LIKELY(m_pSocket))
        name = m_pSocket->peerName();
    return name;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1679, as _ZNK17QWebSocketPrivate8peerPortEv
inline quint16 QWebSocketPrivate::peerPort() const
{
    quint16 port = 0;
    if (Q_LIKELY(m_pSocket))
        port = m_pSocket->peerPort();
    return port;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1691, as _ZNK17QWebSocketPrivate5proxyEv
#if !defined(QT_NO_NETWORKPROXY)
inline QNetworkProxy QWebSocketPrivate::proxy() const
{
    return m_configuration.m_proxy;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1699, as _ZN17QWebSocketPrivate8setProxyERK13QNetworkProxy
#if !defined(QT_NO_NETWORKPROXY)
inline void QWebSocketPrivate::setProxy(const QNetworkProxy &networkProxy)
{
    if (m_configuration.m_proxy != networkProxy)
        m_configuration.m_proxy = networkProxy;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1709, as _ZN17QWebSocketPrivate16setMaskGeneratorEPK14QMaskGenerator
inline void QWebSocketPrivate::setMaskGenerator(const QMaskGenerator *maskGenerator)
{
    if (!maskGenerator)
        m_pMaskGenerator = &m_defaultMaskGenerator;
    else if (maskGenerator != m_pMaskGenerator)
        m_pMaskGenerator = const_cast<QMaskGenerator *>(maskGenerator);
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1720, as _ZNK17QWebSocketPrivate13maskGeneratorEv
inline const QMaskGenerator *QWebSocketPrivate::maskGenerator() const
{
    Q_ASSERT(m_pMaskGenerator);
    return m_pMaskGenerator;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1729, as _ZNK17QWebSocketPrivate14readBufferSizeEv
inline qint64 QWebSocketPrivate::readBufferSize() const
{
    return m_readBufferSize;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1737, as _ZN17QWebSocketPrivate6resumeEv
inline void QWebSocketPrivate::resume()
{
    if (Q_LIKELY(m_pSocket))
        m_pSocket->resume();
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1746, as _ZN17QWebSocketPrivate12setPauseModeE6QFlagsIN15QAbstractSocket9PauseModeEE
inline void QWebSocketPrivate::setPauseMode(QAbstractSocket::PauseModes pauseMode)
{
    m_pauseMode = pauseMode;
    if (Q_LIKELY(m_pSocket))
        m_pSocket->setPauseMode(m_pauseMode);
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1756, as _ZN17QWebSocketPrivate17setReadBufferSizeEx
inline void QWebSocketPrivate::setReadBufferSize(qint64 size)
{
    m_readBufferSize = size;
    if (Q_LIKELY(m_pSocket))
        m_pSocket->setReadBufferSize(m_readBufferSize);
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1524, as _ZNK17QWebSocketPrivate5stateEv
inline QAbstractSocket::SocketState QWebSocketPrivate::state() const
{
    return m_socketState;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 710, as _ZNK17QWebSocketPrivate7versionEv
inline QWebSocketProtocol::Version QWebSocketPrivate::version() const
{
    return m_version;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 718, as _ZNK17QWebSocketPrivate12resourceNameEv
inline QString QWebSocketPrivate::resourceName() const
{
    return m_resourceName;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 726, as _ZNK17QWebSocketPrivate7requestEv
inline QNetworkRequest QWebSocketPrivate::request() const
{
    return m_request;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 734, as _ZNK17QWebSocketPrivate6originEv
inline QString QWebSocketPrivate::origin() const
{
    return m_origin;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 742, as _ZNK17QWebSocketPrivate16handshakeOptionsEv
inline QWebSocketHandshakeOptions QWebSocketPrivate::handshakeOptions() const
{
    return m_options;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 750, as _ZNK17QWebSocketPrivate8protocolEv
inline QString QWebSocketPrivate::protocol() const
{
    return m_protocol;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 758, as _ZNK17QWebSocketPrivate9extensionEv
inline QString QWebSocketPrivate::extension() const
{
    return m_extension;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 766, as _ZNK17QWebSocketPrivate9closeCodeEv
inline QWebSocketProtocol::CloseCode QWebSocketPrivate::closeCode() const
{
    return m_closeCode;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 774, as _ZNK17QWebSocketPrivate11closeReasonEv
inline QString QWebSocketPrivate::closeReason() const
{
    return m_closeReason;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 289, as _ZN17QWebSocketPrivate15ignoreSslErrorsERK5QListI9QSslErrorE
#if !defined(QT_NO_SSL)
inline void QWebSocketPrivate::ignoreSslErrors(const QList<QSslError> &errors)
{
    m_configuration.m_ignoredSslErrors = errors;
    if (Q_LIKELY(m_pSocket)) {
        QSslSocket *pSslSocket = qobject_cast<QSslSocket *>(m_pSocket);
        if (Q_LIKELY(pSslSocket))
            pSslSocket->ignoreSslErrors(errors);
    }
}
#endif  // !defined(QT_NO_SSL)

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 302, as _ZN17QWebSocketPrivate15ignoreSslErrorsEv
#if !defined(QT_NO_SSL)
inline void QWebSocketPrivate::ignoreSslErrors()
{
    m_configuration.m_ignoreSslErrors = true;
    if (Q_LIKELY(m_pSocket)) {
        QSslSocket *pSslSocket = qobject_cast<QSslSocket *>(m_pSocket);
        if (Q_LIKELY(pSslSocket))
            pSslSocket->ignoreSslErrors();
    }
}
#endif  // !defined(QT_NO_SSL)

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 315, as _ZN17QWebSocketPrivate28continueInterruptedHandshakeEv
#if !defined(QT_NO_SSL)
inline void QWebSocketPrivate::continueInterruptedHandshake()
{
    if (Q_LIKELY(m_pSocket)) {
        QSslSocket *pSslSocket = qobject_cast<QSslSocket *>(m_pSocket);
        if (Q_LIKELY(pSslSocket))
            pSslSocket->continueInterruptedHandshake();
    }
}
#endif  // !defined(QT_NO_SSL)

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 273, as _ZN17QWebSocketPrivate19setSslConfigurationERK17QSslConfiguration
#if !defined(QT_NO_SSL)
inline void QWebSocketPrivate::setSslConfiguration(const QSslConfiguration &sslConfiguration)
{
    m_configuration.m_sslConfiguration = sslConfiguration;
}
#endif  // !defined(QT_NO_SSL)

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 281, as _ZNK17QWebSocketPrivate16sslConfigurationEv
#if !defined(QT_NO_SSL)
inline QSslConfiguration QWebSocketPrivate::sslConfiguration() const
{
    return m_configuration.m_sslConfiguration;
}
#endif  // !defined(QT_NO_SSL)

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 327, as _ZN17QWebSocketPrivate25_q_updateSslConfigurationEv
#if !defined(QT_NO_SSL)
inline void QWebSocketPrivate::_q_updateSslConfiguration()
{
    if (QSslSocket *sslSock = qobject_cast<QSslSocket *>(m_pSocket))
        m_configuration.m_sslConfiguration = sslSock->sslConfiguration();
}
#endif  // !defined(QT_NO_SSL)

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 523, as _ZN17QWebSocketPrivate4pingERK10QByteArray
inline void QWebSocketPrivate::ping(const QByteArray &payload)
{
    QByteArray payloadTruncated = payload.left(125);
    m_pingTimer.start();
    quint32 maskingKey = 0;
    if (m_mustMask)
        maskingKey = generateMaskingKey();
    QByteArray pingFrame = getFrameHeader(QWebSocketProtocol::OpCodePing,
                                          quint64(payloadTruncated.size()),
                                          maskingKey, true);
    if (m_mustMask)
        QWebSocketProtocol::mask(&payloadTruncated, maskingKey);
    pingFrame.append(payloadTruncated);
    qint64 ret = writeFrame(pingFrame);
    Q_UNUSED(ret);
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1532, as _ZN17QWebSocketPrivate14setSocketStateEN15QAbstractSocket11SocketStateE
inline void QWebSocketPrivate::setSocketState(QAbstractSocket::SocketState state)
{
    Q_Q(QWebSocket);
    if (m_socketState != state) {
        m_socketState = state;
        Q_EMIT q->stateChanged(m_socketState);
    }
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1544, as _ZN17QWebSocketPrivate30setMaxAllowedIncomingFrameSizeEy
inline void QWebSocketPrivate::setMaxAllowedIncomingFrameSize(quint64 maxAllowedIncomingFrameSize)
{
    m_dataProcessor->setMaxAllowedFrameSize(maxAllowedIncomingFrameSize);
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1552, as _ZNK17QWebSocketPrivate27maxAllowedIncomingFrameSizeEv
inline quint64 QWebSocketPrivate::maxAllowedIncomingFrameSize() const
{
    return m_dataProcessor->maxAllowedFrameSize();
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1560, as _ZN17QWebSocketPrivate32setMaxAllowedIncomingMessageSizeEy
inline void QWebSocketPrivate::setMaxAllowedIncomingMessageSize(quint64 maxAllowedIncomingMessageSize)
{
    m_dataProcessor->setMaxAllowedMessageSize(maxAllowedIncomingMessageSize);
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1568, as _ZNK17QWebSocketPrivate29maxAllowedIncomingMessageSizeEv
inline quint64 QWebSocketPrivate::maxAllowedIncomingMessageSize() const
{
    return m_dataProcessor->maxAllowedMessageSize();
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1576, as _ZN17QWebSocketPrivate22maxIncomingMessageSizeEv
inline quint64 QWebSocketPrivate::maxIncomingMessageSize()
{
    return QWebSocketDataProcessor::maxMessageSize();
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1584, as _ZN17QWebSocketPrivate20maxIncomingFrameSizeEv
inline quint64 QWebSocketPrivate::maxIncomingFrameSize()
{
    return QWebSocketDataProcessor::maxFrameSize();
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1601, as _ZNK17QWebSocketPrivate17outgoingFrameSizeEv
inline quint64 QWebSocketPrivate::outgoingFrameSize() const
{
    return m_outgoingFrameSize;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 545, as _ZN17QWebSocketPrivate10setVersionEN18QWebSocketProtocol7VersionE
inline void QWebSocketPrivate::setVersion(QWebSocketProtocol::Version version)
{
    if (m_version != version)
        m_version = version;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 555, as _ZN17QWebSocketPrivate15setResourceNameERK7QString
inline void QWebSocketPrivate::setResourceName(const QString &resourceName)
{
    if (m_resourceName != resourceName)
        m_resourceName = resourceName;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 564, as _ZN17QWebSocketPrivate10setRequestERK15QNetworkRequestRK26QWebSocketHandshakeOptions
inline void QWebSocketPrivate::setRequest(const QNetworkRequest &request,
                                   const QWebSocketHandshakeOptions &options)
{
    if (m_request != request)
        m_request = request;
    if (m_options != options)
        m_options = options;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 576, as _ZN17QWebSocketPrivate9setOriginERK7QString
inline void QWebSocketPrivate::setOrigin(const QString &origin)
{
    if (m_origin != origin)
        m_origin = origin;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 585, as _ZN17QWebSocketPrivate11setProtocolERK7QString
inline void QWebSocketPrivate::setProtocol(const QString &protocol)
{
    if (m_protocol != protocol)
        m_protocol = protocol;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 594, as _ZN17QWebSocketPrivate12setExtensionERK7QString
inline void QWebSocketPrivate::setExtension(const QString &extension)
{
    if (m_extension != extension)
        m_extension = extension;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 603, as _ZN17QWebSocketPrivate13enableMaskingEb
inline void QWebSocketPrivate::enableMasking(bool enable)
{
    if (m_mustMask != enable)
        m_mustMask = enable;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1618, as _ZN17QWebSocketPrivate14setErrorStringERK7QString
inline void QWebSocketPrivate::setErrorString(const QString &errorString)
{
    if (m_errorString != errorString)
        m_errorString = errorString;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 335, as _ZNK17QWebSocketPrivate21requestedSubProtocolsEv
inline QStringList QWebSocketPrivate::requestedSubProtocols() const
{
    auto subprotocolsRequestedInRawHeader = [this]() {
        QStringList protocols;
        QByteArrayView rawProtocols = m_request.headers().value("Sec-WebSocket-Protocol");
        QLatin1StringView rawProtocolsView(rawProtocols);
        const QStringList &optionsProtocols = m_options.subprotocols();
        for (auto &&entry : rawProtocolsView.tokenize(u',', Qt::SkipEmptyParts)) {
            if (QLatin1StringView trimmed = entry.trimmed(); !trimmed.isEmpty()) {
                if (!optionsProtocols.contains(trimmed))
                    protocols << trimmed;
            }
        }
        return protocols;
    };
    return m_options.subprotocols() + subprotocolsRequestedInRawHeader();
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1369, as _ZN17QWebSocketPrivate15socketDestroyedEP7QObject
inline void QWebSocketPrivate::socketDestroyed(QObject *socket)
{
    Q_ASSERT(m_pSocket);
    if (m_pSocket == socket)
        m_pSocket = nullptr;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1402, as _ZN17QWebSocketPrivate11processPingERK10QByteArray
inline void QWebSocketPrivate::processPing(const QByteArray &data)
{
    Q_ASSERT(m_pSocket);
    quint32 maskingKey = 0;
    if (m_mustMask)
        maskingKey = generateMaskingKey();
    m_pSocket->write(getFrameHeader(QWebSocketProtocol::OpCodePong,
                                    unsigned(data.size()),
                                    maskingKey,
                                    true));
    if (data.size() > 0) {
        QByteArray maskedData = data;
        if (m_mustMask)
            QWebSocketProtocol::mask(&maskedData, maskingKey);
        m_pSocket->write(maskedData);
    }
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1423, as _ZN17QWebSocketPrivate11processPongERK10QByteArray
inline void QWebSocketPrivate::processPong(const QByteArray &data)
{
    Q_Q(QWebSocket);
    Q_EMIT q->pong(static_cast<quint64>(m_pingTimer.elapsed()), data);
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 828, as _ZN17QWebSocketPrivate13doWriteFramesERK10QByteArrayb
inline qint64 QWebSocketPrivate::doWriteFrames(const QByteArray &data, bool isBinary)
{
    qint64 payloadWritten = 0;
    if (Q_UNLIKELY(!m_pSocket) || (state() != QAbstractSocket::ConnectedState))
        return payloadWritten;

    const QWebSocketProtocol::OpCode firstOpCode = isBinary ?
                QWebSocketProtocol::OpCodeBinary : QWebSocketProtocol::OpCodeText;

    int numFrames = data.size() / int(outgoingFrameSize());
    QByteArray tmpData(data);
    tmpData.detach();
    char *payload = tmpData.data();
    quint64 sizeLeft = quint64(data.size()) % outgoingFrameSize();
    if (Q_LIKELY(sizeLeft))
        ++numFrames;

    //catch the case where the payload is zero bytes;
    //in this case, we still need to send a frame
    if (Q_UNLIKELY(numFrames == 0))
        numFrames = 1;
    quint64 currentPosition = 0;
    quint64 bytesLeft = quint64(data.size());

    for (int i = 0; i < numFrames; ++i) {
        quint32 maskingKey = 0;
        if (m_mustMask)
            maskingKey = generateMaskingKey();

        const bool isLastFrame = (i == (numFrames - 1));
        const bool isFirstFrame = (i == 0);

        const quint64 size = qMin(bytesLeft, outgoingFrameSize());
        const QWebSocketProtocol::OpCode opcode = isFirstFrame ? firstOpCode
                                                               : QWebSocketProtocol::OpCodeContinue;

        //write header
        m_pSocket->write(getFrameHeader(opcode, size, maskingKey, isLastFrame));

        //write payload
        if (Q_LIKELY(size > 0)) {
            char *currentData = payload + currentPosition;
            if (m_mustMask)
                QWebSocketProtocol::mask(currentData, size, maskingKey);
            qint64 written = m_pSocket->write(currentData, static_cast<qint64>(size));
            if (Q_LIKELY(written > 0)) {
                payloadWritten += written;
            } else {
                m_pSocket->flush();
                setErrorString(QWebSocket::tr("Error writing bytes to socket: %1.")
                               .arg(m_pSocket->errorString()));
                emitErrorOccurred(QAbstractSocket::NetworkError);
                break;
            }
        }
        currentPosition += size;
        bytesLeft -= size;
    }
    if (Q_UNLIKELY(payloadWritten != data.size())) {
        setErrorString(QWebSocket::tr("Bytes written %1 != %2.")
                       .arg(payloadWritten).arg(data.size()));
        emitErrorOccurred(QAbstractSocket::NetworkError);
    }
    return payloadWritten;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 693, as _ZN17QWebSocketPrivate18releaseConnectionsEPK10QTcpSocket
inline void QWebSocketPrivate::releaseConnections(const QTcpSocket *pTcpSocket)
{
    if (Q_LIKELY(pTcpSocket)) {
        // Explicitly disconnect this signal to avoid warning being printed about a destroyed-signal
        // being disconnected with the wildcard disconnect below
        disconnect(pTcpSocket, &QObject::destroyed, this, &QWebSocketPrivate::socketDestroyed);
        pTcpSocket->disconnect();
        // Re-connect, we need 'socketDestroyed' slot executed
        QObjectPrivate::connect(pTcpSocket, &QObject::destroyed,
                                this, &QWebSocketPrivate::socketDestroyed);
    }
    m_dataProcessor->disconnect();
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 782, as _ZN17QWebSocketPrivate14getFrameHeaderEN18QWebSocketProtocol6OpCodeEyjb
inline QByteArray QWebSocketPrivate::getFrameHeader(QWebSocketProtocol::OpCode opCode,
                                             quint64 payloadLength, quint32 maskingKey,
                                             bool lastFrame)
{
    QByteArray header;
    bool ok = payloadLength <= 0x7FFFFFFFFFFFFFFFULL;

    if (Q_LIKELY(ok)) {
        //FIN, RSV1-3, opcode (RSV-1, RSV-2 and RSV-3 are zero)
        quint8 byte = static_cast<quint8>((opCode & 0x0F) | (lastFrame ? 0x80 : 0x00));
        header.append(static_cast<char>(byte));

        byte = 0x00;
        if (maskingKey != 0)
            byte |= 0x80;
        if (payloadLength <= 125) {
            byte |= static_cast<quint8>(payloadLength);
            header.append(static_cast<char>(byte));
        } else if (payloadLength <= 0xFFFFU) {
            byte |= 126;
            header.append(static_cast<char>(byte));
            quint16 swapped = qToBigEndian<quint16>(static_cast<quint16>(payloadLength));
            header.append(static_cast<const char *>(static_cast<const void *>(&swapped)), 2);
        } else if (payloadLength <= 0x7FFFFFFFFFFFFFFFULL) {
            byte |= 127;
            header.append(static_cast<char>(byte));
            quint64 swapped = qToBigEndian<quint64>(payloadLength);
            header.append(static_cast<const char *>(static_cast<const void *>(&swapped)), 8);
        }

        if (maskingKey != 0) {
            const quint32 mask = qToBigEndian<quint32>(maskingKey);
            header.append(static_cast<const char *>(static_cast<const void *>(&mask)),
                          sizeof(quint32));
        }
    } else {
        setErrorString(QStringLiteral("WebSocket::getHeader: payload too big!"));
        emitErrorOccurred(QAbstractSocket::DatagramTooLargeError);
    }

    return header;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 921, as _ZNK17QWebSocketPrivate18calculateAcceptKeyERK10QByteArray
inline QString QWebSocketPrivate::calculateAcceptKey(const QByteArray &key) const
{
    const QByteArray tmpKey = key + QByteArrayLiteral("258EAFA5-E914-47DA-95CA-C5AB0DC85B11");
    const QByteArray hash = QCryptographicHash::hash(tmpKey, QCryptographicHash::Sha1).toBase64();
    return QString::fromLatin1(hash);
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 897, as _ZNK17QWebSocketPrivate18generateMaskingKeyEv
inline quint32 QWebSocketPrivate::generateMaskingKey() const
{
    return m_pMaskGenerator->nextMask();
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 905, as _ZNK17QWebSocketPrivate11generateKeyEv
inline QByteArray QWebSocketPrivate::generateKey() const
{
    QByteArray key;

    for (int i = 0; i < 4; ++i) {
        const quint32 tmp = m_pMaskGenerator->nextMask();
        key.append(static_cast<const char *>(static_cast<const void *>(&tmp)), sizeof(quint32));
    }

    return key.toBase64();
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 931, as _ZN17QWebSocketPrivate11writeFramesERK5QListI10QByteArrayE
inline qint64 QWebSocketPrivate::writeFrames(const QList<QByteArray> &frames)
{
    qint64 written = 0;
    if (Q_LIKELY(m_pSocket)) {
        QList<QByteArray>::const_iterator it;
        for (it = frames.cbegin(); it < frames.cend(); ++it)
            written += writeFrame(*it);
    }
    return written;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 945, as _ZN17QWebSocketPrivate10writeFrameERK10QByteArray
inline qint64 QWebSocketPrivate::writeFrame(const QByteArray &frame)
{
    qint64 written = 0;
    if (Q_LIKELY(m_pSocket))
        written = m_pSocket->write(frame);
    return written;
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 1763, as _ZN17QWebSocketPrivate17emitErrorOccurredEN15QAbstractSocket11SocketErrorE
inline void QWebSocketPrivate::emitErrorOccurred(QAbstractSocket::SocketError error)
{
    Q_Q(QWebSocket);
    Q_EMIT q->errorOccurred(error);
#if QT_DEPRECATED_SINCE(6, 5)
    QT_WARNING_PUSH
    QT_WARNING_DISABLE_DEPRECATED
    Q_EMIT q->error(error);
    QT_WARNING_POP
#endif
}
//  -----------------------------------------------------------------------

//  QWebSocket *QWebSocketPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWebSocket *ritual_ZN17QWebSocketPrivate6q_funcEv(QWebSocketPrivate *self) {
  return self->q_func();
}

//  const QWebSocket *QWebSocketPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWebSocket *ritual_ZNK17QWebSocketPrivate6q_funcEv(
    const QWebSocketPrivate *self) {
  return self->q_func();
}

//  QWebSocketPrivate::~QWebSocketPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivateD1Ev(QWebSocketPrivate *self) {
  delete self;
}

//  void QWebSocketPrivate::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate5abortEv(QWebSocketPrivate *self) {
  self->abort();
}

//  QAbstractSocket::SocketError QWebSocketPrivate::error() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_ZNK17QWebSocketPrivate5errorEv(
    const QWebSocketPrivate *self) {
  return self->error();
}

//  QString QWebSocketPrivate::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebSocketPrivate11errorStringEv(
    const QWebSocketPrivate *self) {
  return new QString(self->errorString());
}

//  bool QWebSocketPrivate::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QWebSocketPrivate5flushEv(QWebSocketPrivate *self) {
  return self->flush();
}

//  QHostAddress QWebSocketPrivate::localAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK17QWebSocketPrivate12localAddressEv(
    const QWebSocketPrivate *self) {
  return new QHostAddress(self->localAddress());
}

//  quint16 QWebSocketPrivate::localPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK17QWebSocketPrivate9localPortEv(
    const QWebSocketPrivate *self) {
  return self->localPort();
}

//  QAbstractSocket::PauseModes QWebSocketPrivate::pauseMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QWebSocketPrivate9pauseModeEv(
    const QWebSocketPrivate *self) {
  return static_cast<int>(self->pauseMode().toInt());
}

//  QHostAddress QWebSocketPrivate::peerAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK17QWebSocketPrivate11peerAddressEv(
    const QWebSocketPrivate *self) {
  return new QHostAddress(self->peerAddress());
}

//  QString QWebSocketPrivate::peerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebSocketPrivate8peerNameEv(
    const QWebSocketPrivate *self) {
  return new QString(self->peerName());
}

//  quint16 QWebSocketPrivate::peerPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK17QWebSocketPrivate8peerPortEv(
    const QWebSocketPrivate *self) {
  return self->peerPort();
}

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxy QWebSocketPrivate::proxy() const
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZNK17QWebSocketPrivate5proxyEv(
    const QWebSocketPrivate *self) {
  return new QNetworkProxy(self->proxy());
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QWebSocketPrivate::setProxy(const QNetworkProxy &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate8setProxyERK13QNetworkProxy(
    QWebSocketPrivate *self,
    const QNetworkProxy *networkProxy) {
  self->setProxy(*networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QWebSocketPrivate::setMaskGenerator(const QMaskGenerator
//      *maskGenerator)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate16setMaskGeneratorEPK14QMaskGenerator(
    QWebSocketPrivate *self,
    const QMaskGenerator *maskGenerator) {
  self->setMaskGenerator(maskGenerator);
}

//  const QMaskGenerator *QWebSocketPrivate::maskGenerator() const
extern "C" Q_DECL_EXPORT
const QMaskGenerator *ritual_ZNK17QWebSocketPrivate13maskGeneratorEv(
    const QWebSocketPrivate *self) {
  return self->maskGenerator();
}

//  qint64 QWebSocketPrivate::readBufferSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QWebSocketPrivate14readBufferSizeEv(
    const QWebSocketPrivate *self) {
  return self->readBufferSize();
}

//  void QWebSocketPrivate::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate6resumeEv(QWebSocketPrivate *self) {
  self->resume();
}

//  void QWebSocketPrivate::setPauseMode(QAbstractSocket::PauseModes
//      pauseMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate12setPauseModeE6QFlagsIN15QAbstractSocket9PauseModeEE(
    QWebSocketPrivate *self,
    int pauseMode) {
  self->setPauseMode(QFlags<QAbstractSocket::PauseMode>::fromInt(pauseMode));
}

//  void QWebSocketPrivate::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate17setReadBufferSizeEx(
    QWebSocketPrivate *self,
    qint64 size) {
  self->setReadBufferSize(size);
}

//  QAbstractSocket::SocketState QWebSocketPrivate::state() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketState ritual_ZNK17QWebSocketPrivate5stateEv(
    const QWebSocketPrivate *self) {
  return self->state();
}

//  QWebSocketProtocol::Version QWebSocketPrivate::version() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::Version ritual_ZNK17QWebSocketPrivate7versionEv(
    const QWebSocketPrivate *self) {
  return self->version();
}

//  QString QWebSocketPrivate::resourceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebSocketPrivate12resourceNameEv(
    const QWebSocketPrivate *self) {
  return new QString(self->resourceName());
}

//  QNetworkRequest QWebSocketPrivate::request() const
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZNK17QWebSocketPrivate7requestEv(
    const QWebSocketPrivate *self) {
  return new QNetworkRequest(self->request());
}

//  QString QWebSocketPrivate::origin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebSocketPrivate6originEv(
    const QWebSocketPrivate *self) {
  return new QString(self->origin());
}

//  QWebSocketHandshakeOptions QWebSocketPrivate::handshakeOptions() const
extern "C" Q_DECL_EXPORT
QWebSocketHandshakeOptions *ritual_ZNK17QWebSocketPrivate16handshakeOptionsEv(
    const QWebSocketPrivate *self) {
  return new QWebSocketHandshakeOptions(self->handshakeOptions());
}

//  QString QWebSocketPrivate::protocol() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebSocketPrivate8protocolEv(
    const QWebSocketPrivate *self) {
  return new QString(self->protocol());
}

//  QString QWebSocketPrivate::extension() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebSocketPrivate9extensionEv(
    const QWebSocketPrivate *self) {
  return new QString(self->extension());
}

//  QWebSocketProtocol::CloseCode QWebSocketPrivate::closeCode() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::CloseCode ritual_ZNK17QWebSocketPrivate9closeCodeEv(
    const QWebSocketPrivate *self) {
  return self->closeCode();
}

//  QString QWebSocketPrivate::closeReason() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebSocketPrivate11closeReasonEv(
    const QWebSocketPrivate *self) {
  return new QString(self->closeReason());
}

#if !defined(QT_NO_SSL)
//  void QWebSocketPrivate::ignoreSslErrors(const QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate15ignoreSslErrorsERK5QListI9QSslErrorE(
    QWebSocketPrivate *self,
    const QList<QSslError> *errors) {
  self->ignoreSslErrors(*errors);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QWebSocketPrivate::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate15ignoreSslErrorsEv(
    QWebSocketPrivate *self) {
  self->ignoreSslErrors();
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QWebSocketPrivate::continueInterruptedHandshake()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate28continueInterruptedHandshakeEv(
    QWebSocketPrivate *self) {
  self->continueInterruptedHandshake();
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QWebSocketPrivate::setSslConfiguration(const QSslConfiguration
//      &sslConfiguration)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate19setSslConfigurationERK17QSslConfiguration(
    QWebSocketPrivate *self,
    const QSslConfiguration *sslConfiguration) {
  self->setSslConfiguration(*sslConfiguration);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  QSslConfiguration QWebSocketPrivate::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK17QWebSocketPrivate16sslConfigurationEv(
    const QWebSocketPrivate *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QWebSocketPrivate::_q_updateSslConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate25_q_updateSslConfigurationEv(
    QWebSocketPrivate *self) {
  self->_q_updateSslConfiguration();
}
#endif  // !defined(QT_NO_SSL)

//  void QWebSocketPrivate::ping(const QByteArray &payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate4pingERK10QByteArray(
    QWebSocketPrivate *self,
    const QByteArray *payload) {
  self->ping(*payload);
}

//  void QWebSocketPrivate::setSocketState(QAbstractSocket::SocketState
//      state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate14setSocketStateEN15QAbstractSocket11SocketStateE(
    QWebSocketPrivate *self,
    QAbstractSocket::SocketState state) {
  self->setSocketState(state);
}

//  void QWebSocketPrivate::setMaxAllowedIncomingFrameSize(quint64
//      maxAllowedIncomingFrameSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate30setMaxAllowedIncomingFrameSizeEy(
    QWebSocketPrivate *self,
    quint64 maxAllowedIncomingFrameSize) {
  self->setMaxAllowedIncomingFrameSize(maxAllowedIncomingFrameSize);
}

//  quint64 QWebSocketPrivate::maxAllowedIncomingFrameSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QWebSocketPrivate27maxAllowedIncomingFrameSizeEv(
    const QWebSocketPrivate *self) {
  return self->maxAllowedIncomingFrameSize();
}

//  void QWebSocketPrivate::setMaxAllowedIncomingMessageSize(quint64
//      maxAllowedIncomingMessageSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate32setMaxAllowedIncomingMessageSizeEy(
    QWebSocketPrivate *self,
    quint64 maxAllowedIncomingMessageSize) {
  self->setMaxAllowedIncomingMessageSize(maxAllowedIncomingMessageSize);
}

//  quint64 QWebSocketPrivate::maxAllowedIncomingMessageSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QWebSocketPrivate29maxAllowedIncomingMessageSizeEv(
    const QWebSocketPrivate *self) {
  return self->maxAllowedIncomingMessageSize();
}

//  quint64 QWebSocketPrivate::maxIncomingMessageSize()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN17QWebSocketPrivate22maxIncomingMessageSizeEv() {
  return QWebSocketPrivate::maxIncomingMessageSize();
}

//  quint64 QWebSocketPrivate::maxIncomingFrameSize()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN17QWebSocketPrivate20maxIncomingFrameSizeEv() {
  return QWebSocketPrivate::maxIncomingFrameSize();
}

//  quint64 QWebSocketPrivate::outgoingFrameSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK17QWebSocketPrivate17outgoingFrameSizeEv(
    const QWebSocketPrivate *self) {
  return self->outgoingFrameSize();
}

//  void QWebSocketPrivate::setVersion(QWebSocketProtocol::Version version)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate10setVersionEN18QWebSocketProtocol7VersionE(
    QWebSocketPrivate *self,
    QWebSocketProtocol::Version version) {
  self->setVersion(version);
}

//  void QWebSocketPrivate::setResourceName(const QString &resourceName)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate15setResourceNameERK7QString(
    QWebSocketPrivate *self,
    const QString *resourceName) {
  self->setResourceName(*resourceName);
}

//  void QWebSocketPrivate::setRequest(const QNetworkRequest &request, const
//      QWebSocketHandshakeOptions &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate10setRequestERK15QNetworkRequestRK26QWebSocketHandshakeOptions(
    QWebSocketPrivate *self,
    const QNetworkRequest *request,
    const QWebSocketHandshakeOptions *options) {
  self->setRequest(*request, *options);
}

//  void QWebSocketPrivate::setOrigin(const QString &origin)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate9setOriginERK7QString(
    QWebSocketPrivate *self,
    const QString *origin) {
  self->setOrigin(*origin);
}

//  void QWebSocketPrivate::setProtocol(const QString &protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate11setProtocolERK7QString(
    QWebSocketPrivate *self,
    const QString *protocol) {
  self->setProtocol(*protocol);
}

//  void QWebSocketPrivate::setExtension(const QString &extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate12setExtensionERK7QString(
    QWebSocketPrivate *self,
    const QString *extension) {
  self->setExtension(*extension);
}

//  void QWebSocketPrivate::enableMasking(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate13enableMaskingEb(
    QWebSocketPrivate *self,
    bool enable) {
  self->enableMasking(enable);
}

//  void QWebSocketPrivate::setErrorString(const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate14setErrorStringERK7QString(
    QWebSocketPrivate *self,
    const QString *errorString) {
  self->setErrorString(*errorString);
}

//  QStringList QWebSocketPrivate::requestedSubProtocols() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QWebSocketPrivate21requestedSubProtocolsEv(
    const QWebSocketPrivate *self) {
  return new QList<QString>(self->requestedSubProtocols());
}

//  void QWebSocketPrivate::socketDestroyed(QObject *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate15socketDestroyedEP7QObject(
    QWebSocketPrivate *self,
    QObject *socket) {
  self->socketDestroyed(socket);
}

//  void QWebSocketPrivate::processPing(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate11processPingERK10QByteArray(
    QWebSocketPrivate *self,
    const QByteArray *data) {
  self->processPing(*data);
}

//  void QWebSocketPrivate::processPong(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate11processPongERK10QByteArray(
    QWebSocketPrivate *self,
    const QByteArray *data) {
  self->processPong(*data);
}

//  qint64 QWebSocketPrivate::doWriteFrames(const QByteArray &data, bool
//      isBinary)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN17QWebSocketPrivate13doWriteFramesERK10QByteArrayb(
    QWebSocketPrivate *self,
    const QByteArray *data,
    bool isBinary) {
  return self->doWriteFrames(*data, isBinary);
}

//  void QWebSocketPrivate::releaseConnections(const QTcpSocket *pTcpSocket)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate18releaseConnectionsEPK10QTcpSocket(
    QWebSocketPrivate *self,
    const QTcpSocket *pTcpSocket) {
  self->releaseConnections(pTcpSocket);
}

//  QByteArray QWebSocketPrivate::getFrameHeader(QWebSocketProtocol::OpCode
//      opCode, quint64 payloadLength, quint32 maskingKey, bool lastFrame)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QWebSocketPrivate14getFrameHeaderEN18QWebSocketProtocol6OpCodeEyjb(
    QWebSocketPrivate *self,
    QWebSocketProtocol::OpCode opCode,
    quint64 payloadLength,
    quint32 maskingKey,
    bool lastFrame) {
  return new QByteArray(
      self->getFrameHeader(
          opCode,
          payloadLength,
          maskingKey,
          lastFrame));
}

//  QString QWebSocketPrivate::calculateAcceptKey(const QByteArray &key)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebSocketPrivate18calculateAcceptKeyERK10QByteArray(
    const QWebSocketPrivate *self,
    const QByteArray *key) {
  return new QString(self->calculateAcceptKey(*key));
}

//  quint32 QWebSocketPrivate::generateMaskingKey() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK17QWebSocketPrivate18generateMaskingKeyEv(
    const QWebSocketPrivate *self) {
  return self->generateMaskingKey();
}

//  QByteArray QWebSocketPrivate::generateKey() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QWebSocketPrivate11generateKeyEv(
    const QWebSocketPrivate *self) {
  return new QByteArray(self->generateKey());
}

//  qint64 QWebSocketPrivate::writeFrames(const QList<QByteArray> &frames)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN17QWebSocketPrivate11writeFramesERK5QListI10QByteArrayE(
    QWebSocketPrivate *self,
    const QList<QByteArray> *frames) {
  return self->writeFrames(*frames);
}

//  qint64 QWebSocketPrivate::writeFrame(const QByteArray &frame)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN17QWebSocketPrivate10writeFrameERK10QByteArray(
    QWebSocketPrivate *self,
    const QByteArray *frame) {
  return self->writeFrame(*frame);
}

//  void QWebSocketPrivate::emitErrorOccurred(QAbstractSocket::SocketError
//      error)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QWebSocketPrivate17emitErrorOccurredEN15QAbstractSocket11SocketErrorE(
    QWebSocketPrivate *self,
    QAbstractSocket::SocketError error) {
  self->emitErrorOccurred(error);
}
