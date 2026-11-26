//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/qstylekitstyle.h, Qt 6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/qtlabsstylekitexports.h>
#if 1
#include <QtLabsStyleKit/QtLabsStyleKit>
#include <QtLabsStyleKit/qstylekitstyle.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qpalette.h>
#include <QtGui/qicon.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qfontmetrics.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QStyleKitStyle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQStyleKitStyle : QStyleKitStyle {
  using QStyleKitStyle::eventFilter;
  using QStyleKitStyle::event;
};

//  A QStyleKitStyle that Python can take functions over in. Every QStyleKitStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQStyleKitStyleCall0)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef void (*CuteQStyleKitStyleCall1)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef const QRect * (*CuteQStyleKitStyleCall2)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef void (*CuteQStyleKitStyleCall3)(const void *, int, const QStyleOptionComplex *, QPainter *, const QWidget *, int *);
typedef int (*CuteQStyleKitStyleCall4)(const void *, int, const QStyleOptionComplex *, const QPoint *, const QWidget *, int *);
typedef const QRect * (*CuteQStyleKitStyleCall5)(const void *, int, const QStyleOptionComplex *, int, const QWidget *, int *);
typedef const QSize * (*CuteQStyleKitStyleCall6)(const void *, int, const QStyleOption *, const QSize *, const QWidget *, int *);
typedef int (*CuteQStyleKitStyleCall7)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef int (*CuteQStyleKitStyleCall8)(const void *, int, const QStyleOption *, const QWidget *, QStyleHintReturn *, int *);
typedef const QPalette * (*CuteQStyleKitStyleCall9)(const void *, int *);
typedef void (*CuteQStyleKitStyleCall10)(const void *, QWidget *, int *);
typedef void (*CuteQStyleKitStyleCall11)(const void *, QApplication *, int *);
typedef void (*CuteQStyleKitStyleCall12)(const void *, QWidget *, int *);
typedef void (*CuteQStyleKitStyleCall13)(const void *, QApplication *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStyleKitStyleCall14)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStyleKitStyleCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef const QIcon * (*CuteQStyleKitStyleCall16)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QPixmap * (*CuteQStyleKitStyleCall17)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QPixmap * (*CuteQStyleKitStyleCall18)(const void *, int, const QPixmap *, const QStyleOption *, int *);
typedef int (*CuteQStyleKitStyleCall19)(const void *, int, int, int, const QStyleOption *, const QWidget *, int *);
typedef const QRect * (*CuteQStyleKitStyleCall20)(const void *, const QFontMetrics *, const QRect *, int, bool, const QString *, int *);
typedef const QRect * (*CuteQStyleKitStyleCall21)(const void *, const QRect *, int, const QPixmap *, int *);
typedef void (*CuteQStyleKitStyleCall22)(const void *, QPainter *, const QRect *, int, const QPalette *, bool, const QString *, int, int *);
typedef void (*CuteQStyleKitStyleCall23)(const void *, QPainter *, const QRect *, int, const QPixmap *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleKitStyleCall24)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleKitStyleCall25)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleKitStyleCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleKitStyleCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStyleKitStyleCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQStyleKitStyle : public QStyleKitStyle {
public:
  using QStyleKitStyle::QStyleKitStyle;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QStyle13drawPrimitiveENS_16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle11drawControlENS_14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOptionPK7QWidget")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOptionComplexNS_10SubControlEPK7QWidget")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK7QWidget")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle9styleHintENS_9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle15standardPaletteEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle6polishEP7QWidget")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle6polishEP12QApplication")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP7QWidget")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP12QApplication")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap")) {
      taken[23] = call;
      return true;
    }
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

  //  void QStyleKitStyle::drawPrimitive(PrimitiveElement pe, const
  //      QStyleOption *opt, QPainter *p, const QWidget *w) const
  void drawPrimitive(
      QStyle::PrimitiveElement pe,
      const QStyleOption *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQStyleKitStyleCall0 call = reinterpret_cast<CuteQStyleKitStyleCall0>(taken[0]);
      call(this, static_cast<int>(pe), opt, p, w, &handled);
      if (handled) return;
    }
    QStyleKitStyle::drawPrimitive(pe, opt, p, w);
  }

  //  void QStyleKitStyle::drawControl(ControlElement element, const
  //      QStyleOption *opt, QPainter *p, const QWidget *w) const
  void drawControl(
      QStyle::ControlElement element,
      const QStyleOption *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQStyleKitStyleCall1 call = reinterpret_cast<CuteQStyleKitStyleCall1>(taken[1]);
      call(this, static_cast<int>(element), opt, p, w, &handled);
      if (handled) return;
    }
    QStyleKitStyle::drawControl(element, opt, p, w);
  }

  //  QRect QStyleKitStyle::subElementRect(SubElement r, const QStyleOption
  //      *opt, const QWidget *widget) const
  QRect subElementRect(
      QStyle::SubElement r,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQStyleKitStyleCall2 call = reinterpret_cast<CuteQStyleKitStyleCall2>(taken[2]);
      const QRect * given = call(this, static_cast<int>(r), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QStyleKitStyle::subElementRect(r, opt, widget);
  }

  //  void QStyleKitStyle::drawComplexControl(ComplexControl cc, const
  //      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
  void drawComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQStyleKitStyleCall3 call = reinterpret_cast<CuteQStyleKitStyleCall3>(taken[3]);
      call(this, static_cast<int>(cc), opt, p, w, &handled);
      if (handled) return;
    }
    QStyleKitStyle::drawComplexControl(cc, opt, p, w);
  }

  //  SubControl QStyleKitStyle::hitTestComplexControl(ComplexControl cc,
  //      const QStyleOptionComplex *opt, const QPoint &pt, const QWidget
  //      *w) const
  QStyle::SubControl hitTestComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      const QPoint &pt,
      const QWidget *w) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQStyleKitStyleCall4 call = reinterpret_cast<CuteQStyleKitStyleCall4>(taken[4]);
      int given = call(this, static_cast<int>(cc), opt, &pt, w, &handled);
      if (handled) return static_cast<QStyle::SubControl>(given);
    }
    return QStyleKitStyle::hitTestComplexControl(cc, opt, pt, w);
  }

  //  QRect QStyleKitStyle::subControlRect(ComplexControl cc, const
  //      QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const
  QRect subControlRect(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QStyle::SubControl sc,
      const QWidget *w) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQStyleKitStyleCall5 call = reinterpret_cast<CuteQStyleKitStyleCall5>(taken[5]);
      const QRect * given = call(this, static_cast<int>(cc), opt, static_cast<int>(sc), w, &handled);
      if (handled && given) return *given;
    }
    return QStyleKitStyle::subControlRect(cc, opt, sc, w);
  }

  //  QSize QStyleKitStyle::sizeFromContents(ContentsType ct, const
  //      QStyleOption *opt, const QSize &contentsSize, const QWidget
  //      *widget) const
  QSize sizeFromContents(
      QStyle::ContentsType ct,
      const QStyleOption *opt,
      const QSize &contentsSize,
      const QWidget *widget) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQStyleKitStyleCall6 call = reinterpret_cast<CuteQStyleKitStyleCall6>(taken[6]);
      const QSize * given = call(this, static_cast<int>(ct), opt, &contentsSize, widget, &handled);
      if (handled && given) return *given;
    }
    return QStyleKitStyle::sizeFromContents(ct, opt, contentsSize, widget);
  }

  //  int QStyleKitStyle::pixelMetric(PixelMetric m, const QStyleOption
  //      *opt, const QWidget *widget) const
  int pixelMetric(
      QStyle::PixelMetric m,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQStyleKitStyleCall7 call = reinterpret_cast<CuteQStyleKitStyleCall7>(taken[7]);
      int given = call(this, static_cast<int>(m), opt, widget, &handled);
      if (handled) return given;
    }
    return QStyleKitStyle::pixelMetric(m, opt, widget);
  }

  //  int QStyleKitStyle::styleHint(StyleHint sh, const QStyleOption *opt,
  //      const QWidget *w, QStyleHintReturn *shret) const
  int styleHint(
      QStyle::StyleHint sh,
      const QStyleOption *opt,
      const QWidget *w,
      QStyleHintReturn *shret) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQStyleKitStyleCall8 call = reinterpret_cast<CuteQStyleKitStyleCall8>(taken[8]);
      int given = call(this, static_cast<int>(sh), opt, w, shret, &handled);
      if (handled) return given;
    }
    return QStyleKitStyle::styleHint(sh, opt, w, shret);
  }

  //  QPalette QStyleKitStyle::standardPalette() const
  QPalette standardPalette() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQStyleKitStyleCall9 call = reinterpret_cast<CuteQStyleKitStyleCall9>(taken[9]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QStyleKitStyle::standardPalette();
  }

  //  void QStyleKitStyle::polish(QWidget *widget)
  void polish(QWidget *widget) override {
    if (taken[10]) {
      int handled = 0;
      CuteQStyleKitStyleCall10 call = reinterpret_cast<CuteQStyleKitStyleCall10>(taken[10]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QStyleKitStyle::polish(widget);
  }

  //  void QStyleKitStyle::polish(QApplication *application)
  void polish(QApplication *application) override {
    if (taken[11]) {
      int handled = 0;
      CuteQStyleKitStyleCall11 call = reinterpret_cast<CuteQStyleKitStyleCall11>(taken[11]);
      call(this, application, &handled);
      if (handled) return;
    }
    QStyleKitStyle::polish(application);
  }

  //  void QStyleKitStyle::unpolish(QWidget *widget)
  void unpolish(QWidget *widget) override {
    if (taken[12]) {
      int handled = 0;
      CuteQStyleKitStyleCall12 call = reinterpret_cast<CuteQStyleKitStyleCall12>(taken[12]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QStyleKitStyle::unpolish(widget);
  }

  //  void QStyleKitStyle::unpolish(QApplication *application)
  void unpolish(QApplication *application) override {
    if (taken[13]) {
      int handled = 0;
      CuteQStyleKitStyleCall13 call = reinterpret_cast<CuteQStyleKitStyleCall13>(taken[13]);
      call(this, application, &handled);
      if (handled) return;
    }
    QStyleKitStyle::unpolish(application);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QStyleKitStyle::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQStyleKitStyleCall14 call = reinterpret_cast<CuteQStyleKitStyleCall14>(taken[14]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QStyleKitStyle::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QStyleKitStyle::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQStyleKitStyleCall15 call = reinterpret_cast<CuteQStyleKitStyleCall15>(taken[15]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QStyleKitStyle::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QIcon QCommonStyle::standardIcon(StandardPixmap standardIcon, const
  //      QStyleOption *opt, const QWidget *widget) const
  QIcon standardIcon(
      QStyle::StandardPixmap standardIcon,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQStyleKitStyleCall16 call = reinterpret_cast<CuteQStyleKitStyleCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQStyleKitStyleCall17 call = reinterpret_cast<CuteQStyleKitStyleCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQStyleKitStyleCall18 call = reinterpret_cast<CuteQStyleKitStyleCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQStyleKitStyleCall19 call = reinterpret_cast<CuteQStyleKitStyleCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQStyleKitStyleCall20 call = reinterpret_cast<CuteQStyleKitStyleCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQStyleKitStyleCall21 call = reinterpret_cast<CuteQStyleKitStyleCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQStyleKitStyleCall22 call = reinterpret_cast<CuteQStyleKitStyleCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQStyleKitStyleCall23 call = reinterpret_cast<CuteQStyleKitStyleCall23>(taken[23]);
      call(this, painter, &rect, alignment, &pixmap, &handled);
      if (handled) return;
    }
    QStyle::drawItemPixmap(painter, rect, alignment, pixmap);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQStyleKitStyleCall24 call = reinterpret_cast<CuteQStyleKitStyleCall24>(taken[24]);
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
      CuteQStyleKitStyleCall25 call = reinterpret_cast<CuteQStyleKitStyleCall25>(taken[25]);
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
      CuteQStyleKitStyleCall26 call = reinterpret_cast<CuteQStyleKitStyleCall26>(taken[26]);
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
      CuteQStyleKitStyleCall27 call = reinterpret_cast<CuteQStyleKitStyleCall27>(taken[27]);
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
      CuteQStyleKitStyleCall28 call = reinterpret_cast<CuteQStyleKitStyleCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QStyleKitStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QStyleKitStyle10metaObjectEv(
    const QStyleKitStyle *self) {
  return self->metaObject();
}

//  void *QStyleKitStyle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QStyleKitStyle11qt_metacastEPKc(
    QStyleKitStyle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QStyleKitStyle::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QStyleKitStyle11qt_metacallEN11QMetaObject4CallEiPPv(
    QStyleKitStyle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QStyleKitStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStyleKitStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStyleKitStyle::tr(s, c, n));
}

//  QStyleKitStyle::QStyleKitStyle()
extern "C" Q_DECL_EXPORT
QStyleKitStyle *ritual_ZN14QStyleKitStyleC1Ev() {
  return new CuteQStyleKitStyle();
}

//  QStyleKitStyle::QStyleKitStyle(const QString &filePath)
extern "C" Q_DECL_EXPORT
QStyleKitStyle *ritual_ZN14QStyleKitStyleC1ERK7QString(
    const QString *filePath) {
  return new CuteQStyleKitStyle(*filePath);
}

//  QStyleKitStyle::~QStyleKitStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyleD1Ev(QStyleKitStyle *self) {
  delete self;
}

//  QString QStyleKitStyle::stylePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QStyleKitStyle9stylePathEv(const QStyleKitStyle *self) {
  return new QString(self->stylePath());
}

//  void QStyleKitStyle::setStylePath(const QString &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle12setStylePathERK7QString(
    QStyleKitStyle *self,
    const QString *filePath) {
  self->setStylePath(*filePath);
}

//  QString QStyleKitStyle::themeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QStyleKitStyle9themeNameEv(const QStyleKitStyle *self) {
  return new QString(self->themeName());
}

//  void QStyleKitStyle::setThemeName(const QString &themeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle12setThemeNameERK7QString(
    QStyleKitStyle *self,
    const QString *themeName) {
  self->setThemeName(*themeName);
}

//  QStringList QStyleKitStyle::availableThemeNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK14QStyleKitStyle19availableThemeNamesEv(
    const QStyleKitStyle *self) {
  return new QList<QString>(self->availableThemeNames());
}

//  QStringList QStyleKitStyle::customThemeNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK14QStyleKitStyle16customThemeNamesEv(
    const QStyleKitStyle *self) {
  return new QList<QString>(self->customThemeNames());
}

