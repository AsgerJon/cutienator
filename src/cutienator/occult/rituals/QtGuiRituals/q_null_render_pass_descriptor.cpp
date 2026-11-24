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

//  from src/gui/rhi/qrhinull.cpp, line 842, as _ZNK25QNullRenderPassDescriptor16serializedFormatEv
inline QVector<quint32> QNullRenderPassDescriptor::serializedFormat() const
{
    return {};
}

//  from src/gui/rhi/qrhinull.cpp, line 811, as _ZN25QNullRenderPassDescriptorC1EP18QRhiImplementation
inline QNullRenderPassDescriptor::QNullRenderPassDescriptor(QRhiImplementation *rhi)
    : QRhiRenderPassDescriptor(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 816, as _ZN25QNullRenderPassDescriptorD1Ev
inline QNullRenderPassDescriptor::~QNullRenderPassDescriptor()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 821, as _ZN25QNullRenderPassDescriptor7destroyEv
inline void QNullRenderPassDescriptor::destroy()
{
    QRHI_RES_RHI(QRhiNull);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 828, as _ZNK25QNullRenderPassDescriptor12isCompatibleEPK24QRhiRenderPassDescriptor
inline bool QNullRenderPassDescriptor::isCompatible(const QRhiRenderPassDescriptor *other) const
{
    Q_UNUSED(other);
    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 834, as _ZNK25QNullRenderPassDescriptor33newCompatibleRenderPassDescriptorEv
inline QRhiRenderPassDescriptor *QNullRenderPassDescriptor::newCompatibleRenderPassDescriptor() const
{
    QNullRenderPassDescriptor *rpD = new QNullRenderPassDescriptor(m_rhi);
    QRHI_RES_RHI(QRhiNull);
    rhiD->registerResource(rpD, false);
    return rpD;
}
//  -----------------------------------------------------------------------

//  A QNullRenderPassDescriptor that Python can take functions over in. Every QNullRenderPassDescriptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullRenderPassDescriptorCall0)(const void *, int *);
typedef bool (*CuteQNullRenderPassDescriptorCall1)(const void *, const QRhiRenderPassDescriptor *, int *);
typedef void * (*CuteQNullRenderPassDescriptorCall2)(const void *, int *);
typedef int (*CuteQNullRenderPassDescriptorCall3)(const void *, int *);
typedef void * (*CuteQNullRenderPassDescriptorCall4)(const void *, int *);
class CuteQNullRenderPassDescriptor : public QNullRenderPassDescriptor {
public:
  using QNullRenderPassDescriptor::QNullRenderPassDescriptor;
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

  //  void QNullRenderPassDescriptor::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullRenderPassDescriptorCall0 call = reinterpret_cast<CuteQNullRenderPassDescriptorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullRenderPassDescriptor::destroy();
  }

  //  bool QNullRenderPassDescriptor::isCompatible(const
  //      QRhiRenderPassDescriptor *other) const
  bool isCompatible(const QRhiRenderPassDescriptor *other) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullRenderPassDescriptorCall1 call = reinterpret_cast<CuteQNullRenderPassDescriptorCall1>(taken[1]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QNullRenderPassDescriptor::isCompatible(other);
  }

  //  QRhiRenderPassDescriptor
  //      *QNullRenderPassDescriptor::newCompatibleRenderPassDescriptor()
  //      const
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullRenderPassDescriptorCall2 call = reinterpret_cast<CuteQNullRenderPassDescriptorCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QNullRenderPassDescriptor::newCompatibleRenderPassDescriptor();
  }

  //  QRhiResource::Type QRhiRenderPassDescriptor::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNullRenderPassDescriptorCall3 call = reinterpret_cast<CuteQNullRenderPassDescriptorCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiRenderPassDescriptor::resourceType();
  }

  //  const QRhiNativeHandles *QRhiRenderPassDescriptor::nativeHandles()
  const QRhiNativeHandles *nativeHandles() override {
    if (taken[4]) {
      int handled = 0;
      CuteQNullRenderPassDescriptorCall4 call = reinterpret_cast<CuteQNullRenderPassDescriptorCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiRenderPassDescriptor::nativeHandles();
  }
};

//  QNullRenderPassDescriptor::QNullRenderPassDescriptor(QRhiImplementation
//      *rhi)
extern "C" Q_DECL_EXPORT
QNullRenderPassDescriptor *ritual_ZN25QNullRenderPassDescriptorC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQNullRenderPassDescriptor(rhi);
}

//  QNullRenderPassDescriptor::~QNullRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNullRenderPassDescriptorD1Ev(
    QNullRenderPassDescriptor *self) {
  delete self;
}

//  void QNullRenderPassDescriptor::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QNullRenderPassDescriptor7destroyEv(
    QNullRenderPassDescriptor *self) {
  self->destroy();
}

//  bool QNullRenderPassDescriptor::isCompatible(const
//      QRhiRenderPassDescriptor *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QNullRenderPassDescriptor12isCompatibleEPK24QRhiRenderPassDescriptor(
    const QNullRenderPassDescriptor *self,
    const QRhiRenderPassDescriptor *other) {
  return self->isCompatible(other);
}

//  QRhiRenderPassDescriptor
//      *QNullRenderPassDescriptor::newCompatibleRenderPassDescriptor() const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZNK25QNullRenderPassDescriptor33newCompatibleRenderPassDescriptorEv(
    const QNullRenderPassDescriptor *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  a Python function taken by a CuteQNullRenderPassDescriptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullRenderPassDescriptor(
    QNullRenderPassDescriptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullRenderPassDescriptor *>(self)->take(key, call);
}

//  void QNullRenderPassDescriptor::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QNullRenderPassDescriptor7destroyEv(
    QNullRenderPassDescriptor *self) {
  self->QNullRenderPassDescriptor::destroy();
}

//  bool QNullRenderPassDescriptor::isCompatible(const
//      QRhiRenderPassDescriptor *other) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QNullRenderPassDescriptor12isCompatibleEPK24QRhiRenderPassDescriptor(
    const QNullRenderPassDescriptor *self,
    const QRhiRenderPassDescriptor *other) {
  return self->QNullRenderPassDescriptor::isCompatible(other);
}

//  QRhiRenderPassDescriptor
//      *QNullRenderPassDescriptor::newCompatibleRenderPassDescriptor() const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_own_ZNK25QNullRenderPassDescriptor33newCompatibleRenderPassDescriptorEv(
    const QNullRenderPassDescriptor *self) {
  return self->QNullRenderPassDescriptor::newCompatibleRenderPassDescriptor();
}
