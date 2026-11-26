//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <cstring>

//  A QSvgViewportFillStyle that Python can take functions over in. Every QSvgViewportFillStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgViewportFillStyleCall0)(const void *, int *);
typedef bool (*CuteQSvgViewportFillStyleCall1)(const void *, int *);
class CuteQSvgViewportFillStyle : public QSvgViewportFillStyle {
public:
  using QSvgViewportFillStyle::QSvgViewportFillStyle;
  CuteQSvgViewportFillStyle(const QSvgViewportFillStyle & other) : QSvgViewportFillStyle(other) {}
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

  //  Type QSvgViewportFillStyle::type() const
  QSvgStyleProperty::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgViewportFillStyleCall0 call = reinterpret_cast<CuteQSvgViewportFillStyleCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgStyleProperty::Type>(given);
    }
    return QSvgViewportFillStyle::type();
  }

  //  bool QSvgStyleProperty::isDefault() const
  bool isDefault() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgViewportFillStyleCall1 call = reinterpret_cast<CuteQSvgViewportFillStyleCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgStyleProperty::isDefault();
  }
};

//  QSvgViewportFillStyle::QSvgViewportFillStyle(const QBrush &brush)
extern "C" Q_DECL_EXPORT
QSvgViewportFillStyle *ritual_ZN21QSvgViewportFillStyleC1ERK6QBrush(
    const QBrush *brush) {
  return new CuteQSvgViewportFillStyle(*brush);
}

//  QSvgViewportFillStyle::~QSvgViewportFillStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSvgViewportFillStyleD1Ev(QSvgViewportFillStyle *self) {
  delete self;
}

//  void QSvgViewportFillStyle::apply(QPainter *p, const QSvgNode *node,
//      QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSvgViewportFillStyle5applyEP8QPainterPK8QSvgNodeR15QSvgExtraStates(
    QSvgViewportFillStyle *self,
    QPainter *p,
    const QSvgNode *node,
    QSvgExtraStates *states) {
  self->apply(p, node, *states);
}

//  void QSvgViewportFillStyle::revert(QPainter *p, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSvgViewportFillStyle6revertEP8QPainterR15QSvgExtraStates(
    QSvgViewportFillStyle *self,
    QPainter *p,
    QSvgExtraStates *states) {
  self->revert(p, *states);
}

//  Type QSvgViewportFillStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_ZNK21QSvgViewportFillStyle4typeEv(
    const QSvgViewportFillStyle *self) {
  return self->type();
}

//  const QBrush &QSvgViewportFillStyle::qbrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK21QSvgViewportFillStyle6qbrushEv(
    const QSvgViewportFillStyle *self) {
  return new QBrush(self->qbrush());
}

//  a Python function taken by a CuteQSvgViewportFillStyle, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgViewportFillStyle(
    QSvgViewportFillStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgViewportFillStyle *>(self)->take(key, call);
}

//  Type QSvgViewportFillStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_own_ZNK21QSvgViewportFillStyle4typeEv(
    const QSvgViewportFillStyle *self) {
  return self->QSvgViewportFillStyle::type();
}
