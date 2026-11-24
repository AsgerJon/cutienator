//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickcheckdelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcheckdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickCheckDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickCheckDelegate : QQuickCheckDelegate {
  using QQuickCheckDelegate::defaultFont;
  using QQuickCheckDelegate::nextCheckState;
  using QQuickCheckDelegate::accessibleRole;
};

//  const QMetaObject *QQuickCheckDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickCheckDelegate10metaObjectEv(
    const QQuickCheckDelegate *self) {
  return self->metaObject();
}

//  QString QQuickCheckDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickCheckDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickCheckDelegate::tr(s, c, n));
}

//  QQuickCheckDelegate::QQuickCheckDelegate(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickCheckDelegate *ritual_ZN19QQuickCheckDelegateC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickCheckDelegate(parent);
}

//  bool QQuickCheckDelegate::isTristate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickCheckDelegate10isTristateEv(
    const QQuickCheckDelegate *self) {
  return self->isTristate();
}

//  void QQuickCheckDelegate::setTristate(bool tristate)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCheckDelegate11setTristateEb(
    QQuickCheckDelegate *self,
    bool tristate) {
  self->setTristate(tristate);
}

//  Qt::CheckState QQuickCheckDelegate::checkState() const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK19QQuickCheckDelegate10checkStateEv(
    const QQuickCheckDelegate *self) {
  return self->checkState();
}

//  void QQuickCheckDelegate::setCheckState(Qt::CheckState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCheckDelegate13setCheckStateEN2Qt10CheckStateE(
    QQuickCheckDelegate *self,
    Qt::CheckState state) {
  self->setCheckState(state);
}

//  QFont QQuickCheckDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK19QQuickCheckDelegate11defaultFontEv(
    const QQuickCheckDelegate *self) {
  return new QFont(self->defaultFont());
}

//  void QQuickCheckDelegate::buttonChange(ButtonChange change)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCheckDelegate12buttonChangeEN20QQuickAbstractButton12ButtonChangeE(
    QQuickCheckDelegate *self,
    QQuickAbstractButton::ButtonChange change) {
  self->buttonChange(change);
}

//  void QQuickCheckDelegate::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCheckDelegate14nextCheckStateEv(
    QQuickCheckDelegate *self) {
  self->nextCheckState();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickCheckDelegate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK19QQuickCheckDelegate14accessibleRoleEv(
    const QQuickCheckDelegate *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QFont QQuickCheckDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK19QQuickCheckDelegate11defaultFontEv(
    const QQuickCheckDelegate *self) {
  return new QFont(
      static_cast<const OwnQQuickCheckDelegate *>(self)->OwnQQuickCheckDelegate::defaultFont());
}

//  void QQuickCheckDelegate::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickCheckDelegate14nextCheckStateEv(
    QQuickCheckDelegate *self) {
  static_cast<OwnQQuickCheckDelegate *>(self)->OwnQQuickCheckDelegate::nextCheckState();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickCheckDelegate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK19QQuickCheckDelegate14accessibleRoleEv(
    const QQuickCheckDelegate *self) {
  return static_cast<const OwnQQuickCheckDelegate *>(self)->OwnQQuickCheckDelegate::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
