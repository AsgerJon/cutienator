//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuanodecreationattributes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuanodecreationattributes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOpcUaNodeCreationAttributesPrivate::QOpcUaNodeCreationAttributesPrivate(
//      )
extern "C" Q_DECL_EXPORT
QOpcUaNodeCreationAttributesPrivate *ritual_ZN35QOpcUaNodeCreationAttributesPrivateC1Ev() {
  return new QOpcUaNodeCreationAttributesPrivate();
}

//  void QOpcUaNodeCreationAttributesPrivate::setAttributeInMask(QOpcUaNodeCr
//      eationAttributesPrivate::BitMask attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaNodeCreationAttributesPrivate18setAttributeInMaskENS_7BitMaskE(
    QOpcUaNodeCreationAttributesPrivate *self,
    QOpcUaNodeCreationAttributesPrivate::BitMask attribute) {
  self->setAttributeInMask(attribute);
}

//  bool QOpcUaNodeCreationAttributesPrivate::attributeSet(QOpcUaNodeCreation
//      AttributesPrivate::BitMask attribute) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QOpcUaNodeCreationAttributesPrivate12attributeSetENS_7BitMaskE(
    const QOpcUaNodeCreationAttributesPrivate *self,
    QOpcUaNodeCreationAttributesPrivate::BitMask attribute) {
  return self->attributeSet(attribute);
}

//  QOpcUaNodeCreationAttributesPrivate::~QOpcUaNodeCreationAttributesPrivate
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOpcUaNodeCreationAttributesPrivateD1Ev(
    QOpcUaNodeCreationAttributesPrivate *self) {
  delete self;
}
