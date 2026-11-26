//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocket_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/qwebsocket.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsocket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtWebSockets/qwebsockethandshakeoptions.h>
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/private/qdefaultmaskgenerator_p.h>
#include <QtCore/QRandomGenerator>
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
#include <QtWebSockets/private/qwebsocketdataprocessor_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtWebSockets/private/qwebsocketframe_p.h>
#include <QtCore/QtEndian>
#include <QtCore/QDebug>
#include <QtCore/QIODevice>
#include <QtCore/QStringDecoder>
#include <limits.h>
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
#include <QtWebSockets/private/qwebsockethandshakeresponse_p.h>
#include <QtWebSockets/private/qwebsockethandshakerequest_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QString>
#include <QtCore/QTextStream>
#include <QtCore/QByteArray>
#include <QtCore/QStringList>
#include <QtCore/QDateTime>
#include <QtCore/QLocale>
#include <QtCore/QCryptographicHash>
#include <QtCore/QSet>
#include <QtCore/QList>
#include <QtCore/QStringBuilder>   //for more efficient string concatenation
#include <algorithm>
#include <functional>   //for std::greater
#include <iterator>
#include <QtWebSockets/private/qwebsocketframe_p.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QtEndian>
#include <QtCore/QDebug>
#include <QtCore/QIODevice>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 46, as local:qwebsocket_p.cpp:MAX_OUTGOING_FRAME_SIZE_IN_BYTES
namespace {
constexpr quint64 MAX_OUTGOING_FRAME_SIZE_IN_BYTES = std::numeric_limits<int>::max() - 1;
}  // namespace

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 47, as local:qwebsocket_p.cpp:DEFAULT_OUTGOING_FRAME_SIZE_IN_BYTES
namespace {
constexpr quint64 DEFAULT_OUTGOING_FRAME_SIZE_IN_BYTES = 512 * 512 * 2;
}  // namespace

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 57, as local:qwebsocket_p.cpp:isSeparator
namespace {
inline bool isSeparator(char c)
{
    // separators     = "(" | ")" | "<" | ">" | "@"
    //                      | "," | ";" | ":" | "\" | <">
    //                      | "/" | "[" | "]" | "?" | "="
    //                      | "{" | "}" | SP | HT
    static const char separators[] = "()<>@,;:\\\"/[]?={} \t";
    static const char *end = separators + sizeof separators - 1;
    return std::find(separators, end, c) != end;
}
}  // namespace

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 76, as local:qwebsocket_p.cpp:isValidSubProtocolName
namespace {
inline bool isValidSubProtocolName(const QString &protocol)
{
    return std::all_of(protocol.begin(), protocol.end(), [](const QChar &c) {
        return c.unicode() >= 0x21 && c.unicode() <= 0x7E && !isSeparator(c.toLatin1());
    });
}
}  // namespace

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 953, as local:qwebsocket_p.cpp:msgUnsupportedAuthenticateChallenges
static QString msgUnsupportedAuthenticateChallenges(qsizetype count)
{
    // Keep the error on a single line so it can easily be searched for:
    //: 'WWW-Authenticate' is the HTTP header.
    return count == 1
        ? QWebSocket::tr("QWebSocketPrivate::processHandshake: "
                         "Unsupported WWW-Authenticate challenge encountered.")
        : QWebSocket::tr("QWebSocketPrivate::processHandshake: "
                         "Unsupported WWW-Authenticate challenges encountered.");
}

