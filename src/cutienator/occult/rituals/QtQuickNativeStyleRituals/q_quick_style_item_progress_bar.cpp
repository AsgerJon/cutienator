//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemprogressbar_p.h,
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
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemprogressbar_p.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItemProgressBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickStyleItemProgressBar10metaObjectEv(
    const QQuickStyleItemProgressBar *self) {
  return self->metaObject();
}

//  QQuickStyleItemProgressBar::~QQuickStyleItemProgressBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickStyleItemProgressBarD1Ev(
    QQuickStyleItemProgressBar *self) {
  delete self;
}

//  QFont QQuickStyleItemProgressBar::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK26QQuickStyleItemProgressBar9styleFontEP10QQuickItem(
    const QQuickStyleItemProgressBar *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemProgressBar::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QQuickStyleItemProgressBar16connectToControlEv(
    const QQuickStyleItemProgressBar *self) {
  self->connectToControl();
}

//  void QQuickStyleItemProgressBar::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QQuickStyleItemProgressBar10paintEventEP8QPainter(
    const QQuickStyleItemProgressBar *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemProgressBar::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN26QQuickStyleItemProgressBar17calculateGeometryEv(
    QQuickStyleItemProgressBar *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
