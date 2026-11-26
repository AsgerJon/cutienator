//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <QtCore/QVector>

//  A QRhiRenderPassDescriptor that Python can take functions over in. Every QRhiRenderPassDescriptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiRenderPassDescriptorCall0)(const void *, int *);
typedef bool (*CuteQRhiRenderPassDescriptorCall1)(const void *, const QRhiRenderPassDescriptor *, int *);
typedef void * (*CuteQRhiRenderPassDescriptorCall2)(const void *, int *);
typedef void * (*CuteQRhiRenderPassDescriptorCall3)(const void *, int *);
typedef void (*CuteQRhiRenderPassDescriptorCall4)(const void *, int *);
class CuteQRhiRenderPassDescriptor : public QRhiRenderPassDescriptor {
public:
  using QRhiRenderPassDescriptor::QRhiRenderPassDescriptor;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QRhiRenderPassDescriptor12isCompatibleEPKS_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QRhiRenderPassDescriptor13nativeHandlesEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QRhiRenderPassDescriptor33newCompatibleRenderPassDescriptorEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiRenderPassDescriptor::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiRenderPassDescriptorCall0 call = reinterpret_cast<CuteQRhiRenderPassDescriptorCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiRenderPassDescriptor::resourceType();
  }

  //  bool QRhiRenderPassDescriptor::isCompatible(const
  //      QRhiRenderPassDescriptor *other) const
  bool isCompatible(const QRhiRenderPassDescriptor *other) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiRenderPassDescriptorCall1 call = reinterpret_cast<CuteQRhiRenderPassDescriptorCall1>(taken[1]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  const QRhiNativeHandles *QRhiRenderPassDescriptor::nativeHandles()
  const QRhiNativeHandles *nativeHandles() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiRenderPassDescriptorCall2 call = reinterpret_cast<CuteQRhiRenderPassDescriptorCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiRenderPassDescriptor::nativeHandles();
  }

  //  QRhiRenderPassDescriptor
  //      *QRhiRenderPassDescriptor::newCompatibleRenderPassDescriptor()
  //      const
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiRenderPassDescriptorCall3 call = reinterpret_cast<CuteQRhiRenderPassDescriptorCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return {};
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiRenderPassDescriptorCall4 call = reinterpret_cast<CuteQRhiRenderPassDescriptorCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiRenderPassDescriptor::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK24QRhiRenderPassDescriptor12resourceTypeEv(
    const QRhiRenderPassDescriptor *self) {
  return self->resourceType();
}

//  bool QRhiRenderPassDescriptor::isCompatible(const
//      QRhiRenderPassDescriptor *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QRhiRenderPassDescriptor12isCompatibleEPKS_(
    const QRhiRenderPassDescriptor *self,
    const QRhiRenderPassDescriptor *other) {
  return self->isCompatible(other);
}

//  const QRhiNativeHandles *QRhiRenderPassDescriptor::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN24QRhiRenderPassDescriptor13nativeHandlesEv(
    QRhiRenderPassDescriptor *self) {
  return self->nativeHandles();
}

//  QRhiRenderPassDescriptor
//      *QRhiRenderPassDescriptor::newCompatibleRenderPassDescriptor() const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZNK24QRhiRenderPassDescriptor33newCompatibleRenderPassDescriptorEv(
    const QRhiRenderPassDescriptor *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  QVector<quint32> QRhiRenderPassDescriptor::serializedFormat() const
extern "C" Q_DECL_EXPORT
QVector<quint32> *ritual_ZNK24QRhiRenderPassDescriptor16serializedFormatEv(
    const QRhiRenderPassDescriptor *self) {
  return new QVector<quint32>(self->serializedFormat());
}

//  a Python function taken by a CuteQRhiRenderPassDescriptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiRenderPassDescriptor(
    QRhiRenderPassDescriptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiRenderPassDescriptor *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiRenderPassDescriptor::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK24QRhiRenderPassDescriptor12resourceTypeEv(
    const QRhiRenderPassDescriptor *self) {
  return self->QRhiRenderPassDescriptor::resourceType();
}

//  const QRhiNativeHandles *QRhiRenderPassDescriptor::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_own_ZN24QRhiRenderPassDescriptor13nativeHandlesEv(
    QRhiRenderPassDescriptor *self) {
  return self->QRhiRenderPassDescriptor::nativeHandles();
}

//  a QVector<quint32> a ritual of QRhiRenderPassDescriptor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRhiRenderPassDescriptor__QVector_quint32(
    QVector<quint32> *self) {
  delete self;
}
