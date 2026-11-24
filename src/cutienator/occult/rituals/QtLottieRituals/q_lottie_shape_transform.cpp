//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieshapetransform_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieshapetransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QLottieShapeTransform that Python can take functions over in. Every QLottieShapeTransform
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieShapeTransformCall0)(const void *, int *);
typedef int (*CuteQLottieShapeTransformCall1)(const void *, const QJsonObject *, int *);
typedef void (*CuteQLottieShapeTransformCall2)(const void *, int, int *);
typedef const QPointF * (*CuteQLottieShapeTransformCall3)(const void *, int *);
typedef bool (*CuteQLottieShapeTransformCall4)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieShapeTransformCall5)(const void *, int *);
typedef bool (*CuteQLottieShapeTransformCall6)(const void *, int *);
typedef void (*CuteQLottieShapeTransformCall7)(const void *, const QLottieTrimPath *, int *);
typedef const QPainterPath * (*CuteQLottieShapeTransformCall8)(const void *, int *);
typedef bool (*CuteQLottieShapeTransformCall9)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottieShapeTransformCall10)(const void *, int, int *);
typedef void * (*CuteQLottieShapeTransformCall11)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieShapeTransformCall12)(const void *, int *);
class CuteQLottieShapeTransform : public QLottieShapeTransform {
public:
  using QLottieShapeTransform::QLottieShapeTransform;
  CuteQLottieShapeTransform(const QLottieShapeTransform &other) : QLottieShapeTransform(other) {}
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QLottieBasicTransform8positionEv")) {
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

  //  QLottieBase *QLottieShapeTransform::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieShapeTransformCall0 call = reinterpret_cast<CuteQLottieShapeTransformCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieShapeTransform::clone();
  }

  //  int QLottieShapeTransform::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieShapeTransformCall1 call = reinterpret_cast<CuteQLottieShapeTransformCall1>(taken[1]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieShapeTransform::parse(definition);
  }

  //  void QLottieShapeTransform::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieShapeTransformCall2 call = reinterpret_cast<CuteQLottieShapeTransformCall2>(taken[2]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieShapeTransform::updateProperties(frame);
  }

  //  QPointF QLottieBasicTransform::position() const
  QPointF position() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieShapeTransformCall3 call = reinterpret_cast<CuteQLottieShapeTransformCall3>(taken[3]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBasicTransform::position();
  }

  //  bool QLottieShape::isAnimated() const
  bool isAnimated() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieShapeTransformCall4 call = reinterpret_cast<CuteQLottieShapeTransformCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::isAnimated();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieShapeTransformCall5 call = reinterpret_cast<CuteQLottieShapeTransformCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  bool QLottieShape::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieShapeTransformCall6 call = reinterpret_cast<CuteQLottieShapeTransformCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::acceptsTrim();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieShapeTransformCall7 call = reinterpret_cast<CuteQLottieShapeTransformCall7>(taken[7]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieShape::applyTrim(trimmer);
  }

  //  QPainterPath QLottieShape::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieShapeTransformCall8 call = reinterpret_cast<CuteQLottieShapeTransformCall8>(taken[8]);
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
      CuteQLottieShapeTransformCall9 call = reinterpret_cast<CuteQLottieShapeTransformCall9>(taken[9]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieShapeTransformCall10 call = reinterpret_cast<CuteQLottieShapeTransformCall10>(taken[10]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieShapeTransformCall11 call = reinterpret_cast<CuteQLottieShapeTransformCall11>(taken[11]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQLottieShapeTransformCall12 call = reinterpret_cast<CuteQLottieShapeTransformCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieShapeTransform::QLottieShapeTransform(const QLottieShapeTransform
//      &other)
extern "C" Q_DECL_EXPORT
QLottieShapeTransform *ritual_ZN21QLottieShapeTransformC1ERKS_(
    const QLottieShapeTransform *other) {
  return new CuteQLottieShapeTransform(*other);
}

//  QLottieShapeTransform::QLottieShapeTransform(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieShapeTransform *ritual_ZN21QLottieShapeTransformC1EP11QLottieBase(
    QLottieBase *parent) {
  return new CuteQLottieShapeTransform(parent);
}

//  QLottieBase *QLottieShapeTransform::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK21QLottieShapeTransform5cloneEv(
    const QLottieShapeTransform *self) {
  return self->clone();
}

//  int QLottieShapeTransform::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QLottieShapeTransform5parseERK11QJsonObject(
    QLottieShapeTransform *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  void QLottieShapeTransform::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieShapeTransform16updatePropertiesEi(
    QLottieShapeTransform *self,
    int frame) {
  self->updateProperties(frame);
}

//  qreal QLottieShapeTransform::skew() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QLottieShapeTransform4skewEv(
    const QLottieShapeTransform *self) {
  return self->skew();
}

//  qreal QLottieShapeTransform::skewAxis() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QLottieShapeTransform8skewAxisEv(
    const QLottieShapeTransform *self) {
  return self->skewAxis();
}

//  qreal QLottieShapeTransform::shearX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QLottieShapeTransform6shearXEv(
    const QLottieShapeTransform *self) {
  return self->shearX();
}

//  qreal QLottieShapeTransform::shearY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QLottieShapeTransform6shearYEv(
    const QLottieShapeTransform *self) {
  return self->shearY();
}

//  qreal QLottieShapeTransform::shearAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QLottieShapeTransform10shearAngleEv(
    const QLottieShapeTransform *self) {
  return self->shearAngle();
}

//  QLottieShapeTransform::~QLottieShapeTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieShapeTransformD1Ev(QLottieShapeTransform *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieShapeTransform, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieShapeTransform(
    QLottieShapeTransform *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieShapeTransform *>(self)->take(key, call);
}

//  QLottieBase *QLottieShapeTransform::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK21QLottieShapeTransform5cloneEv(
    const QLottieShapeTransform *self) {
  return self->QLottieShapeTransform::clone();
}

//  int QLottieShapeTransform::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN21QLottieShapeTransform5parseERK11QJsonObject(
    QLottieShapeTransform *self,
    const QJsonObject *definition) {
  return self->QLottieShapeTransform::parse(*definition);
}

//  void QLottieShapeTransform::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QLottieShapeTransform16updatePropertiesEi(
    QLottieShapeTransform *self,
    int frame) {
  self->QLottieShapeTransform::updateProperties(frame);
}
