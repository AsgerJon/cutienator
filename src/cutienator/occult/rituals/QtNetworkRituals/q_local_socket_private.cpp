//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qlocalsocket_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(localserver)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qlocalsocket.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qlocalsocket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qlocalsocket.h"
#include "qlocalsocket_p.h"
#include "qnet_unix_p.h"
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <qdir.h>
#include <qdeadlinetimer.h>
#include <qdebug.h>
#include <qstringconverter.h>
#ifdef Q_OS_VXWORKS
#  include <selectLib.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/socket/qlocalsocket_unix.cpp, line 394, as _ZN19QLocalSocketPrivate13parseSockaddrERK11sockaddr_unjR7QStringS4_Rb
inline bool QLocalSocketPrivate::parseSockaddr(const struct ::sockaddr_un &addr,
                                        uint len,
                                        QString &fullServerName,
                                        QString &serverName,
                                        bool &abstractNamespace)
{
    if (len <= offsetof(::sockaddr_un, sun_path))
        return false;
    len -= offsetof(::sockaddr_un, sun_path);
    // check for abstract socket address
    abstractNamespace = PlatformSupportsAbstractNamespace
                                 && (addr.sun_family == PF_UNIX && addr.sun_path[0] == 0);
    QStringDecoder toUtf16(QStringDecoder::System, QStringDecoder::Flag::Stateless);
    // An abstract socket address can be arbitrary binary. To properly handle such a case,
    // we'd have to add new access functions for this very specific case. Instead, we just
    // attempt to decode it according to OS text encoding. If it fails we ignore the result.
    QByteArrayView textData(addr.sun_path + (abstractNamespace ? 1 : 0),
                            len - (abstractNamespace ? 1 : 0));
    QString name = toUtf16(textData);
    if (!name.isEmpty() && !toUtf16.hasError()) {
        //conversion encodes the trailing zeros. So, in case of non-abstract namespace we
        //chop them off as \0 character is not allowed in filenames
        if (!abstractNamespace && (name.at(name.size() - 1) == QChar::fromLatin1('\0'))) {
            int truncPos = name.size() - 1;
            while (truncPos > 0 && name.at(truncPos - 1) == QChar::fromLatin1('\0'))
                truncPos--;
            name.truncate(truncPos);
        }
        fullServerName = name;
        serverName = abstractNamespace
                     ? name
                     : fullServerName.mid(fullServerName.lastIndexOf(u'/') + 1);
        if (serverName.isEmpty())
            serverName = fullServerName;
    }
    return true;
}

//  from src/network/socket/qlocalsocket_unix.cpp, line 432, as _ZN19QLocalSocketPrivate25_q_abortConnectionAttemptEv
inline void QLocalSocketPrivate::_q_abortConnectionAttempt()
{
    Q_Q(QLocalSocket);
    q->close();
}

//  from src/network/socket/qlocalsocket_unix.cpp, line 438, as _ZN19QLocalSocketPrivate20cancelDelayedConnectEv
inline void QLocalSocketPrivate::cancelDelayedConnect()
{
    if (delayConnect) {
        delayConnect->setEnabled(false);
        delete delayConnect;
        delayConnect = nullptr;
        connectTimer->stop();
        delete connectTimer;
        connectTimer = nullptr;
    }
}

//  from src/network/socket/qlocalsocket_unix.cpp, line 374, as _ZN19QLocalSocketPrivate14describeSocketEx
inline void QLocalSocketPrivate::describeSocket(qintptr socketDescriptor)
{
    bool abstractAddress = false;

    struct ::sockaddr_un addr;
    QT_SOCKLEN_T len = sizeof(addr);
    memset(&addr, 0, sizeof(addr));
    const int getpeernameStatus = ::getpeername(socketDescriptor, (sockaddr *)&addr, &len);
    if (getpeernameStatus != 0 || len == offsetof(sockaddr_un, sun_path)) {
        // this is the case when we call it from QLocalServer, then there is no peername
        len = sizeof(addr);
        if (::getsockname(socketDescriptor, (sockaddr *)&addr, &len) != 0)
            return;
    }
    if (parseSockaddr(addr, static_cast<uint>(len), fullServerName, serverName, abstractAddress)) {
        QLocalSocket::SocketOptions options = socketOptions.value();
        socketOptions = options.setFlag(QLocalSocket::AbstractNamespaceOption, abstractAddress);
    }
}
//  -----------------------------------------------------------------------

//  A QLocalSocketPrivate that Python can take functions over in. Every QLocalSocketPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQLocalSocketPrivateCall0)(const void *, char, int *);
typedef const QByteArray * (*CuteQLocalSocketPrivateCall1)(const void *, qint64, int *);
class CuteQLocalSocketPrivate : public QLocalSocketPrivate {
public:
  using QLocalSocketPrivate::QLocalSocketPrivate;
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
      CuteQLocalSocketPrivateCall0 call = reinterpret_cast<CuteQLocalSocketPrivateCall0>(taken[0]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLocalSocketPrivateCall1 call = reinterpret_cast<CuteQLocalSocketPrivateCall1>(taken[1]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QLocalSocket *QLocalSocketPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLocalSocket *ritual_ZN19QLocalSocketPrivate6q_funcEv(
    QLocalSocketPrivate *self) {
  return self->q_func();
}

//  const QLocalSocket *QLocalSocketPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLocalSocket *ritual_ZNK19QLocalSocketPrivate6q_funcEv(
    const QLocalSocketPrivate *self) {
  return self->q_func();
}

#if (!(defined(QT_LOCALSOCKET_TCP))) && (!(defined(Q_OS_WIN)))
//  void QLocalSocketPrivate::_q_abortConnectionAttempt()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLocalSocketPrivate25_q_abortConnectionAttemptEv(
    QLocalSocketPrivate *self) {
  self->_q_abortConnectionAttempt();
}
#endif  // (!(defined(QT_LOCALSOCKET_TCP))) && (!(defined(Q_OS_WIN)))

#if (!(defined(QT_LOCALSOCKET_TCP))) && (!(defined(Q_OS_WIN)))
//  void QLocalSocketPrivate::cancelDelayedConnect()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLocalSocketPrivate20cancelDelayedConnectEv(
    QLocalSocketPrivate *self) {
  self->cancelDelayedConnect();
}
#endif  // (!(defined(QT_LOCALSOCKET_TCP))) && (!(defined(Q_OS_WIN)))

#if (!(defined(QT_LOCALSOCKET_TCP))) && (!(defined(Q_OS_WIN)))
//  void QLocalSocketPrivate::describeSocket(qintptr socketDescriptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLocalSocketPrivate14describeSocketEx(
    QLocalSocketPrivate *self,
    qintptr socketDescriptor) {
  self->describeSocket(socketDescriptor);
}
#endif  // (!(defined(QT_LOCALSOCKET_TCP))) && (!(defined(Q_OS_WIN)))

//  a Python function taken by a CuteQLocalSocketPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLocalSocketPrivate(
    QLocalSocketPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLocalSocketPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(localserver)
