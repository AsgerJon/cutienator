//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottierepeatertransform_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottierepeatertransform_p.h>
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

//  A QLottieRepeaterTransform that Python can take functions over in. Every QLottieRepeaterTransform
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieRepeaterTransformCall0)(const void *, int *);
typedef int (*CuteQLottieRepeaterTransformCall1)(const void *, const QJsonObject *, int *);
typedef void (*CuteQLottieRepeaterTransformCall2)(const void *, int, int *);
typedef const QPointF * (*CuteQLottieRepeaterTransformCall3)(const void *, int *);
typedef bool (*CuteQLottieRepeaterTransformCall4)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieRepeaterTransformCall5)(const void *, int *);
typedef bool (*CuteQLottieRepeaterTransformCall6)(const void *, int *);
typedef void (*CuteQLottieRepeaterTransformCall7)(const void *, const QLottieTrimPath *, int *);
typedef const QPainterPath * (*CuteQLottieRepeaterTransformCall8)(const void *, int *);
typedef bool (*CuteQLottieRepeaterTransformCall9)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottieRepeaterTransformCall10)(const void *, int, int *);
typedef void * (*CuteQLottieRepeaterTransformCall11)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieRepeaterTransformCall12)(const void *, int *);
class CuteQLottieRepeaterTransform : public QLottieRepeaterTransform {
public:
  using QLottieRepeaterTransform::QLottieRepeaterTransform;
  CuteQLottieRepeaterTransform(const QLottieRepeaterTransform &other) : QLottieRepeaterTransform(other) {}
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

  //  QLottieBase *QLottieRepeaterTransform::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall0 call = reinterpret_cast<CuteQLottieRepeaterTransformCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieRepeaterTransform::clone();
  }

  //  int QLottieRepeaterTransform::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall1 call = reinterpret_cast<CuteQLottieRepeaterTransformCall1>(taken[1]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieRepeaterTransform::parse(definition);
  }

  //  void QLottieRepeaterTransform::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall2 call = reinterpret_cast<CuteQLottieRepeaterTransformCall2>(taken[2]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieRepeaterTransform::updateProperties(frame);
  }

  //  QPointF QLottieBasicTransform::position() const
  QPointF position() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall3 call = reinterpret_cast<CuteQLottieRepeaterTransformCall3>(taken[3]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBasicTransform::position();
  }

  //  bool QLottieShape::isAnimated() const
  bool isAnimated() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall4 call = reinterpret_cast<CuteQLottieRepeaterTransformCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::isAnimated();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall5 call = reinterpret_cast<CuteQLottieRepeaterTransformCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  bool QLottieShape::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall6 call = reinterpret_cast<CuteQLottieRepeaterTransformCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::acceptsTrim();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall7 call = reinterpret_cast<CuteQLottieRepeaterTransformCall7>(taken[7]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieShape::applyTrim(trimmer);
  }

  //  QPainterPath QLottieShape::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall8 call = reinterpret_cast<CuteQLottieRepeaterTransformCall8>(taken[8]);
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
      CuteQLottieRepeaterTransformCall9 call = reinterpret_cast<CuteQLottieRepeaterTransformCall9>(taken[9]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall10 call = reinterpret_cast<CuteQLottieRepeaterTransformCall10>(taken[10]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall11 call = reinterpret_cast<CuteQLottieRepeaterTransformCall11>(taken[11]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQLottieRepeaterTransformCall12 call = reinterpret_cast<CuteQLottieRepeaterTransformCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieRepeaterTransform::QLottieRepeaterTransform(const
//      QLottieRepeaterTransform &other)
extern "C" Q_DECL_EXPORT
QLottieRepeaterTransform *ritual_ZN24QLottieRepeaterTransformC1ERKS_(
    const QLottieRepeaterTransform *other) {
  return new CuteQLottieRepeaterTransform(*other);
}

//  QLottieRepeaterTransform::QLottieRepeaterTransform(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieRepeaterTransform *ritual_ZN24QLottieRepeaterTransformC1EP11QLottieBase(
    QLottieBase *parent) {
  return new CuteQLottieRepeaterTransform(parent);
}

//  QLottieBase *QLottieRepeaterTransform::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK24QLottieRepeaterTransform5cloneEv(
    const QLottieRepeaterTransform *self) {
  return self->clone();
}

//  int QLottieRepeaterTransform::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QLottieRepeaterTransform5parseERK11QJsonObject(
    QLottieRepeaterTransform *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  void QLottieRepeaterTransform::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLottieRepeaterTransform16updatePropertiesEi(
    QLottieRepeaterTransform *self,
    int frame) {
  self->updateProperties(frame);
}

//  qreal QLottieRepeaterTransform::startOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QLottieRepeaterTransform12startOpacityEv(
    const QLottieRepeaterTransform *self) {
  return self->startOpacity();
}

//  qreal QLottieRepeaterTransform::endOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QLottieRepeaterTransform10endOpacityEv(
    const QLottieRepeaterTransform *self) {
  return self->endOpacity();
}

//  void QLottieRepeaterTransform::setInstanceCount(int copies)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLottieRepeaterTransform16setInstanceCountEi(
    QLottieRepeaterTransform *self,
    int copies) {
  self->setInstanceCount(copies);
}

//  qreal QLottieRepeaterTransform::opacityAtInstance(int instance) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QLottieRepeaterTransform17opacityAtInstanceEi(
    const QLottieRepeaterTransform *self,
    int instance) {
  return self->opacityAtInstance(instance);
}

//  QLottieRepeaterTransform::~QLottieRepeaterTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLottieRepeaterTransformD1Ev(
    QLottieRepeaterTransform *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieRepeaterTransform, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieRepeaterTransform(
    QLottieRepeaterTransform *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieRepeaterTransform *>(self)->take(key, call);
}

//  QLottieBase *QLottieRepeaterTransform::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK24QLottieRepeaterTransform5cloneEv(
    const QLottieRepeaterTransform *self) {
  return self->QLottieRepeaterTransform::clone();
}

//  int QLottieRepeaterTransform::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN24QLottieRepeaterTransform5parseERK11QJsonObject(
    QLottieRepeaterTransform *self,
    const QJsonObject *definition) {
  return self->QLottieRepeaterTransform::parse(*definition);
}

//  void QLottieRepeaterTransform::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QLottieRepeaterTransform16updatePropertiesEi(
    QLottieRepeaterTransform *self,
    int frame) {
  self->QLottieRepeaterTransform::updateProperties(frame);
}
