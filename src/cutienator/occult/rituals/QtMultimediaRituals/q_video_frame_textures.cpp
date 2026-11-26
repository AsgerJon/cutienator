//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qhwvideobuffer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qhwvideobuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qvideoframe.h>
#include <cstring>

//  A QVideoFrameTextures that Python can take functions over in. Every QVideoFrameTextures
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQVideoFrameTexturesCall0)(const void *, uint, int *);
typedef void (*CuteQVideoFrameTexturesCall1)(const void *, int *);
class CuteQVideoFrameTextures : public QVideoFrameTextures {
public:
  using QVideoFrameTextures::QVideoFrameTextures;
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

  //  QRhiTexture *QVideoFrameTextures::texture(uint plane) const
  QRhiTexture *texture(uint plane) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQVideoFrameTexturesCall0 call = reinterpret_cast<CuteQVideoFrameTexturesCall0>(taken[0]);
      void * given = call(this, plane, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return {};
  }

  //  void QVideoFrameTextures::onFrameEndInvoked()
  void onFrameEndInvoked() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVideoFrameTexturesCall1 call = reinterpret_cast<CuteQVideoFrameTexturesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QVideoFrameTextures::onFrameEndInvoked();
  }
};

//  QVideoFrameTextures::~QVideoFrameTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoFrameTexturesD1Ev(QVideoFrameTextures *self) {
  delete self;
}

//  QRhiTexture *QVideoFrameTextures::texture(uint plane) const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK19QVideoFrameTextures7textureEj(
    const QVideoFrameTextures *self,
    uint plane) {
  return self->texture(plane);
}

//  void QVideoFrameTextures::onFrameEndInvoked()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoFrameTextures17onFrameEndInvokedEv(
    QVideoFrameTextures *self) {
  self->onFrameEndInvoked();
}

//  QVideoFrameTexturesHandlesUPtr QVideoFrameTextures::takeHandles()
extern "C" Q_DECL_EXPORT
QVideoFrameTexturesHandlesUPtr *ritual_ZN19QVideoFrameTextures11takeHandlesEv(
    QVideoFrameTextures *self) {
  return new QVideoFrameTexturesHandlesUPtr(self->takeHandles());
}

//  void QVideoFrameTextures::setSourceFrame(QVideoFrame sourceFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoFrameTextures14setSourceFrameE11QVideoFrame(
    QVideoFrameTextures *self,
    const QVideoFrame *sourceFrame) {
  self->setSourceFrame(*sourceFrame);
}

//  a Python function taken by a CuteQVideoFrameTextures, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVideoFrameTextures(
    QVideoFrameTextures *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVideoFrameTextures *>(self)->take(key, call);
}

//  void QVideoFrameTextures::onFrameEndInvoked()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QVideoFrameTextures17onFrameEndInvokedEv(
    QVideoFrameTextures *self) {
  self->QVideoFrameTextures::onFrameEndInvoked();
}

//  a QVideoFrameTexturesHandlesUPtr a ritual of QVideoFrameTextures gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVideoFrameTextures__QVideoFrameTexturesHandlesUPtr(
    QVideoFrameTexturesHandlesUPtr *self) {
  delete self;
}
