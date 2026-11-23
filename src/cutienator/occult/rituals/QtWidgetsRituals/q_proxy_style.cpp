//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qproxystyle.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qproxystyle.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>
#include <QtGui/qfontmetrics.h>
#include <QtCore/qpoint.h>
#include <QtGui/qicon.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QProxyStyle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQProxyStyle : QProxyStyle {
  using QProxyStyle::event;
};

//  A QProxyStyle that Python can take functions over in. Every QProxyStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQProxyStyleCall0)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef void (*CuteQProxyStyleCall1)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef void (*CuteQProxyStyleCall2)(const void *, int, const QStyleOptionComplex *, QPainter *, const QWidget *, int *);
typedef void (*CuteQProxyStyleCall3)(const void *, QPainter *, const QRect *, int, const QPalette *, bool, const QString *, int, int *);
typedef void (*CuteQProxyStyleCall4)(const void *, QPainter *, const QRect *, int, const QPixmap *, int *);
typedef const QSize * (*CuteQProxyStyleCall5)(const void *, int, const QStyleOption *, const QSize *, const QWidget *, int *);
typedef const QRect * (*CuteQProxyStyleCall6)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QRect * (*CuteQProxyStyleCall7)(const void *, int, const QStyleOptionComplex *, int, const QWidget *, int *);
typedef const QRect * (*CuteQProxyStyleCall8)(const void *, const QFontMetrics *, const QRect *, int, bool, const QString *, int *);
typedef const QRect * (*CuteQProxyStyleCall9)(const void *, const QRect *, int, const QPixmap *, int *);
typedef int (*CuteQProxyStyleCall10)(const void *, int, const QStyleOptionComplex *, const QPoint *, const QWidget *, int *);
typedef int (*CuteQProxyStyleCall11)(const void *, int, const QStyleOption *, const QWidget *, QStyleHintReturn *, int *);
typedef int (*CuteQProxyStyleCall12)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef int (*CuteQProxyStyleCall13)(const void *, int, int, int, const QStyleOption *, const QWidget *, int *);
typedef const QIcon * (*CuteQProxyStyleCall14)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QPixmap * (*CuteQProxyStyleCall15)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QPixmap * (*CuteQProxyStyleCall16)(const void *, int, const QPixmap *, const QStyleOption *, int *);
typedef const QPalette * (*CuteQProxyStyleCall17)(const void *, int *);
typedef void (*CuteQProxyStyleCall18)(const void *, QWidget *, int *);
typedef void (*CuteQProxyStyleCall19)(const void *, QApplication *, int *);
typedef void (*CuteQProxyStyleCall20)(const void *, QWidget *, int *);
typedef void (*CuteQProxyStyleCall21)(const void *, QApplication *, int *);
typedef bool (*CuteQProxyStyleCall22)(const void *, QEvent *, int *);
typedef bool (*CuteQProxyStyleCall23)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQProxyStyleCall24)(const void *, QTimerEvent *, int *);
typedef void (*CuteQProxyStyleCall25)(const void *, QChildEvent *, int *);
typedef void (*CuteQProxyStyleCall26)(const void *, QEvent *, int *);
typedef void (*CuteQProxyStyleCall27)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQProxyStyleCall28)(const void *, const QMetaMethod *, int *);
class CuteQProxyStyle : public QProxyStyle {
public:
  using QProxyStyle::QProxyStyle;
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
    if (!std::strcmp(key, "_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOptionPK7QWidget")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOptionComplexNS_10SubControlEPK7QWidget")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle9styleHintENS_9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK7QWidget")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget")) {
      taken[13] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZNK6QStyle15standardPaletteEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle6polishEP7QWidget")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle6polishEP12QApplication")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP7QWidget")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP12QApplication")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[28] = call;
      return true;
    }
    return false;
  }

  //  void QProxyStyle::drawPrimitive(PrimitiveElement element, const
  //      QStyleOption *option, QPainter *painter, const QWidget *widget)
  //      const
  void drawPrimitive(
      QStyle::PrimitiveElement element,
      const QStyleOption *option,
      QPainter *painter,
      const QWidget *widget) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQProxyStyleCall0 call = reinterpret_cast<CuteQProxyStyleCall0>(taken[0]);
      call(this, static_cast<int>(element), option, painter, widget, &handled);
      if (handled) return;
    }
    QProxyStyle::drawPrimitive(element, option, painter, widget);
  }

  //  void QProxyStyle::drawControl(ControlElement element, const
  //      QStyleOption *option, QPainter *painter, const QWidget *widget)
  //      const
  void drawControl(
      QStyle::ControlElement element,
      const QStyleOption *option,
      QPainter *painter,
      const QWidget *widget) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQProxyStyleCall1 call = reinterpret_cast<CuteQProxyStyleCall1>(taken[1]);
      call(this, static_cast<int>(element), option, painter, widget, &handled);
      if (handled) return;
    }
    QProxyStyle::drawControl(element, option, painter, widget);
  }

  //  void QProxyStyle::drawComplexControl(ComplexControl control, const
  //      QStyleOptionComplex *option, QPainter *painter, const QWidget
  //      *widget) const
  void drawComplexControl(
      QStyle::ComplexControl control,
      const QStyleOptionComplex *option,
      QPainter *painter,
      const QWidget *widget) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQProxyStyleCall2 call = reinterpret_cast<CuteQProxyStyleCall2>(taken[2]);
      call(this, static_cast<int>(control), option, painter, widget, &handled);
      if (handled) return;
    }
    QProxyStyle::drawComplexControl(control, option, painter, widget);
  }

  //  void QProxyStyle::drawItemText(QPainter *painter, const QRect &rect,
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
    if (taken[3]) {
      int handled = 0;
      CuteQProxyStyleCall3 call = reinterpret_cast<CuteQProxyStyleCall3>(taken[3]);
      call(this, painter, &rect, flags, &pal, enabled, &text, static_cast<int>(textRole), &handled);
      if (handled) return;
    }
    QProxyStyle::drawItemText(painter, rect, flags, pal, enabled, text, textRole);
  }

  //  void QProxyStyle::drawItemPixmap(QPainter *painter, const QRect
  //      &rect, int alignment, const QPixmap &pixmap) const
  void drawItemPixmap(
      QPainter *painter,
      const QRect &rect,
      int alignment,
      const QPixmap &pixmap) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQProxyStyleCall4 call = reinterpret_cast<CuteQProxyStyleCall4>(taken[4]);
      call(this, painter, &rect, alignment, &pixmap, &handled);
      if (handled) return;
    }
    QProxyStyle::drawItemPixmap(painter, rect, alignment, pixmap);
  }

  //  QSize QProxyStyle::sizeFromContents(ContentsType type, const
  //      QStyleOption *option, const QSize &size, const QWidget *widget)
  //      const
  QSize sizeFromContents(
      QStyle::ContentsType type,
      const QStyleOption *option,
      const QSize &size,
      const QWidget *widget) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQProxyStyleCall5 call = reinterpret_cast<CuteQProxyStyleCall5>(taken[5]);
      const QSize * given = call(this, static_cast<int>(type), option, &size, widget, &handled);
      if (handled && given) return *given;
    }
    return QProxyStyle::sizeFromContents(type, option, size, widget);
  }

  //  QRect QProxyStyle::subElementRect(SubElement element, const
  //      QStyleOption *option, const QWidget *widget) const
  QRect subElementRect(
      QStyle::SubElement element,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQProxyStyleCall6 call = reinterpret_cast<CuteQProxyStyleCall6>(taken[6]);
      const QRect * given = call(this, static_cast<int>(element), option, widget, &handled);
      if (handled && given) return *given;
    }
    return QProxyStyle::subElementRect(element, option, widget);
  }

  //  QRect QProxyStyle::subControlRect(ComplexControl cc, const
  //      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget)
  //      const
  QRect subControlRect(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QStyle::SubControl sc,
      const QWidget *widget) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQProxyStyleCall7 call = reinterpret_cast<CuteQProxyStyleCall7>(taken[7]);
      const QRect * given = call(this, static_cast<int>(cc), opt, static_cast<int>(sc), widget, &handled);
      if (handled && given) return *given;
    }
    return QProxyStyle::subControlRect(cc, opt, sc, widget);
  }

  //  QRect QProxyStyle::itemTextRect(const QFontMetrics &fm, const QRect
  //      &r, int flags, bool enabled, const QString &text) const
  QRect itemTextRect(
      const QFontMetrics &fm,
      const QRect &r,
      int flags,
      bool enabled,
      const QString &text) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQProxyStyleCall8 call = reinterpret_cast<CuteQProxyStyleCall8>(taken[8]);
      const QRect * given = call(this, &fm, &r, flags, enabled, &text, &handled);
      if (handled && given) return *given;
    }
    return QProxyStyle::itemTextRect(fm, r, flags, enabled, text);
  }

  //  QRect QProxyStyle::itemPixmapRect(const QRect &r, int flags, const
  //      QPixmap &pixmap) const
  QRect itemPixmapRect(
      const QRect &r,
      int flags,
      const QPixmap &pixmap) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQProxyStyleCall9 call = reinterpret_cast<CuteQProxyStyleCall9>(taken[9]);
      const QRect * given = call(this, &r, flags, &pixmap, &handled);
      if (handled && given) return *given;
    }
    return QProxyStyle::itemPixmapRect(r, flags, pixmap);
  }

  //  SubControl QProxyStyle::hitTestComplexControl(ComplexControl control,
  //      const QStyleOptionComplex *option, const QPoint &pos, const
  //      QWidget *widget) const
  QStyle::SubControl hitTestComplexControl(
      QStyle::ComplexControl control,
      const QStyleOptionComplex *option,
      const QPoint &pos,
      const QWidget *widget) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQProxyStyleCall10 call = reinterpret_cast<CuteQProxyStyleCall10>(taken[10]);
      int given = call(this, static_cast<int>(control), option, &pos, widget, &handled);
      if (handled) return static_cast<QStyle::SubControl>(given);
    }
    return QProxyStyle::hitTestComplexControl(control, option, pos, widget);
  }

  //  int QProxyStyle::styleHint(StyleHint hint, const QStyleOption
  //      *option, const QWidget *widget, QStyleHintReturn *returnData)
  //      const
  int styleHint(
      QStyle::StyleHint hint,
      const QStyleOption *option,
      const QWidget *widget,
      QStyleHintReturn *returnData) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQProxyStyleCall11 call = reinterpret_cast<CuteQProxyStyleCall11>(taken[11]);
      int given = call(this, static_cast<int>(hint), option, widget, returnData, &handled);
      if (handled) return given;
    }
    return QProxyStyle::styleHint(hint, option, widget, returnData);
  }

  //  int QProxyStyle::pixelMetric(PixelMetric metric, const QStyleOption
  //      *option, const QWidget *widget) const
  int pixelMetric(
      QStyle::PixelMetric metric,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQProxyStyleCall12 call = reinterpret_cast<CuteQProxyStyleCall12>(taken[12]);
      int given = call(this, static_cast<int>(metric), option, widget, &handled);
      if (handled) return given;
    }
    return QProxyStyle::pixelMetric(metric, option, widget);
  }

  //  int QProxyStyle::layoutSpacing(QSizePolicy::ControlType control1,
  //      QSizePolicy::ControlType control2, Qt::Orientation orientation,
  //      const QStyleOption *option, const QWidget *widget) const
  int layoutSpacing(
      QSizePolicy::ControlType control1,
      QSizePolicy::ControlType control2,
      Qt::Orientation orientation,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQProxyStyleCall13 call = reinterpret_cast<CuteQProxyStyleCall13>(taken[13]);
      int given = call(this, static_cast<int>(control1), static_cast<int>(control2), static_cast<int>(orientation), option, widget, &handled);
      if (handled) return given;
    }
    return QProxyStyle::layoutSpacing(control1, control2, orientation, option, widget);
  }

  //  QIcon QProxyStyle::standardIcon(StandardPixmap standardIcon, const
  //      QStyleOption *option, const QWidget *widget) const
  QIcon standardIcon(
      QStyle::StandardPixmap standardIcon,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQProxyStyleCall14 call = reinterpret_cast<CuteQProxyStyleCall14>(taken[14]);
      const QIcon * given = call(this, static_cast<int>(standardIcon), option, widget, &handled);
      if (handled && given) return *given;
    }
    return QProxyStyle::standardIcon(standardIcon, option, widget);
  }

  //  QPixmap QProxyStyle::standardPixmap(StandardPixmap standardPixmap,
  //      const QStyleOption *opt, const QWidget *widget) const
  QPixmap standardPixmap(
      QStyle::StandardPixmap standardPixmap,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQProxyStyleCall15 call = reinterpret_cast<CuteQProxyStyleCall15>(taken[15]);
      const QPixmap * given = call(this, static_cast<int>(standardPixmap), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QProxyStyle::standardPixmap(standardPixmap, opt, widget);
  }

  //  QPixmap QProxyStyle::generatedIconPixmap(QIcon::Mode iconMode, const
  //      QPixmap &pixmap, const QStyleOption *opt) const
  QPixmap generatedIconPixmap(
      QIcon::Mode iconMode,
      const QPixmap &pixmap,
      const QStyleOption *opt) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQProxyStyleCall16 call = reinterpret_cast<CuteQProxyStyleCall16>(taken[16]);
      const QPixmap * given = call(this, static_cast<int>(iconMode), &pixmap, opt, &handled);
      if (handled && given) return *given;
    }
    return QProxyStyle::generatedIconPixmap(iconMode, pixmap, opt);
  }

  //  QPalette QProxyStyle::standardPalette() const
  QPalette standardPalette() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQProxyStyleCall17 call = reinterpret_cast<CuteQProxyStyleCall17>(taken[17]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QProxyStyle::standardPalette();
  }

  //  void QProxyStyle::polish(QWidget *widget)
  void polish(QWidget *widget) override {
    if (taken[18]) {
      int handled = 0;
      CuteQProxyStyleCall18 call = reinterpret_cast<CuteQProxyStyleCall18>(taken[18]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QProxyStyle::polish(widget);
  }

  //  void QProxyStyle::polish(QApplication *app)
  void polish(QApplication *app) override {
    if (taken[19]) {
      int handled = 0;
      CuteQProxyStyleCall19 call = reinterpret_cast<CuteQProxyStyleCall19>(taken[19]);
      call(this, app, &handled);
      if (handled) return;
    }
    QProxyStyle::polish(app);
  }

  //  void QProxyStyle::unpolish(QWidget *widget)
  void unpolish(QWidget *widget) override {
    if (taken[20]) {
      int handled = 0;
      CuteQProxyStyleCall20 call = reinterpret_cast<CuteQProxyStyleCall20>(taken[20]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QProxyStyle::unpolish(widget);
  }

  //  void QProxyStyle::unpolish(QApplication *app)
  void unpolish(QApplication *app) override {
    if (taken[21]) {
      int handled = 0;
      CuteQProxyStyleCall21 call = reinterpret_cast<CuteQProxyStyleCall21>(taken[21]);
      call(this, app, &handled);
      if (handled) return;
    }
    QProxyStyle::unpolish(app);
  }

  //  bool QProxyStyle::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[22]) {
      int handled = 0;
      CuteQProxyStyleCall22 call = reinterpret_cast<CuteQProxyStyleCall22>(taken[22]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QProxyStyle::event(e);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQProxyStyleCall23 call = reinterpret_cast<CuteQProxyStyleCall23>(taken[23]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQProxyStyleCall24 call = reinterpret_cast<CuteQProxyStyleCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQProxyStyleCall25 call = reinterpret_cast<CuteQProxyStyleCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQProxyStyleCall26 call = reinterpret_cast<CuteQProxyStyleCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQProxyStyleCall27 call = reinterpret_cast<CuteQProxyStyleCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQProxyStyleCall28 call = reinterpret_cast<CuteQProxyStyleCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QProxyStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QProxyStyle10metaObjectEv(
    const QProxyStyle *self) {
  return self->metaObject();
}

//  QString QProxyStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QProxyStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QProxyStyle::tr(s, c, n));
}

//  QProxyStyle::QProxyStyle(QStyle *style)
extern "C" Q_DECL_EXPORT
QProxyStyle *ritual_ZN11QProxyStyleC1EP6QStyle(QStyle *style) {
  return new CuteQProxyStyle(style);
}

//  QProxyStyle::QProxyStyle(const QString &key)
extern "C" Q_DECL_EXPORT
QProxyStyle *ritual_ZN11QProxyStyleC1ERK7QString(const QString *key) {
  return new CuteQProxyStyle(*key);
}

//  QProxyStyle::~QProxyStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QProxyStyleD1Ev(QProxyStyle *self) {
  delete self;
}

//  QStyle *QProxyStyle::baseStyle() const
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZNK11QProxyStyle9baseStyleEv(const QProxyStyle *self) {
  return self->baseStyle();
}

//  void QProxyStyle::setBaseStyle(QStyle *style)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QProxyStyle12setBaseStyleEP6QStyle(
    QProxyStyle *self,
    QStyle *style) {
  self->setBaseStyle(style);
}

//  void QProxyStyle::drawPrimitive(PrimitiveElement element, const
//      QStyleOption *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QProxyStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QProxyStyle *self,
    QStyle::PrimitiveElement element,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawPrimitive(element, option, painter, widget);
}

//  void QProxyStyle::drawControl(ControlElement element, const QStyleOption
//      *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QProxyStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QProxyStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawControl(element, option, painter, widget);
}

//  void QProxyStyle::drawComplexControl(ComplexControl control, const
//      QStyleOptionComplex *option, QPainter *painter, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QProxyStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QProxyStyle *self,
    QStyle::ComplexControl control,
    const QStyleOptionComplex *option,
    QPainter *painter,
    const QWidget *widget) {
  self->drawComplexControl(control, option, painter, widget);
}

