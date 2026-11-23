//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcommonstyle.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcommonstyle.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qicon.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qfontmetrics.h>
#include <QtGui/qpalette.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCommonStyle that Python can take functions over in. Every QCommonStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCommonStyleCall0)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef void (*CuteQCommonStyleCall1)(const void *, int, const QStyleOption *, QPainter *, const QWidget *, int *);
typedef const QRect * (*CuteQCommonStyleCall2)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef void (*CuteQCommonStyleCall3)(const void *, int, const QStyleOptionComplex *, QPainter *, const QWidget *, int *);
typedef int (*CuteQCommonStyleCall4)(const void *, int, const QStyleOptionComplex *, const QPoint *, const QWidget *, int *);
typedef const QRect * (*CuteQCommonStyleCall5)(const void *, int, const QStyleOptionComplex *, int, const QWidget *, int *);
typedef const QSize * (*CuteQCommonStyleCall6)(const void *, int, const QStyleOption *, const QSize *, const QWidget *, int *);
typedef int (*CuteQCommonStyleCall7)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef int (*CuteQCommonStyleCall8)(const void *, int, const QStyleOption *, const QWidget *, QStyleHintReturn *, int *);
typedef const QIcon * (*CuteQCommonStyleCall9)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QPixmap * (*CuteQCommonStyleCall10)(const void *, int, const QStyleOption *, const QWidget *, int *);
typedef const QPixmap * (*CuteQCommonStyleCall11)(const void *, int, const QPixmap *, const QStyleOption *, int *);
typedef int (*CuteQCommonStyleCall12)(const void *, int, int, int, const QStyleOption *, const QWidget *, int *);
typedef void (*CuteQCommonStyleCall13)(const void *, QApplication *, int *);
typedef void (*CuteQCommonStyleCall14)(const void *, QWidget *, int *);
typedef void (*CuteQCommonStyleCall15)(const void *, QWidget *, int *);
typedef void (*CuteQCommonStyleCall16)(const void *, QApplication *, int *);
typedef const QRect * (*CuteQCommonStyleCall17)(const void *, const QFontMetrics *, const QRect *, int, bool, const QString *, int *);
typedef const QRect * (*CuteQCommonStyleCall18)(const void *, const QRect *, int, const QPixmap *, int *);
typedef void (*CuteQCommonStyleCall19)(const void *, QPainter *, const QRect *, int, const QPalette *, bool, const QString *, int, int *);
typedef void (*CuteQCommonStyleCall20)(const void *, QPainter *, const QRect *, int, const QPixmap *, int *);
typedef const QPalette * (*CuteQCommonStyleCall21)(const void *, int *);
typedef bool (*CuteQCommonStyleCall22)(const void *, QEvent *, int *);
typedef bool (*CuteQCommonStyleCall23)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQCommonStyleCall24)(const void *, QTimerEvent *, int *);
typedef void (*CuteQCommonStyleCall25)(const void *, QChildEvent *, int *);
typedef void (*CuteQCommonStyleCall26)(const void *, QEvent *, int *);
typedef void (*CuteQCommonStyleCall27)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQCommonStyleCall28)(const void *, const QMetaMethod *, int *);
class CuteQCommonStyle : public QCommonStyle {
public:
  using QCommonStyle::QCommonStyle;
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
    if (!std::strcmp(key, "_ZNK6QStyle12standardIconENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14standardPixmapENS_14StandardPixmapEPK12QStyleOptionPK7QWidget")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle6polishEP12QApplication")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle6polishEP7QWidget")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP7QWidget")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QStyle8unpolishEP12QApplication")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14itemPixmapRectERK5QRectiRK7QPixmap")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS5_9ColorRoleE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QStyle15standardPaletteEv")) {
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

  //  void QCommonStyle::drawPrimitive(PrimitiveElement pe, const
  //      QStyleOption *opt, QPainter *p, const QWidget *w) const
  void drawPrimitive(
      QStyle::PrimitiveElement pe,
      const QStyleOption *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCommonStyleCall0 call = reinterpret_cast<CuteQCommonStyleCall0>(taken[0]);
      call(this, static_cast<int>(pe), opt, p, w, &handled);
      if (handled) return;
    }
    QCommonStyle::drawPrimitive(pe, opt, p, w);
  }

  //  void QCommonStyle::drawControl(ControlElement element, const
  //      QStyleOption *opt, QPainter *p, const QWidget *w) const
  void drawControl(
      QStyle::ControlElement element,
      const QStyleOption *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCommonStyleCall1 call = reinterpret_cast<CuteQCommonStyleCall1>(taken[1]);
      call(this, static_cast<int>(element), opt, p, w, &handled);
      if (handled) return;
    }
    QCommonStyle::drawControl(element, opt, p, w);
  }

  //  QRect QCommonStyle::subElementRect(SubElement r, const QStyleOption
  //      *opt, const QWidget *widget) const
  QRect subElementRect(
      QStyle::SubElement r,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQCommonStyleCall2 call = reinterpret_cast<CuteQCommonStyleCall2>(taken[2]);
      const QRect * given = call(this, static_cast<int>(r), opt, widget, &handled);
      if (handled && given) return *given;
    }
    return QCommonStyle::subElementRect(r, opt, widget);
  }

  //  void QCommonStyle::drawComplexControl(ComplexControl cc, const
  //      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
  void drawComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      QPainter *p,
      const QWidget *w) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQCommonStyleCall3 call = reinterpret_cast<CuteQCommonStyleCall3>(taken[3]);
      call(this, static_cast<int>(cc), opt, p, w, &handled);
      if (handled) return;
    }
    QCommonStyle::drawComplexControl(cc, opt, p, w);
  }

  //  SubControl QCommonStyle::hitTestComplexControl(ComplexControl cc,
  //      const QStyleOptionComplex *opt, const QPoint &pt, const QWidget
  //      *w) const
  QStyle::SubControl hitTestComplexControl(
      QStyle::ComplexControl cc,
      const QStyleOptionComplex *opt,
      const QPoint &pt,
      const QWidget *w) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQCommonStyleCall4 call = reinterpret_cast<CuteQCommonStyleCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQCommonStyleCall5 call = reinterpret_cast<CuteQCommonStyleCall5>(taken[5]);
      const QRect * given = call(this, static_cast<int>(cc), opt, static_cast<int>(sc), w, &handled);
      if (handled && given) return *given;
    }
    return QCommonStyle::subControlRect(cc, opt, sc, w);
  }

  //  QSize QCommonStyle::sizeFromContents(ContentsType ct, const
  //      QStyleOption *opt, const QSize &contentsSize, const QWidget
  //      *widget) const
  QSize sizeFromContents(
      QStyle::ContentsType ct,
      const QStyleOption *opt,
      const QSize &contentsSize,
      const QWidget *widget) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQCommonStyleCall6 call = reinterpret_cast<CuteQCommonStyleCall6>(taken[6]);
      const QSize * given = call(this, static_cast<int>(ct), opt, &contentsSize, widget, &handled);
      if (handled && given) return *given;
    }
    return QCommonStyle::sizeFromContents(ct, opt, contentsSize, widget);
  }

  //  int QCommonStyle::pixelMetric(PixelMetric m, const QStyleOption *opt,
  //      const QWidget *widget) const
  int pixelMetric(
      QStyle::PixelMetric m,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQCommonStyleCall7 call = reinterpret_cast<CuteQCommonStyleCall7>(taken[7]);
      int given = call(this, static_cast<int>(m), opt, widget, &handled);
      if (handled) return given;
    }
    return QCommonStyle::pixelMetric(m, opt, widget);
  }

  //  int QCommonStyle::styleHint(StyleHint sh, const QStyleOption *opt,
  //      const QWidget *w, QStyleHintReturn *shret) const
  int styleHint(
      QStyle::StyleHint sh,
      const QStyleOption *opt,
      const QWidget *w,
      QStyleHintReturn *shret) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQCommonStyleCall8 call = reinterpret_cast<CuteQCommonStyleCall8>(taken[8]);
      int given = call(this, static_cast<int>(sh), opt, w, shret, &handled);
      if (handled) return given;
    }
    return QCommonStyle::styleHint(sh, opt, w, shret);
  }

  //  QIcon QCommonStyle::standardIcon(StandardPixmap standardIcon, const
  //      QStyleOption *opt, const QWidget *widget) const
  QIcon standardIcon(
      QStyle::StandardPixmap standardIcon,
      const QStyleOption *opt,
      const QWidget *widget) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQCommonStyleCall9 call = reinterpret_cast<CuteQCommonStyleCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQCommonStyleCall10 call = reinterpret_cast<CuteQCommonStyleCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQCommonStyleCall11 call = reinterpret_cast<CuteQCommonStyleCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQCommonStyleCall12 call = reinterpret_cast<CuteQCommonStyleCall12>(taken[12]);
      int given = call(this, static_cast<int>(control1), static_cast<int>(control2), static_cast<int>(orientation), option, widget, &handled);
      if (handled) return given;
    }
    return QCommonStyle::layoutSpacing(control1, control2, orientation, option, widget);
  }

  //  void QCommonStyle::polish(QApplication *app)
  void polish(QApplication *app) override {
    if (taken[13]) {
      int handled = 0;
      CuteQCommonStyleCall13 call = reinterpret_cast<CuteQCommonStyleCall13>(taken[13]);
      call(this, app, &handled);
      if (handled) return;
    }
    QCommonStyle::polish(app);
  }

  //  void QCommonStyle::polish(QWidget *widget)
  void polish(QWidget *widget) override {
    if (taken[14]) {
      int handled = 0;
      CuteQCommonStyleCall14 call = reinterpret_cast<CuteQCommonStyleCall14>(taken[14]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QCommonStyle::polish(widget);
  }

  //  void QCommonStyle::unpolish(QWidget *widget)
  void unpolish(QWidget *widget) override {
    if (taken[15]) {
      int handled = 0;
      CuteQCommonStyleCall15 call = reinterpret_cast<CuteQCommonStyleCall15>(taken[15]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QCommonStyle::unpolish(widget);
  }

  //  void QCommonStyle::unpolish(QApplication *application)
  void unpolish(QApplication *application) override {
    if (taken[16]) {
      int handled = 0;
      CuteQCommonStyleCall16 call = reinterpret_cast<CuteQCommonStyleCall16>(taken[16]);
      call(this, application, &handled);
      if (handled) return;
    }
    QCommonStyle::unpolish(application);
  }

  //  QRect QStyle::itemTextRect(const QFontMetrics &fm, const QRect &r,
  //      int flags, bool enabled, const QString &text) const
  QRect itemTextRect(
      const QFontMetrics &fm,
      const QRect &r,
      int flags,
      bool enabled,
      const QString &text) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQCommonStyleCall17 call = reinterpret_cast<CuteQCommonStyleCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQCommonStyleCall18 call = reinterpret_cast<CuteQCommonStyleCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQCommonStyleCall19 call = reinterpret_cast<CuteQCommonStyleCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQCommonStyleCall20 call = reinterpret_cast<CuteQCommonStyleCall20>(taken[20]);
      call(this, painter, &rect, alignment, &pixmap, &handled);
      if (handled) return;
    }
    QStyle::drawItemPixmap(painter, rect, alignment, pixmap);
  }

  //  QPalette QStyle::standardPalette() const
  QPalette standardPalette() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQCommonStyleCall21 call = reinterpret_cast<CuteQCommonStyleCall21>(taken[21]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QStyle::standardPalette();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQCommonStyleCall22 call = reinterpret_cast<CuteQCommonStyleCall22>(taken[22]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQCommonStyleCall23 call = reinterpret_cast<CuteQCommonStyleCall23>(taken[23]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQCommonStyleCall24 call = reinterpret_cast<CuteQCommonStyleCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQCommonStyleCall25 call = reinterpret_cast<CuteQCommonStyleCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQCommonStyleCall26 call = reinterpret_cast<CuteQCommonStyleCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQCommonStyleCall27 call = reinterpret_cast<CuteQCommonStyleCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQCommonStyleCall28 call = reinterpret_cast<CuteQCommonStyleCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QCommonStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QCommonStyle10metaObjectEv(
    const QCommonStyle *self) {
  return self->metaObject();
}

//  QString QCommonStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QCommonStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCommonStyle::tr(s, c, n));
}

//  QCommonStyle::QCommonStyle()
extern "C" Q_DECL_EXPORT
QCommonStyle *ritual_ZN12QCommonStyleC1Ev() {
  return new CuteQCommonStyle();
}

//  QCommonStyle::~QCommonStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCommonStyleD1Ev(QCommonStyle *self) {
  delete self;
}

//  void QCommonStyle::drawPrimitive(PrimitiveElement pe, const QStyleOption
//      *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QCommonStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QCommonStyle *self,
    QStyle::PrimitiveElement pe,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawPrimitive(pe, opt, p, w);
}

//  void QCommonStyle::drawControl(ControlElement element, const QStyleOption
//      *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QCommonStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QCommonStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawControl(element, opt, p, w);
}

//  QRect QCommonStyle::subElementRect(SubElement r, const QStyleOption *opt,
//      const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QCommonStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QCommonStyle *self,
    QStyle::SubElement r,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QRect(self->subElementRect(r, opt, widget));
}

