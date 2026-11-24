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

//  A QSvgCssEasing that Python can take functions over in. Every QSvgCssEasing
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQSvgCssEasingCall0)(const void *, qreal, int *);
class CuteQSvgCssEasing : public QSvgCssEasing {
public:
  using QSvgCssEasing::QSvgCssEasing;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QSvgEasingInterface8progressEd")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  qreal QSvgEasingInterface::progress(qreal t) const
  qreal progress(qreal t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgCssEasingCall0 call = reinterpret_cast<CuteQSvgCssEasingCall0>(taken[0]);
      qreal given = call(this, t, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QSvgCssEasing::~QSvgCssEasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgCssEasingD1Ev(QSvgCssEasing *self) {
  delete self;
}

//  QSvgCssValues::EasingFunction QSvgCssEasing::easingFunction() const
extern "C" Q_DECL_EXPORT
QSvgCssValues::EasingFunction ritual_ZNK13QSvgCssEasing14easingFunctionEv(
    const QSvgCssEasing *self) {
  return self->easingFunction();
}

//  a Python function taken by a CuteQSvgCssEasing, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgCssEasing(
    QSvgCssEasing *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgCssEasing *>(self)->take(key, call);
}

#endif  // QT_CONFIG(cssparser)
