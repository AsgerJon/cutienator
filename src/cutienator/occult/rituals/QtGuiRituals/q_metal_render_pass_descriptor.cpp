//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(metal)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhimetal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <QtCore/QVector>

//  A QMetalRenderPassDescriptor that Python can take functions over in. Every QMetalRenderPassDescriptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalRenderPassDescriptorCall0)(const void *, int *);
typedef bool (*CuteQMetalRenderPassDescriptorCall1)(const void *, const QRhiRenderPassDescriptor *, int *);
typedef void * (*CuteQMetalRenderPassDescriptorCall2)(const void *, int *);
typedef int (*CuteQMetalRenderPassDescriptorCall3)(const void *, int *);
typedef void * (*CuteQMetalRenderPassDescriptorCall4)(const void *, int *);
class CuteQMetalRenderPassDescriptor : public QMetalRenderPassDescriptor {
public:
  using QMetalRenderPassDescriptor::QMetalRenderPassDescriptor;
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

  //  void QMetalRenderPassDescriptor::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalRenderPassDescriptorCall0 call = reinterpret_cast<CuteQMetalRenderPassDescriptorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalRenderPassDescriptor::destroy();
  }

  //  bool QMetalRenderPassDescriptor::isCompatible(const
  //      QRhiRenderPassDescriptor *other) const
  bool isCompatible(const QRhiRenderPassDescriptor *other) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalRenderPassDescriptorCall1 call = reinterpret_cast<CuteQMetalRenderPassDescriptorCall1>(taken[1]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QMetalRenderPassDescriptor::isCompatible(other);
  }

  //  QRhiRenderPassDescriptor
  //      *QMetalRenderPassDescriptor::newCompatibleRenderPassDescriptor()
  //      const
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalRenderPassDescriptorCall2 call = reinterpret_cast<CuteQMetalRenderPassDescriptorCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QMetalRenderPassDescriptor::newCompatibleRenderPassDescriptor();
  }

  //  QRhiResource::Type QRhiRenderPassDescriptor::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetalRenderPassDescriptorCall3 call = reinterpret_cast<CuteQMetalRenderPassDescriptorCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiRenderPassDescriptor::resourceType();
  }

  //  const QRhiNativeHandles *QRhiRenderPassDescriptor::nativeHandles()
  const QRhiNativeHandles *nativeHandles() override {
    if (taken[4]) {
      int handled = 0;
      CuteQMetalRenderPassDescriptorCall4 call = reinterpret_cast<CuteQMetalRenderPassDescriptorCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiRenderPassDescriptor::nativeHandles();
  }
};

//  void QMetalRenderPassDescriptor::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMetalRenderPassDescriptor7destroyEv(
    QMetalRenderPassDescriptor *self) {
  self->destroy();
}

//  bool QMetalRenderPassDescriptor::isCompatible(const
//      QRhiRenderPassDescriptor *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QMetalRenderPassDescriptor12isCompatibleEPK24QRhiRenderPassDescriptor(
    const QMetalRenderPassDescriptor *self,
    const QRhiRenderPassDescriptor *other) {
  return self->isCompatible(other);
}

//  QRhiRenderPassDescriptor
//      *QMetalRenderPassDescriptor::newCompatibleRenderPassDescriptor()
//      const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZNK26QMetalRenderPassDescriptor33newCompatibleRenderPassDescriptorEv(
    const QMetalRenderPassDescriptor *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  QVector<quint32> QMetalRenderPassDescriptor::serializedFormat() const
extern "C" Q_DECL_EXPORT
QVector<quint32> *ritual_ZNK26QMetalRenderPassDescriptor16serializedFormatEv(
    const QMetalRenderPassDescriptor *self) {
  return new QVector<quint32>(self->serializedFormat());
}

//  a Python function taken by a CuteQMetalRenderPassDescriptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalRenderPassDescriptor(
    QMetalRenderPassDescriptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalRenderPassDescriptor *>(self)->take(key, call);
}

//  a QVector<quint32> a ritual of QMetalRenderPassDescriptor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMetalRenderPassDescriptor__QVector_quint32(
    QVector<quint32> *self) {
  delete self;
}

#endif  // QT_CONFIG(metal)