//  void QProxyStyle::drawItemText(QPainter *painter, const QRect &rect, int
//      flags, const QPalette &pal, bool enabled, const QString &text,
//      QPalette::ColorRole textRole) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QProxyStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE(
    const QProxyStyle *self,
    QPainter *painter,
    const QRect *rect,
    int flags,
    const QPalette *pal,
    bool enabled,
    const QString *text,
    QPalette::ColorRole textRole) {
  self->drawItemText(painter, *rect, flags, *pal, enabled, *text, textRole);
}

//  void QProxyStyle::drawItemPixmap(QPainter *painter, const QRect &rect,
//      int alignment, const QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QProxyStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap(
    const QProxyStyle *self,
    QPainter *painter,
    const QRect *rect,
    int alignment,
    const QPixmap *pixmap) {
  self->drawItemPixmap(painter, *rect, alignment, *pixmap);
}

//  QSize QProxyStyle::sizeFromContents(ContentsType type, const QStyleOption
//      *option, const QSize &size, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QProxyStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QProxyStyle *self,
    QStyle::ContentsType type,
    const QStyleOption *option,
    const QSize *size,
    const QWidget *widget) {
  return new QSize(self->sizeFromContents(type, option, *size, widget));
}

//  QRect QProxyStyle::subElementRect(SubElement element, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QProxyStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QProxyStyle *self,
    QStyle::SubElement element,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QRect(self->subElementRect(element, option, widget));
}

