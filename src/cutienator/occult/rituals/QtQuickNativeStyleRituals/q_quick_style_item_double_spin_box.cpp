//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemdoublespinbox_p.h,
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
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemdoublespinbox_p.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItemDoubleSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickStyleItemDoubleSpinBox10metaObjectEv(
    const QQuickStyleItemDoubleSpinBox *self) {
  return self->metaObject();
}

//  QQuickStyleItemDoubleSpinBox::~QQuickStyleItemDoubleSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickStyleItemDoubleSpinBoxD1Ev(
    QQuickStyleItemDoubleSpinBox *self) {
  delete self;
}

//  QFont QQuickStyleItemDoubleSpinBox::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK28QQuickStyleItemDoubleSpinBox9styleFontEP10QQuickItem(
    const QQuickStyleItemDoubleSpinBox *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemDoubleSpinBox::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QQuickStyleItemDoubleSpinBox16connectToControlEv(
    const QQuickStyleItemDoubleSpinBox *self) {
  self->connectToControl();
}

//  void QQuickStyleItemDoubleSpinBox::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QQuickStyleItemDoubleSpinBox10paintEventEP8QPainter(
    const QQuickStyleItemDoubleSpinBox *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemDoubleSpinBox::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN28QQuickStyleItemDoubleSpinBox17calculateGeometryEv(
    QQuickStyleItemDoubleSpinBox *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
