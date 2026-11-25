//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the file stands under
//  '__has_include(<vulkan/vulkan.h>)' as well, as Qt's 'qvulkaninstance.h'
//  does, because 'qrhivulkan_p.h' names Vulkan's types ('VkBuffer') and a
//  machine with Qt built for Vulkan may lack Vulkan's headers. Kept as it
//  is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiVulkan::BufferReadback::~BufferReadback()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan14BufferReadbackD1Ev(
    QRhiVulkan::BufferReadback *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
