//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketdataprocessor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketdataprocessor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  a Python function taken by a CuteQWebSocketDataProcessor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebSocketDataProcessor(
    QWebSocketDataProcessor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebSocketDataProcessor *>(self)->take(key, call);
}
