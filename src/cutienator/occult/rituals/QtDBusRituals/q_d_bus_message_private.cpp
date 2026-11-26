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
#include <QtDBus/qdbusmessage.h>
#include <QtDBus/private/qdbusmessage_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstringlist.h>
#include <QtDBus/private/qdbus_symbols_p.h>
#include <QtDBus/private/qdbusargument_p.h>
#include <QtDBus/qdbuserror.h>
#include <QtDBus/qdbusmetatype.h>
#include <QtDBus/private/qdbusconnection_p.h>
#include <QtDBus/private/qdbusutil_p.h>
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

//  from src/dbus/qdbusmessage.cpp, line 34, as local:qdbusmessage.cpp:data
#if !defined(QT_NO_DBUS)
static inline const char *data(const QByteArray &arr)
{
    return arr.isEmpty() ? nullptr : arr.constData();
}
#endif  // !defined(QT_NO_DBUS)

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

//  void QDBusMessagePrivate::setParametersValidated(QDBusMessage &msg, bool
//      enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusMessagePrivate22setParametersValidatedER12QDBusMessageb(
    QDBusMessage *msg,
    bool enable) {
  QDBusMessagePrivate::setParametersValidated(*msg, enable);
}

#if !defined(QT_NO_DBUS)
//  bool QDBusMessagePrivate::isLocal(const QDBusMessage &msg)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QDBusMessagePrivate7isLocalERK12QDBusMessage(
    const QDBusMessage *msg) {
  return QDBusMessagePrivate::isLocal(*msg);
}
#endif  // !defined(QT_NO_DBUS)

#endif  // !defined(QT_NO_DBUS)
