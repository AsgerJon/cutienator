//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qpixmapstyle_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qpixmapstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmargins.h>
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qicon.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qfontmetrics.h>
#include <QtGui/qpalette.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPixmapStyle that Python can take functions over in. Every QPixmapStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPixmapStyleCall0)(const void *, QApplication *, int *);
typedef void (*CuteQPixmapStyleCall1)(const void *, QWidget *, int *);
typedef void (*CuteQPixmapStyleCall2)(const void *, QApplication *, int *);
typedef void (*CuteQPixmapStyleCall3)(const void *, QWidget *, int *);
typedef void (*CuteQPixmapStyleCall4)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef void (*CuteQPixmapStyleCall5)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef void (*CuteQPixmapStyleCall6)(const void *, int, const QStyleOptionComplex *, QPainter *, const QWidget *, int *);
typedef const QSize * (*CuteQPixmapStyleCall7)(const void *, int, const QStyleOption *, const QSize *, const QWidget *, int *);
typedef const QRect * (*CuteQPixmapStyleCall8)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QRect * (*CuteQPixmapStyleCall9)(const void *, int, const QStyleOptionComplex *, int, const QWidget *, int *);
typedef int (*CuteQPixmapStyleCall10)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef int (*CuteQPixmapStyleCall11)(const void *, int, const QStyleOption *, const QWidget *, QStyleHintReturn *, int *);
typedef int (*CuteQPixmapStyleCall12)(const void *, int, const QStyleOptionComplex *, const QPoint *, const QWidget *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPixmapStyleCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef const QIcon * (*CuteQPixmapStyleCall14)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QPixmap * (*CuteQPixmapStyleCall15)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QPixmap * (*CuteQPixmapStyleCall16)(const void *, int, const QPixmap *, const QStyleOption *, int *);
typedef int (*CuteQPixmapStyleCall17)(const void *, int, int, int, const QStyleOption *, const QWidget *, int *);
typedef const QRect * (*CuteQPixmapStyleCall18)(const void *, const QFontMetrics *, const QRect *, int, bool, const QString *, int *);
typedef const QRect * (*CuteQPixmapStyleCall19)(const void *, const QRect *, int, const QPixmap *, int *);
typedef void (*CuteQPixmapStyleCall20)(const void *, QPainter *, const QRect *, int, const QPalette *, bool, const QString *, int, int *);
typedef void (*CuteQPixmapStyleCall21)(const void *, QPainter *, const QRect *, int, const QPixmap *, int *);
typedef const QPalette * (*CuteQPixmapStyleCall22)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPixmapStyleCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapStyleCall24)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapStyleCall25)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapStyleCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapStyleCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapStyleCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPixmapStyle : public QPixmapStyle {
public:
  using QPixmapStyle::QPixmapStyle;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QStyle6polishEP12QApplication")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle6polishEP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP12QApplication")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP7QWidget")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle13drawPrimitiveENS_16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle11drawControlENS_14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOptionPK7QWidget")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOptionComplexNS_10SubControlEPK7QWidget")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK7QWidget")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle9styleHintENS_9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget")) {
      taken[12] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle15standardPaletteEv")) {
      taken[22] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
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

  //  void QPixmapStyle::polish(QApplication *application)
  void polish(QApplication *application) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPixmapStyleCall0 call = reinterpret_cast<CuteQPixmapStyleCall0>(taken[0]);
      call(this, application, &handled);
      if (handled) return;
    }
    QPixmapStyle::polish(application);
  }

  //  void QPixmapStyle::polish(QWidget *widget)
  void polish(QWidget *widget) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPixmapStyleCall1 call = reinterpret_cast<CuteQPixmapStyleCall1>(taken[1]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QPixmapStyle::polish(widget);
  }

  //  void QPixmapStyle::unpolish(QApplication *application)
  void unpolish(QApplication *application) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPixmapStyleCall2 call = reinterpret_cast<CuteQPixmapStyleCall2>(taken[2]);
      call(this, application, &handled);
      if (handled) return;
    }
    QPixmapStyle::unpolish(application);
  }

  //  void QPixmapStyle::unpolish(QWidget *widget)
  void unpolish(QWidget *widget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPixmapStyleCall3 call = reinterpret_cast<CuteQPixmapStyleCall3>(taken[3]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QPixmapStyle::unpolish(widget);
  }

  //  void QPixmapStyle::drawPrimitive(PrimitiveElement element, const
  //      QStyleOption *option, QPainter *painter, const QWidget *widget)
  //      const
  void drawPrimitive(
      QStyle::PrimitiveElement element,
      const QStyleOption *option,
      QPainter *painter,
      const QWidget *widget) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPixmapStyleCall4 call = reinterpret_cast<CuteQPixmapStyleCall4>(taken[4]);
      call(this, static_cast<int>(element), option, painter, widget, &handled);
      if (handled) return;
    }
    QPixmapStyle::drawPrimitive(element, option, painter, widget);
  }

  //  void QPixmapStyle::drawControl(ControlElement element, const
  //      QStyleOption *option, QPainter *painter, const QWidget *widget)
  //      const
  void drawControl(
      QStyle::ControlElement element,
      const QStyleOption *option,
      QPainter *painter,
      const QWidget *widget) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPixmapStyleCall5 call = reinterpret_cast<CuteQPixmapStyleCall5>(taken[5]);
      call(this, static_cast<int>(element), option, painter, widget, &handled);
      if (handled) return;
    }
    QPixmapStyle::drawControl(element, option, painter, widget);
  }

  //  void QPixmapStyle::drawComplexControl(ComplexControl cc, const
  //      QStyleOptionComplex *option, QPainter *painter, const QWidget
  //      *widget) const
  void drawComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *option,
      QPainter *painter,
      const QWidget *widget) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPixmapStyleCall6 call = reinterpret_cast<CuteQPixmapStyleCall6>(taken[6]);
      call(this, static_cast<int>(cc), option, painter, widget, &handled);
      if (handled) return;
    }
    QPixmapStyle::drawComplexControl(cc, option, painter, widget);
  }

  //  QSize QPixmapStyle::sizeFromContents(ContentsType type, const
  //      QStyleOption *option, const QSize &contentsSize, const QWidget
  //      *widget) const
  QSize sizeFromContents(
      QStyle::ContentsType type,
      const QStyleOption *option,
      const QSize &contentsSize,
      const QWidget *widget) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPixmapStyleCall7 call = reinterpret_cast<CuteQPixmapStyleCall7>(taken[7]);
      const QSize * given = call(this, static_cast<int>(type), option, &contentsSize, widget, &handled);
      if (handled && given) return *given;
    }
    return QPixmapStyle::sizeFromContents(type, option, contentsSize, widget);
  }

  //  QRect QPixmapStyle::subElementRect(SubElement element, const
  //      QStyleOption *option, const QWidget *widget) const
  QRect subElementRect(
      QStyle::SubElement element,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPixmapStyleCall8 call = reinterpret_cast<CuteQPixmapStyleCall8>(taken[8]);
      const QRect * given = call(this, static_cast<int>(element), option, widget, &handled);
      if (handled && given) return *given;
    }
    return QPixmapStyle::subElementRect(element, option, widget);
  }

  //  QRect QPixmapStyle::subControlRect(ComplexControl cc, const
  //      QStyleOptionComplex *option, SubControl sc, const QWidget
  //      *widget) const
  QRect subControlRect(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *option,
      QStyle::SubControl sc,
      const QWidget *widget) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPixmapStyleCall9 call = reinterpret_cast<CuteQPixmapStyleCall9>(taken[9]);
      const QRect * given = call(this, static_cast<int>(cc), option, static_cast<int>(sc), widget, &handled);
      if (handled && given) return *given;
    }
    return QPixmapStyle::subControlRect(cc, option, sc, widget);
  }

  //  int QPixmapStyle::pixelMetric(PixelMetric metric, const QStyleOption
  //      *option, const QWidget *widget) const
  int pixelMetric(
      QStyle::PixelMetric metric,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPixmapStyleCall10 call = reinterpret_cast<CuteQPixmapStyleCall10>(taken[10]);
      int given = call(this, static_cast<int>(metric), option, widget, &handled);
      if (handled) return given;
    }
    return QPixmapStyle::pixelMetric(metric, option, widget);
  }

  //  int QPixmapStyle::styleHint(StyleHint hint, const QStyleOption
  //      *option, const QWidget *widget, QStyleHintReturn *returnData)
  //      const
  int styleHint(
      QStyle::StyleHint hint,
      const QStyleOption *option,
      const QWidget *widget,
      QStyleHintReturn *returnData) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPixmapStyleCall11 call = reinterpret_cast<CuteQPixmapStyleCall11>(taken[11]);
      int given = call(this, static_cast<int>(hint), option, widget, returnData, &handled);
      if (handled) return given;
    }
    return QPixmapStyle::styleHint(hint, option, widget, returnData);
  }

  //  SubControl QPixmapStyle::hitTestComplexControl(ComplexControl
  //      control, const QStyleOptionComplex *option, const QPoint &pos,
  //      const QWidget *widget) const
  QStyle::SubControl hitTestComplexControl(
      QStyle::ComplexControl control,
      const QStyleOptionComplex *option,
      const QPoint &pos,
      const QWidget *widget) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPixmapStyleCall12 call = reinterpret_cast<CuteQPixmapStyleCall12>(taken[12]);
      int given = call(this, static_cast<int>(control), option, &pos, widget, &handled);
      if (handled) return static_cast<QStyle::SubControl>(given);
    }
    return QPixmapStyle::hitTestComplexControl(control, option, pos, widget);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QPixmapStyle::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPixmapStyleCall13 call = reinterpret_cast<CuteQPixmapStyleCall13>(taken[13]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QPixmapStyle::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QIcon QCommonStyle::standardIcon(StandardPixmap standardIcon, const
  //      QStyleOption *opt, const QWidget *widget) const
  QIcon standardIcon(
      QStyle::StandardPixmap standardIcon,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPixmapStyleCall14 call = reinterpret_cast<CuteQPixmapStyleCall14>(taken[14]);
      const QIcon * given = call(this, static_cast<int>(standardIcon), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QCommonStyle::standardIcon(standardIcon, opt, widget);
  }

  //  QPixmap QCommonStyle::standardPixmap(StandardPixmap sp, const
  //      QStyleOption *opt, const QWidget *widget) const
  QPixmap standardPixmap(
      QStyle::StandardPixmap sp,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQPixmapStyleCall15 call = reinterpret_cast<CuteQPixmapStyleCall15>(taken[15]);
      const QPixmap * given = call(this, static_cast<int>(sp), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QCommonStyle::standardPixmap(sp, opt, widget);
  }

  //  QPixmap QCommonStyle::generatedIconPixmap(QIcon::Mode iconMode, const
  //      QPixmap &pixmap, const QStyleOption *opt) const
  QPixmap generatedIconPixmap(
      QIcon::Mode iconMode,
      const QPixmap &pixmap,
      const QStyleOption *opt) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQPixmapStyleCall16 call = reinterpret_cast<CuteQPixmapStyleCall16>(taken[16]);
      const QPixmap * given = call(this, static_cast<int>(iconMode), &pixmap, opt, &handled);
      if (handled && given) return *given;
    }
    return QCommonStyle::generatedIconPixmap(iconMode, pixmap, opt);
  }

  //  int QCommonStyle::layoutSpacing(QSizePolicy::ControlType control1,
  //      QSizePolicy::ControlType control2, Qt::Orientation orientation,
  //      const QStyleOption *option, const QWidget *widget) const
  int layoutSpacing(
      QSizePolicy::ControlType control1,
      QSizePolicy::ControlType control2,
      Qt::Orientation orientation,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQPixmapStyleCall17 call = reinterpret_cast<CuteQPixmapStyleCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQPixmapStyleCall18 call = reinterpret_cast<CuteQPixmapStyleCall18>(taken[18]);
      const QRect * given = call(this, &fm, &r, flags, enabled, &text, &handled);
      if (handled && given) return *given;
    }
    return QStyle::itemTextRect(fm, r, flags, enabled, text);
  }

  //  QRect QStyle::itemPixmapRect(const QRect &r, int flags, const QPixmap
  //      &pixmap) const
  QRect itemPixmapRect(
      const QRect &r,
      int flags,
      const QPixmap &pixmap) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQPixmapStyleCall19 call = reinterpret_cast<CuteQPixmapStyleCall19>(taken[19]);
      const QRect * given = call(this, &r, flags, &pixmap, &handled);
      if (handled && given) return *given;
    }
    return QStyle::itemPixmapRect(r, flags, pixmap);
  }

  //  void QStyle::drawItemText(QPainter *painter, const QRect &rect, int
  //      flags, const QPalette &pal, bool enabled, const QString &text,
  //      QPalette::ColorRole textRole) const
  void drawItemText(
      QPainter *painter,
      const QRect &rect,
      int flags,
      const QPalette &pal,
      bool enabled,
      const QString &text,
      QPalette::ColorRole textRole) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQPixmapStyleCall20 call = reinterpret_cast<CuteQPixmapStyleCall20>(taken[20]);
      call(this, painter, &rect, flags, &pal, enabled, &text, static_cast<int>(textRole), &handled);
      if (handled) return;
    }
    QStyle::drawItemText(painter, rect, flags, pal, enabled, text, textRole);
  }

  //  void QStyle::drawItemPixmap(QPainter *painter, const QRect &rect, int
  //      alignment, const QPixmap &pixmap) const
  void drawItemPixmap(
      QPainter *painter,
      const QRect &rect,
      int alignment,
      const QPixmap &pixmap) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQPixmapStyleCall21 call = reinterpret_cast<CuteQPixmapStyleCall21>(taken[21]);
      call(this, painter, &rect, alignment, &pixmap, &handled);
      if (handled) return;
    }
    QStyle::drawItemPixmap(painter, rect, alignment, pixmap);
  }

  //  QPalette QStyle::standardPalette() const
  QPalette standardPalette() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQPixmapStyleCall22 call = reinterpret_cast<CuteQPixmapStyleCall22>(taken[22]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QStyle::standardPalette();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQPixmapStyleCall23 call = reinterpret_cast<CuteQPixmapStyleCall23>(taken[23]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQPixmapStyleCall24 call = reinterpret_cast<CuteQPixmapStyleCall24>(taken[24]);
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
      CuteQPixmapStyleCall25 call = reinterpret_cast<CuteQPixmapStyleCall25>(taken[25]);
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
      CuteQPixmapStyleCall26 call = reinterpret_cast<CuteQPixmapStyleCall26>(taken[26]);
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
      CuteQPixmapStyleCall27 call = reinterpret_cast<CuteQPixmapStyleCall27>(taken[27]);
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
      CuteQPixmapStyleCall28 call = reinterpret_cast<CuteQPixmapStyleCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPixmapStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QPixmapStyle10metaObjectEv(
    const QPixmapStyle *self) {
  return self->metaObject();
}

//  QString QPixmapStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QPixmapStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPixmapStyle::tr(s, c, n));
}

//  QPixmapStyle::QPixmapStyle()
extern "C" Q_DECL_EXPORT
QPixmapStyle *ritual_ZN12QPixmapStyleC1Ev() {
  return new CuteQPixmapStyle();
}

//  QPixmapStyle::~QPixmapStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapStyleD1Ev(QPixmapStyle *self) {
  delete self;
}

