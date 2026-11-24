//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qabstractopenxrgraphics_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qabstractopenxrgraphics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qabstractopenxrgraphics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qabstractopenxrgraphics.cpp, line 15, as _ZN23QAbstractOpenXRGraphics11setupWindowEP12QQuickWindow
inline void QAbstractOpenXRGraphics::setupWindow(QQuickWindow *)
{

}
//  -----------------------------------------------------------------------

//  A QAbstractOpenXRGraphics that Python can take functions over in. Every QAbstractOpenXRGraphics
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractOpenXRGraphicsCall0)(const void *, QQuickWindow *, int *);
typedef bool (*CuteQAbstractOpenXRGraphicsCall1)(const void *, QRhi *, int *);
typedef void * (*CuteQAbstractOpenXRGraphicsCall2)(const void *, int *);
typedef void (*CuteQAbstractOpenXRGraphicsCall3)(const void *, int *);
class CuteQAbstractOpenXRGraphics : public QAbstractOpenXRGraphics {
public:
  using QAbstractOpenXRGraphics::QAbstractOpenXRGraphics;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QAbstractOpenXRGraphics11setupWindowEP12QQuickWindow")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstractOpenXRGraphics17finializeGraphicsEP4QRhi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QAbstractOpenXRGraphics3rhiEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QAbstractOpenXRGraphics16releaseResourcesEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QAbstractOpenXRGraphics::setupWindow(QQuickWindow *a0)
  void setupWindow(QQuickWindow *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractOpenXRGraphicsCall0 call = reinterpret_cast<CuteQAbstractOpenXRGraphicsCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractOpenXRGraphics::setupWindow(a0);
  }

  //  bool QAbstractOpenXRGraphics::finializeGraphics(QRhi *rhi)
  bool finializeGraphics(QRhi *rhi) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractOpenXRGraphicsCall1 call = reinterpret_cast<CuteQAbstractOpenXRGraphicsCall1>(taken[1]);
      bool given = call(this, rhi, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRhi *QAbstractOpenXRGraphics::rhi() const
  QRhi *rhi() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractOpenXRGraphicsCall2 call = reinterpret_cast<CuteQAbstractOpenXRGraphicsCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhi *>(given);
    }
    return {};
  }

  //  void QAbstractOpenXRGraphics::releaseResources()
  void releaseResources() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractOpenXRGraphicsCall3 call = reinterpret_cast<CuteQAbstractOpenXRGraphicsCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractOpenXRGraphics::releaseResources();
  }
};

//  QAbstractOpenXRGraphics::~QAbstractOpenXRGraphics()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractOpenXRGraphicsD1Ev(QAbstractOpenXRGraphics *self) {
  delete self;
}

//  void QAbstractOpenXRGraphics::setupWindow(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractOpenXRGraphics11setupWindowEP12QQuickWindow(
    QAbstractOpenXRGraphics *self,
    QQuickWindow *a0) {
  self->setupWindow(a0);
}

//  bool QAbstractOpenXRGraphics::finializeGraphics(QRhi *rhi)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QAbstractOpenXRGraphics17finializeGraphicsEP4QRhi(
    QAbstractOpenXRGraphics *self,
    QRhi *rhi) {
  return self->finializeGraphics(rhi);
}

//  QRhi *QAbstractOpenXRGraphics::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK23QAbstractOpenXRGraphics3rhiEv(
    const QAbstractOpenXRGraphics *self) {
  return self->rhi();
}

//  void QAbstractOpenXRGraphics::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractOpenXRGraphics16releaseResourcesEv(
    QAbstractOpenXRGraphics *self) {
  self->releaseResources();
}

//  a Python function taken by a CuteQAbstractOpenXRGraphics, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractOpenXRGraphics(
    QAbstractOpenXRGraphics *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractOpenXRGraphics *>(self)->take(key, call);
}

//  void QAbstractOpenXRGraphics::setupWindow(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstractOpenXRGraphics11setupWindowEP12QQuickWindow(
    QAbstractOpenXRGraphics *self,
    QQuickWindow *a0) {
  self->QAbstractOpenXRGraphics::setupWindow(a0);
}

//  void QAbstractOpenXRGraphics::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstractOpenXRGraphics16releaseResourcesEv(
    QAbstractOpenXRGraphics *self) {
  self->QAbstractOpenXRGraphics::releaseResources();
}
