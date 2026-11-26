//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <utility>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 136, as _ZN37QNonContiguousByteDeviceByteArrayImpl18advanceReadPointerEx
inline bool QNonContiguousByteDeviceByteArrayImpl::advanceReadPointer(qint64 amount)
{
    currentPosition += amount;
    emit readProgress(currentPosition, size());
    return true;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 143, as _ZNK37QNonContiguousByteDeviceByteArrayImpl5atEndEv
inline bool QNonContiguousByteDeviceByteArrayImpl::atEnd() const
{
    return currentPosition >= size();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 148, as _ZN37QNonContiguousByteDeviceByteArrayImpl5resetEv
inline bool QNonContiguousByteDeviceByteArrayImpl::reset()
{
    currentPosition = 0;
    return true;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 154, as _ZNK37QNonContiguousByteDeviceByteArrayImpl4sizeEv
inline qint64 QNonContiguousByteDeviceByteArrayImpl::size() const
{
    return view.size();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 159, as _ZNK37QNonContiguousByteDeviceByteArrayImpl3posEv
inline qint64 QNonContiguousByteDeviceByteArrayImpl::pos() const
{
    return currentPosition;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 117, as _ZN37QNonContiguousByteDeviceByteArrayImplD1Ev
inline QNonContiguousByteDeviceByteArrayImpl::~QNonContiguousByteDeviceByteArrayImpl()
{
}
//  -----------------------------------------------------------------------

//  A QNonContiguousByteDeviceByteArrayImpl that Python can take functions over in. Every QNonContiguousByteDeviceByteArrayImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNonContiguousByteDeviceByteArrayImplCall0)(const void *, qint64, int *);
typedef bool (*CuteQNonContiguousByteDeviceByteArrayImplCall1)(const void *, int *);
typedef bool (*CuteQNonContiguousByteDeviceByteArrayImplCall2)(const void *, int *);
typedef qint64 (*CuteQNonContiguousByteDeviceByteArrayImplCall3)(const void *, int *);
typedef qint64 (*CuteQNonContiguousByteDeviceByteArrayImplCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNonContiguousByteDeviceByteArrayImplCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNonContiguousByteDeviceByteArrayImplCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceByteArrayImplCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceByteArrayImplCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceByteArrayImplCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceByteArrayImplCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceByteArrayImplCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNonContiguousByteDeviceByteArrayImpl : public QNonContiguousByteDeviceByteArrayImpl {
public:
  using QNonContiguousByteDeviceByteArrayImpl::QNonContiguousByteDeviceByteArrayImpl;
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
    if (!std::strcmp(key, "_ZN24QNonContiguousByteDevice5resetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QNonContiguousByteDevice4sizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QNonContiguousByteDevice3posEv")) {
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

  //  bool QNonContiguousByteDeviceByteArrayImpl::advanceReadPointer(qint64
  //      amount)
  bool advanceReadPointer(qint64 amount) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceByteArrayImplCall0 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall0>(taken[0]);
      bool given = call(this, amount, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceByteArrayImpl::advanceReadPointer(amount);
  }

  //  bool QNonContiguousByteDeviceByteArrayImpl::atEnd() const
  bool atEnd() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceByteArrayImplCall1 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceByteArrayImpl::atEnd();
  }

  //  bool QNonContiguousByteDeviceByteArrayImpl::reset()
  bool reset() override {
    if (taken[2]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceByteArrayImplCall2 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceByteArrayImpl::reset();
  }

  //  qint64 QNonContiguousByteDeviceByteArrayImpl::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceByteArrayImplCall3 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceByteArrayImpl::size();
  }

  //  qint64 QNonContiguousByteDeviceByteArrayImpl::pos() const
  qint64 pos() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceByteArrayImplCall4 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceByteArrayImpl::pos();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceByteArrayImplCall5 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall5>(taken[5]);
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
      CuteQNonContiguousByteDeviceByteArrayImplCall6 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall6>(taken[6]);
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
      CuteQNonContiguousByteDeviceByteArrayImplCall7 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall7>(taken[7]);
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
      CuteQNonContiguousByteDeviceByteArrayImplCall8 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall8>(taken[8]);
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
      CuteQNonContiguousByteDeviceByteArrayImplCall9 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall9>(taken[9]);
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
      CuteQNonContiguousByteDeviceByteArrayImplCall10 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall10>(taken[10]);
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
      CuteQNonContiguousByteDeviceByteArrayImplCall11 call = reinterpret_cast<CuteQNonContiguousByteDeviceByteArrayImplCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNonContiguousByteDeviceByteArrayImpl::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK37QNonContiguousByteDeviceByteArrayImpl10metaObjectEv(
    const QNonContiguousByteDeviceByteArrayImpl *self) {
  return self->metaObject();
}

//  void *QNonContiguousByteDeviceByteArrayImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN37QNonContiguousByteDeviceByteArrayImpl11qt_metacastEPKc(
    QNonContiguousByteDeviceByteArrayImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNonContiguousByteDeviceByteArrayImpl::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN37QNonContiguousByteDeviceByteArrayImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QNonContiguousByteDeviceByteArrayImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QNonContiguousByteDeviceByteArrayImpl::~QNonContiguousByteDeviceByteArray
//      Impl()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QNonContiguousByteDeviceByteArrayImplD1Ev(
    QNonContiguousByteDeviceByteArrayImpl *self) {
  delete self;
}

//  const char *QNonContiguousByteDeviceByteArrayImpl::readPointer(qint64
//      maximumLength, qint64 &len)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN37QNonContiguousByteDeviceByteArrayImpl11readPointerExRx(
    QNonContiguousByteDeviceByteArrayImpl *self,
    qint64 maximumLength,
    qint64 *len) {
  return self->readPointer(maximumLength, *len);
}

//  bool QNonContiguousByteDeviceByteArrayImpl::advanceReadPointer(qint64
//      amount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN37QNonContiguousByteDeviceByteArrayImpl18advanceReadPointerEx(
    QNonContiguousByteDeviceByteArrayImpl *self,
    qint64 amount) {
  return self->advanceReadPointer(amount);
}

//  bool QNonContiguousByteDeviceByteArrayImpl::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK37QNonContiguousByteDeviceByteArrayImpl5atEndEv(
    const QNonContiguousByteDeviceByteArrayImpl *self) {
  return self->atEnd();
}

//  bool QNonContiguousByteDeviceByteArrayImpl::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN37QNonContiguousByteDeviceByteArrayImpl5resetEv(
    QNonContiguousByteDeviceByteArrayImpl *self) {
  return self->reset();
}

//  qint64 QNonContiguousByteDeviceByteArrayImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK37QNonContiguousByteDeviceByteArrayImpl4sizeEv(
    const QNonContiguousByteDeviceByteArrayImpl *self) {
  return self->size();
}

//  qint64 QNonContiguousByteDeviceByteArrayImpl::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK37QNonContiguousByteDeviceByteArrayImpl3posEv(
    const QNonContiguousByteDeviceByteArrayImpl *self) {
  return self->pos();
}

