//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwindowsstyle_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qwindowsstyle_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qicon.h>
#include <QtCore/qpoint.h>
#include <QtGui/qfontmetrics.h>
#include <QtGui/qpalette.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWindowsStyle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWindowsStyle : QWindowsStyle {
  using QWindowsStyle::eventFilter;
};

//  A QWindowsStyle that Python can take functions over in. Every QWindowsStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWindowsStyleCall0)(const void *, QApplication *, int *);
typedef void (*CuteQWindowsStyleCall1)(const void *, QApplication *, int *);
typedef void (*CuteQWindowsStyleCall2)(const void *, QWidget *, int *);
typedef void (*CuteQWindowsStyleCall3)(const void *, QWidget *, int *);
typedef void (*CuteQWindowsStyleCall4)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef void (*CuteQWindowsStyleCall5)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef const QRect * (*CuteQWindowsStyleCall6)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef void (*CuteQWindowsStyleCall7)(const void *, int, const QStyleOptionComplex *, QPainter *, const QWidget *, int *);
typedef const QSize * (*CuteQWindowsStyleCall8)(const void *, int, const QStyleOption *, const QSize *, const QWidget *, int *);
typedef int (*CuteQWindowsStyleCall9)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef int (*CuteQWindowsStyleCall10)(const void *, int, const QStyleOption *, const QWidget *, QStyleHintReturn *, int *);
typedef const QPixmap * (*CuteQWindowsStyleCall11)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QIcon * (*CuteQWindowsStyleCall12)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef bool (*CuteQWindowsStyleCall13)(const void *, QObject *, QEvent *, int *);
typedef int (*CuteQWindowsStyleCall14)(const void *, int, const QStyleOptionComplex *, const QPoint *, const QWidget *, int *);
typedef const QRect * (*CuteQWindowsStyleCall15)(const void *, int, const QStyleOptionComplex *, int, const QWidget *, int *);
typedef const QPixmap * (*CuteQWindowsStyleCall16)(const void *, int, const QPixmap *, const QStyleOption *, int *);
typedef int (*CuteQWindowsStyleCall17)(const void *, int, int, int, const QStyleOption *, const QWidget *, int *);
typedef const QRect * (*CuteQWindowsStyleCall18)(const void *, const QFontMetrics *, const QRect *, int, bool, const QString *, int *);
typedef const QRect * (*CuteQWindowsStyleCall19)(const void *, const QRect *, int, const QPixmap *, int *);
typedef void (*CuteQWindowsStyleCall20)(const void *, QPainter *, const QRect *, int, const QPalette *, bool, const QString *, int, int *);
typedef void (*CuteQWindowsStyleCall21)(const void *, QPainter *, const QRect *, int, const QPixmap *, int *);
typedef const QPalette * (*CuteQWindowsStyleCall22)(const void *, int *);
typedef bool (*CuteQWindowsStyleCall23)(const void *, QEvent *, int *);
typedef void (*CuteQWindowsStyleCall24)(const void *, QTimerEvent *, int *);
typedef void (*CuteQWindowsStyleCall25)(const void *, QChildEvent *, int *);
typedef void (*CuteQWindowsStyleCall26)(const void *, QEvent *, int *);
typedef void (*CuteQWindowsStyleCall27)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQWindowsStyleCall28)(const void *, const QMetaMethod *, int *);
class CuteQWindowsStyle : public QWindowsStyle {
public:
  using QWindowsStyle::QWindowsStyle;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QStyle6polishEP12QApplication")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP12QApplication")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle6polishEP7QWidget")) {
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
    if (!std::strcmp(key, "_ZNK6QStyle14subElementRectENS_10SubElementEPK12QStyleOptionPK7QWidget")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle18drawComplexControlENS_14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle16sizeFromContentsENS_12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle11pixelMetricENS_11PixelMetricEPK12QStyleOptionPK7QWidget")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle9styleHintENS_9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle21hitTestComplexControlENS_14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14subControlRectENS_14ComplexControlEPK19QStyleOptionComplexNS_10SubControlEPK7QWidget")) {
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
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
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

  //  void QWindowsStyle::polish(QApplication *a0)
  void polish(QApplication *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsStyleCall0 call = reinterpret_cast<CuteQWindowsStyleCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindowsStyle::polish(a0);
  }

  //  void QWindowsStyle::unpolish(QApplication *a0)
  void unpolish(QApplication *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsStyleCall1 call = reinterpret_cast<CuteQWindowsStyleCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindowsStyle::unpolish(a0);
  }

  //  void QWindowsStyle::polish(QWidget *a0)
  void polish(QWidget *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsStyleCall2 call = reinterpret_cast<CuteQWindowsStyleCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindowsStyle::polish(a0);
  }

  //  void QWindowsStyle::unpolish(QWidget *a0)
  void unpolish(QWidget *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowsStyleCall3 call = reinterpret_cast<CuteQWindowsStyleCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindowsStyle::unpolish(a0);
  }

  //  void QWindowsStyle::drawPrimitive(PrimitiveElement pe, const
  //      QStyleOption *opt, QPainter *p, const QWidget *w) const
  void drawPrimitive(
      QStyle::PrimitiveElement pe,
      const QStyleOption *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsStyleCall4 call = reinterpret_cast<CuteQWindowsStyleCall4>(taken[4]);
      call(this, static_cast<int>(pe), opt, p, w, &handled);
      if (handled) return;
    }
    QWindowsStyle::drawPrimitive(pe, opt, p, w);
  }

  //  void QWindowsStyle::drawControl(ControlElement element, const
  //      QStyleOption *opt, QPainter *p, const QWidget *w) const
  void drawControl(
      QStyle::ControlElement element,
      const QStyleOption *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsStyleCall5 call = reinterpret_cast<CuteQWindowsStyleCall5>(taken[5]);
      call(this, static_cast<int>(element), opt, p, w, &handled);
      if (handled) return;
    }
    QWindowsStyle::drawControl(element, opt, p, w);
  }

  //  QRect QWindowsStyle::subElementRect(SubElement r, const QStyleOption
  //      *opt, const QWidget *widget) const
  QRect subElementRect(
      QStyle::SubElement r,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsStyleCall6 call = reinterpret_cast<CuteQWindowsStyleCall6>(taken[6]);
      const QRect * given = call(this, static_cast<int>(r), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QWindowsStyle::subElementRect(r, opt, widget);
  }

  //  void QWindowsStyle::drawComplexControl(ComplexControl cc, const
  //      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
  void drawComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowsStyleCall7 call = reinterpret_cast<CuteQWindowsStyleCall7>(taken[7]);
      call(this, static_cast<int>(cc), opt, p, w, &handled);
      if (handled) return;
    }
    QWindowsStyle::drawComplexControl(cc, opt, p, w);
  }

  //  QSize QWindowsStyle::sizeFromContents(ContentsType ct, const
  //      QStyleOption *opt, const QSize &contentsSize, const QWidget
  //      *widget) const
  QSize sizeFromContents(
      QStyle::ContentsType ct,
      const QStyleOption *opt,
      const QSize &contentsSize,
      const QWidget *widget) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWindowsStyleCall8 call = reinterpret_cast<CuteQWindowsStyleCall8>(taken[8]);
      const QSize * given = call(this, static_cast<int>(ct), opt, &contentsSize, widget, &handled);
      if (handled && given) return *given;
    }
    return QWindowsStyle::sizeFromContents(ct, opt, contentsSize, widget);
  }

  //  int QWindowsStyle::pixelMetric(PixelMetric pm, const QStyleOption
  //      *option, const QWidget *widget) const
  int pixelMetric(
      QStyle::PixelMetric pm,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWindowsStyleCall9 call = reinterpret_cast<CuteQWindowsStyleCall9>(taken[9]);
      int given = call(this, static_cast<int>(pm), option, widget, &handled);
      if (handled) return given;
    }
    return QWindowsStyle::pixelMetric(pm, option, widget);
  }

  //  int QWindowsStyle::styleHint(StyleHint hint, const QStyleOption *opt,
  //      const QWidget *widget, QStyleHintReturn *returnData) const
  int styleHint(
      QStyle::StyleHint hint,
      const QStyleOption *opt,
      const QWidget *widget,
      QStyleHintReturn *returnData) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWindowsStyleCall10 call = reinterpret_cast<CuteQWindowsStyleCall10>(taken[10]);
      int given = call(this, static_cast<int>(hint), opt, widget, returnData, &handled);
      if (handled) return given;
    }
    return QWindowsStyle::styleHint(hint, opt, widget, returnData);
  }

  //  QPixmap QWindowsStyle::standardPixmap(StandardPixmap standardPixmap,
  //      const QStyleOption *opt, const QWidget *widget) const
  QPixmap standardPixmap(
      QStyle::StandardPixmap standardPixmap,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQWindowsStyleCall11 call = reinterpret_cast<CuteQWindowsStyleCall11>(taken[11]);
      const QPixmap * given = call(this, static_cast<int>(standardPixmap), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QWindowsStyle::standardPixmap(standardPixmap, opt, widget);
  }

  //  QIcon QWindowsStyle::standardIcon(StandardPixmap standardIcon, const
  //      QStyleOption *option, const QWidget *widget) const
  QIcon standardIcon(
      QStyle::StandardPixmap standardIcon,
      const QStyleOption *option,
      const QWidget *widget) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQWindowsStyleCall12 call = reinterpret_cast<CuteQWindowsStyleCall12>(taken[12]);
      const QIcon * given = call(this, static_cast<int>(standardIcon), option, widget, &handled);
      if (handled && given) return *given;
    }
    return QWindowsStyle::standardIcon(standardIcon, option, widget);
  }

  //  bool QWindowsStyle::eventFilter(QObject *o, QEvent *e)
  bool eventFilter(QObject *o, QEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWindowsStyleCall13 call = reinterpret_cast<CuteQWindowsStyleCall13>(taken[13]);
      bool given = call(this, o, e, &handled);
      if (handled) return given;
    }
    return QWindowsStyle::eventFilter(o, e);
  }

  //  SubControl QCommonStyle::hitTestComplexControl(ComplexControl cc,
  //      const QStyleOptionComplex *opt, const QPoint &pt, const QWidget
  //      *w) const
  QStyle::SubControl hitTestComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      const QPoint &pt,
      const QWidget *w) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQWindowsStyleCall14 call = reinterpret_cast<CuteQWindowsStyleCall14>(taken[14]);
      int given = call(this, static_cast<int>(cc), opt, &pt, w, &handled);
      if (handled) return static_cast<QStyle::SubControl>(given);
    }
    return QCommonStyle::hitTestComplexControl(cc, opt, pt, w);
  }

  //  QRect QCommonStyle::subControlRect(ComplexControl cc, const
  //      QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const
  QRect subControlRect(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QStyle::SubControl sc,
      const QWidget *w) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQWindowsStyleCall15 call = reinterpret_cast<CuteQWindowsStyleCall15>(taken[15]);
      const QRect * given = call(this, static_cast<int>(cc), opt, static_cast<int>(sc), w, &handled);
      if (handled && given) return *given;
    }
    return QCommonStyle::subControlRect(cc, opt, sc, w);
  }

  //  QPixmap QCommonStyle::generatedIconPixmap(QIcon::Mode iconMode, const
  //      QPixmap &pixmap, const QStyleOption *opt) const
  QPixmap generatedIconPixmap(
      QIcon::Mode iconMode,
      const QPixmap &pixmap,
      const QStyleOption *opt) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQWindowsStyleCall16 call = reinterpret_cast<CuteQWindowsStyleCall16>(taken[16]);
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
      CuteQWindowsStyleCall17 call = reinterpret_cast<CuteQWindowsStyleCall17>(taken[17]);
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
      CuteQWindowsStyleCall18 call = reinterpret_cast<CuteQWindowsStyleCall18>(taken[18]);
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
      CuteQWindowsStyleCall19 call = reinterpret_cast<CuteQWindowsStyleCall19>(taken[19]);
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
      CuteQWindowsStyleCall20 call = reinterpret_cast<CuteQWindowsStyleCall20>(taken[20]);
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
      CuteQWindowsStyleCall21 call = reinterpret_cast<CuteQWindowsStyleCall21>(taken[21]);
      call(this, painter, &rect, alignment, &pixmap, &handled);
      if (handled) return;
    }
    QStyle::drawItemPixmap(painter, rect, alignment, pixmap);
  }

  //  QPalette QStyle::standardPalette() const
  QPalette standardPalette() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQWindowsStyleCall22 call = reinterpret_cast<CuteQWindowsStyleCall22>(taken[22]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QStyle::standardPalette();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWindowsStyleCall23 call = reinterpret_cast<CuteQWindowsStyleCall23>(taken[23]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQWindowsStyleCall24 call = reinterpret_cast<CuteQWindowsStyleCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWindowsStyleCall25 call = reinterpret_cast<CuteQWindowsStyleCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWindowsStyleCall26 call = reinterpret_cast<CuteQWindowsStyleCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWindowsStyleCall27 call = reinterpret_cast<CuteQWindowsStyleCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWindowsStyleCall28 call = reinterpret_cast<CuteQWindowsStyleCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QWindowsStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QWindowsStyle10metaObjectEv(
    const QWindowsStyle *self) {
  return self->metaObject();
}

//  QString QWindowsStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QWindowsStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWindowsStyle::tr(s, c, n));
}

//  QWindowsStyle::QWindowsStyle()
extern "C" Q_DECL_EXPORT
QWindowsStyle *ritual_ZN13QWindowsStyleC1Ev() {
  return new CuteQWindowsStyle();
}

//  QWindowsStyle::~QWindowsStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWindowsStyleD1Ev(QWindowsStyle *self) {
  delete self;
}