//  void QPixmapStyle::polish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapStyle6polishEP12QApplication(
    QPixmapStyle *self,
    QApplication *application) {
  self->polish(application);
}

//  void QPixmapStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapStyle6polishEP7QWidget(
    QPixmapStyle *self,
    QWidget *widget) {
  self->polish(widget);
}

//  void QPixmapStyle::unpolish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapStyle8unpolishEP12QApplication(
    QPixmapStyle *self,
    QApplication *application) {
  self->unpolish(application);
}

//  void QPixmapStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapStyle8unpolishEP7QWidget(
    QPixmapStyle *self,
    QWidget *widget) {
  self->unpolish(widget);
}

//  void QPixmapStyle::drawPrimitive(PrimitiveElement element, const
//      QStyleOption *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    QStyle::PrimitiveElement element,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawPrimitive(element, option, painter, widget);
}

//  void QPixmapStyle::drawControl(ControlElement element, const QStyleOption
//      *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawControl(element, option, painter, widget);
}

//  void QPixmapStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *option, QPainter *painter, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawComplexControl(cc, option, painter, widget);
}

//  QSize QPixmapStyle::sizeFromContents(ContentsType type, const
//      QStyleOption *option, const QSize &contentsSize, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QPixmapStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QPixmapStyle *self,
    QStyle::ContentsType type,
    const QStyleOption *option,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->sizeFromContents(
          type,
          option,
          *contentsSize,
          widget));
}

