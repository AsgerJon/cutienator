//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottierepeater_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottierepeater_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottierepeatertransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QLottieRepeater that Python can take functions over in. Every QLottieRepeater
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieRepeaterCall0)(const void *, int *);
typedef void (*CuteQLottieRepeaterCall1)(const void *, int, int *);
typedef bool (*CuteQLottieRepeaterCall2)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieRepeaterCall3)(const void *, int *);
typedef bool (*CuteQLottieRepeaterCall4)(const void *, int *);
typedef void (*CuteQLottieRepeaterCall5)(const void *, const QLottieTrimPath *, int *);
typedef const QPainterPath * (*CuteQLottieRepeaterCall6)(const void *, int *);
typedef bool (*CuteQLottieRepeaterCall7)(const void *, int, const QVariant *, int *);
typedef int (*CuteQLottieRepeaterCall8)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieRepeaterCall9)(const void *, int, int *);
typedef void * (*CuteQLottieRepeaterCall10)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieRepeaterCall11)(const void *, int *);
class CuteQLottieRepeater : public QLottieRepeater {
public:
  using QLottieRepeater::QLottieRepeater;
  CuteQLottieRepeater(const QLottieRepeater & other) : QLottieRepeater(other) {}
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape10isAnimatedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape4pathEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape11acceptsTrimEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieShape9applyTrimERK15QLottieTrimPath")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape12fallbackPathEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieRepeater::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieRepeaterCall0 call = reinterpret_cast<CuteQLottieRepeaterCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieRepeater::clone();
  }

  //  void QLottieRepeater::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieRepeaterCall1 call = reinterpret_cast<CuteQLottieRepeaterCall1>(taken[1]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieRepeater::updateProperties(frame);
  }

  //  bool QLottieShape::isAnimated() const
  bool isAnimated() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieRepeaterCall2 call = reinterpret_cast<CuteQLottieRepeaterCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::isAnimated();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieRepeaterCall3 call = reinterpret_cast<CuteQLottieRepeaterCall3>(taken[3]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  bool QLottieShape::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieRepeaterCall4 call = reinterpret_cast<CuteQLottieRepeaterCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::acceptsTrim();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieRepeaterCall5 call = reinterpret_cast<CuteQLottieRepeaterCall5>(taken[5]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieShape::applyTrim(trimmer);
  }

  //  QPainterPath QLottieShape::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieRepeaterCall6 call = reinterpret_cast<CuteQLottieRepeaterCall6>(taken[6]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::fallbackPath();
  }

  //  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieRepeaterCall7 call = reinterpret_cast<CuteQLottieRepeaterCall7>(taken[7]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  int QLottieBase::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieRepeaterCall8 call = reinterpret_cast<CuteQLottieRepeaterCall8>(taken[8]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieBase::parse(definition);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieRepeaterCall9 call = reinterpret_cast<CuteQLottieRepeaterCall9>(taken[9]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieRepeaterCall10 call = reinterpret_cast<CuteQLottieRepeaterCall10>(taken[10]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieRepeaterCall11 call = reinterpret_cast<CuteQLottieRepeaterCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieRepeater::QLottieRepeater()
extern "C" Q_DECL_EXPORT
QLottieRepeater *ritual_ZN15QLottieRepeaterC1Ev() {
  return new CuteQLottieRepeater();
}

//  QLottieRepeater::QLottieRepeater(const QLottieRepeater &other)
extern "C" Q_DECL_EXPORT
QLottieRepeater *ritual_ZN15QLottieRepeaterC1ERKS_(
    const QLottieRepeater *other) {
  return new CuteQLottieRepeater(*other);
}

//  QLottieRepeater::QLottieRepeater(const QJsonObject &definition,
//      QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieRepeater *ritual_ZN15QLottieRepeaterC1ERK11QJsonObjectP11QLottieBase(
    const QJsonObject *definition,
    QLottieBase *parent) {
  return new CuteQLottieRepeater(*definition, parent);
}

//  QLottieBase *QLottieRepeater::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK15QLottieRepeater5cloneEv(
    const QLottieRepeater *self) {
  return self->clone();
}

//  void QLottieRepeater::construct(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRepeater9constructERK11QJsonObject(
    QLottieRepeater *self,
    const QJsonObject *definition) {
  self->construct(*definition);
}

//  void QLottieRepeater::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRepeater16updatePropertiesEi(
    QLottieRepeater *self,
    int frame) {
  self->updateProperties(frame);
}

//  void QLottieRepeater::render(QLottieRenderer &renderer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QLottieRepeater6renderER15QLottieRenderer(
    const QLottieRepeater *self,
    QLottieRenderer *renderer) {
  self->render(*renderer);
}

//  int QLottieRepeater::copies() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QLottieRepeater6copiesEv(const QLottieRepeater *self) {
  return self->copies();
}

//  qreal QLottieRepeater::offset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QLottieRepeater6offsetEv(const QLottieRepeater *self) {
  return self->offset();
}

//  const QLottieRepeaterTransform &QLottieRepeater::transform() const
extern "C" Q_DECL_EXPORT
QLottieRepeaterTransform *ritual_ZNK15QLottieRepeater9transformEv(
    const QLottieRepeater *self) {
  return new QLottieRepeaterTransform(self->transform());
}

//  QLottieRepeater::~QLottieRepeater()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRepeaterD1Ev(QLottieRepeater *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieRepeater, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieRepeater(
    QLottieRepeater *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieRepeater *>(self)->take(key, call);
}

//  QLottieBase *QLottieRepeater::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK15QLottieRepeater5cloneEv(
    const QLottieRepeater *self) {
  return self->QLottieRepeater::clone();
}

//  void QLottieRepeater::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QLottieRepeater16updatePropertiesEi(
    QLottieRepeater *self,
    int frame) {
  self->QLottieRepeater::updateProperties(frame);
}
