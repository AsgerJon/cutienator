//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: everything after the global includes
//  stands also under '__has_include(<vulkan/vulkan.h>)', the check Qt's
//  'qvulkaninstance.h' makes, because without Vulkan's headers Qt
//  declares none of the Vulkan types ('VkBuffer' and the rest) that
//  'qrhivulkan_p.h' uses. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVkCommandBuffer::Command::~Command()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVkCommandBuffer7CommandD1Ev(
    QVkCommandBuffer::Command *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
