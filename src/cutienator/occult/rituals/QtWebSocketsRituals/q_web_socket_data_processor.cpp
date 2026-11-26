//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketdataprocessor_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QWebSocketDataProcessor'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 6 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketdataprocessor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWebSockets/private/qwebsocketframe_p.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QtEndian>
#include <QtCore/QDebug>
#include <QtCore/QIODevice>
#include <QtWebSockets/private/qwebsocketdataprocessor_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtWebSockets/private/qwebsocketframe_p.h>
#include <QtCore/QtEndian>
#include <QtCore/QDebug>
#include <QtCore/QIODevice>
#include <QtCore/QStringDecoder>
#include <limits.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QString>
#include <QtCore/QSet>
#include <QtCore/QtEndian>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtWebSockets__QWebSocketDataProcessor.cpp, line 1, as moc:QWebSocketDataProcessor
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN23QWebSocketDataProcessorE_t {};
} // unnamed namespace

template <> constexpr inline auto QWebSocketDataProcessor::qt_create_metaobjectdata<qt_meta_tag_ZN23QWebSocketDataProcessorE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QWebSocketDataProcessor",
        "pingReceived",
        "",
        "data",
        "pongReceived",
        "closeReceived",
        "QWebSocketProtocol::CloseCode",
        "closeCode",
        "closeReason",
        "textFrameReceived",
        "frame",
        "lastFrame",
        "binaryFrameReceived",
        "textMessageReceived",
        "message",
        "binaryMessageReceived",
        "errorEncountered",
        "code",
        "description",
        "process",
        "QIODevice*",
        "pIoDevice",
        "clear"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'pingReceived'
        QtMocHelpers::SignalData<void(const QByteArray &)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QByteArray, 3 },
        }}),
        // Signal 'pongReceived'
        QtMocHelpers::SignalData<void(const QByteArray &)>(4, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QByteArray, 3 },
        }}),
        // Signal 'closeReceived'
        QtMocHelpers::SignalData<void(QWebSocketProtocol::CloseCode, const QString &)>(5, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 7 }, { QMetaType::QString, 8 },
        }}),
        // Signal 'textFrameReceived'
        QtMocHelpers::SignalData<void(const QString &, bool)>(9, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 10 }, { QMetaType::Bool, 11 },
        }}),
        // Signal 'binaryFrameReceived'
        QtMocHelpers::SignalData<void(const QByteArray &, bool)>(12, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QByteArray, 10 }, { QMetaType::Bool, 11 },
        }}),
        // Signal 'textMessageReceived'
        QtMocHelpers::SignalData<void(const QString &)>(13, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 14 },
        }}),
        // Signal 'binaryMessageReceived'
        QtMocHelpers::SignalData<void(const QByteArray &)>(15, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QByteArray, 14 },
        }}),
        // Signal 'errorEncountered'
        QtMocHelpers::SignalData<void(QWebSocketProtocol::CloseCode, const QString &)>(16, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 17 }, { QMetaType::QString, 18 },
        }}),
        // Slot 'process'
        QtMocHelpers::SlotData<bool(QIODevice *)>(19, 2, QMC::AccessPublic, QMetaType::Bool, {{
            { 0x80000000 | 20, 21 },
        }}),
        // Slot 'clear'
        QtMocHelpers::SlotData<void()>(22, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QWebSocketDataProcessor, qt_meta_tag_ZN23QWebSocketDataProcessorE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QWebSocketDataProcessor::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QWebSocketDataProcessorE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QWebSocketDataProcessorE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN23QWebSocketDataProcessorE_t>.metaTypes,
    nullptr
} };

