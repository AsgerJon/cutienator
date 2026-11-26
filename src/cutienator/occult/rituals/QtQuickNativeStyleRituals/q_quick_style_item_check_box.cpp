//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemcheckbox_p.h,
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
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemcheckbox_p.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItemCheckBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickStyleItemCheckBox10metaObjectEv(
    const QQuickStyleItemCheckBox *self) {
  return self->metaObject();
}

//  QQuickStyleItemCheckBox::~QQuickStyleItemCheckBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStyleItemCheckBoxD1Ev(
    QQuickStyleItemCheckBox *self) {
  delete self;
}

//  QFont QQuickStyleItemCheckBox::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK23QQuickStyleItemCheckBox9styleFontEP10QQuickItem(
    const QQuickStyleItemCheckBox *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemCheckBox::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QQuickStyleItemCheckBox16connectToControlEv(
    const QQuickStyleItemCheckBox *self) {
  self->connectToControl();
}

//  void QQuickStyleItemCheckBox::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QQuickStyleItemCheckBox10paintEventEP8QPainter(
    const QQuickStyleItemCheckBox *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemCheckBox::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN23QQuickStyleItemCheckBox17calculateGeometryEv(
    QQuickStyleItemCheckBox *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

//  void QQuickStyleItemCheckBox::initStyleOption(QQC2::QStyleOptionButton
//      &styleOption) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QQuickStyleItemCheckBox15initStyleOptionERN4QQC218QStyleOptionButtonE(
    const QQuickStyleItemCheckBox *self,
    QQC2::QStyleOptionButton *styleOption) {
  self->initStyleOption(*styleOption);
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
