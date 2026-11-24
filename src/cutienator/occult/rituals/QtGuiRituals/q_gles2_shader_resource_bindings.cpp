//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrhi_p.h"
#include <qmath.h>
#include <QLoggingCategory>
#include "private/qloggingregistry_p.h"
#include "qrhinull_p.h"
#ifndef QT_NO_OPENGL
#include "qrhigles2_p.h"
#endif
#if QT_CONFIG(vulkan)
#endif
#ifdef Q_OS_WIN
#include "qrhid3d11_p.h"
#include "qrhid3d12_p.h"
#endif
#if QT_CONFIG(metal)
#include "qrhimetal_p.h"
#endif
#include <limits>
#include <memory>
#include "qrhigles2_p.h"
#include <QOffscreenSurface>
#include <QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <qpa/qplatformopenglcontext.h>
#include <qmath.h>
#include <limits>
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

//  from src/gui/rhi/qrhigles2.cpp, line 6857, as _ZN28QGles2ShaderResourceBindingsC1EP18QRhiImplementation
inline QGles2ShaderResourceBindings::QGles2ShaderResourceBindings(QRhiImplementation *rhi)
    : QRhiShaderResourceBindings(rhi)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6862, as _ZN28QGles2ShaderResourceBindingsD1Ev
inline QGles2ShaderResourceBindings::~QGles2ShaderResourceBindings()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 6867, as _ZN28QGles2ShaderResourceBindings7destroyEv
inline void QGles2ShaderResourceBindings::destroy()
{
    QRHI_RES_RHI(QRhiGles2);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhigles2.cpp, line 6874, as _ZN28QGles2ShaderResourceBindings6createEv
inline bool QGles2ShaderResourceBindings::create()
{
    QRHI_RES_RHI(QRhiGles2);
    if (!rhiD->sanityCheckShaderResourceBindings(this))
        return false;

    hasDynamicOffset = false;
    for (int i = 0, ie = m_bindings.size(); i != ie; ++i) {
        const QRhiShaderResourceBinding::Data *b = QRhiImplementation::shaderResourceBindingData(m_bindings.at(i));
        if (b->type == QRhiShaderResourceBinding::UniformBuffer) {
            if (b->u.ubuf.hasDynamicOffset) {
                hasDynamicOffset = true;
                break;
            }
        }
    }

    rhiD->updateLayoutDesc(this);

    generation += 1;
    rhiD->registerResource(this, false);
    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6898, as _ZN28QGles2ShaderResourceBindings15updateResourcesE6QFlagsIN26QRhiShaderResourceBindings10UpdateFlagEE
inline void QGles2ShaderResourceBindings::updateResources(UpdateFlags flags)
{
    Q_UNUSED(flags);
    generation += 1;
}
//  -----------------------------------------------------------------------

//  A QGles2ShaderResourceBindings that Python can take functions over in. Every QGles2ShaderResourceBindings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2ShaderResourceBindingsCall0)(const void *, int *);
typedef bool (*CuteQGles2ShaderResourceBindingsCall1)(const void *, int *);
typedef void (*CuteQGles2ShaderResourceBindingsCall2)(const void *, int, int *);
typedef int (*CuteQGles2ShaderResourceBindingsCall3)(const void *, int *);
class CuteQGles2ShaderResourceBindings : public QGles2ShaderResourceBindings {
public:
  using QGles2ShaderResourceBindings::QGles2ShaderResourceBindings;
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

  //  void QGles2ShaderResourceBindings::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2ShaderResourceBindingsCall0 call = reinterpret_cast<CuteQGles2ShaderResourceBindingsCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2ShaderResourceBindings::destroy();
  }

  //  bool QGles2ShaderResourceBindings::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2ShaderResourceBindingsCall1 call = reinterpret_cast<CuteQGles2ShaderResourceBindingsCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2ShaderResourceBindings::create();
  }

  //  void QGles2ShaderResourceBindings::updateResources(UpdateFlags flags)
  void updateResources(
      QRhiShaderResourceBindings::UpdateFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2ShaderResourceBindingsCall2 call = reinterpret_cast<CuteQGles2ShaderResourceBindingsCall2>(taken[2]);
      call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QGles2ShaderResourceBindings::updateResources(flags);
  }

  //  QRhiResource::Type QRhiShaderResourceBindings::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGles2ShaderResourceBindingsCall3 call = reinterpret_cast<CuteQGles2ShaderResourceBindingsCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiShaderResourceBindings::resourceType();
  }
};

//  QGles2ShaderResourceBindings::QGles2ShaderResourceBindings(QRhiImplementa
//      tion *rhi)
extern "C" Q_DECL_EXPORT
QGles2ShaderResourceBindings *ritual_ZN28QGles2ShaderResourceBindingsC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQGles2ShaderResourceBindings(rhi);
}

//  QGles2ShaderResourceBindings::~QGles2ShaderResourceBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGles2ShaderResourceBindingsD1Ev(
    QGles2ShaderResourceBindings *self) {
  delete self;
}

//  void QGles2ShaderResourceBindings::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGles2ShaderResourceBindings7destroyEv(
    QGles2ShaderResourceBindings *self) {
  self->destroy();
}

//  bool QGles2ShaderResourceBindings::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QGles2ShaderResourceBindings6createEv(
    QGles2ShaderResourceBindings *self) {
  return self->create();
}

//  void QGles2ShaderResourceBindings::updateResources(UpdateFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QGles2ShaderResourceBindings15updateResourcesE6QFlagsIN26QRhiShaderResourceBindings10UpdateFlagEE(
    QGles2ShaderResourceBindings *self,
    int flags) {
  self->updateResources(
      QFlags<QRhiShaderResourceBindings::UpdateFlag>::fromInt(flags));
}

//  a Python function taken by a CuteQGles2ShaderResourceBindings, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2ShaderResourceBindings(
    QGles2ShaderResourceBindings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2ShaderResourceBindings *>(self)->take(key, call);
}

//  void QGles2ShaderResourceBindings::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QGles2ShaderResourceBindings7destroyEv(
    QGles2ShaderResourceBindings *self) {
  self->QGles2ShaderResourceBindings::destroy();
}

//  bool QGles2ShaderResourceBindings::create()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QGles2ShaderResourceBindings6createEv(
    QGles2ShaderResourceBindings *self) {
  return self->QGles2ShaderResourceBindings::create();
}

//  void QGles2ShaderResourceBindings::updateResources(UpdateFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QGles2ShaderResourceBindings15updateResourcesE6QFlagsIN26QRhiShaderResourceBindings10UpdateFlagEE(
    QGles2ShaderResourceBindings *self,
    int flags) {
  self->QGles2ShaderResourceBindings::updateResources(
      QFlags<QRhiShaderResourceBindings::UpdateFlag>::fromInt(flags));
}
