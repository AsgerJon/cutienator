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
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhivulkan_p.h>
#include <QtGui/qpa/qplatformvulkaninstance.h>
#include <QtCore/qmath.h>
#include <QtGui/qwindow.h>
#include <QtGui/private/qvulkandefaultinstance_p.h>
#include <QtCore/q20memory.h>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhivulkan.cpp, line 8528, as _ZN25QVkShaderResourceBindingsD1Ev
inline QVkShaderResourceBindings::~QVkShaderResourceBindings()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8533, as _ZN25QVkShaderResourceBindings7destroyEv
inline void QVkShaderResourceBindings::destroy()
{
    if (!layout)
        return;

    sortedBindings.clear();
    sortedDynamicOffsetBindingNumbers.clear();

    QRhiVulkan::DeferredReleaseEntry e;
    e.type = QRhiVulkan::DeferredReleaseEntry::ShaderResourceBindings;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.shaderResourceBindings.poolIndex = poolIndex;
    e.shaderResourceBindings.layout = layout;

    poolIndex = -1;
    layout = VK_NULL_HANDLE;
    for (int i = 0; i < QVK_FRAMES_IN_FLIGHT; ++i)
        descSets[i] = VK_NULL_HANDLE;

    QRHI_RES_RHI(QRhiVulkan);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8638, as _ZN25QVkShaderResourceBindings15updateResourcesE6QFlagsIN26QRhiShaderResourceBindings10UpdateFlagEE
inline void QVkShaderResourceBindings::updateResources(UpdateFlags flags)
{
    sortedBindings.clear();
    std::copy(m_bindings.cbegin(), m_bindings.cend(), std::back_inserter(sortedBindings));
    if (!flags.testFlag(BindingsAreSorted))
        std::sort(sortedBindings.begin(), sortedBindings.end(), QRhiImplementation::sortedBindingLessThan);

    sortedDynamicOffsetBindingNumbers.clear();
    for (const QRhiShaderResourceBinding &binding : std::as_const(sortedBindings)) {
        const QRhiShaderResourceBinding::Data *b = QRhiImplementation::shaderResourceBindingData(binding);
        if (b->type == QRhiShaderResourceBinding::UniformBuffer && b->u.ubuf.buf) {
            if (b->u.ubuf.hasDynamicOffset)
                sortedDynamicOffsetBindingNumbers.append(b->binding);
        }
    }

    // Reset the state tracking table too - it can deal with assigning a
    // different QRhiBuffer/Texture/Sampler for a binding point, but it cannot
    // detect changes in the associated data, such as the buffer offset. And
    // just like after a create(), a call to updateResources() may lead to now
    // specifying a different offset for the same QRhiBuffer for a given binding
    // point. The same applies to other type of associated data that is not part
    // of the layout, such as the mip level for a StorageImage. Instead of
    // complicating the checks in setShaderResources(), reset the table here
    // just like we do in create().
    for (int i = 0; i < QVK_FRAMES_IN_FLIGHT; ++i) {
        Q_ASSERT(boundResourceData[i].size() == sortedBindings.size());
        for (BoundResourceData &bd : boundResourceData[i])
            memset(&bd, 0, sizeof(BoundResourceData));
    }

    generation += 1;
}
//  -----------------------------------------------------------------------

//  A QVkShaderResourceBindings that Python can take functions over in. Every QVkShaderResourceBindings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkShaderResourceBindingsCall0)(const void *, int *);
typedef bool (*CuteQVkShaderResourceBindingsCall1)(const void *, int *);
typedef void (*CuteQVkShaderResourceBindingsCall2)(const void *, int, int *);
typedef int (*CuteQVkShaderResourceBindingsCall3)(const void *, int *);
class CuteQVkShaderResourceBindings : public QVkShaderResourceBindings {
public:
  using QVkShaderResourceBindings::QVkShaderResourceBindings;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QRhiShaderResourceBindings6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QRhiShaderResourceBindings15updateResourcesE6QFlagsINS_10UpdateFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QVkShaderResourceBindings::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkShaderResourceBindingsCall0 call = reinterpret_cast<CuteQVkShaderResourceBindingsCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkShaderResourceBindings::destroy();
  }

  //  bool QVkShaderResourceBindings::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkShaderResourceBindingsCall1 call = reinterpret_cast<CuteQVkShaderResourceBindingsCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QVkShaderResourceBindings::create();
  }

  //  void QVkShaderResourceBindings::updateResources(UpdateFlags flags)
  void updateResources(
      QRhiShaderResourceBindings::UpdateFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkShaderResourceBindingsCall2 call = reinterpret_cast<CuteQVkShaderResourceBindingsCall2>(taken[2]);
      call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QVkShaderResourceBindings::updateResources(flags);
  }

  //  QRhiResource::Type QRhiShaderResourceBindings::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQVkShaderResourceBindingsCall3 call = reinterpret_cast<CuteQVkShaderResourceBindingsCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiShaderResourceBindings::resourceType();
  }
};

//  QVkShaderResourceBindings::~QVkShaderResourceBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QVkShaderResourceBindingsD1Ev(
    QVkShaderResourceBindings *self) {
  delete self;
}

//  void QVkShaderResourceBindings::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QVkShaderResourceBindings7destroyEv(
    QVkShaderResourceBindings *self) {
  self->destroy();
}

//  void QVkShaderResourceBindings::updateResources(UpdateFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QVkShaderResourceBindings15updateResourcesE6QFlagsIN26QRhiShaderResourceBindings10UpdateFlagEE(
    QVkShaderResourceBindings *self,
    int flags) {
  self->updateResources(
      QFlags<QRhiShaderResourceBindings::UpdateFlag>::fromInt(flags));
}

//  a Python function taken by a CuteQVkShaderResourceBindings, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkShaderResourceBindings(
    QVkShaderResourceBindings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVkShaderResourceBindings *>(self)->take(key, call);
}

//  void QVkShaderResourceBindings::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QVkShaderResourceBindings7destroyEv(
    QVkShaderResourceBindings *self) {
  self->QVkShaderResourceBindings::destroy();
}

//  void QVkShaderResourceBindings::updateResources(UpdateFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QVkShaderResourceBindings15updateResourcesE6QFlagsIN26QRhiShaderResourceBindings10UpdateFlagEE(
    QVkShaderResourceBindings *self,
    int flags) {
  self->QVkShaderResourceBindings::updateResources(
      QFlags<QRhiShaderResourceBindings::UpdateFlag>::fromInt(flags));
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
