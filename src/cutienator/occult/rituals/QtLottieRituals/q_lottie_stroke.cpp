//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiestroke_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiestroke_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtGui/qpen.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QLottieStroke that Python can take functions over in. Every QLottieStroke
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieStrokeCall0)(const void *, int *);
typedef void (*CuteQLottieStrokeCall1)(const void *, int, int *);
typedef int (*CuteQLottieStrokeCall2)(const void *, const QJsonObject *, int *);
typedef const QPen * (*CuteQLottieStrokeCall3)(const void *, int *);
typedef bool (*CuteQLottieStrokeCall4)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieStrokeCall5)(const void *, int *);
typedef bool (*CuteQLottieStrokeCall6)(const void *, int *);
typedef void (*CuteQLottieStrokeCall7)(const void *, const QLottieTrimPath *, int *);
typedef const QPainterPath * (*CuteQLottieStrokeCall8)(const void *, int *);
typedef bool (*CuteQLottieStrokeCall9)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottieStrokeCall10)(const void *, int, int *);
typedef void * (*CuteQLottieStrokeCall11)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieStrokeCall12)(const void *, int *);
class CuteQLottieStroke : public QLottieStroke {
public:
  using QLottieStroke::QLottieStroke;
  CuteQLottieStroke(const QLottieStroke &other) : QLottieStroke(other) {}
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QLottieStroke3penEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape10isAnimatedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape4pathEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape11acceptsTrimEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieShape9applyTrimERK15QLottieTrimPath")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape12fallbackPathEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieStroke::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieStrokeCall0 call = reinterpret_cast<CuteQLottieStrokeCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieStroke::clone();
  }

  //  void QLottieStroke::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieStrokeCall1 call = reinterpret_cast<CuteQLottieStrokeCall1>(taken[1]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieStroke::updateProperties(frame);
  }

  //  int QLottieStroke::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieStrokeCall2 call = reinterpret_cast<CuteQLottieStrokeCall2>(taken[2]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieStroke::parse(definition);
  }

  //  QPen QLottieStroke::pen() const
  QPen pen() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieStrokeCall3 call = reinterpret_cast<CuteQLottieStrokeCall3>(taken[3]);
      const QPen * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieStroke::pen();
  }

  //  bool QLottieShape::isAnimated() const
  bool isAnimated() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieStrokeCall4 call = reinterpret_cast<CuteQLottieStrokeCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::isAnimated();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieStrokeCall5 call = reinterpret_cast<CuteQLottieStrokeCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  bool QLottieShape::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieStrokeCall6 call = reinterpret_cast<CuteQLottieStrokeCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::acceptsTrim();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieStrokeCall7 call = reinterpret_cast<CuteQLottieStrokeCall7>(taken[7]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieShape::applyTrim(trimmer);
  }

  //  QPainterPath QLottieShape::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieStrokeCall8 call = reinterpret_cast<CuteQLottieStrokeCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQLottieStrokeCall9 call = reinterpret_cast<CuteQLottieStrokeCall9>(taken[9]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieStrokeCall10 call = reinterpret_cast<CuteQLottieStrokeCall10>(taken[10]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieStrokeCall11 call = reinterpret_cast<CuteQLottieStrokeCall11>(taken[11]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQLottieStrokeCall12 call = reinterpret_cast<CuteQLottieStrokeCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieStroke::QLottieStroke(const QLottieStroke &other)
extern "C" Q_DECL_EXPORT
QLottieStroke *ritual_ZN13QLottieStrokeC1ERKS_(const QLottieStroke *other) {
  return new CuteQLottieStroke(*other);
}

//  QLottieStroke::QLottieStroke(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieStroke *ritual_ZN13QLottieStrokeC1EP11QLottieBase(
    QLottieBase *parent) {
  return new CuteQLottieStroke(parent);
}

//  QLottieBase *QLottieStroke::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK13QLottieStroke5cloneEv(const QLottieStroke *self) {
  return self->clone();
}

//  void QLottieStroke::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLottieStroke16updatePropertiesEi(
    QLottieStroke *self,
    int frame) {
  self->updateProperties(frame);
}

//  int QLottieStroke::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QLottieStroke5parseERK11QJsonObject(
    QLottieStroke *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  QPen QLottieStroke::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK13QLottieStroke3penEv(const QLottieStroke *self) {
  return new QPen(self->pen());
}

//  qreal QLottieStroke::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QLottieStroke7opacityEv(const QLottieStroke *self) {
  return self->opacity();
}

//  QColor QLottieStroke::getColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK13QLottieStroke8getColorEv(const QLottieStroke *self) {
  return new QColor(self->getColor());
}

//  void QLottieStroke::updateDashPattern()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLottieStroke17updateDashPatternEv(QLottieStroke *self) {
  self->updateDashPattern();
}

//  QLottieStroke::~QLottieStroke()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLottieStrokeD1Ev(QLottieStroke *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieStroke, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieStroke(
    QLottieStroke *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieStroke *>(self)->take(key, call);
}

//  QLottieBase *QLottieStroke::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK13QLottieStroke5cloneEv(
    const QLottieStroke *self) {
  return self->QLottieStroke::clone();
}

//  void QLottieStroke::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QLottieStroke16updatePropertiesEi(
    QLottieStroke *self,
    int frame) {
  self->QLottieStroke::updateProperties(frame);
}

//  int QLottieStroke::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN13QLottieStroke5parseERK11QJsonObject(
    QLottieStroke *self,
    const QJsonObject *definition) {
  return self->QLottieStroke::parse(*definition);
}

//  QPen QLottieStroke::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_own_ZNK13QLottieStroke3penEv(const QLottieStroke *self) {
  return new QPen(self->QLottieStroke::pen());
}
