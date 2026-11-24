//  Written by dev_tooling.RitualGenerator from the records of QtMultimedia/6
//  .12.0/QtMultimedia/private/qvideoframetexturefromsource_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideoframetexturefromsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray that Python can take functions over in. Every QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArrayCall0)(const void *, uint, int *);
typedef void (*CuteQVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArrayCall1)(const void *, int *);
class CuteQVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArray : public QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray {
public:
  using QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::QVideoFrameTexturesFromRhiTextureArray;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QVideoFrameTextures7textureEj")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QVideoFrameTextures17onFrameEndInvokedEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QRhiTexture *QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureAr
  //      ray::texture(uint plane) const
  QRhiTexture *texture(uint plane) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArrayCall0 call = reinterpret_cast<CuteQVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArrayCall0>(taken[0]);
      void * given = call(this, plane, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::texture(plane);
  }

  //  void QVideoFrameTextures::onFrameEndInvoked()
  void onFrameEndInvoked() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArrayCall1 call = reinterpret_cast<CuteQVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArrayCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QVideoFrameTextures::onFrameEndInvoked();
  }
};

//  a Python function taken by a
//      CuteQVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArray, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArray(
    QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVideoTextureHelper_QVideoFrameTexturesFromRhiTextureArray *>(self)->take(key, call);
}
