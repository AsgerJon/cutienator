//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: the line pulling in 'qrhivulkan_p.h' stands under
//  '__has_include(<vulkan/vulkan.h>)' as well, as Qt's 'qvulkaninstance.h'
//  checks it, because that header needs Vulkan's 'vulkan/vulkan.h', missing
//  on a machine without Vulkan's headers, and no ritual here needs it. The
//  line pulling in 'qrhid3d12_p.h' stands under
//  '__has_include(<D3D12MemAlloc.h>)': that header includes
//  'D3D12MemAlloc.h', a library Qt keeps in its source and never installs,
//  and no ritual here needs it. Kept as it is when the generator runs again.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhi_p.h>
#include <QtCore/qmath.h>
#include <QtCore/QLoggingCategory>
#include <QtCore/private/qloggingregistry_p.h>
#include <QtGui/private/qrhinull_p.h>
#ifndef QT_NO_OPENGL
#include <QtGui/private/qrhigles2_p.h>
#endif
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/private/qrhivulkan_p.h>
#endif
#ifdef Q_OS_WIN
#include <QtGui/private/qrhid3d11_p.h>
#if __has_include(<D3D12MemAlloc.h>)
#include <QtGui/private/qrhid3d12_p.h>
#endif
#endif
#if QT_CONFIG(metal)
#include <QtGui/private/qrhimetal_p.h>
#endif
#include <limits>
#include <memory>
#include <QtGui/private/qrhinull_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhi.cpp, line 5819, as _ZN18QRhiImplementation16updateLayoutDescEP26QRhiShaderResourceBindings
inline void QRhiImplementation::updateLayoutDesc(QRhiShaderResourceBindings *srb)
{
    srb->m_layoutDescHash = 0;
    srb->m_layoutDesc.clear();
    auto layoutDescAppender = std::back_inserter(srb->m_layoutDesc);
    for (const QRhiShaderResourceBinding &b : std::as_const(srb->m_bindings)) {
        const QRhiShaderResourceBinding::Data *d = &b.d;
        srb->m_layoutDescHash ^= uint(d->binding) ^ uint(d->stage) ^ uint(d->type)
            ^ uint(d->arraySize());
        layoutDescAppender = d->serialize(layoutDescAppender);
    }
}

