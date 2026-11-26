//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgOpacityStyle that Python can take functions over in. Every QSvgOpacityStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgOpacityStyleCall0)(const void *, int *);
typedef bool (*CuteQSvgOpacityStyleCall1)(const void *, int *);
class CuteQSvgOpacityStyle : public QSvgOpacityStyle {
public:
  using QSvgOpacityStyle::QSvgOpacityStyle;
  CuteQSvgOpacityStyle(const QSvgOpacityStyle & other) : QSvgOpacityStyle(other) {}
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

  //  Type QSvgOpacityStyle::type() const
  QSvgStyleProperty::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgOpacityStyleCall0 call = reinterpret_cast<CuteQSvgOpacityStyleCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgStyleProperty::Type>(given);
    }
    return QSvgOpacityStyle::type();
  }

  //  bool QSvgOpacityStyle::isDefault() const
  bool isDefault() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgOpacityStyleCall1 call = reinterpret_cast<CuteQSvgOpacityStyleCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgOpacityStyle::isDefault();
  }
};

//  QSvgOpacityStyle::QSvgOpacityStyle(qreal opacity)
extern "C" Q_DECL_EXPORT
QSvgOpacityStyle *ritual_ZN16QSvgOpacityStyleC1Ed(qreal opacity) {
  return new CuteQSvgOpacityStyle(opacity);
}

//  QSvgOpacityStyle::~QSvgOpacityStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSvgOpacityStyleD1Ev(QSvgOpacityStyle *self) {
  delete self;
}

//  void QSvgOpacityStyle::apply(QPainter *p, const QSvgNode *node,
//      QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSvgOpacityStyle5applyEP8QPainterPK8QSvgNodeR15QSvgExtraStates(
    QSvgOpacityStyle *self,
    QPainter *p,
    const QSvgNode *node,
    QSvgExtraStates *states) {
  self->apply(p, node, *states);
}

//  void QSvgOpacityStyle::revert(QPainter *p, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSvgOpacityStyle6revertEP8QPainterR15QSvgExtraStates(
    QSvgOpacityStyle *self,
    QPainter *p,
    QSvgExtraStates *states) {
  self->revert(p, *states);
}

//  Type QSvgOpacityStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_ZNK16QSvgOpacityStyle4typeEv(
    const QSvgOpacityStyle *self) {
  return self->type();
}

//  qreal QSvgOpacityStyle::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QSvgOpacityStyle7opacityEv(const QSvgOpacityStyle *self) {
  return self->opacity();
}

//  bool QSvgOpacityStyle::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSvgOpacityStyle9isDefaultEv(const QSvgOpacityStyle *self) {
  return self->isDefault();
}

//  a Python function taken by a CuteQSvgOpacityStyle, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgOpacityStyle(
    QSvgOpacityStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgOpacityStyle *>(self)->take(key, call);
}

//  Type QSvgOpacityStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_own_ZNK16QSvgOpacityStyle4typeEv(
    const QSvgOpacityStyle *self) {
  return self->QSvgOpacityStyle::type();
}

//  bool QSvgOpacityStyle::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QSvgOpacityStyle9isDefaultEv(
    const QSvgOpacityStyle *self) {
  return self->QSvgOpacityStyle::isDefault();
}
