//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemdial_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator
//  runs again.
//  Qt does not export this class, and builds it for macOS and Windows
//  only (quickcontrols2-macos, quickcontrols2-windows). Qt's library
//  offers nothing of it by name: only its virtual functions are
//  called, through the object.
//  Not written: the constructor, 'tr', 'qt_metacast', 'qt_metacall'
//  and the private 'initStyleOption', which is no virtual function.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemdial_p.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItemDial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickStyleItemDial10metaObjectEv(
    const QQuickStyleItemDial *self) {
  return self->metaObject();
}

//  QQuickStyleItemDial::~QQuickStyleItemDial()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickStyleItemDialD1Ev(
    QQuickStyleItemDial *self) {
  delete self;
}

//  QFont QQuickStyleItemDial::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK19QQuickStyleItemDial9styleFontEP10QQuickItem(
    const QQuickStyleItemDial *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemDial::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQuickStyleItemDial16connectToControlEv(
    const QQuickStyleItemDial *self) {
  self->connectToControl();
}

//  void QQuickStyleItemDial::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQuickStyleItemDial10paintEventEP8QPainter(
    const QQuickStyleItemDial *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemDial::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN19QQuickStyleItemDial17calculateGeometryEv(
    QQuickStyleItemDial *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
