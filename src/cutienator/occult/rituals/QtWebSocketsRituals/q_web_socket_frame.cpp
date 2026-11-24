//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketframe_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QString>
#include <QtCore/QSet>
#include <QtCore/QtEndian>
#include <QtWebSockets/private/qwebsocketframe_p.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QtEndian>
#include <QtCore/QDebug>
#include <QtCore/QIODevice>
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

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 58, as _ZNK15QWebSocketFrame9closeCodeEv
inline QWebSocketProtocol::CloseCode QWebSocketFrame::closeCode() const
{
    return isDone() ? m_closeCode : QWebSocketProtocol::CloseCodeGoingAway;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 66, as _ZNK15QWebSocketFrame11closeReasonEv
inline QString QWebSocketFrame::closeReason() const
{
    return isDone() ? m_closeReason : tr("Waiting for more data from socket.");
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

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 90, as _ZNK15QWebSocketFrame11isDataFrameEv
inline bool QWebSocketFrame::isDataFrame() const
{
    return !isControlFrame();
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 98, as _ZNK15QWebSocketFrame19isContinuationFrameEv
inline bool QWebSocketFrame::isContinuationFrame() const
{
    return isDataFrame() && (m_opCode == QWebSocketProtocol::OpCodeContinue);
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 106, as _ZNK15QWebSocketFrame7hasMaskEv
inline bool QWebSocketFrame::hasMask() const
{
    return m_mask != 0;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 114, as _ZNK15QWebSocketFrame4maskEv
inline quint32 QWebSocketFrame::mask() const
{
    return m_mask;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 122, as _ZNK15QWebSocketFrame6opCodeEv
inline QWebSocketProtocol::OpCode QWebSocketFrame::opCode() const
{
    return m_opCode;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 130, as _ZNK15QWebSocketFrame7payloadEv
inline QByteArray QWebSocketFrame::payload() const
{
    return m_payload;
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

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 159, as _ZNK15QWebSocketFrame7isValidEv
inline bool QWebSocketFrame::isValid() const
{
    return isDone() && m_isValid;
}

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 167, as _ZNK15QWebSocketFrame6isDoneEv
inline bool QWebSocketFrame::isDone() const
{
    return m_processingState == PS_DISPATCH_RESULT;
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

//  from ../qtwebsockets/src/websockets/qwebsocketframe.cpp, line 370, as _ZN15QWebSocketFrame8setErrorEN18QWebSocketProtocol9CloseCodeERK7QString
inline void QWebSocketFrame::setError(QWebSocketProtocol::CloseCode code, const QString &closeReason)
{
    clear();
    m_closeCode = code;
    m_closeReason = closeReason;
    m_isValid = false;
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
//  -----------------------------------------------------------------------

//  QString QWebSocketFrame::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QWebSocketFrame2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QWebSocketFrame::tr(sourceText, disambiguation, n));
}

//  QWebSocketFrame::QWebSocketFrame()
extern "C" Q_DECL_EXPORT
QWebSocketFrame *ritual_ZN15QWebSocketFrameC1Ev() {
  return new QWebSocketFrame();
}

//  void QWebSocketFrame::setMaxAllowedFrameSize(quint64 maxAllowedFrameSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebSocketFrame22setMaxAllowedFrameSizeEy(
    QWebSocketFrame *self,
    quint64 maxAllowedFrameSize) {
  self->setMaxAllowedFrameSize(maxAllowedFrameSize);
}

//  quint64 QWebSocketFrame::maxAllowedFrameSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK15QWebSocketFrame19maxAllowedFrameSizeEv(
    const QWebSocketFrame *self) {
  return self->maxAllowedFrameSize();
}

//  quint64 QWebSocketFrame::maxFrameSize()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QWebSocketFrame12maxFrameSizeEv() {
  return QWebSocketFrame::maxFrameSize();
}

//  QWebSocketProtocol::CloseCode QWebSocketFrame::closeCode() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::CloseCode ritual_ZNK15QWebSocketFrame9closeCodeEv(
    const QWebSocketFrame *self) {
  return self->closeCode();
}

//  QString QWebSocketFrame::closeReason() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QWebSocketFrame11closeReasonEv(
    const QWebSocketFrame *self) {
  return new QString(self->closeReason());
}

//  bool QWebSocketFrame::isFinalFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebSocketFrame12isFinalFrameEv(
    const QWebSocketFrame *self) {
  return self->isFinalFrame();
}

//  bool QWebSocketFrame::isControlFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebSocketFrame14isControlFrameEv(
    const QWebSocketFrame *self) {
  return self->isControlFrame();
}

//  bool QWebSocketFrame::isDataFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebSocketFrame11isDataFrameEv(
    const QWebSocketFrame *self) {
  return self->isDataFrame();
}

//  bool QWebSocketFrame::isContinuationFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebSocketFrame19isContinuationFrameEv(
    const QWebSocketFrame *self) {
  return self->isContinuationFrame();
}