//  QRect QProxyStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QProxyStyle14subControlRectEN6QStyle14ComplexControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget(
    const QProxyStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QStyle::SubControl sc,
    const QWidget *widget) {
  return new QRect(self->subControlRect(cc, opt, sc, widget));
}

//  QRect QProxyStyle::itemTextRect(const QFontMetrics &fm, const QRect &r,
//      int flags, bool enabled, const QString &text) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QProxyStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString(
    const QProxyStyle *self,
    const QFontMetrics *fm,
    const QRect *r,
    int flags,
    bool enabled,
    const QString *text) {
  return new QRect(self->itemTextRect(*fm, *r, flags, enabled, *text));
}

//  QRect QProxyStyle::itemPixmapRect(const QRect &r, int flags, const
//      QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QProxyStyle14itemPixmapRectERK5QRectiRK7QPixmap(
    const QProxyStyle *self,
    const QRect *r,
    int flags,
    const QPixmap *pixmap) {
  return new QRect(self->itemPixmapRect(*r, flags, *pixmap));
}

//  SubControl QProxyStyle::hitTestComplexControl(ComplexControl control,
//      const QStyleOptionComplex *option, const QPoint &pos, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_ZNK11QProxyStyle21hitTestComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QProxyStyle *self,
    QStyle::ComplexControl control,
    const QStyleOptionComplex *option,
    const QPoint *pos,
    const QWidget *widget) {
  return self->hitTestComplexControl(control, option, *pos, widget);
}

