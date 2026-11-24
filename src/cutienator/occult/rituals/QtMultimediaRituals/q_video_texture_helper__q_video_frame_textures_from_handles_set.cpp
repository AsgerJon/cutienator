//  Written by dev_tooling.RitualGenerator from the records of QtMultimedia/6
//  .12.0/QtMultimedia/private/qvideoframetexturefromsource_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideoframetexturefromsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet that Python can take functions over in. Every QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQVideoTextureHelper_QVideoFrameTexturesFromHandlesSetCall0)(const void *, uint, int *);
typedef void (*CuteQVideoTextureHelper_QVideoFrameTexturesFromHandlesSetCall1)(const void *, int *);
class CuteQVideoTextureHelper_QVideoFrameTexturesFromHandlesSet : public QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet {
public:
  using QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet::QVideoFrameTexturesFromHandlesSet;
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
      CuteQVideoTextureHelper_QVideoFrameTexturesFromHandlesSetCall0 call = reinterpret_cast<CuteQVideoTextureHelper_QVideoFrameTexturesFromHandlesSetCall0>(taken[0]);
      void * given = call(this, plane, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QVideoTextureHelper::QVideoFrameTexturesFromRhiTextureArray::texture(plane);
  }

  //  void QVideoFrameTextures::onFrameEndInvoked()
  void onFrameEndInvoked() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVideoTextureHelper_QVideoFrameTexturesFromHandlesSetCall1 call = reinterpret_cast<CuteQVideoTextureHelper_QVideoFrameTexturesFromHandlesSetCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QVideoFrameTextures::onFrameEndInvoked();
  }
};

//  a Python function taken by a
//      CuteQVideoTextureHelper_QVideoFrameTexturesFromHandlesSet, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVideoTextureHelper_QVideoFrameTexturesFromHandlesSet(
    QVideoTextureHelper::QVideoFrameTexturesFromHandlesSet *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVideoTextureHelper_QVideoFrameTexturesFromHandlesSet *>(self)->take(key, call);
}
