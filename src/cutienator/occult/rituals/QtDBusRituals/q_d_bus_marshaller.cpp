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
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/private/qdbusargument_p.h>
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/private/qdbusmetatype_p.h>
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

//  from src/dbus/qdbusmarshaller.cpp, line 16, as local:qdbusmarshaller.cpp:qIterAppend
#if !defined(QT_NO_DBUS)
static void qIterAppend(DBusMessageIter *it, QByteArray *ba, int type, const void *arg)
{
    if (ba)
        *ba += char(type);
    else
        q_dbus_message_iter_append_basic(it, type, arg);
}
#endif  // !defined(QT_NO_DBUS)

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

//  from src/dbus/qdbusmarshaller.cpp, line 29, as _ZN15QDBusMarshaller21unregisteredTypeErrorE9QMetaType
#if !defined(QT_NO_DBUS)
inline void QDBusMarshaller::unregisteredTypeError(QMetaType id)
{
    const char *name = id.name();
    qWarning("QDBusMarshaller: type '%s' (%d) is not registered with D-Bus. "
             "Use qDBusRegisterMetaType to register it",
             name ? name : "", id.id());
    error("Unregistered type %1 passed in arguments"_L1
          .arg(QLatin1StringView(id.name())));
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

#if !defined(QT_NO_DBUS)
//  void QDBusMarshaller::unregisteredTypeError(QMetaType t)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusMarshaller21unregisteredTypeErrorE9QMetaType(
    QDBusMarshaller *self,
    const QMetaType *t) {
  self->unregisteredTypeError(*t);
}
#endif  // !defined(QT_NO_DBUS)

#endif  // !defined(QT_NO_DBUS)
