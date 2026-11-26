//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyfileimpl_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyfileimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qnetworkreplyfileimpl_p.h>
#include "QtCore/qdatetime.h"
#include <QtNetwork/private/qnetworkaccessmanager_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QFileInfo>
#include <QtCore/QThread>
#include <QtNetwork/private/qnetworkfile_p.h>
#include <QtNetwork/qnetworkrequest.h>
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

//  from src/network/access/qnetworkreplyfileimpl.cpp, line 159, as _ZN21QNetworkReplyFileImpl5abortEv
inline void QNetworkReplyFileImpl::abort()
{
    close();
}

//  from src/network/access/qnetworkreplyfileimpl.cpp, line 147, as _ZN21QNetworkReplyFileImpl5closeEv
inline void QNetworkReplyFileImpl::close()
{
    Q_D(QNetworkReplyFileImpl);
    QNetworkReply::close();
    if (d->realFile) {
        if (d->realFile->thread() == thread())
            d->realFile->close();
        else
            QMetaObject::invokeMethod(d->realFile, "close", Qt::QueuedConnection);
    }
}

//  from src/network/access/qnetworkreplyfileimpl.cpp, line 164, as _ZNK21QNetworkReplyFileImpl14bytesAvailableEv
inline qint64 QNetworkReplyFileImpl::bytesAvailable() const
{
    Q_D(const QNetworkReplyFileImpl);
    if (!d->isFinished || !d->realFile || !d->realFile->isOpen())
        return QNetworkReply::bytesAvailable();
    return QNetworkReply::bytesAvailable() + d->realFile->bytesAvailable();
}

//  from src/network/access/qnetworkreplyfileimpl.cpp, line 172, as _ZNK21QNetworkReplyFileImpl12isSequentialEv
inline bool QNetworkReplyFileImpl::isSequential () const
{
    return true;
}

//  from src/network/access/qnetworkreplyfileimpl.cpp, line 177, as _ZNK21QNetworkReplyFileImpl4sizeEv
inline qint64 QNetworkReplyFileImpl::size() const
{
    const auto totalSizeOpt = QNetworkHeadersPrivate::toInt(
            headers().value(QHttpHeaders::WellKnownHeader::ContentLength));
    return totalSizeOpt.value_or(0);
}

//  from src/network/access/qnetworkreplyfileimpl.cpp, line 187, as _ZN21QNetworkReplyFileImpl8readDataEPcx
inline qint64 QNetworkReplyFileImpl::readData(char *data, qint64 maxlen)
{
    Q_D(QNetworkReplyFileImpl);
    if (!d->isFinished || !d->realFile || !d->realFile->isOpen())
        return -1;
    qint64 ret = d->realFile->read(data, maxlen);
    if (bytesAvailable() == 0)
        d->realFile->close();
    if (ret == 0 && bytesAvailable() == 0)
        return -1;
    else {
        setAttribute(QNetworkRequest::HttpStatusCodeAttribute, 200);
        setAttribute(QNetworkRequest::HttpReasonPhraseAttribute, "OK"_L1);
        return ret;
    }
}

//  from src/network/access/qnetworkrequest.cpp, line 1885, as _ZN22QNetworkHeadersPrivate5toIntE14QByteArrayView
inline std::optional<qint64> QNetworkHeadersPrivate::toInt(QByteArrayView value)
{
    if (value.empty())
        return std::nullopt;

    bool ok;
    qint64 res = value.toLongLong(&ok);
    if (ok)
        return res;
    return std::nullopt;
}

//  from src/network/access/qnetworkreplyfileimpl.cpp, line 28, as _ZN21QNetworkReplyFileImplD1Ev
inline QNetworkReplyFileImpl::~QNetworkReplyFileImpl()
{
    QNetworkReplyFileImplPrivate *d = (QNetworkReplyFileImplPrivate*) d_func();
    if (d->realFile) {
        if (d->realFile->thread() == QThread::currentThread())
            delete d->realFile;
        else
            QMetaObject::invokeMethod(d->realFile, "deleteLater", Qt::QueuedConnection);
    }
}
//  -----------------------------------------------------------------------

