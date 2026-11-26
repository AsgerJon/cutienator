//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyle.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyle.h>
#include <QtCore/qstring.h>
#include <QtGui/qfontmetrics.h>
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qpalette.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qicon.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QStyle that Python can take functions over in. Every QStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQStyleCall0)(const void *, QWidget *, int *);
typedef void (*CuteQStyleCall1)(const void *, QWidget *, int *);
typedef void (*CuteQStyleCall2)(const void *, QApplication *, int *);
typedef void (*CuteQStyleCall3)(const void *, QApplication *, int *);
typedef const QRect * (*CuteQStyleCall4)(const void *, const QFontMetrics *, const QRect *, int, bool, const QString *, int *);
typedef const QRect * (*CuteQStyleCall5)(const void *, const QRect *, int, const QPixmap *, int *);
typedef void (*CuteQStyleCall6)(const void *, QPainter *, const QRect *, int, const QPalette *, bool, const QString *, int, int *);
typedef void (*CuteQStyleCall7)(const void *, QPainter *, const QRect *, int, const QPixmap *, int *);
typedef const QPalette * (*CuteQStyleCall8)(const void *, int *);
typedef void (*CuteQStyleCall9)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef void (*CuteQStyleCall10)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef const QRect * (*CuteQStyleCall11)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef void (*CuteQStyleCall12)(const void *, int, const QStyleOptionComplex *, QPainter *, const QWidget *, int *);
typedef int (*CuteQStyleCall13)(const void *, int, const QStyleOptionComplex *, const QPoint *, const QWidget *, int *);
typedef const QRect * (*CuteQStyleCall14)(const void *, int, const QStyleOptionComplex *, int, const QWidget *, int *);
typedef int (*CuteQStyleCall15)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QSize * (*CuteQStyleCall16)(const void *, int, const QStyleOption *, const QSize *, const QWidget *, int *);
typedef int (*CuteQStyleCall17)(const void *, int, const QStyleOption *, const QWidget *, QStyleHintReturn *, int *);
typedef const QPixmap * (*CuteQStyleCall18)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QIcon * (*CuteQStyleCall19)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QPixmap * (*CuteQStyleCall20)(const void *, int, const QPixmap *, const QStyleOption *, int *);
typedef int (*CuteQStyleCall21)(const void *, int, int, int, const QStyleOption *, const QWidget *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStyleCall22)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStyleCall23)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleCall24)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleCall25)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQStyle : public QStyle {
public:
  using QStyle::QStyle;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QStyle6polishEP7QWidget")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle6polishEP12QApplication")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP12QApplication")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle15standardPaletteEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle13drawPrimitiveENS_16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle11drawControlENS_14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOptionPK7QWidget")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOptionComplexNS_10SubControlEPK7QWidget")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK7QWidget")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle9styleHintENS_9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget")) {
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

  //  void QStyle::polish(QWidget *widget)
  void polish(QWidget *widget) override {
    if (taken[0]) {
      int handled = 0;
      CuteQStyleCall0 call = reinterpret_cast<CuteQStyleCall0>(taken[0]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QStyle::polish(widget);
  }

  //  void QStyle::unpolish(QWidget *widget)
  void unpolish(QWidget *widget) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStyleCall1 call = reinterpret_cast<CuteQStyleCall1>(taken[1]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QStyle::unpolish(widget);
  }

  //  void QStyle::polish(QApplication *application)
  void polish(QApplication *application) override {
    if (taken[2]) {
      int handled = 0;
      CuteQStyleCall2 call = reinterpret_cast<CuteQStyleCall2>(taken[2]);
      call(this, application, &handled);
      if (handled) return;
    }
    QStyle::polish(application);
  }

  //  void QStyle::unpolish(QApplication *application)
  void unpolish(QApplication *application) override {
    if (taken[3]) {
      int handled = 0;
      CuteQStyleCall3 call = reinterpret_cast<CuteQStyleCall3>(taken[3]);
      call(this, application, &handled);
      if (handled) return;
    }
    QStyle::unpolish(application);
  }

  //  QRect QStyle::itemTextRect(const QFontMetrics &fm, const QRect &r,
  //      int flags, bool enabled, const QString &text) const
  QRect itemTextRect(
      const QFontMetrics &fm,
      const QRect &r,
      int flags,
      bool enabled,
      const QString &text) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQStyleCall4 call = reinterpret_cast<CuteQStyleCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQStyleCall5 call = reinterpret_cast<CuteQStyleCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQStyleCall6 call = reinterpret_cast<CuteQStyleCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQStyleCall7 call = reinterpret_cast<CuteQStyleCall7>(taken[7]);
      call(this, painter, &rect, alignment, &pixmap, &handled);
      if (handled) return;
    }
    QStyle::drawItemPixmap(painter, rect, alignment, pixmap);
  }

  //  QPalette QStyle::standardPalette() const
  QPalette standardPalette() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQStyleCall8 call = reinterpret_cast<CuteQStyleCall8>(taken[8]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QStyle::standardPalette();
  }

  //  void QStyle::drawPrimitive(PrimitiveElement pe, const QStyleOption
  //      *opt, QPainter *p, const QWidget *w) const
  void drawPrimitive(
      QStyle::PrimitiveElement pe,
      const QStyleOption *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQStyleCall9 call = reinterpret_cast<CuteQStyleCall9>(taken[9]);
      call(this, static_cast<int>(pe), opt, p, w, &handled);
      if (handled) return;
    }
  }

  //  void QStyle::drawControl(ControlElement element, const QStyleOption
  //      *opt, QPainter *p, const QWidget *w) const
  void drawControl(
      QStyle::ControlElement element,
      const QStyleOption *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQStyleCall10 call = reinterpret_cast<CuteQStyleCall10>(taken[10]);
      call(this, static_cast<int>(element), opt, p, w, &handled);
      if (handled) return;
    }
  }

  //  QRect QStyle::subElementRect(SubElement subElement, const
  //      QStyleOption *option, const QWidget *widget) const
  QRect subElementRect(
      QStyle::SubElement subElement,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQStyleCall11 call = reinterpret_cast<CuteQStyleCall11>(taken[11]);
      const QRect * given = call(this, static_cast<int>(subElement), option, widget, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QStyle::drawComplexControl(ComplexControl cc, const
  //      QStyleOptionComplex *opt, QPainter *p, const QWidget *widget)
  //      const
  void drawComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QPainter *p,
      const QWidget *widget) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQStyleCall12 call = reinterpret_cast<CuteQStyleCall12>(taken[12]);
      call(this, static_cast<int>(cc), opt, p, widget, &handled);
      if (handled) return;
    }
  }

  //  SubControl QStyle::hitTestComplexControl(ComplexControl cc, const
  //      QStyleOptionComplex *opt, const QPoint &pt, const QWidget
  //      *widget) const
  QStyle::SubControl hitTestComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      const QPoint &pt,
      const QWidget *widget) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQStyleCall13 call = reinterpret_cast<CuteQStyleCall13>(taken[13]);
      int given = call(this, static_cast<int>(cc), opt, &pt, widget, &handled);
      if (handled) return static_cast<QStyle::SubControl>(given);
    }
    return {};
  }

  //  QRect QStyle::subControlRect(ComplexControl cc, const
  //      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget)
  //      const
  QRect subControlRect(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QStyle::SubControl sc,
      const QWidget *widget) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQStyleCall14 call = reinterpret_cast<CuteQStyleCall14>(taken[14]);
      const QRect * given = call(this, static_cast<int>(cc), opt, static_cast<int>(sc), widget, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QStyle::pixelMetric(PixelMetric metric, const QStyleOption
  //      *option, const QWidget *widget) const
  int pixelMetric(
      QStyle::PixelMetric metric,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQStyleCall15 call = reinterpret_cast<CuteQStyleCall15>(taken[15]);
      int given = call(this, static_cast<int>(metric), option, widget, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QSize QStyle::sizeFromContents(ContentsType ct, const QStyleOption
  //      *opt, const QSize &contentsSize, const QWidget *w) const
  QSize sizeFromContents(
      QStyle::ContentsType ct,
      const QStyleOption *opt,
      const QSize &contentsSize,
      const QWidget *w) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQStyleCall16 call = reinterpret_cast<CuteQStyleCall16>(taken[16]);
      const QSize * given = call(this, static_cast<int>(ct), opt, &contentsSize, w, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QStyle::styleHint(StyleHint stylehint, const QStyleOption *opt,
  //      const QWidget *widget, QStyleHintReturn *returnData) const
  int styleHint(
      QStyle::StyleHint stylehint,
      const QStyleOption *opt,
      const QWidget *widget,
      QStyleHintReturn *returnData) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQStyleCall17 call = reinterpret_cast<CuteQStyleCall17>(taken[17]);
      int given = call(this, static_cast<int>(stylehint), opt, widget, returnData, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QPixmap QStyle::standardPixmap(StandardPixmap standardPixmap, const
  //      QStyleOption *opt, const QWidget *widget) const
  QPixmap standardPixmap(
      QStyle::StandardPixmap standardPixmap,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQStyleCall18 call = reinterpret_cast<CuteQStyleCall18>(taken[18]);
      const QPixmap * given = call(this, static_cast<int>(standardPixmap), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QIcon QStyle::standardIcon(StandardPixmap standardIcon, const
  //      QStyleOption *option, const QWidget *widget) const
  QIcon standardIcon(
      QStyle::StandardPixmap standardIcon,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQStyleCall19 call = reinterpret_cast<CuteQStyleCall19>(taken[19]);
      const QIcon * given = call(this, static_cast<int>(standardIcon), option, widget, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QPixmap QStyle::generatedIconPixmap(QIcon::Mode iconMode, const
  //      QPixmap &pixmap, const QStyleOption *opt) const
  QPixmap generatedIconPixmap(
      QIcon::Mode iconMode,
      const QPixmap &pixmap,
      const QStyleOption *opt) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQStyleCall20 call = reinterpret_cast<CuteQStyleCall20>(taken[20]);
      const QPixmap * given = call(this, static_cast<int>(iconMode), &pixmap, opt, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QStyle::layoutSpacing(QSizePolicy::ControlType control1,
  //      QSizePolicy::ControlType control2, Qt::Orientation orientation,
  //      const QStyleOption *option, const QWidget *widget) const
  int layoutSpacing(
      QSizePolicy::ControlType control1,
      QSizePolicy::ControlType control2,
      Qt::Orientation orientation,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQStyleCall21 call = reinterpret_cast<CuteQStyleCall21>(taken[21]);
      int given = call(this, static_cast<int>(control1), static_cast<int>(control2), static_cast<int>(orientation), option, widget, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQStyleCall22 call = reinterpret_cast<CuteQStyleCall22>(taken[22]);
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
      CuteQStyleCall23 call = reinterpret_cast<CuteQStyleCall23>(taken[23]);
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
      CuteQStyleCall24 call = reinterpret_cast<CuteQStyleCall24>(taken[24]);
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
      CuteQStyleCall25 call = reinterpret_cast<CuteQStyleCall25>(taken[25]);
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
      CuteQStyleCall26 call = reinterpret_cast<CuteQStyleCall26>(taken[26]);
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
      CuteQStyleCall27 call = reinterpret_cast<CuteQStyleCall27>(taken[27]);
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
      CuteQStyleCall28 call = reinterpret_cast<CuteQStyleCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QStyle10metaObjectEv(const QStyle *self) {
  return self->metaObject();
}

//  void *QStyle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN6QStyle11qt_metacastEPKc(QStyle *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QStyle::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QStyle11qt_metacallEN11QMetaObject4CallEiPPv(
    QStyle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QStyle2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QStyle::tr(s, c, n));
}

//  QStylePrivate *QStyle::d_func()
extern "C" Q_DECL_EXPORT
QStylePrivate *ritual_ZN6QStyle6d_funcEv(QStyle *self) {
  return self->d_func();
}

//  const QStylePrivate *QStyle::d_func() const
extern "C" Q_DECL_EXPORT
const QStylePrivate *ritual_ZNK6QStyle6d_funcEv(const QStyle *self) {
  return self->d_func();
}

//  QStyle::QStyle(QStylePrivate &dd)
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZN6QStyleC1ER13QStylePrivate(QStylePrivate *dd) {
  return new CuteQStyle(*dd);
}

//  QStyle::QStyle()
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZN6QStyleC1Ev() {
  return new CuteQStyle();
}

//  QStyle::~QStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QStyleD1Ev(QStyle *self) {
  delete self;
}

//  QString QStyle::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QStyle4nameEv(const QStyle *self) {
  return new QString(self->name());
}

//  void QStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QStyle6polishEP7QWidget(QStyle *self, QWidget *widget) {
  self->polish(widget);
}

//  void QStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QStyle8unpolishEP7QWidget(QStyle *self, QWidget *widget) {
  self->unpolish(widget);
}

//  void QStyle::polish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QStyle6polishEP12QApplication(
    QStyle *self,
    QApplication *application) {
  self->polish(application);
}

//  void QStyle::unpolish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QStyle8unpolishEP12QApplication(
    QStyle *self,
    QApplication *application) {
  self->unpolish(application);
}

//  void QStyle::polish(QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QStyle6polishER8QPalette(QStyle *self, QPalette *palette) {
  self->polish(*palette);
}

//  QRect QStyle::itemTextRect(const QFontMetrics &fm, const QRect &r, int
//      flags, bool enabled, const QString &text) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString(
    const QStyle *self,
    const QFontMetrics *fm,
    const QRect *r,
    int flags,
    bool enabled,
    const QString *text) {
  return new QRect(self->itemTextRect(*fm, *r, flags, enabled, *text));
}

//  QRect QStyle::itemPixmapRect(const QRect &r, int flags, const QPixmap
//      &pixmap) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap(
    const QStyle *self,
    const QRect *r,
    int flags,
    const QPixmap *pixmap) {
  return new QRect(self->itemPixmapRect(*r, flags, *pixmap));
}

//  void QStyle::drawItemText(QPainter *painter, const QRect &rect, int
//      flags, const QPalette &pal, bool enabled, const QString &text,
//      QPalette::ColorRole textRole) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE(
    const QStyle *self,
    QPainter *painter,
    const QRect *rect,
    int flags,
    const QPalette *pal,
    bool enabled,
    const QString *text,
    QPalette::ColorRole textRole) {
  self->drawItemText(painter, *rect, flags, *pal, enabled, *text, textRole);
}

//  void QStyle::drawItemPixmap(QPainter *painter, const QRect &rect, int
//      alignment, const QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap(
    const QStyle *self,
    QPainter *painter,
    const QRect *rect,
    int alignment,
    const QPixmap *pixmap) {
  self->drawItemPixmap(painter, *rect, alignment, *pixmap);
}

//  QPalette QStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK6QStyle15standardPaletteEv(const QStyle *self) {
  return new QPalette(self->standardPalette());
}

//  void QStyle::drawPrimitive(PrimitiveElement pe, const QStyleOption *opt,
//      QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QStyle13drawPrimitiveENS_16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QStyle *self,
    QStyle::PrimitiveElement pe,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawPrimitive(pe, opt, p, w);
}

//  void QStyle::drawControl(ControlElement element, const QStyleOption *opt,
//      QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QStyle11drawControlENS_14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawControl(element, opt, p, w);
}

//  QRect QStyle::subElementRect(SubElement subElement, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOptionPK7QWidget(
    const QStyle *self,
    QStyle::SubElement subElement,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QRect(self->subElementRect(subElement, option, widget));
}

//  void QStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, QPainter *p, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QPainter *p,
    const QWidget *widget) {
  self->drawComplexControl(cc, opt, p, widget);
}

//  SubControl QStyle::hitTestComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, const QPoint &pt, const QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    const QPoint *pt,
    const QWidget *widget) {
  return self->hitTestComplexControl(cc, opt, *pt, widget);
}

