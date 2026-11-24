//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qpaintedtextureimage_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qpaintedtextureimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QPaintedTextureImageDataGenerator that Python can take functions over in. Every Qt3DRender::QPaintedTextureImageDataGenerator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qintptr (*CuteQt3DRender_QPaintedTextureImageDataGeneratorCall0)(const void *, int *);
class CuteQt3DRender_QPaintedTextureImageDataGenerator : public Qt3DRender::QPaintedTextureImageDataGenerator {
public:
  using Qt3DRender::QPaintedTextureImageDataGenerator::QPaintedTextureImageDataGenerator;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore16QAbstractFunctor2idEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  qintptr Qt3DRender::QPaintedTextureImageDataGenerator::id() const
  qintptr id() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QPaintedTextureImageDataGeneratorCall0 call = reinterpret_cast<CuteQt3DRender_QPaintedTextureImageDataGeneratorCall0>(taken[0]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DRender::QPaintedTextureImageDataGenerator::id();
  }
};

//  qintptr Qt3DRender::QPaintedTextureImageDataGenerator::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK10Qt3DRender33QPaintedTextureImageDataGenerator2idEv(
    const Qt3DRender::QPaintedTextureImageDataGenerator *self) {
  return self->id();
}

//  a Python function taken by a
//      CuteQt3DRender_QPaintedTextureImageDataGenerator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QPaintedTextureImageDataGenerator(
    Qt3DRender::QPaintedTextureImageDataGenerator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QPaintedTextureImageDataGenerator *>(self)->take(key, call);
}

//  qintptr Qt3DRender::QPaintedTextureImageDataGenerator::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK10Qt3DRender33QPaintedTextureImageDataGenerator2idEv(
    const Qt3DRender::QPaintedTextureImageDataGenerator *self) {
  return self->Qt3DRender::QPaintedTextureImageDataGenerator::id();
}