//  void QStyleKitStyle::drawPrimitive(PrimitiveElement pe, const
//      QStyleOption *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QStyleKitStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::PrimitiveElement pe,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawPrimitive(pe, opt, p, w);
}

//  void QStyleKitStyle::drawControl(ControlElement element, const
//      QStyleOption *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QStyleKitStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawControl(element, opt, p, w);
}

//  QRect QStyleKitStyle::subElementRect(SubElement r, const QStyleOption
//      *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QStyleKitStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::SubElement r,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QRect(self->subElementRect(r, opt, widget));
}

//  void QStyleKitStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QStyleKitStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawComplexControl(cc, opt, p, w);
}

//  SubControl QStyleKitStyle::hitTestComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, const QPoint &pt, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_ZNK14QStyleKitStyle21hitTestComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    const QPoint *pt,
    const QWidget *w) {
  return self->hitTestComplexControl(cc, opt, *pt, w);
}

//  QRect QStyleKitStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QStyleKitStyle14subControlRectEN6QStyle14ComplexControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QStyle::SubControl sc,
    const QWidget *w) {
  return new QRect(self->subControlRect(cc, opt, sc, w));
}

//  QSize QStyleKitStyle::sizeFromContents(ContentsType ct, const
//      QStyleOption *opt, const QSize &contentsSize, const QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QStyleKitStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QStyleKitStyle *self,
    QStyle::ContentsType ct,
    const QStyleOption *opt,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(self->sizeFromContents(ct, opt, *contentsSize, widget));
}