//  bool QWebSocketFrame::hasMask() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebSocketFrame7hasMaskEv(const QWebSocketFrame *self) {
  return self->hasMask();
}

//  quint32 QWebSocketFrame::mask() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK15QWebSocketFrame4maskEv(const QWebSocketFrame *self) {
  return self->mask();
}

//  bool QWebSocketFrame::rsv1() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebSocketFrame4rsv1Ev(const QWebSocketFrame *self) {
  return self->rsv1();
}

//  bool QWebSocketFrame::rsv2() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebSocketFrame4rsv2Ev(const QWebSocketFrame *self) {
  return self->rsv2();
}

//  bool QWebSocketFrame::rsv3() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebSocketFrame4rsv3Ev(const QWebSocketFrame *self) {
  return self->rsv3();
}

//  QWebSocketProtocol::OpCode QWebSocketFrame::opCode() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::OpCode ritual_ZNK15QWebSocketFrame6opCodeEv(
    const QWebSocketFrame *self) {
  return self->opCode();
}

//  QByteArray QWebSocketFrame::payload() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QWebSocketFrame7payloadEv(
    const QWebSocketFrame *self) {
  return new QByteArray(self->payload());
}

//  void QWebSocketFrame::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebSocketFrame5clearEv(QWebSocketFrame *self) {
  self->clear();
}

//  bool QWebSocketFrame::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebSocketFrame7isValidEv(const QWebSocketFrame *self) {
  return self->isValid();
}

//  bool QWebSocketFrame::isDone() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWebSocketFrame6isDoneEv(const QWebSocketFrame *self) {
  return self->isDone();
}

//  void QWebSocketFrame::readFrame(QIODevice *pIoDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebSocketFrame9readFrameEP9QIODevice(
    QWebSocketFrame *self,
    QIODevice *pIoDevice) {
  self->readFrame(pIoDevice);
}

//  ProcessingState QWebSocketFrame::readFrameHeader(QIODevice *pIoDevice)
extern "C" Q_DECL_EXPORT
QWebSocketFrame::ProcessingState ritual_ZN15QWebSocketFrame15readFrameHeaderEP9QIODevice(
    QWebSocketFrame *self,
    QIODevice *pIoDevice) {
  return self->readFrameHeader(pIoDevice);
}

//  ProcessingState QWebSocketFrame::readFramePayloadLength(QIODevice
//      *pIoDevice)
extern "C" Q_DECL_EXPORT
QWebSocketFrame::ProcessingState ritual_ZN15QWebSocketFrame22readFramePayloadLengthEP9QIODevice(
    QWebSocketFrame *self,
    QIODevice *pIoDevice) {
  return self->readFramePayloadLength(pIoDevice);
}

//  ProcessingState QWebSocketFrame::readFrameMask(QIODevice *pIoDevice)
extern "C" Q_DECL_EXPORT
QWebSocketFrame::ProcessingState ritual_ZN15QWebSocketFrame13readFrameMaskEP9QIODevice(
    QWebSocketFrame *self,
    QIODevice *pIoDevice) {
  return self->readFrameMask(pIoDevice);
}

//  ProcessingState QWebSocketFrame::readFramePayload(QIODevice *pIoDevice)
extern "C" Q_DECL_EXPORT
QWebSocketFrame::ProcessingState ritual_ZN15QWebSocketFrame16readFramePayloadEP9QIODevice(
    QWebSocketFrame *self,
    QIODevice *pIoDevice) {
  return self->readFramePayload(pIoDevice);
}

//  void QWebSocketFrame::setError(QWebSocketProtocol::CloseCode code, const
//      QString &closeReason)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebSocketFrame8setErrorEN18QWebSocketProtocol9CloseCodeERK7QString(
    QWebSocketFrame *self,
    QWebSocketProtocol::CloseCode code,
    const QString *closeReason) {
  self->setError(code, *closeReason);
}

//  bool QWebSocketFrame::checkValidity()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QWebSocketFrame13checkValidityEv(QWebSocketFrame *self) {
  return self->checkValidity();
}

//  QWebSocketFrame::~QWebSocketFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebSocketFrameD1Ev(QWebSocketFrame *self) {
  delete self;
}
