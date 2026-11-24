//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qprocess_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qprocess.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qprocess_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <QtCore/qdir.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/qprocess.h>
#include <QtCore/private/qprocess_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qcoreapplication.h>
#if __has_include(<paths.h>)
#include <paths.h>
#endif
#include <QtCore/qdebug.h>
#include <QtCore/private/qdebug_p.h>
#include "qplatformdefs.h"
#include <QtCore/qprocess.h>
#include <QtCore/private/qprocess_p.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/private/qcore_unix_p.h>
#include <QtCore/private/qlocking_p.h>
#ifdef Q_OS_DARWIN
#include <QtCore/private/qcore_mac_p.h>
#endif
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qdir.h>
#include <QtCore/qlist.h>
#include <QtCore/qmutex.h>
#include <QtCore/qsocketnotifier.h>
#include <QtCore/qthread.h>
#ifdef Q_OS_QNX
#  include <sys/neutrino.h>
#endif
#include <errno.h>
#include <limits.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>
#include <termios.h>
#include <unistd.h>
#if __has_include(<paths.h>)
#  include <paths.h>
#endif
#if QT_CONFIG(process)
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qprocess.cpp, line 1053, as _ZN15QProcessPrivateD2Ev
#if QT_CONFIG(process)
inline QProcessPrivate::~QProcessPrivate()
{
    if (stdinChannel.process)
        stdinChannel.process->stdoutChannel.clear();
    if (stdoutChannel.process)
        stdoutChannel.process->stdinChannel.clear();
}
#endif  // QT_CONFIG(process)

//  from src/corelib/io/qprocess_unix.cpp, line 622, as _ZNK15QProcessPrivate14commitChannelsEv
#if QT_CONFIG(process)
inline void QProcessPrivate::commitChannels() const
{
    // copy the stdin socket if asked to (without closing on exec)
    if (stdinChannel.pipe[0] != INVALID_Q_PIPE)
        qt_safe_dup2(stdinChannel.pipe[0], STDIN_FILENO, 0);

    // copy the stdout and stderr if asked to
    if (stdoutChannel.pipe[1] != INVALID_Q_PIPE)
        qt_safe_dup2(stdoutChannel.pipe[1], STDOUT_FILENO, 0);
    if (stderrChannel.pipe[1] != INVALID_Q_PIPE) {
        qt_safe_dup2(stderrChannel.pipe[1], STDERR_FILENO, 0);
    } else {
        // merge stdout and stderr if asked to
        if (processChannelMode == QProcess::MergedChannels)
            qt_safe_dup2(STDOUT_FILENO, STDERR_FILENO, 0);
    }
}
#endif  // QT_CONFIG(process)

//  from src/corelib/io/qprocess.cpp, line 1064, as _ZN15QProcessPrivate8setErrorEN8QProcess12ProcessErrorERK7QString
#if QT_CONFIG(process)
inline void QProcessPrivate::setError(QProcess::ProcessError error, const QString &description)
{
    processError = error;
    if (description.isEmpty()) {
        switch (error) {
        case QProcess::FailedToStart:
            errorString = QProcess::tr("Process failed to start");
            break;
        case QProcess::Crashed:
            errorString = QProcess::tr("Process crashed");
            break;
        case QProcess::Timedout:
            errorString = QProcess::tr("Process operation timed out");
            break;
        case QProcess::ReadError:
            errorString = QProcess::tr("Error reading from process");
            break;
        case QProcess::WriteError:
            errorString = QProcess::tr("Error writing to process");
            break;
        case QProcess::UnknownError:
            errorString.clear();
            break;
        }
    } else {
        errorString = description;
    }
}
#endif  // QT_CONFIG(process)

//  from src/corelib/io/qprocess.cpp, line 1096, as _ZN15QProcessPrivate15setErrorAndEmitEN8QProcess12ProcessErrorERK7QString
#if QT_CONFIG(process)
inline void QProcessPrivate::setErrorAndEmit(QProcess::ProcessError error, const QString &description)
{
    Q_Q(QProcess);
    Q_ASSERT(error != QProcess::UnknownError);
    setError(error, description);
    emit q->errorOccurred(QProcess::ProcessError(processError));
}
#endif  // QT_CONFIG(process)
//  -----------------------------------------------------------------------

//  A QProcessPrivate that Python can take functions over in. Every QProcessPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQProcessPrivateCall0)(const void *, char, int *);
typedef const QByteArray * (*CuteQProcessPrivateCall1)(const void *, qint64, int *);
class CuteQProcessPrivate : public QProcessPrivate {
public:
  using QProcessPrivate::QProcessPrivate;
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
      CuteQProcessPrivateCall0 call = reinterpret_cast<CuteQProcessPrivateCall0>(taken[0]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQProcessPrivateCall1 call = reinterpret_cast<CuteQProcessPrivateCall1>(taken[1]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QProcess *QProcessPrivate::q_func()
extern "C" Q_DECL_EXPORT
QProcess *ritual_ZN15QProcessPrivate6q_funcEv(QProcessPrivate *self) {
  return self->q_func();
}

//  const QProcess *QProcessPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QProcess *ritual_ZNK15QProcessPrivate6q_funcEv(
    const QProcessPrivate *self) {
  return self->q_func();
}

//  QProcessPrivate::~QProcessPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProcessPrivateD1Ev(QProcessPrivate *self) {
  delete self;
}

#if defined(Q_OS_UNIX)
#if QT_CONFIG(process)
//  void QProcessPrivate::commitChannels() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QProcessPrivate14commitChannelsEv(
    const QProcessPrivate *self) {
  self->commitChannels();
}
#endif  // QT_CONFIG(process)
#endif  // defined(Q_OS_UNIX)

#if QT_CONFIG(process)
//  void QProcessPrivate::setError(QProcess::ProcessError error, const
//      QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProcessPrivate8setErrorEN8QProcess12ProcessErrorERK7QString(
    QProcessPrivate *self,
    QProcess::ProcessError error,
    const QString *description) {
  self->setError(error, *description);
}
#endif  // QT_CONFIG(process)

#if QT_CONFIG(process)
//  void QProcessPrivate::setErrorAndEmit(QProcess::ProcessError error, const
//      QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProcessPrivate15setErrorAndEmitEN8QProcess12ProcessErrorERK7QString(
    QProcessPrivate *self,
    QProcess::ProcessError error,
    const QString *description) {
  self->setErrorAndEmit(error, *description);
}
#endif  // QT_CONFIG(process)

//  const QProcessEnvironmentPrivate *QProcessPrivate::environmentPrivate()
//      const
extern "C" Q_DECL_EXPORT
const QProcessEnvironmentPrivate *ritual_ZNK15QProcessPrivate18environmentPrivateEv(
    const QProcessPrivate *self) {
  return self->environmentPrivate();
}

//  a Python function taken by a CuteQProcessPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QProcessPrivate(
    QProcessPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQProcessPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#endif  // QT_CONFIG(processenvironment)
