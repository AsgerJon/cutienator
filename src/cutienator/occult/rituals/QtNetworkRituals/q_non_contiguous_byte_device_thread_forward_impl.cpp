//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpthreaddelegate_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QNonContiguousByteDeviceThreadForwardImpl' is pasted in, cut from what
//  the moc of Qt 6.12.0 writes for its header: Qt's library keeps it to
//  itself; added are 4 rituals that lean on what moc writes for a class of
//  the part Qt keeps to itself, whose ritual file carries moc's output,
//  drafted by a copy of the generator that lets those names through. A copy
//  of a meta-object is a second one: 'qobject_cast' between it and Qt's own
//  does not match. Kept as it is when the generator runs again.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpthreaddelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtNetwork__QNonContiguousByteDeviceThreadForwardImpl.cpp, line 1, as moc:QNonContiguousByteDeviceThreadForwardImpl
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN41QNonContiguousByteDeviceThreadForwardImplE_t {};
} // unnamed namespace

template <> constexpr inline auto QNonContiguousByteDeviceThreadForwardImpl::qt_create_metaobjectdata<qt_meta_tag_ZN41QNonContiguousByteDeviceThreadForwardImplE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QNonContiguousByteDeviceThreadForwardImpl",
        "wantData",
        "",
        "processedData",
        "pos",
        "amount",
        "resetData",
        "bool*",
        "b",
        "haveDataSlot",
        "dataArray",
        "dataAtEnd",
        "dataSize"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'wantData'
        QtMocHelpers::SignalData<void(qint64)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::LongLong, 2 },
        }}),
        // Signal 'processedData'
        QtMocHelpers::SignalData<void(qint64, qint64)>(3, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::LongLong, 4 }, { QMetaType::LongLong, 5 },
        }}),
        // Signal 'resetData'
        QtMocHelpers::SignalData<void(bool *)>(6, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 7, 8 },
        }}),
        // Slot 'haveDataSlot'
        QtMocHelpers::SlotData<void(qint64, const QByteArray &, bool, qint64)>(9, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::LongLong, 4 }, { QMetaType::QByteArray, 10 }, { QMetaType::Bool, 11 }, { QMetaType::LongLong, 12 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QNonContiguousByteDeviceThreadForwardImpl, qt_meta_tag_ZN41QNonContiguousByteDeviceThreadForwardImplE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QNonContiguousByteDeviceThreadForwardImpl::staticMetaObject = { {
    QMetaObject::SuperData::link<QNonContiguousByteDevice::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN41QNonContiguousByteDeviceThreadForwardImplE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN41QNonContiguousByteDeviceThreadForwardImplE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN41QNonContiguousByteDeviceThreadForwardImplE_t>.metaTypes,
    nullptr
} };

void QNonContiguousByteDeviceThreadForwardImpl::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QNonContiguousByteDeviceThreadForwardImpl *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->wantData((*reinterpret_cast<std::add_pointer_t<qint64>>(_a[1]))); break;
        case 1: _t->processedData((*reinterpret_cast<std::add_pointer_t<qint64>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<qint64>>(_a[2]))); break;
        case 2: _t->resetData((*reinterpret_cast<std::add_pointer_t<bool*>>(_a[1]))); break;
        case 3: _t->haveDataSlot((*reinterpret_cast<std::add_pointer_t<qint64>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<bool>>(_a[3])),(*reinterpret_cast<std::add_pointer_t<qint64>>(_a[4]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QNonContiguousByteDeviceThreadForwardImpl::*)(qint64 )>(_a, &QNonContiguousByteDeviceThreadForwardImpl::wantData, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QNonContiguousByteDeviceThreadForwardImpl::*)(qint64 , qint64 )>(_a, &QNonContiguousByteDeviceThreadForwardImpl::processedData, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QNonContiguousByteDeviceThreadForwardImpl::*)(bool * )>(_a, &QNonContiguousByteDeviceThreadForwardImpl::resetData, 2))
            return;
    }
}

