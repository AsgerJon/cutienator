//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QRhiResource that Python can take functions over in. Every QRhiResource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiResourceCall0)(const void *, int *);
typedef void (*CuteQRhiResourceCall1)(const void *, int *);
class CuteQRhiResource : public QRhiResource {
public:
  using QRhiResource::QRhiResource;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  Type QRhiResource::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiResourceCall0 call = reinterpret_cast<CuteQRhiResourceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return {};
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiResourceCall1 call = reinterpret_cast<CuteQRhiResourceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::~QRhiResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiResourceD1Ev(QRhiResource *self) {
  delete self;
}

//  Type QRhiResource::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK12QRhiResource12resourceTypeEv(
    const QRhiResource *self) {
  return self->resourceType();
}

//  void QRhiResource::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiResource7destroyEv(QRhiResource *self) {
  self->destroy();
}

//  void QRhiResource::deleteLater()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiResource11deleteLaterEv(QRhiResource *self) {
  self->deleteLater();
}

//  QByteArray QRhiResource::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QRhiResource4nameEv(const QRhiResource *self) {
  return new QByteArray(self->name());
}

//  void QRhiResource::setName(const QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiResource7setNameERK10QByteArray(
    QRhiResource *self,
    const QByteArray *name) {
  self->setName(*name);
}

//  quint64 QRhiResource::globalResourceId() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK12QRhiResource16globalResourceIdEv(
    const QRhiResource *self) {
  return self->globalResourceId();
}

//  QRhi *QRhiResource::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK12QRhiResource3rhiEv(const QRhiResource *self) {
  return self->rhi();
}

//  QRhiResource::QRhiResource(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QRhiResource *ritual_ZN12QRhiResourceC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQRhiResource(rhi);
}

//  a Python function taken by a CuteQRhiResource, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiResource(
    QRhiResource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiResource *>(self)->take(key, call);
}
