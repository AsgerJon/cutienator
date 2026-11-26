//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QV4::Object
//      *QV4::VariantAssociationPrototype::defaultPrototype(QV4::ExecutionEng
//      ine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV427VariantAssociationPrototype16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::VariantAssociationPrototype::defaultPrototype(e);
}

//  ReturnedValue
//      QV4::VariantAssociationPrototype::fromQVariantMap(ExecutionEngine
//      *engine, const QVariantMap &variantMap, QV4::Heap::Object *container,
//      int property, Heap::ReferenceObject::Flags flags)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV427VariantAssociationPrototype15fromQVariantMapEPNS_15ExecutionEngineERK4QMapI7QString8QVariantEPNS_4Heap6ObjectEi6QFlagsINS9_15ReferenceObject4FlagEE(
    QV4::ExecutionEngine *engine,
    const QMap<QString, QVariant> *variantMap,
    QV4::Heap::Object *container,
    int property,
    int flags) {
  return QV4::VariantAssociationPrototype::fromQVariantMap(
      engine,
      *variantMap,
      container,
      property,
      QFlags<QV4::Heap::ReferenceObject::Flag>::fromInt(flags));
}

//  ReturnedValue
//      QV4::VariantAssociationPrototype::fromQVariantHash(ExecutionEngine
//      *engine, const QVariantHash &variantHash, QV4::Heap::Object
//      *container, int property, Heap::ReferenceObject::Flags flags)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV427VariantAssociationPrototype16fromQVariantHashEPNS_15ExecutionEngineERK5QHashI7QString8QVariantEPNS_4Heap6ObjectEi6QFlagsINS9_15ReferenceObject4FlagEE(
    QV4::ExecutionEngine *engine,
    const QHash<QString, QVariant> *variantHash,
    QV4::Heap::Object *container,
    int property,
    int flags) {
  return QV4::VariantAssociationPrototype::fromQVariantHash(
      engine,
      *variantHash,
      container,
      property,
      QFlags<QV4::Heap::ReferenceObject::Flag>::fromInt(flags));
}
