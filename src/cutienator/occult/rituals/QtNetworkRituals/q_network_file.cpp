//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkfile_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QNetworkFile' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 3 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkfile_p.h>
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
#include <QtNetwork/private/qnetworkfile_p.h>
#include <QtNetwork/private/qnetworkrequest_p.h>
#include <QtCore/QDebug>
#include <QtNetwork/QNetworkReply>
#include <QtCore/QDateTime>
#include <QtCore/QFileInfo>
#include <QtCore/QMetaObject>
#include <QtCore/QCoreApplication>
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/private/qnetworkrequest_p.h>
#include "qplatformdefs.h"
#include <QtNetwork/qnetworkcookie.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/private/qhttpheadershelper_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/qhttp1configuration.h>
#include <QtNetwork/qhttp2configuration.h>
#include <QtNetwork/private/http2protocol_p.h>
#endif
#include "QtCore/qdatetime.h"
#include "QtCore/qlocale.h"
#include "QtCore/qshareddata.h"
#include "QtCore/qtimezone.h"
#include "QtCore/private/qduplicatetracker_p.h"
#include "QtCore/private/qtools_p.h"
#if QT_CONFIG(datestring)
# include <stdio.h>
#endif
#include <algorithm>
#include <QtCore/q20algorithm.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from QtNetwork__QNetworkFile.cpp, line 1, as moc:QNetworkFile
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN12QNetworkFileE_t {};
} // unnamed namespace

template <> constexpr inline auto QNetworkFile::qt_create_metaobjectdata<qt_meta_tag_ZN12QNetworkFileE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QNetworkFile",
        "finished",
        "",
        "ok",
        "headerRead",
        "QHttpHeaders::WellKnownHeader",
        "value",
        "networkError",
        "QNetworkReply::NetworkError",
        "error",
        "message",
        "open",
        "close"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'finished'
        QtMocHelpers::SignalData<void(bool)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 3 },
        }}),
        // Signal 'headerRead'
        QtMocHelpers::SignalData<void(QHttpHeaders::WellKnownHeader, const QByteArray &)>(4, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 5, 2 }, { QMetaType::QByteArray, 6 },
        }}),
        // Signal 'networkError'
        QtMocHelpers::SignalData<void(QNetworkReply::NetworkError, const QString &)>(7, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 8, 9 }, { QMetaType::QString, 10 },
        }}),
        // Slot 'open'
        QtMocHelpers::SlotData<void()>(11, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'close'
        QtMocHelpers::SlotData<void()>(12, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QNetworkFile, qt_meta_tag_ZN12QNetworkFileE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QNetworkFile::staticMetaObject = { {
    QMetaObject::SuperData::link<QFile::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12QNetworkFileE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12QNetworkFileE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN12QNetworkFileE_t>.metaTypes,
    nullptr
} };

void QNetworkFile::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QNetworkFile *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->finished((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 1: _t->headerRead((*reinterpret_cast<std::add_pointer_t<QHttpHeaders::WellKnownHeader>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
        case 2: _t->networkError((*reinterpret_cast<std::add_pointer_t<QNetworkReply::NetworkError>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2]))); break;
        case 3: _t->open(); break;
        case 4: _t->close(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 2:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QNetworkReply::NetworkError >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QNetworkFile::*)(bool )>(_a, &QNetworkFile::finished, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QNetworkFile::*)(QHttpHeaders::WellKnownHeader , const QByteArray & )>(_a, &QNetworkFile::headerRead, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QNetworkFile::*)(QNetworkReply::NetworkError , const QString & )>(_a, &QNetworkFile::networkError, 2))
            return;
    }
}

const QMetaObject *QNetworkFile::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QNetworkFile::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN12QNetworkFileE_t>.strings))
        return static_cast<void*>(this);
    return QFile::qt_metacast(_clname);
}

int QNetworkFile::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QFile::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}

// SIGNAL 0
void QNetworkFile::finished(bool _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void QNetworkFile::headerRead(QHttpHeaders::WellKnownHeader _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1, _t2);
}

// SIGNAL 2
void QNetworkFile::networkError(QNetworkReply::NetworkError _t1, const QString & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 2, nullptr, _t1, _t2);
}
QT_WARNING_POP

//  from src/network/access/qnetworkfile.cpp, line 27, as _ZN12QNetworkFile4openEv
inline void QNetworkFile::open()
{
    bool opened = false;
    QFileInfo fi(fileName());
    if (fi.isDir()) {
        QString msg = QCoreApplication::translate("QNetworkAccessFileBackend",
            "Cannot open %1: Path is a directory").arg(fileName());
        emit networkError(QNetworkReply::ContentOperationNotPermittedError, msg);
    } else {
        emit headerRead(QHttpHeaders::WellKnownHeader::LastModified,
                        QNetworkHeadersPrivate::toHttpDate(fi.lastModified()));
        emit headerRead(QHttpHeaders::WellKnownHeader::ContentLength,
                        QByteArray::number(fi.size()));
        opened = QFile::open(QIODevice::ReadOnly | QIODevice::Unbuffered);
        if (!opened) {
            QString msg = QCoreApplication::translate("QNetworkAccessFileBackend",
                "Error opening %1: %2").arg(fileName(), errorString());
            if (exists())
                emit networkError(QNetworkReply::ContentAccessDenied, msg);
            else
                emit networkError(QNetworkReply::ContentNotFoundError, msg);
        }
    }
    emit finished(opened);
}

