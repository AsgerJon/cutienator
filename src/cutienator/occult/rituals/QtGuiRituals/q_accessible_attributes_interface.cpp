//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qvariant.h>

//  QAccessibleAttributesInterface::~QAccessibleAttributesInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QAccessibleAttributesInterfaceD1Ev(
    QAccessibleAttributesInterface *self) {
  delete self;
}

//  QVariant
//      QAccessibleAttributesInterface::attributeValue(QAccessible::Attribute
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleAttributesInterface *self,
    QAccessible::Attribute key) {
  return new QVariant(self->attributeValue(key));
}
