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

//  from src/gui/rhi/qrhigles2.cpp, line 6493, as _ZNK26QGles2RenderPassDescriptor16serializedFormatEv
inline QVector<quint32> QGles2RenderPassDescriptor::serializedFormat() const
{
    return {};
}

//  from src/gui/rhi/qrhigles2.cpp, line 6462, as _ZN26QGles2RenderPassDescriptorC1EP18QRhiImplementation
inline QGles2RenderPassDescriptor::QGles2RenderPassDescriptor(QRhiImplementation *rhi)
    : QRhiRenderPassDescriptor(rhi)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6467, as _ZN26QGles2RenderPassDescriptorD1Ev
inline QGles2RenderPassDescriptor::~QGles2RenderPassDescriptor()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 6472, as _ZN26QGles2RenderPassDescriptor7destroyEv
inline void QGles2RenderPassDescriptor::destroy()
{
    QRHI_RES_RHI(QRhiGles2);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhigles2.cpp, line 6479, as _ZNK26QGles2RenderPassDescriptor12isCompatibleEPK24QRhiRenderPassDescriptor
inline bool QGles2RenderPassDescriptor::isCompatible(const QRhiRenderPassDescriptor *other) const
{
    Q_UNUSED(other);
    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6485, as _ZNK26QGles2RenderPassDescriptor33newCompatibleRenderPassDescriptorEv
inline QRhiRenderPassDescriptor *QGles2RenderPassDescriptor::newCompatibleRenderPassDescriptor() const
{
    QGles2RenderPassDescriptor *rpD = new QGles2RenderPassDescriptor(m_rhi);
    QRHI_RES_RHI(QRhiGles2);
    rhiD->registerResource(rpD, false);
    return rpD;
}
//  -----------------------------------------------------------------------

//  A QGles2RenderPassDescriptor that Python can take functions over in. Every QGles2RenderPassDescriptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2RenderPassDescriptorCall0)(const void *, int *);
typedef bool (*CuteQGles2RenderPassDescriptorCall1)(const void *, const QRhiRenderPassDescriptor *, int *);
typedef void * (*CuteQGles2RenderPassDescriptorCall2)(const void *, int *);
typedef int (*CuteQGles2RenderPassDescriptorCall3)(const void *, int *);
typedef void * (*CuteQGles2RenderPassDescriptorCall4)(const void *, int *);
class CuteQGles2RenderPassDescriptor : public QGles2RenderPassDescriptor {
public:
  using QGles2RenderPassDescriptor::QGles2RenderPassDescriptor;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QRhiRenderPassDescriptor12isCompatibleEPKS_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QRhiRenderPassDescriptor33newCompatibleRenderPassDescriptorEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QRhiRenderPassDescriptor13nativeHandlesEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QGles2RenderPassDescriptor::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2RenderPassDescriptorCall0 call = reinterpret_cast<CuteQGles2RenderPassDescriptorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2RenderPassDescriptor::destroy();
  }

  //  bool QGles2RenderPassDescriptor::isCompatible(const
  //      QRhiRenderPassDescriptor *other) const
  bool isCompatible(const QRhiRenderPassDescriptor *other) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2RenderPassDescriptorCall1 call = reinterpret_cast<CuteQGles2RenderPassDescriptorCall1>(taken[1]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QGles2RenderPassDescriptor::isCompatible(other);
  }

  //  QRhiRenderPassDescriptor
  //      *QGles2RenderPassDescriptor::newCompatibleRenderPassDescriptor()
  //      const
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2RenderPassDescriptorCall2 call = reinterpret_cast<CuteQGles2RenderPassDescriptorCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QGles2RenderPassDescriptor::newCompatibleRenderPassDescriptor();
  }

  //  QRhiResource::Type QRhiRenderPassDescriptor::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGles2RenderPassDescriptorCall3 call = reinterpret_cast<CuteQGles2RenderPassDescriptorCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiRenderPassDescriptor::resourceType();
  }

  //  const QRhiNativeHandles *QRhiRenderPassDescriptor::nativeHandles()
  const QRhiNativeHandles *nativeHandles() override {
    if (taken[4]) {
      int handled = 0;
      CuteQGles2RenderPassDescriptorCall4 call = reinterpret_cast<CuteQGles2RenderPassDescriptorCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiRenderPassDescriptor::nativeHandles();
  }
};

//  QGles2RenderPassDescriptor::QGles2RenderPassDescriptor(QRhiImplementation
//      *rhi)
extern "C" Q_DECL_EXPORT
QGles2RenderPassDescriptor *ritual_ZN26QGles2RenderPassDescriptorC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQGles2RenderPassDescriptor(rhi);
}

//  QGles2RenderPassDescriptor::~QGles2RenderPassDescriptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGles2RenderPassDescriptorD1Ev(
    QGles2RenderPassDescriptor *self) {
  delete self;
}

//  void QGles2RenderPassDescriptor::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGles2RenderPassDescriptor7destroyEv(
    QGles2RenderPassDescriptor *self) {
  self->destroy();
}

//  bool QGles2RenderPassDescriptor::isCompatible(const
//      QRhiRenderPassDescriptor *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QGles2RenderPassDescriptor12isCompatibleEPK24QRhiRenderPassDescriptor(
    const QGles2RenderPassDescriptor *self,
    const QRhiRenderPassDescriptor *other) {
  return self->isCompatible(other);
}

//  QRhiRenderPassDescriptor
//      *QGles2RenderPassDescriptor::newCompatibleRenderPassDescriptor()
//      const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZNK26QGles2RenderPassDescriptor33newCompatibleRenderPassDescriptorEv(
    const QGles2RenderPassDescriptor *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  a Python function taken by a CuteQGles2RenderPassDescriptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2RenderPassDescriptor(
    QGles2RenderPassDescriptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2RenderPassDescriptor *>(self)->take(key, call);
}

//  void QGles2RenderPassDescriptor::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QGles2RenderPassDescriptor7destroyEv(
    QGles2RenderPassDescriptor *self) {
  self->QGles2RenderPassDescriptor::destroy();
}

//  bool QGles2RenderPassDescriptor::isCompatible(const
//      QRhiRenderPassDescriptor *other) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QGles2RenderPassDescriptor12isCompatibleEPK24QRhiRenderPassDescriptor(
    const QGles2RenderPassDescriptor *self,
    const QRhiRenderPassDescriptor *other) {
  return self->QGles2RenderPassDescriptor::isCompatible(other);
}

//  QRhiRenderPassDescriptor
//      *QGles2RenderPassDescriptor::newCompatibleRenderPassDescriptor()
//      const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_own_ZNK26QGles2RenderPassDescriptor33newCompatibleRenderPassDescriptorEv(
    const QGles2RenderPassDescriptor *self) {
  return self->QGles2RenderPassDescriptor::newCompatibleRenderPassDescriptor();
}

#endif  // QT_CONFIG(opengl)
