//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QNonContiguousByteDevice that Python can take functions over in. Every QNonContiguousByteDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNonContiguousByteDeviceCall0)(const void *, qint64, int *);
typedef bool (*CuteQNonContiguousByteDeviceCall1)(const void *, int *);
typedef qint64 (*CuteQNonContiguousByteDeviceCall2)(const void *, int *);
typedef bool (*CuteQNonContiguousByteDeviceCall3)(const void *, int *);
typedef qint64 (*CuteQNonContiguousByteDeviceCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNonContiguousByteDeviceCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNonContiguousByteDeviceCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNonContiguousByteDevice : public QNonContiguousByteDevice {
public:
  using QNonContiguousByteDevice::QNonContiguousByteDevice;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QNonContiguousByteDevice18advanceReadPointerEx")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QNonContiguousByteDevice5atEndEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QNonContiguousByteDevice3posEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QNonContiguousByteDevice5resetEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QNonContiguousByteDevice4sizeEv")) {
      taken[4] = call;
      return true;
    }
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

  //  bool QNonContiguousByteDevice::advanceReadPointer(qint64 amount)
  bool advanceReadPointer(qint64 amount) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceCall0 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall0>(taken[0]);
      bool given = call(this, amount, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QNonContiguousByteDevice::atEnd() const
  bool atEnd() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceCall1 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qint64 QNonContiguousByteDevice::pos() const
  qint64 pos() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceCall2 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDevice::pos();
  }

  //  bool QNonContiguousByteDevice::reset()
  bool reset() override {
    if (taken[3]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceCall3 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qint64 QNonContiguousByteDevice::size() const
  qint64 size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceCall4 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceCall5 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall5>(taken[5]);
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
      CuteQNonContiguousByteDeviceCall6 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall6>(taken[6]);
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
      CuteQNonContiguousByteDeviceCall7 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall7>(taken[7]);
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
      CuteQNonContiguousByteDeviceCall8 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall8>(taken[8]);
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
      CuteQNonContiguousByteDeviceCall9 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall9>(taken[9]);
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
      CuteQNonContiguousByteDeviceCall10 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall10>(taken[10]);
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
      CuteQNonContiguousByteDeviceCall11 call = reinterpret_cast<CuteQNonContiguousByteDeviceCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNonContiguousByteDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QNonContiguousByteDevice10metaObjectEv(
    const QNonContiguousByteDevice *self) {
  return self->metaObject();
}

//  void *QNonContiguousByteDevice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QNonContiguousByteDevice11qt_metacastEPKc(
    QNonContiguousByteDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNonContiguousByteDevice::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QNonContiguousByteDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    QNonContiguousByteDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNonContiguousByteDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QNonContiguousByteDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNonContiguousByteDevice::tr(s, c, n));
}

//  const char *QNonContiguousByteDevice::readPointer(qint64 maximumLength,
//      qint64 &len)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN24QNonContiguousByteDevice11readPointerExRx(
    QNonContiguousByteDevice *self,
    qint64 maximumLength,
    qint64 *len) {
  return self->readPointer(maximumLength, *len);
}

//  bool QNonContiguousByteDevice::advanceReadPointer(qint64 amount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QNonContiguousByteDevice18advanceReadPointerEx(
    QNonContiguousByteDevice *self,
    qint64 amount) {
  return self->advanceReadPointer(amount);
}

//  bool QNonContiguousByteDevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QNonContiguousByteDevice5atEndEv(
    const QNonContiguousByteDevice *self) {
  return self->atEnd();
}

//  qint64 QNonContiguousByteDevice::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QNonContiguousByteDevice3posEv(
    const QNonContiguousByteDevice *self) {
  return self->pos();
}

//  bool QNonContiguousByteDevice::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QNonContiguousByteDevice5resetEv(
    QNonContiguousByteDevice *self) {
  return self->reset();
}

//  qint64 QNonContiguousByteDevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QNonContiguousByteDevice4sizeEv(
    const QNonContiguousByteDevice *self) {
  return self->size();
}

//  QNonContiguousByteDevice::~QNonContiguousByteDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNonContiguousByteDeviceD1Ev(
    QNonContiguousByteDevice *self) {
  delete self;
}

//  void QNonContiguousByteDevice::readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNonContiguousByteDevice9readyReadEv(
    QNonContiguousByteDevice *self) {
  self->readyRead();
}

//  void QNonContiguousByteDevice::readProgress(qint64 current, qint64 total)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNonContiguousByteDevice12readProgressExx(
    QNonContiguousByteDevice *self,
    qint64 current,
    qint64 total) {
  self->readProgress(current, total);
}

//  a Python function taken by a CuteQNonContiguousByteDevice, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNonContiguousByteDevice(
    QNonContiguousByteDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNonContiguousByteDevice *>(self)->take(key, call);
}

//  qint64 QNonContiguousByteDevice::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK24QNonContiguousByteDevice3posEv(
    const QNonContiguousByteDevice *self) {
  return self->QNonContiguousByteDevice::pos();
}
