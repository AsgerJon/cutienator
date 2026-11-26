//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessfilebackend_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QNetworkAccessFileBackend' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessfilebackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtNetwork/private/qnetworkaccessfilebackend_p.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qdir.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QDateTime>
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

//  from QtNetwork__QNetworkAccessFileBackend.cpp, line 1, as moc:QNetworkAccessFileBackend
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN25QNetworkAccessFileBackendE_t {};
} // unnamed namespace

template <> constexpr inline auto QNetworkAccessFileBackend::qt_create_metaobjectdata<qt_meta_tag_ZN25QNetworkAccessFileBackendE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QNetworkAccessFileBackend",
        "uploadReadyReadSlot",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'uploadReadyReadSlot'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QNetworkAccessFileBackend, qt_meta_tag_ZN25QNetworkAccessFileBackendE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QNetworkAccessFileBackend::staticMetaObject = { {
    QMetaObject::SuperData::link<QNetworkAccessBackend::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QNetworkAccessFileBackendE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QNetworkAccessFileBackendE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN25QNetworkAccessFileBackendE_t>.metaTypes,
    nullptr
} };

void QNetworkAccessFileBackend::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QNetworkAccessFileBackend *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->uploadReadyReadSlot(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QNetworkAccessFileBackend::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QNetworkAccessFileBackend::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QNetworkAccessFileBackendE_t>.strings))
        return static_cast<void*>(this);
    return QNetworkAccessBackend::qt_metacast(_clname);
}

