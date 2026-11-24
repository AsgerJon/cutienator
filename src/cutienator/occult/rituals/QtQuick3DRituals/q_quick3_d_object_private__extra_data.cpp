//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuick3DObjectPrivate::ExtraData::~ExtraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DObjectPrivate9ExtraDataD1Ev(
    QQuick3DObjectPrivate::ExtraData *self) {
  delete self;
}
