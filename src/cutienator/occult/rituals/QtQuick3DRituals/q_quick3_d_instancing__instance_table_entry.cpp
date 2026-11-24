//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/qquick3dinstancing.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3D/qquick3dinstancing.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qcolor.h>

//  QVector3D QQuick3DInstancing::InstanceTableEntry::getPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18QQuick3DInstancing18InstanceTableEntry11getPositionEv(
    const QQuick3DInstancing::InstanceTableEntry *self) {
  return new QVector3D(self->getPosition());
}

//  QVector3D QQuick3DInstancing::InstanceTableEntry::getScale() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK18QQuick3DInstancing18InstanceTableEntry8getScaleEv(
    const QQuick3DInstancing::InstanceTableEntry *self) {
  return new QVector3D(self->getScale());
}

//  QQuaternion QQuick3DInstancing::InstanceTableEntry::getRotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK18QQuick3DInstancing18InstanceTableEntry11getRotationEv(
    const QQuick3DInstancing::InstanceTableEntry *self) {
  return new QQuaternion(self->getRotation());
}

//  QColor QQuick3DInstancing::InstanceTableEntry::getColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QQuick3DInstancing18InstanceTableEntry8getColorEv(
    const QQuick3DInstancing::InstanceTableEntry *self) {
  return new QColor(self->getColor());
}

//  QQuick3DInstancing::InstanceTableEntry::~InstanceTableEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DInstancing18InstanceTableEntryD1Ev(
    QQuick3DInstancing::InstanceTableEntry *self) {
  delete self;
}