//  a Python function taken by a CuteQNonContiguousByteDeviceByteArrayImpl,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNonContiguousByteDeviceByteArrayImpl(
    QNonContiguousByteDeviceByteArrayImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNonContiguousByteDeviceByteArrayImpl *>(self)->take(key, call);
}

//  bool QNonContiguousByteDeviceByteArrayImpl::advanceReadPointer(qint64
//      amount)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN37QNonContiguousByteDeviceByteArrayImpl18advanceReadPointerEx(
    QNonContiguousByteDeviceByteArrayImpl *self,
    qint64 amount) {
  return self->QNonContiguousByteDeviceByteArrayImpl::advanceReadPointer(
      amount);
}

//  bool QNonContiguousByteDeviceByteArrayImpl::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK37QNonContiguousByteDeviceByteArrayImpl5atEndEv(
    const QNonContiguousByteDeviceByteArrayImpl *self) {
  return self->QNonContiguousByteDeviceByteArrayImpl::atEnd();
}

//  bool QNonContiguousByteDeviceByteArrayImpl::reset()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN37QNonContiguousByteDeviceByteArrayImpl5resetEv(
    QNonContiguousByteDeviceByteArrayImpl *self) {
  return self->QNonContiguousByteDeviceByteArrayImpl::reset();
}

//  qint64 QNonContiguousByteDeviceByteArrayImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK37QNonContiguousByteDeviceByteArrayImpl4sizeEv(
    const QNonContiguousByteDeviceByteArrayImpl *self) {
  return self->QNonContiguousByteDeviceByteArrayImpl::size();
}

//  qint64 QNonContiguousByteDeviceByteArrayImpl::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK37QNonContiguousByteDeviceByteArrayImpl3posEv(
    const QNonContiguousByteDeviceByteArrayImpl *self) {
  return self->QNonContiguousByteDeviceByteArrayImpl::pos();
}
