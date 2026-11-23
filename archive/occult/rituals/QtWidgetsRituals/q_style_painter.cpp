//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstylepainter.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>

//  QStylePainter::QStylePainter()
extern "C" Q_DECL_EXPORT
QStylePainter *ritual_ZN13QStylePainterC1Ev() {
  return new QStylePainter();
}

//  QStylePainter::QStylePainter(QWidget *w)
extern "C" Q_DECL_EXPORT
QStylePainter *ritual_ZN13QStylePainterC1EP7QWidget(QWidget *w) {
  return new QStylePainter(w);
}

//  QStylePainter::QStylePainter(QPaintDevice *pd, QWidget *w)
extern "C" Q_DECL_EXPORT
QStylePainter *ritual_ZN13QStylePainterC1EP12QPaintDeviceP7QWidget(
    QPaintDevice *pd,
    QWidget *w) {
  return new QStylePainter(pd, w);
}

//  bool QStylePainter::begin(QWidget *w)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QStylePainter5beginEP7QWidget(
    QStylePainter *self,
    QWidget *w) {
  return self->begin(w);
}

//  bool QStylePainter::begin(QPaintDevice *pd, QWidget *w)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QStylePainter5beginEP12QPaintDeviceP7QWidget(
    QStylePainter *self,
    QPaintDevice *pd,
    QWidget *w) {
  return self->begin(pd, w);
}

//  void QStylePainter::drawPrimitive(QStyle::PrimitiveElement pe, const
//      QStyleOption &opt)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStylePainter13drawPrimitiveEN6QStyle16PrimitiveElementERK12QStyleOption(
    QStylePainter *self,
    QStyle::PrimitiveElement pe,
    const QStyleOption *opt) {
  self->drawPrimitive(pe, *opt);
}

//  void QStylePainter::drawControl(QStyle::ControlElement ce, const
//      QStyleOption &opt)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStylePainter11drawControlEN6QStyle14ControlElementERK12QStyleOption(
    QStylePainter *self,
    QStyle::ControlElement ce,
    const QStyleOption *opt) {
  self->drawControl(ce, *opt);
}

//  void QStylePainter::drawComplexControl(QStyle::ComplexControl cc, const
//      QStyleOptionComplex &opt)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStylePainter18drawComplexControlEN6QStyle14ComplexControlERK19QStyleOptionComplex(
    QStylePainter *self,
    QStyle::ComplexControl cc,
    const QStyleOptionComplex *opt) {
  self->drawComplexControl(cc, *opt);
}

//  void QStylePainter::drawItemText(const QRect &r, int flags, const
//      QPalette &pal, bool enabled, const QString &text, QPalette::ColorRole
//      textRole)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStylePainter12drawItemTextERK5QRectiRK8QPalettebRK7QStringNS3_9ColorRoleE(
    QStylePainter *self,
    const QRect *r,
    int flags,
    const QPalette *pal,
    bool enabled,
    const QString *text,
    QPalette::ColorRole textRole) {
  self->drawItemText(*r, flags, *pal, enabled, *text, textRole);
}

//  void QStylePainter::drawItemPixmap(const QRect &r, int flags, const
//      QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStylePainter14drawItemPixmapERK5QRectiRK7QPixmap(
    QStylePainter *self,
    const QRect *r,
    int flags,
    const QPixmap *pixmap) {
  self->drawItemPixmap(*r, flags, *pixmap);
}

//  QStyle *QStylePainter::style() const
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZNK13QStylePainter5styleEv(const QStylePainter *self) {
  return self->style();
}
