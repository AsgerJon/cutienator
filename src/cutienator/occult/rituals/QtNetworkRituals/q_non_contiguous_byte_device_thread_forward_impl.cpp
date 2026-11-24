//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpthreaddelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpthreaddelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QNonContiguousByteDeviceThreadForwardImpl that Python can take functions over in. Every QNonContiguousByteDeviceThreadForwardImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(http)
typedef qint64 (*CuteQNonContiguousByteDeviceThreadForwardImplCall0)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef bool (*CuteQNonContiguousByteDeviceThreadForwardImplCall1)(const void *, qint64, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef bool (*CuteQNonContiguousByteDeviceThreadForwardImplCall2)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef bool (*CuteQNonContiguousByteDeviceThreadForwardImplCall3)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQNonContiguousByteDeviceThreadForwardImplCall4)(const void *, int *);
#endif  // QT_CONFIG(http)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNonContiguousByteDeviceThreadForwardImplCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNonContiguousByteDeviceThreadForwardImplCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceThreadForwardImplCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceThreadForwardImplCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceThreadForwardImplCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceThreadForwardImplCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceThreadForwardImplCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNonContiguousByteDeviceThreadForwardImpl : public QNonContiguousByteDeviceThreadForwardImpl {
public:
  using QNonContiguousByteDeviceThreadForwardImpl::QNonContiguousByteDeviceThreadForwardImpl;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK24QNonContiguousByteDevice3posEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN24QNonContiguousByteDevice18advanceReadPointerEx")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK24QNonContiguousByteDevice5atEndEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN24QNonContiguousByteDevice5resetEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK24QNonContiguousByteDevice4sizeEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(http)
  //  qint64 QNonContiguousByteDeviceThreadForwardImpl::pos() const
  qint64 pos() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall0 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceThreadForwardImpl::pos();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  bool
  //      QNonContiguousByteDeviceThreadForwardImpl::advanceReadPointer(qin
  //      t64 a)
  bool advanceReadPointer(qint64 a) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall1 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall1>(taken[1]);
      bool given = call(this, a, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceThreadForwardImpl::advanceReadPointer(a);
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  bool QNonContiguousByteDeviceThreadForwardImpl::atEnd() const
  bool atEnd() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall2 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceThreadForwardImpl::atEnd();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  bool QNonContiguousByteDeviceThreadForwardImpl::reset()
  bool reset() override {
    if (taken[3]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall3 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceThreadForwardImpl::reset();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QNonContiguousByteDeviceThreadForwardImpl::size() const
  qint64 size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall4 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceThreadForwardImpl::size();
  }
#endif  // QT_CONFIG(http)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall5 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall6 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall7 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall8 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall9 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall10 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceThreadForwardImplCall11 call = reinterpret_cast<CuteQNonContiguousByteDeviceThreadForwardImplCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QNonContiguousByteDeviceThreadForwardImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK41QNonContiguousByteDeviceThreadForwardImpl10metaObjectEv(
    const QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->metaObject();
}

//  QNonContiguousByteDeviceThreadForwardImpl::~QNonContiguousByteDeviceThrea
//      dForwardImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN41QNonContiguousByteDeviceThreadForwardImplD1Ev(
    QNonContiguousByteDeviceThreadForwardImpl *self) {
  delete self;
}

//  qint64 QNonContiguousByteDeviceThreadForwardImpl::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK41QNonContiguousByteDeviceThreadForwardImpl3posEv(
    const QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->pos();
}

//  const char *QNonContiguousByteDeviceThreadForwardImpl::readPointer(qint64
//      maximumLength, qint64 &len)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl11readPointerExRx(
    QNonContiguousByteDeviceThreadForwardImpl *self,
    qint64 maximumLength,
    qint64 *len) {
  return self->readPointer(maximumLength, *len);
}

//  bool QNonContiguousByteDeviceThreadForwardImpl::advanceReadPointer(qint64
//      a)
extern "C" Q_DECL_EXPORT
bool ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl18advanceReadPointerEx(
    QNonContiguousByteDeviceThreadForwardImpl *self,
    qint64 a) {
  return self->advanceReadPointer(a);
}

//  bool QNonContiguousByteDeviceThreadForwardImpl::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK41QNonContiguousByteDeviceThreadForwardImpl5atEndEv(
    const QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->atEnd();
}

//  bool QNonContiguousByteDeviceThreadForwardImpl::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl5resetEv(
    QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->reset();
}

//  qint64 QNonContiguousByteDeviceThreadForwardImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK41QNonContiguousByteDeviceThreadForwardImpl4sizeEv(
    const QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->size();
}

//  void QNonContiguousByteDeviceThreadForwardImpl::haveDataSlot(qint64 pos,
//      const QByteArray &dataArray, bool dataAtEnd, qint64 dataSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl12haveDataSlotExRK10QByteArraybx(
    QNonContiguousByteDeviceThreadForwardImpl *self,
    qint64 pos,
    const QByteArray *dataArray,
    bool dataAtEnd,
    qint64 dataSize) {
  self->haveDataSlot(pos, *dataArray, dataAtEnd, dataSize);
}

//  a Python function taken by a
//      CuteQNonContiguousByteDeviceThreadForwardImpl, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNonContiguousByteDeviceThreadForwardImpl(
    QNonContiguousByteDeviceThreadForwardImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNonContiguousByteDeviceThreadForwardImpl *>(self)->take(key, call);
}

//  qint64 QNonContiguousByteDeviceThreadForwardImpl::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK41QNonContiguousByteDeviceThreadForwardImpl3posEv(
    const QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->QNonContiguousByteDeviceThreadForwardImpl::pos();
}

//  bool QNonContiguousByteDeviceThreadForwardImpl::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK41QNonContiguousByteDeviceThreadForwardImpl5atEndEv(
    const QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->QNonContiguousByteDeviceThreadForwardImpl::atEnd();
}

//  qint64 QNonContiguousByteDeviceThreadForwardImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK41QNonContiguousByteDeviceThreadForwardImpl4sizeEv(
    const QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->QNonContiguousByteDeviceThreadForwardImpl::size();
}

#endif  // QT_CONFIG(http)
