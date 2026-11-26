//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_qnx_backend_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_QNX)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_qnx_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/private/qconnection_qnx_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 9, as _ZN11QnxClientIoC1EP7QObject
inline QnxClientIo::QnxClientIo(QObject *parent)
    : QtROClientIoDevice(parent)
    , m_socket(new QQnxNativeIo(this))
{
    connect(m_socket, &QQnxNativeIo::readyRead, this, &QtROClientIoDevice::readyRead);
    connect(m_socket,
            static_cast<void(QQnxNativeIo::*)(QAbstractSocket::SocketError)>(&QQnxNativeIo::error),
            this,
            &QnxClientIo::onError);
    connect(m_socket, &QQnxNativeIo::stateChanged, this, &QnxClientIo::onStateChanged);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 21, as _ZN11QnxClientIoD1Ev
inline QnxClientIo::~QnxClientIo()
{
    close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 26, as _ZNK11QnxClientIo10connectionEv
inline QIODevice *QnxClientIo::connection() const
{
    return m_socket;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 46, as _ZN11QnxClientIo15connectToServerEv
inline void QnxClientIo::connectToServer()
{
    if (!isOpen())
        m_socket->connectToServer(url().path());
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 52, as _ZNK11QnxClientIo6isOpenEv
inline bool QnxClientIo::isOpen() const
{
    return !isClosing() && (m_socket->state() == QAbstractSocket::ConnectedState
                            || m_socket->state() == QAbstractSocket::ConnectingState);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 31, as _ZN11QnxClientIo7doCloseEv
inline void QnxClientIo::doClose()
{
    if (m_socket->isOpen()) {
        connect(m_socket, &QQnxNativeIo::disconnected, this, &QObject::deleteLater);
        m_socket->disconnectFromServer();
    } else {
        deleteLater();
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 41, as _ZN11QnxClientIo22doDisconnectFromServerEv
inline void QnxClientIo::doDisconnectFromServer()
{
    m_socket->disconnectFromServer();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QnxClientIo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QnxClientIo10metaObjectEv(
    const QnxClientIo *self) {
  return self->metaObject();
}

//  void *QnxClientIo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QnxClientIo11qt_metacastEPKc(
    QnxClientIo *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QnxClientIo::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QnxClientIo11qt_metacallEN11QMetaObject4CallEiPPv(
    QnxClientIo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QnxClientIo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QnxClientIo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QnxClientIo::tr(s, c, n));
}

//  QnxClientIo::QnxClientIo(QObject *parent)
extern "C" Q_DECL_EXPORT
QnxClientIo *ritual_ZN11QnxClientIoC1EP7QObject(QObject *parent) {
  return new QnxClientIo(parent);
}

//  QnxClientIo::~QnxClientIo()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIoD1Ev(QnxClientIo *self) {
  delete self;
}

//  QIODevice *QnxClientIo::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK11QnxClientIo10connectionEv(const QnxClientIo *self) {
  return self->connection();
}

//  void QnxClientIo::connectToServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIo15connectToServerEv(QnxClientIo *self) {
  self->connectToServer();
}

//  bool QnxClientIo::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QnxClientIo6isOpenEv(const QnxClientIo *self) {
  return self->isOpen();
}

//  void QnxClientIo::onError(QAbstractSocket::SocketError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIo7onErrorEN15QAbstractSocket11SocketErrorE(
    QnxClientIo *self,
    QAbstractSocket::SocketError error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QnxClientIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onError(QAbstractSocket::SocketError)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onError(QAbstractSocket::SocketError)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QnxClientIo::onStateChanged(QAbstractSocket::SocketState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIo14onStateChangedEN15QAbstractSocket11SocketStateE(
    QnxClientIo *self,
    QAbstractSocket::SocketState state) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QnxClientIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onStateChanged(QAbstractSocket::SocketState)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onStateChanged(QAbstractSocket::SocketState)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&state)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QnxClientIo::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIo7doCloseEv(QnxClientIo *self) {
  self->doClose();
}

//  void QnxClientIo::doDisconnectFromServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIo22doDisconnectFromServerEv(QnxClientIo *self) {
  self->doDisconnectFromServer();
}

#endif  // defined(Q_OS_QNX)
