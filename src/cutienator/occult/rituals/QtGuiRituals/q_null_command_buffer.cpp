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

//  from src/gui/rhi/qrhinull.cpp, line 1027, as _ZN18QNullCommandBufferC1EP18QRhiImplementation
inline QNullCommandBuffer::QNullCommandBuffer(QRhiImplementation *rhi)
    : QRhiCommandBuffer(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 1032, as _ZN18QNullCommandBufferD1Ev
inline QNullCommandBuffer::~QNullCommandBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 1037, as _ZN18QNullCommandBuffer7destroyEv
inline void QNullCommandBuffer::destroy()
{
    // nothing to do here
}
//  -----------------------------------------------------------------------

//  A QNullCommandBuffer that Python can take functions over in. Every QNullCommandBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullCommandBufferCall0)(const void *, int *);
typedef int (*CuteQNullCommandBufferCall1)(const void *, int *);
class CuteQNullCommandBuffer : public QNullCommandBuffer {
public:
  using QNullCommandBuffer::QNullCommandBuffer;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QNullCommandBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullCommandBufferCall0 call = reinterpret_cast<CuteQNullCommandBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullCommandBuffer::destroy();
  }

  //  QRhiResource::Type QRhiCommandBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullCommandBufferCall1 call = reinterpret_cast<CuteQNullCommandBufferCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiCommandBuffer::resourceType();
  }
};

//  QNullCommandBuffer::QNullCommandBuffer(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QNullCommandBuffer *ritual_ZN18QNullCommandBufferC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQNullCommandBuffer(rhi);
}

//  QNullCommandBuffer::~QNullCommandBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNullCommandBufferD1Ev(QNullCommandBuffer *self) {
  delete self;
}

//  void QNullCommandBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNullCommandBuffer7destroyEv(QNullCommandBuffer *self) {
  self->destroy();
}

//  a Python function taken by a CuteQNullCommandBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullCommandBuffer(
    QNullCommandBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullCommandBuffer *>(self)->take(key, call);
}

//  void QNullCommandBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QNullCommandBuffer7destroyEv(QNullCommandBuffer *self) {
  self->QNullCommandBuffer::destroy();
}
