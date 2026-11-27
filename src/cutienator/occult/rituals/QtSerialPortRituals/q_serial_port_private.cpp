//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialPort/6.12.0/QtSerialPort/private/qserialport_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the lines pulling in the headers of Unix,
//  copied from Qt's 'qserialport_unix.cpp', and the code taken from that
//  file stand under the condition its rituals stand under,
//  '(!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))', as Qt builds that
//  file on Unix alone. Edited by hand on 2026-11-27: code taken from Qt's
//  source no longer stands under defined(Q_OS_LINUX), which Qt does not
//  write there. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialPort/qserialport.h>
#include <QtSerialPort/QtSerialPort>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialPort/6.12.0/QtSerialPort/private/qserialport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialPort/qserialport.h>
#include <QtSerialPort/qserialportinfo.h>
#include <QtSerialPort/private/qserialportinfo_p.h>
#include <QtSerialPort/private/qserialport_p.h>
#include <QtCore/qdebug.h>
#include <QtSerialPort/private/qserialport_p.h>
#include <QtSerialPort/private/qserialportinfo_p.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmap.h>
#include <QtCore/qsocketnotifier.h>
#include <QtCore/qstandardpaths.h>
#if (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))
#include <QtCore/private/qcore_unix_p.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/time.h>
#include <unistd.h>
#endif  // (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))
#ifdef Q_OS_MACOS
#if defined(MAC_OS_X_VERSION_10_4) && (MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_4)
#include <IOKit/serial/ioss.h>
#endif
#endif
#ifdef Q_OS_LINUX
# ifdef Q_OS_ANDROID
#  include <android/api-level.h>
# else
# endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtserialport/src/serialport/qserialport.cpp, line 18, as _ZN20QSerialPortErrorInfoC1EN11QSerialPort15SerialPortErrorERK7QString
inline QSerialPortErrorInfo::QSerialPortErrorInfo(QSerialPort::SerialPortError newErrorCode,
                                           const QString &newErrorString)
    : errorCode(newErrorCode)
    , errorString(newErrorString)
{
    if (errorString.isNull()) {
        switch (errorCode) {
        case QSerialPort::NoError:
            errorString = QSerialPort::tr("No error");
            break;
        case QSerialPort::OpenError:
            errorString = QSerialPort::tr("Device is already open");
            break;
        case QSerialPort::NotOpenError:
            errorString = QSerialPort::tr("Device is not open");
            break;
        case QSerialPort::TimeoutError:
            errorString = QSerialPort::tr("Operation timed out");
            break;
        case QSerialPort::ReadError:
            errorString = QSerialPort::tr("Error reading from device");
            break;
        case QSerialPort::WriteError:
            errorString = QSerialPort::tr("Error writing to device");
            break;
        case QSerialPort::ResourceError:
            errorString = QSerialPort::tr("Device disappeared from the system");
            break;
        default:
            // an empty string will be interpreted as "Unknown error"
            // from the QIODevice::errorString()
            break;
        }
    }
}

//  from ../qtserialport/src/serialport/qserialport_unix.cpp, line 1088, as _ZN18QSerialPortPrivate12readFromPortEPcx
#if (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))
inline qint64 QSerialPortPrivate::readFromPort(char *data, qint64 maxSize)
{
    return qt_safe_read(descriptor, data, maxSize);
}
#endif  // (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))

//  from ../qtserialport/src/serialport/qserialport.cpp, line 54, as _ZN18QSerialPortPrivateC1Ev
inline QSerialPortPrivate::QSerialPortPrivate()
#if defined(Q_OS_WIN32)
    : readChunkBuffer(QSERIALPORT_BUFFERSIZE, 0)
#endif
{
    writeBufferChunkSize = QSERIALPORT_BUFFERSIZE;
    readBufferChunkSize = QSERIALPORT_BUFFERSIZE;
}

//  from ../qtserialport/src/serialport/qserialport.cpp, line 63, as _ZN18QSerialPortPrivate8setErrorERK20QSerialPortErrorInfo
inline void QSerialPortPrivate::setError(const QSerialPortErrorInfo &errorInfo)
{
    Q_Q(QSerialPort);

    q->setErrorString(errorInfo.errorString);
    error.setValue(errorInfo.errorCode);
    error.notify();
    emit q->errorOccurred(error);
}

#if (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))
//  from ../qtserialport/src/serialport/qserialport_unix.cpp, line 1020, as _ZNK18QSerialPortPrivate25isReadNotificationEnabledEv
inline bool QSerialPortPrivate::isReadNotificationEnabled() const
{
    return readNotifier && readNotifier->isEnabled();
}

//  from ../qtserialport/src/serialport/qserialport_unix.cpp, line 1037, as _ZNK18QSerialPortPrivate26isWriteNotificationEnabledEv
inline bool QSerialPortPrivate::isWriteNotificationEnabled() const
{
    return writeNotifier && writeNotifier->isEnabled();
}

//  from ../qtserialport/src/serialport/qserialport_unix.cpp, line 1093, as _ZN18QSerialPortPrivate11writeToPortEPKcx
inline qint64 QSerialPortPrivate::writeToPort(const char *data, qint64 maxSize)
{
    qint64 bytesWritten = 0;
#if defined(CMSPAR)
    bytesWritten = qt_safe_write(descriptor, data, maxSize);
#else
    if (parity != QSerialPort::MarkParity
            && parity != QSerialPort::SpaceParity) {
        bytesWritten = qt_safe_write(descriptor, data, maxSize);
    } else {// Perform parity emulation.
        bytesWritten = writePerChar(data, maxSize);
    }
#endif

    return bytesWritten;
}