//  int QProxyStyle::styleHint(StyleHint hint, const QStyleOption *option,
//      const QWidget *widget, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QProxyStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QProxyStyle *self,
    QStyle::StyleHint hint,
    const QStyleOption *option,
    const QWidget *widget,
    QStyleHintReturn *returnData) {
  return self->styleHint(hint, option, widget, returnData);
}

//  int QProxyStyle::pixelMetric(PixelMetric metric, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QProxyStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QProxyStyle *self,
    QStyle::PixelMetric metric,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->pixelMetric(metric, option, widget);
}

//  int QProxyStyle::layoutSpacing(QSizePolicy::ControlType control1,
//      QSizePolicy::ControlType control2, Qt::Orientation orientation, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QProxyStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget(
    const QProxyStyle *self,
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

//  QIcon QProxyStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK11QProxyStyle12standardIconEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QProxyStyle *self,
    QStyle::StandardPixmap standardIcon,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QIcon(self->standardIcon(standardIcon, option, widget));
}

//  QPixmap QProxyStyle::standardPixmap(StandardPixmap standardPixmap, const
//      QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK11QProxyStyle14standardPixmapEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QProxyStyle *self,
    QStyle::StandardPixmap standardPixmap,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QPixmap(self->standardPixmap(standardPixmap, opt, widget));
}

