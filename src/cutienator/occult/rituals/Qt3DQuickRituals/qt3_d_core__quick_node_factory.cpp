//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquicknodefactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquicknodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/private/qt3dquicknodefactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3d/qt3dquicknodefactory.cpp, line 17, as _ZN8Qt3DCore16QuickNodeFactory12registerTypeEPKcS2_ii
namespace Qt3DCore {
inline void QuickNodeFactory::registerType(const char *className, const char *quickName, int major, int minor)
{
    m_types.insert(className, Type(quickName, major, minor));
}
}  // namespace Qt3DCore
//  -----------------------------------------------------------------------

//  QNode *Qt3DCore::QuickNodeFactory::createNode(const char *type)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN8Qt3DCore16QuickNodeFactory10createNodeEPKc(
    Qt3DCore::QuickNodeFactory *self,
    const char *type) {
  return self->createNode(type);
}

//  void Qt3DCore::QuickNodeFactory::registerType(const char *className,
//      const char *quickName, int major, int minor)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QuickNodeFactory12registerTypeEPKcS2_ii(
    Qt3DCore::QuickNodeFactory *self,
    const char *className,
    const char *quickName,
    int major,
    int minor) {
  self->registerType(className, quickName, major, minor);
}

//  Qt3DCore::QuickNodeFactory::~QuickNodeFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QuickNodeFactoryD1Ev(
    Qt3DCore::QuickNodeFactory *self) {
  delete self;
}
