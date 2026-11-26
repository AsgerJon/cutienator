//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltypenamecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypewrapper_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlmetaobject_p.h>
#include <QtQml/private/qqmltypedata_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypewrapper.cpp, line 33, as _ZN3QV44Heap15QQmlTypeWrapper4initENS1_12TypeNameModeEP7QObjectPK15QQmlTypePrivate
namespace QV4 {
inline void Heap::QQmlTypeWrapper::init(TypeNameMode m, QObject *o, const QQmlTypePrivate *type)
{
    Q_ASSERT(type);
    FunctionObject::init();
    flags = quint8(m) | quint8(Type);
    object.init(o);
    QQmlType::refHandle(type);
    t.typePrivate = type;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmltypewrapper.cpp, line 43, as _ZN3QV44Heap15QQmlTypeWrapper4initENS1_12TypeNameModeEP7QObjectP17QQmlTypeNameCachePK13QQmlImportRef
namespace QV4 {
inline void Heap::QQmlTypeWrapper::init(
        TypeNameMode m, QObject *o, QQmlTypeNameCache *type, const QQmlImportRef *import)
{
    Q_ASSERT(type);
    FunctionObject::init();
    flags = quint8(m) | quint8(Namespace);
    object.init(o);
    n.typeNamespace = type;
    n.typeNamespace->addref();
    n.importNamespace = import;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmltypewrapper.cpp, line 55, as _ZN3QV44Heap15QQmlTypeWrapper7destroyEv
namespace QV4 {
inline void Heap::QQmlTypeWrapper::destroy()
{
    switch (kind()) {
    case Type:
        Q_ASSERT(t.typePrivate);
        QQmlType::derefHandle(t.typePrivate);
        delete[] t.constructors;
        break;
    case Namespace:
        Q_ASSERT(n.typeNamespace);
        n.typeNamespace->release();
        break;
    }

    object.destroy();
    FunctionObject::destroy();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmltypewrapper.cpp, line 73, as _ZNK3QV44Heap15QQmlTypeWrapper4typeEv
namespace QV4 {
inline QQmlType Heap::QQmlTypeWrapper::type() const
{
    switch (kind()) {
    case Type:
        return QQmlType(t.typePrivate);
    case Namespace:
        return QQmlType();
    }

    Q_UNREACHABLE_RETURN(QQmlType());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmltypewrapper.cpp, line 85, as _ZNK3QV44Heap15QQmlTypeWrapper14queryNamespaceEPKNS_6StringEPNS_15ExecutionEngineE
namespace QV4 {
inline QQmlTypeNameCache::Result Heap::QQmlTypeWrapper::queryNamespace(
        const QV4::String *name, QV4::ExecutionEngine *engine) const
{
    Q_ASSERT(kind() == Namespace);
    Q_ASSERT(n.typeNamespace);
    Q_ASSERT(n.importNamespace);
    return n.typeNamespace->query(name, n.importNamespace, engine->typeLoader());

}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::QQmlTypeWrapper::init(TypeNameMode m, QObject *o, const
//      QQmlTypePrivate *type)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15QQmlTypeWrapper4initENS1_12TypeNameModeEP7QObjectPK15QQmlTypePrivate(
    QV4::Heap::QQmlTypeWrapper *self,
    QV4::Heap::QQmlTypeWrapper::TypeNameMode m,
    QObject *o,
    const QQmlTypePrivate *type) {
  self->init(m, o, type);
}

//  void QV4::Heap::QQmlTypeWrapper::init(TypeNameMode m, QObject *o,
//      QQmlTypeNameCache *type, const QQmlImportRef *import)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15QQmlTypeWrapper4initENS1_12TypeNameModeEP7QObjectP17QQmlTypeNameCachePK13QQmlImportRef(
    QV4::Heap::QQmlTypeWrapper *self,
    QV4::Heap::QQmlTypeWrapper::TypeNameMode m,
    QObject *o,
    QQmlTypeNameCache *type,
    const QQmlImportRef *import) {
  self->init(m, o, type, import);
}

//  void QV4::Heap::QQmlTypeWrapper::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15QQmlTypeWrapper7destroyEv(
    QV4::Heap::QQmlTypeWrapper *self) {
  self->destroy();
}

//  const QMetaObject *QV4::Heap::QQmlTypeWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV44Heap15QQmlTypeWrapper10metaObjectEv(
    const QV4::Heap::QQmlTypeWrapper *self) {
  return self->metaObject();
}

//  QMetaType QV4::Heap::QQmlTypeWrapper::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap15QQmlTypeWrapper8metaTypeEv(
    const QV4::Heap::QQmlTypeWrapper *self) {
  return new QMetaType(self->metaType());
}

//  QQmlType QV4::Heap::QQmlTypeWrapper::type() const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK3QV44Heap15QQmlTypeWrapper4typeEv(
    const QV4::Heap::QQmlTypeWrapper *self) {
  return new QQmlType(self->type());
}

//  TypeNameMode QV4::Heap::QQmlTypeWrapper::typeNameMode() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlTypeWrapper::TypeNameMode ritual_ZNK3QV44Heap15QQmlTypeWrapper12typeNameModeEv(
    const QV4::Heap::QQmlTypeWrapper *self) {
  return self->typeNameMode();
}

//  Kind QV4::Heap::QQmlTypeWrapper::kind() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlTypeWrapper::Kind ritual_ZNK3QV44Heap15QQmlTypeWrapper4kindEv(
    const QV4::Heap::QQmlTypeWrapper *self) {
  return self->kind();
}

//  QQmlTypeNameCache::Result
//      QV4::Heap::QQmlTypeWrapper::queryNamespace(const QV4::String *name,
//      QV4::ExecutionEngine *engine) const
extern "C" Q_DECL_EXPORT
QQmlTypeNameCache::Result *ritual_ZNK3QV44Heap15QQmlTypeWrapper14queryNamespaceEPKNS_6StringEPNS_15ExecutionEngineE(
    const QV4::Heap::QQmlTypeWrapper *self,
    const QV4::String *name,
    QV4::ExecutionEngine *engine) {
  return new QQmlTypeNameCache::Result(self->queryNamespace(name, engine));
}
