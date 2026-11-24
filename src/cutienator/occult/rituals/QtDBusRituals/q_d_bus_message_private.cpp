//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusmessage_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusmessage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdbusmessage.h"
#include "qdbusmessage_p.h"
#include <qdebug.h>
#include <qstringlist.h>
#include "qdbus_symbols_p.h"
#include "qdbusargument_p.h"
#include "qdbuserror.h"
#include "qdbusmetatype.h"
#include "qdbusconnection_p.h"
#include "qdbusutil_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusmessage.cpp, line 39, as _ZN19QDBusMessagePrivateC1Ev
#if !defined(QT_NO_DBUS)
inline QDBusMessagePrivate::QDBusMessagePrivate()
    : localReply(nullptr), ref(1), type(QDBusMessage::InvalidMessage),
      delayedReply(false), parametersValidated(false),
      localMessage(false), autoStartService(true),
      interactiveAuthorizationAllowed(false), isReplyRequired(false)
{
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusmessage.cpp, line 47, as _ZN19QDBusMessagePrivateD1Ev
#if !defined(QT_NO_DBUS)
inline QDBusMessagePrivate::~QDBusMessagePrivate()
{
    delete localReply;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusmessage.cpp, line 52, as _ZN19QDBusMessagePrivate18createResponseLinkEPKS_
#if !defined(QT_NO_DBUS)
inline void QDBusMessagePrivate::createResponseLink(const QDBusMessagePrivate *call)
{
    if (Q_UNLIKELY(call->type != QDBusMessage::MethodCallMessage)) {
        qWarning("QDBusMessage: replying to a message that isn't a method call");
        return;
    }

    if (call->localMessage) {
        localMessage = true;
        call->localReply = new QDBusMessage(*this); // keep an internal copy
    } else {
        serial = call->serial;
        service = call->service;
    }

    // the reply must have a serial or be a local-loop optimization
    Q_ASSERT(serial || localMessage);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusmessage.cpp, line 245, as _ZN19QDBusMessagePrivate7isLocalERK12QDBusMessage
#if !defined(QT_NO_DBUS)
inline bool QDBusMessagePrivate::isLocal(const QDBusMessage &message)
{
    return message.d_ptr->localMessage;
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  QDBusMessagePrivate::QDBusMessagePrivate()
extern "C" Q_DECL_EXPORT
QDBusMessagePrivate *ritual_ZN19QDBusMessagePrivateC1Ev() {
  return new QDBusMessagePrivate();
}

//  QDBusMessagePrivate::~QDBusMessagePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusMessagePrivateD1Ev(QDBusMessagePrivate *self) {
  delete self;
}

#if !defined(QT_NO_DBUS)
//  void QDBusMessagePrivate::createResponseLink(const QDBusMessagePrivate
//      *call)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusMessagePrivate18createResponseLinkEPKS_(
    QDBusMessagePrivate *self,
    const QDBusMessagePrivate *call) {
  self->createResponseLink(call);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  bool QDBusMessagePrivate::isLocal(const QDBusMessage &msg)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QDBusMessagePrivate7isLocalERK12QDBusMessage(
    const QDBusMessage *msg) {
  return QDBusMessagePrivate::isLocal(*msg);
}
#endif  // !defined(QT_NO_DBUS)

#endif  // !defined(QT_NO_DBUS)
