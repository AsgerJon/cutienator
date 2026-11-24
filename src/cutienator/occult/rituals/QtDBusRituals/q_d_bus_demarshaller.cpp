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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdbusargument.h"
#include "qdbusargument_p.h"
#include <qatomic.h>
#include <qbytearray.h>
#include <qdatetime.h>
#include <qline.h>
#include <qlist.h>
#include <qmap.h>
#include <qstring.h>
#include <qstringlist.h>
#include <qrect.h>
#include <qtimezone.h>
#include <qvariant.h>
#include "qdbusmetatype_p.h"
#include "qdbusutil_p.h"
#ifndef QT_NO_DBUS
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusargument.cpp, line 29, as _ZN20QDBusArgumentPrivateD2Ev
#if !defined(QT_NO_DBUS)
inline QDBusArgumentPrivate::~QDBusArgumentPrivate()
{
    if (message)
        q_dbus_message_unref(message);
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  void QDBusDemarshaller::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusDemarshaller5closeEv(QDBusDemarshaller *self) {
  self->close();
}

#endif  // !defined(QT_NO_DBUS)
