//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemspinbox_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it (Qt
//  builds the part for those two only). Kept as it is when the
//  generator runs again.
//  Qt does not export this class: only its virtual functions are called,
//  through the object.
//  Not written: the constructor, 'tr' and the destructor (Qt declares none),
//  and 'initStyleOption', a private function that is not virtual.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemspinbox_p.h>
#include <QtGui/qfont.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *QQuickStyleItemSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickStyleItemSpinBox10metaObjectEv(
    const QQuickStyleItemSpinBox *self) {
  return self->metaObject();
}

//  QFont QQuickStyleItemSpinBox::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK22QQuickStyleItemSpinBox9styleFontEP10QQuickItem(
    const QQuickStyleItemSpinBox *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemSpinBox::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QQuickStyleItemSpinBox16connectToControlEv(
    const QQuickStyleItemSpinBox *self) {
  self->connectToControl();
}

//  void QQuickStyleItemSpinBox::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QQuickStyleItemSpinBox10paintEventEP8QPainter(
    const QQuickStyleItemSpinBox *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemSpinBox::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN22QQuickStyleItemSpinBox17calculateGeometryEv(
    QQuickStyleItemSpinBox *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // Qt builds it for macOS and Windows
