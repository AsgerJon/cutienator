//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvganimate_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvganimate_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgAnimateColor that Python can take functions over in. Every QSvgAnimateColor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgAnimateColorCall0)(const void *, int *);
typedef int (*CuteQSvgAnimateColorCall1)(const void *, int *);
typedef bool (*CuteQSvgAnimateColorCall2)(const void *, int *);
typedef bool (*CuteQSvgAnimateColorCall3)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgAnimateColorCall4)(const void *, int *);
typedef void (*CuteQSvgAnimateColorCall5)(const void *, QSvgAbstractAnimatedProperty *, int *);
class CuteQSvgAnimateColor : public QSvgAnimateColor {
public:
  using QSvgAnimateColor::QSvgAnimateColor;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QSvgAbstractAnimation13animationTypeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QSvgAbstractAnimation8isActiveEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QSvgAbstractAnimation14appendPropertyEP28QSvgAbstractAnimatedProperty")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgAnimateColor::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgAnimateColorCall0 call = reinterpret_cast<CuteQSvgAnimateColorCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgAnimateColor::type();
  }

  //  AnimationType QSvgAnimateNode::animationType() const
  QSvgAbstractAnimation::AnimationType animationType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgAnimateColorCall1 call = reinterpret_cast<CuteQSvgAnimateColorCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgAbstractAnimation::AnimationType>(given);
    }
    return QSvgAnimateNode::animationType();
  }

  //  bool QSvgAnimateNode::isActive() const
  bool isActive() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgAnimateColorCall2 call = reinterpret_cast<CuteQSvgAnimateColorCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgAnimateNode::isActive();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgAnimateColorCall3 call = reinterpret_cast<CuteQSvgAnimateColorCall3>(taken[3]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSvgAnimateColorCall4 call = reinterpret_cast<CuteQSvgAnimateColorCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }

  //  void
  //      QSvgAbstractAnimation::appendProperty(QSvgAbstractAnimatedPropert
  //      y *property)
  void appendProperty(QSvgAbstractAnimatedProperty *property) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSvgAnimateColorCall5 call = reinterpret_cast<CuteQSvgAnimateColorCall5>(taken[5]);
      call(this, property, &handled);
      if (handled) return;
    }
    QSvgAbstractAnimation::appendProperty(property);
  }
};

//  QSvgAnimateColor::QSvgAnimateColor()
extern "C" Q_DECL_EXPORT
QSvgAnimateColor *ritual_ZN16QSvgAnimateColorC1Ev() {
  return new CuteQSvgAnimateColor();
}

//  QSvgAnimateColor::QSvgAnimateColor(QSvgNode *parent)
extern "C" Q_DECL_EXPORT
QSvgAnimateColor *ritual_ZN16QSvgAnimateColorC1EP8QSvgNode(
    QSvgNode *parent) {
  return new CuteQSvgAnimateColor(parent);
}

//  QSvgAnimateColor::~QSvgAnimateColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSvgAnimateColorD1Ev(QSvgAnimateColor *self) {
  delete self;
}

//  Type QSvgAnimateColor::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK16QSvgAnimateColor4typeEv(
    const QSvgAnimateColor *self) {
  return self->type();
}

//  a Python function taken by a CuteQSvgAnimateColor, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgAnimateColor(
    QSvgAnimateColor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgAnimateColor *>(self)->take(key, call);
}

//  Type QSvgAnimateColor::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK16QSvgAnimateColor4typeEv(
    const QSvgAnimateColor *self) {
  return self->QSvgAnimateColor::type();
}
