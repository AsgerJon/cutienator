//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitembutton_p.h,
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
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitembutton_p.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItemButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickStyleItemButton10metaObjectEv(
    const QQuickStyleItemButton *self) {
  return self->metaObject();
}

//  QQuickStyleItemButton::~QQuickStyleItemButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickStyleItemButtonD1Ev(
    QQuickStyleItemButton *self) {
  delete self;
}

//  QFont QQuickStyleItemButton::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK21QQuickStyleItemButton9styleFontEP10QQuickItem(
    const QQuickStyleItemButton *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemButton::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickStyleItemButton16connectToControlEv(
    const QQuickStyleItemButton *self) {
  self->connectToControl();
}

//  void QQuickStyleItemButton::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickStyleItemButton10paintEventEP8QPainter(
    const QQuickStyleItemButton *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemButton::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN21QQuickStyleItemButton17calculateGeometryEv(
    QQuickStyleItemButton *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

//  void QQuickStyleItemButton::initStyleOption(QQC2::QStyleOptionButton
//      &styleOption) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickStyleItemButton15initStyleOptionERN4QQC218QStyleOptionButtonE(
    const QQuickStyleItemButton *self,
    QQC2::QStyleOptionButton *styleOption) {
  self->initStyleOption(*styleOption);
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
