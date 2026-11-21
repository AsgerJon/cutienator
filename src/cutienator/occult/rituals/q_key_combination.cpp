//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qnamespace.h>

//  QKeyCombination::QKeyCombination(Qt::Key key)
extern "C" Q_DECL_EXPORT
QKeyCombination *ritual_ZN15QKeyCombinationC1EN2Qt3KeyE(Qt::Key key) {
  return new QKeyCombination(key);
}

//  QKeyCombination::QKeyCombination(Qt::Modifiers modifiers, Qt::Key key)
extern "C" Q_DECL_EXPORT
QKeyCombination *ritual_ZN15QKeyCombinationC1E6QFlagsIN2Qt8ModifierEENS1_3KeyE(
    int modifiers,
    Qt::Key key) {
  return new QKeyCombination(QFlags<Qt::Modifier>::fromInt(modifiers), key);
}

//  QKeyCombination::QKeyCombination(Qt::KeyboardModifiers modifiers, Qt::Key
//      key)
extern "C" Q_DECL_EXPORT
QKeyCombination *ritual_ZN15QKeyCombinationC1E6QFlagsIN2Qt16KeyboardModifierEENS1_3KeyE(
    int modifiers,
    Qt::Key key) {
  return new QKeyCombination(
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      key);
}

//  Qt::KeyboardModifiers QKeyCombination::keyboardModifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QKeyCombination17keyboardModifiersEv(
    const QKeyCombination *self) {
  return static_cast<int>(self->keyboardModifiers().toInt());
}

//  Qt::Key QKeyCombination::key() const
extern "C" Q_DECL_EXPORT
Qt::Key ritual_ZNK15QKeyCombination3keyEv(const QKeyCombination *self) {
  return self->key();
}

//  QKeyCombination QKeyCombination::fromCombined(int combined)
extern "C" Q_DECL_EXPORT
QKeyCombination *ritual_ZN15QKeyCombination12fromCombinedEi(int combined) {
  return new QKeyCombination(QKeyCombination::fromCombined(combined));
}

//  int QKeyCombination::toCombined() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QKeyCombination10toCombinedEv(const QKeyCombination *self) {
  return self->toCombined();
}

//  int QKeyCombination::operator int() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QKeyCombinationcviEv(const QKeyCombination *self) {
  return self->operator int();
}

//  QKeyCombination::~QKeyCombination()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QKeyCombinationD1Ev(QKeyCombination *self) {
  delete self;
}