int QNetworkAccessFileBackend::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QNetworkAccessBackend::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 156, as _ZN25QNetworkAccessFileBackend19uploadReadyReadSlotEv
inline void QNetworkAccessFileBackend::uploadReadyReadSlot()
{
    if (hasUploadFinished)
        return;

    forever {
        QByteArray data(16 * 1024, Qt::Uninitialized);
        qint64 haveRead = uploadByteDevice()->peek(data.data(), data.size());
        if (haveRead == -1) {
            // EOF
            hasUploadFinished = true;
            file.flush();
            file.close();
            finished();
            break;
        } else if (haveRead == 0) {
            // nothing to read right now, we will be called again later
            break;
        } else {
            qint64 haveWritten;
            data.truncate(haveRead);
            haveWritten = file.write(data);

            if (haveWritten < 0) {
                // write error!
                QString msg = QCoreApplication::translate("QNetworkAccessFileBackend", "Write error writing to %1: %2")
                              .arg(url().toString(), file.errorString());
                error(QNetworkReply::ProtocolFailure, msg);

                finished();
                return;
            } else {
                uploadByteDevice()->skip(haveWritten);
            }


            file.flush();
        }
    }
}

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 78, as _ZN25QNetworkAccessFileBackend4openEv
#if defined(Q_OS_LINUX)
inline void QNetworkAccessFileBackend::open()
{
    QUrl url = this->url();

    if (url.host() == "localhost"_L1)
        url.setHost(QString());
#if !defined(Q_OS_WIN)
    // do not allow UNC paths on Unix
    if (!url.host().isEmpty()) {
        // we handle only local files
        error(QNetworkReply::ProtocolInvalidOperationError,
              QCoreApplication::translate("QNetworkAccessFileBackend", "Request for opening non-local file %1").arg(url.toString()));
        finished();
        return;
    }
#endif // !defined(Q_OS_WIN)
    if (url.path().isEmpty())
        url.setPath("/"_L1);
    setUrl(url);

    QString fileName = url.toLocalFile();
    if (fileName.isEmpty()) {
        if (url.scheme() == "qrc"_L1) {
            fileName = u':' + url.path();
        } else {
#if defined(Q_OS_ANDROID)
            if (url.scheme() == "assets"_L1)
                fileName = "assets:"_L1 + url.path();
            else
#endif
                fileName = url.toString(QUrl::RemoveAuthority | QUrl::RemoveFragment | QUrl::RemoveQuery);
        }
    }
    file.setFileName(fileName);

    if (operation() == QNetworkAccessManager::GetOperation) {
        if (!loadFileInfo())
            return;
    }

    QIODevice::OpenMode mode;
    switch (operation()) {
    case QNetworkAccessManager::GetOperation:
        mode = QIODevice::ReadOnly;
        break;
    case QNetworkAccessManager::PutOperation:
        mode = QIODevice::WriteOnly | QIODevice::Truncate;
        createUploadByteDevice();
        QObject::connect(uploadByteDevice(), SIGNAL(readyRead()), this, SLOT(uploadReadyReadSlot()));
        QMetaObject::invokeMethod(this, "uploadReadyReadSlot", Qt::QueuedConnection);
        break;
    default:
        Q_ASSERT_X(false, "QNetworkAccessFileBackend::open",
                   "Got a request operation I cannot handle!!");
        return;
    }

    mode |= QIODevice::Unbuffered;
    bool opened = file.open(mode);
    if (file.isSequential())
        connect(&file, &QIODevice::readChannelFinished, this, [this]() { finished(); });

    // could we open the file?
    if (!opened) {
        QString msg = QCoreApplication::translate("QNetworkAccessFileBackend", "Error opening %1: %2")
                                                .arg(this->url().toString(), file.errorString());

        // why couldn't we open the file?
        // if we're opening for reading, either it doesn't exist, or it's access denied
        // if we're opening for writing, not existing means it's access denied too
        if (file.exists() || operation() == QNetworkAccessManager::PutOperation)
            error(QNetworkReply::ContentAccessDenied, msg);
        else
            error(QNetworkReply::ContentNotFoundError, msg);
        finished();
    }
}
#endif  // defined(Q_OS_LINUX)

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 230, as _ZN25QNetworkAccessFileBackend4readEPcx
inline qint64 QNetworkAccessFileBackend::read(char *data, qint64 maxlen)
{
    if (operation() != QNetworkAccessManager::GetOperation)
        return 0;
    qint64 actuallyRead = file.read(data, maxlen);
    if (actuallyRead <= 0) {
        // EOF or error
        if (file.error() != QFile::NoError) {
            QString msg = QCoreApplication::translate("QNetworkAccessFileBackend", "Read error reading from %1: %2")
                            .arg(url().toString(), file.errorString());
            error(QNetworkReply::ProtocolFailure, msg);

            finished();
            return -1;
        }

        finished();
        return actuallyRead;
    }
    if (!file.isSequential() && file.atEnd())
        finished();
    totalBytes += actuallyRead;
    return actuallyRead;
}

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 197, as _ZN25QNetworkAccessFileBackend5closeEv
inline void QNetworkAccessFileBackend::close()
{
    if (operation() == QNetworkAccessManager::GetOperation) {
        file.close();
    }
}

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 74, as _ZN25QNetworkAccessFileBackendD0Ev
inline QNetworkAccessFileBackend::~QNetworkAccessFileBackend()
{
}

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 223, as _ZNK25QNetworkAccessFileBackend14bytesAvailableEv
inline qint64 QNetworkAccessFileBackend::bytesAvailable() const
{
    if (operation() != QNetworkAccessManager::GetOperation)
        return 0;
    return file.bytesAvailable();
}

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 67, as _ZN25QNetworkAccessFileBackendC1Ev
inline QNetworkAccessFileBackend::QNetworkAccessFileBackend()
    : QNetworkAccessBackend(QNetworkAccessBackend::TargetType::Local),
      totalBytes(0),
      hasUploadFinished(false)
{
}

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 204, as _ZN25QNetworkAccessFileBackend12loadFileInfoEv
inline bool QNetworkAccessFileBackend::loadFileInfo()
{
    QFileInfo fi(file);
    setHeader(QNetworkRequest::LastModifiedHeader, fi.lastModified());
    setHeader(QNetworkRequest::ContentLengthHeader, fi.size());

    // signal we're open
    metaDataChanged();

    if (fi.isDir()) {
        error(QNetworkReply::ContentOperationNotPermittedError,
              QCoreApplication::translate("QNetworkAccessFileBackend", "Cannot open %1: Path is a directory").arg(url().toString()));
        finished();
        return false;
    }

    return true;
}
//  -----------------------------------------------------------------------