//  void QWindowsStyle::polish(QApplication *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWindowsStyle6polishEP12QApplication(
    QWindowsStyle *self,
    QApplication *a0) {
  self->polish(a0);
}

//  void QWindowsStyle::unpolish(QApplication *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWindowsStyle8unpolishEP12QApplication(
    QWindowsStyle *self,
    QApplication *a0) {
  self->unpolish(a0);
}

//  void QWindowsStyle::polish(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWindowsStyle6polishEP7QWidget(
    QWindowsStyle *self,
    QWidget *a0) {
  self->polish(a0);
}

//  void QWindowsStyle::unpolish(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWindowsStyle8unpolishEP7QWidget(
    QWindowsStyle *self,
    QWidget *a0) {
  self->unpolish(a0);
}

//  void QWindowsStyle::drawPrimitive(PrimitiveElement pe, const QStyleOption
//      *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QWindowsStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QWindowsStyle *self,
    QStyle::PrimitiveElement pe,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawPrimitive(pe, opt, p, w);
}

//  void QWindowsStyle::drawControl(ControlElement element, const
//      QStyleOption *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QWindowsStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QWindowsStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawControl(element, opt, p, w);
}

//  QRect QWindowsStyle::subElementRect(SubElement r, const QStyleOption
//      *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QWindowsStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QWindowsStyle *self,
    QStyle::SubElement r,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QRect(self->subElementRect(r, opt, widget));
}

