//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qmorphtarget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qmorphtarget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/qmorphtarget.h>
#include "Qt3DAnimation/private/qmorphtarget_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/frontend/qmorphtarget.cpp, line 60, as _ZN13Qt3DAnimation19QMorphTargetPrivateC1Ev
namespace Qt3DAnimation {
inline QMorphTargetPrivate::QMorphTargetPrivate()
    : QObjectPrivate()
{

}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qmorphtarget.cpp, line 66, as _ZN13Qt3DAnimation19QMorphTargetPrivate20updateAttributeNamesEv
namespace Qt3DAnimation {
inline void QMorphTargetPrivate::updateAttributeNames()
{
    m_attributeNames.clear();
    for (const Qt3DCore::QAttribute *attr : std::as_const(m_targetAttributes))
        m_attributeNames.push_back(attr->name());
}
}  // namespace Qt3DAnimation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::QMorphTargetPrivate::QMorphTargetPrivate()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphTargetPrivate *ritual_ZN13Qt3DAnimation19QMorphTargetPrivateC1Ev() {
  return new Qt3DAnimation::QMorphTargetPrivate();
}

//  void Qt3DAnimation::QMorphTargetPrivate::updateAttributeNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation19QMorphTargetPrivate20updateAttributeNamesEv(
    Qt3DAnimation::QMorphTargetPrivate *self) {
  self->updateAttributeNames();
}

//  QMorphTarget *Qt3DAnimation::QMorphTargetPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphTarget *ritual_ZN13Qt3DAnimation19QMorphTargetPrivate6q_funcEv(
    Qt3DAnimation::QMorphTargetPrivate *self) {
  return self->q_func();
}

//  const QMorphTarget *Qt3DAnimation::QMorphTargetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QMorphTarget *ritual_ZNK13Qt3DAnimation19QMorphTargetPrivate6q_funcEv(
    const Qt3DAnimation::QMorphTargetPrivate *self) {
  return self->q_func();
}
