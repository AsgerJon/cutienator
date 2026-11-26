//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QNonContiguousByteDeviceRingBufferImpl' is pasted in, cut from what the
//  moc of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 2 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <memory>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
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

//  from QtCore__QNonContiguousByteDeviceRingBufferImpl.cpp, line 1, as moc:QNonContiguousByteDeviceRingBufferImpl
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN38QNonContiguousByteDeviceRingBufferImplE_t {};
} // unnamed namespace

template <> constexpr inline auto QNonContiguousByteDeviceRingBufferImpl::qt_create_metaobjectdata<qt_meta_tag_ZN38QNonContiguousByteDeviceRingBufferImplE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QNonContiguousByteDeviceRingBufferImpl"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QNonContiguousByteDeviceRingBufferImpl, qt_meta_tag_ZN38QNonContiguousByteDeviceRingBufferImplE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QNonContiguousByteDeviceRingBufferImpl::staticMetaObject = { {
    QMetaObject::SuperData::link<QNonContiguousByteDevice::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN38QNonContiguousByteDeviceRingBufferImplE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN38QNonContiguousByteDeviceRingBufferImplE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN38QNonContiguousByteDeviceRingBufferImplE_t>.metaTypes,
    nullptr
} };

void QNonContiguousByteDeviceRingBufferImpl::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QNonContiguousByteDeviceRingBufferImpl *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QNonContiguousByteDeviceRingBufferImpl::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QNonContiguousByteDeviceRingBufferImpl::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN38QNonContiguousByteDeviceRingBufferImplE_t>.strings))
        return static_cast<void*>(this);
    return QNonContiguousByteDevice::qt_metacast(_clname);
}

