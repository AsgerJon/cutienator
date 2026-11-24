//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessfilebackend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessfilebackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qnetworkaccessfilebackend_p.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qdir.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QDateTime>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 197, as _ZN25QNetworkAccessFileBackend5closeEv
inline void QNetworkAccessFileBackend::close()
{
    if (operation() == QNetworkAccessManager::GetOperation) {
        file.close();
    }
}

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 223, as _ZNK25QNetworkAccessFileBackend14bytesAvailableEv
inline qint64 QNetworkAccessFileBackend::bytesAvailable() const
{
    if (operation() != QNetworkAccessManager::GetOperation)
        return 0;
    return file.bytesAvailable();
}

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
typedef bool (*CuteQNetworkAccessFileBackendCall3)(const void *, int *);
#if QT_CONFIG(ssl)
typedef void (*CuteQNetworkAccessFileBackendCall4)(const void *, const QSslConfiguration *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef const QSslConfiguration * (*CuteQNetworkAccessFileBackendCall5)(const void *, int *);
#endif  // QT_CONFIG(ssl)
typedef void (*CuteQNetworkAccessFileBackendCall6)(const void *, int *);
typedef const QByteArrayView * (*CuteQNetworkAccessFileBackendCall7)(const void *, int *);
typedef void (*CuteQNetworkAccessFileBackendCall8)(const void *, qint64, int *);
typedef bool (*CuteQNetworkAccessFileBackendCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessFileBackendCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessFileBackendCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkAccessFileBackend : public QNetworkAccessFileBackend {
public:
  using QNetworkAccessFileBackend::QNetworkAccessFileBackend;
  void *taken[17] = {};

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
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend5startEv")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend19setSslConfigurationERK17QSslConfiguration")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZNK21QNetworkAccessBackend16sslConfigurationEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend15ignoreSslErrorsEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend11readPointerEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend18advanceReadPointerEx")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend10wantToReadEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
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

  //  bool QNetworkAccessBackend::start()
  bool start() override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall3 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkAccessBackend::start();
  }

#if QT_CONFIG(ssl)
  //  void QNetworkAccessBackend::setSslConfiguration(const
  //      QSslConfiguration &configuration)
  void setSslConfiguration(const QSslConfiguration &configuration) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall4 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall4>(taken[4]);
      call(this, &configuration, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::setSslConfiguration(configuration);
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  QSslConfiguration QNetworkAccessBackend::sslConfiguration() const
  QSslConfiguration sslConfiguration() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall5 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall5>(taken[5]);
      const QSslConfiguration * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNetworkAccessBackend::sslConfiguration();
  }
#endif  // QT_CONFIG(ssl)

  //  void QNetworkAccessBackend::ignoreSslErrors()
  void ignoreSslErrors() override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall6 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::ignoreSslErrors();
  }

  //  QByteArrayView QNetworkAccessBackend::readPointer()
  QByteArrayView readPointer() override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall7 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall7>(taken[7]);
      const QByteArrayView * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNetworkAccessBackend::readPointer();
  }

  //  void QNetworkAccessBackend::advanceReadPointer(qint64 distance)
  void advanceReadPointer(qint64 distance) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall8 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall8>(taken[8]);
      call(this, distance, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::advanceReadPointer(distance);
  }

  //  bool QNetworkAccessBackend::wantToRead()
  bool wantToRead() override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall9 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkAccessBackend::wantToRead();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall10 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall11 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall12 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall13 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall14 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall15 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendCall16 call = reinterpret_cast<CuteQNetworkAccessFileBackendCall16>(taken[16]);
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

//  QNetworkAccessFileBackend::~QNetworkAccessFileBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNetworkAccessFileBackendD1Ev(
    QNetworkAccessFileBackend *self) {
  delete self;
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

//  void QNetworkAccessFileBackend::uploadReadyReadSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNetworkAccessFileBackend19uploadReadyReadSlotEv(
    QNetworkAccessFileBackend *self) {
  self->uploadReadyReadSlot();
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
