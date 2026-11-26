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
#include <QtGui/private/qrhinull_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhinull.cpp, line 1003, as _ZN20QNullComputePipelineC1EP18QRhiImplementation
inline QNullComputePipeline::QNullComputePipeline(QRhiImplementation *rhi)
    : QRhiComputePipeline(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 1008, as _ZN20QNullComputePipelineD1Ev
inline QNullComputePipeline::~QNullComputePipeline()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 1013, as _ZN20QNullComputePipeline7destroyEv
inline void QNullComputePipeline::destroy()
{
    QRHI_RES_RHI(QRhiNull);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 1020, as _ZN20QNullComputePipeline6createEv
inline bool QNullComputePipeline::create()
{
    QRHI_RES_RHI(QRhiNull);
    rhiD->registerResource(this);
    return true;
}
//  -----------------------------------------------------------------------

//  A QNullComputePipeline that Python can take functions over in. Every QNullComputePipeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullComputePipelineCall0)(const void *, int *);
typedef bool (*CuteQNullComputePipelineCall1)(const void *, int *);
typedef int (*CuteQNullComputePipelineCall2)(const void *, int *);
class CuteQNullComputePipeline : public QNullComputePipeline {
public:
  using QNullComputePipeline::QNullComputePipeline;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QRhiComputePipeline6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QNullComputePipeline::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullComputePipelineCall0 call = reinterpret_cast<CuteQNullComputePipelineCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullComputePipeline::destroy();
  }

  //  bool QNullComputePipeline::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullComputePipelineCall1 call = reinterpret_cast<CuteQNullComputePipelineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNullComputePipeline::create();
  }

  //  QRhiResource::Type QRhiComputePipeline::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullComputePipelineCall2 call = reinterpret_cast<CuteQNullComputePipelineCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiComputePipeline::resourceType();
  }
};

//  QNullComputePipeline::QNullComputePipeline(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QNullComputePipeline *ritual_ZN20QNullComputePipelineC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQNullComputePipeline(rhi);
}

//  QNullComputePipeline::~QNullComputePipeline()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNullComputePipelineD1Ev(QNullComputePipeline *self) {
  delete self;
}

//  void QNullComputePipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNullComputePipeline7destroyEv(QNullComputePipeline *self) {
  self->destroy();
}

//  bool QNullComputePipeline::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QNullComputePipeline6createEv(QNullComputePipeline *self) {
  return self->create();
}

//  a Python function taken by a CuteQNullComputePipeline, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullComputePipeline(
    QNullComputePipeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullComputePipeline *>(self)->take(key, call);
}

//  void QNullComputePipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QNullComputePipeline7destroyEv(
    QNullComputePipeline *self) {
  self->QNullComputePipeline::destroy();
}

//  bool QNullComputePipeline::create()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QNullComputePipeline6createEv(
    QNullComputePipeline *self) {
  return self->QNullComputePipeline::create();
}
