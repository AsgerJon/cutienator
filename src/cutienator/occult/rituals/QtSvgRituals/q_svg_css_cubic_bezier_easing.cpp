//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgcsseasing_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgcsseasing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>

//  A QSvgCssCubicBezierEasing that Python can take functions over in. Every QSvgCssCubicBezierEasing
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQSvgCssCubicBezierEasingCall0)(const void *, qreal, int *);
class CuteQSvgCssCubicBezierEasing : public QSvgCssCubicBezierEasing {
public:
  using QSvgCssCubicBezierEasing::QSvgCssCubicBezierEasing;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QSvgEasingInterface8progressEd")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  qreal QSvgCssCubicBezierEasing::progress(qreal t) const
  qreal progress(qreal t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgCssCubicBezierEasingCall0 call = reinterpret_cast<CuteQSvgCssCubicBezierEasingCall0>(taken[0]);
      qreal given = call(this, t, &handled);
      if (handled) return given;
    }
    return QSvgCssCubicBezierEasing::progress(t);
  }
};

//  QSvgCssCubicBezierEasing::QSvgCssCubicBezierEasing(QSvgCssValues::EasingF
//      unction easingFunction, QPointF c1, QPointF c2)
extern "C" Q_DECL_EXPORT
QSvgCssCubicBezierEasing *ritual_ZN24QSvgCssCubicBezierEasingC1EN13QSvgCssValues14EasingFunctionE7QPointFS2_(
    QSvgCssValues::EasingFunction easingFunction,
    const QPointF *c1,
    const QPointF *c2) {
  return new CuteQSvgCssCubicBezierEasing(easingFunction, *c1, *c2);
}

//  QSvgCssCubicBezierEasing::~QSvgCssCubicBezierEasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSvgCssCubicBezierEasingD1Ev(
    QSvgCssCubicBezierEasing *self) {
  delete self;
}

//  qreal QSvgCssCubicBezierEasing::progress(qreal t) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QSvgCssCubicBezierEasing8progressEd(
    const QSvgCssCubicBezierEasing *self,
    qreal t) {
  return self->progress(t);
}

//  QPointF QSvgCssCubicBezierEasing::c1() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QSvgCssCubicBezierEasing2c1Ev(
    const QSvgCssCubicBezierEasing *self) {
  return new QPointF(self->c1());
}

//  QPointF QSvgCssCubicBezierEasing::c2() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QSvgCssCubicBezierEasing2c2Ev(
    const QSvgCssCubicBezierEasing *self) {
  return new QPointF(self->c2());
}

//  a Python function taken by a CuteQSvgCssCubicBezierEasing, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgCssCubicBezierEasing(
    QSvgCssCubicBezierEasing *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgCssCubicBezierEasing *>(self)->take(key, call);
}

//  qreal QSvgCssCubicBezierEasing::progress(qreal t) const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK24QSvgCssCubicBezierEasing8progressEd(
    const QSvgCssCubicBezierEasing *self,
    qreal t) {
  return self->QSvgCssCubicBezierEasing::progress(t);
}
