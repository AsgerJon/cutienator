//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtransform_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>

//  void QSGTransform::setMatrix(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGTransform9setMatrixERK10QMatrix4x4(
    QSGTransform *self,
    const QMatrix4x4 *matrix) {
  self->setMatrix(*matrix);
}

//  QMatrix4x4 QSGTransform::matrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK12QSGTransform6matrixEv(const QSGTransform *self) {
  return new QMatrix4x4(self->matrix());
}

//  bool QSGTransform::isIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSGTransform10isIdentityEv(const QSGTransform *self) {
  return self->isIdentity();
}

//  bool QSGTransform::operator==(const QMatrix4x4 &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSGTransformeqERK10QMatrix4x4(
    const QSGTransform *self,
    const QMatrix4x4 *other) {
  return self->operator==(*other);
}

//  bool QSGTransform::operator!=(const QMatrix4x4 &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSGTransformneERK10QMatrix4x4(
    const QSGTransform *self,
    const QMatrix4x4 *other) {
  return self->operator!=(*other);
}

//  bool QSGTransform::operator==(const QSGTransform &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSGTransformeqERKS_(
    const QSGTransform *self,
    const QSGTransform *other) {
  return self->operator==(*other);
}

//  bool QSGTransform::operator!=(const QSGTransform &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSGTransformneERKS_(
    const QSGTransform *self,
    const QSGTransform *other) {
  return self->operator!=(*other);
}

//  int QSGTransform::compareTo(const QSGTransform &other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSGTransform9compareToERKS_(
    const QSGTransform *self,
    const QSGTransform *other) {
  return self->compareTo(*other);
}

//  const float *QSGTransform::invertedData() const
extern "C" Q_DECL_EXPORT
const float *ritual_ZNK12QSGTransform12invertedDataEv(
    const QSGTransform *self) {
  return self->invertedData();
}

//  QSGTransform::~QSGTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGTransformD1Ev(QSGTransform *self) {
  delete self;
}
