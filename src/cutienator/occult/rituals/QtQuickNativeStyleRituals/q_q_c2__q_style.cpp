//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyle_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25:
//  the includes stand under the '#if' now, as Qt's Linux kit lacks
//  the header, and the header is included by its own path with no
//  module header of QtQuickNativeStyle before it. Qt builds the
//  class for macOS and Windows only. Qt does not export the class
//  and defines its constructors in its library, so the Cute class,
//  'take' and 'qt_metacast' are gone; what is left are the inline
//  functions and the virtual functions called through the object.
//  The two 'own_' rituals stay, as 'polish' and 'handleThemeChange'
//  are inline. Qt's library offers no function 'QQC2::QStyle::...'
//  for the others, so they have no 'own_' ritual.
//  Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyle_p.h>
#include <QtGui/qfontmetrics.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>
#include <QtGui/qfont.h>
#include <QtCore/qmargins.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <QtGui/qicon.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *QQC2::QStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK4QQC26QStyle10metaObjectEv(
    const QQC2::QStyle *self) {
  return self->metaObject();
}

//  QStylePrivate *QQC2::QStyle::d_func()
extern "C" Q_DECL_EXPORT
QQC2::QStylePrivate *ritual_ZN4QQC26QStyle6d_funcEv(QQC2::QStyle *self) {
  return self->d_func();
}

//  const QStylePrivate *QQC2::QStyle::d_func() const
extern "C" Q_DECL_EXPORT
const QQC2::QStylePrivate *ritual_ZNK4QQC26QStyle6d_funcEv(
    const QQC2::QStyle *self) {
  return self->d_func();
}

//  QQC2::QStyle::~QStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC26QStyleD1Ev(QQC2::QStyle *self) {
  delete self;
}

//  QRect QQC2::QStyle::itemTextRect(const QFontMetrics &fm, const QRect &r,
//      int flags, bool enabled, const QString &text) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK4QQC26QStyle12itemTextRectERK12QFontMetricsRK5QRectibRK7QString(
    const QQC2::QStyle *self,
    const QFontMetrics *fm,
    const QRect *r,
    int flags,
    bool enabled,
    const QString *text) {
  return new QRect(self->itemTextRect(*fm, *r, flags, enabled, *text));
}

//  QRect QQC2::QStyle::itemPixmapRect(const QRect &r, int flags, const
//      QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK4QQC26QStyle14itemPixmapRectERK5QRectiRK7QPixmap(
    const QQC2::QStyle *self,
    const QRect *r,
    int flags,
    const QPixmap *pixmap) {
  return new QRect(self->itemPixmapRect(*r, flags, *pixmap));
}

//  QRect QQC2::QStyle::subElementRect(SubElement subElement, const
//      QStyleOption *option) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK4QQC26QStyle14subElementRectENS0_10SubElementEPKNS_12QStyleOptionE(
    const QQC2::QStyle *self,
    QQC2::QStyle::SubElement subElement,
    const QQC2::QStyleOption *option) {
  return new QRect(self->subElementRect(subElement, option));
}

//  QRect QQC2::QStyle::subControlRect(ComplexControl cc, const
//      QStyleOptionComplex *opt, SubControl sc) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK4QQC26QStyle14subControlRectENS0_14ComplexControlEPKNS_19QStyleOptionComplexENS0_10SubControlE(
    const QQC2::QStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *opt,
    QQC2::QStyle::SubControl sc) {
  return new QRect(self->subControlRect(cc, opt, sc));
}

//  QSize QQC2::QStyle::sizeFromContents(ContentsType ct, const QStyleOption
//      *opt, const QSize &contentsSize) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK4QQC26QStyle16sizeFromContentsENS0_12ContentsTypeEPKNS_12QStyleOptionERK5QSize(
    const QQC2::QStyle *self,
    QQC2::QStyle::ContentsType ct,
    const QQC2::QStyleOption *opt,
    const QSize *contentsSize) {
  return new QSize(self->sizeFromContents(ct, opt, *contentsSize));
}

