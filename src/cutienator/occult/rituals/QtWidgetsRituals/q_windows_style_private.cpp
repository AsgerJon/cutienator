//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwindowsstyle_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(style_windows)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwindowsstyle_p.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwindowsstyle_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QWindowsStylePrivate that Python can take functions over in. Every QWindowsStylePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(tabbar)
typedef void (*CuteQWindowsStylePrivateCall0)(const void *, const QStyleOptionTab *, const QWidget *, QRect *, QRect *, int *);
#endif  // QT_CONFIG(tabbar)
class CuteQWindowsStylePrivate : public QWindowsStylePrivate {
public:
  using QWindowsStylePrivate::QWindowsStylePrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK19QCommonStylePrivate9tabLayoutEPK15QStyleOptionTabPK7QWidgetP5QRectS7_")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
    return false;
  }

#if QT_CONFIG(tabbar)
  //  void QCommonStylePrivate::tabLayout(const QStyleOptionTab *opt, const
  //      QWidget *widget, QRect *textRect, QRect *pixmapRect) const
  void tabLayout(
      const QStyleOptionTab *opt,
      const QWidget *widget,
      QRect *textRect,
      QRect *pixmapRect) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsStylePrivateCall0 call = reinterpret_cast<CuteQWindowsStylePrivateCall0>(taken[0]);
      call(this, opt, widget, textRect, pixmapRect, &handled);
      if (handled) return;
    }
    QCommonStylePrivate::tabLayout(opt, widget, textRect, pixmapRect);
  }
#endif  // QT_CONFIG(tabbar)
};

//  QWindowsStyle *QWindowsStylePrivate::q_func()
extern "C" Q_DECL_EXPORT
QWindowsStyle *ritual_ZN20QWindowsStylePrivate6q_funcEv(
    QWindowsStylePrivate *self) {
  return self->q_func();
}

//  const QWindowsStyle *QWindowsStylePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWindowsStyle *ritual_ZNK20QWindowsStylePrivate6q_funcEv(
    const QWindowsStylePrivate *self) {
  return self->q_func();
}

//  QWindowsStylePrivate::QWindowsStylePrivate()
extern "C" Q_DECL_EXPORT
QWindowsStylePrivate *ritual_ZN20QWindowsStylePrivateC1Ev() {
  return new CuteQWindowsStylePrivate();
}

//  int QWindowsStylePrivate::pixelMetricFromSystemDp(QStyle::PixelMetric pm,
//      const QStyleOption *option, const QWidget *widget)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QWindowsStylePrivate23pixelMetricFromSystemDpEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    QStyle::PixelMetric pm,
    const QStyleOption *option,
    const QWidget *widget) {
  return QWindowsStylePrivate::pixelMetricFromSystemDp(pm, option, widget);
}

//  int QWindowsStylePrivate::fixedPixelMetric(QStyle::PixelMetric pm)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QWindowsStylePrivate16fixedPixelMetricEN6QStyle11PixelMetricE(
    QStyle::PixelMetric pm) {
  return QWindowsStylePrivate::fixedPixelMetric(pm);
}

//  qreal QWindowsStylePrivate::nativeMetricScaleFactor(const QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QWindowsStylePrivate23nativeMetricScaleFactorEPK7QWidget(
    const QWidget *widget) {
  return QWindowsStylePrivate::nativeMetricScaleFactor(widget);
}

//  bool QWindowsStylePrivate::hasSeenAlt(const QWidget *widget) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWindowsStylePrivate10hasSeenAltEPK7QWidget(
    const QWindowsStylePrivate *self,
    const QWidget *widget) {
  return self->hasSeenAlt(widget);
}

//  bool QWindowsStylePrivate::altDown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWindowsStylePrivate7altDownEv(
    const QWindowsStylePrivate *self) {
  return self->altDown();
}

//  a Python function taken by a CuteQWindowsStylePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsStylePrivate(
    QWindowsStylePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsStylePrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(style_windows)
