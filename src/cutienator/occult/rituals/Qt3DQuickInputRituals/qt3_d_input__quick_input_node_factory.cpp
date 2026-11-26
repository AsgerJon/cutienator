//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickInput
//  /6.12.0/Qt3DQuickInput/private/qt3dquickinputnodefactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuickInput/6.12.0/Qt3DQuickInput/private/qt3dquickinput_global_p.h>
#include <Qt3DQuickInput/Qt3DQuickInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickInput/6.12.0/Qt3DQuickInput/private/qt3dquickinputnodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickInput/private/qt3dquickinputnodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3dinput/qt3dquickinputnodefactory.cpp, line 17, as _ZN9Qt3DInput21QuickInputNodeFactory12registerTypeEPKcS2_ii
namespace Qt3DInput {
inline void QuickInputNodeFactory::registerType(const char *className, const char *quickName, int major, int minor)
{
    m_types.insert(className, Type(quickName, major, minor));
}
}  // namespace Qt3DInput
//  -----------------------------------------------------------------------

//  Qt3DCore::QNode *Qt3DInput::QuickInputNodeFactory::createNode(const char
//      *type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN9Qt3DInput21QuickInputNodeFactory10createNodeEPKc(
    Qt3DInput::QuickInputNodeFactory *self,
    const char *type) {
  return self->createNode(type);
}

//  void Qt3DInput::QuickInputNodeFactory::registerType(const char
//      *className, const char *quickName, int major, int minor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput21QuickInputNodeFactory12registerTypeEPKcS2_ii(
    Qt3DInput::QuickInputNodeFactory *self,
    const char *className,
    const char *quickName,
    int major,
    int minor) {
  self->registerType(className, quickName, major, minor);
}

//  Qt3DInput::QuickInputNodeFactory::~QuickInputNodeFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput21QuickInputNodeFactoryD1Ev(
    Qt3DInput::QuickInputNodeFactory *self) {
  delete self;
}
