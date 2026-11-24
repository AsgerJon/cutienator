//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgCompOpStyle that Python can take functions over in. Every QSvgCompOpStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgCompOpStyleCall0)(const void *, int *);
typedef bool (*CuteQSvgCompOpStyleCall1)(const void *, int *);
class CuteQSvgCompOpStyle : public QSvgCompOpStyle {
public:
  using QSvgCompOpStyle::QSvgCompOpStyle;
  CuteQSvgCompOpStyle(const QSvgCompOpStyle &other) : QSvgCompOpStyle(other) {}
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

  //  Type QSvgCompOpStyle::type() const
  QSvgStyleProperty::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgCompOpStyleCall0 call = reinterpret_cast<CuteQSvgCompOpStyleCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgStyleProperty::Type>(given);
    }
    return QSvgCompOpStyle::type();
  }

  //  bool QSvgStyleProperty::isDefault() const
  bool isDefault() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgCompOpStyleCall1 call = reinterpret_cast<CuteQSvgCompOpStyleCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgStyleProperty::isDefault();
  }
};

//  QSvgCompOpStyle::QSvgCompOpStyle(QPainter::CompositionMode mode)
extern "C" Q_DECL_EXPORT
QSvgCompOpStyle *ritual_ZN15QSvgCompOpStyleC1EN8QPainter15CompositionModeE(
    QPainter::CompositionMode mode) {
  return new CuteQSvgCompOpStyle(mode);
}

//  QSvgCompOpStyle::~QSvgCompOpStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgCompOpStyleD1Ev(QSvgCompOpStyle *self) {
  delete self;
}

//  Type QSvgCompOpStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_ZNK15QSvgCompOpStyle4typeEv(
    const QSvgCompOpStyle *self) {
  return self->type();
}

//  a Python function taken by a CuteQSvgCompOpStyle, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgCompOpStyle(
    QSvgCompOpStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgCompOpStyle *>(self)->take(key, call);
}

//  Type QSvgCompOpStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_own_ZNK15QSvgCompOpStyle4typeEv(
    const QSvgCompOpStyle *self) {
  return self->QSvgCompOpStyle::type();
}
