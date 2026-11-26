//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiegstroke_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiegstroke_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtGui/qpen.h>
#include <cstring>

//  A QLottieGStroke that Python can take functions over in. Every QLottieGStroke
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieGStrokeCall0)(const void *, int *);
typedef void (*CuteQLottieGStrokeCall1)(const void *, int, int *);
typedef int (*CuteQLottieGStrokeCall2)(const void *, const QJsonObject *, int *);
typedef const QPen * (*CuteQLottieGStrokeCall3)(const void *, int *);
class CuteQLottieGStroke : public QLottieGStroke {
public:
  using QLottieGStroke::QLottieGStroke;
  CuteQLottieGStroke(const QLottieGStroke & other) : QLottieGStroke(other) {}
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QLottieGStroke5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QLottieGStroke16updatePropertiesEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QLottieGStroke5parseERK11QJsonObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QLottieGStroke3penEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieGStroke::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieGStrokeCall0 call = reinterpret_cast<CuteQLottieGStrokeCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieGStroke::clone();
  }

  //  void QLottieGStroke::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieGStrokeCall1 call = reinterpret_cast<CuteQLottieGStrokeCall1>(taken[1]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieGStroke::updateProperties(frame);
  }

  //  int QLottieGStroke::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieGStrokeCall2 call = reinterpret_cast<CuteQLottieGStrokeCall2>(taken[2]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieGStroke::parse(definition);
  }

  //  QPen QLottieGStroke::pen() const
  QPen pen() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieGStrokeCall3 call = reinterpret_cast<CuteQLottieGStrokeCall3>(taken[3]);
      const QPen * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieGStroke::pen();
  }
};

//  QLottieGStroke::QLottieGStroke(const QLottieGStroke &other)
extern "C" Q_DECL_EXPORT
QLottieGStroke *ritual_ZN14QLottieGStrokeC1ERKS_(
    const QLottieGStroke *other) {
  return new CuteQLottieGStroke(*other);
}

//  QLottieGStroke::QLottieGStroke(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieGStroke *ritual_ZN14QLottieGStrokeC1EP11QLottieBase(
    QLottieBase *parent) {
  return new CuteQLottieGStroke(parent);
}

//  QLottieBase *QLottieGStroke::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK14QLottieGStroke5cloneEv(const QLottieGStroke *self) {
  return self->clone();
}

//  void QLottieGStroke::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLottieGStroke16updatePropertiesEi(
    QLottieGStroke *self,
    int frame) {
  self->updateProperties(frame);
}

//  void QLottieGStroke::render(QLottieRenderer &renderer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QLottieGStroke6renderER15QLottieRenderer(
    const QLottieGStroke *self,
    QLottieRenderer *renderer) {
  self->render(*renderer);
}

//  int QLottieGStroke::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QLottieGStroke5parseERK11QJsonObject(
    QLottieGStroke *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  QPen QLottieGStroke::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK14QLottieGStroke3penEv(const QLottieGStroke *self) {
  return new QPen(self->pen());
}

//  QLottieGStroke::~QLottieGStroke()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLottieGStrokeD1Ev(QLottieGStroke *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieGStroke, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieGStroke(
    QLottieGStroke *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieGStroke *>(self)->take(key, call);
}

//  QLottieBase *QLottieGStroke::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK14QLottieGStroke5cloneEv(
    const QLottieGStroke *self) {
  return self->QLottieGStroke::clone();
}

//  void QLottieGStroke::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QLottieGStroke16updatePropertiesEi(
    QLottieGStroke *self,
    int frame) {
  self->QLottieGStroke::updateProperties(frame);
}

//  int QLottieGStroke::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN14QLottieGStroke5parseERK11QJsonObject(
    QLottieGStroke *self,
    const QJsonObject *definition) {
  return self->QLottieGStroke::parse(*definition);
}

//  QPen QLottieGStroke::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_own_ZNK14QLottieGStroke3penEv(const QLottieGStroke *self) {
  return new QPen(self->QLottieGStroke::pen());
}
