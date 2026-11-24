//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexture_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexture_platform.h>

//  QNativeInterface::QSGVulkanTexture::~QSGVulkanTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface16QSGVulkanTextureD1Ev(
    QNativeInterface::QSGVulkanTexture *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
