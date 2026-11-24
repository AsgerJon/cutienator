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

//  from src/gui/rhi/qrhigles2.cpp, line 6434, as _ZN13QGles2SamplerD1Ev
inline QGles2Sampler::~QGles2Sampler()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 6439, as _ZN13QGles2Sampler7destroyEv
inline void QGles2Sampler::destroy()
{
    QRHI_RES_RHI(QRhiGles2);
    if (rhiD)
        rhiD->unregisterResource(this);
}
//  -----------------------------------------------------------------------

//  A QGles2Sampler that Python can take functions over in. Every QGles2Sampler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2SamplerCall0)(const void *, int *);
typedef bool (*CuteQGles2SamplerCall1)(const void *, int *);
typedef int (*CuteQGles2SamplerCall2)(const void *, int *);
class CuteQGles2Sampler : public QGles2Sampler {
public:
  using QGles2Sampler::QGles2Sampler;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiSampler6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QGles2Sampler::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2SamplerCall0 call = reinterpret_cast<CuteQGles2SamplerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2Sampler::destroy();
  }

  //  bool QGles2Sampler::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2SamplerCall1 call = reinterpret_cast<CuteQGles2SamplerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2Sampler::create();
  }

  //  QRhiResource::Type QRhiSampler::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2SamplerCall2 call = reinterpret_cast<CuteQGles2SamplerCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSampler::resourceType();
  }
};

//  QGles2Sampler::~QGles2Sampler()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGles2SamplerD1Ev(QGles2Sampler *self) {
  delete self;
}

//  void QGles2Sampler::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGles2Sampler7destroyEv(QGles2Sampler *self) {
  self->destroy();
}

//  a Python function taken by a CuteQGles2Sampler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2Sampler(
    QGles2Sampler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2Sampler *>(self)->take(key, call);
}

//  void QGles2Sampler::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGles2Sampler7destroyEv(QGles2Sampler *self) {
  self->QGles2Sampler::destroy();
}