//  QRect QPixmapStyle::subElementRect(SubElement element, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QPixmapStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QPixmapStyle *self,
    QStyle::SubElement element,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QRect(self->subElementRect(element, option, widget));
}

//  QRect QPixmapStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *option, SubControl sc, const QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QPixmapStyle14subControlRectEN6QStyle14ComplexControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget(
    const QPixmapStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *option,
    QStyle::SubControl sc,
    const QWidget *widget) {
  return new QRect(self->subControlRect(cc, option, sc, widget));
}

//  int QPixmapStyle::pixelMetric(PixelMetric metric, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPixmapStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QPixmapStyle *self,
    QStyle::PixelMetric metric,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->pixelMetric(metric, option, widget);
}

//  int QPixmapStyle::styleHint(StyleHint hint, const QStyleOption *option,
//      const QWidget *widget, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPixmapStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QPixmapStyle *self,
    QStyle::StyleHint hint,
    const QStyleOption *option,
    const QWidget *widget,
    QStyleHintReturn *returnData) {
  return self->styleHint(hint, option, widget, returnData);
}

//  SubControl QPixmapStyle::hitTestComplexControl(ComplexControl control,
//      const QStyleOptionComplex *option, const QPoint &pos, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_ZNK12QPixmapStyle21hitTestComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QPixmapStyle *self,
    QStyle::ComplexControl control,
    const QStyleOptionComplex *option,
    const QPoint *pos,
    const QWidget *widget) {
  return self->hitTestComplexControl(control, option, *pos, widget);
}

