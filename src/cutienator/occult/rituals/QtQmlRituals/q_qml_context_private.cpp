//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlcontext_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlcontext.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmlcontext_p.h"
#include "qqmlcomponentattached_p.h"
#include "qqmlcomponent_p.h"
#include "qqmlexpression_p.h"
#include "qqmlengine_p.h"
#include "qqmlengine.h"
#include "qqmlinfo.h"
#include "qqmlabstracturlinterceptor.h"
#include <qjsengine.h>
#include <QtCore/qvarlengtharray.h>
#include <private/qmetaobject_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qqueue.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlcontext.cpp, line 593, as _ZN18QQmlContextPrivate15emitDestructionEv
inline void QQmlContextPrivate::emitDestruction()
{
    m_data->emitDestruction();
}
//  -----------------------------------------------------------------------

//  QQmlContext *QQmlContextPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZN18QQmlContextPrivate6q_funcEv(
    QQmlContextPrivate *self) {
  return self->q_func();
}

//  const QQmlContext *QQmlContextPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlContext *ritual_ZNK18QQmlContextPrivate6q_funcEv(
    const QQmlContextPrivate *self) {
  return self->q_func();
}

//  QQmlContextPrivate *QQmlContextPrivate::get(QQmlContext *context)
extern "C" Q_DECL_EXPORT
QQmlContextPrivate *ritual_ZN18QQmlContextPrivate3getEP11QQmlContext(
    QQmlContext *context) {
  return QQmlContextPrivate::get(context);
}

//  QQmlContext *QQmlContextPrivate::get(QQmlContextPrivate *context)
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZN18QQmlContextPrivate3getEPS_(
    QQmlContextPrivate *context) {
  return QQmlContextPrivate::get(context);
}

//  int QQmlContextPrivate::notifyIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlContextPrivate11notifyIndexEv(
    const QQmlContextPrivate *self) {
  return self->notifyIndex();
}

//  void QQmlContextPrivate::setNotifyIndex(int notifyIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlContextPrivate14setNotifyIndexEi(
    QQmlContextPrivate *self,
    int notifyIndex) {
  self->setNotifyIndex(notifyIndex);
}

//  int QQmlContextPrivate::numPropertyValues() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlContextPrivate17numPropertyValuesEv(
    const QQmlContextPrivate *self) {
  return self->numPropertyValues();
}

//  void QQmlContextPrivate::appendPropertyValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlContextPrivate19appendPropertyValueERK8QVariant(
    QQmlContextPrivate *self,
    const QVariant *value) {
  self->appendPropertyValue(*value);
}

//  void QQmlContextPrivate::setPropertyValue(int index, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlContextPrivate16setPropertyValueEiRK8QVariant(
    QQmlContextPrivate *self,
    int index,
    const QVariant *value) {
  self->setPropertyValue(index, *value);
}

//  QVariant QQmlContextPrivate::propertyValue(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QQmlContextPrivate13propertyValueEi(
    const QQmlContextPrivate *self,
    int index) {
  return new QVariant(self->propertyValue(index));
}

//  void QQmlContextPrivate::appendInstance(QObject *instance)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlContextPrivate14appendInstanceEP7QObject(
    QQmlContextPrivate *self,
    QObject *instance) {
  self->appendInstance(instance);
}

//  void QQmlContextPrivate::cleanInstances()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlContextPrivate14cleanInstancesEv(
    QQmlContextPrivate *self) {
  self->cleanInstances();
}

//  void QQmlContextPrivate::emitDestruction()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlContextPrivate15emitDestructionEv(
    QQmlContextPrivate *self) {
  self->emitDestruction();
}

//  QQmlContextPrivate::QQmlContextPrivate(QQmlContextData *data)
extern "C" Q_DECL_EXPORT
QQmlContextPrivate *ritual_ZN18QQmlContextPrivateC1EP15QQmlContextData(
    QQmlContextData *data) {
  return new QQmlContextPrivate(data);
}
