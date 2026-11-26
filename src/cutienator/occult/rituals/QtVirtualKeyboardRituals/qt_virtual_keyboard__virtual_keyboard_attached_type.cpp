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

//  void *QtVirtualKeyboard::VirtualKeyboardAttachedType::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedType11qt_metacastEPKc(
    QtVirtualKeyboard::VirtualKeyboardAttachedType *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtVirtualKeyboard::VirtualKeyboardAttachedType::qt_metacall(QMetaObje
//      ct::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedType11qt_metacallEN11QMetaObject4CallEiPPv(
    QtVirtualKeyboard::VirtualKeyboardAttachedType *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QtVirtualKeyboard::VirtualKeyboardAttachedType::VirtualKeyboardAttachedTy
//      pe(QObject *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::VirtualKeyboardAttachedType *ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedTypeC1EP7QObject(
    QObject *parent) {
  return new QtVirtualKeyboard::VirtualKeyboardAttachedType(parent);
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

//  void QtVirtualKeyboard::VirtualKeyboardAttachedType::extraDictionariesCha
//      nged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard27VirtualKeyboardAttachedType24extraDictionariesChangedEv(
    QtVirtualKeyboard::VirtualKeyboardAttachedType *self) {
  self->extraDictionariesChanged();
}
