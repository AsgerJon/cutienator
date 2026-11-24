//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgQualityStyle that Python can take functions over in. Every QSvgQualityStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgQualityStyleCall0)(const void *, int *);
typedef bool (*CuteQSvgQualityStyleCall1)(const void *, int *);
class CuteQSvgQualityStyle : public QSvgQualityStyle {
public:
  using QSvgQualityStyle::QSvgQualityStyle;
  CuteQSvgQualityStyle(const QSvgQualityStyle &other) : QSvgQualityStyle(other) {}
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

  //  Type QSvgQualityStyle::type() const
  QSvgStyleProperty::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgQualityStyleCall0 call = reinterpret_cast<CuteQSvgQualityStyleCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgStyleProperty::Type>(given);
    }
    return QSvgQualityStyle::type();
  }

  //  bool QSvgStyleProperty::isDefault() const
  bool isDefault() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgQualityStyleCall1 call = reinterpret_cast<CuteQSvgQualityStyleCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgStyleProperty::isDefault();
  }
};

//  QSvgQualityStyle::QSvgQualityStyle(int color)
extern "C" Q_DECL_EXPORT
QSvgQualityStyle *ritual_ZN16QSvgQualityStyleC1Ei(int color) {
  return new CuteQSvgQualityStyle(color);
}

//  QSvgQualityStyle::~QSvgQualityStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSvgQualityStyleD1Ev(QSvgQualityStyle *self) {
  delete self;
}

//  Type QSvgQualityStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_ZNK16QSvgQualityStyle4typeEv(
    const QSvgQualityStyle *self) {
  return self->type();
}

//  void QSvgQualityStyle::setImageRendering(ImageRendering a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSvgQualityStyle17setImageRenderingENS_14ImageRenderingE(
    QSvgQualityStyle *self,
    QSvgQualityStyle::ImageRendering a0) {
  self->setImageRendering(a0);
}

//  a Python function taken by a CuteQSvgQualityStyle, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgQualityStyle(
    QSvgQualityStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgQualityStyle *>(self)->take(key, call);
}

//  Type QSvgQualityStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_own_ZNK16QSvgQualityStyle4typeEv(
    const QSvgQualityStyle *self) {
  return self->QSvgQualityStyle::type();
}