//  bool QPixmapStyle::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPixmapStyle11eventFilterEP7QObjectP6QEvent(
    QPixmapStyle *self,
    QObject *watched,
    QEvent *event) {
  return self->eventFilter(watched, event);
}

//  void QPixmapStyle::addDescriptor(ControlDescriptor control, const QString
//      &fileName, QMargins margins, QTileRules tileRules)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapStyle13addDescriptorENS_17ControlDescriptorERK7QString8QMargins10QTileRules(
    QPixmapStyle *self,
    QPixmapStyle::ControlDescriptor control,
    const QString *fileName,
    const QMargins *margins,
    const QTileRules *tileRules) {
  self->addDescriptor(control, *fileName, *margins, *tileRules);
}

//  void QPixmapStyle::copyDescriptor(ControlDescriptor source,
//      ControlDescriptor dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapStyle14copyDescriptorENS_17ControlDescriptorES0_(
    QPixmapStyle *self,
    QPixmapStyle::ControlDescriptor source,
    QPixmapStyle::ControlDescriptor dest) {
  self->copyDescriptor(source, dest);
}

//  void QPixmapStyle::drawCachedPixmap(ControlDescriptor control, const
//      QRect &rect, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle16drawCachedPixmapENS_17ControlDescriptorERK5QRectP8QPainter(
    const QPixmapStyle *self,
    QPixmapStyle::ControlDescriptor control,
    const QRect *rect,
    QPainter *p) {
  self->drawCachedPixmap(control, *rect, p);
}

