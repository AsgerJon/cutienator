//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcheckbox_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcheckbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtGui/qfont.h>

//  Only a class built on QQuickCheckBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickCheckBox : QQuickCheckBox {
  using QQuickCheckBox::defaultFont;
  using QQuickCheckBox::nextCheckState;
};

//  const QMetaObject *QQuickCheckBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickCheckBox10metaObjectEv(
    const QQuickCheckBox *self) {
  return self->metaObject();
}

//  QString QQuickCheckBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickCheckBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickCheckBox::tr(s, c, n));
}

//  QQuickCheckBox::QQuickCheckBox(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickCheckBox *ritual_ZN14QQuickCheckBoxC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickCheckBox(parent);
}

//  bool QQuickCheckBox::isTristate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickCheckBox10isTristateEv(const QQuickCheckBox *self) {
  return self->isTristate();
}

//  void QQuickCheckBox::setTristate(bool tristate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickCheckBox11setTristateEb(
    QQuickCheckBox *self,
    bool tristate) {
  self->setTristate(tristate);
}

//  Qt::CheckState QQuickCheckBox::checkState() const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK14QQuickCheckBox10checkStateEv(
    const QQuickCheckBox *self) {
  return self->checkState();
}

//  void QQuickCheckBox::setCheckState(Qt::CheckState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickCheckBox13setCheckStateEN2Qt10CheckStateE(
    QQuickCheckBox *self,
    Qt::CheckState state) {
  self->setCheckState(state);
}

//  QJSValue QQuickCheckBox::getNextCheckState() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK14QQuickCheckBox17getNextCheckStateEv(
    const QQuickCheckBox *self) {
  return new QJSValue(self->getNextCheckState());
}

//  void QQuickCheckBox::setNextCheckState(const QJSValue &callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickCheckBox17setNextCheckStateERK8QJSValue(
    QQuickCheckBox *self,
    const QJSValue *callback) {
  self->setNextCheckState(*callback);
}

//  QFont QQuickCheckBox::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQuickCheckBox11defaultFontEv(
    const QQuickCheckBox *self) {
  return new QFont(self->defaultFont());
}

//  void QQuickCheckBox::buttonChange(ButtonChange change)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickCheckBox12buttonChangeEN20QQuickAbstractButton12ButtonChangeE(
    QQuickCheckBox *self,
    QQuickAbstractButton::ButtonChange change) {
  self->buttonChange(change);
}

//  void QQuickCheckBox::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickCheckBox14nextCheckStateEv(QQuickCheckBox *self) {
  self->nextCheckState();
}

//  QFont QQuickCheckBox::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK14QQuickCheckBox11defaultFontEv(
    const QQuickCheckBox *self) {
  return new QFont(
      static_cast<const OwnQQuickCheckBox *>(self)->OwnQQuickCheckBox::defaultFont());
}

//  void QQuickCheckBox::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickCheckBox14nextCheckStateEv(QQuickCheckBox *self) {
  static_cast<OwnQQuickCheckBox *>(self)->OwnQQuickCheckBox::nextCheckState();
}
