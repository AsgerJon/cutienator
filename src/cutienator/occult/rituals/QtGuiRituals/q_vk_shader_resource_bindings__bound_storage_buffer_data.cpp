//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file also stands under
//  '__has_include(<vulkan/vulkan.h>)', as in Qt's 'qvulkaninstance.h',
//  since 'qrhivulkan_p.h' uses the types of Vulkan's own header, which a
//  machine with Qt but without Vulkan's headers lacks. Kept as it is
//  when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVkShaderResourceBindings::BoundStorageBufferData::~BoundStorageBufferDat
//      a()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QVkShaderResourceBindings22BoundStorageBufferDataD1Ev(
    QVkShaderResourceBindings::BoundStorageBufferData *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