//  A QNetworkAccessFileBackend that Python can take functions over in. Every QNetworkAccessFileBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNetworkAccessFileBackendCall0)(const void *, int *);
typedef void (*CuteQNetworkAccessFileBackendCall1)(const void *, int *);
typedef qint64 (*CuteQNetworkAccessFileBackendCall2)(const void *, int *);
typedef qint64 (*CuteQNetworkAccessFileBackendCall3)(const void *, char *, qint64, int *);
typedef bool (*CuteQNetworkAccessFileBackendCall4)(const void *, int *);
#if QT_CONFIG(ssl)
typedef void (*CuteQNetworkAccessFileBackendCall5)(const void *, const QSslConfiguration *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef const QSslConfiguration * (*CuteQNetworkAccessFileBackendCall6)(const void *, int *);
#endif  // QT_CONFIG(ssl)
typedef void (*CuteQNetworkAccessFileBackendCall7)(const void *, int *);
typedef const QByteArrayView * (*CuteQNetworkAccessFileBackendCall8)(const void *, int *);
typedef void (*CuteQNetworkAccessFileBackendCall9)(const void *, qint64, int *);
typedef bool (*CuteQNetworkAccessFileBackendCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessFileBackendCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessFileBackendCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkAccessFileBackend : public QNetworkAccessFileBackend {
public:
  using QNetworkAccessFileBackend::QNetworkAccessFileBackend;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend4openEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend5closeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QNetworkAccessBackend14bytesAvailableEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend4readEPcx")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend5startEv")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend19setSslConfigurationERK17QSslConfiguration")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZNK21QNetworkAccessBackend16sslConfigurationEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend15ignoreSslErrorsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend11readPointerEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend18advanceReadPointerEx")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend10wantToReadEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QNetworkAccessFileBackend::open()
  void open() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall0 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkAccessFileBackend::open();
  }

  //  void QNetworkAccessFileBackend::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall1 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkAccessFileBackend::close();
  }

  //  qint64 QNetworkAccessFileBackend::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall2 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkAccessFileBackend::bytesAvailable();
  }

  //  qint64 QNetworkAccessFileBackend::read(char *data, qint64 maxlen)
  qint64 read(char *data, qint64 maxlen) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall3 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall3>(taken[3]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QNetworkAccessFileBackend::read(data, maxlen);
  }

  //  bool QNetworkAccessBackend::start()
  bool start() override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall4 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkAccessBackend::start();
  }

#if QT_CONFIG(ssl)
  //  void QNetworkAccessBackend::setSslConfiguration(const
  //      QSslConfiguration &configuration)
  void setSslConfiguration(const QSslConfiguration &configuration) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall5 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall5>(taken[5]);
      call(this, &configuration, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::setSslConfiguration(configuration);
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  QSslConfiguration QNetworkAccessBackend::sslConfiguration() const
  QSslConfiguration sslConfiguration() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall6 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall6>(taken[6]);
      const QSslConfiguration * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNetworkAccessBackend::sslConfiguration();
  }
#endif  // QT_CONFIG(ssl)

  //  void QNetworkAccessBackend::ignoreSslErrors()
  void ignoreSslErrors() override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall7 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::ignoreSslErrors();
  }

  //  QByteArrayView QNetworkAccessBackend::readPointer()
  QByteArrayView readPointer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall8 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall8>(taken[8]);
      const QByteArrayView * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNetworkAccessBackend::readPointer();
  }

  //  void QNetworkAccessBackend::advanceReadPointer(qint64 distance)
  void advanceReadPointer(qint64 distance) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall9 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall9>(taken[9]);
      call(this, distance, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::advanceReadPointer(distance);
  }

  //  bool QNetworkAccessBackend::wantToRead()
  bool wantToRead() override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall10 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkAccessBackend::wantToRead();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall11 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall12 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall13 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall14 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall15 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall16 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall17 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkAccessFileBackend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QNetworkAccessFileBackend10metaObjectEv(
    const QNetworkAccessFileBackend *self) {
  return self->metaObject();
}