//  void QWindowsStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QWindowsStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QWindowsStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawComplexControl(cc, opt, p, w);
}

//  QSize QWindowsStyle::sizeFromContents(ContentsType ct, const QStyleOption
//      *opt, const QSize &contentsSize, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QWindowsStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QWindowsStyle *self,
    QStyle::ContentsType ct,
    const QStyleOption *opt,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(self->sizeFromContents(ct, opt, *contentsSize, widget));
}

//  int QWindowsStyle::pixelMetric(PixelMetric pm, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QWindowsStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QWindowsStyle *self,
    QStyle::PixelMetric pm,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->pixelMetric(pm, option, widget);
}

//  int QWindowsStyle::styleHint(StyleHint hint, const QStyleOption *opt,
//      const QWidget *widget, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QWindowsStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QWindowsStyle *self,
    QStyle::StyleHint hint,
    const QStyleOption *opt,
    const QWidget *widget,
    QStyleHintReturn *returnData) {
  return self->styleHint(hint, opt, widget, returnData);
}

//  QPixmap QWindowsStyle::standardPixmap(StandardPixmap standardPixmap,
//      const QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK13QWindowsStyle14standardPixmapEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QWindowsStyle *self,
    QStyle::StandardPixmap standardPixmap,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QPixmap(self->standardPixmap(standardPixmap, opt, widget));
}

