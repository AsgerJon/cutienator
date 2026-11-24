//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiebasictransform_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiebasictransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiespatialproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QLottieBasicTransform that Python can take functions over in. Every QLottieBasicTransform
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieBasicTransformCall0)(const void *, int *);
typedef int (*CuteQLottieBasicTransformCall1)(const void *, const QJsonObject *, int *);
typedef void (*CuteQLottieBasicTransformCall2)(const void *, int, int *);
typedef const QPointF * (*CuteQLottieBasicTransformCall3)(const void *, int *);
typedef bool (*CuteQLottieBasicTransformCall4)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieBasicTransformCall5)(const void *, int *);
typedef bool (*CuteQLottieBasicTransformCall6)(const void *, int *);
typedef void (*CuteQLottieBasicTransformCall7)(const void *, const QLottieTrimPath *, int *);
typedef const QPainterPath * (*CuteQLottieBasicTransformCall8)(const void *, int *);
typedef bool (*CuteQLottieBasicTransformCall9)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottieBasicTransformCall10)(const void *, int, int *);
typedef void * (*CuteQLottieBasicTransformCall11)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieBasicTransformCall12)(const void *, int *);
class CuteQLottieBasicTransform : public QLottieBasicTransform {
public:
  using QLottieBasicTransform::QLottieBasicTransform;
  CuteQLottieBasicTransform(const QLottieBasicTransform &other) : QLottieBasicTransform(other) {}
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

  //  QLottieBase *QLottieBasicTransform::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieBasicTransformCall0 call = reinterpret_cast<CuteQLottieBasicTransformCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBasicTransform::clone();
  }

  //  int QLottieBasicTransform::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieBasicTransformCall1 call = reinterpret_cast<CuteQLottieBasicTransformCall1>(taken[1]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieBasicTransform::parse(definition);
  }

  //  void QLottieBasicTransform::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieBasicTransformCall2 call = reinterpret_cast<CuteQLottieBasicTransformCall2>(taken[2]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieBasicTransform::updateProperties(frame);
  }

  //  QPointF QLottieBasicTransform::position() const
  QPointF position() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieBasicTransformCall3 call = reinterpret_cast<CuteQLottieBasicTransformCall3>(taken[3]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBasicTransform::position();
  }

  //  bool QLottieShape::isAnimated() const
  bool isAnimated() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieBasicTransformCall4 call = reinterpret_cast<CuteQLottieBasicTransformCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::isAnimated();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieBasicTransformCall5 call = reinterpret_cast<CuteQLottieBasicTransformCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  bool QLottieShape::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieBasicTransformCall6 call = reinterpret_cast<CuteQLottieBasicTransformCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::acceptsTrim();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieBasicTransformCall7 call = reinterpret_cast<CuteQLottieBasicTransformCall7>(taken[7]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieShape::applyTrim(trimmer);
  }

  //  QPainterPath QLottieShape::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieBasicTransformCall8 call = reinterpret_cast<CuteQLottieBasicTransformCall8>(taken[8]);
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
      CuteQLottieBasicTransformCall9 call = reinterpret_cast<CuteQLottieBasicTransformCall9>(taken[9]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieBasicTransformCall10 call = reinterpret_cast<CuteQLottieBasicTransformCall10>(taken[10]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieBasicTransformCall11 call = reinterpret_cast<CuteQLottieBasicTransformCall11>(taken[11]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQLottieBasicTransformCall12 call = reinterpret_cast<CuteQLottieBasicTransformCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieBasicTransform::QLottieBasicTransform(const QLottieBasicTransform
//      &other)
extern "C" Q_DECL_EXPORT
QLottieBasicTransform *ritual_ZN21QLottieBasicTransformC1ERKS_(
    const QLottieBasicTransform *other) {
  return new CuteQLottieBasicTransform(*other);
}

//  QLottieBasicTransform::QLottieBasicTransform(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieBasicTransform *ritual_ZN21QLottieBasicTransformC1EP11QLottieBase(
    QLottieBase *parent) {
  return new CuteQLottieBasicTransform(parent);
}

//  QLottieBase *QLottieBasicTransform::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK21QLottieBasicTransform5cloneEv(
    const QLottieBasicTransform *self) {
  return self->clone();
}

//  int QLottieBasicTransform::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QLottieBasicTransform5parseERK11QJsonObject(
    QLottieBasicTransform *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  void QLottieBasicTransform::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieBasicTransform16updatePropertiesEi(
    QLottieBasicTransform *self,
    int frame) {
  self->updateProperties(frame);
}

//  QPointF QLottieBasicTransform::anchorPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK21QLottieBasicTransform11anchorPointEv(
    const QLottieBasicTransform *self) {
  return new QPointF(self->anchorPoint());
}

//  QPointF QLottieBasicTransform::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK21QLottieBasicTransform8positionEv(
    const QLottieBasicTransform *self) {
  return new QPointF(self->position());
}