//  QPixmap QProxyStyle::generatedIconPixmap(QIcon::Mode iconMode, const
//      QPixmap &pixmap, const QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK11QProxyStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption(
    const QProxyStyle *self,
    QIcon::Mode iconMode,
    const QPixmap *pixmap,
    const QStyleOption *opt) {
  return new QPixmap(self->generatedIconPixmap(iconMode, *pixmap, opt));
}

//  QPalette QProxyStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK11QProxyStyle15standardPaletteEv(
    const QProxyStyle *self) {
  return new QPalette(self->standardPalette());
}

//  void QProxyStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QProxyStyle6polishEP7QWidget(
    QProxyStyle *self,
    QWidget *widget) {
  self->polish(widget);
}

//  void QProxyStyle::polish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QProxyStyle6polishEP12QApplication(
    QProxyStyle *self,
    QApplication *app) {
  self->polish(app);
}

//  void QProxyStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QProxyStyle8unpolishEP7QWidget(
    QProxyStyle *self,
    QWidget *widget) {
  self->unpolish(widget);
}

//  void QProxyStyle::unpolish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QProxyStyle8unpolishEP12QApplication(
    QProxyStyle *self,
    QApplication *app) {
  self->unpolish(app);
}

//  bool QProxyStyle::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QProxyStyle5eventEP6QEvent(QProxyStyle *self, QEvent *e) {
  return self->event(e);
}

