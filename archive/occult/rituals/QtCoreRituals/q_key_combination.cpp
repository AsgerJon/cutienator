//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qnamespace.h>
#include <QtCore/qlist.h>

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

//  bool operator==(const QKeyCombination &lhs, const QKeyCombination &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK15QKeyCombinationS1_(
    const QKeyCombination *lhs,
    const QKeyCombination *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QKeyCombination &lhs, const QKeyCombination &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK15QKeyCombinationS1_(
    const QKeyCombination *lhs,
    const QKeyCombination *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QKeyCombination::~QKeyCombination()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QKeyCombinationD1Ev(QKeyCombination *self) {
  delete self;
}

//  QList<QKeyCombination>::QList()
extern "C" Q_DECL_EXPORT
QList<QKeyCombination> *ritual_list_make_QKeyCombination() {
  return new QList<QKeyCombination>();
}

//  void QList<QKeyCombination>::append(const QKeyCombination &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QKeyCombination(
    QList<QKeyCombination> *self,
    const QKeyCombination *element) {
  self->append(*element);
}

//  qsizetype QList<QKeyCombination>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QKeyCombination(
    const QList<QKeyCombination> *self) {
  return self->size();
}

//  const QKeyCombination &QList<QKeyCombination>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QKeyCombination *ritual_list_at_QKeyCombination(
    const QList<QKeyCombination> *self,
    long long index) {
  return new QKeyCombination(self->at(index));
}

//  QList<QKeyCombination>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QKeyCombination(QList<QKeyCombination> *self) {
  delete self;
}
