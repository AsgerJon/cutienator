//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbuscontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbuscontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/qdbusmessage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdbusmessage.h"
#include "qdbusconnection.h"
#include "qdbusabstractadaptor.h"
#include "qdbuscontext.h"
#include "qdbuscontext_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbuscontext.cpp, line 16, as _ZN19QDBusContextPrivate3setEP7QObjectPS_
#if !defined(QT_NO_DBUS)
inline QDBusContextPrivate *QDBusContextPrivate::set(QObject *obj, QDBusContextPrivate *newContext)
{
    // determine if this is an adaptor or not
    if (qobject_cast<QDBusAbstractAdaptor *>(obj))
        obj = obj->parent();

    Q_ASSERT(obj);

    void *ptr = obj->qt_metacast("QDBusContext");
    QDBusContext *q_ptr = reinterpret_cast<QDBusContext *>(ptr);
    if (q_ptr) {
        QDBusContextPrivate *old = q_ptr->d_ptr;
        q_ptr->d_ptr = newContext;
        return old;
    }

    return nullptr;
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  QDBusContextPrivate::QDBusContextPrivate(const QDBusConnection &conn,
//      const QDBusMessage &msg)
extern "C" Q_DECL_EXPORT
QDBusContextPrivate *ritual_ZN19QDBusContextPrivateC1ERK15QDBusConnectionRK12QDBusMessage(
    const QDBusConnection *conn,
    const QDBusMessage *msg) {
  return new QDBusContextPrivate(*conn, *msg);
}

#if !defined(QT_NO_DBUS)
//  QDBusContextPrivate *QDBusContextPrivate::set(QObject *obj,
//      QDBusContextPrivate *newContext)
extern "C" Q_DECL_EXPORT
QDBusContextPrivate *ritual_ZN19QDBusContextPrivate3setEP7QObjectPS_(
    QObject *obj,
    QDBusContextPrivate *newContext) {
  return QDBusContextPrivate::set(obj, newContext);
}
#endif  // !defined(QT_NO_DBUS)

//  QDBusContextPrivate::~QDBusContextPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusContextPrivateD1Ev(QDBusContextPrivate *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
