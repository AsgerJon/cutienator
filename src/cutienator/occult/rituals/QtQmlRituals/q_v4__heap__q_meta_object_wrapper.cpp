//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmetaobjectwrapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmetaobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4qmetaobjectwrapper.cpp, line 17, as _ZN3QV44Heap18QMetaObjectWrapper4initEPK11QMetaObject
namespace QV4 {
using namespace Qt::StringLiterals;
inline void Heap::QMetaObjectWrapper::init(const QMetaObject *metaObject)
{
    FunctionObject::init();
    m_metaObject = metaObject;
}
}  // namespace QV4

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

//  void QV4::Heap::QMetaObjectWrapper::init(const QMetaObject *metaObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap18QMetaObjectWrapper4initEPK11QMetaObject(
    QV4::Heap::QMetaObjectWrapper *self,
    const QMetaObject *metaObject) {
  self->init(metaObject);
}

//  void QV4::Heap::QMetaObjectWrapper::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap18QMetaObjectWrapper7destroyEv(
    QV4::Heap::QMetaObjectWrapper *self) {
  self->destroy();
}

//  const QMetaObject *QV4::Heap::QMetaObjectWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV44Heap18QMetaObjectWrapper10metaObjectEv(
    const QV4::Heap::QMetaObjectWrapper *self) {
  return self->metaObject();
}

//  QMetaType QV4::Heap::QMetaObjectWrapper::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap18QMetaObjectWrapper8metaTypeEv(
    const QV4::Heap::QMetaObjectWrapper *self) {
  return new QMetaType(self->metaType());
}