//  QPointF QLottieBasicTransform::scale() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK21QLottieBasicTransform5scaleEv(
    const QLottieBasicTransform *self) {
  return new QPointF(self->scale());
}

//  qreal QLottieBasicTransform::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QLottieBasicTransform8rotationEv(
    const QLottieBasicTransform *self) {
  return self->rotation();
}

//  qreal QLottieBasicTransform::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QLottieBasicTransform7opacityEv(
    const QLottieBasicTransform *self) {
  return self->opacity();
}

//  bool QLottieBasicTransform::splitPosition() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QLottieBasicTransform13splitPositionEv(
    const QLottieBasicTransform *self) {
  return self->splitPosition();
}

//  QLottieSpatialProperty QLottieBasicTransform::anchorPointProperty() const
extern "C" Q_DECL_EXPORT
QLottieSpatialProperty *ritual_ZNK21QLottieBasicTransform19anchorPointPropertyEv(
    const QLottieBasicTransform *self) {
  return new QLottieSpatialProperty(self->anchorPointProperty());
}

//  QLottieSpatialProperty QLottieBasicTransform::positionProperty() const
extern "C" Q_DECL_EXPORT
QLottieSpatialProperty *ritual_ZNK21QLottieBasicTransform16positionPropertyEv(
    const QLottieBasicTransform *self) {
  return new QLottieSpatialProperty(self->positionProperty());
}

//  bool QLottieBasicTransform::hasLinkedLayerTransform() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QLottieBasicTransform23hasLinkedLayerTransformEv(
    const QLottieBasicTransform *self) {
  return self->hasLinkedLayerTransform();
}

//  void QLottieBasicTransform::setHasLinkedLayerTransform(bool
//      hasLinkedLayerTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieBasicTransform26setHasLinkedLayerTransformEb(
    QLottieBasicTransform *self,
    bool hasLinkedLayerTransform) {
  self->setHasLinkedLayerTransform(hasLinkedLayerTransform);
}

//  QLottieBasicTransform::~QLottieBasicTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieBasicTransformD1Ev(QLottieBasicTransform *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieBasicTransform, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieBasicTransform(
    QLottieBasicTransform *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieBasicTransform *>(self)->take(key, call);
}

//  QLottieBase *QLottieBasicTransform::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK21QLottieBasicTransform5cloneEv(
    const QLottieBasicTransform *self) {
  return self->QLottieBasicTransform::clone();
}

//  int QLottieBasicTransform::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN21QLottieBasicTransform5parseERK11QJsonObject(
    QLottieBasicTransform *self,
    const QJsonObject *definition) {
  return self->QLottieBasicTransform::parse(*definition);
}

//  void QLottieBasicTransform::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QLottieBasicTransform16updatePropertiesEi(
    QLottieBasicTransform *self,
    int frame) {
  self->QLottieBasicTransform::updateProperties(frame);
}

//  QPointF QLottieBasicTransform::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK21QLottieBasicTransform8positionEv(
    const QLottieBasicTransform *self) {
  return new QPointF(self->QLottieBasicTransform::position());
}
