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
