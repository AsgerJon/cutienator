//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QByteDeviceWrappingIoDevice' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
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

//  from QtCore__QByteDeviceWrappingIoDevice.cpp, line 1, as moc:QByteDeviceWrappingIoDevice
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN27QByteDeviceWrappingIoDeviceE_t {};
} // unnamed namespace

template <> constexpr inline auto QByteDeviceWrappingIoDevice::qt_create_metaobjectdata<qt_meta_tag_ZN27QByteDeviceWrappingIoDeviceE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QByteDeviceWrappingIoDevice"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QByteDeviceWrappingIoDevice, qt_meta_tag_ZN27QByteDeviceWrappingIoDeviceE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QByteDeviceWrappingIoDevice::staticMetaObject = { {
    QMetaObject::SuperData::link<QIODevice::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QByteDeviceWrappingIoDeviceE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QByteDeviceWrappingIoDeviceE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN27QByteDeviceWrappingIoDeviceE_t>.metaTypes,
    nullptr
} };

void QByteDeviceWrappingIoDevice::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QByteDeviceWrappingIoDevice *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QByteDeviceWrappingIoDevice::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QByteDeviceWrappingIoDevice::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QByteDeviceWrappingIoDeviceE_t>.strings))
        return static_cast<void*>(this);
    return QIODevice::qt_metacast(_clname);
}

