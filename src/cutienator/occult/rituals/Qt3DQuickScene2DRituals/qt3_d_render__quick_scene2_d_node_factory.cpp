//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickScene
//  2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2dnodefactory_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2d_global_p.h>
#include <Qt3DQuickScene2D/Qt3DQuickScene2D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2dnodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/private/qt3dquickscene2dnodefactory_p.h>
#include <Qt3DRender/private/qrenderaspect_p.h>
#include <QtCore/qcoreapplication.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3dscene2d/qt3dquickscene2dnodefactory.cpp, line 21, as _ZN10Qt3DRender23QuickScene2DNodeFactory12registerTypeEPKcS2_ii
namespace Qt3DRender {
inline void QuickScene2DNodeFactory::registerType(const char *className, const char *quickName,
                                           int major, int minor)
{
    m_types.insert(className, Type(quickName, major, minor));
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  Qt3DCore::QNode *Qt3DRender::QuickScene2DNodeFactory::createNode(const
//      char *type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN10Qt3DRender23QuickScene2DNodeFactory10createNodeEPKc(
    Qt3DRender::QuickScene2DNodeFactory *self,
    const char *type) {
  return self->createNode(type);
}

//  void Qt3DRender::QuickScene2DNodeFactory::registerType(const char
//      *className, const char *quickName, int major, int minor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QuickScene2DNodeFactory12registerTypeEPKcS2_ii(
    Qt3DRender::QuickScene2DNodeFactory *self,
    const char *className,
    const char *quickName,
    int major,
    int minor) {
  self->registerType(className, quickName, major, minor);
}

//  Qt3DRender::QuickScene2DNodeFactory::~QuickScene2DNodeFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QuickScene2DNodeFactoryD1Ev(
    Qt3DRender::QuickScene2DNodeFactory *self) {
  delete self;
}