//  int QStyleKitStyle::pixelMetric(PixelMetric m, const QStyleOption *opt,
//      const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStyleKitStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::PixelMetric m,
    const QStyleOption *opt,
    const QWidget *widget) {
  return self->pixelMetric(m, opt, widget);
}

//  int QStyleKitStyle::styleHint(StyleHint sh, const QStyleOption *opt,
//      const QWidget *w, QStyleHintReturn *shret) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStyleKitStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QStyleKitStyle *self,
    QStyle::StyleHint sh,
    const QStyleOption *opt,
    const QWidget *w,
    QStyleHintReturn *shret) {
  return self->styleHint(sh, opt, w, shret);
}

//  QPalette QStyleKitStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK14QStyleKitStyle15standardPaletteEv(
    const QStyleKitStyle *self) {
  return new QPalette(self->standardPalette());
}

//  void QStyleKitStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle6polishEP7QWidget(
    QStyleKitStyle *self,
    QWidget *widget) {
  self->polish(widget);
}

//  void QStyleKitStyle::polish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle6polishEP12QApplication(
    QStyleKitStyle *self,
    QApplication *application) {
  self->polish(application);
}

//  void QStyleKitStyle::polish(QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle6polishER8QPalette(
    QStyleKitStyle *self,
    QPalette *palette) {
  self->polish(*palette);
}

