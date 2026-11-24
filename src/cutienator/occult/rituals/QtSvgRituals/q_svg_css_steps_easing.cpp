//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgcsseasing_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtSvg/qtsvgglobal.h>
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#if QT_CONFIG(cssparser)
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgcsseasing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgCssStepsEasing that Python can take functions over in. Every QSvgCssStepsEasing
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQSvgCssStepsEasingCall0)(const void *, qreal, int *);
class CuteQSvgCssStepsEasing : public QSvgCssStepsEasing {
public:
  using QSvgCssStepsEasing::QSvgCssStepsEasing;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QSvgEasingInterface8progressEd")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  qreal QSvgCssStepsEasing::progress(qreal t) const
  qreal progress(qreal t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgCssStepsEasingCall0 call = reinterpret_cast<CuteQSvgCssStepsEasingCall0>(taken[0]);
      qreal given = call(this, t, &handled);
      if (handled) return given;
    }
    return QSvgCssStepsEasing::progress(t);
  }
};

//  QSvgCssStepsEasing::QSvgCssStepsEasing(quint32 stops,
//      QSvgCssValues::StepPosition position)
extern "C" Q_DECL_EXPORT
QSvgCssStepsEasing *ritual_ZN18QSvgCssStepsEasingC1EjN13QSvgCssValues12StepPositionE(
    quint32 stops,
    QSvgCssValues::StepPosition position) {
  return new CuteQSvgCssStepsEasing(stops, position);
}

//  QSvgCssStepsEasing::~QSvgCssStepsEasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSvgCssStepsEasingD1Ev(QSvgCssStepsEasing *self) {
  delete self;
}

//  qreal QSvgCssStepsEasing::progress(qreal t) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QSvgCssStepsEasing8progressEd(
    const QSvgCssStepsEasing *self,
    qreal t) {
  return self->progress(t);
}

//  quint32 QSvgCssStepsEasing::stops() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK18QSvgCssStepsEasing5stopsEv(
    const QSvgCssStepsEasing *self) {
  return self->stops();
}

//  QSvgCssValues::StepPosition QSvgCssStepsEasing::stepPosition() const
extern "C" Q_DECL_EXPORT
QSvgCssValues::StepPosition ritual_ZNK18QSvgCssStepsEasing12stepPositionEv(
    const QSvgCssStepsEasing *self) {
  return self->stepPosition();
}

//  a Python function taken by a CuteQSvgCssStepsEasing, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgCssStepsEasing(
    QSvgCssStepsEasing *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgCssStepsEasing *>(self)->take(key, call);
}

//  qreal QSvgCssStepsEasing::progress(qreal t) const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK18QSvgCssStepsEasing8progressEd(
    const QSvgCssStepsEasing *self,
    qreal t) {
  return self->QSvgCssStepsEasing::progress(t);
}

#endif  // QT_CONFIG(cssparser)
