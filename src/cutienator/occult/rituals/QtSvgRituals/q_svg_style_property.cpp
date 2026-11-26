//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgStyleProperty that Python can take functions over in. Every QSvgStyleProperty
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgStylePropertyCall0)(const void *, int *);
typedef bool (*CuteQSvgStylePropertyCall1)(const void *, int *);
class CuteQSvgStyleProperty : public QSvgStyleProperty {
public:
  using QSvgStyleProperty::QSvgStyleProperty;
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

  //  Type QSvgStyleProperty::type() const
  QSvgStyleProperty::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgStylePropertyCall0 call = reinterpret_cast<CuteQSvgStylePropertyCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgStyleProperty::Type>(given);
    }
    return {};
  }

  //  bool QSvgStyleProperty::isDefault() const
  bool isDefault() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgStylePropertyCall1 call = reinterpret_cast<CuteQSvgStylePropertyCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgStyleProperty::isDefault();
  }
};

//  QSvgStyleProperty::~QSvgStyleProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgStylePropertyD1Ev(QSvgStyleProperty *self) {
  delete self;
}

//  void QSvgStyleProperty::apply(QPainter *p, const QSvgNode *node,
//      QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgStyleProperty5applyEP8QPainterPK8QSvgNodeR15QSvgExtraStates(
    QSvgStyleProperty *self,
    QPainter *p,
    const QSvgNode *node,
    QSvgExtraStates *states) {
  self->apply(p, node, *states);
}

//  void QSvgStyleProperty::revert(QPainter *p, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgStyleProperty6revertEP8QPainterR15QSvgExtraStates(
    QSvgStyleProperty *self,
    QPainter *p,
    QSvgExtraStates *states) {
  self->revert(p, *states);
}

//  Type QSvgStyleProperty::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_ZNK17QSvgStyleProperty4typeEv(
    const QSvgStyleProperty *self) {
  return self->type();
}

//  bool QSvgStyleProperty::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSvgStyleProperty9isDefaultEv(
    const QSvgStyleProperty *self) {
  return self->isDefault();
}

//  a Python function taken by a CuteQSvgStyleProperty, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgStyleProperty(
    QSvgStyleProperty *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgStyleProperty *>(self)->take(key, call);
}

//  bool QSvgStyleProperty::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QSvgStyleProperty9isDefaultEv(
    const QSvgStyleProperty *self) {
  return self->QSvgStyleProperty::isDefault();
}