//  QProxyStylePrivate *QProxyStyle::d_func()
extern "C" Q_DECL_EXPORT
QProxyStylePrivate *ritual_ZN11QProxyStyle6d_funcEv(QProxyStyle *self) {
  return self->d_func();
}

//  const QProxyStylePrivate *QProxyStyle::d_func() const
extern "C" Q_DECL_EXPORT
const QProxyStylePrivate *ritual_ZNK11QProxyStyle6d_funcEv(
    const QProxyStyle *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQProxyStyle, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QProxyStyle(
    QProxyStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQProxyStyle *>(self)->take(key, call);
}

//  void QProxyStyle::drawPrimitive(PrimitiveElement element, const
//      QStyleOption *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QProxyStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QProxyStyle *self,
    QStyle::PrimitiveElement element,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->QProxyStyle::drawPrimitive(element, option, painter, widget);
}

//  void QProxyStyle::drawControl(ControlElement element, const QStyleOption
//      *option, QPainter *painter, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QProxyStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QProxyStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *option,
    QPainter *painter,
    const QWidget *widget) {
  self->QProxyStyle::drawControl(element, option, painter, widget);
}

//  void QProxyStyle::drawComplexControl(ComplexControl control, const
//      QStyleOptionComplex *option, QPainter *painter, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QProxyStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QProxyStyle *self,
    QStyle::ComplexControl control,
    const QStyleOptionComplex *option,
    QPainter *painter,
    const QWidget *widget) {
  self->QProxyStyle::drawComplexControl(control, option, painter, widget);
}

