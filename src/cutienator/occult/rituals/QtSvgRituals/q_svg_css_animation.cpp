//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgcssanimation_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgcssanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgCssAnimation that Python can take functions over in. Every QSvgCssAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgCssAnimationCall0)(const void *, int *);
typedef void (*CuteQSvgCssAnimationCall1)(const void *, QSvgAbstractAnimatedProperty *, int *);
typedef bool (*CuteQSvgCssAnimationCall2)(const void *, int *);
class CuteQSvgCssAnimation : public QSvgCssAnimation {
public:
  using QSvgCssAnimation::QSvgCssAnimation;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QSvgAbstractAnimation13animationTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QSvgAbstractAnimation14appendPropertyEP28QSvgAbstractAnimatedProperty")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QSvgAbstractAnimation8isActiveEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  AnimationType QSvgCssAnimation::animationType() const
  QSvgAbstractAnimation::AnimationType animationType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgCssAnimationCall0 call = reinterpret_cast<CuteQSvgCssAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgAbstractAnimation::AnimationType>(given);
    }
    return QSvgCssAnimation::animationType();
  }

  //  void
  //      QSvgAbstractAnimation::appendProperty(QSvgAbstractAnimatedPropert
  //      y *property)
  void appendProperty(QSvgAbstractAnimatedProperty *property) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgCssAnimationCall1 call = reinterpret_cast<CuteQSvgCssAnimationCall1>(taken[1]);
      call(this, property, &handled);
      if (handled) return;
    }
    QSvgAbstractAnimation::appendProperty(property);
  }

  //  bool QSvgAbstractAnimation::isActive() const
  bool isActive() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgCssAnimationCall2 call = reinterpret_cast<CuteQSvgCssAnimationCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgAbstractAnimation::isActive();
  }
};

//  QSvgCssAnimation::QSvgCssAnimation()
extern "C" Q_DECL_EXPORT
QSvgCssAnimation *ritual_ZN16QSvgCssAnimationC1Ev() {
  return new CuteQSvgCssAnimation();
}

//  QSvgCssAnimation::~QSvgCssAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSvgCssAnimationD1Ev(QSvgCssAnimation *self) {
  delete self;
}

//  AnimationType QSvgCssAnimation::animationType() const
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimation::AnimationType ritual_ZNK16QSvgCssAnimation13animationTypeEv(
    const QSvgCssAnimation *self) {
  return self->animationType();
}

//  a Python function taken by a CuteQSvgCssAnimation, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgCssAnimation(
    QSvgCssAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgCssAnimation *>(self)->take(key, call);
}

//  AnimationType QSvgCssAnimation::animationType() const
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimation::AnimationType ritual_own_ZNK16QSvgCssAnimation13animationTypeEv(
    const QSvgCssAnimation *self) {
  return self->QSvgCssAnimation::animationType();
}
