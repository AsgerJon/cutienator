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
  return new QProxyStyle(style);
}

//  QProxyStyle::QProxyStyle(const QString &key)
extern "C" Q_DECL_EXPORT
QProxyStyle *ritual_ZN11QProxyStyleC1ERK7QString(const QString *key) {
  return new QProxyStyle(*key);
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
