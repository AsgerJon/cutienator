//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  '__has_include(<vulkan/vulkan.h>)' beside 'QT_CONFIG(vulkan)', as
//  Qt's 'qvulkaninstance.h' checks it, since without Vulkan's headers
//  'qrhivulkan_p.h' fails on 'VkBuffer'. Kept as it is when the
//  generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVkShaderResourceBindings::BoundResourceData::~BoundResourceData()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QVkShaderResourceBindings17BoundResourceDataD1Ev(
    QVkShaderResourceBindings::BoundResourceData *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