//  void QPixmapStyle::addPixmap(ControlPixmap control, const QString
//      &fileName, QMargins margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapStyle9addPixmapENS_13ControlPixmapERK7QString8QMargins(
    QPixmapStyle *self,
    QPixmapStyle::ControlPixmap control,
    const QString *fileName,
    const QMargins *margins) {
  self->addPixmap(control, *fileName, *margins);
}

//  void QPixmapStyle::copyPixmap(ControlPixmap source, ControlPixmap dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPixmapStyle10copyPixmapENS_13ControlPixmapES0_(
    QPixmapStyle *self,
    QPixmapStyle::ControlPixmap source,
    QPixmapStyle::ControlPixmap dest) {
  self->copyPixmap(source, dest);
}

//  void QPixmapStyle::drawPushButton(const QStyleOption *option, QPainter
//      *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle14drawPushButtonEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawPushButton(option, painter, widget);
}

//  void QPixmapStyle::drawLineEdit(const QStyleOption *option, QPainter
//      *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle12drawLineEditEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawLineEdit(option, painter, widget);
}

//  void QPixmapStyle::drawTextEdit(const QStyleOption *option, QPainter
//      *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle12drawTextEditEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawTextEdit(option, painter, widget);
}

//  void QPixmapStyle::drawCheckBox(const QStyleOption *option, QPainter
//      *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle12drawCheckBoxEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawCheckBox(option, painter, widget);
}