//  from src/gui/rhi/qrhi.cpp, line 8940, as _ZN18QRhiImplementation33sanityCheckShaderResourceBindingsEP26QRhiShaderResourceBindings
inline bool QRhiImplementation::sanityCheckShaderResourceBindings(QRhiShaderResourceBindings *srb)
{
#ifndef QT_NO_DEBUG
    bool bindingsOk = true;
    const int CHECKED_BINDINGS_COUNT = 64;
    bool bindingSeen[CHECKED_BINDINGS_COUNT] = {};
    for (auto it = srb->cbeginBindings(), end = srb->cendBindings(); it != end; ++it) {
        const int binding = shaderResourceBindingData(*it)->binding;
        if (binding >= CHECKED_BINDINGS_COUNT)
            continue;
        if (binding < 0) {
            qWarning("Invalid binding number %d", binding);
            bindingsOk = false;
            continue;
        }
        switch (shaderResourceBindingData(*it)->type) {
        case QRhiShaderResourceBinding::UniformBuffer:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Uniform buffer duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        case QRhiShaderResourceBinding::SampledTexture:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Combined image sampler duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        case QRhiShaderResourceBinding::Texture:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Texture duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        case QRhiShaderResourceBinding::Sampler:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Sampler duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        case QRhiShaderResourceBinding::ImageLoad:
        case QRhiShaderResourceBinding::ImageStore:
        case QRhiShaderResourceBinding::ImageLoadStore:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Image duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        case QRhiShaderResourceBinding::BufferLoad:
        case QRhiShaderResourceBinding::BufferStore:
        case QRhiShaderResourceBinding::BufferLoadStore:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Buffer duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        default:
            qWarning("Unknown binding type %d", int(shaderResourceBindingData(*it)->type));
            bindingsOk = false;
            break;
        }
    }

    if (!bindingsOk) {
        qWarning() << *srb;
        return false;
    }
#else
    Q_UNUSED(srb);
#endif
    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 942, as _ZN27QNullShaderResourceBindingsC1EP18QRhiImplementation
inline QNullShaderResourceBindings::QNullShaderResourceBindings(QRhiImplementation *rhi)
    : QRhiShaderResourceBindings(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 947, as _ZN27QNullShaderResourceBindingsD1Ev
inline QNullShaderResourceBindings::~QNullShaderResourceBindings()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 952, as _ZN27QNullShaderResourceBindings7destroyEv
inline void QNullShaderResourceBindings::destroy()
{
    QRHI_RES_RHI(QRhiNull);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 959, as _ZN27QNullShaderResourceBindings6createEv
inline bool QNullShaderResourceBindings::create()
{
    QRHI_RES_RHI(QRhiNull);
    if (!rhiD->sanityCheckShaderResourceBindings(this))
        return false;

    rhiD->updateLayoutDesc(this);

    rhiD->registerResource(this, false);
    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 971, as _ZN27QNullShaderResourceBindings15updateResourcesE6QFlagsIN26QRhiShaderResourceBindings10UpdateFlagEE
inline void QNullShaderResourceBindings::updateResources(UpdateFlags flags)
{
    Q_UNUSED(flags);
}
//  -----------------------------------------------------------------------

//  A QNullShaderResourceBindings that Python can take functions over in. Every QNullShaderResourceBindings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullShaderResourceBindingsCall0)(const void *, int *);
typedef bool (*CuteQNullShaderResourceBindingsCall1)(const void *, int *);
typedef void (*CuteQNullShaderResourceBindingsCall2)(const void *, int, int *);
typedef int (*CuteQNullShaderResourceBindingsCall3)(const void *, int *);
class CuteQNullShaderResourceBindings : public QNullShaderResourceBindings {
public:
  using QNullShaderResourceBindings::QNullShaderResourceBindings;
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

  //  void QNullShaderResourceBindings::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullShaderResourceBindingsCall0 call = reinterpret_cast<CuteQNullShaderResourceBindingsCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullShaderResourceBindings::destroy();
  }

  //  bool QNullShaderResourceBindings::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullShaderResourceBindingsCall1 call = reinterpret_cast<CuteQNullShaderResourceBindingsCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNullShaderResourceBindings::create();
  }

  //  void QNullShaderResourceBindings::updateResources(UpdateFlags flags)
  void updateResources(
      QRhiShaderResourceBindings::UpdateFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullShaderResourceBindingsCall2 call = reinterpret_cast<CuteQNullShaderResourceBindingsCall2>(taken[2]);
      call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QNullShaderResourceBindings::updateResources(flags);
  }

  //  QRhiResource::Type QRhiShaderResourceBindings::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNullShaderResourceBindingsCall3 call = reinterpret_cast<CuteQNullShaderResourceBindingsCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiShaderResourceBindings::resourceType();
  }
};

//  QNullShaderResourceBindings::QNullShaderResourceBindings(QRhiImplementati
//      on *rhi)
extern "C" Q_DECL_EXPORT
QNullShaderResourceBindings *ritual_ZN27QNullShaderResourceBindingsC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQNullShaderResourceBindings(rhi);
}

//  QNullShaderResourceBindings::~QNullShaderResourceBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QNullShaderResourceBindingsD1Ev(
    QNullShaderResourceBindings *self) {
  delete self;
}

//  void QNullShaderResourceBindings::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QNullShaderResourceBindings7destroyEv(
    QNullShaderResourceBindings *self) {
  self->destroy();
}

//  bool QNullShaderResourceBindings::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QNullShaderResourceBindings6createEv(
    QNullShaderResourceBindings *self) {
  return self->create();
}

//  void QNullShaderResourceBindings::updateResources(UpdateFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QNullShaderResourceBindings15updateResourcesE6QFlagsIN26QRhiShaderResourceBindings10UpdateFlagEE(
    QNullShaderResourceBindings *self,
    int flags) {
  self->updateResources(
      QFlags<QRhiShaderResourceBindings::UpdateFlag>::fromInt(flags));
}

//  a Python function taken by a CuteQNullShaderResourceBindings, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullShaderResourceBindings(
    QNullShaderResourceBindings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullShaderResourceBindings *>(self)->take(key, call);
}

//  void QNullShaderResourceBindings::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QNullShaderResourceBindings7destroyEv(
    QNullShaderResourceBindings *self) {
  self->QNullShaderResourceBindings::destroy();
}

//  bool QNullShaderResourceBindings::create()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QNullShaderResourceBindings6createEv(
    QNullShaderResourceBindings *self) {
  return self->QNullShaderResourceBindings::create();
}

//  void QNullShaderResourceBindings::updateResources(UpdateFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QNullShaderResourceBindings15updateResourcesE6QFlagsIN26QRhiShaderResourceBindings10UpdateFlagEE(
    QNullShaderResourceBindings *self,
    int flags) {
  self->QNullShaderResourceBindings::updateResources(
      QFlags<QRhiShaderResourceBindings::UpdateFlag>::fromInt(flags));
}