//  A QNetworkReplyFileImpl that Python can take functions over in. Every QNetworkReplyFileImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNetworkReplyFileImplCall0)(const void *, int *);
typedef void (*CuteQNetworkReplyFileImplCall1)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyFileImplCall2)(const void *, int *);
typedef bool (*CuteQNetworkReplyFileImplCall3)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyFileImplCall4)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyFileImplCall5)(const void *, char *, qint64, int *);
typedef void (*CuteQNetworkReplyFileImplCall6)(const void *, qint64, int *);
typedef void (*CuteQNetworkReplyFileImplCall7)(const void *, int *);
#if QT_CONFIG(ssl)
typedef void (*CuteQNetworkReplyFileImplCall8)(const void *, const QSslConfiguration *, int *);
#endif  // QT_CONFIG(ssl)
typedef bool (*CuteQNetworkReplyFileImplCall9)(const void *, int, int *);
typedef qint64 (*CuteQNetworkReplyFileImplCall10)(const void *, int *);
typedef bool (*CuteQNetworkReplyFileImplCall11)(const void *, qint64, int *);
typedef bool (*CuteQNetworkReplyFileImplCall12)(const void *, int *);
typedef bool (*CuteQNetworkReplyFileImplCall13)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyFileImplCall14)(const void *, int *);
typedef bool (*CuteQNetworkReplyFileImplCall15)(const void *, int *);
typedef bool (*CuteQNetworkReplyFileImplCall16)(const void *, int, int *);
typedef bool (*CuteQNetworkReplyFileImplCall17)(const void *, int, int *);
typedef qint64 (*CuteQNetworkReplyFileImplCall18)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQNetworkReplyFileImplCall19)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkReplyFileImplCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkReplyFileImplCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyFileImplCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyFileImplCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyFileImplCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyFileImplCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyFileImplCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkReplyFileImpl : public QNetworkReplyFileImpl {
public:
  using QNetworkReplyFileImpl::QNetworkReplyFileImpl;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QNetworkReply5abortEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QNetworkReply17setReadBufferSizeEx")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QNetworkReply15ignoreSslErrorsEv")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN13QNetworkReply33setSslConfigurationImplementationERK17QSslConfiguration")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
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

  //  void QNetworkReplyFileImpl::abort()
  void abort() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall0 call = reinterpret_cast<CuteQNetworkReplyFileImplCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReplyFileImpl::abort();
  }

  //  void QNetworkReplyFileImpl::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall1 call = reinterpret_cast<CuteQNetworkReplyFileImplCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReplyFileImpl::close();
  }

  //  qint64 QNetworkReplyFileImpl::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall2 call = reinterpret_cast<CuteQNetworkReplyFileImplCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyFileImpl::bytesAvailable();
  }

  //  bool QNetworkReplyFileImpl::isSequential() const
  bool isSequential() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall3 call = reinterpret_cast<CuteQNetworkReplyFileImplCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyFileImpl::isSequential();
  }

  //  qint64 QNetworkReplyFileImpl::size() const
  qint64 size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall4 call = reinterpret_cast<CuteQNetworkReplyFileImplCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyFileImpl::size();
  }

  //  qint64 QNetworkReplyFileImpl::readData(char *data, qint64 maxlen)
  qint64 readData(char *data, qint64 maxlen) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall5 call = reinterpret_cast<CuteQNetworkReplyFileImplCall5>(taken[5]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QNetworkReplyFileImpl::readData(data, maxlen);
  }

  //  void QNetworkReply::setReadBufferSize(qint64 size)
  void setReadBufferSize(qint64 size) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall6 call = reinterpret_cast<CuteQNetworkReplyFileImplCall6>(taken[6]);
      call(this, size, &handled);
      if (handled) return;
    }
    QNetworkReply::setReadBufferSize(size);
  }

  //  void QNetworkReply::ignoreSslErrors()
  void ignoreSslErrors() override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall7 call = reinterpret_cast<CuteQNetworkReplyFileImplCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReply::ignoreSslErrors();
  }

