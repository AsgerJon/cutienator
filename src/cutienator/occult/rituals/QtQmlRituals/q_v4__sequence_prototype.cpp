//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

//  QV4::Object
//      *QV4::SequencePrototype::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV417SequencePrototype16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::SequencePrototype::defaultPrototype(e);
}

//  QVariant QV4::SequencePrototype::toVariant(const Sequence *object)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN3QV417SequencePrototype9toVariantEPKNS_8SequenceE(
    const QV4::Sequence *object) {
  return new QVariant(QV4::SequencePrototype::toVariant(object));
}

//  QVariant QV4::SequencePrototype::toVariant(const Value &array, QMetaType
//      targetType)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN3QV417SequencePrototype9toVariantERKNS_5ValueE9QMetaType(
    const QV4::Value *array,
    const QMetaType *targetType) {
  return new QVariant(
      QV4::SequencePrototype::toVariant(
          *array,
          *targetType));
}
