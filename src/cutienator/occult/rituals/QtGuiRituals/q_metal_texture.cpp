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
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QMetalTexture that Python can take functions over in. Every QMetalTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalTextureCall0)(const void *, int *);
typedef bool (*CuteQMetalTextureCall1)(const void *, int *);
typedef bool (*CuteQMetalTextureCall2)(const void *, const QRhiTexture::NativeTexture *, int *);
typedef const QRhiTexture::NativeTexture * (*CuteQMetalTextureCall3)(const void *, int *);
typedef int (*CuteQMetalTextureCall4)(const void *, int *);
typedef void (*CuteQMetalTextureCall5)(const void *, int, int *);
class CuteQMetalTexture : public QMetalTexture {
public:
  using QMetalTexture::QMetalTexture;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture10createFromENS_13NativeTextureE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture13nativeTextureEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture15setNativeLayoutEi")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  void QMetalTexture::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalTextureCall0 call = reinterpret_cast<CuteQMetalTextureCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalTexture::destroy();
  }

  //  bool QMetalTexture::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalTextureCall1 call = reinterpret_cast<CuteQMetalTextureCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalTexture::create();
  }

  //  bool QMetalTexture::createFrom(NativeTexture src)
  bool createFrom(QRhiTexture::NativeTexture src) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalTextureCall2 call = reinterpret_cast<CuteQMetalTextureCall2>(taken[2]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QMetalTexture::createFrom(src);
  }

  //  NativeTexture QMetalTexture::nativeTexture()
  QRhiTexture::NativeTexture nativeTexture() override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetalTextureCall3 call = reinterpret_cast<CuteQMetalTextureCall3>(taken[3]);
      const QRhiTexture::NativeTexture * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMetalTexture::nativeTexture();
  }

  //  QRhiResource::Type QRhiTexture::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQMetalTextureCall4 call = reinterpret_cast<CuteQMetalTextureCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiTexture::resourceType();
  }

  //  void QRhiTexture::setNativeLayout(int layout)
  void setNativeLayout(int layout) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMetalTextureCall5 call = reinterpret_cast<CuteQMetalTextureCall5>(taken[5]);
      call(this, layout, &handled);
      if (handled) return;
    }
    QRhiTexture::setNativeLayout(layout);
  }
};

//  a Python function taken by a CuteQMetalTexture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalTexture(
    QMetalTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalTexture *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
