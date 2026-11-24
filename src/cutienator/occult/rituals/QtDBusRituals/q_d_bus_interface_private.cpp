//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusinterface_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/qdbusinterface.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdbusinterface.h"
#include "qdbusinterface_p.h"
#include "qdbus_symbols_p.h"
#include <QtCore/qpointer.h>
#include <QtCore/qstringlist.h>
#include "qdbusmetatype_p.h"
#include "qdbusconnection_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusinterface.cpp, line 136, as _ZN21QDBusInterfacePrivateD1Ev
#if !defined(QT_NO_DBUS)
inline QDBusInterfacePrivate::~QDBusInterfacePrivate()
{
    if (metaObject && !metaObject->cached)
        delete metaObject;
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  QDBusInterface *QDBusInterfacePrivate::q_func()
extern "C" Q_DECL_EXPORT
QDBusInterface *ritual_ZN21QDBusInterfacePrivate6q_funcEv(
    QDBusInterfacePrivate *self) {
  return self->q_func();
}

//  const QDBusInterface *QDBusInterfacePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDBusInterface *ritual_ZNK21QDBusInterfacePrivate6q_funcEv(
    const QDBusInterfacePrivate *self) {
  return self->q_func();
}

//  QDBusInterfacePrivate::~QDBusInterfacePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusInterfacePrivateD1Ev(QDBusInterfacePrivate *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