//  QRect QStyle::subControlRect(ComplexControl cc, const QStyleOptionComplex
//      *opt, SubControl sc, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOptionComplexNS_10SubControlEPK7QWidget(
    const QStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QStyle::SubControl sc,
    const QWidget *widget) {
  return new QRect(self->subControlRect(cc, opt, sc, widget));
}

//  int QStyle::pixelMetric(PixelMetric metric, const QStyleOption *option,
//      const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QStyle *self,
    QStyle::PixelMetric metric,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->pixelMetric(metric, option, widget);
}

//  QSize QStyle::sizeFromContents(ContentsType ct, const QStyleOption *opt,
//      const QSize &contentsSize, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QStyle *self,
    QStyle::ContentsType ct,
    const QStyleOption *opt,
    const QSize *contentsSize,
    const QWidget *w) {
  return new QSize(self->sizeFromContents(ct, opt, *contentsSize, w));
}

//  int QStyle::styleHint(StyleHint stylehint, const QStyleOption *opt, const
//      QWidget *widget, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QStyle9styleHintENS_9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QStyle *self,
    QStyle::StyleHint stylehint,
    const QStyleOption *opt,
    const QWidget *widget,
    QStyleHintReturn *returnData) {
  return self->styleHint(stylehint, opt, widget, returnData);
}

