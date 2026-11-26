//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dlightmapbaker_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dlightmapbaker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/private/qquick3dlightmapbaker_p.h>
#include <QtQuick3D/private/qquick3dviewport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/quick3d/qquick3dlightmapbaker.cpp, line 230, as _ZN21QQuick3DLightmapBaker13BakingControl5resetEv
inline void QQuick3DLightmapBaker::BakingControl::reset() {
    cancelFlag = false;
}

//  from ../qtquick3d/src/quick3d/qquick3dlightmapbaker.cpp, line 234, as _ZN21QQuick3DLightmapBaker13BakingControl13requestCancelEv
inline void QQuick3DLightmapBaker::BakingControl::requestCancel() {
    cancelFlag = true;
}

//  from ../qtquick3d/src/quick3d/qquick3dlightmapbaker.cpp, line 238, as _ZNK21QQuick3DLightmapBaker13BakingControl11isCancelledEv
inline bool QQuick3DLightmapBaker::BakingControl::isCancelled() const {
    return cancelFlag;
}
//  -----------------------------------------------------------------------

//  void QQuick3DLightmapBaker::BakingControl::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DLightmapBaker13BakingControl5resetEv(
    QQuick3DLightmapBaker::BakingControl *self) {
  self->reset();
}

//  void QQuick3DLightmapBaker::BakingControl::requestCancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DLightmapBaker13BakingControl13requestCancelEv(
    QQuick3DLightmapBaker::BakingControl *self) {
  self->requestCancel();
}

//  bool QQuick3DLightmapBaker::BakingControl::isCancelled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DLightmapBaker13BakingControl11isCancelledEv(
    const QQuick3DLightmapBaker::BakingControl *self) {
  return self->isCancelled();
}

//  QQuick3DLightmapBaker::BakingControl::~BakingControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DLightmapBaker13BakingControlD1Ev(
    QQuick3DLightmapBaker::BakingControl *self) {
  delete self;
}
