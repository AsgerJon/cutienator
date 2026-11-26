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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusdemarshaller.cpp, line 14, as local:qdbusdemarshaller.cpp:qIterGet
template <typename T>
static inline T qIterGet(DBusMessageIter *it)
{
    // Use a union of expected and largest type q_dbus_message_iter_get_basic
    // will return to ensure reading the wrong basic type does not result in
    // stack overwrite
    union {
        // The value to be extracted
        T t;
        // Largest type that q_dbus_message_iter_get_basic will return
        // according to dbus_message_iter_get_basic API documentation
        dbus_uint64_t maxValue;
        // A pointer to ensure no stack overwrite in case there is a platform
        // where sizeof(void*) > sizeof(dbus_uint64_t)
        void* ptr;
    } value;

    // Initialize the value in case a narrower type is extracted to it.
    // Note that the result of extracting a narrower type in place of a wider
    // one and vice-versa will be platform-dependent.
    value.t = T();

    q_dbus_message_iter_get_basic(it, &value);
    q_dbus_message_iter_next(it);
    return value.t;
}

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