//  void QPixmapStyle::drawRadioButton(const QStyleOption *option, QPainter
//      *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle15drawRadioButtonEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawRadioButton(option, painter, widget);
}

//  void QPixmapStyle::drawPanelItemViewItem(const QStyleOption *option,
//      QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle21drawPanelItemViewItemEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawPanelItemViewItem(option, painter, widget);
}

//  void QPixmapStyle::drawProgressBarBackground(const QStyleOption *option,
//      QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle25drawProgressBarBackgroundEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawProgressBarBackground(option, painter, widget);
}

//  void QPixmapStyle::drawProgressBarLabel(const QStyleOption *option,
//      QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle20drawProgressBarLabelEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawProgressBarLabel(option, painter, widget);
}

//  void QPixmapStyle::drawProgressBarFill(const QStyleOption *option,
//      QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle19drawProgressBarFillEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawProgressBarFill(option, painter, widget);
}

//  void QPixmapStyle::drawSlider(const QStyleOptionComplex *option, QPainter
//      *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle10drawSliderEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOptionComplex *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawSlider(option, painter, widget);
}

//  void QPixmapStyle::drawComboBox(const QStyleOptionComplex *option,
//      QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle12drawComboBoxEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOptionComplex *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawComboBox(option, painter, widget);
}

//  void QPixmapStyle::drawScrollBar(const QStyleOptionComplex *option,
//      QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPixmapStyle13drawScrollBarEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    const QStyleOptionComplex *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawScrollBar(option, painter, widget);
}

//  QSize QPixmapStyle::pushButtonSizeFromContents(const QStyleOption
//      *option, const QSize &contentsSize, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QPixmapStyle26pushButtonSizeFromContentsEPK12QStyleOptionRK5QSizePK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->pushButtonSizeFromContents(
          option,
          *contentsSize,
          widget));
}

//  QSize QPixmapStyle::lineEditSizeFromContents(const QStyleOption *option,
//      const QSize &contentsSize, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QPixmapStyle24lineEditSizeFromContentsEPK12QStyleOptionRK5QSizePK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->lineEditSizeFromContents(
          option,
          *contentsSize,
          widget));
}

//  QSize QPixmapStyle::progressBarSizeFromContents(const QStyleOption
//      *option, const QSize &contentsSize, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QPixmapStyle27progressBarSizeFromContentsEPK12QStyleOptionRK5QSizePK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->progressBarSizeFromContents(
          option,
          *contentsSize,
          widget));
}

//  QSize QPixmapStyle::sliderSizeFromContents(const QStyleOption *option,
//      const QSize &contentsSize, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QPixmapStyle22sliderSizeFromContentsEPK12QStyleOptionRK5QSizePK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->sliderSizeFromContents(
          option,
          *contentsSize,
          widget));
}

//  QSize QPixmapStyle::comboBoxSizeFromContents(const QStyleOption *option,
//      const QSize &contentsSize, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QPixmapStyle24comboBoxSizeFromContentsEPK12QStyleOptionRK5QSizePK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->comboBoxSizeFromContents(
          option,
          *contentsSize,
          widget));
}

//  QSize QPixmapStyle::itemViewSizeFromContents(const QStyleOption *option,
//      const QSize &contentsSize, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QPixmapStyle24itemViewSizeFromContentsEPK12QStyleOptionRK5QSizePK7QWidget(
    const QPixmapStyle *self,
    const QStyleOption *option,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->itemViewSizeFromContents(
          option,
          *contentsSize,
          widget));
}

//  QPixmapStylePrivate *QPixmapStyle::d_func()
extern "C" Q_DECL_EXPORT
QPixmapStylePrivate *ritual_ZN12QPixmapStyle6d_funcEv(QPixmapStyle *self) {
  return self->d_func();
}

