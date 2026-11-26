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

//  void *QQuickCheckDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickCheckDelegate11qt_metacastEPKc(
    QQuickCheckDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickCheckDelegate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickCheckDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickCheckDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QQuickCheckDelegate::tristateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCheckDelegate15tristateChangedEv(
    QQuickCheckDelegate *self) {
  self->tristateChanged();
}

//  void QQuickCheckDelegate::checkStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCheckDelegate17checkStateChangedEv(
    QQuickCheckDelegate *self) {
  self->checkStateChanged();
}

//  void QQuickCheckDelegate::nextCheckStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCheckDelegate21nextCheckStateChangedEv(
    QQuickCheckDelegate *self) {
  self->nextCheckStateChanged();
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

//  QQuickCheckDelegatePrivate *QQuickCheckDelegate::d_func()
extern "C" Q_DECL_EXPORT
QQuickCheckDelegatePrivate *ritual_ZN19QQuickCheckDelegate6d_funcEv(
    QQuickCheckDelegate *self) {
  return self->d_func();
}

//  const QQuickCheckDelegatePrivate *QQuickCheckDelegate::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickCheckDelegatePrivate *ritual_ZNK19QQuickCheckDelegate6d_funcEv(
    const QQuickCheckDelegate *self) {
  return self->d_func();
}

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
