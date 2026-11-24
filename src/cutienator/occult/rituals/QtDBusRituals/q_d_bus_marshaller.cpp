//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusargument_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusargument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/private/qdbusargument_p.h>
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/private/qdbusmetatype_p.h>
#include <QtDBus/private/qdbusutil_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusmarshaller.cpp, line 336, as _ZN15QDBusMarshaller5errorERK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusMarshaller::error(const QString &msg)
{
    ok = false;
    if (parent)
        parent->error(msg);
    else
        errorString = msg;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusmarshaller.cpp, line 484, as _ZN15QDBusMarshaller20appendRegisteredTypeERK8QVariant
#if !defined(QT_NO_DBUS)
inline bool QDBusMarshaller::appendRegisteredType(const QVariant &arg)
{
    ref.ref();                  // reference up
    QDBusArgument self(QDBusArgumentPrivate::create(this));
    return QDBusMetaType::marshall(self, arg.metaType(), arg.constData());
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

#if !defined(QT_NO_DBUS)
//  void QDBusMarshaller::error(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusMarshaller5errorERK7QString(
    QDBusMarshaller *self,
    const QString *message) {
  self->error(*message);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  bool QDBusMarshaller::appendRegisteredType(const QVariant &arg)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusMarshaller20appendRegisteredTypeERK8QVariant(
    QDBusMarshaller *self,
    const QVariant *arg) {
  return self->appendRegisteredType(*arg);
}
#endif  // !defined(QT_NO_DBUS)

#endif  // !defined(QT_NO_DBUS)
