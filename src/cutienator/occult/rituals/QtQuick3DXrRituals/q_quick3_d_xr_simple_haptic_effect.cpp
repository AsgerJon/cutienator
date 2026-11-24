//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DXr/6.
//  12.0/QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquick3dxrabstracthapticeffect_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 49, as _ZN28QQuick3DXrSimpleHapticEffect9amplitudeEv
inline float QQuick3DXrSimpleHapticEffect::amplitude()
{
    return m_amplitude;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 67, as _ZN28QQuick3DXrSimpleHapticEffect8durationEv
inline float QQuick3DXrSimpleHapticEffect::duration()
{
    return m_duration;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrabstracthapticeffect.cpp, line 86, as _ZN28QQuick3DXrSimpleHapticEffect9frequencyEv
inline float QQuick3DXrSimpleHapticEffect::frequency()
{
    return m_frequency;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrSimpleHapticEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuick3DXrSimpleHapticEffect10metaObjectEv(
    const QQuick3DXrSimpleHapticEffect *self) {
  return self->metaObject();
}

//  float QQuick3DXrSimpleHapticEffect::amplitude()
extern "C" Q_DECL_EXPORT
float ritual_ZN28QQuick3DXrSimpleHapticEffect9amplitudeEv(
    QQuick3DXrSimpleHapticEffect *self) {
  return self->amplitude();
}

//  float QQuick3DXrSimpleHapticEffect::duration()
extern "C" Q_DECL_EXPORT
float ritual_ZN28QQuick3DXrSimpleHapticEffect8durationEv(
    QQuick3DXrSimpleHapticEffect *self) {
  return self->duration();
}

//  float QQuick3DXrSimpleHapticEffect::frequency()
extern "C" Q_DECL_EXPORT
float ritual_ZN28QQuick3DXrSimpleHapticEffect9frequencyEv(
    QQuick3DXrSimpleHapticEffect *self) {
  return self->frequency();
}