//  QPixmap QStyle::standardPixmap(StandardPixmap standardPixmap, const
//      QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QStyle *self,
    QStyle::StandardPixmap standardPixmap,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QPixmap(self->standardPixmap(standardPixmap, opt, widget));
}

//  QIcon QStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QStyle *self,
    QStyle::StandardPixmap standardIcon,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QIcon(self->standardIcon(standardIcon, option, widget));
}

//  QPixmap QStyle::generatedIconPixmap(QIcon::Mode iconMode, const QPixmap
//      &pixmap, const QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK6QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption(
    const QStyle *self,
    QIcon::Mode iconMode,
    const QPixmap *pixmap,
    const QStyleOption *opt) {
  return new QPixmap(self->generatedIconPixmap(iconMode, *pixmap, opt));
}

//  QRect QStyle::visualRect(Qt::LayoutDirection direction, const QRect
//      &boundingRect, const QRect &logicalRect)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN6QStyle10visualRectEN2Qt15LayoutDirectionERK5QRectS4_(
    Qt::LayoutDirection direction,
    const QRect *boundingRect,
    const QRect *logicalRect) {
  return new QRect(
      QStyle::visualRect(
          direction,
          *boundingRect,
          *logicalRect));
}

//  QPoint QStyle::visualPos(Qt::LayoutDirection direction, const QRect
//      &boundingRect, const QPoint &logicalPos)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN6QStyle9visualPosEN2Qt15LayoutDirectionERK5QRectRK6QPoint(
    Qt::LayoutDirection direction,
    const QRect *boundingRect,
    const QPoint *logicalPos) {
  return new QPoint(
      QStyle::visualPos(
          direction,
          *boundingRect,
          *logicalPos));
}

