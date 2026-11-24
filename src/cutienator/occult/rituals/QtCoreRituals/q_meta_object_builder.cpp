//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmetatype.h>

//  QMetaObjectBuilder::QMetaObjectBuilder()
extern "C" Q_DECL_EXPORT
QMetaObjectBuilder *ritual_ZN18QMetaObjectBuilderC1Ev() {
  return new QMetaObjectBuilder();
}

//  QMetaObjectBuilder::QMetaObjectBuilder(const QMetaObject *prototype,
//      QMetaObjectBuilder::AddMembers members)
extern "C" Q_DECL_EXPORT
QMetaObjectBuilder *ritual_ZN18QMetaObjectBuilderC1EPK11QMetaObject6QFlagsINS_9AddMemberEE(
    const QMetaObject *prototype,
    int members) {
  return new QMetaObjectBuilder(
      prototype,
      QFlags<QMetaObjectBuilder::AddMember>::fromInt(members));
}

//  QMetaObjectBuilder::~QMetaObjectBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilderD1Ev(QMetaObjectBuilder *self) {
  delete self;
}

//  QByteArray QMetaObjectBuilder::className() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QMetaObjectBuilder9classNameEv(
    const QMetaObjectBuilder *self) {
  return new QByteArray(self->className());
}

//  void QMetaObjectBuilder::setClassName(const QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder12setClassNameERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *name) {
  self->setClassName(*name);
}

//  const QMetaObject *QMetaObjectBuilder::superClass() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QMetaObjectBuilder10superClassEv(
    const QMetaObjectBuilder *self) {
  return self->superClass();
}

//  void QMetaObjectBuilder::setSuperClass(const QMetaObject *meta)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder13setSuperClassEPK11QMetaObject(
    QMetaObjectBuilder *self,
    const QMetaObject *meta) {
  self->setSuperClass(meta);
}

//  MetaObjectFlags QMetaObjectBuilder::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QMetaObjectBuilder5flagsEv(const QMetaObjectBuilder *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QMetaObjectBuilder::setFlags(MetaObjectFlags a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder8setFlagsE6QFlagsIN14QtMocConstants14MetaObjectFlagEE(
    QMetaObjectBuilder *self,
    int a0) {
  self->setFlags(QFlags<QtMocConstants::MetaObjectFlag>::fromInt(a0));
}

//  int QMetaObjectBuilder::methodCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QMetaObjectBuilder11methodCountEv(
    const QMetaObjectBuilder *self) {
  return self->methodCount();
}

//  int QMetaObjectBuilder::constructorCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QMetaObjectBuilder16constructorCountEv(
    const QMetaObjectBuilder *self) {
  return self->constructorCount();
}

//  int QMetaObjectBuilder::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QMetaObjectBuilder13propertyCountEv(
    const QMetaObjectBuilder *self) {
  return self->propertyCount();
}

//  int QMetaObjectBuilder::enumeratorCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QMetaObjectBuilder15enumeratorCountEv(
    const QMetaObjectBuilder *self) {
  return self->enumeratorCount();
}

//  int QMetaObjectBuilder::classInfoCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QMetaObjectBuilder14classInfoCountEv(
    const QMetaObjectBuilder *self) {
  return self->classInfoCount();
}

//  int QMetaObjectBuilder::relatedMetaObjectCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QMetaObjectBuilder22relatedMetaObjectCountEv(
    const QMetaObjectBuilder *self) {
  return self->relatedMetaObjectCount();
}

//  QMetaMethodBuilder QMetaObjectBuilder::addMethod(const QByteArray
//      &signature)
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZN18QMetaObjectBuilder9addMethodERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *signature) {
  return new QMetaMethodBuilder(self->addMethod(*signature));
}

//  QMetaMethodBuilder QMetaObjectBuilder::addMethod(const QByteArray
//      &signature, const QByteArray &returnType)
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZN18QMetaObjectBuilder9addMethodERK10QByteArrayS2_(
    QMetaObjectBuilder *self,
    const QByteArray *signature,
    const QByteArray *returnType) {
  return new QMetaMethodBuilder(self->addMethod(*signature, *returnType));
}

//  QMetaMethodBuilder QMetaObjectBuilder::addMethod(const QMetaMethod
//      &prototype)
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZN18QMetaObjectBuilder9addMethodERK11QMetaMethod(
    QMetaObjectBuilder *self,
    const QMetaMethod *prototype) {
  return new QMetaMethodBuilder(self->addMethod(*prototype));
}

//  QMetaMethodBuilder QMetaObjectBuilder::addSlot(const QByteArray
//      &signature)
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZN18QMetaObjectBuilder7addSlotERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *signature) {
  return new QMetaMethodBuilder(self->addSlot(*signature));
}

