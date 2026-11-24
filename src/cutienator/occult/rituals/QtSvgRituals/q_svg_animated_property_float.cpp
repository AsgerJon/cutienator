//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QSvgAnimatedPropertyFloat that Python can take functions over in. Every QSvgAnimatedPropertyFloat
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSvgAnimatedPropertyFloatCall0)(const void *, uint, qreal, int *);
class CuteQSvgAnimatedPropertyFloat : public QSvgAnimatedPropertyFloat {
public:
  using QSvgAnimatedPropertyFloat::QSvgAnimatedPropertyFloat;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28QSvgAbstractAnimatedProperty11interpolateEjd")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QSvgAnimatedPropertyFloat::interpolate(uint index, qreal t)
  //      const
  void interpolate(uint index, qreal t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgAnimatedPropertyFloatCall0 call = reinterpret_cast<CuteQSvgAnimatedPropertyFloatCall0>(taken[0]);
      call(this, index, t, &handled);
      if (handled) return;
    }
    QSvgAnimatedPropertyFloat::interpolate(index, t);
  }
};

//  QSvgAnimatedPropertyFloat::QSvgAnimatedPropertyFloat(const QString &name)
extern "C" Q_DECL_EXPORT
QSvgAnimatedPropertyFloat *ritual_ZN25QSvgAnimatedPropertyFloatC1ERK7QString(
    const QString *name) {
  return new CuteQSvgAnimatedPropertyFloat(*name);
}

//  QSvgAnimatedPropertyFloat::~QSvgAnimatedPropertyFloat()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSvgAnimatedPropertyFloatD1Ev(
    QSvgAnimatedPropertyFloat *self) {
  delete self;
}

//  void QSvgAnimatedPropertyFloat::appendValue(const qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSvgAnimatedPropertyFloat11appendValueEd(
    QSvgAnimatedPropertyFloat *self,
    qreal value) {
  self->appendValue(value);
}

//  void QSvgAnimatedPropertyFloat::interpolate(uint index, qreal t) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QSvgAnimatedPropertyFloat11interpolateEjd(
    const QSvgAnimatedPropertyFloat *self,
    uint index,
    qreal t) {
  self->interpolate(index, t);
}

//  a Python function taken by a CuteQSvgAnimatedPropertyFloat, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgAnimatedPropertyFloat(
    QSvgAnimatedPropertyFloat *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgAnimatedPropertyFloat *>(self)->take(key, call);
}

//  void QSvgAnimatedPropertyFloat::interpolate(uint index, qreal t) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK25QSvgAnimatedPropertyFloat11interpolateEjd(
    const QSvgAnimatedPropertyFloat *self,
    uint index,
    qreal t) {
  self->QSvgAnimatedPropertyFloat::interpolate(index, t);
}
