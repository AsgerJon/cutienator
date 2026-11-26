//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickRende
//  r/6.12.0/Qt3DQuickRender/private/qt3dquickrendernodefactory_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrender_global_p.h>
#include <Qt3DQuickRender/Qt3DQuickRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrendernodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickRender/private/qt3dquickrendernodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3drender/qt3dquickrendernodefactory.cpp, line 17, as _ZN10Qt3DRender22QuickRenderNodeFactory12registerTypeEPKcS2_ii
namespace Qt3DRender {
inline void QuickRenderNodeFactory::registerType(const char *className, const char *quickName, int major, int minor)
{
    m_types.insert(className, Type(quickName, major, minor));
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  Qt3DCore::QNode *Qt3DRender::QuickRenderNodeFactory::createNode(const
//      char *type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN10Qt3DRender22QuickRenderNodeFactory10createNodeEPKc(
    Qt3DRender::QuickRenderNodeFactory *self,
    const char *type) {
  return self->createNode(type);
}

//  void Qt3DRender::QuickRenderNodeFactory::registerType(const char
//      *className, const char *quickName, int major, int minor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QuickRenderNodeFactory12registerTypeEPKcS2_ii(
    Qt3DRender::QuickRenderNodeFactory *self,
    const char *className,
    const char *quickName,
    int major,
    int minor) {
  self->registerType(className, quickName, major, minor);
}

//  Qt3DRender::QuickRenderNodeFactory::~QuickRenderNodeFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QuickRenderNodeFactoryD1Ev(
    Qt3DRender::QuickRenderNodeFactory *self) {
  delete self;
}
