//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrhinull_p.h"
#include <qmath.h>
#include <QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhinull.cpp, line 786, as _ZN12QNullSamplerC1EP18QRhiImplementationN11QRhiSampler6FilterES3_S3_NS2_11AddressModeES4_S4_
inline QNullSampler::QNullSampler(QRhiImplementation *rhi, Filter magFilter, Filter minFilter, Filter mipmapMode,
                           AddressMode u, AddressMode v, AddressMode w)
    : QRhiSampler(rhi, magFilter, minFilter, mipmapMode, u, v, w)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 792, as _ZN12QNullSamplerD1Ev
inline QNullSampler::~QNullSampler()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 797, as _ZN12QNullSampler7destroyEv
inline void QNullSampler::destroy()
{
    QRHI_RES_RHI(QRhiNull);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 804, as _ZN12QNullSampler6createEv
inline bool QNullSampler::create()
{
    QRHI_RES_RHI(QRhiNull);
    rhiD->registerResource(this);
    return true;
}
//  -----------------------------------------------------------------------

//  A QNullSampler that Python can take functions over in. Every QNullSampler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullSamplerCall0)(const void *, int *);
typedef bool (*CuteQNullSamplerCall1)(const void *, int *);
typedef int (*CuteQNullSamplerCall2)(const void *, int *);
class CuteQNullSampler : public QNullSampler {
public:
  using QNullSampler::QNullSampler;
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

  //  void QNullSampler::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullSamplerCall0 call = reinterpret_cast<CuteQNullSamplerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullSampler::destroy();
  }

  //  bool QNullSampler::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullSamplerCall1 call = reinterpret_cast<CuteQNullSamplerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNullSampler::create();
  }

  //  QRhiResource::Type QRhiSampler::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullSamplerCall2 call = reinterpret_cast<CuteQNullSamplerCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSampler::resourceType();
  }
};

//  QNullSampler::QNullSampler(QRhiImplementation *rhi, Filter magFilter,
//      Filter minFilter, Filter mipmapMode, AddressMode u, AddressMode v,
//      AddressMode w)
extern "C" Q_DECL_EXPORT
QNullSampler *ritual_ZN12QNullSamplerC1EP18QRhiImplementationN11QRhiSampler6FilterES3_S3_NS2_11AddressModeES4_S4_(
    QRhiImplementation *rhi,
    QRhiSampler::Filter magFilter,
    QRhiSampler::Filter minFilter,
    QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u,
    QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w) {
  return new CuteQNullSampler(
      rhi,
      magFilter,
      minFilter,
      mipmapMode,
      u,
      v,
      w);
}

//  QNullSampler::~QNullSampler()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QNullSamplerD1Ev(QNullSampler *self) {
  delete self;
}

//  void QNullSampler::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QNullSampler7destroyEv(QNullSampler *self) {
  self->destroy();
}

//  bool QNullSampler::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QNullSampler6createEv(QNullSampler *self) {
  return self->create();
}

//  a Python function taken by a CuteQNullSampler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullSampler(
    QNullSampler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullSampler *>(self)->take(key, call);
}

//  void QNullSampler::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QNullSampler7destroyEv(QNullSampler *self) {
  self->QNullSampler::destroy();
}

//  bool QNullSampler::create()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QNullSampler6createEv(QNullSampler *self) {
  return self->QNullSampler::create();
}
