//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmllistwrapper_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtQml/private/qqmllist_p.h>
#include <QtQml/private/qv4arrayiterator_p.h>
#include <QtQml/private/qv4arrayobject_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qml/qml/qqmllistwrapper.cpp, line 122, as _ZN3QV44Heap14QmlListWrapper4initEP7QObjecti9QMetaType
namespace QV4 {
using namespace Qt::StringLiterals;
inline void Heap::QmlListWrapper::init(QObject *object, int propertyId, QMetaType propertyType)
{
    Object::init();
    m_object.init(object);
    m_propertyType = propertyType.iface();
    void *args[] = { property(), nullptr };
    QMetaObject::metacall(object, QMetaObject::ReadProperty, propertyId, args);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmllistwrapper.cpp, line 131, as _ZN3QV44Heap14QmlListWrapper4initEP7QObjectRK16QQmlListPropertyIS2_E9QMetaType
namespace QV4 {
using namespace Qt::StringLiterals;
inline void Heap::QmlListWrapper::init(
        QObject *object, const QQmlListProperty<QObject> &list, QMetaType propertyType)
{
    Object::init();
    m_object.init(object);
    m_propertyType = propertyType.iface();
    *property() = list;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmllistwrapper.cpp, line 140, as _ZN3QV44Heap14QmlListWrapper7destroyEv
namespace QV4 {
using namespace Qt::StringLiterals;
inline void Heap::QmlListWrapper::destroy()
{
    m_object.destroy();
    Object::destroy();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::QmlListWrapper::init(QObject *object, int propertyId,
//      QMetaType propertyType)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14QmlListWrapper4initEP7QObjecti9QMetaType(
    QV4::Heap::QmlListWrapper *self,
    QObject *object,
    int propertyId,
    const QMetaType *propertyType) {
  self->init(object, propertyId, *propertyType);
}

//  void QV4::Heap::QmlListWrapper::init(QObject *object, const
//      QQmlListProperty<QObject> &list, QMetaType propertyType)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14QmlListWrapper4initEP7QObjectRK16QQmlListPropertyIS2_E9QMetaType(
    QV4::Heap::QmlListWrapper *self,
    QObject *object,
    const QQmlListProperty<QObject> *list,
    const QMetaType *propertyType) {
  self->init(object, *list, *propertyType);
}

//  void QV4::Heap::QmlListWrapper::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14QmlListWrapper7destroyEv(
    QV4::Heap::QmlListWrapper *self) {
  self->destroy();
}

//  QObject *QV4::Heap::QmlListWrapper::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV44Heap14QmlListWrapper6objectEv(
    const QV4::Heap::QmlListWrapper *self) {
  return self->object();
}

//  QMetaType QV4::Heap::QmlListWrapper::propertyType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap14QmlListWrapper12propertyTypeEv(
    const QV4::Heap::QmlListWrapper *self) {
  return new QMetaType(self->propertyType());
}

//  QMetaType QV4::Heap::QmlListWrapper::elementType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap14QmlListWrapper11elementTypeEv(
    const QV4::Heap::QmlListWrapper *self) {
  return new QMetaType(self->elementType());
}

//  const QQmlListProperty<QObject> *QV4::Heap::QmlListWrapper::property()
//      const
extern "C" Q_DECL_EXPORT
const QQmlListProperty<QObject> *ritual_ZNK3QV44Heap14QmlListWrapper8propertyEv(
    const QV4::Heap::QmlListWrapper *self) {
  return self->property();
}

//  QQmlListProperty<QObject> *QV4::Heap::QmlListWrapper::property()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN3QV44Heap14QmlListWrapper8propertyEv(
    QV4::Heap::QmlListWrapper *self) {
  return self->property();
}