//  QIcon QWindowsStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK13QWindowsStyle12standardIconEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QWindowsStyle *self,
    QStyle::StandardPixmap standardIcon,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QIcon(self->standardIcon(standardIcon, option, widget));
}

//  bool QWindowsStyle::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QWindowsStyle11eventFilterEP7QObjectP6QEvent(
    QWindowsStyle *self,
    QObject *o,
    QEvent *e) {
  return self->eventFilter(o, e);
}

//  a Python function taken by a CuteQWindowsStyle, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsStyle(
    QWindowsStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsStyle *>(self)->take(key, call);
}

//  void QWindowsStyle::polish(QApplication *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QWindowsStyle6polishEP12QApplication(
    QWindowsStyle *self,
    QApplication *a0) {
  self->QWindowsStyle::polish(a0);
}

//  void QWindowsStyle::unpolish(QApplication *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QWindowsStyle8unpolishEP12QApplication(
    QWindowsStyle *self,
    QApplication *a0) {
  self->QWindowsStyle::unpolish(a0);
}

//  void QWindowsStyle::polish(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QWindowsStyle6polishEP7QWidget(
    QWindowsStyle *self,
    QWidget *a0) {
  self->QWindowsStyle::polish(a0);
}

//  void QWindowsStyle::unpolish(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QWindowsStyle8unpolishEP7QWidget(
    QWindowsStyle *self,
    QWidget *a0) {
  self->QWindowsStyle::unpolish(a0);
}