//  void QStyleKitStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle8unpolishEP7QWidget(
    QStyleKitStyle *self,
    QWidget *widget) {
  self->unpolish(widget);
}

//  void QStyleKitStyle::unpolish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle8unpolishEP12QApplication(
    QStyleKitStyle *self,
    QApplication *application) {
  self->unpolish(application);
}

//  bool QStyleKitStyle::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QStyleKitStyle11eventFilterEP7QObjectP6QEvent(
    QStyleKitStyle *self,
    QObject *watched,
    QEvent *event) {
  return self->eventFilter(watched, event);
}

//  bool QStyleKitStyle::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QStyleKitStyle5eventEP6QEvent(
    QStyleKitStyle *self,
    QEvent *event) {
  return self->event(event);
}

//  void QStyleKitStyle::stylePathChanged(const QString &stylePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle16stylePathChangedERK7QString(
    QStyleKitStyle *self,
    const QString *stylePath) {
  self->stylePathChanged(*stylePath);
}

//  void QStyleKitStyle::themeNameChanged(const QString &themeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle16themeNameChangedERK7QString(
    QStyleKitStyle *self,
    const QString *themeName) {
  self->themeNameChanged(*themeName);
}

//  void QStyleKitStyle::availableThemeNamesChanged(const QStringList
//      &availableThemeNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle26availableThemeNamesChangedERK5QListI7QStringE(
    QStyleKitStyle *self,
    const QList<QString> *availableThemeNames) {
  self->availableThemeNamesChanged(*availableThemeNames);
}

