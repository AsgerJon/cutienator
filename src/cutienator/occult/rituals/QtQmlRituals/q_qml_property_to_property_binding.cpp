//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlproperty.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlanybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlpropertytopropertybinding_p.h>
#include <QtQml/private/qqmlanybinding_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/qqmlinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 52, as _ZN29QQmlPropertyToPropertyBindingC1EP10QQmlEngineRK12QQmlProperty
inline QQmlPropertyToPropertyBinding::QQmlPropertyToPropertyBinding(
        QQmlEngine *engine, const QQmlProperty &source)
    : engine(engine)
    , sourceObject(source.object())
    , sourcePropertyIndex(QQmlPropertyPrivate::get(source)->encodedIndex())
{
}
//  -----------------------------------------------------------------------

//  QQmlAnyBinding QQmlPropertyToPropertyBinding::create(QQmlEngine *engine,
//      const QQmlProperty &source, const QQmlProperty &target)
extern "C" Q_DECL_EXPORT
QQmlAnyBinding *ritual_ZN29QQmlPropertyToPropertyBinding6createEP10QQmlEngineRK12QQmlPropertyS4_(
    QQmlEngine *engine,
    const QQmlProperty *source,
    const QQmlProperty *target) {
  return new QQmlAnyBinding(
      QQmlPropertyToPropertyBinding::create(
          engine,
          *source,
          *target));
}

//  QQmlPropertyToPropertyBinding::QQmlPropertyToPropertyBinding(QQmlEngine
//      *engine, const QQmlProperty &source)
extern "C" Q_DECL_EXPORT
QQmlPropertyToPropertyBinding *ritual_ZN29QQmlPropertyToPropertyBindingC1EP10QQmlEngineRK12QQmlProperty(
    QQmlEngine *engine,
    const QQmlProperty *source) {
  return new QQmlPropertyToPropertyBinding(engine, *source);
}

//  void QQmlPropertyToPropertyBinding::doConnectNotify(QQmlNotifierEndpoint
//      *endpoint, const QMetaProperty &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlPropertyToPropertyBinding15doConnectNotifyEP20QQmlNotifierEndpointRK13QMetaProperty(
    QQmlPropertyToPropertyBinding *self,
    QQmlNotifierEndpoint *endpoint,
    const QMetaProperty *property) {
  self->doConnectNotify(endpoint, *property);
}

//  QQmlPropertyToPropertyBinding::~QQmlPropertyToPropertyBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlPropertyToPropertyBindingD1Ev(
    QQmlPropertyToPropertyBinding *self) {
  delete self;
}