//  void QCommonStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QCommonStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QCommonStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QPainter *p,
    const QWidget *w) {
  self->drawComplexControl(cc, opt, p, w);
}

//  SubControl QCommonStyle::hitTestComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, const QPoint &pt, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_ZNK12QCommonStyle21hitTestComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QCommonStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    const QPoint *pt,
    const QWidget *w) {
  return self->hitTestComplexControl(cc, opt, *pt, w);
}

//  QRect QCommonStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QCommonStyle14subControlRectEN6QStyle14ComplexControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget(
    const QCommonStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QStyle::SubControl sc,
    const QWidget *w) {
  return new QRect(self->subControlRect(cc, opt, sc, w));
}

//  QSize QCommonStyle::sizeFromContents(ContentsType ct, const QStyleOption
//      *opt, const QSize &contentsSize, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QCommonStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QCommonStyle *self,
    QStyle::ContentsType ct,
    const QStyleOption *opt,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(self->sizeFromContents(ct, opt, *contentsSize, widget));
}

//  int QCommonStyle::pixelMetric(PixelMetric m, const QStyleOption *opt,
//      const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QCommonStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QCommonStyle *self,
    QStyle::PixelMetric m,
    const QStyleOption *opt,
    const QWidget *widget) {
  return self->pixelMetric(m, opt, widget);
}

