//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qtexturegenerator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qtexturegenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QTextureGenerator that Python can take functions over in. Every Qt3DRender::QTextureGenerator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qintptr (*CuteQt3DRender_QTextureGeneratorCall0)(const void *, int *);
class CuteQt3DRender_QTextureGenerator : public Qt3DRender::QTextureGenerator {
public:
  using Qt3DRender::QTextureGenerator::QTextureGenerator;
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
      CuteQt3DRender_QTextureGeneratorCall0 call = reinterpret_cast<CuteQt3DRender_QTextureGeneratorCall0>(taken[0]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  Qt3DRender::QTextureGenerator::~QTextureGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17QTextureGeneratorD1Ev(
    Qt3DRender::QTextureGenerator *self) {
  delete self;
}

//  QTextureDataPtr Qt3DRender::QTextureGenerator::operator()()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureDataPtr *ritual_ZN10Qt3DRender17QTextureGeneratorclEv(
    Qt3DRender::QTextureGenerator *self) {
  return new Qt3DRender::QTextureDataPtr(self->operator()());
}

//  bool Qt3DRender::QTextureGenerator::operator==(const QTextureGenerator
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender17QTextureGeneratoreqERKS0_(
    const Qt3DRender::QTextureGenerator *self,
    const Qt3DRender::QTextureGenerator *other) {
  return self->operator==(*other);
}

//  a Python function taken by a CuteQt3DRender_QTextureGenerator, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QTextureGenerator(
    Qt3DRender::QTextureGenerator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QTextureGenerator *>(self)->take(key, call);
}

//  a Qt3DRender::QTextureDataPtr a ritual of Qt3DRender::QTextureGenerator
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QTextureGenerator__Qt3DRender_QTextureDataPtr(
    Qt3DRender::QTextureDataPtr *self) {
  delete self;
}
