//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttp2connection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttp2connection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qbytedatabuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/http2frames_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHttp2Stream that Python can take functions over in. Every QHttp2Stream
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttp2StreamCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttp2StreamCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttp2StreamCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttp2StreamCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttp2StreamCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttp2StreamCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttp2StreamCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHttp2Stream : public QHttp2Stream {
public:
  using QHttp2Stream::QHttp2Stream;
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
      CuteQHttp2StreamCall0 call = reinterpret_cast<CuteQHttp2StreamCall0>(taken[0]);
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
      CuteQHttp2StreamCall1 call = reinterpret_cast<CuteQHttp2StreamCall1>(taken[1]);
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
      CuteQHttp2StreamCall2 call = reinterpret_cast<CuteQHttp2StreamCall2>(taken[2]);
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
      CuteQHttp2StreamCall3 call = reinterpret_cast<CuteQHttp2StreamCall3>(taken[3]);
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
      CuteQHttp2StreamCall4 call = reinterpret_cast<CuteQHttp2StreamCall4>(taken[4]);
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
      CuteQHttp2StreamCall5 call = reinterpret_cast<CuteQHttp2StreamCall5>(taken[5]);
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
      CuteQHttp2StreamCall6 call = reinterpret_cast<CuteQHttp2StreamCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHttp2Stream::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QHttp2Stream10metaObjectEv(
    const QHttp2Stream *self) {
  return self->metaObject();
}

//  QString QHttp2Stream::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QHttp2Stream2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHttp2Stream::tr(s, c, n));
}

//  QHttp2Stream::~QHttp2Stream()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2StreamD1Ev(QHttp2Stream *self) {
  delete self;
}

//  quint32 QHttp2Stream::streamID() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK12QHttp2Stream8streamIDEv(const QHttp2Stream *self) {
  return self->streamID();
}

//  bool QHttp2Stream::isUploadBlocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHttp2Stream15isUploadBlockedEv(const QHttp2Stream *self) {
  return self->isUploadBlocked();
}

//  bool QHttp2Stream::isUploadingDATA() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHttp2Stream15isUploadingDATAEv(const QHttp2Stream *self) {
  return self->isUploadingDATA();
}

//  State QHttp2Stream::state() const
extern "C" Q_DECL_EXPORT
QHttp2Stream::State ritual_ZNK12QHttp2Stream5stateEv(
    const QHttp2Stream *self) {
  return self->state();
}

//  bool QHttp2Stream::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHttp2Stream8isActiveEv(const QHttp2Stream *self) {
  return self->isActive();
}

//  bool QHttp2Stream::isPromisedStream() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHttp2Stream16isPromisedStreamEv(const QHttp2Stream *self) {
  return self->isPromisedStream();
}

//  bool QHttp2Stream::wasReset() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHttp2Stream8wasResetEv(const QHttp2Stream *self) {
  return self->wasReset();
}

//  bool QHttp2Stream::wasResetbyPeer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QHttp2Stream14wasResetbyPeerEv(const QHttp2Stream *self) {
  return self->wasResetbyPeer();
}

//  quint32 QHttp2Stream::RST_STREAMCodeReceived() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK12QHttp2Stream22RST_STREAMCodeReceivedEv(
    const QHttp2Stream *self) {
  return self->RST_STREAMCodeReceived();
}

//  quint32 QHttp2Stream::RST_STREAMCodeSent() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK12QHttp2Stream18RST_STREAMCodeSentEv(
    const QHttp2Stream *self) {
  return self->RST_STREAMCodeSent();
}

//  QByteDataBuffer QHttp2Stream::downloadBuffer() const
extern "C" Q_DECL_EXPORT
QByteDataBuffer *ritual_ZNK12QHttp2Stream14downloadBufferEv(
    const QHttp2Stream *self) {
  return new QByteDataBuffer(self->downloadBuffer());
}

//  QByteDataBuffer QHttp2Stream::takeDownloadBuffer()
extern "C" Q_DECL_EXPORT
QByteDataBuffer *ritual_ZN12QHttp2Stream18takeDownloadBufferEv(
    QHttp2Stream *self) {
  return new QByteDataBuffer(self->takeDownloadBuffer());
}

//  void QHttp2Stream::clearDownloadBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream19clearDownloadBufferEv(QHttp2Stream *self) {
  self->clearDownloadBuffer();
}

//  Configuration QHttp2Stream::configuration() const
extern "C" Q_DECL_EXPORT
QHttp2Stream::Configuration *ritual_ZNK12QHttp2Stream13configurationEv(
    const QHttp2Stream *self) {
  return new QHttp2Stream::Configuration(self->configuration());
}

//  bool QHttp2Stream::sendRST_STREAM(Http2::Http2Error errorCode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttp2Stream14sendRST_STREAMEN5Http210Http2ErrorE(
    QHttp2Stream *self,
    Http2::Http2Error errorCode) {
  return self->sendRST_STREAM(errorCode);
}

