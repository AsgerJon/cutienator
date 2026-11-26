//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QNonContiguousByteDeviceIoDeviceImpl' is pasted in, cut from what the
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtCore__QNonContiguousByteDeviceIoDeviceImpl.cpp, line 1, as moc:QNonContiguousByteDeviceIoDeviceImpl
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN36QNonContiguousByteDeviceIoDeviceImplE_t {};
} // unnamed namespace

template <> constexpr inline auto QNonContiguousByteDeviceIoDeviceImpl::qt_create_metaobjectdata<qt_meta_tag_ZN36QNonContiguousByteDeviceIoDeviceImplE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QNonContiguousByteDeviceIoDeviceImpl"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QNonContiguousByteDeviceIoDeviceImpl, qt_meta_tag_ZN36QNonContiguousByteDeviceIoDeviceImplE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QNonContiguousByteDeviceIoDeviceImpl::staticMetaObject = { {
    QMetaObject::SuperData::link<QNonContiguousByteDevice::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN36QNonContiguousByteDeviceIoDeviceImplE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN36QNonContiguousByteDeviceIoDeviceImplE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN36QNonContiguousByteDeviceIoDeviceImplE_t>.metaTypes,
    nullptr
} };

void QNonContiguousByteDeviceIoDeviceImpl::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QNonContiguousByteDeviceIoDeviceImpl *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QNonContiguousByteDeviceIoDeviceImpl::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QNonContiguousByteDeviceIoDeviceImpl::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN36QNonContiguousByteDeviceIoDeviceImplE_t>.strings))
        return static_cast<void*>(this);
    return QNonContiguousByteDevice::qt_metacast(_clname);
}

