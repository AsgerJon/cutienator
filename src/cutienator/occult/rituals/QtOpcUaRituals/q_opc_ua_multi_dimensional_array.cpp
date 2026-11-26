//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuamultidimensionalarray.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuamultidimensionalarray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>

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

//  QOpcUaMultiDimensionalArray &QOpcUaMultiDimensionalArray::operator=(const
//      QOpcUaMultiDimensionalArray &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaMultiDimensionalArray *ritual_ZN27QOpcUaMultiDimensionalArrayaSERKS_(
    QOpcUaMultiDimensionalArray *self,
    const QOpcUaMultiDimensionalArray *rhs) {
  return &(self->operator=(*rhs));
}

//  QOpcUaMultiDimensionalArray::QOpcUaMultiDimensionalArray(const
//      QVariantList &valueArray, const QList<quint32> &arrayDimensions)
extern "C" Q_DECL_EXPORT
QOpcUaMultiDimensionalArray *ritual_ZN27QOpcUaMultiDimensionalArrayC1ERK5QListI8QVariantERKS0_IjE(
    const QList<QVariant> *valueArray,
    const QList<quint32> *arrayDimensions) {
  return new QOpcUaMultiDimensionalArray(*valueArray, *arrayDimensions);
}

//  QOpcUaMultiDimensionalArray::QOpcUaMultiDimensionalArray(const
//      QList<quint32> &arrayDimensions)
extern "C" Q_DECL_EXPORT
QOpcUaMultiDimensionalArray *ritual_ZN27QOpcUaMultiDimensionalArrayC1ERK5QListIjE(
    const QList<quint32> *arrayDimensions) {
  return new QOpcUaMultiDimensionalArray(*arrayDimensions);
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

//  QVariantList &QOpcUaMultiDimensionalArray::valueArrayRef()
extern "C" Q_DECL_EXPORT
QVariantList *ritual_ZN27QOpcUaMultiDimensionalArray13valueArrayRefEv(
    QOpcUaMultiDimensionalArray *self) {
  return &(self->valueArrayRef());
}

//  void QOpcUaMultiDimensionalArray::setValueArray(const QVariantList
//      &valueArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaMultiDimensionalArray13setValueArrayERK5QListI8QVariantE(
    QOpcUaMultiDimensionalArray *self,
    const QList<QVariant> *valueArray) {
  self->setValueArray(*valueArray);
}

//  int QOpcUaMultiDimensionalArray::arrayIndex(const QList<quint32>
//      &indices) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOpcUaMultiDimensionalArray10arrayIndexERK5QListIjE(
    const QOpcUaMultiDimensionalArray *self,
    const QList<quint32> *indices) {
  return self->arrayIndex(*indices);
}

//  QVariant QOpcUaMultiDimensionalArray::value(const QList<quint32>
//      &indices) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27QOpcUaMultiDimensionalArray5valueERK5QListIjE(
    const QOpcUaMultiDimensionalArray *self,
    const QList<quint32> *indices) {
  return new QVariant(self->value(*indices));
}

//  bool QOpcUaMultiDimensionalArray::setValue(const QList<quint32> &indices,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QOpcUaMultiDimensionalArray8setValueERK5QListIjERK8QVariant(
    QOpcUaMultiDimensionalArray *self,
    const QList<quint32> *indices,
    const QVariant *value) {
  return self->setValue(*indices, *value);
}

//  bool QOpcUaMultiDimensionalArray::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QOpcUaMultiDimensionalArray7isValidEv(
    const QOpcUaMultiDimensionalArray *self) {
  return self->isValid();
}

//  QList<quint32> QOpcUaMultiDimensionalArray::arrayDimensions() const
extern "C" Q_DECL_EXPORT
QList<quint32> *ritual_ZNK27QOpcUaMultiDimensionalArray15arrayDimensionsEv(
    const QOpcUaMultiDimensionalArray *self) {
  return new QList<quint32>(self->arrayDimensions());
}

//  void QOpcUaMultiDimensionalArray::setArrayDimensions(const QList<quint32>
//      &arrayDimensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpcUaMultiDimensionalArray18setArrayDimensionsERK5QListIjE(
    QOpcUaMultiDimensionalArray *self,
    const QList<quint32> *arrayDimensions) {
  self->setArrayDimensions(*arrayDimensions);
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

//  a QList<quint32> a ritual of QOpcUaMultiDimensionalArray gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpcUaMultiDimensionalArray__QList_quint32(
    QList<quint32> *self) {
  delete self;
}
