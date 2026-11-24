//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicslayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicslayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QLayoutStyleInfo::QLayoutStyleInfo()
extern "C" Q_DECL_EXPORT
QLayoutStyleInfo *ritual_ZN16QLayoutStyleInfoC1Ev() {
  return new QLayoutStyleInfo();
}

//  QLayoutStyleInfo::QLayoutStyleInfo(QStyle *style, QWidget *widget)
extern "C" Q_DECL_EXPORT
QLayoutStyleInfo *ritual_ZN16QLayoutStyleInfoC1EP6QStyleP7QWidget(
    QStyle *style,
    QWidget *widget) {
  return new QLayoutStyleInfo(style, widget);
}

//  void QLayoutStyleInfo::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLayoutStyleInfo10invalidateEv(QLayoutStyleInfo *self) {
  self->invalidate();
}

//  QStyle *QLayoutStyleInfo::style() const
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZNK16QLayoutStyleInfo5styleEv(const QLayoutStyleInfo *self) {
  return self->style();
}

//  QWidget *QLayoutStyleInfo::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK16QLayoutStyleInfo6widgetEv(
    const QLayoutStyleInfo *self) {
  return self->widget();
}

//  bool QLayoutStyleInfo::operator==(const QLayoutStyleInfo &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLayoutStyleInfoeqERKS_(
    const QLayoutStyleInfo *self,
    const QLayoutStyleInfo *other) {
  return self->operator==(*other);
}

//  bool QLayoutStyleInfo::operator!=(const QLayoutStyleInfo &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLayoutStyleInfoneERKS_(
    const QLayoutStyleInfo *self,
    const QLayoutStyleInfo *other) {
  return self->operator!=(*other);
}

//  void QLayoutStyleInfo::setDefaultSpacing(Qt::Orientation o, qreal
//      spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLayoutStyleInfo17setDefaultSpacingEN2Qt11OrientationEd(
    QLayoutStyleInfo *self,
    Qt::Orientation o,
    qreal spacing) {
  self->setDefaultSpacing(o, spacing);
}

//  qreal QLayoutStyleInfo::defaultSpacing(Qt::Orientation o) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QLayoutStyleInfo14defaultSpacingEN2Qt11OrientationE(
    const QLayoutStyleInfo *self,
    Qt::Orientation o) {
  return self->defaultSpacing(o);
}

//  qreal QLayoutStyleInfo::perItemSpacing(QSizePolicy::ControlType control1,
//      QSizePolicy::ControlType control2, Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QLayoutStyleInfo14perItemSpacingEN11QSizePolicy11ControlTypeES1_N2Qt11OrientationE(
    const QLayoutStyleInfo *self,
    QSizePolicy::ControlType control1,
    QSizePolicy::ControlType control2,
    Qt::Orientation orientation) {
  return self->perItemSpacing(control1, control2, orientation);
}

//  QLayoutStyleInfo::~QLayoutStyleInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLayoutStyleInfoD1Ev(QLayoutStyleInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