//  void QProxyStyle::drawItemText(QPainter *painter, const QRect &rect, int
//      flags, const QPalette &pal, bool enabled, const QString &text,
//      QPalette::ColorRole textRole) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QProxyStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE(
    const QProxyStyle *self,
    QPainter *painter,
    const QRect *rect,
    int flags,
    const QPalette *pal,
    bool enabled,
    const QString *text,
    QPalette::ColorRole textRole) {
  self->QProxyStyle::drawItemText(
      painter,
      *rect,
      flags,
      *pal,
      enabled,
      *text,
      textRole);
}

//  void QProxyStyle::drawItemPixmap(QPainter *painter, const QRect &rect,
//      int alignment, const QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QProxyStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap(
    const QProxyStyle *self,
    QPainter *painter,
    const QRect *rect,
    int alignment,
    const QPixmap *pixmap) {
  self->QProxyStyle::drawItemPixmap(painter, *rect, alignment, *pixmap);
}

//  QSize QProxyStyle::sizeFromContents(ContentsType type, const QStyleOption
//      *option, const QSize &size, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QProxyStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QProxyStyle *self,
    QStyle::ContentsType type,
    const QStyleOption *option,
    const QSize *size,
    const QWidget *widget) {
  return new QSize(
      self->QProxyStyle::sizeFromContents(
          type,
          option,
          *size,
          widget));
}

//  QRect QProxyStyle::subElementRect(SubElement element, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK11QProxyStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QProxyStyle *self,
    QStyle::SubElement element,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QRect(
      self->QProxyStyle::subElementRect(
          element,
          option,
          widget));
}

//  QRect QProxyStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *opt, SubControl sc, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK11QProxyStyle14subControlRectEN6QStyle14ComplexControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget(
    const QProxyStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QStyle::SubControl sc,
    const QWidget *widget) {
  return new QRect(self->QProxyStyle::subControlRect(cc, opt, sc, widget));
}

//  QRect QProxyStyle::itemTextRect(const QFontMetrics &fm, const QRect &r,
//      int flags, bool enabled, const QString &text) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK11QProxyStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString(
    const QProxyStyle *self,
    const QFontMetrics *fm,
    const QRect *r,
    int flags,
    bool enabled,
    const QString *text) {
  return new QRect(
      self->QProxyStyle::itemTextRect(
          *fm,
          *r,
          flags,
          enabled,
          *text));
}