#if QT_CONFIG(ssl)
  //  void QNetworkReply::setSslConfigurationImplementation(const
  //      QSslConfiguration &a0)
  void setSslConfigurationImplementation(
      const QSslConfiguration &a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall8 call = reinterpret_cast<CuteQNetworkReplyFileImplCall8>(taken[8]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QNetworkReply::setSslConfigurationImplementation(a0);
  }
#endif  // QT_CONFIG(ssl)

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall9 call = reinterpret_cast<CuteQNetworkReplyFileImplCall9>(taken[9]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall10 call = reinterpret_cast<CuteQNetworkReplyFileImplCall10>(taken[10]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall11 call = reinterpret_cast<CuteQNetworkReplyFileImplCall11>(taken[11]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall12 call = reinterpret_cast<CuteQNetworkReplyFileImplCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[13]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall13 call = reinterpret_cast<CuteQNetworkReplyFileImplCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall14 call = reinterpret_cast<CuteQNetworkReplyFileImplCall14>(taken[14]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall15 call = reinterpret_cast<CuteQNetworkReplyFileImplCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[16]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall16 call = reinterpret_cast<CuteQNetworkReplyFileImplCall16>(taken[16]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[17]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall17 call = reinterpret_cast<CuteQNetworkReplyFileImplCall17>(taken[17]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[18]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall18 call = reinterpret_cast<CuteQNetworkReplyFileImplCall18>(taken[18]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QIODevice::readLineData(data, maxlen);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[19]) {
      int handled = 0;
      CuteQNetworkReplyFileImplCall19 call = reinterpret_cast<CuteQNetworkReplyFileImplCall19>(taken[19]);
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
      CuteQNetworkReplyFileImplCall20 call = reinterpret_cast<CuteQNetworkReplyFileImplCall20>(taken[20]);
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
      CuteQNetworkReplyFileImplCall21 call = reinterpret_cast<CuteQNetworkReplyFileImplCall21>(taken[21]);
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
      CuteQNetworkReplyFileImplCall22 call = reinterpret_cast<CuteQNetworkReplyFileImplCall22>(taken[22]);
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
      CuteQNetworkReplyFileImplCall23 call = reinterpret_cast<CuteQNetworkReplyFileImplCall23>(taken[23]);
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
      CuteQNetworkReplyFileImplCall24 call = reinterpret_cast<CuteQNetworkReplyFileImplCall24>(taken[24]);
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
      CuteQNetworkReplyFileImplCall25 call = reinterpret_cast<CuteQNetworkReplyFileImplCall25>(taken[25]);
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
      CuteQNetworkReplyFileImplCall26 call = reinterpret_cast<CuteQNetworkReplyFileImplCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkReplyFileImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QNetworkReplyFileImpl10metaObjectEv(
    const QNetworkReplyFileImpl *self) {
  return self->metaObject();
}

//  void *QNetworkReplyFileImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QNetworkReplyFileImpl11qt_metacastEPKc(
    QNetworkReplyFileImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNetworkReplyFileImpl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QNetworkReplyFileImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QNetworkReplyFileImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QNetworkReplyFileImpl::~QNetworkReplyFileImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyFileImplD1Ev(QNetworkReplyFileImpl *self) {
  delete self;
}

//  void QNetworkReplyFileImpl::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyFileImpl5abortEv(QNetworkReplyFileImpl *self) {
  self->abort();
}

//  void QNetworkReplyFileImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyFileImpl5closeEv(QNetworkReplyFileImpl *self) {
  self->close();
}

//  qint64 QNetworkReplyFileImpl::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QNetworkReplyFileImpl14bytesAvailableEv(
    const QNetworkReplyFileImpl *self) {
  return self->bytesAvailable();
}

//  bool QNetworkReplyFileImpl::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkReplyFileImpl12isSequentialEv(
    const QNetworkReplyFileImpl *self) {
  return self->isSequential();
}

//  qint64 QNetworkReplyFileImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QNetworkReplyFileImpl4sizeEv(
    const QNetworkReplyFileImpl *self) {
  return self->size();
}

//  qint64 QNetworkReplyFileImpl::readData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN21QNetworkReplyFileImpl8readDataEPcx(
    QNetworkReplyFileImpl *self,
    char *data,
    qint64 maxlen) {
  return self->readData(data, maxlen);
}

//  void QNetworkReplyFileImpl::fileOpenFinished(bool isOpen)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyFileImpl16fileOpenFinishedEb(
    QNetworkReplyFileImpl *self,
    bool isOpen) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkReplyFileImpl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fileOpenFinished(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fileOpenFinished(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&isOpen)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QNetworkReplyFileImplPrivate *QNetworkReplyFileImpl::d_func()
extern "C" Q_DECL_EXPORT
QNetworkReplyFileImplPrivate *ritual_ZN21QNetworkReplyFileImpl6d_funcEv(
    QNetworkReplyFileImpl *self) {
  return self->d_func();
}

//  const QNetworkReplyFileImplPrivate *QNetworkReplyFileImpl::d_func() const
extern "C" Q_DECL_EXPORT
const QNetworkReplyFileImplPrivate *ritual_ZNK21QNetworkReplyFileImpl6d_funcEv(
    const QNetworkReplyFileImpl *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQNetworkReplyFileImpl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkReplyFileImpl(
    QNetworkReplyFileImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkReplyFileImpl *>(self)->take(key, call);
}

//  void QNetworkReplyFileImpl::abort()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QNetworkReplyFileImpl5abortEv(
    QNetworkReplyFileImpl *self) {
  self->QNetworkReplyFileImpl::abort();
}

//  void QNetworkReplyFileImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QNetworkReplyFileImpl5closeEv(
    QNetworkReplyFileImpl *self) {
  self->QNetworkReplyFileImpl::close();
}

//  qint64 QNetworkReplyFileImpl::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK21QNetworkReplyFileImpl14bytesAvailableEv(
    const QNetworkReplyFileImpl *self) {
  return self->QNetworkReplyFileImpl::bytesAvailable();
}

//  bool QNetworkReplyFileImpl::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QNetworkReplyFileImpl12isSequentialEv(
    const QNetworkReplyFileImpl *self) {
  return self->QNetworkReplyFileImpl::isSequential();
}

//  qint64 QNetworkReplyFileImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK21QNetworkReplyFileImpl4sizeEv(
    const QNetworkReplyFileImpl *self) {
  return self->QNetworkReplyFileImpl::size();
}

//  qint64 QNetworkReplyFileImpl::readData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN21QNetworkReplyFileImpl8readDataEPcx(
    QNetworkReplyFileImpl *self,
    char *data,
    qint64 maxlen) {
  return self->QNetworkReplyFileImpl::readData(data, maxlen);
}
