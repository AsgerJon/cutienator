//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qtextureimagedatagenerator.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DRender/qtextureimagedatagenerator.h>
#include <cstring>

//  A Qt3DRender::QTextureImageDataGenerator that Python can take functions over in. Every Qt3DRender::QTextureImageDataGenerator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qintptr (*CuteQt3DRender_QTextureImageDataGeneratorCall0)(const void *, int *);
class CuteQt3DRender_QTextureImageDataGenerator : public Qt3DRender::QTextureImageDataGenerator {
public:
  using Qt3DRender::QTextureImageDataGenerator::QTextureImageDataGenerator;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore16QAbstractFunctor2idEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  qintptr Qt3DCore::QAbstractFunctor::id() const
  qintptr id() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QTextureImageDataGeneratorCall0 call = reinterpret_cast<CuteQt3DRender_QTextureImageDataGeneratorCall0>(taken[0]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  Qt3DRender::QTextureImageDataGenerator::~QTextureImageDataGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender26QTextureImageDataGeneratorD1Ev(
    Qt3DRender::QTextureImageDataGenerator *self) {
  delete self;
}

//  a Python function taken by a CuteQt3DRender_QTextureImageDataGenerator,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QTextureImageDataGenerator(
    Qt3DRender::QTextureImageDataGenerator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QTextureImageDataGenerator *>(self)->take(key, call);
}
