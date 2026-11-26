//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsxpstyle_p.h,
//  Qt 6.12.0, as the Qt of Windows installs it. Edited from the
//  file the generator wrote, which gave the class a Cute class and
//  rituals for its constructor and 'tr'. Kept as it is when the
//  generator runs again.
//  Qt does not export this class: only its virtual functions are called,
//  through the object, and its inline functions. Not written: the
//  constructors, 'tr'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsxpstyle_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>
#include <QtGui/qfont.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qpalette.h>
#include <QtGui/qicon.h>
#include <QtGui/qpainter.h>

//  const QMetaObject *QQC2::QWindowsXPStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK4QQC215QWindowsXPStyle10metaObjectEv(
    const QQC2::QWindowsXPStyle *self) {
  return self->metaObject();
}

//  QQC2::QWindowsXPStyle::~QWindowsXPStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC215QWindowsXPStyleD1Ev(
    QQC2::QWindowsXPStyle *self) {
  delete self;
}

//  QQC2::QWindowsXPStylePrivate *QQC2::QWindowsXPStyle::d_func()
extern "C" Q_DECL_EXPORT
QQC2::QWindowsXPStylePrivate *ritual_ZN4QQC215QWindowsXPStyle6d_funcEv(
    QQC2::QWindowsXPStyle *self) {
  return self->d_func();
}

//  const QQC2::QWindowsXPStylePrivate *QQC2::QWindowsXPStyle::d_func() const
extern "C" Q_DECL_EXPORT
const QQC2::QWindowsXPStylePrivate *ritual_ZNK4QQC215QWindowsXPStyle6d_funcEv(
    const QQC2::QWindowsXPStyle *self) {
  return self->d_func();
}

//  void QQC2::QWindowsXPStyle::drawPrimitive(PrimitiveElement pe, const
//      QStyleOption *option, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC215QWindowsXPStyle13drawPrimitiveENS_6QStyle16PrimitiveElementEPKNS_12QStyleOptionEP8QPainter(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::PrimitiveElement pe,
    const QQC2::QStyleOption *option,
    QPainter *p) {
  self->drawPrimitive(pe, option, p);
}

//  void QQC2::QWindowsXPStyle::drawControl(ControlElement element, const
//      QStyleOption *option, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC215QWindowsXPStyle11drawControlENS_6QStyle14ControlElementEPKNS_12QStyleOptionEP8QPainter(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::ControlElement element,
    const QQC2::QStyleOption *option,
    QPainter *p) {
  self->drawControl(element, option, p);
}

//  QRect QQC2::QWindowsXPStyle::subElementRect(SubElement r, const
//      QStyleOption *option) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK4QQC215QWindowsXPStyle14subElementRectENS_6QStyle10SubElementEPKNS_12QStyleOptionE(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::SubElement r,
    const QQC2::QStyleOption *option) {
  return new QRect(self->subElementRect(r, option));
}

//  QRect QQC2::QWindowsXPStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *option, SubControl sc) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK4QQC215QWindowsXPStyle14subControlRectENS_6QStyle14ComplexControlEPKNS_19QStyleOptionComplexENS1_10SubControlE(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *option,
    QQC2::QStyle::SubControl sc) {
  return new QRect(
      self->subControlRect(
          cc,
          option,
          sc));
}

//  void QQC2::QWindowsXPStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *option, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC215QWindowsXPStyle18drawComplexControlENS_6QStyle14ComplexControlEPKNS_19QStyleOptionComplexEP8QPainter(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *option,
    QPainter *p) {
  self->drawComplexControl(cc, option, p);
}

//  QSize QQC2::QWindowsXPStyle::sizeFromContents(ContentsType ct, const
//      QStyleOption *option, const QSize &contentsSize) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK4QQC215QWindowsXPStyle16sizeFromContentsENS_6QStyle12ContentsTypeEPKNS_12QStyleOptionERK5QSize(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::ContentsType ct,
    const QQC2::QStyleOption *option,
    const QSize *contentsSize) {
  return new QSize(
      self->sizeFromContents(
          ct,
          option,
          *contentsSize));
}

//  int QQC2::QWindowsXPStyle::pixelMetric(PixelMetric pm, const QStyleOption
//      *option) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QQC215QWindowsXPStyle11pixelMetricENS_6QStyle11PixelMetricEPKNS_12QStyleOptionE(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::PixelMetric pm,
    const QQC2::QStyleOption *option) {
  return self->pixelMetric(pm, option);
}

//  int QQC2::QWindowsXPStyle::styleHint(StyleHint hint, const QStyleOption
//      *option, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QQC215QWindowsXPStyle9styleHintENS_6QStyle9StyleHintEPKNS_12QStyleOptionEPNS_16QStyleHintReturnE(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::StyleHint hint,
    const QQC2::QStyleOption *option,
    QQC2::QStyleHintReturn *returnData) {
  return self->styleHint(hint, option, returnData);
}

//  QPalette QQC2::QWindowsXPStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK4QQC215QWindowsXPStyle15standardPaletteEv(
    const QQC2::QWindowsXPStyle *self) {
  return new QPalette(self->standardPalette());
}

//  QPixmap QQC2::QWindowsXPStyle::standardPixmap(StandardPixmap
//      standardIcon, const QStyleOption *option) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK4QQC215QWindowsXPStyle14standardPixmapENS_6QStyle14StandardPixmapEPKNS_12QStyleOptionE(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::StandardPixmap standardIcon,
    const QQC2::QStyleOption *option) {
  return new QPixmap(
      self->standardPixmap(
          standardIcon,
          option));
}

//  QIcon QQC2::QWindowsXPStyle::standardIcon(StandardPixmap standardIcon,
//      const QStyleOption *option) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK4QQC215QWindowsXPStyle12standardIconENS_6QStyle14StandardPixmapEPKNS_12QStyleOptionE(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::StandardPixmap standardIcon,
    const QQC2::QStyleOption *option) {
  return new QIcon(
      self->standardIcon(
          standardIcon,
          option));
}

//  QMargins QQC2::QWindowsXPStyle::ninePatchMargins(QQC2::QStyle::ComplexControl
//      cc, const QStyleOptionComplex *opt, const QSize &imageSize) const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK4QQC215QWindowsXPStyle16ninePatchMarginsENS_6QStyle14ComplexControlEPKNS_19QStyleOptionComplexERK5QSize(
    const QQC2::QWindowsXPStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *opt,
    const QSize *imageSize) {
  return new QMargins(
      self->ninePatchMargins(
          cc,
          opt,
          *imageSize));
}

#endif  // defined(Q_OS_WIN)
