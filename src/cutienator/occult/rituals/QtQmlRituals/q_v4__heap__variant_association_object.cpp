//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 2. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4variantassociationobject_p.h>
#include <QtQml/private/qqmlengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4variantassociationobject.cpp, line 114, as _ZN3QV44Heap24VariantAssociationObject4initERK4QMapI7QString8QVariantEPNS0_6ObjectEi6QFlagsINS0_15ReferenceObject4FlagEE
namespace QV4::Heap {
inline void VariantAssociationObject::init(
        const QVariantMap &variantMap, QV4::Heap::Object *container, int property,
        Heap::ReferenceObject::Flags flags)
{
    ReferenceObject::init(container, property, flags);
    m_type = AssociationType::VariantMap;

    if (container)
        new (m_variantAssociation) QVariantMap(variantMap);
    else
        createElementWrappers(variantMap);
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4variantassociationobject.cpp, line 127, as _ZN3QV44Heap24VariantAssociationObject4initERK5QHashI7QString8QVariantEPNS0_6ObjectEi6QFlagsINS0_15ReferenceObject4FlagEE
namespace QV4::Heap {
inline void VariantAssociationObject::init(
        const QVariantHash &variantHash, QV4::Heap::Object *container, int property,
        Heap::ReferenceObject::Flags flags)
{
    ReferenceObject::init(container, property, flags);
    m_type = AssociationType::VariantHash;

    if (container)
        new (m_variantAssociation) QVariantHash(variantHash);
    else
        createElementWrappers(variantHash);
}
}  // namespace QV4::Heap

//  from ../qtdeclarative/src/qml/jsruntime/qv4variantassociationobject.cpp, line 171, as _ZN3QV44Heap24VariantAssociationObject10setVariantERK8QVariant
namespace QV4::Heap {
inline bool VariantAssociationObject::setVariant(const QVariant &variant)
{
    // Should only happen from readReference(). Therefore we are attached.
    Q_ASSERT(object());

    auto metatypeId = variant.metaType().id();

    if (metatypeId != QMetaType::QVariantMap && metatypeId != QMetaType::QVariantHash)
        return false;

    if (metatypeId == QMetaType::QVariantMap && m_type == AssociationType::VariantMap) {
        *reinterpret_cast<QVariantMap *>(&m_variantAssociation) = variant.toMap();
    } else if (metatypeId == QMetaType::QVariantMap && m_type == AssociationType::VariantHash) {
        std::destroy_at(reinterpret_cast<QVariantHash *>(&m_variantAssociation));
        new (m_variantAssociation) QVariantMap(variant.toMap());
        m_type = AssociationType::VariantMap;
    } else if (metatypeId == QMetaType::QVariantHash && m_type == AssociationType::VariantHash) {
        *reinterpret_cast<QVariantHash *>(&m_variantAssociation) = variant.toHash();
    } else if (metatypeId == QMetaType::QVariantHash && m_type == AssociationType::VariantMap) {
        std::destroy_at(reinterpret_cast<QVariantMap *>(&m_variantAssociation));
        new (m_variantAssociation) QVariantHash(variant.toHash());
        m_type = AssociationType::VariantHash;
    }

    return true;
}
}  // namespace QV4::Heap
//  -----------------------------------------------------------------------

//  void QV4::Heap::VariantAssociationObject::markObjects(Heap::Base *b,
//      MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap24VariantAssociationObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::VariantAssociationObject::markObjects(b, stack);
}

//  void QV4::Heap::VariantAssociationObject::init(const QVariantMap
//      &variantMap, QV4::Heap::Object *container, int property,
//      Heap::ReferenceObject::Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap24VariantAssociationObject4initERK4QMapI7QString8QVariantEPNS0_6ObjectEi6QFlagsINS0_15ReferenceObject4FlagEE(
    QV4::Heap::VariantAssociationObject *self,
    const QMap<QString, QVariant> *variantMap,
    QV4::Heap::Object *container,
    int property,
    int flags) {
  self->init(
      *variantMap,
      container,
      property,
      QFlags<QV4::Heap::ReferenceObject::Flag>::fromInt(flags));
}

//  void QV4::Heap::VariantAssociationObject::init(const QVariantHash
//      &variantHash, QV4::Heap::Object *container, int property,
//      Heap::ReferenceObject::Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap24VariantAssociationObject4initERK5QHashI7QString8QVariantEPNS0_6ObjectEi6QFlagsINS0_15ReferenceObject4FlagEE(
    QV4::Heap::VariantAssociationObject *self,
    const QHash<QString, QVariant> *variantHash,
    QV4::Heap::Object *container,
    int property,
    int flags) {
  self->init(
      *variantHash,
      container,
      property,
      QFlags<QV4::Heap::ReferenceObject::Flag>::fromInt(flags));
}

//  void *QV4::Heap::VariantAssociationObject::storagePointer()
extern "C" Q_DECL_EXPORT
void *ritual_ZN3QV44Heap24VariantAssociationObject14storagePointerEv(
    QV4::Heap::VariantAssociationObject *self) {
  return self->storagePointer();
}

//  bool QV4::Heap::VariantAssociationObject::setVariant(const QVariant
//      &variant)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap24VariantAssociationObject10setVariantERK8QVariant(
    QV4::Heap::VariantAssociationObject *self,
    const QVariant *variant) {
  return self->setVariant(*variant);
}

//  QV4::Heap::VariantAssociationObject as the
//      QV4::Heap::VariantAssociationObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::VariantAssociationObjectData *ritual_cast_QV4_Heap_VariantAssociationObject_QV4_Heap_VariantAssociationObjectData(
    QV4::Heap::VariantAssociationObject *self) {
  return static_cast<QV4::Heap::VariantAssociationObjectData *>(self);
}


//  void QV4::Heap::VariantAssociationObject::createElementWrappers<QMap<
//      QString, QVariant>>(const QMap<QString, QVariant> &association)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap24VariantAssociationObject21createElementWrappersI4QMapI7QString8QVariantEEEvRKT_(
    QV4::Heap::VariantAssociationObject *self,
    const QMap<QString, QVariant> *association) {
  self->createElementWrappers<QMap<QString, QVariant>>(*association);
}

//  void QV4::Heap::VariantAssociationObject::createElementWrappers<QHash<
//      QString, QVariant>>(const QHash<QString, QVariant> &association)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap24VariantAssociationObject21createElementWrappersI5QHashI7QString8QVariantEEEvRKT_(
    QV4::Heap::VariantAssociationObject *self,
    const QHash<QString, QVariant> *association) {
  self->createElementWrappers<QHash<QString, QVariant>>(*association);
}
