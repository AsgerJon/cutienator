//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <cstring>

//  A QSvgSolidColorPaint that Python can take functions over in. Every QSvgSolidColorPaint
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgSolidColorPaintCall0)(const void *, int *);
class CuteQSvgSolidColorPaint : public QSvgSolidColorPaint {
public:
  using QSvgSolidColorPaint::QSvgSolidColorPaint;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QSvgPaintServer4typeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgSolidColorPaint::type() const
  QSvgPaintServer::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgSolidColorPaintCall0 call = reinterpret_cast<CuteQSvgSolidColorPaintCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgPaintServer::Type>(given);
    }
    return QSvgSolidColorPaint::type();
  }
};

//  QSvgSolidColorPaint::QSvgSolidColorPaint(const QColor &color)
extern "C" Q_DECL_EXPORT
QSvgSolidColorPaint *ritual_ZN19QSvgSolidColorPaintC1ERK6QColor(
    const QColor *color) {
  return new CuteQSvgSolidColorPaint(*color);
}

//  QSvgSolidColorPaint::~QSvgSolidColorPaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSvgSolidColorPaintD1Ev(QSvgSolidColorPaint *self) {
  delete self;
}

//  Type QSvgSolidColorPaint::type() const
extern "C" Q_DECL_EXPORT
QSvgPaintServer::Type ritual_ZNK19QSvgSolidColorPaint4typeEv(
    const QSvgSolidColorPaint *self) {
  return self->type();
}

//  const QColor &QSvgSolidColorPaint::qcolor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QSvgSolidColorPaint6qcolorEv(
    const QSvgSolidColorPaint *self) {
  return new QColor(self->qcolor());
}

//  a Python function taken by a CuteQSvgSolidColorPaint, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgSolidColorPaint(
    QSvgSolidColorPaint *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgSolidColorPaint *>(self)->take(key, call);
}

//  Type QSvgSolidColorPaint::type() const
extern "C" Q_DECL_EXPORT
QSvgPaintServer::Type ritual_own_ZNK19QSvgSolidColorPaint4typeEv(
    const QSvgSolidColorPaint *self) {
  return self->QSvgSolidColorPaint::type();
}
