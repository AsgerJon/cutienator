//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qfusionstyle_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfusionstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpalette.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qicon.h>
#include <QtGui/qfontmetrics.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QFusionStyle that Python can take functions over in. Every QFusionStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(style_fusion)
typedef const QPalette * (*CuteQFusionStyleCall0)(const void *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef void (*CuteQFusionStyleCall1)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef void (*CuteQFusionStyleCall2)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef int (*CuteQFusionStyleCall3)(const void *, int, const QStyleOption *, const QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef void (*CuteQFusionStyleCall4)(const void *, int, const QStyleOptionComplex *, QPainter *, const QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef const QRect * (*CuteQFusionStyleCall5)(const void *, int, const QStyleOption *, const QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef const QSize * (*CuteQFusionStyleCall6)(const void *, int, const QStyleOption *, const QSize *, const QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef int (*CuteQFusionStyleCall7)(const void *, int, const QStyleOptionComplex *, const QPoint *, const QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef const QRect * (*CuteQFusionStyleCall8)(const void *, int, const QStyleOptionComplex *, int, const QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef const QPixmap * (*CuteQFusionStyleCall9)(const void *, int, const QPixmap *, const QStyleOption *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef int (*CuteQFusionStyleCall10)(const void *, int, const QStyleOption *, const QWidget *, QStyleHintReturn *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef const QRect * (*CuteQFusionStyleCall11)(const void *, const QRect *, int, const QPixmap *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef const QIcon * (*CuteQFusionStyleCall12)(const void *, int, const QStyleOption *, const QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef const QPixmap * (*CuteQFusionStyleCall13)(const void *, int, const QStyleOption *, const QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef void (*CuteQFusionStyleCall14)(const void *, QPainter *, const QRect *, int, const QPixmap *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef void (*CuteQFusionStyleCall15)(const void *, QPainter *, const QRect *, int, const QPalette *, bool, const QString *, int, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef void (*CuteQFusionStyleCall16)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef void (*CuteQFusionStyleCall17)(const void *, QApplication *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef void (*CuteQFusionStyleCall18)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
typedef void (*CuteQFusionStyleCall19)(const void *, QApplication *, int *);
#endif  // QT_CONFIG(style_fusion)
typedef int (*CuteQFusionStyleCall20)(const void *, int, int, int, const QStyleOption *, const QWidget *, int *);
typedef const QRect * (*CuteQFusionStyleCall21)(const void *, const QFontMetrics *, const QRect *, int, bool, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFusionStyleCall22)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFusionStyleCall23)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFusionStyleCall24)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFusionStyleCall25)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFusionStyleCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFusionStyleCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFusionStyleCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFusionStyle : public QFusionStyle {
public:
  using QFusionStyle::QFusionStyle;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle15standardPaletteEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle13drawPrimitiveENS_16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle11drawControlENS_14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK7QWidget")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOptionPK7QWidget")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOptionComplexNS_10SubControlEPK7QWidget")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle9styleHintENS_9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZN6QStyle6polishEP7QWidget")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZN6QStyle6polishEP12QApplication")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP7QWidget")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP12QApplication")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(style_fusion)
    if (!std::strcmp(key, "_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString")) {
      taken[21] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(style_fusion)
  //  QPalette QFusionStyle::standardPalette() const
  QPalette standardPalette() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFusionStyleCall0 call = reinterpret_cast<CuteQFusionStyleCall0>(taken[0]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFusionStyle::standardPalette();
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  void QFusionStyle::drawPrimitive(PrimitiveElement elem, const
  //      QStyleOption *option, QPainter *painter, const QWidget *widget)
  //      const
  void drawPrimitive(
      QStyle::PrimitiveElement elem,
      const QStyleOption *option,
      QPainter *painter,
      const QWidget *widget) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFusionStyleCall1 call = reinterpret_cast<CuteQFusionStyleCall1>(taken[1]);
      call(this, static_cast<int>(elem), option, painter, widget, &handled);
      if (handled) return;
    }
    QFusionStyle::drawPrimitive(elem, option, painter, widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  void QFusionStyle::drawControl(ControlElement ce, const QStyleOption
  //      *option, QPainter *painter, const QWidget *widget) const
  void drawControl(
      QStyle::ControlElement ce,
      const QStyleOption *option,
      QPainter *painter,
      const QWidget *widget) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQFusionStyleCall2 call = reinterpret_cast<CuteQFusionStyleCall2>(taken[2]);
      call(this, static_cast<int>(ce), option, painter, widget, &handled);
      if (handled) return;
    }
    QFusionStyle::drawControl(ce, option, painter, widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  int QFusionStyle::pixelMetric(PixelMetric metric, const QStyleOption
  //      *option, const QWidget *widget) const
  int pixelMetric(
      QStyle::PixelMetric metric,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFusionStyleCall3 call = reinterpret_cast<CuteQFusionStyleCall3>(taken[3]);
      int given = call(this, static_cast<int>(metric), option, widget, &handled);
      if (handled) return given;
    }
    return QFusionStyle::pixelMetric(metric, option, widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  void QFusionStyle::drawComplexControl(ComplexControl control, const
  //      QStyleOptionComplex *option, QPainter *painter, const QWidget
  //      *widget) const
  void drawComplexControl(
      QStyle::ComplexControl control,
      const QStyleOptionComplex *option,
      QPainter *painter,
      const QWidget *widget) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFusionStyleCall4 call = reinterpret_cast<CuteQFusionStyleCall4>(taken[4]);
      call(this, static_cast<int>(control), option, painter, widget, &handled);
      if (handled) return;
    }
    QFusionStyle::drawComplexControl(control, option, painter, widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  QRect QFusionStyle::subElementRect(SubElement r, const QStyleOption
  //      *opt, const QWidget *widget) const
  QRect subElementRect(
      QStyle::SubElement r,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFusionStyleCall5 call = reinterpret_cast<CuteQFusionStyleCall5>(taken[5]);
      const QRect * given = call(this, static_cast<int>(r), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QFusionStyle::subElementRect(r, opt, widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  QSize QFusionStyle::sizeFromContents(ContentsType type, const
  //      QStyleOption *option, const QSize &size, const QWidget *widget)
  //      const
  QSize sizeFromContents(
      QStyle::ContentsType type,
      const QStyleOption *option,
      const QSize &size,
      const QWidget *widget) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFusionStyleCall6 call = reinterpret_cast<CuteQFusionStyleCall6>(taken[6]);
      const QSize * given = call(this, static_cast<int>(type), option, &size, widget, &handled);
      if (handled && given) return *given;
    }
    return QFusionStyle::sizeFromContents(type, option, size, widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  SubControl QFusionStyle::hitTestComplexControl(ComplexControl cc,
  //      const QStyleOptionComplex *opt, const QPoint &pt, const QWidget
  //      *w) const
  QStyle::SubControl hitTestComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      const QPoint &pt,
      const QWidget *w) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFusionStyleCall7 call = reinterpret_cast<CuteQFusionStyleCall7>(taken[7]);
      int given = call(this, static_cast<int>(cc), opt, &pt, w, &handled);
      if (handled) return static_cast<QStyle::SubControl>(given);
    }
    return QFusionStyle::hitTestComplexControl(cc, opt, pt, w);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  QRect QFusionStyle::subControlRect(ComplexControl cc, const
  //      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget)
  //      const
  QRect subControlRect(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QStyle::SubControl sc,
      const QWidget *widget) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFusionStyleCall8 call = reinterpret_cast<CuteQFusionStyleCall8>(taken[8]);
      const QRect * given = call(this, static_cast<int>(cc), opt, static_cast<int>(sc), widget, &handled);
      if (handled && given) return *given;
    }
    return QFusionStyle::subControlRect(cc, opt, sc, widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  QPixmap QFusionStyle::generatedIconPixmap(QIcon::Mode iconMode, const
  //      QPixmap &pixmap, const QStyleOption *opt) const
  QPixmap generatedIconPixmap(
      QIcon::Mode iconMode,
      const QPixmap &pixmap,
      const QStyleOption *opt) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFusionStyleCall9 call = reinterpret_cast<CuteQFusionStyleCall9>(taken[9]);
      const QPixmap * given = call(this, static_cast<int>(iconMode), &pixmap, opt, &handled);
      if (handled && given) return *given;
    }
    return QFusionStyle::generatedIconPixmap(iconMode, pixmap, opt);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  int QFusionStyle::styleHint(StyleHint hint, const QStyleOption
  //      *option, const QWidget *widget, QStyleHintReturn *returnData)
  //      const
  int styleHint(
      QStyle::StyleHint hint,
      const QStyleOption *option,
      const QWidget *widget,
      QStyleHintReturn *returnData) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFusionStyleCall10 call = reinterpret_cast<CuteQFusionStyleCall10>(taken[10]);
      int given = call(this, static_cast<int>(hint), option, widget, returnData, &handled);
      if (handled) return given;
    }
    return QFusionStyle::styleHint(hint, option, widget, returnData);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  QRect QFusionStyle::itemPixmapRect(const QRect &r, int flags, const
  //      QPixmap &pixmap) const
  QRect itemPixmapRect(
      const QRect &r,
      int flags,
      const QPixmap &pixmap) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQFusionStyleCall11 call = reinterpret_cast<CuteQFusionStyleCall11>(taken[11]);
      const QRect * given = call(this, &r, flags, &pixmap, &handled);
      if (handled && given) return *given;
    }
    return QFusionStyle::itemPixmapRect(r, flags, pixmap);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  QIcon QFusionStyle::standardIcon(StandardPixmap standardIcon, const
  //      QStyleOption *option, const QWidget *widget) const
  QIcon standardIcon(
      QStyle::StandardPixmap standardIcon,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQFusionStyleCall12 call = reinterpret_cast<CuteQFusionStyleCall12>(taken[12]);
      const QIcon * given = call(this, static_cast<int>(standardIcon), option, widget, &handled);
      if (handled && given) return *given;
    }
    return QFusionStyle::standardIcon(standardIcon, option, widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  QPixmap QFusionStyle::standardPixmap(StandardPixmap standardPixmap,
  //      const QStyleOption *opt, const QWidget *widget) const
  QPixmap standardPixmap(
      QStyle::StandardPixmap standardPixmap,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQFusionStyleCall13 call = reinterpret_cast<CuteQFusionStyleCall13>(taken[13]);
      const QPixmap * given = call(this, static_cast<int>(standardPixmap), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QFusionStyle::standardPixmap(standardPixmap, opt, widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  void QFusionStyle::drawItemPixmap(QPainter *painter, const QRect
  //      &rect, int alignment, const QPixmap &pixmap) const
  void drawItemPixmap(
      QPainter *painter,
      const QRect &rect,
      int alignment,
      const QPixmap &pixmap) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQFusionStyleCall14 call = reinterpret_cast<CuteQFusionStyleCall14>(taken[14]);
      call(this, painter, &rect, alignment, &pixmap, &handled);
      if (handled) return;
    }
    QFusionStyle::drawItemPixmap(painter, rect, alignment, pixmap);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  void QFusionStyle::drawItemText(QPainter *painter, const QRect &rect,
  //      int flags, const QPalette &pal, bool enabled, const QString
  //      &text, QPalette::ColorRole textRole) const
  void drawItemText(
      QPainter *painter,
      const QRect &rect,
      int flags,
      const QPalette &pal,
      bool enabled,
      const QString &text,
      QPalette::ColorRole textRole) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQFusionStyleCall15 call = reinterpret_cast<CuteQFusionStyleCall15>(taken[15]);
      call(this, painter, &rect, flags, &pal, enabled, &text, static_cast<int>(textRole), &handled);
      if (handled) return;
    }
    QFusionStyle::drawItemText(painter, rect, flags, pal, enabled, text, textRole);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  void QFusionStyle::polish(QWidget *widget)
  void polish(QWidget *widget) override {
    if (taken[16]) {
      int handled = 0;
      CuteQFusionStyleCall16 call = reinterpret_cast<CuteQFusionStyleCall16>(taken[16]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QFusionStyle::polish(widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  void QFusionStyle::polish(QApplication *app)
  void polish(QApplication *app) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFusionStyleCall17 call = reinterpret_cast<CuteQFusionStyleCall17>(taken[17]);
      call(this, app, &handled);
      if (handled) return;
    }
    QFusionStyle::polish(app);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  void QFusionStyle::unpolish(QWidget *widget)
  void unpolish(QWidget *widget) override {
    if (taken[18]) {
      int handled = 0;
      CuteQFusionStyleCall18 call = reinterpret_cast<CuteQFusionStyleCall18>(taken[18]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QFusionStyle::unpolish(widget);
  }
#endif  // QT_CONFIG(style_fusion)

#if QT_CONFIG(style_fusion)
  //  void QFusionStyle::unpolish(QApplication *app)
  void unpolish(QApplication *app) override {
    if (taken[19]) {
      int handled = 0;
      CuteQFusionStyleCall19 call = reinterpret_cast<CuteQFusionStyleCall19>(taken[19]);
      call(this, app, &handled);
      if (handled) return;
    }
    QFusionStyle::unpolish(app);
  }
#endif  // QT_CONFIG(style_fusion)

  //  int QCommonStyle::layoutSpacing(QSizePolicy::ControlType control1,
  //      QSizePolicy::ControlType control2, Qt::Orientation orientation,
  //      const QStyleOption *option, const QWidget *widget) const
  int layoutSpacing(
      QSizePolicy::ControlType control1,
      QSizePolicy::ControlType control2,
      Qt::Orientation orientation,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQFusionStyleCall20 call = reinterpret_cast<CuteQFusionStyleCall20>(taken[20]);
      int given = call(this, static_cast<int>(control1), static_cast<int>(control2), static_cast<int>(orientation), option, widget, &handled);
      if (handled) return given;
    }
    return QCommonStyle::layoutSpacing(control1, control2, orientation, option, widget);
  }

  //  QRect QStyle::itemTextRect(const QFontMetrics &fm, const QRect &r,
  //      int flags, bool enabled, const QString &text) const
  QRect itemTextRect(
      const QFontMetrics &fm,
      const QRect &r,
      int flags,
      bool enabled,
      const QString &text) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQFusionStyleCall21 call = reinterpret_cast<CuteQFusionStyleCall21>(taken[21]);
      const QRect * given = call(this, &fm, &r, flags, enabled, &text, &handled);
      if (handled && given) return *given;
    }
    return QStyle::itemTextRect(fm, r, flags, enabled, text);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFusionStyleCall22 call = reinterpret_cast<CuteQFusionStyleCall22>(taken[22]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFusionStyleCall23 call = reinterpret_cast<CuteQFusionStyleCall23>(taken[23]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFusionStyleCall24 call = reinterpret_cast<CuteQFusionStyleCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQFusionStyleCall25 call = reinterpret_cast<CuteQFusionStyleCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQFusionStyleCall26 call = reinterpret_cast<CuteQFusionStyleCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQFusionStyleCall27 call = reinterpret_cast<CuteQFusionStyleCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQFusionStyleCall28 call = reinterpret_cast<CuteQFusionStyleCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFusionStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QFusionStyle10metaObjectEv(
    const QFusionStyle *self) {
  return self->metaObject();
}

//  void *QFusionStyle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QFusionStyle11qt_metacastEPKc(
    QFusionStyle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QFusionStyle::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QFusionStyle11qt_metacallEN11QMetaObject4CallEiPPv(
    QFusionStyle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QFusionStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QFusionStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFusionStyle::tr(s, c, n));
}

//  QFusionStylePrivate *QFusionStyle::d_func()
extern "C" Q_DECL_EXPORT
QFusionStylePrivate *ritual_ZN12QFusionStyle6d_funcEv(QFusionStyle *self) {
  return self->d_func();
}

//  const QFusionStylePrivate *QFusionStyle::d_func() const
extern "C" Q_DECL_EXPORT
const QFusionStylePrivate *ritual_ZNK12QFusionStyle6d_funcEv(
    const QFusionStyle *self) {
  return self->d_func();
}

//  QFusionStyle::QFusionStyle()
extern "C" Q_DECL_EXPORT
QFusionStyle *ritual_ZN12QFusionStyleC1Ev() {
  return new CuteQFusionStyle();
}

//  QFusionStyle::~QFusionStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFusionStyleD1Ev(QFusionStyle *self) {
  delete self;
}

//  QPalette QFusionStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK12QFusionStyle15standardPaletteEv(
    const QFusionStyle *self) {
  return new QPalette(self->standardPalette());
}

//  void QFusionStyle::drawPrimitive(PrimitiveElement elem, const
//      QStyleOption *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QFusionStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QFusionStyle *self,
    QStyle::PrimitiveElement elem,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawPrimitive(elem, option, painter, widget);
}

//  void QFusionStyle::drawControl(ControlElement ce, const QStyleOption
//      *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QFusionStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QFusionStyle *self,
    QStyle::ControlElement ce,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawControl(ce, option, painter, widget);
}

//  int QFusionStyle::pixelMetric(PixelMetric metric, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFusionStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QFusionStyle *self,
    QStyle::PixelMetric metric,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->pixelMetric(metric, option, widget);
}

//  void QFusionStyle::drawComplexControl(ComplexControl control, const
//      QStyleOptionComplex *option, QPainter *painter, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QFusionStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QFusionStyle *self,
    QStyle::ComplexControl control,
    const QStyleOptionComplex *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawComplexControl(control, option, painter, widget);
}

//  QRect QFusionStyle::subElementRect(SubElement r, const QStyleOption *opt,
//      const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QFusionStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QFusionStyle *self,
    QStyle::SubElement r,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QRect(self->subElementRect(r, opt, widget));
}

//  QSize QFusionStyle::sizeFromContents(ContentsType type, const
//      QStyleOption *option, const QSize &size, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QFusionStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QFusionStyle *self,
    QStyle::ContentsType type,
    const QStyleOption *option,
    const QSize *size,
    const QWidget *widget) {
  return new QSize(self->sizeFromContents(type, option, *size, widget));
}

//  SubControl QFusionStyle::hitTestComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, const QPoint &pt, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_ZNK12QFusionStyle21hitTestComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QFusionStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    const QPoint *pt,
    const QWidget *w) {
  return self->hitTestComplexControl(cc, opt, *pt, w);
}

//  QRect QFusionStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QFusionStyle14subControlRectEN6QStyle14ComplexControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget(
    const QFusionStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QStyle::SubControl sc,
    const QWidget *widget) {
  return new QRect(self->subControlRect(cc, opt, sc, widget));
}

//  QPixmap QFusionStyle::generatedIconPixmap(QIcon::Mode iconMode, const
//      QPixmap &pixmap, const QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK12QFusionStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption(
    const QFusionStyle *self,
    QIcon::Mode iconMode,
    const QPixmap *pixmap,
    const QStyleOption *opt) {
  return new QPixmap(self->generatedIconPixmap(iconMode, *pixmap, opt));
}

//  int QFusionStyle::styleHint(StyleHint hint, const QStyleOption *option,
//      const QWidget *widget, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFusionStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QFusionStyle *self,
    QStyle::StyleHint hint,
    const QStyleOption *option,
    const QWidget *widget,
    QStyleHintReturn *returnData) {
  return self->styleHint(hint, option, widget, returnData);
}

//  QRect QFusionStyle::itemPixmapRect(const QRect &r, int flags, const
//      QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QFusionStyle14itemPixmapRectERK5QRectiRK7QPixmap(
    const QFusionStyle *self,
    const QRect *r,
    int flags,
    const QPixmap *pixmap) {
  return new QRect(self->itemPixmapRect(*r, flags, *pixmap));
}

//  QIcon QFusionStyle::iconFromTheme(StandardPixmap standardIcon) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK12QFusionStyle13iconFromThemeEN6QStyle14StandardPixmapE(
    const QFusionStyle *self,
    QStyle::StandardPixmap standardIcon) {
  return new QIcon(self->iconFromTheme(standardIcon));
}

//  QIcon QFusionStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK12QFusionStyle12standardIconEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QFusionStyle *self,
    QStyle::StandardPixmap standardIcon,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QIcon(self->standardIcon(standardIcon, option, widget));
}

//  QPixmap QFusionStyle::standardPixmap(StandardPixmap standardPixmap, const
//      QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK12QFusionStyle14standardPixmapEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QFusionStyle *self,
    QStyle::StandardPixmap standardPixmap,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QPixmap(self->standardPixmap(standardPixmap, opt, widget));
}

//  void QFusionStyle::drawItemPixmap(QPainter *painter, const QRect &rect,
//      int alignment, const QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QFusionStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap(
    const QFusionStyle *self,
    QPainter *painter,
    const QRect *rect,
    int alignment,
    const QPixmap *pixmap) {
  self->drawItemPixmap(painter, *rect, alignment, *pixmap);
}

//  void QFusionStyle::drawItemText(QPainter *painter, const QRect &rect, int
//      flags, const QPalette &pal, bool enabled, const QString &text,
//      QPalette::ColorRole textRole) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QFusionStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE(
    const QFusionStyle *self,
    QPainter *painter,
    const QRect *rect,
    int flags,
    const QPalette *pal,
    bool enabled,
    const QString *text,
    QPalette::ColorRole textRole) {
  self->drawItemText(painter, *rect, flags, *pal, enabled, *text, textRole);
}

//  void QFusionStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFusionStyle6polishEP7QWidget(
    QFusionStyle *self,
    QWidget *widget) {
  self->polish(widget);
}

//  void QFusionStyle::polish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFusionStyle6polishEP12QApplication(
    QFusionStyle *self,
    QApplication *app) {
  self->polish(app);
}

//  void QFusionStyle::polish(QPalette &pal)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFusionStyle6polishER8QPalette(
    QFusionStyle *self,
    QPalette *pal) {
  self->polish(*pal);
}

//  void QFusionStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFusionStyle8unpolishEP7QWidget(
    QFusionStyle *self,
    QWidget *widget) {
  self->unpolish(widget);
}

//  void QFusionStyle::unpolish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFusionStyle8unpolishEP12QApplication(
    QFusionStyle *self,
    QApplication *app) {
  self->unpolish(app);
}

//  QFusionStyle::QFusionStyle(QFusionStylePrivate &dd)
extern "C" Q_DECL_EXPORT
QFusionStyle *ritual_ZN12QFusionStyleC1ER19QFusionStylePrivate(
    QFusionStylePrivate *dd) {
  return new CuteQFusionStyle(*dd);
}

//  bool QFusionStyle::isHighContrast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QFusionStyle14isHighContrastEv(const QFusionStyle *self) {
  return self->isHighContrast();
}

//  Qt::ColorScheme QFusionStyle::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_ZNK12QFusionStyle11colorSchemeEv(
    const QFusionStyle *self) {
  return self->colorScheme();
}

//  a Python function taken by a CuteQFusionStyle, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFusionStyle(
    QFusionStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFusionStyle *>(self)->take(key, call);
}

//  QPalette QFusionStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK12QFusionStyle15standardPaletteEv(
    const QFusionStyle *self) {
  return new QPalette(self->QFusionStyle::standardPalette());
}

//  void QFusionStyle::drawPrimitive(PrimitiveElement elem, const
//      QStyleOption *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QFusionStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QFusionStyle *self,
    QStyle::PrimitiveElement elem,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->QFusionStyle::drawPrimitive(elem, option, painter, widget);
}

//  void QFusionStyle::drawControl(ControlElement ce, const QStyleOption
//      *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QFusionStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QFusionStyle *self,
    QStyle::ControlElement ce,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->QFusionStyle::drawControl(ce, option, painter, widget);
}

//  int QFusionStyle::pixelMetric(PixelMetric metric, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QFusionStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QFusionStyle *self,
    QStyle::PixelMetric metric,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->QFusionStyle::pixelMetric(metric, option, widget);
}

//  void QFusionStyle::drawComplexControl(ComplexControl control, const
//      QStyleOptionComplex *option, QPainter *painter, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QFusionStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QFusionStyle *self,
    QStyle::ComplexControl control,
    const QStyleOptionComplex *option,
    QPainter *painter,
    const QWidget *widget) {
  self->QFusionStyle::drawComplexControl(control, option, painter, widget);
}

//  QRect QFusionStyle::subElementRect(SubElement r, const QStyleOption *opt,
//      const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK12QFusionStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QFusionStyle *self,
    QStyle::SubElement r,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QRect(self->QFusionStyle::subElementRect(r, opt, widget));
}

