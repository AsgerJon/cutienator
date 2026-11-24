//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DExtras::QTextureAtlasGenerator that Python can take functions over in. Every Qt3DExtras::QTextureAtlasGenerator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qintptr (*CuteQt3DExtras_QTextureAtlasGeneratorCall0)(const void *, int *);
class CuteQt3DExtras_QTextureAtlasGenerator : public Qt3DExtras::QTextureAtlasGenerator {
public:
  using Qt3DExtras::QTextureAtlasGenerator::QTextureAtlasGenerator;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore16QAbstractFunctor2idEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  qintptr Qt3DExtras::QTextureAtlasGenerator::id() const
  qintptr id() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QTextureAtlasGeneratorCall0 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasGeneratorCall0>(taken[0]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DExtras::QTextureAtlasGenerator::id();
  }
};

//  qintptr Qt3DExtras::QTextureAtlasGenerator::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK10Qt3DExtras22QTextureAtlasGenerator2idEv(
    const Qt3DExtras::QTextureAtlasGenerator *self) {
  return self->id();
}

//  a Python function taken by a CuteQt3DExtras_QTextureAtlasGenerator, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QTextureAtlasGenerator(
    Qt3DExtras::QTextureAtlasGenerator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QTextureAtlasGenerator *>(self)->take(key, call);
}

//  qintptr Qt3DExtras::QTextureAtlasGenerator::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK10Qt3DExtras22QTextureAtlasGenerator2idEv(
    const Qt3DExtras::QTextureAtlasGenerator *self) {
  return self->Qt3DExtras::QTextureAtlasGenerator::id();
}
