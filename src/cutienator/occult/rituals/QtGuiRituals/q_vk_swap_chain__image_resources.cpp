//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands also under
//  '__has_include(<vulkan/vulkan.h>)', as Qt's 'qvulkaninstance.h' does,
//  because 'qrhivulkan_p.h' cannot compile on a machine without the
//  headers of Vulkan. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVkSwapChain::ImageResources::~ImageResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVkSwapChain14ImageResourcesD1Ev(
    QVkSwapChain::ImageResources *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
