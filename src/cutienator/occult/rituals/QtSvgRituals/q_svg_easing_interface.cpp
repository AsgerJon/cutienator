//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgeasinginterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgeasinginterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgEasingInterface that Python can take functions over in. Every QSvgEasingInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQSvgEasingInterfaceCall0)(const void *, qreal, int *);
class CuteQSvgEasingInterface : public QSvgEasingInterface {
public:
  using QSvgEasingInterface::QSvgEasingInterface;
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
      CuteQSvgEasingInterfaceCall0 call = reinterpret_cast<CuteQSvgEasingInterfaceCall0>(taken[0]);
      qreal given = call(this, t, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QSvgEasingInterface::QSvgEasingInterface()
extern "C" Q_DECL_EXPORT
QSvgEasingInterface *ritual_ZN19QSvgEasingInterfaceC1Ev() {
  return new CuteQSvgEasingInterface();
}

//  QSvgEasingInterface::~QSvgEasingInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSvgEasingInterfaceD1Ev(QSvgEasingInterface *self) {
  delete self;
}

//  qreal QSvgEasingInterface::progress(qreal t) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QSvgEasingInterface8progressEd(
    const QSvgEasingInterface *self,
    qreal t) {
  return self->progress(t);
}

//  a Python function taken by a CuteQSvgEasingInterface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgEasingInterface(
    QSvgEasingInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgEasingInterface *>(self)->take(key, call);
}