//  void QWindowsStyle::drawPrimitive(PrimitiveElement pe, const QStyleOption
//      *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QWindowsStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QWindowsStyle *self,
    QStyle::PrimitiveElement pe,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->QWindowsStyle::drawPrimitive(pe, opt, p, w);
}

//  void QWindowsStyle::drawControl(ControlElement element, const
//      QStyleOption *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QWindowsStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QWindowsStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->QWindowsStyle::drawControl(element, opt, p, w);
}

//  QRect QWindowsStyle::subElementRect(SubElement r, const QStyleOption
//      *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK13QWindowsStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QWindowsStyle *self,
    QStyle::SubElement r,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QRect(self->QWindowsStyle::subElementRect(r, opt, widget));
}

//  void QWindowsStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QWindowsStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QWindowsStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QPainter *p,
    const QWidget *w) {
  self->QWindowsStyle::drawComplexControl(cc, opt, p, w);
}

//  QSize QWindowsStyle::sizeFromContents(ContentsType ct, const QStyleOption
//      *opt, const QSize &contentsSize, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK13QWindowsStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QWindowsStyle *self,
    QStyle::ContentsType ct,
    const QStyleOption *opt,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->QWindowsStyle::sizeFromContents(
          ct,
          opt,
          *contentsSize,
          widget));
}

//  int QWindowsStyle::pixelMetric(PixelMetric pm, const QStyleOption
//      *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QWindowsStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QWindowsStyle *self,
    QStyle::PixelMetric pm,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->QWindowsStyle::pixelMetric(pm, option, widget);
}

//  int QWindowsStyle::styleHint(StyleHint hint, const QStyleOption *opt,
//      const QWidget *widget, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QWindowsStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QWindowsStyle *self,
    QStyle::StyleHint hint,
    const QStyleOption *opt,
    const QWidget *widget,
    QStyleHintReturn *returnData) {
  return self->QWindowsStyle::styleHint(hint, opt, widget, returnData);
}

//  QPixmap QWindowsStyle::standardPixmap(StandardPixmap standardPixmap,
//      const QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK13QWindowsStyle14standardPixmapEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QWindowsStyle *self,
    QStyle::StandardPixmap standardPixmap,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QPixmap(
      self->QWindowsStyle::standardPixmap(
          standardPixmap,
          opt,
          widget));
}

//  QIcon QWindowsStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK13QWindowsStyle12standardIconEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QWindowsStyle *self,
    QStyle::StandardPixmap standardIcon,
    const QStyleOption *option,
    const QWidget *widget) {
  return new QIcon(
      self->QWindowsStyle::standardIcon(
          standardIcon,
          option,
          widget));
}

//  bool QWindowsStyle::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QWindowsStyle11eventFilterEP7QObjectP6QEvent(
    QWindowsStyle *self,
    QObject *o,
    QEvent *e) {
  return static_cast<OwnQWindowsStyle *>(self)->OwnQWindowsStyle::eventFilter(
      o,
      e);
}
