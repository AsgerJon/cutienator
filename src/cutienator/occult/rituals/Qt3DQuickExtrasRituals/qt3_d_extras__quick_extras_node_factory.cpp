//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickExtra
//  s/6.12.0/Qt3DQuickExtras/private/qt3dquickextrasnodefactory_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/qt3dquickextras_global_p.h>
#include <Qt3DQuickExtras/Qt3DQuickExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/qt3dquickextrasnodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickExtras/private/qt3dquickextrasnodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3dextras/qt3dquickextrasnodefactory.cpp, line 17, as _ZN10Qt3DExtras22QuickExtrasNodeFactory12registerTypeEPKcS2_ii
namespace Qt3DExtras {
inline void QuickExtrasNodeFactory::registerType(const char *className, const char *quickName, int major, int minor)
{
    m_types.insert(className, Type(quickName, major, minor));
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  Qt3DCore::QNode *Qt3DExtras::QuickExtrasNodeFactory::createNode(const
//      char *type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN10Qt3DExtras22QuickExtrasNodeFactory10createNodeEPKc(
    Qt3DExtras::QuickExtrasNodeFactory *self,
    const char *type) {
  return self->createNode(type);
}

//  void Qt3DExtras::QuickExtrasNodeFactory::registerType(const char
//      *className, const char *quickName, int major, int minor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QuickExtrasNodeFactory12registerTypeEPKcS2_ii(
    Qt3DExtras::QuickExtrasNodeFactory *self,
    const char *className,
    const char *quickName,
    int major,
    int minor) {
  self->registerType(className, quickName, major, minor);
}

//  Qt3DExtras::QuickExtrasNodeFactory::~QuickExtrasNodeFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QuickExtrasNodeFactoryD1Ev(
    Qt3DExtras::QuickExtrasNodeFactory *self) {
  delete self;
}
