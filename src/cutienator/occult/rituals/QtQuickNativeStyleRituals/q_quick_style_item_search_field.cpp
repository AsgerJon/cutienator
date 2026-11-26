//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemsearchfield_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it (Qt
//  builds the part for those two only). Kept as it is when the
//  generator runs again.
//  Qt does not export this class: only its virtual functions are called,
//  through the object.
//  Not written: the constructor, 'tr' and the destructor (Qt declares none),
//  and 'initStyleOption', a private function that is not virtual.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if (defined(Q_OS_MACOS) || defined(Q_OS_WIN)) \
    && QT_CONFIG(qml_delegate_model)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemsearchfield_p.h>
#include <QtGui/qfont.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *QQuickStyleItemSearchField::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickStyleItemSearchField10metaObjectEv(
    const QQuickStyleItemSearchField *self) {
  return self->metaObject();
}

//  QFont QQuickStyleItemSearchField::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK26QQuickStyleItemSearchField9styleFontEP10QQuickItem(
    const QQuickStyleItemSearchField *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemSearchField::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QQuickStyleItemSearchField16connectToControlEv(
    const QQuickStyleItemSearchField *self) {
  self->connectToControl();
}

//  void QQuickStyleItemSearchField::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QQuickStyleItemSearchField10paintEventEP8QPainter(
    const QQuickStyleItemSearchField *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemSearchField::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN26QQuickStyleItemSearchField17calculateGeometryEv(
    QQuickStyleItemSearchField *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // Qt builds it for macOS and Windows
