//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiefill_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiefill_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>
#include <QtGui/QVector4D>

//  A QLottieFill that Python can take functions over in. Every QLottieFill
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieFillCall0)(const void *, int *);
typedef void (*CuteQLottieFillCall1)(const void *, int, int *);
typedef int (*CuteQLottieFillCall2)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieFillCall3)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieFillCall4)(const void *, int *);
typedef bool (*CuteQLottieFillCall5)(const void *, int *);
typedef void (*CuteQLottieFillCall6)(const void *, const QLottieTrimPath *, int *);
typedef const QPainterPath * (*CuteQLottieFillCall7)(const void *, int *);
typedef bool (*CuteQLottieFillCall8)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottieFillCall9)(const void *, int, int *);
typedef void * (*CuteQLottieFillCall10)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieFillCall11)(const void *, int *);
class CuteQLottieFill : public QLottieFill {
public:
  using QLottieFill::QLottieFill;
  CuteQLottieFill(const QLottieFill & other) : QLottieFill(other) {}
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
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape10isAnimatedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape4pathEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape11acceptsTrimEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieShape9applyTrimERK15QLottieTrimPath")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape12fallbackPathEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
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

  //  QLottieBase *QLottieFill::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieFillCall0 call = reinterpret_cast<CuteQLottieFillCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieFill::clone();
  }

  //  void QLottieFill::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieFillCall1 call = reinterpret_cast<CuteQLottieFillCall1>(taken[1]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieFill::updateProperties(frame);
  }

  //  int QLottieFill::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieFillCall2 call = reinterpret_cast<CuteQLottieFillCall2>(taken[2]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieFill::parse(definition);
  }

  //  bool QLottieShape::isAnimated() const
  bool isAnimated() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieFillCall3 call = reinterpret_cast<CuteQLottieFillCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::isAnimated();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieFillCall4 call = reinterpret_cast<CuteQLottieFillCall4>(taken[4]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  bool QLottieShape::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieFillCall5 call = reinterpret_cast<CuteQLottieFillCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::acceptsTrim();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieFillCall6 call = reinterpret_cast<CuteQLottieFillCall6>(taken[6]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieShape::applyTrim(trimmer);
  }

  //  QPainterPath QLottieShape::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieFillCall7 call = reinterpret_cast<CuteQLottieFillCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQLottieFillCall8 call = reinterpret_cast<CuteQLottieFillCall8>(taken[8]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieFillCall9 call = reinterpret_cast<CuteQLottieFillCall9>(taken[9]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieFillCall10 call = reinterpret_cast<CuteQLottieFillCall10>(taken[10]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieFillCall11 call = reinterpret_cast<CuteQLottieFillCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieFill::QLottieFill(const QLottieFill &other)
extern "C" Q_DECL_EXPORT
QLottieFill *ritual_ZN11QLottieFillC1ERKS_(const QLottieFill *other) {
  return new CuteQLottieFill(*other);
}

//  QLottieFill::QLottieFill(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieFill *ritual_ZN11QLottieFillC1EP11QLottieBase(QLottieBase *parent) {
  return new CuteQLottieFill(parent);
}

//  QLottieBase *QLottieFill::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK11QLottieFill5cloneEv(const QLottieFill *self) {
  return self->clone();
}

//  void QLottieFill::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieFill16updatePropertiesEi(
    QLottieFill *self,
    int frame) {
  self->updateProperties(frame);
}

//  void QLottieFill::render(QLottieRenderer &renderer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QLottieFill6renderER15QLottieRenderer(
    const QLottieFill *self,
    QLottieRenderer *renderer) {
  self->render(*renderer);
}

//  int QLottieFill::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QLottieFill5parseERK11QJsonObject(
    QLottieFill *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  QColor QLottieFill::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QLottieFill5colorEv(const QLottieFill *self) {
  return new QColor(self->color());
}

//  qreal QLottieFill::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QLottieFill7opacityEv(const QLottieFill *self) {
  return self->opacity();
}

//  Qt::FillRule QLottieFill::fillRule() const
extern "C" Q_DECL_EXPORT
Qt::FillRule ritual_ZNK11QLottieFill8fillRuleEv(const QLottieFill *self) {
  return self->fillRule();
}

//  QLottieProperty4D<QVector4D> QLottieFill::colorProperty() const
extern "C" Q_DECL_EXPORT
QLottieProperty4D<QVector4D> *ritual_ZNK11QLottieFill13colorPropertyEv(
    const QLottieFill *self) {
  return new QLottieProperty4D<QVector4D>(self->colorProperty());
}

//  QLottieProperty<qreal> QLottieFill::opacityProperty() const
extern "C" Q_DECL_EXPORT
QLottieProperty<qreal> *ritual_ZNK11QLottieFill15opacityPropertyEv(
    const QLottieFill *self) {
  return new QLottieProperty<qreal>(self->opacityProperty());
}

//  QLottieFill::~QLottieFill()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieFillD1Ev(QLottieFill *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieFill, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieFill(
    QLottieFill *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieFill *>(self)->take(key, call);
}

//  QLottieBase *QLottieFill::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK11QLottieFill5cloneEv(const QLottieFill *self) {
  return self->QLottieFill::clone();
}

//  void QLottieFill::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QLottieFill16updatePropertiesEi(
    QLottieFill *self,
    int frame) {
  self->QLottieFill::updateProperties(frame);
}

//  int QLottieFill::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN11QLottieFill5parseERK11QJsonObject(
    QLottieFill *self,
    const QJsonObject *definition) {
  return self->QLottieFill::parse(*definition);
}

//  a QLottieProperty4D<QVector4D> a ritual of QLottieFill gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QLottieFill__QLottieProperty4D_QVector4D(
    QLottieProperty4D<QVector4D> *self) {
  delete self;
}

//  a QLottieProperty<qreal> a ritual of QLottieFill gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QLottieFill__QLottieProperty_qreal(
    QLottieProperty<qreal> *self) {
  delete self;
}