//  int QStyle::sliderPositionFromValue(int min, int max, int val, int space,
//      bool upsideDown)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QStyle23sliderPositionFromValueEiiiib(
    int min,
    int max,
    int val,
    int space,
    bool upsideDown) {
  return QStyle::sliderPositionFromValue(min, max, val, space, upsideDown);
}

//  int QStyle::sliderValueFromPosition(int min, int max, int pos, int space,
//      bool upsideDown)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QStyle23sliderValueFromPositionEiiiib(
    int min,
    int max,
    int pos,
    int space,
    bool upsideDown) {
  return QStyle::sliderValueFromPosition(min, max, pos, space, upsideDown);
}

//  Qt::Alignment QStyle::visualAlignment(Qt::LayoutDirection direction,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QStyle15visualAlignmentEN2Qt15LayoutDirectionE6QFlagsINS0_13AlignmentFlagEE(
    Qt::LayoutDirection direction,
    int alignment) {
  return static_cast<int>(
      QStyle::visualAlignment(
          direction,
          QFlags<Qt::AlignmentFlag>::fromInt(alignment)).toInt());
}

//  QRect QStyle::alignedRect(Qt::LayoutDirection direction, Qt::Alignment
//      alignment, const QSize &size, const QRect &rectangle)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN6QStyle11alignedRectEN2Qt15LayoutDirectionE6QFlagsINS0_13AlignmentFlagEERK5QSizeRK5QRect(
    Qt::LayoutDirection direction,
    int alignment,
    const QSize *size,
    const QRect *rectangle) {
  return new QRect(
      QStyle::alignedRect(
          direction,
          QFlags<Qt::AlignmentFlag>::fromInt(alignment),
          *size,
          *rectangle));
}

