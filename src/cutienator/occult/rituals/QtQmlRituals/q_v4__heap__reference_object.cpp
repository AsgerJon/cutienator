//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::ReferenceObject::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15ReferenceObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::ReferenceObject::markObjects(b, stack);
}

//  void QV4::Heap::ReferenceObject::init(Object *object, int property, Flags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15ReferenceObject4initEPNS0_6ObjectEi6QFlagsINS1_4FlagEE(
    QV4::Heap::ReferenceObject *self,
    QV4::Heap::Object *object,
    int property,
    int flags) {
  self->init(
      object,
      property,
      QFlags<QV4::Heap::ReferenceObject::Flag>::fromInt(flags));
}

//  Flags QV4::Heap::ReferenceObject::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Heap15ReferenceObject5flagsEv(
    const QV4::Heap::ReferenceObject *self) {
  return static_cast<int>(self->flags().toInt());
}

//  Object *QV4::Heap::ReferenceObject::object() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZNK3QV44Heap15ReferenceObject6objectEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->object();
}

//  void QV4::Heap::ReferenceObject::setObject(Object *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15ReferenceObject9setObjectEPNS0_6ObjectE(
    QV4::Heap::ReferenceObject *self,
    QV4::Heap::Object *object) {
  self->setObject(object);
}

//  int QV4::Heap::ReferenceObject::property() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Heap15ReferenceObject8propertyEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->property();
}

//  bool QV4::Heap::ReferenceObject::canWriteBack() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap15ReferenceObject12canWriteBackEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->canWriteBack();
}

//  bool QV4::Heap::ReferenceObject::isVariant() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap15ReferenceObject9isVariantEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->isVariant();
}

//  bool QV4::Heap::ReferenceObject::enforcesLocation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap15ReferenceObject16enforcesLocationEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->enforcesLocation();
}

//  void QV4::Heap::ReferenceObject::setLocation(const Function *function,
//      quint16 statement)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15ReferenceObject11setLocationEPKNS_8FunctionEt(
    QV4::Heap::ReferenceObject *self,
    const QV4::Function *function,
    quint16 statement) {
  self->setLocation(function, statement);
}

//  const Function *QV4::Heap::ReferenceObject::function() const
extern "C" Q_DECL_EXPORT
const QV4::Function *ritual_ZNK3QV44Heap15ReferenceObject8functionEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->function();
}

//  quint16 QV4::Heap::ReferenceObject::statementIndex() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK3QV44Heap15ReferenceObject14statementIndexEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->statementIndex();
}

//  bool QV4::Heap::ReferenceObject::isAttachedToProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap15ReferenceObject20isAttachedToPropertyEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->isAttachedToProperty();
}

//  bool QV4::Heap::ReferenceObject::isReference() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap15ReferenceObject11isReferenceEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->isReference();
}

//  bool QV4::Heap::ReferenceObject::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap15ReferenceObject7isDirtyEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->isDirty();
}

//  void QV4::Heap::ReferenceObject::setDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15ReferenceObject8setDirtyEb(
    QV4::Heap::ReferenceObject *self,
    bool dirty) {
  self->setDirty(dirty);
}

//  bool QV4::Heap::ReferenceObject::isAlwaysDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap15ReferenceObject13isAlwaysDirtyEv(
    const QV4::Heap::ReferenceObject *self) {
  return self->isAlwaysDirty();
}

//  void QV4::Heap::ReferenceObject::setAlwaysDirty(bool alwaysDirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15ReferenceObject14setAlwaysDirtyEb(
    QV4::Heap::ReferenceObject *self,
    bool alwaysDirty) {
  self->setAlwaysDirty(alwaysDirty);
}

//  bool QV4::Heap::ReferenceObject::isConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap15ReferenceObject11isConnectedEv(
    QV4::Heap::ReferenceObject *self) {
  return self->isConnected();
}

//  void QV4::Heap::ReferenceObject::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15ReferenceObject7destroyEv(
    QV4::Heap::ReferenceObject *self) {
  self->destroy();
}

//  bool QV4::Heap::ReferenceObject::hasFlag(Flag flag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap15ReferenceObject7hasFlagENS1_4FlagE(
    const QV4::Heap::ReferenceObject *self,
    QV4::Heap::ReferenceObject::Flag flag) {
  return self->hasFlag(flag);
}

//  void QV4::Heap::ReferenceObject::setFlag(Flag flag, bool set)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15ReferenceObject7setFlagENS1_4FlagEb(
    QV4::Heap::ReferenceObject *self,
    QV4::Heap::ReferenceObject::Flag flag,
    bool set) {
  self->setFlag(flag, set);
}

//  QV4::Heap::ReferenceObject as the QV4::Heap::ReferenceObjectData it is
//      built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ReferenceObjectData *ritual_cast_QV4_Heap_ReferenceObject_QV4_Heap_ReferenceObjectData(
    QV4::Heap::ReferenceObject *self) {
  return static_cast<QV4::Heap::ReferenceObjectData *>(self);
}
