//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickAnima
//  tion/6.12.0/Qt3DQuickAnimation/private/qt3dquickanimationnodefactory_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <Qt3DQuickAnimation/6.12.0/Qt3DQuickAnimation/private/qt3dquickanimation_global_p.h>
#include <Qt3DQuickAnimation/Qt3DQuickAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickAnimation/6.12.0/Qt3DQuickAnimation/private/qt3dquickanimationnodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickAnimation/private/qt3dquickanimationnodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3danimation/qt3dquickanimationnodefactory.cpp, line 17, as _ZN13Qt3DAnimation25QuickAnimationNodeFactory12registerTypeEPKcS2_ii
namespace Qt3DAnimation {
inline void QuickAnimationNodeFactory::registerType(const char *className, const char *quickName, int major, int minor)
{
    m_types.insert(className, Type(quickName, major, minor));
}
}  // namespace Qt3DAnimation
//  -----------------------------------------------------------------------

//  Qt3DCore::QNode
//      *Qt3DAnimation::QuickAnimationNodeFactory::createNode(const char
//      *type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN13Qt3DAnimation25QuickAnimationNodeFactory10createNodeEPKc(
    Qt3DAnimation::QuickAnimationNodeFactory *self,
    const char *type) {
  return self->createNode(type);
}

//  void Qt3DAnimation::QuickAnimationNodeFactory::registerType(const char
//      *className, const char *quickName, int major, int minor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation25QuickAnimationNodeFactory12registerTypeEPKcS2_ii(
    Qt3DAnimation::QuickAnimationNodeFactory *self,
    const char *className,
    const char *quickName,
    int major,
    int minor) {
  self->registerType(className, quickName, major, minor);
}

//  Qt3DAnimation::QuickAnimationNodeFactory::~QuickAnimationNodeFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation25QuickAnimationNodeFactoryD1Ev(
    Qt3DAnimation::QuickAnimationNodeFactory *self) {
  delete self;
}