//  int QCommonStyle::styleHint(StyleHint sh, const QStyleOption *opt, const
//      QWidget *w, QStyleHintReturn *shret) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QCommonStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QCommonStyle *self,
    QStyle::StyleHint sh,
    const QStyleOption *opt,
    const QWidget *w,
    QStyleHintReturn *shret) {
  return self->styleHint(sh, opt, w, shret);
}

//  QIcon QCommonStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK12QCommonStyle12standardIconEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QCommonStyle *self,
    QStyle::StandardPixmap standardIcon,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QIcon(self->standardIcon(standardIcon, opt, widget));
}

//  QPixmap QCommonStyle::standardPixmap(StandardPixmap sp, const
//      QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK12QCommonStyle14standardPixmapEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QCommonStyle *self,
    QStyle::StandardPixmap sp,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QPixmap(self->standardPixmap(sp, opt, widget));
}

//  QPixmap QCommonStyle::generatedIconPixmap(QIcon::Mode iconMode, const
//      QPixmap &pixmap, const QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK12QCommonStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption(
    const QCommonStyle *self,
    QIcon::Mode iconMode,
    const QPixmap *pixmap,
    const QStyleOption *opt) {
  return new QPixmap(self->generatedIconPixmap(iconMode, *pixmap, opt));
}