int QNonContiguousByteDeviceRingBufferImpl::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QNonContiguousByteDevice::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 173, as _ZN38QNonContiguousByteDeviceRingBufferImpl11readPointerExRx
inline const char* QNonContiguousByteDeviceRingBufferImpl::readPointer(qint64 maximumLength, qint64 &len)
{
    if (atEnd()) {
        len = -1;
        return nullptr;
    }

    const char *returnValue = ringBuffer->readPointerAtPosition(currentPosition, len);

    if (maximumLength != -1)
        len = qMin(len, maximumLength);

    return returnValue;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 188, as _ZN38QNonContiguousByteDeviceRingBufferImpl18advanceReadPointerEx
inline bool QNonContiguousByteDeviceRingBufferImpl::advanceReadPointer(qint64 amount)
{
    currentPosition += amount;
    emit readProgress(currentPosition, size());
    return true;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 205, as _ZN38QNonContiguousByteDeviceRingBufferImpl5resetEv
inline bool QNonContiguousByteDeviceRingBufferImpl::reset()
{
    currentPosition = 0;
    return true;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 200, as _ZNK38QNonContiguousByteDeviceRingBufferImpl3posEv
inline qint64 QNonContiguousByteDeviceRingBufferImpl::pos() const
{
    return currentPosition;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 211, as _ZNK38QNonContiguousByteDeviceRingBufferImpl4sizeEv
inline qint64 QNonContiguousByteDeviceRingBufferImpl::size() const
{
    return ringBuffer->size();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 195, as _ZNK38QNonContiguousByteDeviceRingBufferImpl5atEndEv
inline bool QNonContiguousByteDeviceRingBufferImpl::atEnd() const
{
    return currentPosition >= size();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 164, as _ZN38QNonContiguousByteDeviceRingBufferImplC1ESt10shared_ptrI11QRingBufferE
inline QNonContiguousByteDeviceRingBufferImpl::QNonContiguousByteDeviceRingBufferImpl(std::shared_ptr<QRingBuffer> rb)
    : QNonContiguousByteDevice(), ringBuffer(std::move(rb))
{
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 169, as _ZN38QNonContiguousByteDeviceRingBufferImplD1Ev
inline QNonContiguousByteDeviceRingBufferImpl::~QNonContiguousByteDeviceRingBufferImpl()
{
}
//  -----------------------------------------------------------------------

//  A QNonContiguousByteDeviceRingBufferImpl that Python can take functions over in. Every QNonContiguousByteDeviceRingBufferImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNonContiguousByteDeviceRingBufferImplCall0)(const void *, qint64, int *);
typedef bool (*CuteQNonContiguousByteDeviceRingBufferImplCall1)(const void *, int *);
typedef bool (*CuteQNonContiguousByteDeviceRingBufferImplCall2)(const void *, int *);
typedef qint64 (*CuteQNonContiguousByteDeviceRingBufferImplCall3)(const void *, int *);
typedef qint64 (*CuteQNonContiguousByteDeviceRingBufferImplCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNonContiguousByteDeviceRingBufferImplCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNonContiguousByteDeviceRingBufferImplCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceRingBufferImplCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceRingBufferImplCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceRingBufferImplCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceRingBufferImplCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceRingBufferImplCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNonContiguousByteDeviceRingBufferImpl : public QNonContiguousByteDeviceRingBufferImpl {
public:
  using QNonContiguousByteDeviceRingBufferImpl::QNonContiguousByteDeviceRingBufferImpl;
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

  //  bool
  //      QNonContiguousByteDeviceRingBufferImpl::advanceReadPointer(qint64
  //      amount)
  bool advanceReadPointer(qint64 amount) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceRingBufferImplCall0 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall0>(taken[0]);
      bool given = call(this, amount, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceRingBufferImpl::advanceReadPointer(amount);
  }

  //  bool QNonContiguousByteDeviceRingBufferImpl::atEnd() const
  bool atEnd() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceRingBufferImplCall1 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceRingBufferImpl::atEnd();
  }

  //  bool QNonContiguousByteDeviceRingBufferImpl::reset()
  bool reset() override {
    if (taken[2]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceRingBufferImplCall2 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceRingBufferImpl::reset();
  }

  //  qint64 QNonContiguousByteDeviceRingBufferImpl::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceRingBufferImplCall3 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceRingBufferImpl::size();
  }

  //  qint64 QNonContiguousByteDeviceRingBufferImpl::pos() const
  qint64 pos() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceRingBufferImplCall4 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceRingBufferImpl::pos();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceRingBufferImplCall5 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall5>(taken[5]);
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
      CuteQNonContiguousByteDeviceRingBufferImplCall6 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall6>(taken[6]);
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
      CuteQNonContiguousByteDeviceRingBufferImplCall7 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall7>(taken[7]);
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
      CuteQNonContiguousByteDeviceRingBufferImplCall8 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall8>(taken[8]);
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
      CuteQNonContiguousByteDeviceRingBufferImplCall9 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall9>(taken[9]);
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
      CuteQNonContiguousByteDeviceRingBufferImplCall10 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall10>(taken[10]);
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
      CuteQNonContiguousByteDeviceRingBufferImplCall11 call = reinterpret_cast<CuteQNonContiguousByteDeviceRingBufferImplCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNonContiguousByteDeviceRingBufferImpl::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK38QNonContiguousByteDeviceRingBufferImpl10metaObjectEv(
    const QNonContiguousByteDeviceRingBufferImpl *self) {
  return self->metaObject();
}

//  void *QNonContiguousByteDeviceRingBufferImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN38QNonContiguousByteDeviceRingBufferImpl11qt_metacastEPKc(
    QNonContiguousByteDeviceRingBufferImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNonContiguousByteDeviceRingBufferImpl::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN38QNonContiguousByteDeviceRingBufferImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QNonContiguousByteDeviceRingBufferImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNonContiguousByteDeviceRingBufferImpl::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN38QNonContiguousByteDeviceRingBufferImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNonContiguousByteDeviceRingBufferImpl::tr(s, c, n));
}

//  QNonContiguousByteDeviceRingBufferImpl::QNonContiguousByteDeviceRingBuffe
//      rImpl(std::shared_ptr<QRingBuffer> rb)
extern "C" Q_DECL_EXPORT
QNonContiguousByteDeviceRingBufferImpl *ritual_ZN38QNonContiguousByteDeviceRingBufferImplC1ESt10shared_ptrI11QRingBufferE(
    const std::shared_ptr<QRingBuffer> *rb) {
  return new CuteQNonContiguousByteDeviceRingBufferImpl(*rb);
}

//  QNonContiguousByteDeviceRingBufferImpl::~QNonContiguousByteDeviceRingBuff
//      erImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QNonContiguousByteDeviceRingBufferImplD1Ev(
    QNonContiguousByteDeviceRingBufferImpl *self) {
  delete self;
}

//  const char *QNonContiguousByteDeviceRingBufferImpl::readPointer(qint64
//      maximumLength, qint64 &len)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN38QNonContiguousByteDeviceRingBufferImpl11readPointerExRx(
    QNonContiguousByteDeviceRingBufferImpl *self,
    qint64 maximumLength,
    qint64 *len) {
  return self->readPointer(maximumLength, *len);
}

//  bool QNonContiguousByteDeviceRingBufferImpl::advanceReadPointer(qint64
//      amount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN38QNonContiguousByteDeviceRingBufferImpl18advanceReadPointerEx(
    QNonContiguousByteDeviceRingBufferImpl *self,
    qint64 amount) {
  return self->advanceReadPointer(amount);
}

//  bool QNonContiguousByteDeviceRingBufferImpl::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK38QNonContiguousByteDeviceRingBufferImpl5atEndEv(
    const QNonContiguousByteDeviceRingBufferImpl *self) {
  return self->atEnd();
}

//  bool QNonContiguousByteDeviceRingBufferImpl::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN38QNonContiguousByteDeviceRingBufferImpl5resetEv(
    QNonContiguousByteDeviceRingBufferImpl *self) {
  return self->reset();
}

//  qint64 QNonContiguousByteDeviceRingBufferImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK38QNonContiguousByteDeviceRingBufferImpl4sizeEv(
    const QNonContiguousByteDeviceRingBufferImpl *self) {
  return self->size();
}

