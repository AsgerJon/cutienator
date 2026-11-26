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
#include <QtCore/QList>
#include <QtCore/QPointer>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4identifierhash_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4identifierhashdata_p.h>
#include <QtQml/private/qprimefornumbits_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQml/private/qqmlcomponentattached_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlexpression_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlabstracturlinterceptor.h>
#include <QtQml/qjsengine.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qqueue.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 120, as _ZN3QV414IdentifierHashD1Ev
inline QV4::IdentifierHash::~IdentifierHash()
{
    if (d && !d->refCount.deref())
        delete d;
}

//  from ../qtdeclarative/src/qml/qml/qqmlcontext.cpp, line 555, as _ZN18QQmlContextPrivate13context_countEP16QQmlListPropertyI7QObjectE
inline qsizetype QQmlContextPrivate::context_count(QQmlListProperty<QObject> *prop)
{
    QQmlContext *context = static_cast<QQmlContext*>(prop->object);
    QQmlContextPrivate *d = QQmlContextPrivate::get(context);
    int contextProperty = (int)(quintptr)prop->data;

    if (d->propertyValue(contextProperty).userType() != qMetaTypeId<QList<QObject*> >())
        return 0;
    else
        return ((const QList<QObject> *)d->propertyValue(contextProperty).constData())->size();
}

//  from ../qtdeclarative/src/qml/qml/qqmlcontext.cpp, line 567, as _ZN18QQmlContextPrivate10context_atEP16QQmlListPropertyI7QObjectEx
inline QObject *QQmlContextPrivate::context_at(QQmlListProperty<QObject> *prop, qsizetype index)
{
    QQmlContext *context = static_cast<QQmlContext*>(prop->object);
    QQmlContextPrivate *d = QQmlContextPrivate::get(context);
    int contextProperty = (int)(quintptr)prop->data;

    if (d->propertyValue(contextProperty).userType() != qMetaTypeId<QList<QObject*> >())
        return nullptr;
    else
        return ((const QList<QObject*> *)d->propertyValue(contextProperty).constData())->at(index);
}

//  from ../qtdeclarative/src/qml/qml/qqmlcontext.cpp, line 593, as _ZN18QQmlContextPrivate15emitDestructionEv
inline void QQmlContextPrivate::emitDestruction()
{
    m_data->emitDestruction();
}

//  from ../qtdeclarative/src/qml/qml/qqmlcontext.cpp, line 601, as _ZN18QQmlContextPrivateC1EP11QQmlContextRK14QQmlRefPointerI15QQmlContextDataEP10QQmlEngine
inline QQmlContextPrivate::QQmlContextPrivate(
        QQmlContext *publicContext, const QQmlRefPointer<QQmlContextData> &parent,
        QQmlEngine *engine) :
    m_data(new QQmlContextData(QQmlContextData::OwnedByPublicContext, publicContext,
                               parent, engine))
{
    Q_ASSERT(publicContext != nullptr);
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

//  qsizetype QQmlContextPrivate::context_count(QQmlListProperty<QObject>
//      *a0)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN18QQmlContextPrivate13context_countEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *a0) {
  return QQmlContextPrivate::context_count(a0);
}

//  QObject *QQmlContextPrivate::context_at(QQmlListProperty<QObject> *a0,
//      qsizetype a1)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN18QQmlContextPrivate10context_atEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *a0,
    qsizetype a1) {
  return QQmlContextPrivate::context_at(a0, a1);
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

//  QList<QPointer<QObject>> QQmlContextPrivate::instances() const
extern "C" Q_DECL_EXPORT
QList<QPointer<QObject>> *ritual_ZNK18QQmlContextPrivate9instancesEv(
    const QQmlContextPrivate *self) {
  return new QList<QPointer<QObject>>(self->instances());
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

//  QQmlContextPrivate::QQmlContextPrivate(QQmlContext *publicContext, const
//      QQmlRefPointer<QQmlContextData> &parent, QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
QQmlContextPrivate *ritual_ZN18QQmlContextPrivateC1EP11QQmlContextRK14QQmlRefPointerI15QQmlContextDataEP10QQmlEngine(
    QQmlContext *publicContext,
    const QQmlRefPointer<QQmlContextData> *parent,
    QQmlEngine *engine) {
  return new QQmlContextPrivate(publicContext, *parent, engine);
}

//  a QList<QPointer<QObject>> a ritual of QQmlContextPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlContextPrivate__QList_QPointer_QObject(
    QList<QPointer<QObject>> *self) {
  delete self;
}