//  from src/network/access/qnetworkfile.cpp, line 53, as _ZN12QNetworkFile5closeEv
inline void QNetworkFile::close()
{
    // This override is needed because 'using' keyword cannot be used for slots. And the base
    // function is not an invokable/slot function.
    QFile::close();
}

//  from src/network/access/qnetworkrequest.cpp, line 1826, as _ZN22QNetworkHeadersPrivate10toHttpDateERK9QDateTime
inline QByteArray QNetworkHeadersPrivate::toHttpDate(const QDateTime &dt)
{
    return QLocale::c().toString(dt.toUTC(), u"ddd, dd MMM yyyy hh:mm:ss 'GMT'").toLatin1();
}

//  from src/network/access/qnetworkfile.cpp, line 17, as _ZN12QNetworkFileC1Ev
inline QNetworkFile::QNetworkFile()
    : QFile()
{
}

//  from src/network/access/qnetworkfile.cpp, line 22, as _ZN12QNetworkFileC1ERK7QString
inline QNetworkFile::QNetworkFile(const QString &name)
    : QFile(name)
{
}
//  -----------------------------------------------------------------------

//  A QNetworkFile that Python can take functions over in. Every QNetworkFile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNetworkFileCall0)(const void *, int *);
typedef QString * (*CuteQNetworkFileCall1)(const void *, int *);
typedef bool (*CuteQNetworkFileCall2)(const void *, int, int *);
typedef qint64 (*CuteQNetworkFileCall3)(const void *, int *);
typedef bool (*CuteQNetworkFileCall4)(const void *, qint64, int *);
typedef int (*CuteQNetworkFileCall5)(const void *, int *);
typedef bool (*CuteQNetworkFileCall6)(const void *, int, int *);
typedef bool (*CuteQNetworkFileCall7)(const void *, int *);
typedef qint64 (*CuteQNetworkFileCall8)(const void *, int *);
typedef bool (*CuteQNetworkFileCall9)(const void *, qint64, int *);
typedef bool (*CuteQNetworkFileCall10)(const void *, int *);
typedef qint64 (*CuteQNetworkFileCall11)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQNetworkFileCall12)(const void *, char *, qint64, int *);
typedef bool (*CuteQNetworkFileCall13)(const void *, int *);
typedef qint64 (*CuteQNetworkFileCall14)(const void *, int *);
typedef qint64 (*CuteQNetworkFileCall15)(const void *, int *);
typedef bool (*CuteQNetworkFileCall16)(const void *, int *);
typedef bool (*CuteQNetworkFileCall17)(const void *, int, int *);
typedef bool (*CuteQNetworkFileCall18)(const void *, int, int *);
typedef qint64 (*CuteQNetworkFileCall19)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkFileCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkFileCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkFileCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkFileCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkFileCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkFileCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkFileCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkFile : public QNetworkFile {
public:
  using QNetworkFile::QNetworkFile;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFileDevice8fileNameEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFileDevice6resizeEx")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFileDevice11permissionsEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFileDevice14setPermissionsE6QFlagsINS_10PermissionEE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[19] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QNetworkFile::close()
  void close() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkFileCall0 call = reinterpret_cast<CuteQNetworkFileCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkFile::close();
  }

  //  QString QFile::fileName() const
  QString fileName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkFileCall1 call = reinterpret_cast<CuteQNetworkFileCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFile::fileName();
  }

  //  bool QFile::open(OpenMode flags)
  bool open(QIODeviceBase::OpenMode flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkFileCall2 call = reinterpret_cast<CuteQNetworkFileCall2>(taken[2]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QFile::open(flags);
  }

  //  qint64 QFile::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkFileCall3 call = reinterpret_cast<CuteQNetworkFileCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFile::size();
  }

  //  bool QFile::resize(qint64 sz)
  bool resize(qint64 sz) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkFileCall4 call = reinterpret_cast<CuteQNetworkFileCall4>(taken[4]);
      bool given = call(this, sz, &handled);
      if (handled) return given;
    }
    return QFile::resize(sz);
  }

  //  Permissions QFile::permissions() const
  QFileDevice::Permissions permissions() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkFileCall5 call = reinterpret_cast<CuteQNetworkFileCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return QFlags<QFileDevice::Permission>::fromInt(given);
    }
    return QFile::permissions();
  }

  //  bool QFile::setPermissions(Permissions permissionSpec)
  bool setPermissions(QFileDevice::Permissions permissionSpec) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkFileCall6 call = reinterpret_cast<CuteQNetworkFileCall6>(taken[6]);
      bool given = call(this, static_cast<int>(permissionSpec.toInt()), &handled);
      if (handled) return given;
    }
    return QFile::setPermissions(permissionSpec);
  }

  //  bool QFileDevice::isSequential() const
  bool isSequential() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkFileCall7 call = reinterpret_cast<CuteQNetworkFileCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::isSequential();
  }

  //  qint64 QFileDevice::pos() const
  qint64 pos() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkFileCall8 call = reinterpret_cast<CuteQNetworkFileCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::pos();
  }

  //  bool QFileDevice::seek(qint64 offset)
  bool seek(qint64 offset) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkFileCall9 call = reinterpret_cast<CuteQNetworkFileCall9>(taken[9]);
      bool given = call(this, offset, &handled);
      if (handled) return given;
    }
    return QFileDevice::seek(offset);
  }

  //  bool QFileDevice::atEnd() const
  bool atEnd() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkFileCall10 call = reinterpret_cast<CuteQNetworkFileCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::atEnd();
  }

  //  qint64 QFileDevice::readData(char *data, qint64 maxlen)
  qint64 readData(char *data, qint64 maxlen) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNetworkFileCall11 call = reinterpret_cast<CuteQNetworkFileCall11>(taken[11]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QFileDevice::readData(data, maxlen);
  }

  //  qint64 QFileDevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNetworkFileCall12 call = reinterpret_cast<CuteQNetworkFileCall12>(taken[12]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QFileDevice::readLineData(data, maxlen);
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[13]) {
      int handled = 0;
      CuteQNetworkFileCall13 call = reinterpret_cast<CuteQNetworkFileCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQNetworkFileCall14 call = reinterpret_cast<CuteQNetworkFileCall14>(taken[14]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQNetworkFileCall15 call = reinterpret_cast<CuteQNetworkFileCall15>(taken[15]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQNetworkFileCall16 call = reinterpret_cast<CuteQNetworkFileCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[17]) {
      int handled = 0;
      CuteQNetworkFileCall17 call = reinterpret_cast<CuteQNetworkFileCall17>(taken[17]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[18]) {
      int handled = 0;
      CuteQNetworkFileCall18 call = reinterpret_cast<CuteQNetworkFileCall18>(taken[18]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[19]) {
      int handled = 0;
      CuteQNetworkFileCall19 call = reinterpret_cast<CuteQNetworkFileCall19>(taken[19]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQNetworkFileCall20 call = reinterpret_cast<CuteQNetworkFileCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQNetworkFileCall21 call = reinterpret_cast<CuteQNetworkFileCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQNetworkFileCall22 call = reinterpret_cast<CuteQNetworkFileCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQNetworkFileCall23 call = reinterpret_cast<CuteQNetworkFileCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQNetworkFileCall24 call = reinterpret_cast<CuteQNetworkFileCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQNetworkFileCall25 call = reinterpret_cast<CuteQNetworkFileCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQNetworkFileCall26 call = reinterpret_cast<CuteQNetworkFileCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QNetworkFile10metaObjectEv(
    const QNetworkFile *self) {
  return self->metaObject();
}

//  void *QNetworkFile::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QNetworkFile11qt_metacastEPKc(
    QNetworkFile *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNetworkFile::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QNetworkFile11qt_metacallEN11QMetaObject4CallEiPPv(
    QNetworkFile *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNetworkFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QNetworkFile2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkFile::tr(s, c, n));
}

//  QNetworkFile::QNetworkFile()
extern "C" Q_DECL_EXPORT
QNetworkFile *ritual_ZN12QNetworkFileC1Ev() {
  return new CuteQNetworkFile();
}

//  QNetworkFile::QNetworkFile(const QString &name)
extern "C" Q_DECL_EXPORT
QNetworkFile *ritual_ZN12QNetworkFileC1ERK7QString(const QString *name) {
  return new CuteQNetworkFile(*name);
}

//  void QNetworkFile::open()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QNetworkFile4openEv(QNetworkFile *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkFile")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "open()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "open()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNetworkFile::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QNetworkFile5closeEv(QNetworkFile *self) {
  self->close();
}

//  void QNetworkFile::finished(bool ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QNetworkFile8finishedEb(QNetworkFile *self, bool ok) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkFile")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "finished(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "finished(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&ok)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNetworkFile::headerRead(QHttpHeaders::WellKnownHeader a0, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QNetworkFile10headerReadEN12QHttpHeaders15WellKnownHeaderERK10QByteArray(
    QNetworkFile *self,
    QHttpHeaders::WellKnownHeader a0,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkFile")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "headerRead(QHttpHeaders::WellKnownHeader,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "headerRead(QHttpHeaders::WellKnownHeader,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNetworkFile::networkError(QNetworkReply::NetworkError error, const
//      QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QNetworkFile12networkErrorEN13QNetworkReply12NetworkErrorERK7QString(
    QNetworkFile *self,
    QNetworkReply::NetworkError error,
    const QString *message) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkFile")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "networkError(QNetworkReply::NetworkError,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "networkError(QNetworkReply::NetworkError,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&error)),
      const_cast<void *>(static_cast<const void *>(message)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQNetworkFile, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkFile(
    QNetworkFile *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkFile *>(self)->take(key, call);
}

//  void QNetworkFile::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QNetworkFile5closeEv(QNetworkFile *self) {
  self->QNetworkFile::close();
}
