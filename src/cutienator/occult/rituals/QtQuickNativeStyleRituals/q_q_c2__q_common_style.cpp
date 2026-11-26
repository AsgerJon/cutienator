//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qcommonstyle_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it (Qt
//  builds the part for those two only). Kept as it is when the
//  generator runs again.
//  Qt does not export this class: only its virtual functions are
//  called, through the object, and its inline functions.
//  Not written: the constructors and 'tr'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qcommonstyle_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>
#include <QtGui/qfont.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qicon.h>
#include <QtGui/qpainter.h>

//  const QMetaObject *QQC2::QCommonStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK4QQC212QCommonStyle10metaObjectEv(
    const QQC2::QCommonStyle *self) {
  return self->metaObject();
}

//  QQC2::QCommonStyle::~QCommonStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC212QCommonStyleD1Ev(
    QQC2::QCommonStyle *self) {
  delete self;
}

//  QQC2::QCommonStylePrivate *QQC2::QCommonStyle::d_func()
extern "C" Q_DECL_EXPORT
QQC2::QCommonStylePrivate *ritual_ZN4QQC212QCommonStyle6d_funcEv(QQC2::QCommonStyle *self) {
  return self->d_func();
}

//  const QQC2::QCommonStylePrivate *QQC2::QCommonStyle::d_func() const
extern "C" Q_DECL_EXPORT
const QQC2::QCommonStylePrivate *ritual_ZNK4QQC212QCommonStyle6d_funcEv(
    const QQC2::QCommonStyle *self) {
  return self->d_func();
}

//  void QQC2::QCommonStyle::drawPrimitive(PrimitiveElement pe, const
//      QStyleOption *opt, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC212QCommonStyle13drawPrimitiveENS_6QStyle16PrimitiveElementEPKNS_12QStyleOptionEP8QPainter(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::PrimitiveElement pe,
    const QQC2::QStyleOption *opt,
    QPainter *p) {
  self->drawPrimitive(pe, opt, p);
}

//  void QQC2::QCommonStyle::drawControl(ControlElement element, const
//      QStyleOption *opt, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC212QCommonStyle11drawControlENS_6QStyle14ControlElementEPKNS_12QStyleOptionEP8QPainter(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::ControlElement element,
    const QQC2::QStyleOption *opt,
    QPainter *p) {
  self->drawControl(element, opt, p);
}

//  void QQC2::QCommonStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC212QCommonStyle18drawComplexControlENS_6QStyle14ComplexControlEPKNS_19QStyleOptionComplexEP8QPainter(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *opt,
    QPainter *p) {
  self->drawComplexControl(cc, opt, p);
}

//  QRect QQC2::QCommonStyle::subElementRect(SubElement r, const QStyleOption
//      *opt) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK4QQC212QCommonStyle14subElementRectENS_6QStyle10SubElementEPKNS_12QStyleOptionE(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::SubElement r,
    const QQC2::QStyleOption *opt) {
  return new QRect(self->subElementRect(r, opt));
}

//  QRect QQC2::QCommonStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *opt, SubControl sc) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK4QQC212QCommonStyle14subControlRectENS_6QStyle14ComplexControlEPKNS_19QStyleOptionComplexENS1_10SubControlE(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *opt,
    QQC2::QStyle::SubControl sc) {
  return new QRect(self->subControlRect(cc, opt, sc));
}

//  SubControl QQC2::QCommonStyle::hitTestComplexControl(ComplexControl cc,
//      const QStyleOptionComplex *opt, const QPoint &pt) const
extern "C" Q_DECL_EXPORT
QQC2::QStyle::SubControl ritual_ZNK4QQC212QCommonStyle21hitTestComplexControlENS_6QStyle14ComplexControlEPKNS_19QStyleOptionComplexERK6QPoint(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *opt,
    const QPoint *pt) {
  return self->hitTestComplexControl(cc, opt, *pt);
}

