//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>

//  QMetaMethodBuilder::QMetaMethodBuilder()
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZN18QMetaMethodBuilderC1Ev() {
  return new QMetaMethodBuilder();
}

//  int QMetaMethodBuilder::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QMetaMethodBuilder5indexEv(const QMetaMethodBuilder *self) {
  return self->index();
}

//  QMetaMethod::MethodType QMetaMethodBuilder::methodType() const
extern "C" Q_DECL_EXPORT
QMetaMethod::MethodType ritual_ZNK18QMetaMethodBuilder10methodTypeEv(
    const QMetaMethodBuilder *self) {
  return self->methodType();
}

//  QByteArray QMetaMethodBuilder::signature() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QMetaMethodBuilder9signatureEv(
    const QMetaMethodBuilder *self) {
  return new QByteArray(self->signature());
}

//  QByteArray QMetaMethodBuilder::returnType() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QMetaMethodBuilder10returnTypeEv(
    const QMetaMethodBuilder *self) {
  return new QByteArray(self->returnType());
}

//  void QMetaMethodBuilder::setReturnType(const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaMethodBuilder13setReturnTypeERK10QByteArray(
    QMetaMethodBuilder *self,
    const QByteArray *value) {
  self->setReturnType(*value);
}

//  QList<QByteArrayView> QMetaMethodBuilder::parameterTypes() const
extern "C" Q_DECL_EXPORT
QList<QByteArrayView> *ritual_ZNK18QMetaMethodBuilder14parameterTypesEv(
    const QMetaMethodBuilder *self) {
  return new QList<QByteArrayView>(self->parameterTypes());
}

//  QList<QByteArray> QMetaMethodBuilder::parameterNames() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK18QMetaMethodBuilder14parameterNamesEv(
    const QMetaMethodBuilder *self) {
  return new QList<QByteArray>(self->parameterNames());
}

//  void QMetaMethodBuilder::setParameterNames(const QList<QByteArray>
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaMethodBuilder17setParameterNamesERK5QListI10QByteArrayE(
    QMetaMethodBuilder *self,
    const QList<QByteArray> *value) {
  self->setParameterNames(*value);
}

//  QByteArray QMetaMethodBuilder::tag() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QMetaMethodBuilder3tagEv(
    const QMetaMethodBuilder *self) {
  return new QByteArray(self->tag());
}

//  void QMetaMethodBuilder::setTag(const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaMethodBuilder6setTagERK10QByteArray(
    QMetaMethodBuilder *self,
    const QByteArray *value) {
  self->setTag(*value);
}

//  QMetaMethod::Access QMetaMethodBuilder::access() const
extern "C" Q_DECL_EXPORT
QMetaMethod::Access ritual_ZNK18QMetaMethodBuilder6accessEv(
    const QMetaMethodBuilder *self) {
  return self->access();
}

//  void QMetaMethodBuilder::setAccess(QMetaMethod::Access value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaMethodBuilder9setAccessEN11QMetaMethod6AccessE(
    QMetaMethodBuilder *self,
    QMetaMethod::Access value) {
  self->setAccess(value);
}

//  int QMetaMethodBuilder::attributes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QMetaMethodBuilder10attributesEv(
    const QMetaMethodBuilder *self) {
  return self->attributes();
}

//  void QMetaMethodBuilder::setAttributes(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaMethodBuilder13setAttributesEi(
    QMetaMethodBuilder *self,
    int value) {
  self->setAttributes(value);
}

//  bool QMetaMethodBuilder::isConst() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QMetaMethodBuilder7isConstEv(
    const QMetaMethodBuilder *self) {
  return self->isConst();
}

//  void QMetaMethodBuilder::setConst(bool methodIsConst)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaMethodBuilder8setConstEb(
    QMetaMethodBuilder *self,
    bool methodIsConst) {
  self->setConst(methodIsConst);
}

//  int QMetaMethodBuilder::revision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QMetaMethodBuilder8revisionEv(
    const QMetaMethodBuilder *self) {
  return self->revision();
}

//  void QMetaMethodBuilder::setRevision(int revision)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaMethodBuilder11setRevisionEi(
    QMetaMethodBuilder *self,
    int revision) {
  self->setRevision(revision);
}

//  QMetaMethodBuilder::QMetaMethodBuilder(const QMetaObjectBuilder *mobj,
//      int index, QMetaMethod::MethodType type)
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZN18QMetaMethodBuilderC1EPK18QMetaObjectBuilderiN11QMetaMethod10MethodTypeE(
    const QMetaObjectBuilder *mobj,
    int index,
    QMetaMethod::MethodType type) {
  return new QMetaMethodBuilder(mobj, index, type);
}

//  QMetaMethodBuilder::~QMetaMethodBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetaMethodBuilderD1Ev(QMetaMethodBuilder *self) {
  delete self;
}
