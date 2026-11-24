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
#include <QtDBus/qdbusargument.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusargument.h>
#include <QtDBus/private/qdbusargument_p.h>
#include <QtCore/qatomic.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qline.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qrect.h>
#include <QtCore/qtimezone.h>
#include <QtCore/qvariant.h>
#include <QtDBus/private/qdbusmetatype_p.h>
#include <QtDBus/private/qdbusutil_p.h>
#ifndef QT_NO_DBUS
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusargument.cpp, line 99, as _ZN20QDBusArgumentPrivate9checkReadEPS_
#if !defined(QT_NO_DBUS)
inline bool QDBusArgumentPrivate::checkRead(QDBusArgumentPrivate *d)
{
    if (!d)
        return false;
    if (d->direction == Direction::Demarshalling)
        return true;

#ifdef QT_DEBUG
    qFatal("QDBusArgument: read from a write-only object");
#else
    qWarning("QDBusArgument: read from a write-only object");
#endif

    return false;
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  QDBusArgumentPrivate::~QDBusArgumentPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDBusArgumentPrivateD1Ev(QDBusArgumentPrivate *self) {
  delete self;
}

#if !defined(QT_NO_DBUS)
//  bool QDBusArgumentPrivate::checkRead(QDBusArgumentPrivate *d)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QDBusArgumentPrivate9checkReadEPS_(QDBusArgumentPrivate *d) {
  return QDBusArgumentPrivate::checkRead(d);
}
#endif  // !defined(QT_NO_DBUS)

//  QDBusMarshaller *QDBusArgumentPrivate::marshaller()
extern "C" Q_DECL_EXPORT
QDBusMarshaller *ritual_ZN20QDBusArgumentPrivate10marshallerEv(
    QDBusArgumentPrivate *self) {
  return self->marshaller();
}

//  QDBusDemarshaller *QDBusArgumentPrivate::demarshaller()
extern "C" Q_DECL_EXPORT
QDBusDemarshaller *ritual_ZN20QDBusArgumentPrivate12demarshallerEv(
    QDBusArgumentPrivate *self) {
  return self->demarshaller();
}

//  QDBusArgument QDBusArgumentPrivate::create(QDBusArgumentPrivate *d)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN20QDBusArgumentPrivate6createEPS_(
    QDBusArgumentPrivate *d) {
  return new QDBusArgument(QDBusArgumentPrivate::create(d));
}

#endif  // !defined(QT_NO_DBUS)
