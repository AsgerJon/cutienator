//  Written by dev_tooling.RitualGenerator from the records of
//  QtUiTools/6.12.0/QtUiTools/private/quiloader_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtUiTools/QtUiTools>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtUiTools/6.12.0/QtUiTools/private/quiloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>

//  QByteArray QUiTranslatableStringValue::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK26QUiTranslatableStringValue5valueEv(
    const QUiTranslatableStringValue *self) {
  return new QByteArray(self->value());
}

//  void QUiTranslatableStringValue::setValue(const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QUiTranslatableStringValue8setValueERK10QByteArray(
    QUiTranslatableStringValue *self,
    const QByteArray *value) {
  self->setValue(*value);
}

//  QByteArray QUiTranslatableStringValue::qualifier() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK26QUiTranslatableStringValue9qualifierEv(
    const QUiTranslatableStringValue *self) {
  return new QByteArray(self->qualifier());
}

//  void QUiTranslatableStringValue::setQualifier(const QByteArray
//      &qualifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QUiTranslatableStringValue12setQualifierERK10QByteArray(
    QUiTranslatableStringValue *self,
    const QByteArray *qualifier) {
  self->setQualifier(*qualifier);
}

//  QString QUiTranslatableStringValue::translate(const QByteArray
//      &className, bool idBased) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QUiTranslatableStringValue9translateERK10QByteArrayb(
    const QUiTranslatableStringValue *self,
    const QByteArray *className,
    bool idBased) {
  return new QString(self->translate(*className, idBased));
}

//  QUiTranslatableStringValue::~QUiTranslatableStringValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QUiTranslatableStringValueD1Ev(
    QUiTranslatableStringValue *self) {
  delete self;
}