//  QSize QFusionStyle::sizeFromContents(ContentsType type, const
//      QStyleOption *option, const QSize &size, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QFusionStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QFusionStyle *self,
    QStyle::ContentsType type,
    const QStyleOption *option,
    const QSize *size,
    const QWidget *widget) {
  return new QSize(
      self->QFusionStyle::sizeFromContents(
          type,
          option,
          *size,
          widget));
}

//  SubControl QFusionStyle::hitTestComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, const QPoint &pt, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_own_ZNK12QFusionStyle21hitTestComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QFusionStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    const QPoint *pt,
    const QWidget *w) {
  return self->QFusionStyle::hitTestComplexControl(cc, opt, *pt, w);
}

//  QRect QFusionStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK12QFusionStyle14subControlRectEN6QStyle14ComplexControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget(
    const QFusionStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QStyle::SubControl sc,
    const QWidget *widget) {
  return new QRect(self->QFusionStyle::subControlRect(cc, opt, sc, widget));
}

//  QPixmap QFusionStyle::generatedIconPixmap(QIcon::Mode iconMode, const
//      QPixmap &pixmap, const QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK12QFusionStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption(
    const QFusionStyle *self,
    QIcon::Mode iconMode,
    const QPixmap *pixmap,
    const QStyleOption *opt) {
  return new QPixmap(
      self->QFusionStyle::generatedIconPixmap(
          iconMode,
          *pixmap,
          opt));
}

