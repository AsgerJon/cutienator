//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhigles2_p.h>
#include <QtGui/QOffscreenSurface>
#include <QtGui/QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpa/qplatformopenglcontext.h>
#include <QtCore/qmath.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhigles2.cpp, line 7195, as _ZN19QGles2CommandBufferC1EP18QRhiImplementation
inline QGles2CommandBuffer::QGles2CommandBuffer(QRhiImplementation *rhi)
    : QRhiCommandBuffer(rhi)
{
    resetState();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7201, as _ZN19QGles2CommandBufferD1Ev
inline QGles2CommandBuffer::~QGles2CommandBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7206, as _ZN19QGles2CommandBuffer7destroyEv
inline void QGles2CommandBuffer::destroy()
{
    // nothing to do here
}
//  -----------------------------------------------------------------------

//  A QGles2CommandBuffer that Python can take functions over in. Every QGles2CommandBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2CommandBufferCall0)(const void *, int *);
typedef int (*CuteQGles2CommandBufferCall1)(const void *, int *);
class CuteQGles2CommandBuffer : public QGles2CommandBuffer {
public:
  using QGles2CommandBuffer::QGles2CommandBuffer;
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

  //  void QGles2CommandBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2CommandBufferCall0 call = reinterpret_cast<CuteQGles2CommandBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2CommandBuffer::destroy();
  }

  //  QRhiResource::Type QRhiCommandBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2CommandBufferCall1 call = reinterpret_cast<CuteQGles2CommandBufferCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiCommandBuffer::resourceType();
  }
};

//  QGles2CommandBuffer::QGles2CommandBuffer(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QGles2CommandBuffer *ritual_ZN19QGles2CommandBufferC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQGles2CommandBuffer(rhi);
}

//  QGles2CommandBuffer::~QGles2CommandBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGles2CommandBufferD1Ev(QGles2CommandBuffer *self) {
  delete self;
}

//  void QGles2CommandBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGles2CommandBuffer7destroyEv(QGles2CommandBuffer *self) {
  self->destroy();
}

//  void QGles2CommandBuffer::resetCommands()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGles2CommandBuffer13resetCommandsEv(
    QGles2CommandBuffer *self) {
  self->resetCommands();
}

//  void QGles2CommandBuffer::resetState()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGles2CommandBuffer10resetStateEv(
    QGles2CommandBuffer *self) {
  self->resetState();
}

//  void QGles2CommandBuffer::resetCachedState()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGles2CommandBuffer16resetCachedStateEv(
    QGles2CommandBuffer *self) {
  self->resetCachedState();
}

//  a Python function taken by a CuteQGles2CommandBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2CommandBuffer(
    QGles2CommandBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2CommandBuffer *>(self)->take(key, call);
}

//  void QGles2CommandBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGles2CommandBuffer7destroyEv(
    QGles2CommandBuffer *self) {
  self->QGles2CommandBuffer::destroy();
}

#endif  // QT_CONFIG(opengl)
