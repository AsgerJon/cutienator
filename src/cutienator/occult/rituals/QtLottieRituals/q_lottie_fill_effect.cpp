//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiefilleffect_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiefilleffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QLottieFillEffect that Python can take functions over in. Every QLottieFillEffect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieFillEffectCall0)(const void *, int *);
typedef void (*CuteQLottieFillEffectCall1)(const void *, int, int *);
typedef bool (*CuteQLottieFillEffectCall2)(const void *, int, const QVariant *, int *);
typedef int (*CuteQLottieFillEffectCall3)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieFillEffectCall4)(const void *, int, int *);
typedef void * (*CuteQLottieFillEffectCall5)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieFillEffectCall6)(const void *, int *);
class CuteQLottieFillEffect : public QLottieFillEffect {
public:
  using QLottieFillEffect::QLottieFillEffect;
  CuteQLottieFillEffect(const QLottieFillEffect &other) : QLottieFillEffect(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieFillEffect::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieFillEffectCall0 call = reinterpret_cast<CuteQLottieFillEffectCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieFillEffect::clone();
  }

  //  void QLottieFillEffect::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieFillEffectCall1 call = reinterpret_cast<CuteQLottieFillEffectCall1>(taken[1]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieFillEffect::updateProperties(frame);
  }

  //  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieFillEffectCall2 call = reinterpret_cast<CuteQLottieFillEffectCall2>(taken[2]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  int QLottieBase::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieFillEffectCall3 call = reinterpret_cast<CuteQLottieFillEffectCall3>(taken[3]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieBase::parse(definition);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieFillEffectCall4 call = reinterpret_cast<CuteQLottieFillEffectCall4>(taken[4]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieFillEffectCall5 call = reinterpret_cast<CuteQLottieFillEffectCall5>(taken[5]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieFillEffectCall6 call = reinterpret_cast<CuteQLottieFillEffectCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieFillEffect::QLottieFillEffect()
extern "C" Q_DECL_EXPORT
QLottieFillEffect *ritual_ZN17QLottieFillEffectC1Ev() {
  return new CuteQLottieFillEffect();
}

//  QLottieFillEffect::QLottieFillEffect(const QLottieFillEffect &other)
extern "C" Q_DECL_EXPORT
QLottieFillEffect *ritual_ZN17QLottieFillEffectC1ERKS_(
    const QLottieFillEffect *other) {
  return new CuteQLottieFillEffect(*other);
}

//  QLottieBase *QLottieFillEffect::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK17QLottieFillEffect5cloneEv(
    const QLottieFillEffect *self) {
  return self->clone();
}

//  void QLottieFillEffect::construct(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLottieFillEffect9constructERK11QJsonObject(
    QLottieFillEffect *self,
    const QJsonObject *definition) {
  self->construct(*definition);
}

//  void QLottieFillEffect::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLottieFillEffect16updatePropertiesEi(
    QLottieFillEffect *self,
    int frame) {
  self->updateProperties(frame);
}

//  QColor QLottieFillEffect::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QLottieFillEffect5colorEv(
    const QLottieFillEffect *self) {
  return new QColor(self->color());
}

//  qreal QLottieFillEffect::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QLottieFillEffect7opacityEv(
    const QLottieFillEffect *self) {
  return self->opacity();
}

//  QLottieFillEffect::~QLottieFillEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLottieFillEffectD1Ev(QLottieFillEffect *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieFillEffect, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieFillEffect(
    QLottieFillEffect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieFillEffect *>(self)->take(key, call);
}

//  QLottieBase *QLottieFillEffect::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK17QLottieFillEffect5cloneEv(
    const QLottieFillEffect *self) {
  return self->QLottieFillEffect::clone();
}

//  void QLottieFillEffect::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QLottieFillEffect16updatePropertiesEi(
    QLottieFillEffect *self,
    int frame) {
  self->QLottieFillEffect::updateProperties(frame);
}