int QNonContiguousByteDeviceIoDeviceImpl::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QNonContiguousByteDevice::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 238, as _ZN36QNonContiguousByteDeviceIoDeviceImpl11readPointerExRx
inline const char *QNonContiguousByteDeviceIoDeviceImpl::readPointer(qint64 maximumLength, qint64 &len)
{
    if (eof) {
        len = -1;
        return nullptr;
    }

    if (currentReadBuffer == nullptr)
        currentReadBuffer = new QByteArray(currentReadBufferSize, '\0'); // lazy alloc

    if (maximumLength == -1)
        maximumLength = currentReadBufferSize;

    if (currentReadBufferAmount - currentReadBufferPosition > 0) {
        len = currentReadBufferAmount - currentReadBufferPosition;
        return currentReadBuffer->data() + currentReadBufferPosition;
    }

    qint64 haveRead = device->read(currentReadBuffer->data(),
                                   qMin(maximumLength, currentReadBufferSize));

    if ((haveRead == -1) || (haveRead == 0 && device->atEnd() && !device->isSequential())) {
        eof = true;
        len = -1;
        // size was unknown before, emit a readProgress with the final size
        if (size() == -1)
            emit readProgress(totalAdvancements, totalAdvancements);
        return nullptr;
    }

    currentReadBufferAmount = haveRead;
    currentReadBufferPosition = 0;

    len = haveRead;
    return currentReadBuffer->data();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 275, as _ZN36QNonContiguousByteDeviceIoDeviceImpl18advanceReadPointerEx
inline bool QNonContiguousByteDeviceIoDeviceImpl::advanceReadPointer(qint64 amount)
{
    totalAdvancements += amount;

    // normal advancement
    currentReadBufferPosition += amount;

    if (size() == -1)
        emit readProgress(totalAdvancements, totalAdvancements);
    else
        emit readProgress(totalAdvancements, size());

    // advancing over that what has actually been read before
    if (currentReadBufferPosition > currentReadBufferAmount) {
        qint64 i = currentReadBufferPosition - currentReadBufferAmount;
        while (i > 0) {
            if (!device->getChar(nullptr)) {
                emit readProgress(totalAdvancements - i, size());
                return false; // ### FIXME handle eof
            }
            i--;
        }

        currentReadBufferPosition = 0;
        currentReadBufferAmount = 0;
    }

    return true;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 310, as _ZN36QNonContiguousByteDeviceIoDeviceImpl5resetEv
inline bool QNonContiguousByteDeviceIoDeviceImpl::reset()
{
    bool reset = (initialPosition == 0) ? device->reset() : device->seek(initialPosition);
    if (reset) {
        eof = false; // assume eof is false, it will be true after a read has been attempted
        totalAdvancements = 0; // reset the progress counter
        if (currentReadBuffer) {
            delete currentReadBuffer;
            currentReadBuffer = nullptr;
        }
        currentReadBufferAmount = 0;
        currentReadBufferPosition = 0;
        return true;
    }

    return false;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 338, as _ZNK36QNonContiguousByteDeviceIoDeviceImpl3posEv
inline qint64 QNonContiguousByteDeviceIoDeviceImpl::pos() const
{
    if (device->isSequential())
        return -1;

    return device->pos();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 328, as _ZNK36QNonContiguousByteDeviceIoDeviceImpl4sizeEv
inline qint64 QNonContiguousByteDeviceIoDeviceImpl::size() const
{
    // note that this is different from the size() implementation of QIODevice!

    if (device->isSequential())
        return -1;

    return device->size() - initialPosition;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 305, as _ZNK36QNonContiguousByteDeviceIoDeviceImpl5atEndEv
inline bool QNonContiguousByteDeviceIoDeviceImpl::atEnd() const
{
    return eof;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 216, as _ZN36QNonContiguousByteDeviceIoDeviceImplC1EP9QIODevice
inline QNonContiguousByteDeviceIoDeviceImpl::QNonContiguousByteDeviceIoDeviceImpl(QIODevice *d)
    : QNonContiguousByteDevice(),
      device(d),
      currentReadBuffer(nullptr),
      currentReadBufferSize(16 * 1024),
      currentReadBufferAmount(0),
      currentReadBufferPosition(0),
      totalAdvancements(0),
      eof(false),
      initialPosition(d->pos())
{
    connect(device, &QIODevice::readyRead, this,
            &QNonContiguousByteDevice::readyRead);
    connect(device, &QIODevice::readChannelFinished, this,
            &QNonContiguousByteDevice::readyRead);
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 233, as _ZN36QNonContiguousByteDeviceIoDeviceImplD1Ev
inline QNonContiguousByteDeviceIoDeviceImpl::~QNonContiguousByteDeviceIoDeviceImpl()
{
    delete currentReadBuffer;
}
//  -----------------------------------------------------------------------

//  A QNonContiguousByteDeviceIoDeviceImpl that Python can take functions over in. Every QNonContiguousByteDeviceIoDeviceImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNonContiguousByteDeviceIoDeviceImplCall0)(const void *, qint64, int *);
typedef bool (*CuteQNonContiguousByteDeviceIoDeviceImplCall1)(const void *, int *);
typedef bool (*CuteQNonContiguousByteDeviceIoDeviceImplCall2)(const void *, int *);
typedef qint64 (*CuteQNonContiguousByteDeviceIoDeviceImplCall3)(const void *, int *);
typedef qint64 (*CuteQNonContiguousByteDeviceIoDeviceImplCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNonContiguousByteDeviceIoDeviceImplCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNonContiguousByteDeviceIoDeviceImplCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceIoDeviceImplCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceIoDeviceImplCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceIoDeviceImplCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceIoDeviceImplCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNonContiguousByteDeviceIoDeviceImplCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNonContiguousByteDeviceIoDeviceImpl : public QNonContiguousByteDeviceIoDeviceImpl {
public:
  using QNonContiguousByteDeviceIoDeviceImpl::QNonContiguousByteDeviceIoDeviceImpl;
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

  //  bool QNonContiguousByteDeviceIoDeviceImpl::advanceReadPointer(qint64
  //      amount)
  bool advanceReadPointer(qint64 amount) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceIoDeviceImplCall0 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall0>(taken[0]);
      bool given = call(this, amount, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceIoDeviceImpl::advanceReadPointer(amount);
  }

  //  bool QNonContiguousByteDeviceIoDeviceImpl::atEnd() const
  bool atEnd() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceIoDeviceImplCall1 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceIoDeviceImpl::atEnd();
  }

  //  bool QNonContiguousByteDeviceIoDeviceImpl::reset()
  bool reset() override {
    if (taken[2]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceIoDeviceImplCall2 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceIoDeviceImpl::reset();
  }

  //  qint64 QNonContiguousByteDeviceIoDeviceImpl::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceIoDeviceImplCall3 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceIoDeviceImpl::size();
  }

  //  qint64 QNonContiguousByteDeviceIoDeviceImpl::pos() const
  qint64 pos() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceIoDeviceImplCall4 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNonContiguousByteDeviceIoDeviceImpl::pos();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNonContiguousByteDeviceIoDeviceImplCall5 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall5>(taken[5]);
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
      CuteQNonContiguousByteDeviceIoDeviceImplCall6 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall6>(taken[6]);
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
      CuteQNonContiguousByteDeviceIoDeviceImplCall7 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall7>(taken[7]);
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
      CuteQNonContiguousByteDeviceIoDeviceImplCall8 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall8>(taken[8]);
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
      CuteQNonContiguousByteDeviceIoDeviceImplCall9 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall9>(taken[9]);
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
      CuteQNonContiguousByteDeviceIoDeviceImplCall10 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall10>(taken[10]);
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
      CuteQNonContiguousByteDeviceIoDeviceImplCall11 call = reinterpret_cast<CuteQNonContiguousByteDeviceIoDeviceImplCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNonContiguousByteDeviceIoDeviceImpl::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK36QNonContiguousByteDeviceIoDeviceImpl10metaObjectEv(
    const QNonContiguousByteDeviceIoDeviceImpl *self) {
  return self->metaObject();
}

//  void *QNonContiguousByteDeviceIoDeviceImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN36QNonContiguousByteDeviceIoDeviceImpl11qt_metacastEPKc(
    QNonContiguousByteDeviceIoDeviceImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNonContiguousByteDeviceIoDeviceImpl::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN36QNonContiguousByteDeviceIoDeviceImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QNonContiguousByteDeviceIoDeviceImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNonContiguousByteDeviceIoDeviceImpl::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN36QNonContiguousByteDeviceIoDeviceImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNonContiguousByteDeviceIoDeviceImpl::tr(s, c, n));
}

//  QNonContiguousByteDeviceIoDeviceImpl::QNonContiguousByteDeviceIoDeviceImp
//      l(QIODevice *d)
extern "C" Q_DECL_EXPORT
QNonContiguousByteDeviceIoDeviceImpl *ritual_ZN36QNonContiguousByteDeviceIoDeviceImplC1EP9QIODevice(
    QIODevice *d) {
  return new CuteQNonContiguousByteDeviceIoDeviceImpl(d);
}

//  QNonContiguousByteDeviceIoDeviceImpl::~QNonContiguousByteDeviceIoDeviceIm
//      pl()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QNonContiguousByteDeviceIoDeviceImplD1Ev(
    QNonContiguousByteDeviceIoDeviceImpl *self) {
  delete self;
}

//  const char *QNonContiguousByteDeviceIoDeviceImpl::readPointer(qint64
//      maximumLength, qint64 &len)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN36QNonContiguousByteDeviceIoDeviceImpl11readPointerExRx(
    QNonContiguousByteDeviceIoDeviceImpl *self,
    qint64 maximumLength,
    qint64 *len) {
  return self->readPointer(maximumLength, *len);
}

//  bool QNonContiguousByteDeviceIoDeviceImpl::advanceReadPointer(qint64
//      amount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN36QNonContiguousByteDeviceIoDeviceImpl18advanceReadPointerEx(
    QNonContiguousByteDeviceIoDeviceImpl *self,
    qint64 amount) {
  return self->advanceReadPointer(amount);
}

//  bool QNonContiguousByteDeviceIoDeviceImpl::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK36QNonContiguousByteDeviceIoDeviceImpl5atEndEv(
    const QNonContiguousByteDeviceIoDeviceImpl *self) {
  return self->atEnd();
}

//  bool QNonContiguousByteDeviceIoDeviceImpl::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN36QNonContiguousByteDeviceIoDeviceImpl5resetEv(
    QNonContiguousByteDeviceIoDeviceImpl *self) {
  return self->reset();
}

//  qint64 QNonContiguousByteDeviceIoDeviceImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK36QNonContiguousByteDeviceIoDeviceImpl4sizeEv(
    const QNonContiguousByteDeviceIoDeviceImpl *self) {
  return self->size();
}