//  void *QNetworkAccessFileBackend::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QNetworkAccessFileBackend11qt_metacastEPKc(
    QNetworkAccessFileBackend *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNetworkAccessFileBackend::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QNetworkAccessFileBackend11qt_metacallEN11QMetaObject4CallEiPPv(
    QNetworkAccessFileBackend *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if defined(Q_OS_LINUX)
//  QString QNetworkAccessFileBackend::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QNetworkAccessFileBackend2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkAccessFileBackend::tr(s, c, n));
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  QNetworkAccessFileBackend::QNetworkAccessFileBackend()
extern "C" Q_DECL_EXPORT
QNetworkAccessFileBackend *ritual_ZN25QNetworkAccessFileBackendC1Ev() {
  return new CuteQNetworkAccessFileBackend();
}
#endif  // defined(Q_OS_LINUX)

//  QNetworkAccessFileBackend::~QNetworkAccessFileBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNetworkAccessFileBackendD1Ev(
    QNetworkAccessFileBackend *self) {
  delete self;
}

//  void QNetworkAccessFileBackend::open()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNetworkAccessFileBackend4openEv(
    QNetworkAccessFileBackend *self) {
  self->open();
}

//  void QNetworkAccessFileBackend::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNetworkAccessFileBackend5closeEv(
    QNetworkAccessFileBackend *self) {
  self->close();
}

//  qint64 QNetworkAccessFileBackend::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK25QNetworkAccessFileBackend14bytesAvailableEv(
    const QNetworkAccessFileBackend *self) {
  return self->bytesAvailable();
}

//  qint64 QNetworkAccessFileBackend::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN25QNetworkAccessFileBackend4readEPcx(
    QNetworkAccessFileBackend *self,
    char *data,
    qint64 maxlen) {
  return self->read(data, maxlen);
}

//  void QNetworkAccessFileBackend::uploadReadyReadSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNetworkAccessFileBackend19uploadReadyReadSlotEv(
    QNetworkAccessFileBackend *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkAccessFileBackend")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "uploadReadyReadSlot()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "uploadReadyReadSlot()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QNetworkAccessFileBackend::loadFileInfo()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QNetworkAccessFileBackend12loadFileInfoEv(
    QNetworkAccessFileBackend *self) {
  return self->loadFileInfo();
}

//  a Python function taken by a CuteQNetworkAccessFileBackend, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkAccessFileBackend(
    QNetworkAccessFileBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkAccessFileBackend *>(self)->take(key, call);
}

#if defined(Q_OS_LINUX)
//  void QNetworkAccessFileBackend::open()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QNetworkAccessFileBackend4openEv(
    QNetworkAccessFileBackend *self) {
  self->QNetworkAccessFileBackend::open();
}
#endif  // defined(Q_OS_LINUX)

//  void QNetworkAccessFileBackend::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QNetworkAccessFileBackend5closeEv(
    QNetworkAccessFileBackend *self) {
  self->QNetworkAccessFileBackend::close();
}

//  qint64 QNetworkAccessFileBackend::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK25QNetworkAccessFileBackend14bytesAvailableEv(
    const QNetworkAccessFileBackend *self) {
  return self->QNetworkAccessFileBackend::bytesAvailable();
}

//  qint64 QNetworkAccessFileBackend::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN25QNetworkAccessFileBackend4readEPcx(
    QNetworkAccessFileBackend *self,
    char *data,
    qint64 maxlen) {
  return self->QNetworkAccessFileBackend::read(data, maxlen);
}
