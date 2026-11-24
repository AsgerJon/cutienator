//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qabstractspritesheet_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qabstractspritesheet_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DExtras::QAbstractSpriteSheetPrivate that Python can take functions over in. Every Qt3DExtras::QAbstractSpriteSheetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QAbstractSpriteSheetPrivateCall0)(const void *, int *);
typedef int (*CuteQt3DExtras_QAbstractSpriteSheetPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DExtras_QAbstractSpriteSheetPrivateCall2)(const void *, int *);
typedef void (*CuteQt3DExtras_QAbstractSpriteSheetPrivateCall3)(const void *, int *);
typedef void (*CuteQt3DExtras_QAbstractSpriteSheetPrivateCall4)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QAbstractSpriteSheetPrivateCall5)(const void *, int *);
class CuteQt3DExtras_QAbstractSpriteSheetPrivate : public Qt3DExtras::QAbstractSpriteSheetPrivate {
public:
  using Qt3DExtras::QAbstractSpriteSheetPrivate::QAbstractSpriteSheetPrivate;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate4initEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DExtras27QAbstractSpriteSheetPrivate8maxIndexEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate11updateSizesEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate15updateTransformEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DExtras::QAbstractSpriteSheetPrivate::init()
  void init() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QAbstractSpriteSheetPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QAbstractSpriteSheetPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DExtras::QAbstractSpriteSheetPrivate::init();
  }

  //  int Qt3DExtras::QAbstractSpriteSheetPrivate::maxIndex() const
  int maxIndex() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QAbstractSpriteSheetPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QAbstractSpriteSheetPrivateCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DExtras::QAbstractSpriteSheetPrivate::updateSizes()
  void updateSizes() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DExtras_QAbstractSpriteSheetPrivateCall2 call = reinterpret_cast<CuteQt3DExtras_QAbstractSpriteSheetPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DExtras::QAbstractSpriteSheetPrivate::updateTransform()
  void updateTransform() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DExtras_QAbstractSpriteSheetPrivateCall3 call = reinterpret_cast<CuteQt3DExtras_QAbstractSpriteSheetPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DExtras_QAbstractSpriteSheetPrivateCall4 call = reinterpret_cast<CuteQt3DExtras_QAbstractSpriteSheetPrivateCall4>(taken[4]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DExtras_QAbstractSpriteSheetPrivateCall5 call = reinterpret_cast<CuteQt3DExtras_QAbstractSpriteSheetPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  void Qt3DExtras::QAbstractSpriteSheetPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate4initEv(
    Qt3DExtras::QAbstractSpriteSheetPrivate *self) {
  self->init();
}

//  int Qt3DExtras::QAbstractSpriteSheetPrivate::maxIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras27QAbstractSpriteSheetPrivate8maxIndexEv(
    const Qt3DExtras::QAbstractSpriteSheetPrivate *self) {
  return self->maxIndex();
}

//  void Qt3DExtras::QAbstractSpriteSheetPrivate::updateSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate11updateSizesEv(
    Qt3DExtras::QAbstractSpriteSheetPrivate *self) {
  self->updateSizes();
}

//  void Qt3DExtras::QAbstractSpriteSheetPrivate::updateTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate15updateTransformEv(
    Qt3DExtras::QAbstractSpriteSheetPrivate *self) {
  self->updateTransform();
}

//  QAbstractSpriteSheet *Qt3DExtras::QAbstractSpriteSheetPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QAbstractSpriteSheet *ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate6q_funcEv(
    Qt3DExtras::QAbstractSpriteSheetPrivate *self) {
  return self->q_func();
}

//  const QAbstractSpriteSheet
//      *Qt3DExtras::QAbstractSpriteSheetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QAbstractSpriteSheet *ritual_ZNK10Qt3DExtras27QAbstractSpriteSheetPrivate6q_funcEv(
    const Qt3DExtras::QAbstractSpriteSheetPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QAbstractSpriteSheetPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QAbstractSpriteSheetPrivate(
    Qt3DExtras::QAbstractSpriteSheetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QAbstractSpriteSheetPrivate *>(self)->take(key, call);
}
