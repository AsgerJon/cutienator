//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquicktoolseparator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktoolseparator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickToolSeparator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickToolSeparator : QQuickToolSeparator {
  using QQuickToolSeparator::defaultFont;
  using QQuickToolSeparator::accessibleRole;
};

//  const QMetaObject *QQuickToolSeparator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickToolSeparator10metaObjectEv(
    const QQuickToolSeparator *self) {
  return self->metaObject();
}

//  QString QQuickToolSeparator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickToolSeparator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickToolSeparator::tr(s, c, n));
}

//  QQuickToolSeparator::QQuickToolSeparator(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickToolSeparator *ritual_ZN19QQuickToolSeparatorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickToolSeparator(parent);
}

//  Qt::Orientation QQuickToolSeparator::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK19QQuickToolSeparator11orientationEv(
    const QQuickToolSeparator *self) {
  return self->orientation();
}

//  void QQuickToolSeparator::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickToolSeparator14setOrientationEN2Qt11OrientationE(
    QQuickToolSeparator *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  bool QQuickToolSeparator::isHorizontal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickToolSeparator12isHorizontalEv(
    const QQuickToolSeparator *self) {
  return self->isHorizontal();
}

//  bool QQuickToolSeparator::isVertical() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickToolSeparator10isVerticalEv(
    const QQuickToolSeparator *self) {
  return self->isVertical();
}

//  QFont QQuickToolSeparator::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK19QQuickToolSeparator11defaultFontEv(
    const QQuickToolSeparator *self) {
  return new QFont(self->defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickToolSeparator::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK19QQuickToolSeparator14accessibleRoleEv(
    const QQuickToolSeparator *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QFont QQuickToolSeparator::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK19QQuickToolSeparator11defaultFontEv(
    const QQuickToolSeparator *self) {
  return new QFont(
      static_cast<const OwnQQuickToolSeparator *>(self)->OwnQQuickToolSeparator::defaultFont());
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickToolSeparator::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK19QQuickToolSeparator14accessibleRoleEv(
    const QQuickToolSeparator *self) {
  return static_cast<const OwnQQuickToolSeparator *>(self)->OwnQQuickToolSeparator::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
