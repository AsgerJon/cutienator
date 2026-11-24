//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <cstring>

//  A QSvgFontStyle that Python can take functions over in. Every QSvgFontStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFontStyleCall0)(const void *, int *);
typedef bool (*CuteQSvgFontStyleCall1)(const void *, int *);
class CuteQSvgFontStyle : public QSvgFontStyle {
public:
  using QSvgFontStyle::QSvgFontStyle;
  CuteQSvgFontStyle(const QSvgFontStyle &other) : QSvgFontStyle(other) {}
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

  //  Type QSvgFontStyle::type() const
  QSvgStyleProperty::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFontStyleCall0 call = reinterpret_cast<CuteQSvgFontStyleCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgStyleProperty::Type>(given);
    }
    return QSvgFontStyle::type();
  }

  //  bool QSvgStyleProperty::isDefault() const
  bool isDefault() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFontStyleCall1 call = reinterpret_cast<CuteQSvgFontStyleCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgStyleProperty::isDefault();
  }
};

//  QSvgFontStyle::QSvgFontStyle()
extern "C" Q_DECL_EXPORT
QSvgFontStyle *ritual_ZN13QSvgFontStyleC1Ev() {
  return new CuteQSvgFontStyle();
}

//  QSvgFontStyle::~QSvgFontStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFontStyleD1Ev(QSvgFontStyle *self) {
  delete self;
}

//  Type QSvgFontStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_ZNK13QSvgFontStyle4typeEv(
    const QSvgFontStyle *self) {
  return self->type();
}

//  void QSvgFontStyle::setSize(qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFontStyle7setSizeEd(QSvgFontStyle *self, qreal size) {
  self->setSize(size);
}

//  void QSvgFontStyle::setTextAnchor(Qt::Alignment anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFontStyle13setTextAnchorE6QFlagsIN2Qt13AlignmentFlagEE(
    QSvgFontStyle *self,
    int anchor) {
  self->setTextAnchor(QFlags<Qt::AlignmentFlag>::fromInt(anchor));
}

//  void QSvgFontStyle::setFamily(const QString &family)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFontStyle9setFamilyERK7QString(
    QSvgFontStyle *self,
    const QString *family) {
  self->setFamily(*family);
}

//  void QSvgFontStyle::setStyle(QFont::Style fontStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFontStyle8setStyleEN5QFont5StyleE(
    QSvgFontStyle *self,
    QFont::Style fontStyle) {
  self->setStyle(fontStyle);
}

//  void QSvgFontStyle::setVariant(QFont::Capitalization fontVariant)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFontStyle10setVariantEN5QFont14CapitalizationE(
    QSvgFontStyle *self,
    QFont::Capitalization fontVariant) {
  self->setVariant(fontVariant);
}

//  void QSvgFontStyle::setWeight(int weight)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFontStyle9setWeightEi(QSvgFontStyle *self, int weight) {
  self->setWeight(weight);
}

//  const QFont &QSvgFontStyle::qfont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QSvgFontStyle5qfontEv(const QSvgFontStyle *self) {
  return new QFont(self->qfont());
}

//  a Python function taken by a CuteQSvgFontStyle, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFontStyle(
    QSvgFontStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFontStyle *>(self)->take(key, call);
}

//  Type QSvgFontStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_own_ZNK13QSvgFontStyle4typeEv(
    const QSvgFontStyle *self) {
  return self->QSvgFontStyle::type();
}