//  QMetaMethodBuilder QMetaObjectBuilder::addSignal(const QByteArray
//      &signature)
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZN18QMetaObjectBuilder9addSignalERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *signature) {
  return new QMetaMethodBuilder(self->addSignal(*signature));
}

//  QMetaMethodBuilder QMetaObjectBuilder::addConstructor(const QByteArray
//      &signature)
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZN18QMetaObjectBuilder14addConstructorERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *signature) {
  return new QMetaMethodBuilder(self->addConstructor(*signature));
}

//  QMetaMethodBuilder QMetaObjectBuilder::addConstructor(const QMetaMethod
//      &prototype)
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZN18QMetaObjectBuilder14addConstructorERK11QMetaMethod(
    QMetaObjectBuilder *self,
    const QMetaMethod *prototype) {
  return new QMetaMethodBuilder(self->addConstructor(*prototype));
}

//  QMetaPropertyBuilder QMetaObjectBuilder::addProperty(const QByteArray
//      &name, const QByteArray &type, int notifierId)
extern "C" Q_DECL_EXPORT
QMetaPropertyBuilder *ritual_ZN18QMetaObjectBuilder11addPropertyERK10QByteArrayS2_i(
    QMetaObjectBuilder *self,
    const QByteArray *name,
    const QByteArray *type,
    int notifierId) {
  return new QMetaPropertyBuilder(
      self->addProperty(
          *name,
          *type,
          notifierId));
}

//  QMetaPropertyBuilder QMetaObjectBuilder::addProperty(const QByteArray
//      &name, const QByteArray &type, QMetaType metaType, int notifierId)
extern "C" Q_DECL_EXPORT
QMetaPropertyBuilder *ritual_ZN18QMetaObjectBuilder11addPropertyERK10QByteArrayS2_9QMetaTypei(
    QMetaObjectBuilder *self,
    const QByteArray *name,
    const QByteArray *type,
    const QMetaType *metaType,
    int notifierId) {
  return new QMetaPropertyBuilder(
      self->addProperty(
          *name,
          *type,
          *metaType,
          notifierId));
}

//  QMetaPropertyBuilder QMetaObjectBuilder::addProperty(const QMetaProperty
//      &prototype)
extern "C" Q_DECL_EXPORT
QMetaPropertyBuilder *ritual_ZN18QMetaObjectBuilder11addPropertyERK13QMetaProperty(
    QMetaObjectBuilder *self,
    const QMetaProperty *prototype) {
  return new QMetaPropertyBuilder(self->addProperty(*prototype));
}

//  QMetaEnumBuilder QMetaObjectBuilder::addEnumerator(const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
QMetaEnumBuilder *ritual_ZN18QMetaObjectBuilder13addEnumeratorERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *name) {
  return new QMetaEnumBuilder(self->addEnumerator(*name));
}

//  QMetaEnumBuilder QMetaObjectBuilder::addEnumerator(const QMetaEnum
//      &prototype)
extern "C" Q_DECL_EXPORT
QMetaEnumBuilder *ritual_ZN18QMetaObjectBuilder13addEnumeratorERK9QMetaEnum(
    QMetaObjectBuilder *self,
    const QMetaEnum *prototype) {
  return new QMetaEnumBuilder(self->addEnumerator(*prototype));
}

//  int QMetaObjectBuilder::addClassInfo(const QByteArray &name, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectBuilder12addClassInfoERK10QByteArrayS2_(
    QMetaObjectBuilder *self,
    const QByteArray *name,
    const QByteArray *value) {
  return self->addClassInfo(*name, *value);
}

//  int QMetaObjectBuilder::addRelatedMetaObject(const QMetaObject *meta)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectBuilder20addRelatedMetaObjectEPK11QMetaObject(
    QMetaObjectBuilder *self,
    const QMetaObject *meta) {
  return self->addRelatedMetaObject(meta);
}

//  void QMetaObjectBuilder::addMetaObject(const QMetaObject *prototype,
//      QMetaObjectBuilder::AddMembers members)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder13addMetaObjectEPK11QMetaObject6QFlagsINS_9AddMemberEE(
    QMetaObjectBuilder *self,
    const QMetaObject *prototype,
    int members) {
  self->addMetaObject(
      prototype,
      QFlags<QMetaObjectBuilder::AddMember>::fromInt(members));
}

//  QMetaMethodBuilder QMetaObjectBuilder::method(int index) const
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZNK18QMetaObjectBuilder6methodEi(
    const QMetaObjectBuilder *self,
    int index) {
  return new QMetaMethodBuilder(self->method(index));
}

//  QMetaMethodBuilder QMetaObjectBuilder::signal(int index) const
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZNK18QMetaObjectBuilder6signalEi(
    const QMetaObjectBuilder *self,
    int index) {
  return new QMetaMethodBuilder(self->signal(index));
}