//  int QFusionStyle::styleHint(StyleHint hint, const QStyleOption *option,
//      const QWidget *widget, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QFusionStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QFusionStyle *self,
    QStyle::StyleHint hint,
    const QStyleOption *option,
    const QWidget *widget,
    QStyleHintReturn *returnData) {
  return self->QFusionStyle::styleHint(hint, option, widget, returnData);
}

//  QRect QFusionStyle::itemPixmapRect(const QRect &r, int flags, const
//      QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK12QFusionStyle14itemPixmapRectERK5QRectiRK7QPixmap(
    const QFusionStyle *self,
    const QRect *r,
    int flags,
    const QPixmap *pixmap) {
  return new QRect(self->QFusionStyle::itemPixmapRect(*r, flags, *pixmap));
}

//  QIcon QFusionStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK12QFusionStyle12standardIconEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QFusionStyle *self,
    QStyle::StandardPixmap standardIcon,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QIcon(
      self->QFusionStyle::standardIcon(
          standardIcon,
          option,
          widget));
}

//  QPixmap QFusionStyle::standardPixmap(StandardPixmap standardPixmap, const
//      QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK12QFusionStyle14standardPixmapEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QFusionStyle *self,
    QStyle::StandardPixmap standardPixmap,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QPixmap(
      self->QFusionStyle::standardPixmap(
          standardPixmap,
          opt,
          widget));
}

