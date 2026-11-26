//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemscrollbar_p.h,
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
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemscrollbar_p.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItemScrollBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickStyleItemScrollBar10metaObjectEv(
    const QQuickStyleItemScrollBar *self) {
  return self->metaObject();
}

//  QQuickStyleItemScrollBar::~QQuickStyleItemScrollBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickStyleItemScrollBarD1Ev(
    QQuickStyleItemScrollBar *self) {
  delete self;
}

//  QFont QQuickStyleItemScrollBar::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK24QQuickStyleItemScrollBar9styleFontEP10QQuickItem(
    const QQuickStyleItemScrollBar *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemScrollBar::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QQuickStyleItemScrollBar16connectToControlEv(
    const QQuickStyleItemScrollBar *self) {
  self->connectToControl();
}

//  void QQuickStyleItemScrollBar::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QQuickStyleItemScrollBar10paintEventEP8QPainter(
    const QQuickStyleItemScrollBar *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemScrollBar::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN24QQuickStyleItemScrollBar17calculateGeometryEv(
    QQuickStyleItemScrollBar *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