const QMetaObject *QNonContiguousByteDeviceThreadForwardImpl::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QNonContiguousByteDeviceThreadForwardImpl::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN41QNonContiguousByteDeviceThreadForwardImplE_t>.strings))
        return static_cast<void*>(this);
    return QNonContiguousByteDevice::qt_metacast(_clname);
}

int QNonContiguousByteDeviceThreadForwardImpl::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QNonContiguousByteDevice::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 4;
    }
    return _id;
}

// SIGNAL 0
void QNonContiguousByteDeviceThreadForwardImpl::wantData(qint64 _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void QNonContiguousByteDeviceThreadForwardImpl::processedData(qint64 _t1, qint64 _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1, _t2);
}

// SIGNAL 2
void QNonContiguousByteDeviceThreadForwardImpl::resetData(bool * _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 2, nullptr, _t1);
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

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

//  void *QNonContiguousByteDeviceThreadForwardImpl::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl11qt_metacastEPKc(
    QNonContiguousByteDeviceThreadForwardImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      QNonContiguousByteDeviceThreadForwardImpl::qt_metacall(QMetaObject::C
//      all a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QNonContiguousByteDeviceThreadForwardImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNonContiguousByteDeviceThreadForwardImpl::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNonContiguousByteDeviceThreadForwardImpl::tr(s, c, n));
}

//  QNonContiguousByteDeviceThreadForwardImpl::QNonContiguousByteDeviceThread
//      ForwardImpl(bool aE, qint64 s)
extern "C" Q_DECL_EXPORT
QNonContiguousByteDeviceThreadForwardImpl *ritual_ZN41QNonContiguousByteDeviceThreadForwardImplC1Ebx(
    bool aE,
    qint64 s) {
  return new CuteQNonContiguousByteDeviceThreadForwardImpl(aE, s);
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

//  void QNonContiguousByteDeviceThreadForwardImpl::wantData(qint64 a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl8wantDataEx(
    QNonContiguousByteDeviceThreadForwardImpl *self,
    qint64 a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNonContiguousByteDeviceThreadForwardImpl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "wantData(qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "wantData(qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNonContiguousByteDeviceThreadForwardImpl::processedData(qint64 pos,
//      qint64 amount)
extern "C" Q_DECL_EXPORT
void ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl13processedDataExx(
    QNonContiguousByteDeviceThreadForwardImpl *self,
    qint64 pos,
    qint64 amount) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNonContiguousByteDeviceThreadForwardImpl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "processedData(qint64,qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "processedData(qint64,qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&pos)),
      const_cast<void *>(static_cast<const void *>(&amount)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNonContiguousByteDeviceThreadForwardImpl::resetData(bool *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN41QNonContiguousByteDeviceThreadForwardImpl9resetDataEPb(
    QNonContiguousByteDeviceThreadForwardImpl *self,
    bool *b) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNonContiguousByteDeviceThreadForwardImpl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "resetData(bool *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "resetData(bool *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&b)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
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

//  bool QNonContiguousByteDeviceThreadForwardImpl::advanceReadPointer(qint64
//      a)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN41QNonContiguousByteDeviceThreadForwardImpl18advanceReadPointerEx(
    QNonContiguousByteDeviceThreadForwardImpl *self,
    qint64 a) {
  return self->QNonContiguousByteDeviceThreadForwardImpl::advanceReadPointer(
      a);
}

//  bool QNonContiguousByteDeviceThreadForwardImpl::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK41QNonContiguousByteDeviceThreadForwardImpl5atEndEv(
    const QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->QNonContiguousByteDeviceThreadForwardImpl::atEnd();
}

//  bool QNonContiguousByteDeviceThreadForwardImpl::reset()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN41QNonContiguousByteDeviceThreadForwardImpl5resetEv(
    QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->QNonContiguousByteDeviceThreadForwardImpl::reset();
}

//  qint64 QNonContiguousByteDeviceThreadForwardImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK41QNonContiguousByteDeviceThreadForwardImpl4sizeEv(
    const QNonContiguousByteDeviceThreadForwardImpl *self) {
  return self->QNonContiguousByteDeviceThreadForwardImpl::size();
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