//  from ../qtserialport/src/serialport/qserialport_unix.cpp, line 876, as _ZN18QSerialPortPrivate15handleExceptionEv
inline void QSerialPortPrivate::handleException()
{
    gotException = true;
}
#endif  // (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))
//  -----------------------------------------------------------------------

//  A QSerialPortPrivate that Python can take functions over in. Every QSerialPortPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSerialPortPrivateCall0)(const void *, char, int *);
typedef const QByteArray * (*CuteQSerialPortPrivateCall1)(const void *, qint64, int *);
class CuteQSerialPortPrivate : public QSerialPortPrivate {
public:
  using QSerialPortPrivate::QSerialPortPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSerialPortPrivateCall0 call = reinterpret_cast<CuteQSerialPortPrivateCall0>(taken[0]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSerialPortPrivateCall1 call = reinterpret_cast<CuteQSerialPortPrivateCall1>(taken[1]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QSerialPort *QSerialPortPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSerialPort *ritual_ZN18QSerialPortPrivate6q_funcEv(
    QSerialPortPrivate *self) {
  return self->q_func();
}

//  const QSerialPort *QSerialPortPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSerialPort *ritual_ZNK18QSerialPortPrivate6q_funcEv(
    const QSerialPortPrivate *self) {
  return self->q_func();
}

//  QSerialPortPrivate::QSerialPortPrivate()
extern "C" Q_DECL_EXPORT
QSerialPortPrivate *ritual_ZN18QSerialPortPrivateC1Ev() {
  return new CuteQSerialPortPrivate();
}

//  void QSerialPortPrivate::setError(const QSerialPortErrorInfo &errorInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSerialPortPrivate8setErrorERK20QSerialPortErrorInfo(
    QSerialPortPrivate *self,
    const QSerialPortErrorInfo *errorInfo) {
  self->setError(*errorInfo);
}

//  void QSerialPortPrivate::setBindableError(QSerialPort::SerialPortError
//      error)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSerialPortPrivate16setBindableErrorEN11QSerialPort15SerialPortErrorE(
    QSerialPortPrivate *self,
    QSerialPort::SerialPortError error) {
  self->setBindableError(error);
}

//  bool QSerialPortPrivate::setBindableDataBits(QSerialPort::DataBits
//      dataBits)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSerialPortPrivate19setBindableDataBitsEN11QSerialPort8DataBitsE(
    QSerialPortPrivate *self,
    QSerialPort::DataBits dataBits) {
  return self->setBindableDataBits(dataBits);
}

//  bool QSerialPortPrivate::setBindableParity(QSerialPort::Parity parity)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSerialPortPrivate17setBindableParityEN11QSerialPort6ParityE(
    QSerialPortPrivate *self,
    QSerialPort::Parity parity) {
  return self->setBindableParity(parity);
}

//  bool QSerialPortPrivate::setBindableStopBits(QSerialPort::StopBits
//      stopBits)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSerialPortPrivate19setBindableStopBitsEN11QSerialPort8StopBitsE(
    QSerialPortPrivate *self,
    QSerialPort::StopBits stopBits) {
  return self->setBindableStopBits(stopBits);
}

//  bool QSerialPortPrivate::setBindableFlowControl(QSerialPort::FlowControl
//      flowControl)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSerialPortPrivate22setBindableFlowControlEN11QSerialPort11FlowControlE(
    QSerialPortPrivate *self,
    QSerialPort::FlowControl flowControl) {
  return self->setBindableFlowControl(flowControl);
}

//  bool QSerialPortPrivate::setBindableBreakEnabled(bool isBreakEnabled)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSerialPortPrivate23setBindableBreakEnabledEb(
    QSerialPortPrivate *self,
    bool isBreakEnabled) {
  return self->setBindableBreakEnabled(isBreakEnabled);
}

#if (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))
//  bool QSerialPortPrivate::isReadNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSerialPortPrivate25isReadNotificationEnabledEv(
    const QSerialPortPrivate *self) {
  return self->isReadNotificationEnabled();
}
#endif  // (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))

#if (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))
//  bool QSerialPortPrivate::isWriteNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSerialPortPrivate26isWriteNotificationEnabledEv(
    const QSerialPortPrivate *self) {
  return self->isWriteNotificationEnabled();
}
#endif  // (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))

#if (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))
//  qint64 QSerialPortPrivate::writeToPort(const char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN18QSerialPortPrivate11writeToPortEPKcx(
    QSerialPortPrivate *self,
    const char *data,
    qint64 maxSize) {
  return self->writeToPort(data, maxSize);
}
#endif  // (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))

#if (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))
//  void QSerialPortPrivate::handleException()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSerialPortPrivate15handleExceptionEv(
    QSerialPortPrivate *self) {
  self->handleException();
}
#endif  // (!(defined(Q_OS_WIN32))) && (defined(Q_OS_UNIX))

//  a Python function taken by a CuteQSerialPortPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSerialPortPrivate(
    QSerialPortPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSerialPortPrivate *>(self)->take(key, call);
}
