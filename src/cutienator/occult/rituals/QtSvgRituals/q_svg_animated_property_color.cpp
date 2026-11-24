//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSvgAnimatedPropertyColor that Python can take functions over in. Every QSvgAnimatedPropertyColor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSvgAnimatedPropertyColorCall0)(const void *, uint, qreal, int *);
class CuteQSvgAnimatedPropertyColor : public QSvgAnimatedPropertyColor {
public:
  using QSvgAnimatedPropertyColor::QSvgAnimatedPropertyColor;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28QSvgAbstractAnimatedProperty11interpolateEjd")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QSvgAnimatedPropertyColor::interpolate(uint index, qreal t)
  //      const
  void interpolate(uint index, qreal t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgAnimatedPropertyColorCall0 call = reinterpret_cast<CuteQSvgAnimatedPropertyColorCall0>(taken[0]);
      call(this, index, t, &handled);
      if (handled) return;
    }
    QSvgAnimatedPropertyColor::interpolate(index, t);
  }
};

//  QSvgAnimatedPropertyColor::QSvgAnimatedPropertyColor(const QString &name)
extern "C" Q_DECL_EXPORT
QSvgAnimatedPropertyColor *ritual_ZN25QSvgAnimatedPropertyColorC1ERK7QString(
    const QString *name) {
  return new CuteQSvgAnimatedPropertyColor(*name);
}

//  QSvgAnimatedPropertyColor::~QSvgAnimatedPropertyColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSvgAnimatedPropertyColorD1Ev(
    QSvgAnimatedPropertyColor *self) {
  delete self;
}

//  void QSvgAnimatedPropertyColor::setColors(const QList<QColor> &colors)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSvgAnimatedPropertyColor9setColorsERK5QListI6QColorE(
    QSvgAnimatedPropertyColor *self,
    const QList<QColor> *colors) {
  self->setColors(*colors);
}

//  void QSvgAnimatedPropertyColor::appendColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSvgAnimatedPropertyColor11appendColorERK6QColor(
    QSvgAnimatedPropertyColor *self,
    const QColor *color) {
  self->appendColor(*color);
}

//  QList<QColor> QSvgAnimatedPropertyColor::colors() const
extern "C" Q_DECL_EXPORT
QList<QColor> *ritual_ZNK25QSvgAnimatedPropertyColor6colorsEv(
    const QSvgAnimatedPropertyColor *self) {
  return new QList<QColor>(self->colors());
}

//  void QSvgAnimatedPropertyColor::interpolate(uint index, qreal t) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QSvgAnimatedPropertyColor11interpolateEjd(
    const QSvgAnimatedPropertyColor *self,
    uint index,
    qreal t) {
  self->interpolate(index, t);
}

//  a Python function taken by a CuteQSvgAnimatedPropertyColor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgAnimatedPropertyColor(
    QSvgAnimatedPropertyColor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgAnimatedPropertyColor *>(self)->take(key, call);
}

//  void QSvgAnimatedPropertyColor::interpolate(uint index, qreal t) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK25QSvgAnimatedPropertyColor11interpolateEjd(
    const QSvgAnimatedPropertyColor *self,
    uint index,
    qreal t) {
  self->QSvgAnimatedPropertyColor::interpolate(index, t);
}
