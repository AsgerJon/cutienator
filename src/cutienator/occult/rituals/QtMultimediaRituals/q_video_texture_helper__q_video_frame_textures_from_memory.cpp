//  Written by dev_tooling.RitualGenerator from the records of QtMultimedia/6
//  .12.0/QtMultimedia/private/qvideoframetexturefromsource_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideoframetexturefromsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QVideoTextureHelper::QVideoFrameTexturesFromMemory that Python can take functions over in. Every QVideoTextureHelper::QVideoFrameTexturesFromMemory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVideoTextureHelper_QVideoFrameTexturesFromMemoryCall0)(const void *, int *);
typedef void * (*CuteQVideoTextureHelper_QVideoFrameTexturesFromMemoryCall1)(const void *, uint, int *);
class CuteQVideoTextureHelper_QVideoFrameTexturesFromMemory : public QVideoTextureHelper::QVideoFrameTexturesFromMemory {
public:
  using QVideoTextureHelper::QVideoFrameTexturesFromMemory::QVideoFrameTexturesFromMemory;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QVideoFrameTextures17onFrameEndInvokedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QVideoFrameTextures7textureEj")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QVideoTextureHelper::QVideoFrameTexturesFromMemory::onFrameEndIn
  //      voked()
  void onFrameEndInvoked() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVideoTextureHelper_QVideoFrameTexturesFromMemoryCall0 call = reinterpret_cast<CuteQVideoTextureHelper_QVideoFrameTexturesFromMemoryCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVideoTextureHelper::QVideoFrameTexturesFromMemory::onFrameEndInvoked();
  }

  //  QRhiTexture *QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureAr
  //      ray::texture(uint plane) const
  QRhiTexture *texture(uint plane) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQVideoTextureHelper_QVideoFrameTexturesFromMemoryCall1 call = reinterpret_cast<CuteQVideoTextureHelper_QVideoFrameTexturesFromMemoryCall1>(taken[1]);
      void * given = call(this, plane, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::texture(plane);
  }
};

//  a Python function taken by a
//      CuteQVideoTextureHelper_QVideoFrameTexturesFromMemory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVideoTextureHelper_QVideoFrameTexturesFromMemory(
    QVideoTextureHelper::QVideoFrameTexturesFromMemory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVideoTextureHelper_QVideoFrameTexturesFromMemory *>(self)->take(key, call);
}
