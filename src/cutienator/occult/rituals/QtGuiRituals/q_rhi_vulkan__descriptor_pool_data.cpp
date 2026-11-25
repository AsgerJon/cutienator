//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  '__has_include(<vulkan/vulkan.h>)' as well, as Qt's
//  'qvulkaninstance.h' checks it: 'qrhivulkan_p.h' needs the headers
//  of Vulkan, outside Qt, which a machine may lack.
//  Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiVulkan::DescriptorPoolData::DescriptorPoolData()
extern "C" Q_DECL_EXPORT
QRhiVulkan::DescriptorPoolData *ritual_ZN10QRhiVulkan18DescriptorPoolDataC1Ev() {
  return new QRhiVulkan::DescriptorPoolData();
}

//  QRhiVulkan::DescriptorPoolData::~DescriptorPoolData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan18DescriptorPoolDataD1Ev(
    QRhiVulkan::DescriptorPoolData *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
