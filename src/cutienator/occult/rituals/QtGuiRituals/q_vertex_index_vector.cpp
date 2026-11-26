//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtriangulator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtriangulator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Type QVertexIndexVector::type() const
extern "C" Q_DECL_EXPORT
QVertexIndexVector::Type ritual_ZNK18QVertexIndexVector4typeEv(
    const QVertexIndexVector *self) {
  return self->type();
}

//  void QVertexIndexVector::setDataUint(const QList<quint32> &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QVertexIndexVector11setDataUintERK5QListIjE(
    QVertexIndexVector *self,
    const QList<quint32> *data) {
  self->setDataUint(*data);
}

//  void QVertexIndexVector::setDataUshort(const QList<quint16> &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QVertexIndexVector13setDataUshortERK5QListItE(
    QVertexIndexVector *self,
    const QList<quint16> *data) {
  self->setDataUshort(*data);
}

//  const void *QVertexIndexVector::data() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK18QVertexIndexVector4dataEv(
    const QVertexIndexVector *self) {
  return self->data();
}

//  int QVertexIndexVector::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QVertexIndexVector4sizeEv(const QVertexIndexVector *self) {
  return self->size();
}

//  QVertexIndexVector::~QVertexIndexVector()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QVertexIndexVectorD1Ev(QVertexIndexVector *self) {
  delete self;
}
