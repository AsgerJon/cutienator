//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsggeometry.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsggeometry.h>

//  Attribute QSGGeometry::Attribute::create(int pos, int tupleSize, int
//      primitiveType, bool isPosition)
extern "C" Q_DECL_EXPORT
QSGGeometry::Attribute *ritual_ZN11QSGGeometry9Attribute6createEiiib(
    int pos,
    int tupleSize,
    int primitiveType,
    bool isPosition) {
  return new QSGGeometry::Attribute(
      QSGGeometry::Attribute::create(
          pos,
          tupleSize,
          primitiveType,
          isPosition));
}

//  Attribute QSGGeometry::Attribute::createWithAttributeType(int pos, int
//      tupleSize, int primitiveType, AttributeType attributeType)
extern "C" Q_DECL_EXPORT
QSGGeometry::Attribute *ritual_ZN11QSGGeometry9Attribute23createWithAttributeTypeEiiiNS_13AttributeTypeE(
    int pos,
    int tupleSize,
    int primitiveType,
    QSGGeometry::AttributeType attributeType) {
  return new QSGGeometry::Attribute(
      QSGGeometry::Attribute::createWithAttributeType(
          pos,
          tupleSize,
          primitiveType,
          attributeType));
}

//  QSGGeometry::Attribute::~Attribute()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry9AttributeD1Ev(QSGGeometry::Attribute *self) {
  delete self;
}