//  qint64 QNonContiguousByteDeviceIoDeviceImpl::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK36QNonContiguousByteDeviceIoDeviceImpl3posEv(
    const QNonContiguousByteDeviceIoDeviceImpl *self) {
  return self->pos();
}

//  a Python function taken by a CuteQNonContiguousByteDeviceIoDeviceImpl,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNonContiguousByteDeviceIoDeviceImpl(
    QNonContiguousByteDeviceIoDeviceImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNonContiguousByteDeviceIoDeviceImpl *>(self)->take(key, call);
}

//  bool QNonContiguousByteDeviceIoDeviceImpl::advanceReadPointer(qint64
//      amount)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN36QNonContiguousByteDeviceIoDeviceImpl18advanceReadPointerEx(
    QNonContiguousByteDeviceIoDeviceImpl *self,
    qint64 amount) {
  return self->QNonContiguousByteDeviceIoDeviceImpl::advanceReadPointer(
      amount);
}

//  bool QNonContiguousByteDeviceIoDeviceImpl::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK36QNonContiguousByteDeviceIoDeviceImpl5atEndEv(
    const QNonContiguousByteDeviceIoDeviceImpl *self) {
  return self->QNonContiguousByteDeviceIoDeviceImpl::atEnd();
}

//  bool QNonContiguousByteDeviceIoDeviceImpl::reset()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN36QNonContiguousByteDeviceIoDeviceImpl5resetEv(
    QNonContiguousByteDeviceIoDeviceImpl *self) {
  return self->QNonContiguousByteDeviceIoDeviceImpl::reset();
}

//  qint64 QNonContiguousByteDeviceIoDeviceImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK36QNonContiguousByteDeviceIoDeviceImpl4sizeEv(
    const QNonContiguousByteDeviceIoDeviceImpl *self) {
  return self->QNonContiguousByteDeviceIoDeviceImpl::size();
}

//  qint64 QNonContiguousByteDeviceIoDeviceImpl::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK36QNonContiguousByteDeviceIoDeviceImpl3posEv(
    const QNonContiguousByteDeviceIoDeviceImpl *self) {
  return self->QNonContiguousByteDeviceIoDeviceImpl::pos();
}
