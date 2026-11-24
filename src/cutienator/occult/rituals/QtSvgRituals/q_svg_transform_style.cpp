//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <cstring>

//  A QSvgTransformStyle that Python can take functions over in. Every QSvgTransformStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgTransformStyleCall0)(const void *, int *);
typedef bool (*CuteQSvgTransformStyleCall1)(const void *, int *);
class CuteQSvgTransformStyle : public QSvgTransformStyle {
public:
  using QSvgTransformStyle::QSvgTransformStyle;
  CuteQSvgTransformStyle(const QSvgTransformStyle &other) : QSvgTransformStyle(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QSvgStyleProperty4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QSvgStyleProperty9isDefaultEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgTransformStyle::type() const
  QSvgStyleProperty::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgTransformStyleCall0 call = reinterpret_cast<CuteQSvgTransformStyleCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgStyleProperty::Type>(given);
    }
    return QSvgTransformStyle::type();
  }

  //  bool QSvgTransformStyle::isDefault() const
  bool isDefault() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgTransformStyleCall1 call = reinterpret_cast<CuteQSvgTransformStyleCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgTransformStyle::isDefault();
  }
};

//  QSvgTransformStyle::QSvgTransformStyle(const QTransform &transform)
extern "C" Q_DECL_EXPORT
QSvgTransformStyle *ritual_ZN18QSvgTransformStyleC1ERK10QTransform(
    const QTransform *transform) {
  return new CuteQSvgTransformStyle(*transform);
}

//  QSvgTransformStyle::~QSvgTransformStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSvgTransformStyleD1Ev(QSvgTransformStyle *self) {
  delete self;
}

//  Type QSvgTransformStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_ZNK18QSvgTransformStyle4typeEv(
    const QSvgTransformStyle *self) {
  return self->type();
}

//  const QTransform &QSvgTransformStyle::qtransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK18QSvgTransformStyle10qtransformEv(
    const QSvgTransformStyle *self) {
  return new QTransform(self->qtransform());
}

//  bool QSvgTransformStyle::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSvgTransformStyle9isDefaultEv(
    const QSvgTransformStyle *self) {
  return self->isDefault();
}

//  a Python function taken by a CuteQSvgTransformStyle, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgTransformStyle(
    QSvgTransformStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgTransformStyle *>(self)->take(key, call);
}

//  Type QSvgTransformStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_own_ZNK18QSvgTransformStyle4typeEv(
    const QSvgTransformStyle *self) {
  return self->QSvgTransformStyle::type();
}

//  bool QSvgTransformStyle::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QSvgTransformStyle9isDefaultEv(
    const QSvgTransformStyle *self) {
  return self->QSvgTransformStyle::isDefault();
}
