//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemcombobox_p.h,
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
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemcombobox_p.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItemComboBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickStyleItemComboBox10metaObjectEv(
    const QQuickStyleItemComboBox *self) {
  return self->metaObject();
}

//  QQuickStyleItemComboBox::~QQuickStyleItemComboBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStyleItemComboBoxD1Ev(
    QQuickStyleItemComboBox *self) {
  delete self;
}

//  QFont QQuickStyleItemComboBox::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK23QQuickStyleItemComboBox9styleFontEP10QQuickItem(
    const QQuickStyleItemComboBox *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemComboBox::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QQuickStyleItemComboBox16connectToControlEv(
    const QQuickStyleItemComboBox *self) {
  self->connectToControl();
}

//  void QQuickStyleItemComboBox::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QQuickStyleItemComboBox10paintEventEP8QPainter(
    const QQuickStyleItemComboBox *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemComboBox::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN23QQuickStyleItemComboBox17calculateGeometryEv(
    QQuickStyleItemComboBox *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
