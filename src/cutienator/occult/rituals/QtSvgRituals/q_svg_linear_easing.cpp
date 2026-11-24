//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvganimate_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvganimate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgLinearEasing that Python can take functions over in. Every QSvgLinearEasing
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQSvgLinearEasingCall0)(const void *, qreal, int *);
class CuteQSvgLinearEasing : public QSvgLinearEasing {
public:
  using QSvgLinearEasing::QSvgLinearEasing;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QSvgEasingInterface8progressEd")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  qreal QSvgLinearEasing::progress(qreal t) const
  qreal progress(qreal t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgLinearEasingCall0 call = reinterpret_cast<CuteQSvgLinearEasingCall0>(taken[0]);
      qreal given = call(this, t, &handled);
      if (handled) return given;
    }
    return QSvgLinearEasing::progress(t);
  }
};

//  QSvgLinearEasing::~QSvgLinearEasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSvgLinearEasingD1Ev(QSvgLinearEasing *self) {
  delete self;
}

//  qreal QSvgLinearEasing::progress(qreal t) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QSvgLinearEasing8progressEd(
    const QSvgLinearEasing *self,
    qreal t) {
  return self->progress(t);
}

//  a Python function taken by a CuteQSvgLinearEasing, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgLinearEasing(
    QSvgLinearEasing *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgLinearEasing *>(self)->take(key, call);
}

//  qreal QSvgLinearEasing::progress(qreal t) const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK16QSvgLinearEasing8progressEd(
    const QSvgLinearEasing *self,
    qreal t) {
  return self->QSvgLinearEasing::progress(t);
}
