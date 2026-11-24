//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(vulkan)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGTexturePlatformVulkan::QSGTexturePlatformVulkan(QSGTexture *t)
extern "C" Q_DECL_EXPORT
QSGTexturePlatformVulkan *ritual_ZN24QSGTexturePlatformVulkanC1EP10QSGTexture(
    QSGTexture *t) {
  return new QSGTexturePlatformVulkan(t);
}

#endif  // QT_CONFIG(vulkan)