//  int QStyle::layoutSpacing(QSizePolicy::ControlType control1,
//      QSizePolicy::ControlType control2, Qt::Orientation orientation, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget(
    const QStyle *self,
    QSizePolicy::ControlType control1,
    QSizePolicy::ControlType control2,
    Qt::Orientation orientation,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->layoutSpacing(
      control1,
      control2,
      orientation,
      option,
      widget);
}

//  int QStyle::combinedLayoutSpacing(QSizePolicy::ControlTypes controls1,
//      QSizePolicy::ControlTypes controls2, Qt::Orientation orientation,
//      QStyleOption *option, QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QStyle21combinedLayoutSpacingE6QFlagsIN11QSizePolicy11ControlTypeEES3_N2Qt11OrientationEP12QStyleOptionP7QWidget(
    const QStyle *self,
    int controls1,
    int controls2,
    Qt::Orientation orientation,
    QStyleOption *option,
    QWidget *widget) {
  return self->combinedLayoutSpacing(
      QFlags<QSizePolicy::ControlType>::fromInt(controls1),
      QFlags<QSizePolicy::ControlType>::fromInt(controls2),
      orientation,
      option,
      widget);
}

//  const QStyle *QStyle::proxy() const
extern "C" Q_DECL_EXPORT
const QStyle *ritual_ZNK6QStyle5proxyEv(const QStyle *self) {
  return self->proxy();
}