//  bool QHttp2Stream::sendDATA(const QByteArray &payload, bool endStream)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttp2Stream8sendDATAERK10QByteArrayb(
    QHttp2Stream *self,
    const QByteArray *payload,
    bool endStream) {
  return self->sendDATA(*payload, endStream);
}

//  bool QHttp2Stream::sendDATA(QIODevice *device, bool endStream)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttp2Stream8sendDATAEP9QIODeviceb(
    QHttp2Stream *self,
    QIODevice *device,
    bool endStream) {
  return self->sendDATA(device, endStream);
}

//  bool QHttp2Stream::sendDATA(QNonContiguousByteDevice *device, bool
//      endStream)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QHttp2Stream8sendDATAEP24QNonContiguousByteDeviceb(
    QHttp2Stream *self,
    QNonContiguousByteDevice *device,
    bool endStream) {
  return self->sendDATA(device, endStream);
}

//  void QHttp2Stream::sendWINDOW_UPDATE(quint32 delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream17sendWINDOW_UPDATEEj(
    QHttp2Stream *self,
    quint32 delta) {
  self->sendWINDOW_UPDATE(delta);
}

//  void QHttp2Stream::maybeResumeUpload()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream17maybeResumeUploadEv(QHttp2Stream *self) {
  self->maybeResumeUpload();
}

//  void QHttp2Stream::uploadDeviceReadChannelFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream31uploadDeviceReadChannelFinishedEv(
    QHttp2Stream *self) {
  self->uploadDeviceReadChannelFinished();
}

//  void QHttp2Stream::uploadDeviceDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream21uploadDeviceDestroyedEv(QHttp2Stream *self) {
  self->uploadDeviceDestroyed();
}

//  QHttp2Stream::QHttp2Stream(QHttp2Connection *connection, quint32
//      streamID, Configuration configuration)
extern "C" Q_DECL_EXPORT
QHttp2Stream *ritual_ZN12QHttp2StreamC1EP16QHttp2ConnectionjNS_13ConfigurationE(
    QHttp2Connection *connection,
    quint32 streamID,
    const QHttp2Stream::Configuration *configuration) {
  return new CuteQHttp2Stream(connection, streamID, *configuration);
}

//  QHttp2Connection *QHttp2Stream::getConnection() const
extern "C" Q_DECL_EXPORT
QHttp2Connection *ritual_ZNK12QHttp2Stream13getConnectionEv(
    const QHttp2Stream *self) {
  return self->getConnection();
}

//  void QHttp2Stream::setState(State newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream8setStateENS_5StateE(
    QHttp2Stream *self,
    QHttp2Stream::State newState) {
  self->setState(newState);
}

//  void QHttp2Stream::transitionState(StateTransition transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream15transitionStateENS_15StateTransitionE(
    QHttp2Stream *self,
    QHttp2Stream::StateTransition transition) {
  self->transitionState(transition);
}

//  void QHttp2Stream::internalSendDATA()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream16internalSendDATAEv(QHttp2Stream *self) {
  self->internalSendDATA();
}

//  void QHttp2Stream::finishSendDATA()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream14finishSendDATAEv(QHttp2Stream *self) {
  self->finishSendDATA();
}

//  void QHttp2Stream::handleDATA(const Http2::Frame &inboundFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream10handleDATAERKN5Http25FrameE(
    QHttp2Stream *self,
    const Http2::Frame *inboundFrame) {
  self->handleDATA(*inboundFrame);
}

//  void QHttp2Stream::handleRST_STREAM(const Http2::Frame &inboundFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream16handleRST_STREAMERKN5Http25FrameE(
    QHttp2Stream *self,
    const Http2::Frame *inboundFrame) {
  self->handleRST_STREAM(*inboundFrame);
}

//  void QHttp2Stream::handleWINDOW_UPDATE(const Http2::Frame &inboundFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream19handleWINDOW_UPDATEERKN5Http25FrameE(
    QHttp2Stream *self,
    const Http2::Frame *inboundFrame) {
  self->handleWINDOW_UPDATE(*inboundFrame);
}

//  void QHttp2Stream::finishWithError(Http2::Http2Error errorCode, const
//      QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream15finishWithErrorEN5Http210Http2ErrorERK7QString(
    QHttp2Stream *self,
    Http2::Http2Error errorCode,
    const QString *message) {
  self->finishWithError(errorCode, *message);
}

//  void QHttp2Stream::finishWithError(Http2::Http2Error errorCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream15finishWithErrorEN5Http210Http2ErrorE(
    QHttp2Stream *self,
    Http2::Http2Error errorCode) {
  self->finishWithError(errorCode);
}

//  void QHttp2Stream::streamError(Http2::Http2Error errorCode, const QString
//      &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QHttp2Stream11streamErrorEN5Http210Http2ErrorERK7QString(
    QHttp2Stream *self,
    Http2::Http2Error errorCode,
    const QString *message) {
  self->streamError(errorCode, *message);
}

//  a Python function taken by a CuteQHttp2Stream, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttp2Stream(
    QHttp2Stream *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttp2Stream *>(self)->take(key, call);
}