//  qint64 QNonContiguousByteDeviceRingBufferImpl::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK38QNonContiguousByteDeviceRingBufferImpl3posEv(
    const QNonContiguousByteDeviceRingBufferImpl *self) {
  return self->pos();
}

//  a Python function taken by a CuteQNonContiguousByteDeviceRingBufferImpl,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNonContiguousByteDeviceRingBufferImpl(
    QNonContiguousByteDeviceRingBufferImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNonContiguousByteDeviceRingBufferImpl *>(self)->take(key, call);
}

//  bool QNonContiguousByteDeviceRingBufferImpl::advanceReadPointer(qint64
//      amount)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN38QNonContiguousByteDeviceRingBufferImpl18advanceReadPointerEx(
    QNonContiguousByteDeviceRingBufferImpl *self,
    qint64 amount) {
  return self->QNonContiguousByteDeviceRingBufferImpl::advanceReadPointer(
      amount);
}

//  bool QNonContiguousByteDeviceRingBufferImpl::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK38QNonContiguousByteDeviceRingBufferImpl5atEndEv(
    const QNonContiguousByteDeviceRingBufferImpl *self) {
  return self->QNonContiguousByteDeviceRingBufferImpl::atEnd();
}

//  bool QNonContiguousByteDeviceRingBufferImpl::reset()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN38QNonContiguousByteDeviceRingBufferImpl5resetEv(
    QNonContiguousByteDeviceRingBufferImpl *self) {
  return self->QNonContiguousByteDeviceRingBufferImpl::reset();
}

//  qint64 QNonContiguousByteDeviceRingBufferImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK38QNonContiguousByteDeviceRingBufferImpl4sizeEv(
    const QNonContiguousByteDeviceRingBufferImpl *self) {
  return self->QNonContiguousByteDeviceRingBufferImpl::size();
}

//  qint64 QNonContiguousByteDeviceRingBufferImpl::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK38QNonContiguousByteDeviceRingBufferImpl3posEv(
    const QNonContiguousByteDeviceRingBufferImpl *self) {
  return self->QNonContiguousByteDeviceRingBufferImpl::pos();
}