//  QMetaMethodBuilder QMetaObjectBuilder::constructor(int index) const
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZNK18QMetaObjectBuilder11constructorEi(
    const QMetaObjectBuilder *self,
    int index) {
  return new QMetaMethodBuilder(self->constructor(index));
}

//  QMetaPropertyBuilder QMetaObjectBuilder::property(int index) const
extern "C" Q_DECL_EXPORT
QMetaPropertyBuilder *ritual_ZNK18QMetaObjectBuilder8propertyEi(
    const QMetaObjectBuilder *self,
    int index) {
  return new QMetaPropertyBuilder(self->property(index));
}

//  QMetaEnumBuilder QMetaObjectBuilder::enumerator(int index) const
extern "C" Q_DECL_EXPORT
QMetaEnumBuilder *ritual_ZNK18QMetaObjectBuilder10enumeratorEi(
    const QMetaObjectBuilder *self,
    int index) {
  return new QMetaEnumBuilder(self->enumerator(index));
}

//  const QMetaObject *QMetaObjectBuilder::relatedMetaObject(int index) const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QMetaObjectBuilder17relatedMetaObjectEi(
    const QMetaObjectBuilder *self,
    int index) {
  return self->relatedMetaObject(index);
}

//  QByteArray QMetaObjectBuilder::classInfoName(int index) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QMetaObjectBuilder13classInfoNameEi(
    const QMetaObjectBuilder *self,
    int index) {
  return new QByteArray(self->classInfoName(index));
}

//  QByteArray QMetaObjectBuilder::classInfoValue(int index) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QMetaObjectBuilder14classInfoValueEi(
    const QMetaObjectBuilder *self,
    int index) {
  return new QByteArray(self->classInfoValue(index));
}

//  void QMetaObjectBuilder::removeMethod(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder12removeMethodEi(
    QMetaObjectBuilder *self,
    int index) {
  self->removeMethod(index);
}

//  void QMetaObjectBuilder::removeSignal(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder12removeSignalEi(
    QMetaObjectBuilder *self,
    int index) {
  self->removeSignal(index);
}

//  void QMetaObjectBuilder::removeConstructor(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder17removeConstructorEi(
    QMetaObjectBuilder *self,
    int index) {
  self->removeConstructor(index);
}

//  void QMetaObjectBuilder::removeProperty(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder14removePropertyEi(
    QMetaObjectBuilder *self,
    int index) {
  self->removeProperty(index);
}

//  void QMetaObjectBuilder::removeEnumerator(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder16removeEnumeratorEi(
    QMetaObjectBuilder *self,
    int index) {
  self->removeEnumerator(index);
}

//  void QMetaObjectBuilder::removeClassInfo(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder15removeClassInfoEi(
    QMetaObjectBuilder *self,
    int index) {
  self->removeClassInfo(index);
}

//  void QMetaObjectBuilder::removeRelatedMetaObject(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaObjectBuilder23removeRelatedMetaObjectEi(
    QMetaObjectBuilder *self,
    int index) {
  self->removeRelatedMetaObject(index);
}

//  int QMetaObjectBuilder::indexOfMethod(const QByteArray &signature)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectBuilder13indexOfMethodERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *signature) {
  return self->indexOfMethod(*signature);
}

//  int QMetaObjectBuilder::indexOfSignal(const QByteArray &signature)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectBuilder13indexOfSignalERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *signature) {
  return self->indexOfSignal(*signature);
}

//  int QMetaObjectBuilder::indexOfSlot(const QByteArray &signature)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectBuilder11indexOfSlotERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *signature) {
  return self->indexOfSlot(*signature);
}

//  int QMetaObjectBuilder::indexOfConstructor(const QByteArray &signature)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectBuilder18indexOfConstructorERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *signature) {
  return self->indexOfConstructor(*signature);
}

//  int QMetaObjectBuilder::indexOfProperty(const QByteArray &name)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectBuilder15indexOfPropertyERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *name) {
  return self->indexOfProperty(*name);
}

//  int QMetaObjectBuilder::indexOfEnumerator(const QByteArray &name)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectBuilder17indexOfEnumeratorERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *name) {
  return self->indexOfEnumerator(*name);
}

//  int QMetaObjectBuilder::indexOfClassInfo(const QByteArray &name)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QMetaObjectBuilder16indexOfClassInfoERK10QByteArray(
    QMetaObjectBuilder *self,
    const QByteArray *name) {
  return self->indexOfClassInfo(*name);
}

//  QMetaObject *QMetaObjectBuilder::toMetaObject() const
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_ZNK18QMetaObjectBuilder12toMetaObjectEv(
    const QMetaObjectBuilder *self) {
  return self->toMetaObject();
}
