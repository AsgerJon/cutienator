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

//  const QMetaObject *QStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QStyle10metaObjectEv(const QStyle *self) {
  return self->metaObject();
}

//  QString QStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QStyle2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QStyle::tr(s, c, n));
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