//  const QPixmapStylePrivate *QPixmapStyle::d_func() const
extern "C" Q_DECL_EXPORT
const QPixmapStylePrivate *ritual_ZNK12QPixmapStyle6d_funcEv(
    const QPixmapStyle *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPixmapStyle, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPixmapStyle(
    QPixmapStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPixmapStyle *>(self)->take(key, call);
}

//  void QPixmapStyle::polish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPixmapStyle6polishEP12QApplication(
    QPixmapStyle *self,
    QApplication *application) {
  self->QPixmapStyle::polish(application);
}

//  void QPixmapStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPixmapStyle6polishEP7QWidget(
    QPixmapStyle *self,
    QWidget *widget) {
  self->QPixmapStyle::polish(widget);
}

//  void QPixmapStyle::unpolish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPixmapStyle8unpolishEP12QApplication(
    QPixmapStyle *self,
    QApplication *application) {
  self->QPixmapStyle::unpolish(application);
}

//  void QPixmapStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPixmapStyle8unpolishEP7QWidget(
    QPixmapStyle *self,
    QWidget *widget) {
  self->QPixmapStyle::unpolish(widget);
}

//  void QPixmapStyle::drawPrimitive(PrimitiveElement element, const
//      QStyleOption *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QPixmapStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    QStyle::PrimitiveElement element,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->QPixmapStyle::drawPrimitive(element, option, painter, widget);
}

//  void QPixmapStyle::drawControl(ControlElement element, const QStyleOption
//      *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QPixmapStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->QPixmapStyle::drawControl(element, option, painter, widget);
}

//  void QPixmapStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *option, QPainter *painter, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QPixmapStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QPixmapStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *option,
    QPainter *painter,
    const QWidget *widget) {
  self->QPixmapStyle::drawComplexControl(cc, option, painter, widget);
}

//  QSize QPixmapStyle::sizeFromContents(ContentsType type, const
//      QStyleOption *option, const QSize &contentsSize, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QPixmapStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QPixmapStyle *self,
    QStyle::ContentsType type,
    const QStyleOption *option,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->QPixmapStyle::sizeFromContents(
          type,
          option,
          *contentsSize,
          widget));
}

//  QRect QPixmapStyle::subElementRect(SubElement element, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK12QPixmapStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QPixmapStyle *self,
    QStyle::SubElement element,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QRect(
      self->QPixmapStyle::subElementRect(
          element,
          option,
          widget));
}

//  QRect QPixmapStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *option, SubControl sc, const QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK12QPixmapStyle14subControlRectEN6QStyle14ComplexControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget(
    const QPixmapStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *option,
    QStyle::SubControl sc,
    const QWidget *widget) {
  return new QRect(
      self->QPixmapStyle::subControlRect(
          cc,
          option,
          sc,
          widget));
}

//  int QPixmapStyle::pixelMetric(PixelMetric metric, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QPixmapStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QPixmapStyle *self,
    QStyle::PixelMetric metric,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->QPixmapStyle::pixelMetric(metric, option, widget);
}

//  int QPixmapStyle::styleHint(StyleHint hint, const QStyleOption *option,
//      const QWidget *widget, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QPixmapStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QPixmapStyle *self,
    QStyle::StyleHint hint,
    const QStyleOption *option,
    const QWidget *widget,
    QStyleHintReturn *returnData) {
  return self->QPixmapStyle::styleHint(hint, option, widget, returnData);
}

//  SubControl QPixmapStyle::hitTestComplexControl(ComplexControl control,
//      const QStyleOptionComplex *option, const QPoint &pos, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_own_ZNK12QPixmapStyle21hitTestComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QPixmapStyle *self,
    QStyle::ComplexControl control,
    const QStyleOptionComplex *option,
    const QPoint *pos,
    const QWidget *widget) {
  return self->QPixmapStyle::hitTestComplexControl(
      control,
      option,
      *pos,
      widget);
}

//  bool QPixmapStyle::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QPixmapStyle11eventFilterEP7QObjectP6QEvent(
    QPixmapStyle *self,
    QObject *watched,
    QEvent *event) {
  return self->QPixmapStyle::eventFilter(watched, event);
}
