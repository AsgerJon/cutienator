//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qmetacontainer.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Object
//      *QV4::SequencePrototype::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV417SequencePrototype16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::SequencePrototype::defaultPrototype(e);
}

//  void QV4::SequencePrototype::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417SequencePrototype4initEv(QV4::SequencePrototype *self) {
  self->init();
}

//  ReturnedValue QV4::SequencePrototype::method_valueOf(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417SequencePrototype14method_valueOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::SequencePrototype::method_valueOf(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::SequencePrototype::method_shift(const FunctionObject
//      *b, const Value *thisObject, const Value *a2, int a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417SequencePrototype12method_shiftEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *a2,
    int a3) {
  return QV4::SequencePrototype::method_shift(b, thisObject, a2, a3);
}

//  ReturnedValue QV4::SequencePrototype::method_unshift(const FunctionObject
//      *f, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417SequencePrototype14method_unshiftEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::SequencePrototype::method_unshift(f, thisObject, argv, argc);
}

//  ReturnedValue QV4::SequencePrototype::method_push(const FunctionObject
//      *f, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417SequencePrototype11method_pushEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::SequencePrototype::method_push(f, thisObject, argv, argc);
}

//  ReturnedValue QV4::SequencePrototype::method_pop(const FunctionObject *f,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417SequencePrototype10method_popEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::SequencePrototype::method_pop(f, thisObject, argv, argc);
}

//  ReturnedValue QV4::SequencePrototype::method_getLength(const
//      FunctionObject *b, const Value *thisObject, const Value *a2, int a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417SequencePrototype16method_getLengthEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *a2,
    int a3) {
  return QV4::SequencePrototype::method_getLength(b, thisObject, a2, a3);
}

//  ReturnedValue QV4::SequencePrototype::method_setLength(const
//      FunctionObject *f, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417SequencePrototype16method_setLengthEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::SequencePrototype::method_setLength(f, thisObject, argv, argc);
}

//  ReturnedValue QV4::SequencePrototype::newSequence(QV4::ExecutionEngine
//      *engine, QMetaType type, QMetaSequence metaSequence, const void
//      *data, Heap::Object *object, int propertyIndex,
//      Heap::ReferenceObject::Flags flags)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417SequencePrototype11newSequenceEPNS_15ExecutionEngineE9QMetaType13QMetaSequencePKvPNS_4Heap6ObjectEi6QFlagsINS7_15ReferenceObject4FlagEE(
    QV4::ExecutionEngine *engine,
    const QMetaType *type,
    const QMetaSequence *metaSequence,
    const void *data,
    QV4::Heap::Object *object,
    int propertyIndex,
    int flags) {
  return QV4::SequencePrototype::newSequence(
      engine,
      *type,
      *metaSequence,
      data,
      object,
      propertyIndex,
      QFlags<QV4::Heap::ReferenceObject::Flag>::fromInt(flags));
}

//  ReturnedValue QV4::SequencePrototype::fromVariant(QV4::ExecutionEngine
//      *engine, const QVariant &vd)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417SequencePrototype11fromVariantEPNS_15ExecutionEngineERK8QVariant(
    QV4::ExecutionEngine *engine,
    const QVariant *vd) {
  return QV4::SequencePrototype::fromVariant(engine, *vd);
}

//  ReturnedValue QV4::SequencePrototype::fromData(QV4::ExecutionEngine
//      *engine, QMetaType type, QMetaSequence metaSequence, const void
//      *data)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417SequencePrototype8fromDataEPNS_15ExecutionEngineE9QMetaType13QMetaSequencePKv(
    QV4::ExecutionEngine *engine,
    const QMetaType *type,
    const QMetaSequence *metaSequence,
    const void *data) {
  return QV4::SequencePrototype::fromData(
      engine,
      *type,
      *metaSequence,
      data);
}

//  QMetaType QV4::SequencePrototype::metaTypeForSequence(const Sequence
//      *object)
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZN3QV417SequencePrototype19metaTypeForSequenceEPKNS_8SequenceE(
    const QV4::Sequence *object) {
  return new QMetaType(QV4::SequencePrototype::metaTypeForSequence(object));
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

//  void *QV4::SequencePrototype::rawContainerPtr(const Sequence *sequence,
//      QMetaType typeHint)
extern "C" Q_DECL_EXPORT
void *ritual_ZN3QV417SequencePrototype15rawContainerPtrEPKNS_8SequenceE9QMetaType(
    const QV4::Sequence *sequence,
    const QMetaType *typeHint) {
  return QV4::SequencePrototype::rawContainerPtr(sequence, *typeHint);
}

//  RawCopyResult QV4::SequencePrototype::setRawContainer(Sequence *sequence,
//      const void *container, QMetaType typeHint)
extern "C" Q_DECL_EXPORT
QV4::SequencePrototype::RawCopyResult ritual_ZN3QV417SequencePrototype15setRawContainerEPNS_8SequenceEPKv9QMetaType(
    QV4::Sequence *sequence,
    const void *container,
    const QMetaType *typeHint) {
  return QV4::SequencePrototype::setRawContainer(
      sequence,
      container,
      *typeHint);
}

//  RawCopyResult QV4::SequencePrototype::getRawContainer(const Sequence
//      *sequence, void *container, QMetaType typeHint)
extern "C" Q_DECL_EXPORT
QV4::SequencePrototype::RawCopyResult ritual_ZN3QV417SequencePrototype15getRawContainerEPKNS_8SequenceEPv9QMetaType(
    const QV4::Sequence *sequence,
    void *container,
    const QMetaType *typeHint) {
  return QV4::SequencePrototype::getRawContainer(
      sequence,
      container,
      *typeHint);
}
