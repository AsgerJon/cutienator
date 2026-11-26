//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#include <QtQmlModels/private/qqmldmobjectdata_p.h>
#include <QtQml/private/qv4identifierhash_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4identifierhashdata_p.h>
#include <QtQml/private/qprimefornumbits_p.h>
#include <QtQmlModels/private/qqmldmobjectdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmladaptormodel.cpp, line 13, as _ZN16QQmlAdaptorModel9AccessorsD2Ev
inline QQmlAdaptorModel::Accessors::~Accessors()
{
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 120, as _ZN3QV414IdentifierHashD1Ev
inline QV4::IdentifierHash::~IdentifierHash()
{
    if (d && !d->refCount.deref())
        delete d;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmobjectdata.cpp, line 19, as _ZN16QQmlDMObjectData9initProxyEv
inline QQmlRefPointer<QQmlContextData> QQmlDMObjectData::initProxy()
{
    QQmlRefPointer<QQmlContextData> ctxt = QQmlContextData::createChild(contextData());
    QQDMIncubationTask *it = incubationTask();
    it->proxiedObject = m_modelData;
    it->proxyContext = ctxt;
    ctxt->setContextObject(this);
    // We don't own the proxied object. We need to clear it if it goes away.
    QObject::connect(m_modelData, &QObject::destroyed,
                     this, &QQmlDelegateModelItem::childContextObjectDestroyed);
    return ctxt;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQmlDMObjectData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlDMObjectData10metaObjectEv(
    const QQmlDMObjectData *self) {
  return self->metaObject();
}

//  void *QQmlDMObjectData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQmlDMObjectData11qt_metacastEPKc(
    QQmlDMObjectData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlDMObjectData::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQmlDMObjectData11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlDMObjectData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QObject *QQmlDMObjectData::modelData() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QQmlDMObjectData9modelDataEv(
    const QQmlDMObjectData *self) {
  return self->modelData();
}

//  QQmlRefPointer<QQmlContextData> QQmlDMObjectData::initProxy()
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlContextData> *ritual_ZN16QQmlDMObjectData9initProxyEv(
    QQmlDMObjectData *self) {
  return new QQmlRefPointer<QQmlContextData>(self->initProxy());
}

//  void QQmlDMObjectData::modelDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDMObjectData16modelDataChangedEv(
    QQmlDMObjectData *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlDMObjectData")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "modelDataChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "modelDataChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a QQmlRefPointer<QQmlContextData> a ritual of QQmlDMObjectData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlDMObjectData__QQmlRefPointer_QQmlContextData(
    QQmlRefPointer<QQmlContextData> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