//  QFont QQC2::QStyle::font(ControlElement element, const QStyle::State
//      state) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK4QQC26QStyle4fontENS0_14ControlElementE6QFlagsINS0_9StateFlagEE(
    const QQC2::QStyle *self,
    QQC2::QStyle::ControlElement element,
    int state) {
  return new QFont(
      self->font(
          element,
          QFlags<QQC2::QStyle::StateFlag>::fromInt(state)));
}

//  QMargins QQC2::QStyle::ninePatchMargins(ControlElement ce, const
//      QStyleOption *opt, const QSize &imageSize) const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK4QQC26QStyle16ninePatchMarginsENS0_14ControlElementEPKNS_12QStyleOptionERK5QSize(
    const QQC2::QStyle *self,
    QQC2::QStyle::ControlElement ce,
    const QQC2::QStyleOption *opt,
    const QSize *imageSize) {
  return new QMargins(self->ninePatchMargins(ce, opt, *imageSize));
}

//  QMargins QQC2::QStyle::ninePatchMargins(ComplexControl cc, const
//      QStyleOptionComplex *opt, const QSize &imageSize) const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK4QQC26QStyle16ninePatchMarginsENS0_14ComplexControlEPKNS_19QStyleOptionComplexERK5QSize(
    const QQC2::QStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *opt,
    const QSize *imageSize) {
  return new QMargins(self->ninePatchMargins(cc, opt, *imageSize));
}

//  SubControl QQC2::QStyle::hitTestComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, const QPoint &pt) const
extern "C" Q_DECL_EXPORT
QQC2::QStyle::SubControl ritual_ZNK4QQC26QStyle21hitTestComplexControlENS0_14ComplexControlEPKNS_19QStyleOptionComplexERK6QPoint(
    const QQC2::QStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *opt,
    const QPoint *pt) {
  return self->hitTestComplexControl(cc, opt, *pt);
}

//  int QQC2::QStyle::pixelMetric(PixelMetric metric, const QStyleOption
//      *option) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QQC26QStyle11pixelMetricENS0_11PixelMetricEPKNS_12QStyleOptionE(
    const QQC2::QStyle *self,
    QQC2::QStyle::PixelMetric metric,
    const QQC2::QStyleOption *option) {
  return self->pixelMetric(metric, option);
}

//  int QQC2::QStyle::styleHint(StyleHint stylehint, const QStyleOption *opt,
//      QStyleHintReturn *returnData) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QQC26QStyle9styleHintENS0_9StyleHintEPKNS_12QStyleOptionEPNS_16QStyleHintReturnE(
    const QQC2::QStyle *self,
    QQC2::QStyle::StyleHint stylehint,
    const QQC2::QStyleOption *opt,
    QQC2::QStyleHintReturn *returnData) {
  return self->styleHint(stylehint, opt, returnData);
}

//  void QQC2::QStyle::drawItemText(QPainter *painter, const QRect &rect, int
//      flags, const QPalette &pal, bool enabled, const QString &text,
//      QPalette::ColorRole textRole) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC26QStyle12drawItemTextEP8QPainterRK5QRectiRK8QPalettebRK7QStringNS6_9ColorRoleE(
    const QQC2::QStyle *self,
    QPainter *painter,
    const QRect *rect,
    int flags,
    const QPalette *pal,
    bool enabled,
    const QString *text,
    QPalette::ColorRole textRole) {
  self->drawItemText(painter, *rect, flags, *pal, enabled, *text, textRole);
}

//  void QQC2::QStyle::drawItemPixmap(QPainter *painter, const QRect &rect,
//      int alignment, const QPixmap &pixmap) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC26QStyle14drawItemPixmapEP8QPainterRK5QRectiRK7QPixmap(
    const QQC2::QStyle *self,
    QPainter *painter,
    const QRect *rect,
    int alignment,
    const QPixmap *pixmap) {
  self->drawItemPixmap(painter, *rect, alignment, *pixmap);
}

