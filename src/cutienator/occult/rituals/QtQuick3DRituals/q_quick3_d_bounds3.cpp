//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dmodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>

//  QVector3D QQuick3DBounds3::minimum() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK15QQuick3DBounds37minimumEv(
    const QQuick3DBounds3 *self) {
  return new QVector3D(self->minimum());
}

//  QVector3D QQuick3DBounds3::maximum() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK15QQuick3DBounds37maximumEv(
    const QQuick3DBounds3 *self) {
  return new QVector3D(self->maximum());
}

//  QQuick3DBounds3::~QQuick3DBounds3()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuick3DBounds3D1Ev(QQuick3DBounds3 *self) {
  delete self;
}