//  void QStyleKitStyle::customThemeNamesChanged(const QStringList
//      &customThemeNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStyleKitStyle23customThemeNamesChangedERK5QListI7QStringE(
    QStyleKitStyle *self,
    const QList<QString> *customThemeNames) {
  self->customThemeNamesChanged(*customThemeNames);
}

//  QStyleKitStylePrivate *QStyleKitStyle::d_func()
extern "C" Q_DECL_EXPORT
QStyleKitStylePrivate *ritual_ZN14QStyleKitStyle6d_funcEv(
    QStyleKitStyle *self) {
  return self->d_func();
}

//  const QStyleKitStylePrivate *QStyleKitStyle::d_func() const
extern "C" Q_DECL_EXPORT
const QStyleKitStylePrivate *ritual_ZNK14QStyleKitStyle6d_funcEv(
    const QStyleKitStyle *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQStyleKitStyle, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStyleKitStyle(
    QStyleKitStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStyleKitStyle *>(self)->take(key, call);
}

//  void QStyleKitStyle::drawPrimitive(PrimitiveElement pe, const
//      QStyleOption *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK14QStyleKitStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::PrimitiveElement pe,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->QStyleKitStyle::drawPrimitive(pe, opt, p, w);
}

//  void QStyleKitStyle::drawControl(ControlElement element, const
//      QStyleOption *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK14QStyleKitStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->QStyleKitStyle::drawControl(element, opt, p, w);
}