//  void QStyle::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QStyle7setNameERK7QString(QStyle *self, const QString *name) {
  self->setName(*name);
}

//  void QStyle::setProxy(QStyle *style)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QStyle8setProxyEPS_(QStyle *self, QStyle *style) {
  self->setProxy(style);
}

//  a Python function taken by a CuteQStyle, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStyle(QStyle *self, const char *key, void *call) {
  return static_cast<CuteQStyle *>(self)->take(key, call);
}

//  void QStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QStyle6polishEP7QWidget(QStyle *self, QWidget *widget) {
  self->QStyle::polish(widget);
}

//  void QStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QStyle8unpolishEP7QWidget(QStyle *self, QWidget *widget) {
  self->QStyle::unpolish(widget);
}

//  void QStyle::polish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QStyle6polishEP12QApplication(
    QStyle *self,
    QApplication *application) {
  self->QStyle::polish(application);
}

//  void QStyle::unpolish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QStyle8unpolishEP12QApplication(
    QStyle *self,
    QApplication *application) {
  self->QStyle::unpolish(application);
}

//  QRect QStyle::itemTextRect(const QFontMetrics &fm, const QRect &r, int
//      flags, bool enabled, const QString &text) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString(
    const QStyle *self,
    const QFontMetrics *fm,
    const QRect *r,
    int flags,
    bool enabled,
    const QString *text) {
  return new QRect(
      self->QStyle::itemTextRect(
          *fm,
          *r,
          flags,
          enabled,
          *text));
}

//  QRect QStyle::itemPixmapRect(const QRect &r, int flags, const QPixmap
//      &pixmap) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap(
    const QStyle *self,
    const QRect *r,
    int flags,
    const QPixmap *pixmap) {
  return new QRect(self->QStyle::itemPixmapRect(*r, flags, *pixmap));
}

//  void QStyle::drawItemText(QPainter *painter, const QRect &rect, int
//      flags, const QPalette &pal, bool enabled, const QString &text,
//      QPalette::ColorRole textRole) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE(
    const QStyle *self,
    QPainter *painter,
    const QRect *rect,
    int flags,
    const QPalette *pal,
    bool enabled,
    const QString *text,
    QPalette::ColorRole textRole) {
  self->QStyle::drawItemText(
      painter,
      *rect,
      flags,
      *pal,
      enabled,
      *text,
      textRole);
}

//  void QStyle::drawItemPixmap(QPainter *painter, const QRect &rect, int
//      alignment, const QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap(
    const QStyle *self,
    QPainter *painter,
    const QRect *rect,
    int alignment,
    const QPixmap *pixmap) {
  self->QStyle::drawItemPixmap(painter, *rect, alignment, *pixmap);
}

//  QPalette QStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK6QStyle15standardPaletteEv(const QStyle *self) {
  return new QPalette(self->QStyle::standardPalette());
}
