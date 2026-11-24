//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlprivate.h>
#include <QtQml/qjsprimitivevalue.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>

//  QDateTime QQmlPrivate::AOTCompiledContext::constructDateTime(const
//      QJSPrimitiveValue &arg) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QQmlPrivate18AOTCompiledContext17constructDateTimeERK17QJSPrimitiveValue(
    const QQmlPrivate::AOTCompiledContext *self,
    const QJSPrimitiveValue *arg) {
  return new QDateTime(self->constructDateTime(*arg));
}

//  void
//      QQmlPrivate::AOTCompiledContext::initCallQmlContextPropertyLookup(uin
//      t index, int relativeMethodIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext32initCallQmlContextPropertyLookupEji(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    int relativeMethodIndex) {
  self->initCallQmlContextPropertyLookup(index, relativeMethodIndex);
}

//  void QQmlPrivate::AOTCompiledContext::initCallObjectPropertyLookup(uint
//      index, QObject *object, int relativeMethodIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext28initCallObjectPropertyLookupEjP7QObjecti(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object,
    int relativeMethodIndex) {
  self->initCallObjectPropertyLookup(index, object, relativeMethodIndex);
}

//  void QQmlPrivate::AOTCompiledContext::initLoadGlobalLookup(uint index,
//      QMetaType type) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext20initLoadGlobalLookupEj9QMetaType(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    const QMetaType *type) {
  self->initLoadGlobalLookup(index, *type);
}

//  void
//      QQmlPrivate::AOTCompiledContext::initLoadScopeObjectPropertyLookup(ui
//      nt index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext33initLoadScopeObjectPropertyLookupEj(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index) {
  self->initLoadScopeObjectPropertyLookup(index);
}

//  void QQmlPrivate::AOTCompiledContext::initGetObjectLookup(uint index,
//      QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext19initGetObjectLookupEjP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object) {
  self->initGetObjectLookup(index, object);
}

//  void QQmlPrivate::AOTCompiledContext::initGetValueLookup(uint index,
//      const QMetaObject *metaObject) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext18initGetValueLookupEjPK11QMetaObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    const QMetaObject *metaObject) {
  self->initGetValueLookup(index, metaObject);
}

//  void QQmlPrivate::AOTCompiledContext::initSetObjectLookup(uint index,
//      QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext19initSetObjectLookupEjP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    QObject *object) {
  self->initSetObjectLookup(index, object);
}

//  void QQmlPrivate::AOTCompiledContext::initSetValueLookup(uint index,
//      const QMetaObject *metaObject) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext18initSetValueLookupEjPK11QMetaObject(
    const QQmlPrivate::AOTCompiledContext *self,
    uint index,
    const QMetaObject *metaObject) {
  self->initSetValueLookup(index, metaObject);
}

//  void QQmlPrivate::AOTCompiledContext::setImplicitDestructible(QObject
//      *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23setImplicitDestructibleEP7QObject(
    const QQmlPrivate::AOTCompiledContext *self,
    QObject *object) {
  self->setImplicitDestructible(object);
}

//  void QQmlPrivate::AOTCompiledContext::setImplicitDestructible(const
//      QVariant &variant) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQmlPrivate18AOTCompiledContext23setImplicitDestructibleERK8QVariant(
    const QQmlPrivate::AOTCompiledContext *self,
    const QVariant *variant) {
  self->setImplicitDestructible(*variant);
}

//  QQmlPrivate::AOTCompiledContext::~AOTCompiledContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate18AOTCompiledContextD1Ev(
    QQmlPrivate::AOTCompiledContext *self) {
  delete self;
}
