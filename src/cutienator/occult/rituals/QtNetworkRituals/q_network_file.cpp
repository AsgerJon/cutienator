//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkfile_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkfile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qnetworkfile_p.h>
#include <QtNetwork/private/qnetworkrequest_p.h>
#include <QtCore/QDebug>
#include <QtNetwork/QNetworkReply>
#include <QtCore/QDateTime>
#include <QtCore/QFileInfo>
#include <QtCore/QMetaObject>
#include <QtCore/QCoreApplication>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qnetworkfile.cpp, line 53, as _ZN12QNetworkFile5closeEv
inline void QNetworkFile::close()
{
    // This override is needed because 'using' keyword cannot be used for slots. And the base
    // function is not an invokable/slot function.
    QFile::close();
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
