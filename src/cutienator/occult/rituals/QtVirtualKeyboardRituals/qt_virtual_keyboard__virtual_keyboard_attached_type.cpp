//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/virtualkeyboardattachedtype_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/virtualkeyboardattachedtype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject
//      *QtVirtualKeyboard::VirtualKeyboardAttachedType::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard27VirtualKeyboardAttachedType10metaObjectEv(
    const QtVirtualKeyboard::VirtualKeyboardAttachedType *self) {
  return self->metaObject();
}

//  QString QtVirtualKeyboard::VirtualKeyboardAttachedType::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedType2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QtVirtualKeyboard::VirtualKeyboardAttachedType::tr(
          s,
          c,
          n));
}

//  void
//      QtVirtualKeyboard::VirtualKeyboardAttachedType::qt_qmlMarker_anonymou
//      s()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedType22qt_qmlMarker_anonymousEv(
    QtVirtualKeyboard::VirtualKeyboardAttachedType *self) {
  self->qt_qmlMarker_anonymous();
}

//  QStringList
//      QtVirtualKeyboard::VirtualKeyboardAttachedType::extraDictionaries()
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QtVirtualKeyboard27VirtualKeyboardAttachedType17extraDictionariesEv(
    const QtVirtualKeyboard::VirtualKeyboardAttachedType *self) {
  return new QList<QString>(self->extraDictionaries());
}

//  void QtVirtualKeyboard::VirtualKeyboardAttachedType::setExtraDictionaries
//      (const QStringList &dictionaries)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedType20setExtraDictionariesERK5QListI7QStringE(
    QtVirtualKeyboard::VirtualKeyboardAttachedType *self,
    const QList<QString> *dictionaries) {
  self->setExtraDictionaries(*dictionaries);
}
