//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuastructuredefinition.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuastructuredefinition.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuastructurefield.h>
#include <QtCore/qlist.h>

//  QOpcUaStructureDefinition::QOpcUaStructureDefinition()
extern "C" Q_DECL_EXPORT
QOpcUaStructureDefinition *ritual_ZN25QOpcUaStructureDefinitionC1Ev() {
  return new QOpcUaStructureDefinition();
}

//  QOpcUaStructureDefinition::QOpcUaStructureDefinition(const
//      QOpcUaStructureDefinition &a0)
extern "C" Q_DECL_EXPORT
QOpcUaStructureDefinition *ritual_ZN25QOpcUaStructureDefinitionC1ERKS_(
    const QOpcUaStructureDefinition *a0) {
  return new QOpcUaStructureDefinition(*a0);
}

//  QVariant QOpcUaStructureDefinition::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QOpcUaStructureDefinitioncv8QVariantEv(
    const QOpcUaStructureDefinition *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaStructureDefinition::~QOpcUaStructureDefinition()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaStructureDefinitionD1Ev(
    QOpcUaStructureDefinition *self) {
  delete self;
}

//  QString QOpcUaStructureDefinition::defaultEncodingId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaStructureDefinition17defaultEncodingIdEv(
    const QOpcUaStructureDefinition *self) {
  return new QString(self->defaultEncodingId());
}

//  void QOpcUaStructureDefinition::setDefaultEncodingId(const QString
//      &defaultEncodingId)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaStructureDefinition20setDefaultEncodingIdERK7QString(
    QOpcUaStructureDefinition *self,
    const QString *defaultEncodingId) {
  self->setDefaultEncodingId(*defaultEncodingId);
}

//  QString QOpcUaStructureDefinition::baseDataType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaStructureDefinition12baseDataTypeEv(
    const QOpcUaStructureDefinition *self) {
  return new QString(self->baseDataType());
}

//  void QOpcUaStructureDefinition::setBaseDataType(const QString
//      &baseDataType)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaStructureDefinition15setBaseDataTypeERK7QString(
    QOpcUaStructureDefinition *self,
    const QString *baseDataType) {
  self->setBaseDataType(*baseDataType);
}

//  QOpcUaStructureDefinition::StructureType
//      QOpcUaStructureDefinition::structureType() const
extern "C" Q_DECL_EXPORT
QOpcUaStructureDefinition::StructureType ritual_ZNK25QOpcUaStructureDefinition13structureTypeEv(
    const QOpcUaStructureDefinition *self) {
  return self->structureType();
}

//  QList<QOpcUaStructureField> QOpcUaStructureDefinition::fields() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaStructureField> *ritual_ZNK25QOpcUaStructureDefinition6fieldsEv(
    const QOpcUaStructureDefinition *self) {
  return new QList<QOpcUaStructureField>(self->fields());
}

//  void QOpcUaStructureDefinition::setFields(const
//      QList<QOpcUaStructureField> &fields)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaStructureDefinition9setFieldsERK5QListI20QOpcUaStructureFieldE(
    QOpcUaStructureDefinition *self,
    const QList<QOpcUaStructureField> *fields) {
  self->setFields(*fields);
}

//  bool operator==(const QOpcUaStructureDefinition &lhs, const
//      QOpcUaStructureDefinition &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK25QOpcUaStructureDefinitionS1_(
    const QOpcUaStructureDefinition *lhs,
    const QOpcUaStructureDefinition *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaStructureDefinition &lhs, const
//      QOpcUaStructureDefinition &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK25QOpcUaStructureDefinitionS1_(
    const QOpcUaStructureDefinition *lhs,
    const QOpcUaStructureDefinition *rhs) {
  return operator!=(*lhs, *rhs);
}
