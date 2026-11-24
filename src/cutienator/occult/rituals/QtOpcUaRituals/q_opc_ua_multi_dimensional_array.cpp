//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuamultidimensionalarray.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuamultidimensionalarray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QOpcUaMultiDimensionalArray::QOpcUaMultiDimensionalArray()
extern "C" Q_DECL_EXPORT
QOpcUaMultiDimensionalArray *ritual_ZN27QOpcUaMultiDimensionalArrayC1Ev() {
  return new QOpcUaMultiDimensionalArray();
}

//  QOpcUaMultiDimensionalArray::QOpcUaMultiDimensionalArray(const
//      QOpcUaMultiDimensionalArray &other)
extern "C" Q_DECL_EXPORT
QOpcUaMultiDimensionalArray *ritual_ZN27QOpcUaMultiDimensionalArrayC1ERKS_(
    const QOpcUaMultiDimensionalArray *other) {
  return new QOpcUaMultiDimensionalArray(*other);
}

//  QOpcUaMultiDimensionalArray::~QOpcUaMultiDimensionalArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaMultiDimensionalArrayD1Ev(
    QOpcUaMultiDimensionalArray *self) {
  delete self;
}

//  QVariantList QOpcUaMultiDimensionalArray::valueArray() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK27QOpcUaMultiDimensionalArray10valueArrayEv(
    const QOpcUaMultiDimensionalArray *self) {
  return new QList<QVariant>(self->valueArray());
}

//  void QOpcUaMultiDimensionalArray::setValueArray(const QVariantList
//      &valueArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaMultiDimensionalArray13setValueArrayERK5QListI8QVariantE(
    QOpcUaMultiDimensionalArray *self,
    const QList<QVariant> *valueArray) {
  self->setValueArray(*valueArray);
}

//  bool QOpcUaMultiDimensionalArray::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QOpcUaMultiDimensionalArray7isValidEv(
    const QOpcUaMultiDimensionalArray *self) {
  return self->isValid();
}

//  bool QOpcUaMultiDimensionalArray::operator==(const
//      QOpcUaMultiDimensionalArray &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QOpcUaMultiDimensionalArrayeqERKS_(
    const QOpcUaMultiDimensionalArray *self,
    const QOpcUaMultiDimensionalArray *other) {
  return self->operator==(*other);
}

//  QVariant QOpcUaMultiDimensionalArray::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27QOpcUaMultiDimensionalArraycv8QVariantEv(
    const QOpcUaMultiDimensionalArray *self) {
  return new QVariant(self->operator QVariant());
}