//  from ../qtwebsockets/src/websockets/qdefaultmaskgenerator_p.cpp, line 35, as _ZN21QDefaultMaskGeneratorC1EP7QObject
inline QDefaultMaskGenerator::QDefaultMaskGenerator(QObject *parent) :
    QMaskGenerator(parent)
{
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 85, as _ZN23QWebSocketConfigurationC1Ev
inline QWebSocketConfiguration::QWebSocketConfiguration() :
#ifndef QT_NO_SSL
    m_sslConfiguration(QSslConfiguration::defaultConfiguration()),
    m_ignoredSslErrors(),
    m_ignoreSslErrors(false),
#endif
#ifndef QT_NO_NETWORKPROXY
    m_proxy(QNetworkProxy::DefaultProxy),
#endif
    m_pSocket(nullptr)
{
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 39, as _ZN23QWebSocketDataProcessorC1EP7QObject
inline QWebSocketDataProcessor::QWebSocketDataProcessor(QObject *parent) :
    QObject(parent),
    m_processingState(PS_READ_HEADER),
    m_isFinalFrame(false),
    m_isFragmented(false),
    m_opCode(QWebSocketProtocol::OpCodeClose),
    m_isControlFrame(false),
    m_hasMask(false),
    m_mask(0),
    m_payloadLength(0),
    m_decoder(QStringDecoder(QStringDecoder::Utf8, QStringDecoder::Flag::ConvertInvalidToNull)),
    m_waitTimer(new QChronoTimer(this))
{
    clear();
    // initialize the internal timeout timer
    using namespace std::chrono_literals;
    m_waitTimer->setInterval(5s);
    m_waitTimer->setSingleShot(true);
    m_waitTimer->callOnTimeout(this, &QWebSocketDataProcessor::timeout);
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

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 159, as _ZNK26QWebSocketHandshakeRequest10requestUrlEv
inline QUrl QWebSocketHandshakeRequest::requestUrl() const
{
    return m_requestUrl;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 135, as _ZNK26QWebSocketHandshakeRequest6originEv
inline QString QWebSocketHandshakeRequest::origin() const
{
    return m_origin;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 87, as _ZNK26QWebSocketHandshakeRequest7headersEv
inline QHttpHeaders QWebSocketHandshakeRequest::headers() const
{
    return m_parser.headers();
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 143, as _ZNK26QWebSocketHandshakeRequest9protocolsEv
inline QList<QString> QWebSocketHandshakeRequest::protocols() const
{
    return m_protocols;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 236, as _ZNK27QWebSocketHandshakeResponse15acceptedVersionEv
inline QWebSocketProtocol::Version QWebSocketHandshakeResponse::acceptedVersion() const
{
    return m_acceptedVersion;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 78, as _ZNK27QWebSocketHandshakeResponse16acceptedProtocolEv
inline QString QWebSocketHandshakeResponse::acceptedProtocol() const
{
    return m_acceptedProtocol;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 260, as _ZNK27QWebSocketHandshakeResponse17acceptedExtensionEv
inline QString QWebSocketHandshakeResponse::acceptedExtension() const
{
    return m_acceptedExtension;
}

//  from ../qtwebsockets/src/websockets/qdefaultmaskgenerator_p.cpp, line 45, as _ZN21QDefaultMaskGeneratorD1Ev
inline QDefaultMaskGenerator::~QDefaultMaskGenerator()
{
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 231, as _ZN23QWebSocketDataProcessor5clearEv
inline void QWebSocketDataProcessor::clear()
{
    m_processingState = PS_READ_HEADER;
    m_isFinalFrame = false;
    m_isFragmented = false;
    m_opCode = QWebSocketProtocol::OpCodeClose;
    m_hasMask = false;
    m_mask = 0;
    m_binaryMessage.clear();
    m_textMessage.clear();
    m_payloadLength = 0;
    m_decoder.resetState();
    m_hasFailed = false;
    frame.clear();
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 337, as _ZN23QWebSocketDataProcessor7timeoutEv
inline void QWebSocketDataProcessor::timeout()
{
    reportError(QWebSocketProtocol::CloseCodeGoingAway,
                tr("Timeout when reading data from socket."));
}

//  from ../qtwebsockets/src/websockets/qdefaultmaskgenerator_p.cpp, line 52, as _ZN21QDefaultMaskGenerator4seedEv
inline bool QDefaultMaskGenerator::seed() noexcept
{
    return true;
}

//  from ../qtwebsockets/src/websockets/qdefaultmaskgenerator_p.cpp, line 62, as _ZN21QDefaultMaskGenerator8nextMaskEv
inline quint32 QDefaultMaskGenerator::nextMask() noexcept
{
    quint32 value = QRandomGenerator::global()->generate();
    while (Q_UNLIKELY(value == 0)) {
        // a mask of zero has a special meaning
        value = QRandomGenerator::global()->generate();
    }
    return value;
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

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 253, as _ZN23QWebSocketDataProcessor11reportErrorEN18QWebSocketProtocol9CloseCodeERK7QString
inline void QWebSocketDataProcessor::reportError(QWebSocketProtocol::CloseCode code,
                                          const QString &description)
{
    clear();
    m_hasFailed = true;
    Q_EMIT errorEncountered(code, description);
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 101, as _ZN17QWebSocketPrivateC1ERK7QStringN18QWebSocketProtocol7VersionE
inline QWebSocketPrivate::QWebSocketPrivate(const QString &origin, QWebSocketProtocol::Version version) :
    QObjectPrivate(),
    m_pSocket(nullptr),
    m_errorString(),
    m_version(version),
    m_resourceName(),
    m_request(),
    m_origin(origin),
    m_protocol(),
    m_extension(),
    m_socketState(QAbstractSocket::UnconnectedState),
    m_pauseMode(QAbstractSocket::PauseNever),
    m_readBufferSize(0),
    m_key(),
    m_mustMask(true),
    m_isClosingHandshakeSent(false),
    m_isClosingHandshakeReceived(false),
    m_closeCode(QWebSocketProtocol::CloseCodeNormal),
    m_closeReason(),
    m_pingTimer(),
    m_configuration(),
    m_pMaskGenerator(&m_defaultMaskGenerator),
    m_defaultMaskGenerator(),
    m_outgoingFrameSize(DEFAULT_OUTGOING_FRAME_SIZE_IN_BYTES)
{
    m_pingTimer.start();
}

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

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 921, as _ZNK17QWebSocketPrivate18calculateAcceptKeyERK10QByteArray
inline QString QWebSocketPrivate::calculateAcceptKey(const QByteArray &key) const
{
    const QByteArray tmpKey = key + QByteArrayLiteral("258EAFA5-E914-47DA-95CA-C5AB0DC85B11");
    const QByteArray hash = QCryptographicHash::hash(tmpKey, QCryptographicHash::Sha1).toBase64();
    return QString::fromLatin1(hash);
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 357, as _ZN17QWebSocketPrivate11upgradeFromEP10QTcpSocketRK26QWebSocketHandshakeRequestRK27QWebSocketHandshakeResponseP7QObject
inline QWebSocket *QWebSocketPrivate::upgradeFrom(QTcpSocket *pTcpSocket,
                                           const QWebSocketHandshakeRequest &request,
                                           const QWebSocketHandshakeResponse &response,
                                           QObject *parent)
{
    QWebSocket *pWebSocket = new QWebSocket(pTcpSocket, response.acceptedVersion(), parent);
    if (Q_LIKELY(pWebSocket)) {
        QNetworkRequest netRequest(request.requestUrl());
        netRequest.setHeaders(request.headers());
#ifndef QT_NO_SSL
        if (QSslSocket *sslSock = qobject_cast<QSslSocket *>(pTcpSocket))
            pWebSocket->setSslConfiguration(sslSock->sslConfiguration());
#endif
        QWebSocketHandshakeOptions options;
        options.setSubprotocols(request.protocols());

        pWebSocket->d_func()->setExtension(response.acceptedExtension());
        pWebSocket->d_func()->setOrigin(request.origin());
        pWebSocket->d_func()->setRequest(netRequest, options);
        pWebSocket->d_func()->setProtocol(response.acceptedProtocol());
        pWebSocket->d_func()->setResourceName(request.requestUrl().toString(QUrl::RemoveUserInfo));
        //a server should not send masked frames
        pWebSocket->d_func()->enableMasking(false);
    }

    return pWebSocket;
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

#if defined(Q_OS_LINUX)
//  QWebSocketPrivate::QWebSocketPrivate(const QString &origin,
//      QWebSocketProtocol::Version version)
extern "C" Q_DECL_EXPORT
QWebSocketPrivate *ritual_ZN17QWebSocketPrivateC1ERK7QStringN18QWebSocketProtocol7VersionE(
    const QString *origin,
    QWebSocketProtocol::Version version) {
  return new QWebSocketPrivate(*origin, version);
}
#endif  // defined(Q_OS_LINUX)

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

//  QStringList QWebSocketPrivate::requestedSubProtocols() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QWebSocketPrivate21requestedSubProtocolsEv(
    const QWebSocketPrivate *self) {
  return new QList<QString>(self->requestedSubProtocols());
}

//  QString QWebSocketPrivate::calculateAcceptKey(const QByteArray &key)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QWebSocketPrivate18calculateAcceptKeyERK10QByteArray(
    const QWebSocketPrivate *self,
    const QByteArray *key) {
  return new QString(self->calculateAcceptKey(*key));
}

//  QWebSocket *QWebSocketPrivate::upgradeFrom(QTcpSocket *tcpSocket, const
//      QWebSocketHandshakeRequest &request, const
//      QWebSocketHandshakeResponse &response, QObject *parent)
extern "C" Q_DECL_EXPORT
QWebSocket *ritual_ZN17QWebSocketPrivate11upgradeFromEP10QTcpSocketRK26QWebSocketHandshakeRequestRK27QWebSocketHandshakeResponseP7QObject(
    QTcpSocket *tcpSocket,
    const QWebSocketHandshakeRequest *request,
    const QWebSocketHandshakeResponse *response,
    QObject *parent) {
  return QWebSocketPrivate::upgradeFrom(
      tcpSocket,
      *request,
      *response,
      parent);
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
