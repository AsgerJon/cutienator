//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmetaobjectwrapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmetaobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4qmetaobjectwrapper_p.h>
#include <QtQml/private/qqmlobjectorgadget_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4qmetaobjectwrapper.cpp, line 23, as _ZN3QV44Heap18QMetaObjectWrapper7destroyEv
namespace QV4 {
using namespace Qt::StringLiterals;
inline void Heap::QMetaObjectWrapper::destroy()
{
    delete[] m_constructors;
    FunctionObject::destroy();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  const QV4::VTable *QV4::QMetaObjectWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV418QMetaObjectWrapper12staticVTableEv() {
  return QV4::QMetaObjectWrapper::staticVTable();
}

//  void QV4::QMetaObjectWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418QMetaObjectWrapper10__dataTestEv(
    QV4::QMetaObjectWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QMetaObjectWrapper *QV4::QMetaObjectWrapper::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::QMetaObjectWrapper *ritual_ZNK3QV418QMetaObjectWrapper11d_uncheckedEv(
    const QV4::QMetaObjectWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QMetaObjectWrapper *QV4::QMetaObjectWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QMetaObjectWrapper *ritual_ZNK3QV418QMetaObjectWrapper1dEv(
    const QV4::QMetaObjectWrapper *self) {
  return self->d();
}

//  void QV4::QMetaObjectWrapper::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418QMetaObjectWrapper14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::QMetaObjectWrapper::virtualDestroy(b);
}

//  ReturnedValue QV4::QMetaObjectWrapper::create(ExecutionEngine *engine,
//      const QMetaObject *metaObject)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QMetaObjectWrapper6createEPNS_15ExecutionEngineEPK11QMetaObject(
    QV4::ExecutionEngine *engine,
    const QMetaObject *metaObject) {
  return QV4::QMetaObjectWrapper::create(engine, metaObject);
}

//  const QMetaObject *QV4::QMetaObjectWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV418QMetaObjectWrapper10metaObjectEv(
    const QV4::QMetaObjectWrapper *self) {
  return self->metaObject();
}

//  ReturnedValue QV4::QMetaObjectWrapper::virtualCallAsConstructor(const
//      FunctionObject *a0, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QMetaObjectWrapper24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *a0,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::QMetaObjectWrapper::virtualCallAsConstructor(
      a0,
      argv,
      argc,
      a3);
}

//  bool QV4::QMetaObjectWrapper::virtualIsEqualTo(Managed *a, Managed *b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV418QMetaObjectWrapper16virtualIsEqualToEPNS_7ManagedES2_(
    QV4::Managed *a,
    QV4::Managed *b) {
  return QV4::QMetaObjectWrapper::virtualIsEqualTo(a, b);
}

//  void QV4::QMetaObjectWrapper::init(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418QMetaObjectWrapper4initEPNS_15ExecutionEngineE(
    QV4::QMetaObjectWrapper *self,
    QV4::ExecutionEngine *engine) {
  self->init(engine);
}

//  ReturnedValue QV4::QMetaObjectWrapper::constructInternal(const
//      QMetaObject *mo, const QQmlPropertyData *constructors,
//      Heap::FunctionObject *d, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QMetaObjectWrapper17constructInternalEPK11QMetaObjectPK16QQmlPropertyDataPNS_4Heap14FunctionObjectEPKNS_5ValueEi(
    const QMetaObject *mo,
    const QQmlPropertyData *constructors,
    QV4::Heap::FunctionObject *d,
    const QV4::Value *argv,
    int argc) {
  return QV4::QMetaObjectWrapper::constructInternal(
      mo,
      constructors,
      d,
      argv,
      argc);
}
