//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaenumdefinition.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaenumdefinition.h>
#include <QtCore/qvariant.h>
#include <QtOpcUa/qopcuaenumfield.h>
#include <QtCore/qlist.h>

//  QOpcUaEnumDefinition::QOpcUaEnumDefinition()
extern "C" Q_DECL_EXPORT
QOpcUaEnumDefinition *ritual_ZN20QOpcUaEnumDefinitionC1Ev() {
  return new QOpcUaEnumDefinition();
}

//  QOpcUaEnumDefinition::QOpcUaEnumDefinition(const QOpcUaEnumDefinition
//      &other)
extern "C" Q_DECL_EXPORT
QOpcUaEnumDefinition *ritual_ZN20QOpcUaEnumDefinitionC1ERKS_(
    const QOpcUaEnumDefinition *other) {
  return new QOpcUaEnumDefinition(*other);
}

//  void QOpcUaEnumDefinition::swap(QOpcUaEnumDefinition &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaEnumDefinition4swapERS_(
    QOpcUaEnumDefinition *self,
    QOpcUaEnumDefinition *other) {
  self->swap(*other);
}

//  QOpcUaEnumDefinition
//      &QOpcUaEnumDefinition::operator=(QOpcUaEnumDefinition &&other)
extern "C" Q_DECL_EXPORT
QOpcUaEnumDefinition *ritual_ZN20QOpcUaEnumDefinitionaSEOS_(
    QOpcUaEnumDefinition *self,
    QOpcUaEnumDefinition *other) {
  return &(self->operator=(std::move(*other)));
}

//  QOpcUaEnumDefinition::QOpcUaEnumDefinition(QOpcUaEnumDefinition &&other)
extern "C" Q_DECL_EXPORT
QOpcUaEnumDefinition *ritual_ZN20QOpcUaEnumDefinitionC1EOS_(
    QOpcUaEnumDefinition *other) {
  return new QOpcUaEnumDefinition(std::move(*other));
}

//  QOpcUaEnumDefinition &QOpcUaEnumDefinition::operator=(const
//      QOpcUaEnumDefinition &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaEnumDefinition *ritual_ZN20QOpcUaEnumDefinitionaSERKS_(
    QOpcUaEnumDefinition *self,
    const QOpcUaEnumDefinition *rhs) {
  return &(self->operator=(*rhs));
}

//  QVariant QOpcUaEnumDefinition::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QOpcUaEnumDefinitioncv8QVariantEv(
    const QOpcUaEnumDefinition *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaEnumDefinition::~QOpcUaEnumDefinition()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaEnumDefinitionD1Ev(QOpcUaEnumDefinition *self) {
  delete self;
}

//  QList<QOpcUaEnumField> QOpcUaEnumDefinition::fields() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaEnumField> *ritual_ZNK20QOpcUaEnumDefinition6fieldsEv(
    const QOpcUaEnumDefinition *self) {
  return new QList<QOpcUaEnumField>(self->fields());
}

//  void QOpcUaEnumDefinition::setFields(const QList<QOpcUaEnumField>
//      &fields)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QOpcUaEnumDefinition9setFieldsERK5QListI15QOpcUaEnumFieldE(
    QOpcUaEnumDefinition *self,
    const QList<QOpcUaEnumField> *fields) {
  self->setFields(*fields);
}

//  bool operator==(const QOpcUaEnumDefinition &lhs, const
//      QOpcUaEnumDefinition &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QOpcUaEnumDefinitionS1_(
    const QOpcUaEnumDefinition *lhs,
    const QOpcUaEnumDefinition *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaEnumDefinition &lhs, const
//      QOpcUaEnumDefinition &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QOpcUaEnumDefinitionS1_(
    const QOpcUaEnumDefinition *lhs,
    const QOpcUaEnumDefinition *rhs) {
  return operator!=(*lhs, *rhs);
}