//  QSize QQC2::QCommonStyle::sizeFromContents(ContentsType ct, const
//      QStyleOption *opt, const QSize &contentsSize) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK4QQC212QCommonStyle16sizeFromContentsENS_6QStyle12ContentsTypeEPKNS_12QStyleOptionERK5QSize(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::ContentsType ct,
    const QQC2::QStyleOption *opt,
    const QSize *contentsSize) {
  return new QSize(
      self->sizeFromContents(
          ct,
          opt,
          *contentsSize));
}

//  QFont QQC2::QCommonStyle::font(ControlElement element, const QQC2::QStyle::State
//      state) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK4QQC212QCommonStyle4fontENS_6QStyle14ControlElementE6QFlagsINS1_9StateFlagEE(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::ControlElement element,
    int state) {
  return new QFont(
      self->font(
          element,
          QFlags<QQC2::QStyle::StateFlag>::fromInt(state)));
}

//  QMargins QQC2::QCommonStyle::ninePatchMargins(ComplexControl cc, const
//      QStyleOptionComplex *opt, const QSize &imageSize) const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK4QQC212QCommonStyle16ninePatchMarginsENS_6QStyle14ComplexControlEPKNS_19QStyleOptionComplexERK5QSize(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *opt,
    const QSize *imageSize) {
  return new QMargins(
      self->ninePatchMargins(
          cc,
          opt,
          *imageSize));
}

//  QMargins QQC2::QCommonStyle::ninePatchMargins(ControlElement ce, const
//      QStyleOption *opt, const QSize &imageSize) const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK4QQC212QCommonStyle16ninePatchMarginsENS_6QStyle14ControlElementEPKNS_12QStyleOptionERK5QSize(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::ControlElement ce,
    const QQC2::QStyleOption *opt,
    const QSize *imageSize) {
  return new QMargins(self->ninePatchMargins(ce, opt, *imageSize));
}

//  int QQC2::QCommonStyle::pixelMetric(PixelMetric pm, const QStyleOption *opt)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QQC212QCommonStyle11pixelMetricENS_6QStyle11PixelMetricEPKNS_12QStyleOptionE(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::PixelMetric pm,
    const QQC2::QStyleOption *opt) {
  return self->pixelMetric(pm, opt);
}

//  int QQC2::QCommonStyle::styleHint(StyleHint sh, const QStyleOption *opt,
//      QStyleHintReturn *shret) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QQC212QCommonStyle9styleHintENS_6QStyle9StyleHintEPKNS_12QStyleOptionEPNS_16QStyleHintReturnE(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::StyleHint sh,
    const QQC2::QStyleOption *opt,
    QQC2::QStyleHintReturn *shret) {
  return self->styleHint(sh, opt, shret);
}

//  QPixmap QQC2::QCommonStyle::standardPixmap(StandardPixmap sp, const
//      QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK4QQC212QCommonStyle14standardPixmapENS_6QStyle14StandardPixmapEPKNS_12QStyleOptionE(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::StandardPixmap sp,
    const QQC2::QStyleOption *opt) {
  return new QPixmap(self->standardPixmap(sp, opt));
}

//  QPixmap QQC2::QCommonStyle::generatedIconPixmap(QIcon::Mode iconMode, const
//      QPixmap &pixmap, const QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK4QQC212QCommonStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPKNS_12QStyleOptionE(
    const QQC2::QCommonStyle *self,
    QIcon::Mode iconMode,
    const QPixmap *pixmap,
    const QQC2::QStyleOption *opt) {
  return new QPixmap(
      self->generatedIconPixmap(
          iconMode,
          *pixmap,
          opt));
}

//  QIcon QQC2::QCommonStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK4QQC212QCommonStyle12standardIconENS_6QStyle14StandardPixmapEPKNS_12QStyleOptionE(
    const QQC2::QCommonStyle *self,
    QQC2::QStyle::StandardPixmap standardIcon,
    const QQC2::QStyleOption *opt) {
  return new QIcon(self->standardIcon(standardIcon, opt));
}

#endif  // Qt builds it for macOS and Windows