//  QRect QProxyStyle::itemPixmapRect(const QRect &r, int flags, const
//      QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK11QProxyStyle14itemPixmapRectERK5QRectiRK7QPixmap(
    const QProxyStyle *self,
    const QRect *r,
    int flags,
    const QPixmap *pixmap) {
  return new QRect(self->QProxyStyle::itemPixmapRect(*r, flags, *pixmap));
}

//  SubControl QProxyStyle::hitTestComplexControl(ComplexControl control,
//      const QStyleOptionComplex *option, const QPoint &pos, const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_own_ZNK11QProxyStyle21hitTestComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QProxyStyle *self,
    QStyle::ComplexControl control,
    const QStyleOptionComplex *option,
    const QPoint *pos,
    const QWidget *widget) {
  return self->QProxyStyle::hitTestComplexControl(
      control,
      option,
      *pos,
      widget);
}

//  int QProxyStyle::styleHint(StyleHint hint, const QStyleOption *option,
//      const QWidget *widget, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QProxyStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QProxyStyle *self,
    QStyle::StyleHint hint,
    const QStyleOption *option,
    const QWidget *widget,
    QStyleHintReturn *returnData) {
  return self->QProxyStyle::styleHint(hint, option, widget, returnData);
}

//  int QProxyStyle::pixelMetric(PixelMetric metric, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QProxyStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QProxyStyle *self,
    QStyle::PixelMetric metric,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->QProxyStyle::pixelMetric(metric, option, widget);
}

//  int QProxyStyle::layoutSpacing(QSizePolicy::ControlType control1,
//      QSizePolicy::ControlType control2, Qt::Orientation orientation, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QProxyStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget(
    const QProxyStyle *self,
    QSizePolicy::ControlType control1,
    QSizePolicy::ControlType control2,
    Qt::Orientation orientation,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->QProxyStyle::layoutSpacing(
      control1,
      control2,
      orientation,
      option,
      widget);
}

//  QIcon QProxyStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK11QProxyStyle12standardIconEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QProxyStyle *self,
    QStyle::StandardPixmap standardIcon,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QIcon(
      self->QProxyStyle::standardIcon(
          standardIcon,
          option,
          widget));
}

//  QPixmap QProxyStyle::standardPixmap(StandardPixmap standardPixmap, const
//      QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK11QProxyStyle14standardPixmapEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QProxyStyle *self,
    QStyle::StandardPixmap standardPixmap,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QPixmap(
      self->QProxyStyle::standardPixmap(
          standardPixmap,
          opt,
          widget));
}

//  QPixmap QProxyStyle::generatedIconPixmap(QIcon::Mode iconMode, const
//      QPixmap &pixmap, const QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK11QProxyStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption(
    const QProxyStyle *self,
    QIcon::Mode iconMode,
    const QPixmap *pixmap,
    const QStyleOption *opt) {
  return new QPixmap(
      self->QProxyStyle::generatedIconPixmap(
          iconMode,
          *pixmap,
          opt));
}

//  QPalette QProxyStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK11QProxyStyle15standardPaletteEv(
    const QProxyStyle *self) {
  return new QPalette(self->QProxyStyle::standardPalette());
}

//  void QProxyStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QProxyStyle6polishEP7QWidget(
    QProxyStyle *self,
    QWidget *widget) {
  self->QProxyStyle::polish(widget);
}

//  void QProxyStyle::polish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QProxyStyle6polishEP12QApplication(
    QProxyStyle *self,
    QApplication *app) {
  self->QProxyStyle::polish(app);
}

//  void QProxyStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QProxyStyle8unpolishEP7QWidget(
    QProxyStyle *self,
    QWidget *widget) {
  self->QProxyStyle::unpolish(widget);
}

//  void QProxyStyle::unpolish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QProxyStyle8unpolishEP12QApplication(
    QProxyStyle *self,
    QApplication *app) {
  self->QProxyStyle::unpolish(app);
}

//  bool QProxyStyle::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QProxyStyle5eventEP6QEvent(
    QProxyStyle *self,
    QEvent *e) {
  return static_cast<OwnQProxyStyle *>(self)->OwnQProxyStyle::event(e);
}
