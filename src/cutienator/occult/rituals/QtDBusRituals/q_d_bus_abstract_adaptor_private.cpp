//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusabstractadaptor_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/qdbusabstractadaptor.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusabstractadaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdbusabstractadaptor.h"
#include "qdbusabstractadaptor_p.h"
#include <QtCore/qcoreapplication.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qset.h>
#include <QtCore/qthread.h>
#include "qdbusconnection.h"
#include "qdbusconnection_p.h"  // for qDBusParametersForMethod
#include "qdbusmetatype_p.h"
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusabstractadaptor.cpp, line 60, as _ZN27QDBusAbstractAdaptorPrivate24retrieveIntrospectionXmlEP20QDBusAbstractAdaptor
#if !defined(QT_NO_DBUS)
inline QString QDBusAbstractAdaptorPrivate::retrieveIntrospectionXml(QDBusAbstractAdaptor *adaptor)
{
    return adaptor->d_func()->xml;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusabstractadaptor.cpp, line 65, as _ZN27QDBusAbstractAdaptorPrivate20saveIntrospectionXmlEP20QDBusAbstractAdaptorRK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusAbstractAdaptorPrivate::saveIntrospectionXml(QDBusAbstractAdaptor *adaptor,
                                                       const QString &xml)
{
    adaptor->d_func()->xml = xml;
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  QDBusAbstractAdaptor *QDBusAbstractAdaptorPrivate::q_func()
extern "C" Q_DECL_EXPORT
QDBusAbstractAdaptor *ritual_ZN27QDBusAbstractAdaptorPrivate6q_funcEv(
    QDBusAbstractAdaptorPrivate *self) {
  return self->q_func();
}

//  const QDBusAbstractAdaptor *QDBusAbstractAdaptorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDBusAbstractAdaptor *ritual_ZNK27QDBusAbstractAdaptorPrivate6q_funcEv(
    const QDBusAbstractAdaptorPrivate *self) {
  return self->q_func();
}

//  QDBusAbstractAdaptorPrivate::QDBusAbstractAdaptorPrivate()
extern "C" Q_DECL_EXPORT
QDBusAbstractAdaptorPrivate *ritual_ZN27QDBusAbstractAdaptorPrivateC1Ev() {
  return new QDBusAbstractAdaptorPrivate();
}

#if !defined(QT_NO_DBUS)
//  QString QDBusAbstractAdaptorPrivate::retrieveIntrospectionXml(QDBusAbstra
//      ctAdaptor *adaptor)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDBusAbstractAdaptorPrivate24retrieveIntrospectionXmlEP20QDBusAbstractAdaptor(
    QDBusAbstractAdaptor *adaptor) {
  return new QString(
      QDBusAbstractAdaptorPrivate::retrieveIntrospectionXml(
          adaptor));
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void
//      QDBusAbstractAdaptorPrivate::saveIntrospectionXml(QDBusAbstractAdapto
//      r *adaptor, const QString &xml)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDBusAbstractAdaptorPrivate20saveIntrospectionXmlEP20QDBusAbstractAdaptorRK7QString(
    QDBusAbstractAdaptor *adaptor,
    const QString *xml) {
  QDBusAbstractAdaptorPrivate::saveIntrospectionXml(adaptor, *xml);
}
#endif  // !defined(QT_NO_DBUS)

#endif  // !defined(QT_NO_DBUS)