//  int QCommonStyle::layoutSpacing(QSizePolicy::ControlType control1,
//      QSizePolicy::ControlType control2, Qt::Orientation orientation, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QCommonStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget(
    const QCommonStyle *self,
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

//  void QCommonStyle::polish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCommonStyle6polishEP12QApplication(
    QCommonStyle *self,
    QApplication *app) {
  self->polish(app);
}

//  void QCommonStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCommonStyle6polishEP7QWidget(
    QCommonStyle *self,
    QWidget *widget) {
  self->polish(widget);
}

//  void QCommonStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCommonStyle8unpolishEP7QWidget(
    QCommonStyle *self,
    QWidget *widget) {
  self->unpolish(widget);
}

//  void QCommonStyle::unpolish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCommonStyle8unpolishEP12QApplication(
    QCommonStyle *self,
    QApplication *application) {
  self->unpolish(application);
}

//  a Python function taken by a CuteQCommonStyle, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCommonStyle(
    QCommonStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCommonStyle *>(self)->take(key, call);
}

//  void QCommonStyle::drawPrimitive(PrimitiveElement pe, const QStyleOption
//      *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QCommonStyle13drawPrimitiveEN6QStyle16PrimitiveElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QCommonStyle *self,
    QStyle::PrimitiveElement pe,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->QCommonStyle::drawPrimitive(pe, opt, p, w);
}