//  void QQC2::QStyle::drawPrimitive(PrimitiveElement pe, const QStyleOption
//      *opt, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC26QStyle13drawPrimitiveENS0_16PrimitiveElementEPKNS_12QStyleOptionEP8QPainter(
    const QQC2::QStyle *self,
    QQC2::QStyle::PrimitiveElement pe,
    const QQC2::QStyleOption *opt,
    QPainter *p) {
  self->drawPrimitive(pe, opt, p);
}

//  void QQC2::QStyle::drawControl(ControlElement element, const QStyleOption
//      *opt, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC26QStyle11drawControlENS0_14ControlElementEPKNS_12QStyleOptionEP8QPainter(
    const QQC2::QStyle *self,
    QQC2::QStyle::ControlElement element,
    const QQC2::QStyleOption *opt,
    QPainter *p) {
  self->drawControl(element, opt, p);
}

//  void QQC2::QStyle::drawComplexControl(ComplexControl cc, const
//      QStyleOptionComplex *opt, QPainter *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC26QStyle18drawComplexControlENS0_14ComplexControlEPKNS_19QStyleOptionComplexEP8QPainter(
    const QQC2::QStyle *self,
    QQC2::QStyle::ComplexControl cc,
    const QQC2::QStyleOptionComplex *opt,
    QPainter *p) {
  self->drawComplexControl(cc, opt, p);
}

//  QPalette QQC2::QStyle::standardPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK4QQC26QStyle15standardPaletteEv(
    const QQC2::QStyle *self) {
  return new QPalette(self->standardPalette());
}

//  QPixmap QQC2::QStyle::standardPixmap(StandardPixmap standardPixmap, const
//      QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK4QQC26QStyle14standardPixmapENS0_14StandardPixmapEPKNS_12QStyleOptionE(
    const QQC2::QStyle *self,
    QQC2::QStyle::StandardPixmap standardPixmap,
    const QQC2::QStyleOption *opt) {
  return new QPixmap(self->standardPixmap(standardPixmap, opt));
}

//  QIcon QQC2::QStyle::standardIcon(StandardPixmap standardIcon, const
//      QStyleOption *option) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK4QQC26QStyle12standardIconENS0_14StandardPixmapEPKNS_12QStyleOptionE(
    const QQC2::QStyle *self,
    QQC2::QStyle::StandardPixmap standardIcon,
    const QQC2::QStyleOption *option) {
  return new QIcon(self->standardIcon(standardIcon, option));
}

//  QPixmap QQC2::QStyle::generatedIconPixmap(QIcon::Mode iconMode, const
//      QPixmap &pixmap, const QStyleOption *opt) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK4QQC26QStyle19generatedIconPixmapEN5QIcon4ModeERK7QPixmapPKNS_12QStyleOptionE(
    const QQC2::QStyle *self,
    QIcon::Mode iconMode,
    const QPixmap *pixmap,
    const QQC2::QStyleOption *opt) {
  return new QPixmap(self->generatedIconPixmap(iconMode, *pixmap, opt));
}

//  void QQC2::QStyle::polish()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC26QStyle6polishEv(QQC2::QStyle *self) {
  self->polish();
}

//  const QStyle *QQC2::QStyle::proxy() const
extern "C" Q_DECL_EXPORT
const QQC2::QStyle *ritual_ZNK4QQC26QStyle5proxyEv(
    const QQC2::QStyle *self) {
  return self->proxy();
}

//  void QQC2::QStyle::handleThemeChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC26QStyle17handleThemeChangeEv(QQC2::QStyle *self) {
  self->handleThemeChange();
}

//  void QQC2::QStyle::polish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN4QQC26QStyle6polishEv(QQC2::QStyle *self) {
  self->QQC2::QStyle::polish();
}

//  void QQC2::QStyle::handleThemeChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN4QQC26QStyle17handleThemeChangeEv(QQC2::QStyle *self) {
  self->QQC2::QStyle::handleThemeChange();
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