int QByteDeviceWrappingIoDevice::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QIODevice::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 367, as _ZN27QByteDeviceWrappingIoDevice5resetEv
inline bool QByteDeviceWrappingIoDevice::reset()
{
    return byteDevice->reset();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 380, as _ZN27QByteDeviceWrappingIoDevice8readDataEPcx
inline qint64 QByteDeviceWrappingIoDevice::readData(char *data, qint64 maxSize)
{
    qint64 len;
    const char *readPointer = byteDevice->readPointer(maxSize, len);
    if (len == -1)
        return -1;

    memcpy(data, readPointer, len);
    byteDevice->advanceReadPointer(len);
    return len;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 392, as _ZN27QByteDeviceWrappingIoDevice9writeDataEPKcx
inline qint64 QByteDeviceWrappingIoDevice::writeData(const char *data, qint64 maxSize)
{
    Q_UNUSED(data);
    Q_UNUSED(maxSize);
    return -1;
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 357, as _ZNK27QByteDeviceWrappingIoDevice12isSequentialEv
inline bool QByteDeviceWrappingIoDevice::isSequential() const
{
    return (byteDevice->size() == -1);
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 372, as _ZNK27QByteDeviceWrappingIoDevice4sizeEv
inline qint64 QByteDeviceWrappingIoDevice::size() const
{
    if (isSequential())
        return 0;

    return byteDevice->size();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 362, as _ZNK27QByteDeviceWrappingIoDevice5atEndEv
inline bool QByteDeviceWrappingIoDevice::atEnd() const
{
    return byteDevice->atEnd();
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 346, as _ZN27QByteDeviceWrappingIoDeviceC1EP24QNonContiguousByteDevice
inline QByteDeviceWrappingIoDevice::QByteDeviceWrappingIoDevice(QNonContiguousByteDevice *bd)
    : QIODevice(nullptr), byteDevice(bd)
{
    connect(bd, &QNonContiguousByteDevice::readyRead, this, &QIODevice::readyRead);

    open(ReadOnly);
}

//  from src/corelib/io/qnoncontiguousbytedevice.cpp, line 354, as _ZN27QByteDeviceWrappingIoDeviceD1Ev
inline QByteDeviceWrappingIoDevice::~QByteDeviceWrappingIoDevice()
    = default;
//  -----------------------------------------------------------------------

//  Only a class built on QByteDeviceWrappingIoDevice may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQByteDeviceWrappingIoDevice : QByteDeviceWrappingIoDevice {
  using QByteDeviceWrappingIoDevice::readData;
};

//  A QByteDeviceWrappingIoDevice that Python can take functions over in. Every QByteDeviceWrappingIoDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall0)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall1)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall2)(const void *, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall3)(const void *, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall4)(const void *, char *, qint64, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall5)(const void *, int, int *);
typedef void (*CuteQByteDeviceWrappingIoDeviceCall6)(const void *, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall7)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall8)(const void *, qint64, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall9)(const void *, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall10)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall11)(const void *, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall12)(const void *, int, int *);
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall13)(const void *, int, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall14)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQByteDeviceWrappingIoDeviceCall15)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQByteDeviceWrappingIoDeviceCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQByteDeviceWrappingIoDeviceCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQByteDeviceWrappingIoDeviceCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQByteDeviceWrappingIoDeviceCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQByteDeviceWrappingIoDeviceCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQByteDeviceWrappingIoDeviceCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQByteDeviceWrappingIoDevice : public QByteDeviceWrappingIoDevice {
public:
  using QByteDeviceWrappingIoDevice::QByteDeviceWrappingIoDevice;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QByteDeviceWrappingIoDevice::isSequential() const
  bool isSequential() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall0 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QByteDeviceWrappingIoDevice::isSequential();
  }

  //  bool QByteDeviceWrappingIoDevice::atEnd() const
  bool atEnd() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall1 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QByteDeviceWrappingIoDevice::atEnd();
  }

  //  bool QByteDeviceWrappingIoDevice::reset()
  bool reset() override {
    if (taken[2]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall2 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QByteDeviceWrappingIoDevice::reset();
  }

  //  qint64 QByteDeviceWrappingIoDevice::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall3 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QByteDeviceWrappingIoDevice::size();
  }

  //  qint64 QByteDeviceWrappingIoDevice::readData(char *data, qint64
  //      maxSize)
  qint64 readData(char *data, qint64 maxSize) override {
    if (taken[4]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall4 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall4>(taken[4]);
      qint64 given = call(this, data, maxSize, &handled);
      if (handled) return given;
    }
    return QByteDeviceWrappingIoDevice::readData(data, maxSize);
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[5]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall5 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall5>(taken[5]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  void QIODevice::close()
  void close() override {
    if (taken[6]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall6 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QIODevice::close();
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall7 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall7>(taken[7]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[8]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall8 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall8>(taken[8]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall9 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall10 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall10>(taken[10]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall11 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[12]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall12 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall12>(taken[12]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[13]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall13 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall13>(taken[13]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[14]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall14 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall14>(taken[14]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QIODevice::readLineData(data, maxlen);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[15]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall15 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall15>(taken[15]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall16 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall17 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall18 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall19 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall20 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall21 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQByteDeviceWrappingIoDeviceCall22 call = reinterpret_cast<CuteQByteDeviceWrappingIoDeviceCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QByteDeviceWrappingIoDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QByteDeviceWrappingIoDevice10metaObjectEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->metaObject();
}

//  void *QByteDeviceWrappingIoDevice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QByteDeviceWrappingIoDevice11qt_metacastEPKc(
    QByteDeviceWrappingIoDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QByteDeviceWrappingIoDevice::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QByteDeviceWrappingIoDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    QByteDeviceWrappingIoDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QByteDeviceWrappingIoDevice::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QByteDeviceWrappingIoDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QByteDeviceWrappingIoDevice::tr(s, c, n));
}

//  QByteDeviceWrappingIoDevice::QByteDeviceWrappingIoDevice(QNonContiguousBy
//      teDevice *bd)
extern "C" Q_DECL_EXPORT
QByteDeviceWrappingIoDevice *ritual_ZN27QByteDeviceWrappingIoDeviceC1EP24QNonContiguousByteDevice(
    QNonContiguousByteDevice *bd) {
  return new CuteQByteDeviceWrappingIoDevice(bd);
}

//  QByteDeviceWrappingIoDevice::~QByteDeviceWrappingIoDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QByteDeviceWrappingIoDeviceD1Ev(
    QByteDeviceWrappingIoDevice *self) {
  delete self;
}

//  bool QByteDeviceWrappingIoDevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QByteDeviceWrappingIoDevice12isSequentialEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->isSequential();
}

//  bool QByteDeviceWrappingIoDevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QByteDeviceWrappingIoDevice5atEndEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->atEnd();
}

//  bool QByteDeviceWrappingIoDevice::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QByteDeviceWrappingIoDevice5resetEv(
    QByteDeviceWrappingIoDevice *self) {
  return self->reset();
}

//  qint64 QByteDeviceWrappingIoDevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK27QByteDeviceWrappingIoDevice4sizeEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->size();
}

//  qint64 QByteDeviceWrappingIoDevice::readData(char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN27QByteDeviceWrappingIoDevice8readDataEPcx(
    QByteDeviceWrappingIoDevice *self,
    char *data,
    qint64 maxSize) {
  return self->readData(data, maxSize);
}

//  qint64 QByteDeviceWrappingIoDevice::writeData(const char *data, qint64
//      maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN27QByteDeviceWrappingIoDevice9writeDataEPKcx(
    QByteDeviceWrappingIoDevice *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  a Python function taken by a CuteQByteDeviceWrappingIoDevice, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QByteDeviceWrappingIoDevice(
    QByteDeviceWrappingIoDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQByteDeviceWrappingIoDevice *>(self)->take(key, call);
}

//  bool QByteDeviceWrappingIoDevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QByteDeviceWrappingIoDevice12isSequentialEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->QByteDeviceWrappingIoDevice::isSequential();
}

//  bool QByteDeviceWrappingIoDevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QByteDeviceWrappingIoDevice5atEndEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->QByteDeviceWrappingIoDevice::atEnd();
}

//  bool QByteDeviceWrappingIoDevice::reset()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QByteDeviceWrappingIoDevice5resetEv(
    QByteDeviceWrappingIoDevice *self) {
  return self->QByteDeviceWrappingIoDevice::reset();
}

//  qint64 QByteDeviceWrappingIoDevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK27QByteDeviceWrappingIoDevice4sizeEv(
    const QByteDeviceWrappingIoDevice *self) {
  return self->QByteDeviceWrappingIoDevice::size();
}

//  qint64 QByteDeviceWrappingIoDevice::readData(char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN27QByteDeviceWrappingIoDevice8readDataEPcx(
    QByteDeviceWrappingIoDevice *self,
    char *data,
    qint64 maxSize) {
  return static_cast<OwnQByteDeviceWrappingIoDevice *>(self)->OwnQByteDeviceWrappingIoDevice::readData(
      data,
      maxSize);
}
