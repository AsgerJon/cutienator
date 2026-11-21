//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcommonstyle.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcommonstyle.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qicon.h>
#include <QtGui/qpixmap.h>

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
  return new QCommonStyle();
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