//  QRect QStyleKitStyle::subElementRect(SubElement r, const QStyleOption
//      *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK14QStyleKitStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::SubElement r,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QRect(self->QStyleKitStyle::subElementRect(r, opt, widget));
}

//  void QStyleKitStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK14QStyleKitStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QPainter *p,
    const QWidget *w) {
  self->QStyleKitStyle::drawComplexControl(cc, opt, p, w);
}

//  SubControl QStyleKitStyle::hitTestComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, const QPoint &pt, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_own_ZNK14QStyleKitStyle21hitTestComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    const QPoint *pt,
    const QWidget *w) {
  return self->QStyleKitStyle::hitTestComplexControl(cc, opt, *pt, w);
}

//  QRect QStyleKitStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK14QStyleKitStyle14subControlRectEN6QStyle14ComplexControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QStyle::SubControl sc,
    const QWidget *w) {
  return new QRect(self->QStyleKitStyle::subControlRect(cc, opt, sc, w));
}

//  QSize QStyleKitStyle::sizeFromContents(ContentsType ct, const
//      QStyleOption *opt, const QSize &contentsSize, const QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK14QStyleKitStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QStyleKitStyle *self,
    QStyle::ContentsType ct,
    const QStyleOption *opt,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->QStyleKitStyle::sizeFromContents(
          ct,
          opt,
          *contentsSize,
          widget));
}

//  int QStyleKitStyle::pixelMetric(PixelMetric m, const QStyleOption *opt,
//      const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QStyleKitStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QStyleKitStyle *self,
    QStyle::PixelMetric m,
    const QStyleOption *opt,
    const QWidget *widget) {
  return self->QStyleKitStyle::pixelMetric(m, opt, widget);
}

//  int QStyleKitStyle::styleHint(StyleHint sh, const QStyleOption *opt,
//      const QWidget *w, QStyleHintReturn *shret) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QStyleKitStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QStyleKitStyle *self,
    QStyle::StyleHint sh,
    const QStyleOption *opt,
    const QWidget *w,
    QStyleHintReturn *shret) {
  return self->QStyleKitStyle::styleHint(sh, opt, w, shret);
}

//  QPalette QStyleKitStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK14QStyleKitStyle15standardPaletteEv(
    const QStyleKitStyle *self) {
  return new QPalette(self->QStyleKitStyle::standardPalette());
}

//  void QStyleKitStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QStyleKitStyle6polishEP7QWidget(
    QStyleKitStyle *self,
    QWidget *widget) {
  self->QStyleKitStyle::polish(widget);
}

//  void QStyleKitStyle::polish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QStyleKitStyle6polishEP12QApplication(
    QStyleKitStyle *self,
    QApplication *application) {
  self->QStyleKitStyle::polish(application);
}

//  void QStyleKitStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QStyleKitStyle8unpolishEP7QWidget(
    QStyleKitStyle *self,
    QWidget *widget) {
  self->QStyleKitStyle::unpolish(widget);
}

//  void QStyleKitStyle::unpolish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QStyleKitStyle8unpolishEP12QApplication(
    QStyleKitStyle *self,
    QApplication *application) {
  self->QStyleKitStyle::unpolish(application);
}

//  bool QStyleKitStyle::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QStyleKitStyle11eventFilterEP7QObjectP6QEvent(
    QStyleKitStyle *self,
    QObject *watched,
    QEvent *event) {
  return static_cast<OwnQStyleKitStyle *>(self)->OwnQStyleKitStyle::eventFilter(
      watched,
      event);
}

//  bool QStyleKitStyle::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QStyleKitStyle5eventEP6QEvent(
    QStyleKitStyle *self,
    QEvent *event) {
  return static_cast<OwnQStyleKitStyle *>(self)->OwnQStyleKitStyle::event(
      event);
}

#endif  // 1
