//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvulkaninstance.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(vulkan)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#if __has_include(<vulkan/vulkan.h>) || defined(Q_QDOC)
#include <QtGui/QtGui>
#include <QtGui/qvulkaninstance.h>

//  QVulkanLayer::~QVulkanLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVulkanLayerD1Ev(QVulkanLayer *self) {
  delete self;
}

#endif  // __has_include(<vulkan/vulkan.h>) || defined(Q_QDOC)
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#endif  // QT_CONFIG(vulkan)
