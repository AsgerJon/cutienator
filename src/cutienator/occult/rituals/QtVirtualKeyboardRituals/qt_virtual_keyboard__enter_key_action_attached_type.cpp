//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/enterkeyactionattachedtype_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/enterkeyactionattachedtype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject
//      *QtVirtualKeyboard::EnterKeyActionAttachedType::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard26EnterKeyActionAttachedType10metaObjectEv(
    const QtVirtualKeyboard::EnterKeyActionAttachedType *self) {
  return self->metaObject();
}

//  void *QtVirtualKeyboard::EnterKeyActionAttachedType::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType11qt_metacastEPKc(
    QtVirtualKeyboard::EnterKeyActionAttachedType *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtVirtualKeyboard::EnterKeyActionAttachedType::qt_metacall(QMetaObjec
//      t::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType11qt_metacallEN11QMetaObject4CallEiPPv(
    QtVirtualKeyboard::EnterKeyActionAttachedType *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtVirtualKeyboard::EnterKeyActionAttachedType::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QtVirtualKeyboard::EnterKeyActionAttachedType::tr(
          s,
          c,
          n));
}

//  void
//      QtVirtualKeyboard::EnterKeyActionAttachedType::qt_qmlMarker_anonymous
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType22qt_qmlMarker_anonymousEv(
    QtVirtualKeyboard::EnterKeyActionAttachedType *self) {
  self->qt_qmlMarker_anonymous();
}

//  QtVirtualKeyboard::EnterKeyActionAttachedType::EnterKeyActionAttachedType
//      (QObject *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::EnterKeyActionAttachedType *ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedTypeC1EP7QObject(
    QObject *parent) {
  return new QtVirtualKeyboard::EnterKeyActionAttachedType(parent);
}

//  int QtVirtualKeyboard::EnterKeyActionAttachedType::actionId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtVirtualKeyboard26EnterKeyActionAttachedType8actionIdEv(
    const QtVirtualKeyboard::EnterKeyActionAttachedType *self) {
  return self->actionId();
}

//  void QtVirtualKeyboard::EnterKeyActionAttachedType::setActionId(int
//      actionId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType11setActionIdEi(
    QtVirtualKeyboard::EnterKeyActionAttachedType *self,
    int actionId) {
  self->setActionId(actionId);
}

//  QString QtVirtualKeyboard::EnterKeyActionAttachedType::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QtVirtualKeyboard26EnterKeyActionAttachedType5labelEv(
    const QtVirtualKeyboard::EnterKeyActionAttachedType *self) {
  return new QString(self->label());
}

//  void QtVirtualKeyboard::EnterKeyActionAttachedType::setLabel(const
//      QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType8setLabelERK7QString(
    QtVirtualKeyboard::EnterKeyActionAttachedType *self,
    const QString *label) {
  self->setLabel(*label);
}

//  bool QtVirtualKeyboard::EnterKeyActionAttachedType::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard26EnterKeyActionAttachedType7enabledEv(
    const QtVirtualKeyboard::EnterKeyActionAttachedType *self) {
  return self->enabled();
}

//  void QtVirtualKeyboard::EnterKeyActionAttachedType::setEnabled(bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType10setEnabledEb(
    QtVirtualKeyboard::EnterKeyActionAttachedType *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QtVirtualKeyboard::EnterKeyActionAttachedType::actionIdChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType15actionIdChangedEv(
    QtVirtualKeyboard::EnterKeyActionAttachedType *self) {
  self->actionIdChanged();
}

//  void QtVirtualKeyboard::EnterKeyActionAttachedType::labelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType12labelChangedEv(
    QtVirtualKeyboard::EnterKeyActionAttachedType *self) {
  self->labelChanged();
}

//  void QtVirtualKeyboard::EnterKeyActionAttachedType::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard26EnterKeyActionAttachedType14enabledChangedEv(
    QtVirtualKeyboard::EnterKeyActionAttachedType *self) {
  self->enabledChanged();
}