void QWebSocketDataProcessor::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QWebSocketDataProcessor *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->pingReceived((*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[1]))); break;
        case 1: _t->pongReceived((*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[1]))); break;
        case 2: _t->closeReceived((*reinterpret_cast<std::add_pointer_t<QWebSocketProtocol::CloseCode>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2]))); break;
        case 3: _t->textFrameReceived((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<bool>>(_a[2]))); break;
        case 4: _t->binaryFrameReceived((*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<bool>>(_a[2]))); break;
        case 5: _t->textMessageReceived((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1]))); break;
        case 6: _t->binaryMessageReceived((*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[1]))); break;
        case 7: _t->errorEncountered((*reinterpret_cast<std::add_pointer_t<QWebSocketProtocol::CloseCode>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2]))); break;
        case 8: { bool _r = _t->process((*reinterpret_cast<std::add_pointer_t<QIODevice*>>(_a[1])));
            if (_a[0]) *reinterpret_cast<bool*>(_a[0]) = std::move(_r); }  break;
        case 9: _t->clear(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QWebSocketDataProcessor::*)(const QByteArray & )>(_a, &QWebSocketDataProcessor::pingReceived, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QWebSocketDataProcessor::*)(const QByteArray & )>(_a, &QWebSocketDataProcessor::pongReceived, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QWebSocketDataProcessor::*)(QWebSocketProtocol::CloseCode , const QString & )>(_a, &QWebSocketDataProcessor::closeReceived, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QWebSocketDataProcessor::*)(const QString & , bool )>(_a, &QWebSocketDataProcessor::textFrameReceived, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QWebSocketDataProcessor::*)(const QByteArray & , bool )>(_a, &QWebSocketDataProcessor::binaryFrameReceived, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (QWebSocketDataProcessor::*)(const QString & )>(_a, &QWebSocketDataProcessor::textMessageReceived, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (QWebSocketDataProcessor::*)(const QByteArray & )>(_a, &QWebSocketDataProcessor::binaryMessageReceived, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (QWebSocketDataProcessor::*)(QWebSocketProtocol::CloseCode , const QString & )>(_a, &QWebSocketDataProcessor::errorEncountered, 7))
            return;
    }
}

const QMetaObject *QWebSocketDataProcessor::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QWebSocketDataProcessor::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QWebSocketDataProcessorE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QWebSocketDataProcessor::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 10)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 10;
    }
    return _id;
}

// SIGNAL 0
void QWebSocketDataProcessor::pingReceived(const QByteArray & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void QWebSocketDataProcessor::pongReceived(const QByteArray & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1);
}

// SIGNAL 2
void QWebSocketDataProcessor::closeReceived(QWebSocketProtocol::CloseCode _t1, const QString & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 2, nullptr, _t1, _t2);
}

// SIGNAL 3
void QWebSocketDataProcessor::textFrameReceived(const QString & _t1, bool _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 3, nullptr, _t1, _t2);
}

// SIGNAL 4
void QWebSocketDataProcessor::binaryFrameReceived(const QByteArray & _t1, bool _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 4, nullptr, _t1, _t2);
}

// SIGNAL 5
void QWebSocketDataProcessor::textMessageReceived(const QString & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 5, nullptr, _t1);
}

// SIGNAL 6
void QWebSocketDataProcessor::binaryMessageReceived(const QByteArray & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 6, nullptr, _t1);
}