//  void QCommonStyle::drawControl(ControlElement element, const QStyleOption
//      *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QCommonStyle11drawControlEN6QStyle14ControlElementEPK12QStyleOptionP8QPainterPK7QWidget(
    const QCommonStyle *self,
    QStyle::ControlElement element,
    const QStyleOption *opt,
    QPainter *p,
    const QWidget *w) {
  self->QCommonStyle::drawControl(element, opt, p, w);
}

//  QRect QCommonStyle::subElementRect(SubElement r, const QStyleOption *opt,
//      const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK12QCommonStyle14subElementRectEN6QStyle10SubElementEPK12QStyleOptionPK7QWidget(
    const QCommonStyle *self,
    QStyle::SubElement r,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QRect(self->QCommonStyle::subElementRect(r, opt, widget));
}

//  void QCommonStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, QPainter *p, const QWidget *w) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QCommonStyle18drawComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexP8QPainterPK7QWidget(
    const QCommonStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QPainter *p,
    const QWidget *w) {
  self->QCommonStyle::drawComplexControl(cc, opt, p, w);
}

//  SubControl QCommonStyle::hitTestComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, const QPoint &pt, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_own_ZNK12QCommonStyle21hitTestComplexControlEN6QStyle14ComplexControlEPK19QStyleOptionComplexRK6QPointPK7QWidget(
    const QCommonStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    const QPoint *pt,
    const QWidget *w) {
  return self->QCommonStyle::hitTestComplexControl(cc, opt, *pt, w);
}

//  QRect QCommonStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *opt, SubControl sc, const QWidget *w) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK12QCommonStyle14subControlRectEN6QStyle14ComplexControlEPK19QStyleOptionComplexNS0_10SubControlEPK7QWidget(
    const QCommonStyle *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt,
    QStyle::SubControl sc,
    const QWidget *w) {
  return new QRect(self->QCommonStyle::subControlRect(cc, opt, sc, w));
}

