//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemradiobutton_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator
//  runs again.
//  Qt does not export this class, and builds it for macOS and Windows
//  only (quickcontrols2-macos, quickcontrols2-windows). Qt's library
//  offers nothing of it by name: only its virtual functions are
//  called, through the object.
//  Not written: the constructor, 'tr', 'qt_metacast', 'qt_metacall'
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemradiobutton_p.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItemRadioButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickStyleItemRadioButton10metaObjectEv(
    const QQuickStyleItemRadioButton *self) {
  return self->metaObject();
}

//  QQuickStyleItemRadioButton::~QQuickStyleItemRadioButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickStyleItemRadioButtonD1Ev(
    QQuickStyleItemRadioButton *self) {
  delete self;
}

//  QFont QQuickStyleItemRadioButton::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK26QQuickStyleItemRadioButton9styleFontEP10QQuickItem(
    const QQuickStyleItemRadioButton *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemRadioButton::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QQuickStyleItemRadioButton16connectToControlEv(
    const QQuickStyleItemRadioButton *self) {
  self->connectToControl();
}

//  void QQuickStyleItemRadioButton::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QQuickStyleItemRadioButton10paintEventEP8QPainter(
    const QQuickStyleItemRadioButton *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemRadioButton::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN26QQuickStyleItemRadioButton17calculateGeometryEv(
    QQuickStyleItemRadioButton *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

//  void QQuickStyleItemRadioButton::initStyleOption(QQC2::QStyleOptionButton
//      &styleOption) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QQuickStyleItemRadioButton15initStyleOptionERN4QQC218QStyleOptionButtonE(
    const QQuickStyleItemRadioButton *self,
    QQC2::QStyleOptionButton *styleOption) {
  self->initStyleOption(*styleOption);
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