// SIGNAL 7
void QWebSocketDataProcessor::errorEncountered(QWebSocketProtocol::CloseCode _t1, const QString & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 7, nullptr, _t1, _t2);
}
QT_WARNING_POP

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

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 63, as _ZN23QWebSocketDataProcessorD0Ev
inline QWebSocketDataProcessor::~QWebSocketDataProcessor()
{
    clear();
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 66, as _ZNK15QWebSocketFrame11closeReasonEv
inline QString QWebSocketFrame::closeReason() const
{
    return isDone() ? m_closeReason : tr("Waiting for more data from socket.");
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 90, as _ZNK15QWebSocketFrame11isDataFrameEv
inline bool QWebSocketFrame::isDataFrame() const
{
    return !isControlFrame();
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 74, as _ZNK15QWebSocketFrame12isFinalFrameEv
inline bool QWebSocketFrame::isFinalFrame() const
{
    return m_isFinalFrame;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 82, as _ZNK15QWebSocketFrame14isControlFrameEv
inline bool QWebSocketFrame::isControlFrame() const
{
    return (m_opCode & 0x08) == 0x08;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 98, as _ZNK15QWebSocketFrame19isContinuationFrameEv
inline bool QWebSocketFrame::isContinuationFrame() const
{
    return isDataFrame() && (m_opCode == QWebSocketProtocol::OpCodeContinue);
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 167, as _ZNK15QWebSocketFrame6isDoneEv
inline bool QWebSocketFrame::isDone() const
{
    return m_processingState == PS_DISPATCH_RESULT;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 122, as _ZNK15QWebSocketFrame6opCodeEv
inline QWebSocketProtocol::OpCode QWebSocketFrame::opCode() const
{
    return m_opCode;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 159, as _ZNK15QWebSocketFrame7isValidEv
inline bool QWebSocketFrame::isValid() const
{
    return isDone() && m_isValid;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 130, as _ZNK15QWebSocketFrame7payloadEv
inline QByteArray QWebSocketFrame::payload() const
{
    return m_payload;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 58, as _ZNK15QWebSocketFrame9closeCodeEv
inline QWebSocketProtocol::CloseCode QWebSocketFrame::closeCode() const
{
    return isDone() ? m_closeCode : QWebSocketProtocol::CloseCodeGoingAway;
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

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 325, as _ZN15QWebSocketFrame13readFrameMaskEP9QIODevice
inline QWebSocketFrame::ProcessingState QWebSocketFrame::readFrameMask(QIODevice *pIoDevice)
{
    if (Q_LIKELY(pIoDevice->bytesAvailable() >= 4)) {
        if (Q_UNLIKELY(pIoDevice->read(reinterpret_cast<char *>(&m_mask), sizeof(m_mask)) < 4)) {
            setError(QWebSocketProtocol::CloseCodeGoingAway,
                     tr("Error while reading from the network: %1.").arg(pIoDevice->errorString()));
            return PS_DISPATCH_RESULT;
        }
        m_mask = qFromBigEndian(m_mask);
        return PS_READ_PAYLOAD;
    }
    return PS_WAIT_FOR_MORE_DATA;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 224, as _ZN15QWebSocketFrame15readFrameHeaderEP9QIODevice
inline QWebSocketFrame::ProcessingState QWebSocketFrame::readFrameHeader(QIODevice *pIoDevice)
{
    if (Q_LIKELY(pIoDevice->bytesAvailable() >= 2)) {
        // FIN, RSV1-3, Opcode
        char header[2] = {0};
        if (Q_UNLIKELY(pIoDevice->read(header, 2) < 2)) {
            setError(QWebSocketProtocol::CloseCodeGoingAway,
                     tr("Error occurred while reading header from the network: %1")
                        .arg(pIoDevice->errorString()));
            return PS_DISPATCH_RESULT;
        }
        m_isFinalFrame = (header[0] & 0x80) != 0;
        m_rsv1 = (header[0] & 0x40);
        m_rsv2 = (header[0] & 0x20);
        m_rsv3 = (header[0] & 0x10);
        m_opCode = static_cast<QWebSocketProtocol::OpCode>(header[0] & 0x0F);

        // Mask
        // Use zero as mask value to mean there's no mask to read.
        // When the mask value is read, it over-writes this non-zero value.
        m_mask = header[1] & 0x80;
        // PayloadLength
        m_length = (header[1] & 0x7F);

        if (!checkValidity())
            return PS_DISPATCH_RESULT;

        switch (m_length) {
        case 126:
        case 127:
            return PS_READ_PAYLOAD_LENGTH;
        default:
            return hasMask() ? PS_READ_MASK : PS_READ_PAYLOAD;
        }
    }
    return PS_WAIT_FOR_MORE_DATA;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 342, as _ZN15QWebSocketFrame16readFramePayloadEP9QIODevice
inline QWebSocketFrame::ProcessingState QWebSocketFrame::readFramePayload(QIODevice *pIoDevice)
{
    if (!m_length)
        return PS_DISPATCH_RESULT;

    if (Q_UNLIKELY(m_length > maxAllowedFrameSize())) {
        setError(QWebSocketProtocol::CloseCodeTooMuchData, tr("Maximum framesize exceeded."));
        return PS_DISPATCH_RESULT;
    }
    if (quint64(pIoDevice->bytesAvailable()) >= m_length) {
        m_payload = pIoDevice->read(int(m_length));
        // m_length can be safely cast to an integer,
        // because MAX_FRAME_SIZE_IN_BYTES = MAX_INT
        if (Q_UNLIKELY(m_payload.size() != int(m_length))) {
            // some error occurred; refer to the Qt documentation of QIODevice::read()
            setError(QWebSocketProtocol::CloseCodeAbnormalDisconnection,
                     tr("Some serious error occurred while reading from the network."));
        } else if (hasMask()) {
            QWebSocketProtocol::mask(&m_payload, mask());
        }
        return PS_DISPATCH_RESULT;
    }
    return PS_WAIT_FOR_MORE_DATA;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 265, as _ZN15QWebSocketFrame22readFramePayloadLengthEP9QIODevice
inline QWebSocketFrame::ProcessingState QWebSocketFrame::readFramePayloadLength(QIODevice *pIoDevice)
{
    // see https://tools.ietf.org/html/rfc6455#page-28 paragraph 5.2
    // in all cases, the minimal number of bytes MUST be used to encode the length,
    // for example, the length of a 124-byte-long string can't be encoded as the
    // sequence 126, 0, 124"
    switch (m_length) {
    case 126:
        if (Q_LIKELY(pIoDevice->bytesAvailable() >= 2)) {
            uchar length[2] = {0};
            if (Q_UNLIKELY(pIoDevice->read(reinterpret_cast<char *>(length), 2) < 2)) {
                setError(QWebSocketProtocol::CloseCodeGoingAway,
                         tr("Error occurred while reading from the network: %1")
                            .arg(pIoDevice->errorString()));
                return PS_DISPATCH_RESULT;
            }
            m_length = qFromBigEndian<quint16>(reinterpret_cast<const uchar *>(length));
            if (Q_UNLIKELY(m_length < 126)) {

                setError(QWebSocketProtocol::CloseCodeProtocolError,
                            tr("Lengths smaller than 126 must be expressed as one byte."));
                return PS_DISPATCH_RESULT;
            }
            return hasMask() ? PS_READ_MASK : PS_READ_PAYLOAD;
        }
        break;
    case 127:
        if (Q_LIKELY(pIoDevice->bytesAvailable() >= 8)) {
            uchar length[8] = {0};
            if (Q_UNLIKELY(pIoDevice->read(reinterpret_cast<char *>(length), 8) < 8)) {
                setError(QWebSocketProtocol::CloseCodeAbnormalDisconnection,
                         tr("Something went wrong during reading from the network."));
                return PS_DISPATCH_RESULT;
            }
            // Most significant bit must be set to 0 as
            // per https://tools.ietf.org/html/rfc6455#section-5.2
            m_length = qFromBigEndian<quint64>(length);
            if (Q_UNLIKELY(m_length & (quint64(1) << 63))) {
                setError(QWebSocketProtocol::CloseCodeProtocolError,
                            tr("Highest bit of payload length is not 0."));
                return PS_DISPATCH_RESULT;
            }
            if (Q_UNLIKELY(m_length <= 0xFFFFu)) {
                setError(QWebSocketProtocol::CloseCodeProtocolError,
                            tr("Lengths smaller than 65536 (2^16) must be expressed as 2 bytes."));
                return PS_DISPATCH_RESULT;
            }
            return hasMask() ? PS_READ_MASK : PS_READ_PAYLOAD;
        }
        break;
    default:
        Q_UNREACHABLE();
        break;
    }
    return PS_WAIT_FOR_MORE_DATA;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 381, as _ZN15QWebSocketFrame13checkValidityEv
inline bool QWebSocketFrame::checkValidity()
{
    if (Q_UNLIKELY(m_rsv1 || m_rsv2 || m_rsv3)) {
        setError(QWebSocketProtocol::CloseCodeProtocolError, tr("Rsv field is non-zero"));
    } else if (Q_UNLIKELY(QWebSocketProtocol::isOpCodeReserved(m_opCode))) {
        setError(QWebSocketProtocol::CloseCodeProtocolError, tr("Used reserved opcode"));
    } else if (isControlFrame()) {
        if (Q_UNLIKELY(m_length > 125)) {
            setError(QWebSocketProtocol::CloseCodeProtocolError,
                     tr("Control frame is larger than 125 bytes"));
        } else if (Q_UNLIKELY(!m_isFinalFrame)) {
            setError(QWebSocketProtocol::CloseCodeProtocolError,
                     tr("Control frames cannot be fragmented"));
        } else {
            m_isValid = true;
        }
    } else {
        m_isValid = true;
    }
    return m_isValid;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 370, as _ZN15QWebSocketFrame8setErrorEN18QWebSocketProtocol9CloseCodeERK7QString
inline void QWebSocketFrame::setError(QWebSocketProtocol::CloseCode code, const QString &closeReason)
{
    clear();
    m_closeCode = code;
    m_closeReason = closeReason;
    m_isValid = false;
}

//  from ../qtwebsockets/src/websockets/qwebsocketprotocol.cpp, line 158, as _ZN18QWebSocketProtocol4maskEP10QByteArrayj
inline void QWebSocketProtocol::mask(QByteArray *payload, quint32 maskingKey)
{
    Q_ASSERT(payload);
    mask(payload->data(), quint64(payload->size()), maskingKey);
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 114, as _ZNK15QWebSocketFrame4maskEv
inline quint32 QWebSocketFrame::mask() const
{
    return m_mask;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 106, as _ZNK15QWebSocketFrame7hasMaskEv
inline bool QWebSocketFrame::hasMask() const
{
    return m_mask != 0;
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

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 114, as _ZN23QWebSocketDataProcessor14setIdleTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE
inline void QWebSocketDataProcessor::setIdleTimeout(std::chrono::milliseconds timeout)
{
    Q_ASSERT(!m_waitTimer->isActive());
    m_waitTimer->setInterval(timeout);
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 123, as _ZNK23QWebSocketDataProcessor11idleTimeoutEv
inline std::chrono::milliseconds QWebSocketDataProcessor::idleTimeout() const
{
    using namespace std::chrono;
    return duration_cast<milliseconds>(m_waitTimer->interval());
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

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 264, as _ZN23QWebSocketDataProcessor19processControlFrameERK15QWebSocketFrame
inline bool QWebSocketDataProcessor::processControlFrame(const QWebSocketFrame &frame)
{
    bool mustStopProcessing = true; //control frames never expect additional frames to be processed
    switch (frame.opCode()) {
    case QWebSocketProtocol::OpCodePing:
        Q_EMIT pingReceived(frame.payload());
        break;

    case QWebSocketProtocol::OpCodePong:
        Q_EMIT pongReceived(frame.payload());
        break;

    case QWebSocketProtocol::OpCodeClose:
    {
        quint16 closeCode = QWebSocketProtocol::CloseCodeNormal;
        QString closeReason;
        QByteArray payload = frame.payload();
        if (Q_UNLIKELY(payload.size() == 1)) {
            //size is either 0 (no close code and no reason)
            //or >= 2 (at least a close code of 2 bytes)
            closeCode = QWebSocketProtocol::CloseCodeProtocolError;
            closeReason = tr("Payload of close frame is too small.");
        } else if (Q_LIKELY(payload.size() > 1)) {
            //close frame can have a close code and reason
            closeCode = qFromBigEndian<quint16>(reinterpret_cast<const uchar *>(payload.constData()));
            if (Q_UNLIKELY(!QWebSocketProtocol::isCloseCodeValid(closeCode))) {
                closeCode = QWebSocketProtocol::CloseCodeProtocolError;
                closeReason = tr("Invalid close code %1 detected.").arg(closeCode);
            } else {
                if (payload.size() > 2) {
                    auto toUtf16 = QStringDecoder(QStringDecoder::Utf8,
                        QStringDecoder::Flag::Stateless | QStringDecoder::Flag::ConvertInvalidToNull);
                    closeReason = toUtf16(QByteArrayView(payload).sliced(2));
                    if (Q_UNLIKELY(toUtf16.hasError())) {
                        closeCode = QWebSocketProtocol::CloseCodeWrongDatatype;
                        closeReason = tr("Invalid UTF-8 code encountered.");
                    }
                }
            }
        }
        Q_EMIT closeReceived(static_cast<QWebSocketProtocol::CloseCode>(closeCode), closeReason);
        break;
    }

    case QWebSocketProtocol::OpCodeContinue:
    case QWebSocketProtocol::OpCodeBinary:
    case QWebSocketProtocol::OpCodeText:
    case QWebSocketProtocol::OpCodeReserved3:
    case QWebSocketProtocol::OpCodeReserved4:
    case QWebSocketProtocol::OpCodeReserved5:
    case QWebSocketProtocol::OpCodeReserved6:
    case QWebSocketProtocol::OpCodeReserved7:
    case QWebSocketProtocol::OpCodeReservedC:
    case QWebSocketProtocol::OpCodeReservedB:
    case QWebSocketProtocol::OpCodeReservedD:
    case QWebSocketProtocol::OpCodeReservedE:
    case QWebSocketProtocol::OpCodeReservedF:
        //do nothing
        //case statements added to make C++ compiler happy
        break;

    default:
        Q_EMIT errorEncountered(QWebSocketProtocol::CloseCodeProtocolError,
                                tr("Invalid opcode detected: %1").arg(int(frame.opCode())));
        //do nothing
        break;
    }
    return mustStopProcessing;
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 253, as _ZN23QWebSocketDataProcessor11reportErrorEN18QWebSocketProtocol9CloseCodeERK7QString
inline void QWebSocketDataProcessor::reportError(QWebSocketProtocol::CloseCode code,
                                          const QString &description)
{
    clear();
    m_hasFailed = true;
    Q_EMIT errorEncountered(code, description);
}

//  from ../qtwebsockets/src/websockets/qwebsocketdataprocessor.cpp, line 337, as _ZN23QWebSocketDataProcessor7timeoutEv
inline void QWebSocketDataProcessor::timeout()
{
    reportError(QWebSocketProtocol::CloseCodeGoingAway,
                tr("Timeout when reading data from socket."));
}
//  -----------------------------------------------------------------------

//  A QWebSocketDataProcessor that Python can take functions over in. Every QWebSocketDataProcessor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebSocketDataProcessorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebSocketDataProcessorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketDataProcessorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketDataProcessorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketDataProcessorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketDataProcessorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketDataProcessorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebSocketDataProcessor : public QWebSocketDataProcessor {
public:
  using QWebSocketDataProcessor::QWebSocketDataProcessor;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebSocketDataProcessorCall0 call = reinterpret_cast<CuteQWebSocketDataProcessorCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebSocketDataProcessorCall1 call = reinterpret_cast<CuteQWebSocketDataProcessorCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebSocketDataProcessorCall2 call = reinterpret_cast<CuteQWebSocketDataProcessorCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebSocketDataProcessorCall3 call = reinterpret_cast<CuteQWebSocketDataProcessorCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebSocketDataProcessorCall4 call = reinterpret_cast<CuteQWebSocketDataProcessorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebSocketDataProcessorCall5 call = reinterpret_cast<CuteQWebSocketDataProcessorCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebSocketDataProcessorCall6 call = reinterpret_cast<CuteQWebSocketDataProcessorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebSocketDataProcessor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QWebSocketDataProcessor10metaObjectEv(
    const QWebSocketDataProcessor *self) {
  return self->metaObject();
}

//  void *QWebSocketDataProcessor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QWebSocketDataProcessor11qt_metacastEPKc(
    QWebSocketDataProcessor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebSocketDataProcessor::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QWebSocketDataProcessor11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebSocketDataProcessor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebSocketDataProcessor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QWebSocketDataProcessor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebSocketDataProcessor::tr(s, c, n));
}

//  QWebSocketDataProcessor::QWebSocketDataProcessor(QObject *parent)
extern "C" Q_DECL_EXPORT
QWebSocketDataProcessor *ritual_ZN23QWebSocketDataProcessorC1EP7QObject(
    QObject *parent) {
  return new CuteQWebSocketDataProcessor(parent);
}

//  QWebSocketDataProcessor::~QWebSocketDataProcessor()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessorD1Ev(QWebSocketDataProcessor *self) {
  delete self;
}

//  void QWebSocketDataProcessor::setMaxAllowedFrameSize(quint64
//      maxAllowedFrameSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor22setMaxAllowedFrameSizeEy(
    QWebSocketDataProcessor *self,
    quint64 maxAllowedFrameSize) {
  self->setMaxAllowedFrameSize(maxAllowedFrameSize);
}

//  quint64 QWebSocketDataProcessor::maxAllowedFrameSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK23QWebSocketDataProcessor19maxAllowedFrameSizeEv(
    const QWebSocketDataProcessor *self) {
  return self->maxAllowedFrameSize();
}

//  void QWebSocketDataProcessor::setMaxAllowedMessageSize(quint64
//      maxAllowedMessageSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor24setMaxAllowedMessageSizeEy(
    QWebSocketDataProcessor *self,
    quint64 maxAllowedMessageSize) {
  self->setMaxAllowedMessageSize(maxAllowedMessageSize);
}

//  quint64 QWebSocketDataProcessor::maxAllowedMessageSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK23QWebSocketDataProcessor21maxAllowedMessageSizeEv(
    const QWebSocketDataProcessor *self) {
  return self->maxAllowedMessageSize();
}

//  quint64 QWebSocketDataProcessor::maxMessageSize()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN23QWebSocketDataProcessor14maxMessageSizeEv() {
  return QWebSocketDataProcessor::maxMessageSize();
}

//  quint64 QWebSocketDataProcessor::maxFrameSize()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN23QWebSocketDataProcessor12maxFrameSizeEv() {
  return QWebSocketDataProcessor::maxFrameSize();
}

//  void QWebSocketDataProcessor::setIdleTimeout(std::chrono::milliseconds
//      timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor14setIdleTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QWebSocketDataProcessor *self,
    long long timeout) {
  self->setIdleTimeout(std::chrono::milliseconds(timeout));
}

//  std::chrono::milliseconds QWebSocketDataProcessor::idleTimeout() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK23QWebSocketDataProcessor11idleTimeoutEv(
    const QWebSocketDataProcessor *self) {
  return static_cast<long long>(self->idleTimeout().count());
}

//  void QWebSocketDataProcessor::pingReceived(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor12pingReceivedERK10QByteArray(
    QWebSocketDataProcessor *self,
    const QByteArray *data) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWebSocketDataProcessor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pingReceived(const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pingReceived(const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(data)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QWebSocketDataProcessor::pongReceived(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor12pongReceivedERK10QByteArray(
    QWebSocketDataProcessor *self,
    const QByteArray *data) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWebSocketDataProcessor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pongReceived(const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pongReceived(const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(data)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QWebSocketDataProcessor::closeReceived(QWebSocketProtocol::CloseCode
//      closeCode, const QString &closeReason)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor13closeReceivedEN18QWebSocketProtocol9CloseCodeERK7QString(
    QWebSocketDataProcessor *self,
    QWebSocketProtocol::CloseCode closeCode,
    const QString *closeReason) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWebSocketDataProcessor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "closeReceived(QWebSocketProtocol::CloseCode,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "closeReceived(QWebSocketProtocol::CloseCode,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&closeCode)),
      const_cast<void *>(static_cast<const void *>(closeReason)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QWebSocketDataProcessor::textFrameReceived(const QString &frame,
//      bool lastFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor17textFrameReceivedERK7QStringb(
    QWebSocketDataProcessor *self,
    const QString *frame,
    bool lastFrame) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWebSocketDataProcessor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textFrameReceived(const QString &,bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textFrameReceived(const QString &,bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(frame)),
      const_cast<void *>(static_cast<const void *>(&lastFrame)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QWebSocketDataProcessor::binaryFrameReceived(const QByteArray
//      &frame, bool lastFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor19binaryFrameReceivedERK10QByteArrayb(
    QWebSocketDataProcessor *self,
    const QByteArray *frame,
    bool lastFrame) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWebSocketDataProcessor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "binaryFrameReceived(const QByteArray &,bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "binaryFrameReceived(const QByteArray &,bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(frame)),
      const_cast<void *>(static_cast<const void *>(&lastFrame)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QWebSocketDataProcessor::textMessageReceived(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor19textMessageReceivedERK7QString(
    QWebSocketDataProcessor *self,
    const QString *message) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWebSocketDataProcessor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textMessageReceived(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textMessageReceived(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(message)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QWebSocketDataProcessor::binaryMessageReceived(const QByteArray
//      &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor21binaryMessageReceivedERK10QByteArray(
    QWebSocketDataProcessor *self,
    const QByteArray *message) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWebSocketDataProcessor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "binaryMessageReceived(const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "binaryMessageReceived(const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(message)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QWebSocketDataProcessor::errorEncountered(QWebSocketProtocol::CloseCo
//      de code, const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor16errorEncounteredEN18QWebSocketProtocol9CloseCodeERK7QString(
    QWebSocketDataProcessor *self,
    QWebSocketProtocol::CloseCode code,
    const QString *description) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWebSocketDataProcessor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "errorEncountered(QWebSocketProtocol::CloseCode,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "errorEncountered(QWebSocketProtocol::CloseCode,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&code)),
      const_cast<void *>(static_cast<const void *>(description)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QWebSocketDataProcessor::process(QIODevice *pIoDevice)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QWebSocketDataProcessor7processEP9QIODevice(
    QWebSocketDataProcessor *self,
    QIODevice *pIoDevice) {
  return self->process(pIoDevice);
}

//  void QWebSocketDataProcessor::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor5clearEv(
    QWebSocketDataProcessor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWebSocketDataProcessor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "clear()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "clear()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QWebSocketDataProcessor::processControlFrame(const QWebSocketFrame
//      &frame)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QWebSocketDataProcessor19processControlFrameERK15QWebSocketFrame(
    QWebSocketDataProcessor *self,
    const QWebSocketFrame *frame) {
  return self->processControlFrame(*frame);
}

//  void QWebSocketDataProcessor::reportError(QWebSocketProtocol::CloseCode
//      code, const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor11reportErrorEN18QWebSocketProtocol9CloseCodeERK7QString(
    QWebSocketDataProcessor *self,
    QWebSocketProtocol::CloseCode code,
    const QString *description) {
  self->reportError(code, *description);
}

//  void QWebSocketDataProcessor::timeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketDataProcessor7timeoutEv(
    QWebSocketDataProcessor *self) {
  self->timeout();
}

//  a Python function taken by a CuteQWebSocketDataProcessor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebSocketDataProcessor(
    QWebSocketDataProcessor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebSocketDataProcessor *>(self)->take(key, call);
}
