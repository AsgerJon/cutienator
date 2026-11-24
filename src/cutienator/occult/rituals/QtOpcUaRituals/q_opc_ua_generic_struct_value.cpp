//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuagenericstructvalue.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuagenericstructvalue.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuastructuredefinition.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QOpcUaGenericStructValue::QOpcUaGenericStructValue()
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructValue *ritual_ZN24QOpcUaGenericStructValueC1Ev() {
  return new QOpcUaGenericStructValue();
}

//  QOpcUaGenericStructValue::~QOpcUaGenericStructValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaGenericStructValueD1Ev(
    QOpcUaGenericStructValue *self) {
  delete self;
}

//  QOpcUaGenericStructValue::QOpcUaGenericStructValue(const QString
//      &typeName, const QString &typeId, const QOpcUaStructureDefinition
//      &definition)
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructValue *ritual_ZN24QOpcUaGenericStructValueC1ERK7QStringS2_RK25QOpcUaStructureDefinition(
    const QString *typeName,
    const QString *typeId,
    const QOpcUaStructureDefinition *definition) {
  return new QOpcUaGenericStructValue(*typeName, *typeId, *definition);
}

//  QOpcUaGenericStructValue::QOpcUaGenericStructValue(const QString
//      &typeName, const QString &typeId, const QOpcUaStructureDefinition
//      &definition, const QHash<QString, QVariant> &fields)
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructValue *ritual_ZN24QOpcUaGenericStructValueC1ERK7QStringS2_RK25QOpcUaStructureDefinitionRK5QHashIS0_8QVariantE(
    const QString *typeName,
    const QString *typeId,
    const QOpcUaStructureDefinition *definition,
    const QHash<QString, QVariant> *fields) {
  return new QOpcUaGenericStructValue(
      *typeName,
      *typeId,
      *definition,
      *fields);
}

//  QOpcUaGenericStructValue::QOpcUaGenericStructValue(const
//      QOpcUaGenericStructValue &other)
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructValue *ritual_ZN24QOpcUaGenericStructValueC1ERKS_(
    const QOpcUaGenericStructValue *other) {
  return new QOpcUaGenericStructValue(*other);
}

//  QVariant QOpcUaGenericStructValue::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QOpcUaGenericStructValuecv8QVariantEv(
    const QOpcUaGenericStructValue *self) {
  return new QVariant(self->operator QVariant());
}

//  QString QOpcUaGenericStructValue::typeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QOpcUaGenericStructValue8typeNameEv(
    const QOpcUaGenericStructValue *self) {
  return new QString(self->typeName());
}

//  void QOpcUaGenericStructValue::setTypeName(const QString &typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaGenericStructValue11setTypeNameERK7QString(
    QOpcUaGenericStructValue *self,
    const QString *typeName) {
  self->setTypeName(*typeName);
}

//  QString QOpcUaGenericStructValue::typeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QOpcUaGenericStructValue6typeIdEv(
    const QOpcUaGenericStructValue *self) {
  return new QString(self->typeId());
}

//  void QOpcUaGenericStructValue::setTypeId(const QString &typeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaGenericStructValue9setTypeIdERK7QString(
    QOpcUaGenericStructValue *self,
    const QString *typeId) {
  self->setTypeId(*typeId);
}

//  QOpcUaStructureDefinition QOpcUaGenericStructValue::structureDefinition()
//      const
extern "C" Q_DECL_EXPORT
QOpcUaStructureDefinition *ritual_ZNK24QOpcUaGenericStructValue19structureDefinitionEv(
    const QOpcUaGenericStructValue *self) {
  return new QOpcUaStructureDefinition(self->structureDefinition());
}

//  void QOpcUaGenericStructValue::setStructureDefinition(const
//      QOpcUaStructureDefinition &structureDefinition)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaGenericStructValue22setStructureDefinitionERK25QOpcUaStructureDefinition(
    QOpcUaGenericStructValue *self,
    const QOpcUaStructureDefinition *structureDefinition) {
  self->setStructureDefinition(*structureDefinition);
}

//  QHash<QString, QVariant> QOpcUaGenericStructValue::fields() const
extern "C" Q_DECL_EXPORT
QHash<QString, QVariant> *ritual_ZNK24QOpcUaGenericStructValue6fieldsEv(
    const QOpcUaGenericStructValue *self) {
  return new QHash<QString, QVariant>(self->fields());
}

//  void QOpcUaGenericStructValue::setFields(const QHash<QString, QVariant>
//      &fields)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaGenericStructValue9setFieldsERK5QHashI7QString8QVariantE(
    QOpcUaGenericStructValue *self,
    const QHash<QString, QVariant> *fields) {
  self->setFields(*fields);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QString QOpcUaGenericStructValue::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QOpcUaGenericStructValue8toStringEv(
    const QOpcUaGenericStructValue *self) {
  return new QString(self->toString());
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QOpcUaGenericStructValue &s)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK24QOpcUaGenericStructValue(
    const QDebug *debug,
    const QOpcUaGenericStructValue *s) {
  return new QDebug(operator<<(*debug, *s));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  bool operator==(const QOpcUaGenericStructValue &lhs, const
//      QOpcUaGenericStructValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK24QOpcUaGenericStructValueS1_(
    const QOpcUaGenericStructValue *lhs,
    const QOpcUaGenericStructValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaGenericStructValue &lhs, const
//      QOpcUaGenericStructValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK24QOpcUaGenericStructValueS1_(
    const QOpcUaGenericStructValue *lhs,
    const QOpcUaGenericStructValue *rhs) {
  return operator!=(*lhs, *rhs);
}