//  QSize QCommonStyle::sizeFromContents(ContentsType ct, const QStyleOption
//      *opt, const QSize &contentsSize, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QCommonStyle16sizeFromContentsEN6QStyle12ContentsTypeEPK12QStyleOptionRK5QSizePK7QWidget(
    const QCommonStyle *self,
    QStyle::ContentsType ct,
    const QStyleOption *opt,
    const QSize *contentsSize,
    const QWidget *widget) {
  return new QSize(
      self->QCommonStyle::sizeFromContents(
          ct,
          opt,
          *contentsSize,
          widget));
}

//  int QCommonStyle::pixelMetric(PixelMetric m, const QStyleOption *opt,
//      const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QCommonStyle11pixelMetricEN6QStyle11PixelMetricEPK12QStyleOptionPK7QWidget(
    const QCommonStyle *self,
    QStyle::PixelMetric m,
    const QStyleOption *opt,
    const QWidget *widget) {
  return self->QCommonStyle::pixelMetric(m, opt, widget);
}

//  int QCommonStyle::styleHint(StyleHint sh, const QStyleOption *opt, const
//      QWidget *w, QStyleHintReturn *shret) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QCommonStyle9styleHintEN6QStyle9StyleHintEPK12QStyleOptionPK7QWidgetP16QStyleHintReturn(
    const QCommonStyle *self,
    QStyle::StyleHint sh,
    const QStyleOption *opt,
    const QWidget *w,
    QStyleHintReturn *shret) {
  return self->QCommonStyle::styleHint(sh, opt, w, shret);
}

//  QIcon QCommonStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK12QCommonStyle12standardIconEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QCommonStyle *self,
    QStyle::StandardPixmap standardIcon,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QIcon(
      self->QCommonStyle::standardIcon(
          standardIcon,
          opt,
          widget));
}

//  QPixmap QCommonStyle::standardPixmap(StandardPixmap sp, const
//      QStyleOption *opt, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK12QCommonStyle14standardPixmapEN6QStyle14StandardPixmapEPK12QStyleOptionPK7QWidget(
    const QCommonStyle *self,
    QStyle::StandardPixmap sp,
    const QStyleOption *opt,
    const QWidget *widget) {
  return new QPixmap(self->QCommonStyle::standardPixmap(sp, opt, widget));
}

//  QPixmap QCommonStyle::generatedIconPixmap(QIcon::Mode iconMode, const
//      QPixmap &pixmap, const QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK12QCommonStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPK12QStyleOption(
    const QCommonStyle *self,
    QIcon::Mode iconMode,
    const QPixmap *pixmap,
    const QStyleOption *opt) {
  return new QPixmap(
      self->QCommonStyle::generatedIconPixmap(
          iconMode,
          *pixmap,
          opt));
}

//  int QCommonStyle::layoutSpacing(QSizePolicy::ControlType control1,
//      QSizePolicy::ControlType control2, Qt::Orientation orientation, const
//      QStyleOption *option, const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QCommonStyle13layoutSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationEPK12QStyleOptionPK7QWidget(
    const QCommonStyle *self,
    QSizePolicy::ControlType control1,
    QSizePolicy::ControlType control2,
    Qt::Orientation orientation,
    const QStyleOption *option,
    const QWidget *widget) {
  return self->QCommonStyle::layoutSpacing(
      control1,
      control2,
      orientation,
      option,
      widget);
}

//  void QCommonStyle::polish(QApplication *app)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QCommonStyle6polishEP12QApplication(
    QCommonStyle *self,
    QApplication *app) {
  self->QCommonStyle::polish(app);
}

//  void QCommonStyle::polish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QCommonStyle6polishEP7QWidget(
    QCommonStyle *self,
    QWidget *widget) {
  self->QCommonStyle::polish(widget);
}

//  void QCommonStyle::unpolish(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QCommonStyle8unpolishEP7QWidget(
    QCommonStyle *self,
    QWidget *widget) {
  self->QCommonStyle::unpolish(widget);
}

//  void QCommonStyle::unpolish(QApplication *application)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QCommonStyle8unpolishEP12QApplication(
    QCommonStyle *self,
    QApplication *application) {
  self->QCommonStyle::unpolish(application);
}