//  void QFusionStyle::drawItemPixmap(QPainter *painter, const QRect &rect,
//      int alignment, const QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QFusionStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap(
    const QFusionStyle *self,
    QPainter *painter,
    const QRect *rect,
    int alignment,
    const QPixmap *pixmap) {
  self->QFusionStyle::drawItemPixmap(painter, *rect, alignment, *pixmap);
}

//  void QFusionStyle::drawItemText(QPainter *painter, const QRect &rect, int
//      flags, const QPalette &pal, bool enabled, const QString &text,
//      QPalette::ColorRole textRole) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QFusionStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE(
    const QFusionStyle *self,
    QPainter *painter,
    const QRect *rect,
    int flags,
    const QPalette *pal,
    bool enabled,
    const QString *text,
    QPalette::ColorRole textRole) {
  self->QFusionStyle::drawItemText(
      painter,
      *rect,
      flags,
      *pal,
      enabled,
      *text,
      textRole);
}

//  void QFusionStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QFusionStyle6polishEP7QWidget(
    QFusionStyle *self,
    QWidget *widget) {
  self->QFusionStyle::polish(widget);
}

//  void QFusionStyle::polish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QFusionStyle6polishEP12QApplication(
    QFusionStyle *self,
    QApplication *app) {
  self->QFusionStyle::polish(app);
}

//  void QFusionStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QFusionStyle8unpolishEP7QWidget(
    QFusionStyle *self,
    QWidget *widget) {
  self->QFusionStyle::unpolish(widget);
}

//  void QFusionStyle::unpolish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QFusionStyle8unpolishEP12QApplication(
    QFusionStyle *self,
    QApplication *app) {
  self->QFusionStyle::unpolish(app);
}

#endif  // QT_CONFIG(style_fusion)
#endif  // QT_CONFIG(style_fusion)
