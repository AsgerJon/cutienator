//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsstyle_p.h,
//  Qt 6.12.0, as the Qt of Windows installs it. Edited from the
//  file the generator wrote, which gave the class a Cute class and
//  rituals for its constructor and 'tr'. Kept as it is when the
//  generator runs again.
//  Qt does not export this class: only its virtual functions are called,
//  through the object, and its inline functions. Not written: the
//  constructors, 'refreshPalette', 'tr'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsstyle_p.h>
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

//  const QMetaObject *QQC2::QWindowsStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK4QQC213QWindowsStyle10metaObjectEv(
    const QQC2::QWindowsStyle *self) {
  return self->metaObject();
}

//  QQC2::QWindowsStyle::~QWindowsStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC213QWindowsStyleD1Ev(
    QQC2::QWindowsStyle *self) {
  delete self;
}

//  QQC2::QWindowsStylePrivate *QQC2::QWindowsStyle::d_func()
extern "C" Q_DECL_EXPORT
QQC2::QWindowsStylePrivate *ritual_ZN4QQC213QWindowsStyle6d_funcEv(
    QQC2::QWindowsStyle *self) {
  return self->d_func();
}

//  const QQC2::QWindowsStylePrivate *QQC2::QWindowsStyle::d_func() const
extern "C" Q_DECL_EXPORT
const QQC2::QWindowsStylePrivate *ritual_ZNK4QQC213QWindowsStyle6d_funcEv(
    const QQC2::QWindowsStyle *self) {
  return self->d_func();
}

//  void QQC2::QWindowsStyle::drawPrimitive(PrimitiveElement pe, const
//      QStyleOption *opt, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC213QWindowsStyle13drawPrimitiveENS_6QStyle16PrimitiveElementEPKNS_12QStyleOptionEP8QPainter(
    const QQC2::QWindowsStyle *self,
    QQC2::QStyle::PrimitiveElement pe,
    const QQC2::QStyleOption *opt,
    QPainter *p) {
  self->drawPrimitive(pe, opt, p);
}

//  void QQC2::QWindowsStyle::drawControl(ControlElement element, const
//      QStyleOption *opt, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC213QWindowsStyle11drawControlENS_6QStyle14ControlElementEPKNS_12QStyleOptionEP8QPainter(
    const QQC2::QWindowsStyle *self,
    QQC2::QStyle::ControlElement element,
    const QQC2::QStyleOption *opt,
    QPainter *p) {
  self->drawControl(element, opt, p);
}

//  void QQC2::QWindowsStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC213QWindowsStyle18drawComplexControlENS_6QStyle14ComplexControlEPKNS_19QStyleOptionComplexEP8QPainter(
    const QQC2::QWindowsStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *opt,
    QPainter *p) {
  self->drawComplexControl(cc, opt, p);
}

//  QRect QQC2::QWindowsStyle::subElementRect(SubElement r, const
//      QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK4QQC213QWindowsStyle14subElementRectENS_6QStyle10SubElementEPKNS_12QStyleOptionE(
    const QQC2::QWindowsStyle *self,
    QQC2::QStyle::SubElement r,
    const QQC2::QStyleOption *opt) {
  return new QRect(self->subElementRect(r, opt));
}

//  QSize QQC2::QWindowsStyle::sizeFromContents(ContentsType ct, const
//      QStyleOption *opt, const QSize &contentsSize) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK4QQC213QWindowsStyle16sizeFromContentsENS_6QStyle12ContentsTypeEPKNS_12QStyleOptionERK5QSize(
    const QQC2::QWindowsStyle *self,
    QQC2::QStyle::ContentsType ct,
    const QQC2::QStyleOption *opt,
    const QSize *contentsSize) {
  return new QSize(
      self->sizeFromContents(
          ct,
          opt,
          *contentsSize));
}

//  int QQC2::QWindowsStyle::pixelMetric(PixelMetric pm, const QStyleOption
//      *option) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QQC213QWindowsStyle11pixelMetricENS_6QStyle11PixelMetricEPKNS_12QStyleOptionE(
    const QQC2::QWindowsStyle *self,
    QQC2::QStyle::PixelMetric pm,
    const QQC2::QStyleOption *option) {
  return self->pixelMetric(pm, option);
}

//  int QQC2::QWindowsStyle::styleHint(StyleHint hint, const QStyleOption
//      *opt, QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QQC213QWindowsStyle9styleHintENS_6QStyle9StyleHintEPKNS_12QStyleOptionEPNS_16QStyleHintReturnE(
    const QQC2::QWindowsStyle *self,
    QQC2::QStyle::StyleHint hint,
    const QQC2::QStyleOption *opt,
    QQC2::QStyleHintReturn *returnData) {
  return self->styleHint(hint, opt, returnData);
}

//  QPixmap QQC2::QWindowsStyle::standardPixmap(StandardPixmap
//      standardPixmap, const QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK4QQC213QWindowsStyle14standardPixmapENS_6QStyle14StandardPixmapEPKNS_12QStyleOptionE(
    const QQC2::QWindowsStyle *self,
    QQC2::QStyle::StandardPixmap standardPixmap,
    const QQC2::QStyleOption *opt) {
  return new QPixmap(
      self->standardPixmap(
          standardPixmap,
          opt));
}

//  QIcon QQC2::QWindowsStyle::standardIcon(StandardPixmap standardIcon,
//      const QStyleOption *option) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK4QQC213QWindowsStyle12standardIconENS_6QStyle14StandardPixmapEPKNS_12QStyleOptionE(
    const QQC2::QWindowsStyle *self,
    QQC2::QStyle::StandardPixmap standardIcon,
    const QQC2::QStyleOption *option) {
  return new QIcon(
      self->standardIcon(
          standardIcon,
          option));
}

//  void QQC2::QWindowsStyle::polish()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC213QWindowsStyle6polishEv(QQC2::QWindowsStyle *self) {
  self->polish();
}

//  void QQC2::QWindowsStyle::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC213QWindowsStyle10timerEventEP11QTimerEvent(
    QQC2::QWindowsStyle *self,
    QTimerEvent *event) {
  self->timerEvent(
      event);
}

#endif  // defined(Q_OS_WIN)
